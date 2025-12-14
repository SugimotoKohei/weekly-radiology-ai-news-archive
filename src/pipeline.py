from __future__ import annotations

import os
from datetime import datetime
from pathlib import Path
from typing import List, cast

from dateutil import tz

from src.buttondown_client import ButtondownClient, EmailStatus
from src.newsletter_generator import (
    DEFAULT_TEMPLATE_PATH,
    NewsletterGenerator,
    NewsletterTemplate,
)
from src.pubmed_client import PubMedClient

DEFAULT_QUERY = (
    "(deep learning[Title/Abstract] OR artificial intelligence[Title/Abstract])"
    " AND (tomography[MeSH Terms] OR CT[Title/Abstract] OR MRI[Title/Abstract]"
    " OR \"magnetic resonance\"[Title/Abstract])"
    " AND (segmentation[Title/Abstract] OR detection[Title/Abstract] OR classification[Title/Abstract])"
)


def _ensure_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Environment variable {name} is required")
    return value


def _is_github_actions() -> bool:
    return os.getenv("GITHUB_ACTIONS", "").lower() == "true"


def _actions_send_allowed() -> bool:
    return os.getenv("BUTTONDOWN_ALLOW_ACTIONS_SEND", "").lower() in {"1", "true", "yes"}


def _issues_dir() -> Path:
    path = Path(__file__).resolve().parents[1] / "issues"
    path.mkdir(exist_ok=True)
    return path


def _next_issue_number(issues_path: Path) -> int:
    files: List[Path] = sorted(issues_path.glob("*.md"))
    return len(files) + 1


def _save_issue_markdown(date_str: str, issue_no: int, content: str) -> Path:
    issues_path = _issues_dir()
    filename = f"{date_str}_ct-mri-ai-weekly-{issue_no:03d}.md"
    target = issues_path / filename
    target.write_text(content, encoding="utf-8")
    return target


def _inject_pubmed_links(markdown: str) -> str:
    """Ensure each paper heading includes a PubMed link.

    Idempotent: if a heading already contains a markdown link, it is left unchanged.
    """
    import re

    def repl(match: re.Match[str]) -> str:
        line = match.group(0)
        if "](" in line:
            return line
        pmid = match.group(1)
        url = f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
        return f"{line} ([PubMed]({url}))"

    # Match headings like: ### ... (PMID: 12345678)
    pattern = re.compile(r"^### .*\(PMID:\s*(\d+)\)\s*$", re.MULTILINE)
    return pattern.sub(repl, markdown)


def _enforce_editorial_one_paragraph(markdown: str, *, max_chars: int = 480) -> str:
    """Coerce the editorial section to a single paragraph.

    If multiple paragraphs are present, keep only the first one.
    """
    import re

    header_re = re.compile(r"^##\s*総括・編集後記\s*$", re.MULTILINE)
    m = header_re.search(markdown)
    if not m:
        return markdown

    start = m.end()
    rest = markdown[start:]
    next_header = re.search(r"^\s*##\s+", rest, flags=re.MULTILINE)
    end = start + (next_header.start() if next_header else len(rest))

    body = markdown[start:end]
    lines = [ln.rstrip() for ln in body.splitlines()]

    # Split into paragraphs by blank lines.
    paragraphs: list[str] = []
    buf: list[str] = []
    for ln in lines:
        if ln.strip() == "":
            if buf:
                paragraphs.append(" ".join(s.strip() for s in buf if s.strip()))
                buf = []
            continue
        buf.append(ln)
    if buf:
        paragraphs.append(" ".join(s.strip() for s in buf if s.strip()))

    first = (paragraphs[0] if paragraphs else "").strip()
    if not first:
        return markdown

    if len(first) > max_chars:
        first = first[: max_chars - 1].rstrip() + "…"

    new_body = "\n\n" + first + "\n"
    return markdown[:start] + new_body + markdown[end:]


def _postprocess_newsletter(markdown: str) -> str:
    markdown = _inject_pubmed_links(markdown)
    markdown = _enforce_editorial_one_paragraph(markdown)
    return markdown


def run_dry_run(*, fixture_path: Path) -> Path:
    """Dry-run that avoids network calls and creates a debug markdown in issues/."""

    class _StubResponse:
        def __init__(self, *, content: bytes):
            self.content = content
            self.status_code = 200

        def raise_for_status(self) -> None:
            return None

    class _StubSession:
        def __init__(self, xml_bytes: bytes):
            self._xml_bytes = xml_bytes

        def get(self, url, params=None, timeout=None):  # noqa: ANN001
            return _StubResponse(content=self._xml_bytes)

    if not fixture_path.exists():
        raise FileNotFoundError(f"Fixture not found: {fixture_path}")

    xml_bytes = fixture_path.read_bytes()
    client = PubMedClient(session=_StubSession(xml_bytes))
    papers = client.fetch_details(["dry-run"])
    if not papers:
        raise RuntimeError("Dry-run fixture produced 0 papers")

    jst = tz.gettz("Asia/Tokyo")
    now = datetime.now(tz=jst)
    today_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%H%M%S")

    template = NewsletterTemplate.from_file(DEFAULT_TEMPLATE_PATH)
    generator = NewsletterGenerator(api_key="dry-run", template=template)
    content = generator._build_fallback_content(  # noqa: SLF001
        papers,
        today_str,
        error=RuntimeError("dry-run (no external API calls)"),
    )

    issues_path = _issues_dir()
    filename = f"_dry_run_{today_str}_{time_str}.md"
    target = issues_path / filename
    target.write_text(content, encoding="utf-8")
    print(f"[INFO] Dry-run wrote {target}")
    return target


def run_pipeline() -> None:
    jst = tz.gettz("Asia/Tokyo")
    today = datetime.now(tz=jst)
    today_str = today.strftime("%Y-%m-%d")
    query = os.getenv("PUBMED_QUERY", DEFAULT_QUERY)
    days = int(os.getenv("PUBMED_RELDAYS", "7"))
    fallback_days = int(os.getenv("PUBMED_FALLBACK_RELDAYS", "30"))
    if fallback_days < days:
        fallback_days = days
    retmax = int(os.getenv("PUBMED_RETMAX", "40"))

    pubmed_client = PubMedClient(api_key=os.getenv("PUBMED_API_KEY"))
    papers = pubmed_client.get_recent_papers(query, days=days, retmax=retmax)
    if not papers and fallback_days > days:
        print(
            f"[INFO] No PubMed articles found in last {days} days. "
            f"Retrying with {fallback_days} days."
        )
        papers = pubmed_client.get_recent_papers(
            query,
            days=fallback_days,
            retmax=retmax,
        )
    if not papers:
        print("[INFO] No new PubMed articles found even after fallback. Exiting.")
        return

    template_path = Path(os.getenv("NEWSLETTER_TEMPLATE_PATH", str(DEFAULT_TEMPLATE_PATH)))
    template = NewsletterTemplate.from_file(template_path)
    generator = NewsletterGenerator(api_key=_ensure_env("GEMINI_API_KEY"), template=template)
    newsletter_md = generator.generate(papers, today_str)
    newsletter_md = _postprocess_newsletter(newsletter_md)

    issues_path = _issues_dir()
    issue_no = _next_issue_number(issues_path)
    md_path = _save_issue_markdown(today_str, issue_no, newsletter_md)
    print(f"[INFO] Saved newsletter markdown to {md_path}")

    valid_statuses = {"draft", "about_to_send", "scheduled", "imported", "transactional", "sent"}
    buttondown_status = os.getenv("BUTTONDOWN_STATUS", "draft")
    if buttondown_status not in valid_statuses:
        raise RuntimeError(
            "BUTTONDOWN_STATUS must be one of " + ", ".join(sorted(valid_statuses))
        )
    if _is_github_actions() and buttondown_status != "draft" and not _actions_send_allowed():
        raise RuntimeError(
            "Refusing to send non-draft email in GitHub Actions. "
            "Set BUTTONDOWN_STATUS=draft, or explicitly opt-in with BUTTONDOWN_ALLOW_ACTIONS_SEND=true."
        )
    buttondown = ButtondownClient(api_key=_ensure_env("BUTTONDOWN_API_KEY"))
    subject = f"CT/MRI×AI Weekly #{issue_no} - {today_str}"
    email_status = cast(EmailStatus, buttondown_status)
    try:
        resp = buttondown.send_email(
            subject=subject,
            body=newsletter_md,
            status=email_status,
        )
        resp_id = resp.get("id") if isinstance(resp, dict) else None
        if resp_id is not None:
            print(f"[INFO] Buttondown email request submitted (id={resp_id}, status={email_status})")
        else:
            print(f"[INFO] Buttondown email request submitted (status={email_status})")
    except RuntimeError as err:
        print(f"[ERROR] Buttondown send failed: {err}")
        raise


if __name__ == "__main__":
    run_pipeline()


__all__ = ["run_pipeline", "run_dry_run"]
