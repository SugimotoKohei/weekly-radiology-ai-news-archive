import sys
from pathlib import Path

import requests

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.newsletter_generator import (
    DEFAULT_REQUIRED_SECTIONS,
    DEFAULT_TEMPLATE_PATH,
    NewsletterGenerator,
    NewsletterTemplate,
)
from src.pubmed_client import PubMedPaper


def _sample_template() -> NewsletterTemplate:
    return NewsletterTemplate(
        system_prompt="system",
        user_prompt_template="今日: {today}\n{papers_json}",
        required_sections=DEFAULT_REQUIRED_SECTIONS,
        temperature=0.0,
        top_picks_max=2,
    )


def test_has_required_sections_returns_true():
    text = "\n".join(DEFAULT_REQUIRED_SECTIONS)
    assert NewsletterGenerator._has_required_sections(text, DEFAULT_REQUIRED_SECTIONS)

def test_has_required_sections_is_robust_to_heading_variants():
    text = """
## 今週のTop Picks
- a

## Method Spotlight
- b

## Dataset/Benchmark
- c

## Review and Big Picture
- d

## 総括・編集後記
- e
""".strip()
    assert NewsletterGenerator._has_required_sections(text, DEFAULT_REQUIRED_SECTIONS)


def test_has_required_sections_missing_one_returns_false():
    text = "\n".join(DEFAULT_REQUIRED_SECTIONS[:-1])
    assert not NewsletterGenerator._has_required_sections(text, DEFAULT_REQUIRED_SECTIONS)


def test_template_from_file_loads_required_sections():
    template = NewsletterTemplate.from_file(DEFAULT_TEMPLATE_PATH)
    assert list(template.required_sections) == DEFAULT_REQUIRED_SECTIONS
    assert "{today}" in template.user_prompt_template
    assert "{papers_json}" in template.user_prompt_template


def test_generate_returns_fallback_when_invoke_fails(monkeypatch):
    template = _sample_template()
    generator = NewsletterGenerator(api_key="dummy", template=template)

    def _raise_error(payload):  # noqa: ANN001
        raise requests.HTTPError("404 Not Found")

    monkeypatch.setattr(generator, "_invoke", _raise_error)

    papers = [
        PubMedPaper(
            pmid="1",
            title="Test Paper",
            abstract="Short abstract",
            journal="Test Journal",
            pub_year="2025",
            pub_date="2025-11-09",
            authors=["A"],
            authors_total=1,
            affiliations=["Affiliation A"],
            link="https://example.com",
        )
    ]

    result = generator.generate(papers, "2025-11-09", max_retries=0)
    assert "Fallback" in result
    assert "404 Not Found" in result
    assert "Test Paper" in result
