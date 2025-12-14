from pathlib import Path
import sys


PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


from src.summary_image_generator import (  # noqa: E402
    SummaryImageSpec,
    build_github_raw_url,
    build_summary_image_prompt,
    extract_top_picks_titles,
    maybe_prepend_summary_image,
)


def test_extract_top_picks_titles_finds_headings_in_section():
    md = """
## 今週の Top Picks

### Paper A (PMID: 111) ([PubMed](https://pubmed.ncbi.nlm.nih.gov/111/))

### Paper B (PMID: 222)

## Method Spotlight
### Paper C (PMID: 333)
""".strip()
    assert extract_top_picks_titles(md, max_items=3) == ["Paper A", "Paper B"]


def test_build_summary_image_prompt_contains_required_text():
    spec = SummaryImageSpec(date_str="2025-12-14", issue_no=8, top_picks=["A", "B", "C"])
    prompt = build_summary_image_prompt(spec)
    assert "CT/MRI×AI Weekly" in prompt
    assert "2025-12-14" in prompt
    assert "#008" in prompt


def test_maybe_prepend_summary_image_is_idempotent():
    md = "body"
    url = "https://example.com/x.png"
    out1 = maybe_prepend_summary_image(md, image_url=url)
    out2 = maybe_prepend_summary_image(out1, image_url=url)
    assert out1 == out2


def test_build_github_raw_url_is_expected_format():
    url = build_github_raw_url(repo="owner/repo", ref="main", path="issues/a.png")
    assert url == "https://raw.githubusercontent.com/owner/repo/main/issues/a.png"

