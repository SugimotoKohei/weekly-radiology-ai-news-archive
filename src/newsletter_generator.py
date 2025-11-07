from __future__ import annotations

import json
import textwrap
from typing import Iterable, List, Sequence

import requests

from pubmed_client import PubMedPaper


GEMINI_ENDPOINT = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-pro-latest:generateContent"
REQUIRED_SECTIONS = [
    "今週の Top Picks",
    "Method Spotlight",
    "Dataset / Benchmark",
    "Review & Big Picture",
    "総括・編集後記",
]


class NewsletterGenerator:
    def __init__(self, api_key: str, *, model_endpoint: str = GEMINI_ENDPOINT, temperature: float = 0.2) -> None:
        if not api_key:
            raise ValueError("GEMINI_API_KEY is required")
        self.api_key = api_key
        self.model_endpoint = model_endpoint
        self.temperature = temperature

    def generate(self, papers: Sequence[PubMedPaper], today_str: str, *, max_retries: int = 2) -> str:
        if not papers:
            raise ValueError("papers must not be empty")
        payload = self._build_payload(papers, today_str)
        last_error = None
        for attempt in range(max_retries + 1):
            try:
                text = self._invoke(payload)
            except Exception as exc:  # noqa: BLE001
                last_error = exc
            else:
                if self._has_required_sections(text):
                    return text.strip()
                last_error = RuntimeError("Generated content missing required sections")
            payload["generationConfig"]["temperature"] = max(0.0, self.temperature - 0.05 * (attempt + 1))
        raise RuntimeError(f"Newsletter generation failed: {last_error}")

    def _build_payload(self, papers: Sequence[PubMedPaper], today_str: str) -> dict:
        system_prompt = textwrap.dedent(
            """
            あなたは放射線科医かつ医用画像AI研究者であり、ニュースレター編集者です。
            セクション構成: 今週の Top Picks / Method Spotlight / Dataset / Benchmark / Review & Big Picture / 総括・編集後記。
            各論文でタスク・データ・手法・指標・So what・Limitation を必ず触れてください。
            出力は Markdown のみ。
            """
        ).strip()
        paper_dicts = [paper.to_dict() for paper in papers]
        user_prompt = textwrap.dedent(
            f"""
            今日の日付: {today_str}

            以下の論文候補を基にニュースレターを作成してください。CT/MRI に関連する内容を優先し、
            Top Picks は最大3本、その他セクションにも最低1本ずつ触れてください。

            論文リスト (JSON):
            {json.dumps(paper_dicts, ensure_ascii=False, indent=2)}
            """
        ).strip()
        return {
            "contents": [
                {"parts": [{"text": system_prompt}]},
                {"parts": [{"text": user_prompt}]},
            ],
            "generationConfig": {
                "temperature": self.temperature,
            },
        }

    def _invoke(self, payload: dict) -> str:
        headers = {
            "Content-Type": "application/json",
            "x-goog-api-key": self.api_key,
        }
        resp = requests.post(self.model_endpoint, headers=headers, json=payload, timeout=120)
        resp.raise_for_status()
        data = resp.json()
        candidates = data.get("candidates", [])
        if not candidates:
            raise RuntimeError("Gemini response missing candidates")
        parts: Iterable[dict] = candidates[0].get("content", {}).get("parts", [])
        texts: List[str] = [part.get("text", "") for part in parts if part.get("text")]
        if not texts:
            raise RuntimeError("Gemini response missing text parts")
        return "\n".join(texts)

    @staticmethod
    def _has_required_sections(text: str) -> bool:
        lowered = text.lower()
        return all(section.lower() in lowered for section in REQUIRED_SECTIONS)


__all__ = ["NewsletterGenerator", "REQUIRED_SECTIONS"]
