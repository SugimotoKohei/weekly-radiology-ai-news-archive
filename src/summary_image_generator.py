from __future__ import annotations

import base64
import os
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence

import requests


GEMINI_IMAGE_API_BASE = "https://generativelanguage.googleapis.com/v1beta/models"


@dataclass(frozen=True)
class SummaryImageSpec:
    date_str: str
    issue_no: int
    featured_title: str
    featured_pmid: str
    featured_authors: str
    featured_journal: str
    featured_year: str
    setting: Dict[str, str]
    key_results: List[str]
    discussion: str
    limitation: str
    conclusion: str


def _ensure_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Environment variable {name} is required")
    return value


def _extract_section(markdown: str, header_text: str) -> str:
    header_re = re.compile(rf"^##\s*{re.escape(header_text)}\s*$", flags=re.MULTILINE)
    m = header_re.search(markdown)
    if not m:
        return ""
    start = m.end()
    rest = markdown[start:]
    next_header = re.search(r"^\s*##\s+", rest, flags=re.MULTILINE)
    end = start + (next_header.start() if next_header else len(rest))
    return markdown[start:end]


def extract_top_picks_titles(markdown: str, *, max_items: int = 3) -> List[str]:
    """Extract paper titles from the Top Picks section."""
    section_re = re.compile(
        r"^##\s*今週の\s*Top\s*Picks\s*$",
        flags=re.MULTILINE,
    )
    m = section_re.search(markdown)
    if not m:
        return []
    start = m.end()
    rest = markdown[start:]
    next_header = re.search(r"^\s*##\s+", rest, flags=re.MULTILINE)
    end = start + (next_header.start() if next_header else len(rest))
    body = markdown[start:end]

    titles: List[str] = []
    heading_re = re.compile(
        r"^###\s+(.+?)\s+\(PMID:\s*(?:\[\s*)?\d+(?:\s*\]\([^)]+\))?\)\s*$",
        flags=re.MULTILINE,
    )
    for match in heading_re.finditer(body):
        title = match.group(1).strip()
        if title:
            titles.append(title)
        if len(titles) >= max_items:
            break
    return titles


def extract_featured_top_pick(markdown: str) -> Optional[Dict[str, Any]]:
    """Extract the first Top Pick block as structured data.

    Expected structure:
      ## 今週の Top Picks
      ### <title> (PMID: <pmid>) ([PubMed](<link>))
      - **雑誌名**: ...
      - **著者名**: ...
      - **所属**: ...
      - **タスク**: ...
      - **データ**: ...
      - **手法**: ...
      - **成果**: ...
      - **新規性**: ...
      - **限界**: ...
    """
    top_picks_body = _extract_section(markdown, "今週の Top Picks")
    if not top_picks_body:
        return None

    heading_re = re.compile(
        r"^###\s+(?P<title>.+?)\s+\(PMID:\s*(?:\[\s*)?(?P<pmid>\d+)(?:\s*\]\([^)]+\))?\)\s*$",
        flags=re.MULTILINE,
    )
    m = heading_re.search(top_picks_body)
    if not m:
        return None

    title = m.group("title").strip()
    pmid = m.group("pmid").strip()
    start = m.end()
    rest = top_picks_body[start:]
    next_heading = heading_re.search(rest)
    block = rest[: next_heading.start() if next_heading else len(rest)]

    fields: Dict[str, str] = {}
    bullet_re = re.compile(r"^\s*-\s*\*\*(?P<label>[^*]+)\*\*\s*:\s*(?P<value>.+?)\s*$")
    for line in block.splitlines():
        bm = bullet_re.match(line)
        if not bm:
            continue
        label = bm.group("label").strip()
        value = bm.group("value").strip()
        fields[label] = value

    return {
        "title": title,
        "pmid": pmid,
        "journal": fields.get("雑誌名", ""),
        "authors": fields.get("著者名", ""),
        "affiliations": fields.get("所属", ""),
        "task": fields.get("タスク", ""),
        "data": fields.get("データ", ""),
        "methods": fields.get("手法", ""),
        "results": fields.get("成果", ""),
        "novelty": fields.get("新規性", ""),
        "limitation": fields.get("限界", ""),
    }


def _split_journal_year(journal_field: str) -> tuple[str, str]:
    if not journal_field:
        return "", ""
    # Often: "<journal>, 2025"
    m = re.match(r"^(.*?)(?:,\s*(\d{4}))\s*$", journal_field)
    if m:
        return m.group(1).strip(), m.group(2).strip()
    return journal_field.strip(), ""


def _heuristic_setting(featured: Dict[str, Any]) -> Dict[str, str]:
    data = (featured.get("data") or "").strip()
    methods = (featured.get("methods") or "").strip()
    results = (featured.get("results") or "").strip()
    affiliations = (featured.get("affiliations") or "").strip()

    setting = {
        "Study design": "Not specified",
        "Population": data or "Not specified",
        "Exclusion criteria": "Not specified",
        "Data source / Setting": affiliations or "Not specified",
        "Primary outcome": (featured.get("task") or "").strip() or "Not specified",
        "Key secondary outcomes": "Not specified",
        "Statistical methods": "Not specified",
    }

    lowered = methods.lower()
    if "retrospective" in lowered or "後ろ向き" in methods:
        setting["Study design"] = "Retrospective"
    elif "prospective" in lowered or "前向き" in methods:
        setting["Study design"] = "Prospective"

    if re.search(r"p\s*[<=>]\s*0\.\d+", results, flags=re.IGNORECASE) or "p<" in results.lower():
        setting["Statistical methods"] = "Reported (see Key Results)"

    return setting


def _key_results_lines(results: str, *, max_items: int = 3) -> List[str]:
    if not results:
        return []
    # Prefer sentences with numbers.
    candidates: List[str] = []
    for sent in re.split(r"[。.\n]+", results):
        s = sent.strip()
        if not s:
            continue
        if re.search(r"\d", s):
            candidates.append(s)
    if not candidates:
        candidates = [results.strip()]
    return candidates[:max_items]


def build_summary_image_prompt(spec: SummaryImageSpec) -> str:
    subtitle = (
        f"{spec.featured_title} — {spec.featured_authors} — {spec.featured_journal}"
        + (f", {spec.featured_year}" if spec.featured_year else "")
    ).strip(" —")
    # Provide a short suggestion; the model can refine it.
    japanese_title_hint = "結論: 主要アウトカムが改善（臨床的に意味のある差）"

    setting_lines = "\n".join([f"- {k}: {v}" for k, v in spec.setting.items()])
    key_results_lines = "\n".join([f"- {v}" for v in spec.key_results]) or "- (Not specified)"

    # The user requested the prompt to follow this spec; we include it verbatim as a guiding spec,
    # then provide the concrete content to instantiate.
    return f"""\
# clinical_paper_infographic_spec_jp.yaml
# スタイル: グレー調の臨床論文インフォグラフィック（3カラム）
# コンセプト: 「左で Setting、中央で Key Results、右で Discussion / Limitation / Conclusion を一望」

全体デザイン設定:
テーマ: "Clinical Paper Infographic – 3-column layout"
用途: "臨床論文・レビュー論文の要点を、1枚の画像で提示する"
レイアウト:
形式: "A4横 または 16:9 横長"
構成: "上部ヘッダー + 下部3カラム（左: Setting / 中央: Key Results / 右: Discussion, Limitation, Conclusion）"
下部カラム比率:
左カラム: "約30%"
中央カラム: "約40%"
右カラム: "約30%"
ビジュアル・アイデンティティ:
背景色全体: "#E5E7EB 〜 #F3F4F6 のグレー調"
ヘッダー背景色: "#374151"
本文背景色: "#F3F4F6"
左カラム背景色: "#F9FAFB"
中央カラム背景色: "#FFFFFF"
右カラム背景色: "#F3F4F6"
文字色:
メイン: "#111827"
サブ: "#4B5563"
ヘッダー文字: "#FFFFFF"
アクセントカラー: "#2563EB"
アイコン:
スタイル: "カラーのシンプルなフラットアイコン"
配置方針: "左カラムの各項目に1つずつ縦に配置し、中央・右カラムでは原則使用しない"
タイポグラフィ:
タイトル: "太めのサンセリフ体（日本語・英語両対応）"
セクション見出し: "中サイズ・太字・オールキャップ（SETTING, KEY RESULTS など）"
本文: "読みやすいサンセリフ体、行間はやや広め"
強調表現: "太字またはアクセントカラーで示す"

ページ構成:
- セクション: "Header"
位置: "ページ上端・全幅（高さ 15% 程度）"
内容:
- "日本語のインフォグラフィックタイトル（結論を含む短い一文）"
- "サブタイトルとして、論文の原文タイトル + 著者 + ジャーナル名 + 年を英語のまま記載"
デザイン:
- "ヘッダーのみ背景色を #374151 にし、文字は白。"
- "タイトルを大きく中央揃え、その下にサブタイトルを小さめに配置。"
- "ヘッダー下端に細い明るいグレーの水平線を入れて本文と区切る。"

- セクション: "Left Column – SETTING"
位置: "下部左カラム（高さ 約85% のうち左30%）"
内容ブロック:
ラベル: "SETTING"
要素:
- "Study design"
- "Population"
- "Exclusion criteria"
- "Data source / Setting"
- "Primary outcome"
- "Key secondary outcomes"
- "Statistical methods"
デザイン:
- "左カラム全体の背景は #F9FAFB。"
- "最上部に 'SETTING' の見出しバーを配置（やや濃いグレー背景 + 白文字）。"
- "各要素の左に、内容に適したカラーアイコンを1つずつ縦に配置する。"
- "ボックスで囲まず、余白と行間でブロックを区切る。"

- セクション: "Center Column – KEY RESULTS"
位置: "下部中央カラム（高さ 約85% のうち中央40%）"
内容ブロック:
ラベル: "KEY RESULTS"
説明:
- "中央カラムを 'KEY RESULTS' とし、重要な結果をグラフ中心で表示する。"
- "グラフ・図表を主役とし、文字はポイントのみ補足的に添える。"
- "必要に応じて複数のグラフを配置するが、視覚的要素を優先する。"
デザイン:
- "中央カラムの背景は #FFFFFF。"
- "最上部に 'KEY RESULTS' の見出しバーを配置し、その下にグラフを大きくレイアウトする。"
- "グラフは横長レイアウトを基本とし、テキストは最小限に抑える。"

- セクション: "Right Column – DISCUSSION / LIMITATION / CONCLUSION"
位置: "下部右カラム（高さ 約85% のうち右30%）"
内容ブロック:
- ブロック: "DISCUSSION"
説明:
- "見出し: '| DISCUSSION'。"
- "主要な臨床的解釈を日本語で1〜3文に要約する。"
- ブロック: "LIMITATION"
説明:
- "見出し: '| LIMITATION'。"
- "外的妥当性、選択バイアス、データ欠損、追跡期間などの制約を日本語で示す。"
- ブロック: "CONCLUSION"
説明:
- "見出し: '| CONCLUSION'。"
- "実臨床での位置づけや推奨、今後の研究の方向性を日本語で1〜3文にまとめる。"
デザイン:
- "右カラムの背景は #F3F4F6。"
- "各ブロックは、見出しバー（縦棒付き英語見出し）とその下の日本語テキストで構成する。"
- "DISCUSSION → LIMITATION → CONCLUSION の順に縦に並べる。"
デザインルール:
- "セクション見出しは英語（SETTING / KEY RESULTS / | DISCUSSION / | LIMITATION / | CONCLUSION）で統一し、本文は日本語で要約する。"
- "SETTING 内の各項目見出し（例: Study design, Population, Exclusion criteria, Data source / Setting, Primary outcome, Key secondary outcomes, Statistical methods）は英語で記載する。"
- "中央カラムの KEY RESULTS を最も視覚的に強調し、グラフ・図表を主役として大きく配置する。テキストはポイントのみ補足的に添え、視覚的要素を優先する。"
- "右カラムはテキスト中心とし、DISCUSSION・LIMITATION・CONCLUSION の3ブロックで構成する。"
- "アイコンは左カラムのみで使用し、画面全体をすっきり保つ。"
- "色数はグレー系のベース + アクセントの青 1 色 + アイコン用の穏やかな色合いに抑える。"
- "150 DPI 以上でエクスポートし、A4横 or 16:9 スライドで読める文字サイズを確保する。"

---

この仕様に従って、以下の内容を反映して画像を生成する:

Header:
- 日本語タイトル（結論を含む短い一文）: {japanese_title_hint}
- サブタイトル（英語のまま）: {subtitle}
- 右上に小さく: "Draft" / "CT/MRI×AI Weekly #{spec.issue_no:03d} · {spec.date_str}"

Left Column – SETTING:
{setting_lines}

Center Column – KEY RESULTS（グラフ中心。数値があれば可視化。なければ概念図でOK）:
{key_results_lines}

Right Column:
- | DISCUSSION: {spec.discussion or "Not specified"}
- | LIMITATION: {spec.limitation or "Not specified"}
- | CONCLUSION: {spec.conclusion or "Not specified"}
"""



def generate_summary_image_bytes(
    *,
    api_key: str,
    prompt: str,
    model: str = "gemini-2.5-flash-image",
    aspect_ratio: str = "16:9",
    timeout_s: int = 180,
) -> bytes:
    url = f"{GEMINI_IMAGE_API_BASE}/{model}:generateContent"
    headers = {"Content-Type": "application/json", "x-goog-api-key": api_key}
    # Follow the Gemini API REST example for image generation: keep the request minimal.
    # Aspect ratio is expressed in the prompt; optional config fields are API-version dependent.
    payload = {"contents": [{"parts": [{"text": prompt}]}]}
    resp = requests.post(url, headers=headers, json=payload, timeout=timeout_s)
    try:
        resp.raise_for_status()
    except requests.HTTPError as exc:
        raise RuntimeError(f"Gemini image generation failed: {resp.status_code} {resp.text}") from exc
    data = resp.json()
    candidates = data.get("candidates", [])
    if not candidates:
        raise RuntimeError("Gemini image response missing candidates")
    parts = candidates[0].get("content", {}).get("parts", [])
    for part in parts:
        inline = part.get("inlineData") or part.get("inline_data")
        if inline and inline.get("data"):
            return base64.b64decode(inline["data"])
    raise RuntimeError("Gemini image response missing inlineData")


def default_summary_image_path(*, issues_dir: Path, date_str: str, issue_no: int) -> Path:
    return issues_dir / f"{date_str}_ct-mri-ai-weekly-{issue_no:03d}_summary.png"


def insert_summary_image_after_top_picks(markdown: str, *, image_url: str) -> str:
    """Insert the summary image after the Top Picks section.

    Intended placement:
    - After the last Top Pick paper block
    - Before the next `##` section (e.g., editorial)
    """
    if not image_url:
        return markdown
    image_md = f"![Summary]({image_url})"
    if image_md in markdown:
        return markdown

    top_picks = _extract_section(markdown, "今週の Top Picks")
    if not top_picks.strip():
        # If the section is missing, append at the end.
        return markdown.rstrip() + "\n\n" + image_md + "\n"

    # Find the Top Picks section range in the full markdown.
    header_re = re.compile(r"^##\s*今週の\s*Top\s*Picks\s*$", flags=re.MULTILINE)
    m = header_re.search(markdown)
    if not m:
        return markdown.rstrip() + "\n\n" + image_md + "\n"
    start = m.end()
    rest = markdown[start:]
    next_header = re.search(r"^\s*##\s+", rest, flags=re.MULTILINE)
    end = start + (next_header.start() if next_header else len(rest))

    before = markdown[:end].rstrip()
    after = markdown[end:].lstrip("\n")
    return before + "\n\n" + image_md + "\n\n" + after


def build_github_raw_url(*, repo: str, ref: str, path: str) -> str:
    # Example:
    # https://raw.githubusercontent.com/<owner>/<repo>/<ref>/<path>
    return f"https://raw.githubusercontent.com/{repo}/{ref}/{path.lstrip('/')}"
