from pathlib import Path
import sys


PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


from src.summary_image_generator import (  # noqa: E402
    SummaryImageSpec,
    build_github_raw_url,
    build_summary_image_prompt,
    extract_featured_top_pick,
    extract_top_picks_titles,
    insert_summary_image_after_top_picks,
)


def test_extract_top_picks_titles_finds_headings_in_section():
    md = """
## 今週の Top Picks

### Paper A (PMID: [111](https://pubmed.ncbi.nlm.nih.gov/111/))

### Paper B (PMID: 222)

## Method Spotlight
### Paper C (PMID: 333)
""".strip()
    assert extract_top_picks_titles(md, max_items=3) == ["Paper A", "Paper B"]


def test_build_summary_image_prompt_contains_required_text():
    spec = SummaryImageSpec(
        date_str="2025-12-14",
        issue_no=8,
        featured_title="Paper A",
        featured_pmid="111",
        featured_authors="A, B",
        featured_journal="Journal",
        featured_year="2025",
        setting={"Study design": "Retrospective"},
        key_results=["AUC 0.9"],
        discussion="x",
        limitation="y",
        conclusion="z",
    )
    prompt = build_summary_image_prompt(spec)
    assert "clinical_paper_infographic_spec_jp.yaml" in prompt
    assert "Clinical Paper Infographic – 3-column layout" in prompt
    assert "SETTING" in prompt
    assert "KEY RESULTS" in prompt
    assert "2025-12-14" in prompt
    assert "#008" in prompt


def test_insert_summary_image_after_top_picks_is_idempotent():
    md = "## 今週の Top Picks\n\n### A (PMID: [1](https://pubmed.ncbi.nlm.nih.gov/1/))\n\n## 総括・編集後記\nx\n"
    url = "https://example.com/x.png"
    out1 = insert_summary_image_after_top_picks(md, image_url=url)
    out2 = insert_summary_image_after_top_picks(out1, image_url=url)
    assert out1 == out2


def test_build_github_raw_url_is_expected_format():
    url = build_github_raw_url(repo="owner/repo", ref="main", path="issues/a.png")
    assert url == "https://raw.githubusercontent.com/owner/repo/main/issues/a.png"


def test_extract_featured_top_pick_parses_fields():
    md = """
## 今週の Top Picks

### Paper A (PMID: [111](https://pubmed.ncbi.nlm.nih.gov/111/))
- **雑誌名**: Journal, 2025
- **著者名**: A, B 他
- **所属**: Inst
- **タスク**: T
- **データ**: P
- **手法**: M
- **成果**: R
- **新規性**: N
- **限界**: L

## Method Spotlight
""".strip()
    featured = extract_featured_top_pick(md)
    assert featured is not None
    assert featured["title"] == "Paper A"
    assert featured["pmid"] == "111"
    assert featured["journal"] == "Journal, 2025"
    assert featured["authors"] == "A, B 他"


def test_insert_summary_image_after_top_picks_places_before_editorial():
    md = """
## 今週の Top Picks

### Paper A (PMID: [111](https://pubmed.ncbi.nlm.nih.gov/111/))
- **雑誌名**: J

## 総括・編集後記
E
""".strip()
    out = insert_summary_image_after_top_picks(md, image_url="https://example.com/s.png")
    # Image should appear before the editorial header.
    assert out.index("![Summary](https://example.com/s.png)") < out.index("## 総括・編集後記")
