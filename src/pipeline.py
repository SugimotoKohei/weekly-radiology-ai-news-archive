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
from src.summary_image_generator import (
    SummaryImageSpec,
    build_github_raw_url,
    build_summary_image_prompt,
    default_summary_image_path,
    extract_featured_top_pick,
    extract_top_picks_titles,
    generate_summary_image_bytes,
    maybe_prepend_summary_image,
)

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


def _normalize_pmid_links(markdown: str) -> str:
    """Normalize PubMed links so the PMID digits are clickable.

    Target format:
      ### ... (PMID: [12345678](https://pubmed.ncbi.nlm.nih.gov/12345678/))

    Handles older formats like:
      ### ... (PMID: 12345678) ([PubMed](https://pubmed.ncbi.nlm.nih.gov/12345678/))
      ### ... (PMID: 12345678)
    """
    import re

    def _url(pmid: str) -> str:
        return f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"

    # Case 1: already in desired form -> keep.
    # Case 2: convert "PMID: 123) ([PubMed](...))" -> "PMID: [123](...)"
    pattern_with_pubmed = re.compile(
        r"^(### .*?)\(\s*PMID:\s*(\d+)\s*\)\s*\(\s*\[PubMed\]\(([^)]+)\)\s*\)\s*$",
        re.MULTILINE,
    )

    def repl_with_pubmed(match: re.Match[str]) -> str:
        prefix = match.group(1).rstrip()
        if not prefix.endswith(" "):
            prefix += " "
        pmid = match.group(2)
        url = match.group(3).strip()
        return f"{prefix}(PMID: [{pmid}]({url}))"

    markdown = pattern_with_pubmed.sub(repl_with_pubmed, markdown)

    # Case 3: add link to bare PMID digits
    pattern_bare = re.compile(
        r"^(### .*?)\(\s*PMID:\s*(\d+)\s*\)\s*$",
        re.MULTILINE,
    )

    def repl_bare(match: re.Match[str]) -> str:
        prefix = match.group(1).rstrip()
        if not prefix.endswith(" "):
            prefix += " "
        pmid = match.group(2)
        return f"{prefix}(PMID: [{pmid}]({_url(pmid)}))"

    markdown = pattern_bare.sub(repl_bare, markdown)
    return markdown


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


def _remove_so_what(markdown: str) -> str:
    """Remove 'So what' lines if the model outputs them."""
    import re

    lines = markdown.splitlines()
    kept: list[str] = []
    for line in lines:
        if re.search(r"\bso what\b", line, flags=re.IGNORECASE):
            continue
        kept.append(line)
    return "\n".join(kept)


def _normalize_limitation_label(markdown: str) -> str:
    """Remove English parenthetical from the limitation label, if present."""
    import re

    patterns = [
        r"限界\s*（\s*limitation\s*）\s*[:：]",
        r"限界\s*\(\s*limitation\s*\)\s*[:：]",
    ]
    out = markdown
    for pat in patterns:
        out = re.sub(pat, "限界:", out, flags=re.IGNORECASE)
    # Normalize spacing after the label.
    out = re.sub(r"限界:\s*", "限界: ", out)
    return out


def _normalize_journal_label(markdown: str) -> str:
    """Remove year suffix from the journal label line, if present.

    Examples:
      **雑誌名**: Journal Name (2025)  -> **雑誌名**: Journal Name
      **雑誌名**: Journal Name, 2025  -> **雑誌名**: Journal Name
    """
    import re

    lines = markdown.splitlines()
    out_lines: list[str] = []
    pattern = re.compile(r"^(\s*[-*]\s+\*\*雑誌名\*\*:\s*)(.+?)\s*$")
    for line in lines:
        m = pattern.match(line)
        if not m:
            out_lines.append(line)
            continue
        prefix = m.group(1)
        value = m.group(2).strip()
        value = re.sub(r"\s*\(\s*\d{4}\s*\)\s*$", "", value)
        value = re.sub(r"\s*,\s*\d{4}\s*$", "", value)
        out_lines.append(f"{prefix}{value}")
    return "\n".join(out_lines)


def _postprocess_newsletter(markdown: str) -> str:
    markdown = _normalize_pmid_links(markdown)
    markdown = _remove_so_what(markdown)
    markdown = _normalize_limitation_label(markdown)
    markdown = _normalize_journal_label(markdown)
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

    # Optional: generate a summary image using a Gemini image model (aka "nano banana").
    if os.getenv("SUMMARY_IMAGE_ENABLED", "").lower() in {"1", "true", "yes"}:
        import re

        featured = extract_featured_top_pick(newsletter_md) or {}
        journal, year = ("", "")
        if featured.get("journal"):
            # Try to split "<journal>, 2025" into parts.
            m = re.match(r"^(.*?)(?:,\s*(\d{4}))\s*$", str(featured.get("journal")))
            if m:
                journal, year = m.group(1).strip(), m.group(2).strip()
            else:
                journal = str(featured.get("journal"))

        setting = {
            "Study design": "Not specified",
            "Population": str(featured.get("data") or "Not specified"),
            "Exclusion criteria": "Not specified",
            "Data source / Setting": str(featured.get("affiliations") or "Not specified"),
            "Primary outcome": str(featured.get("task") or "Not specified"),
            "Key secondary outcomes": "Not specified",
            "Statistical methods": "Not specified",
        }

        results_text = str(featured.get("results") or "")
        key_results = []
        if results_text:
            key_results = [s.strip() for s in re.split(r"[。.\n]+", results_text) if s.strip()][:3]
        discussion = str(featured.get("novelty") or "")
        limitation = str(featured.get("limitation") or "")
        conclusion = str(featured.get("results") or "")

        spec = SummaryImageSpec(
            date_str=today_str,
            issue_no=issue_no,
            featured_title=str(featured.get("title") or "Top Pick"),
            featured_pmid=str(featured.get("pmid") or ""),
            featured_authors=str(featured.get("authors") or ""),
            featured_journal=journal,
            featured_year=year,
            setting=setting,
            key_results=key_results,
            discussion=discussion,
            limitation=limitation,
            conclusion=conclusion,
        )
        prompt = build_summary_image_prompt(spec)

        image_model = os.getenv("SUMMARY_IMAGE_MODEL", "gemini-2.5-flash-image")
        aspect_ratio = os.getenv("SUMMARY_IMAGE_ASPECT_RATIO", "16:9")
        png_bytes = generate_summary_image_bytes(
            api_key=_ensure_env("GEMINI_API_KEY"),
            prompt=prompt,
            model=image_model,
            aspect_ratio=aspect_ratio,
        )
        image_path = default_summary_image_path(
            issues_dir=issues_path, date_str=today_str, issue_no=issue_no
        )
        image_path.write_bytes(png_bytes)
        print(f"[INFO] Saved summary image to {image_path}")

        if os.getenv("SUMMARY_IMAGE_EMBED", "").lower() in {"1", "true", "yes"}:
            repo = os.getenv("GITHUB_REPOSITORY", "")
            ref = os.getenv("GITHUB_REF_NAME", "main")
            if repo:
                raw_url = build_github_raw_url(
                    repo=repo, ref=ref, path=str(image_path.relative_to(Path(__file__).resolve().parents[1]))
                )
                newsletter_md = maybe_prepend_summary_image(newsletter_md, image_url=raw_url)
            else:
                print("[WARN] SUMMARY_IMAGE_EMBED is set but GITHUB_REPOSITORY is missing; skipping embed.")

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
