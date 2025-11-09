import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.newsletter_generator import (
    DEFAULT_REQUIRED_SECTIONS,
    DEFAULT_TEMPLATE_PATH,
    NewsletterGenerator,
    NewsletterTemplate,
)


def test_has_required_sections_returns_true():
    text = "\n".join(DEFAULT_REQUIRED_SECTIONS)
    assert NewsletterGenerator._has_required_sections(text, DEFAULT_REQUIRED_SECTIONS)


def test_has_required_sections_missing_one_returns_false():
    text = "\n".join(DEFAULT_REQUIRED_SECTIONS[:-1])
    assert not NewsletterGenerator._has_required_sections(text, DEFAULT_REQUIRED_SECTIONS)


def test_template_from_file_loads_required_sections():
    template = NewsletterTemplate.from_file(DEFAULT_TEMPLATE_PATH)
    assert list(template.required_sections) == DEFAULT_REQUIRED_SECTIONS
    assert "{today}" in template.user_prompt_template
    assert "{papers_json}" in template.user_prompt_template
