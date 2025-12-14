from __future__ import annotations

import base64
import os
import re
from dataclasses import dataclass
from pathlib import Path
from typing import List, Sequence

import requests


GEMINI_IMAGE_API_BASE = "https://generativelanguage.googleapis.com/v1beta/models"


@dataclass(frozen=True)
class SummaryImageSpec:
    date_str: str
    issue_no: int
    top_picks: Sequence[str]


def _ensure_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Environment variable {name} is required")
    return value


def extract_top_picks_titles(markdown: str, *, max_items: int = 3) -> List[str]:
    """Extract paper titles from the Top Picks section.

    We expect headings like:
      ### <title> (PMID: <pmid>) ([PubMed](...))
    """
    # Grab the Top Picks section body.
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
    heading_re = re.compile(r"^###\s+(.+?)\s+\(PMID:\s*\d+\).*?$", flags=re.MULTILINE)
    for match in heading_re.finditer(body):
        title = match.group(1).strip()
        if title:
            titles.append(title)
        if len(titles) >= max_items:
            break
    return titles


def build_summary_image_prompt(spec: SummaryImageSpec) -> str:
    top_picks_lines = "\n".join([f"- {t}" for t in spec.top_picks[:3]]) or "- (該当なし)"
    return f"""\
あなたはプロのデザイン制作者です。以下の内容を元に、ニュースレターの「サマリー画像」(16:9) を1枚生成してください。

要件:
- 画像は 16:9、モダンで読みやすいインフォグラフィック風（フラット寄り、余白多め、視認性重視）。
- 背景は白〜薄いグレー、アクセントに青系を少し。
- 文字は日本語で可読に。長文は避け、短い行にする。
- 余計な装飾・透かし・小さすぎる文字は避ける。

画像内に必ず入れるテキスト:
- タイトル: CT/MRI×AI Weekly
- 日付: {spec.date_str}
- Issue: #{spec.issue_no:03d}
- セクション見出し: Top Picks
- Top Picks（3本まで）:
{top_picks_lines}

視覚要素:
- CT/MRI を連想するシンプルなアイコン（抽象的でOK）
- 「Draft」相当の控えめなラベル（小さく右上）
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
    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {
            "responseModalities": ["Image"],
        },
        "imageConfig": {"aspectRatio": aspect_ratio},
    }
    resp = requests.post(url, headers=headers, json=payload, timeout=timeout_s)
    resp.raise_for_status()
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


def maybe_prepend_summary_image(markdown: str, *, image_url: str) -> str:
    if not image_url:
        return markdown
    # Avoid double-prepending if rerun.
    if markdown.lstrip().startswith("![Summary]("):
        return markdown
    return f"![Summary]({image_url})\n\n{markdown}"


def build_github_raw_url(*, repo: str, ref: str, path: str) -> str:
    # Example:
    # https://raw.githubusercontent.com/<owner>/<repo>/<ref>/<path>
    return f"https://raw.githubusercontent.com/{repo}/{ref}/{path.lstrip('/')}"

