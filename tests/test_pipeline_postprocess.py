from pathlib import Path
import sys


PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


from src.pipeline import _enforce_editorial_one_paragraph, _normalize_pmid_links  # noqa: E402
from src.pipeline import _normalize_limitation_label  # noqa: E402
from src.pipeline import _remove_so_what  # noqa: E402


def test_normalize_pmid_links_adds_clickable_digits():
    text = "### Title (PMID: 12345678)\n\nBody\n"
    out = _normalize_pmid_links(text)
    assert "(PMID: [12345678](https://pubmed.ncbi.nlm.nih.gov/12345678/))" in out


def test_normalize_pmid_links_converts_pubmed_suffix_form():
    text = "### Title (PMID: 12345678) ([PubMed](https://pubmed.ncbi.nlm.nih.gov/12345678/))\n"
    out = _normalize_pmid_links(text)
    assert out.strip() == "### Title (PMID: [12345678](https://pubmed.ncbi.nlm.nih.gov/12345678/))"


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


def test_remove_so_what_drops_lines_containing_so_what():
    text = "a\n* **So what**: b\nc\nSo what: d\ne\n"
    out = _remove_so_what(text)
    assert "So what" not in out
    assert out.splitlines() == ["a", "c", "e"]


def test_normalize_limitation_label_removes_english_parenthetical():
    text = "* 限界（Limitation）: abc\n* 限界(limitation)： def\n"
    out = _normalize_limitation_label(text)
    assert "（Limitation）" not in out
    assert "(limitation)" not in out.lower()
    assert "* 限界: abc" in out
    assert "* 限界: def" in out
