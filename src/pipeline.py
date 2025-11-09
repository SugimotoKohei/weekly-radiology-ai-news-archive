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


def run_pipeline() -> None:
    jst = tz.gettz("Asia/Tokyo")
    today = datetime.now(tz=jst)
    today_str = today.strftime("%Y-%m-%d")
    query = os.getenv("PUBMED_QUERY", DEFAULT_QUERY)
    days = int(os.getenv("PUBMED_RELDAYS", "7"))
    retmax = int(os.getenv("PUBMED_RETMAX", "40"))

    pubmed_client = PubMedClient(api_key=os.getenv("PUBMED_API_KEY"))
    papers = pubmed_client.get_recent_papers(query, days=days, retmax=retmax)
    if not papers:
        print("[INFO] No new PubMed articles found. Exiting.")
        return

    template_path = Path(os.getenv("NEWSLETTER_TEMPLATE_PATH", str(DEFAULT_TEMPLATE_PATH)))
    template = NewsletterTemplate.from_file(template_path)
    generator = NewsletterGenerator(api_key=_ensure_env("GEMINI_API_KEY"), template=template)
    newsletter_md = generator.generate(papers, today_str)

    issues_path = _issues_dir()
    issue_no = _next_issue_number(issues_path)
    md_path = _save_issue_markdown(today_str, issue_no, newsletter_md)
    print(f"[INFO] Saved newsletter markdown to {md_path}")

    buttondown_status = os.getenv("BUTTONDOWN_STATUS", "sent")
    if buttondown_status not in {"sent", "draft"}:
        raise RuntimeError("BUTTONDOWN_STATUS must be 'sent' or 'draft'")
    buttondown = ButtondownClient(api_key=_ensure_env("BUTTONDOWN_API_KEY"))
    subject = f"CT/MRI×AI Weekly #{issue_no} - {today_str}"
    email_status = cast(EmailStatus, buttondown_status)
    buttondown.send_email(subject=subject, body=newsletter_md, status=email_status)
    print("[INFO] Buttondown email request submitted")


if __name__ == "__main__":
    run_pipeline()
