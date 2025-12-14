from pathlib import Path
import sys


PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


from src.email_renderer import EmailRenderContext, render_newsletter_html  # noqa: E402


def test_render_newsletter_html_wraps_markdown():
    md = "## 今週の Top Picks\n\n### A (PMID: [1](https://pubmed.ncbi.nlm.nih.gov/1/))\n\n- **雑誌名**: X\n"
    html = render_newsletter_html(md, ctx=EmailRenderContext(subject="S", date_str="2025-12-14", issue_no=1))
    assert "<!doctype html>" in html.lower()
    assert "Issue #001" in html
    assert "今週の Top Picks" in html
    assert "https://pubmed.ncbi.nlm.nih.gov/1/" in html

