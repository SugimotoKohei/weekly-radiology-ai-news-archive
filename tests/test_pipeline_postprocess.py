from pathlib import Path
import sys


PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


from src.pipeline import _enforce_editorial_one_paragraph, _inject_pubmed_links  # noqa: E402


def test_inject_pubmed_links_adds_link_to_heading():
    text = "### Title (PMID: 12345678)\n\nBody\n"
    out = _inject_pubmed_links(text)
    assert "([PubMed](https://pubmed.ncbi.nlm.nih.gov/12345678/))" in out


def test_inject_pubmed_links_is_idempotent_when_link_present():
    text = "### Title (PMID: 12345678) ([PubMed](https://pubmed.ncbi.nlm.nih.gov/12345678/))\n"
    out = _inject_pubmed_links(text)
    assert out == text


def test_enforce_editorial_one_paragraph_keeps_only_first_paragraph():
    text = (
        "## 総括・編集後記\n\n"
        "第一段落です。\n\n"
        "第二段落です。\n\n"
        "## 次のセクション\nx\n"
    )
    out = _enforce_editorial_one_paragraph(text)
    assert "第二段落です" not in out
    assert "第一段落です" in out

