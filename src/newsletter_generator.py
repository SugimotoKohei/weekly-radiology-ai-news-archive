from __future__ import annotations

import json
import os
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List, Sequence

import requests
import yaml

from src.pubmed_client import PubMedPaper


GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
GEMINI_ENDPOINT = (
    f"https://generativelanguage.googleapis.com/v1beta/models/{GEMINI_MODEL}:generateContent"
)
DEFAULT_REQUIRED_SECTIONS = [
    "今週の Top Picks",
    "総括・編集後記",
]
DEFAULT_TEMPLATE_PATH = (
    Path(__file__).resolve().parents[1] / "configs" / "base" / "newsletter_template.yaml"
)


@dataclass
class NewsletterTemplate:
    system_prompt: str
    user_prompt_template: str
    required_sections: Sequence[str] = tuple(DEFAULT_REQUIRED_SECTIONS)
    temperature: float = 0.2
    top_picks_max: int = 3

    @classmethod
    def from_file(cls, path: str | Path) -> "NewsletterTemplate":
        config_path = Path(path)
        data = yaml.safe_load(config_path.read_text(encoding="utf-8")) or {}
        system_prompt = data.get("system_prompt")
        user_prompt_template = data.get("user_prompt_template")
        if not system_prompt or not user_prompt_template:
            raise ValueError(f"Template file {config_path} missing required prompts")
        required_sections = data.get("required_sections") or DEFAULT_REQUIRED_SECTIONS
        temperature = float(data.get("temperature", 0.2))
        top_picks_max = int(data.get("top_picks_max", 3))
        return cls(
            system_prompt=system_prompt.strip(),
            user_prompt_template=user_prompt_template.strip(),
            required_sections=required_sections,
            temperature=temperature,
            top_picks_max=top_picks_max,
        )


class NewsletterGenerator:
    def __init__(
        self,
        api_key: str,
        template: NewsletterTemplate,
        *,
        model_endpoint: str = GEMINI_ENDPOINT,
    ) -> None:
        if not api_key:
            raise ValueError("GEMINI_API_KEY is required")
        self.api_key = api_key
        self.model_endpoint = model_endpoint
        self.template = template
        self.temperature = template.temperature

    def generate(self, papers: Sequence[PubMedPaper], today_str: str, *, max_retries: int = 2) -> str:
        if not papers:
            raise ValueError("papers must not be empty")
        payload = self._build_payload(papers, today_str)
        last_error: Exception | None = None
        for attempt in range(max_retries + 1):
            try:
                text = self._invoke(payload)
            except Exception as exc:  # noqa: BLE001
                last_error = exc
            else:
                if self._has_required_sections(text, self.template.required_sections):
                    return text.strip()
                last_error = RuntimeError("Generated content missing required sections")
            payload["generationConfig"]["temperature"] = max(0.0, self.temperature - 0.05 * (attempt + 1))
        fallback = self._build_fallback_content(papers, today_str, last_error)
        return fallback

    def _build_payload(self, papers: Sequence[PubMedPaper], today_str: str) -> dict:
        paper_dicts = [paper.to_dict() for paper in papers]
        user_prompt = self.template.user_prompt_template.format(
            today=today_str,
            top_picks_max=self.template.top_picks_max,
            papers_json=json.dumps(paper_dicts, ensure_ascii=False, indent=2),
        )
        return {
            "contents": [
                {"parts": [{"text": self.template.system_prompt}]},
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
    def _normalize_for_section_match(value: str) -> str:
        lowered = value.lower()
        lowered = lowered.replace("＆", "&")
        lowered = lowered.replace("&", " and ")
        lowered = lowered.replace("：", ":")
        lowered = lowered.replace("\u3000", " ")  # full-width space
        lowered = re.sub(r"[\s#*_`>\-:|/\\]+", "", lowered)
        return lowered

    @classmethod
    def _section_variants(cls, section: str) -> List[str]:
        variants = [section]
        if section == "今週の Top Picks":
            variants.extend(["今週のTop Picks", "今週のTopPicks", "今週のトップピックス"])
        if section == "Dataset / Benchmark":
            variants.extend(["Dataset/Benchmark", "Dataset & Benchmark", "Dataset and Benchmark"])
        if section == "Review & Big Picture":
            variants.extend(["Review and Big Picture"])
        return variants

    @classmethod
    def _has_required_sections(cls, text: str, sections: Sequence[str]) -> bool:
        normalized_text = cls._normalize_for_section_match(text)
        for section in sections:
            normalized_variants = [
                cls._normalize_for_section_match(v) for v in cls._section_variants(section)
            ]
            if not any(v and v in normalized_text for v in normalized_variants):
                return False
        return True

    def _build_fallback_content(
        self,
        papers: Sequence[PubMedPaper],
        today_str: str,
        error: Exception | None,
    ) -> str:
        reason = str(error) if error else "unknown error"
        sections = list(self.template.required_sections)
        lines: List[str] = [
            "# CT/MRI×AI Weekly (Fallback Mode)",
            "",
            f"- Date: {today_str}",
            f"- Status: Gemini generation failed ({reason})",
            "",
            "---",
            "",
        ]
        # Top picks fallback
        lines.append("## 今週の Top Picks (Fallback)")
        highlighted = papers[: self.template.top_picks_max]
        if not highlighted:
            lines.append("- 今週は該当論文が取得できませんでした。")
        else:
            for paper in highlighted:
                meta_parts = []
                if paper.journal:
                    meta_parts.append(paper.journal)
                if paper.pub_year:
                    meta_parts.append(str(paper.pub_year))
                meta = ", ".join(meta_parts) if meta_parts else "N/A"
                bullet = f"- [{paper.title}]({paper.link}) — {meta}"
                if paper.abstract:
                    bullet += f"\n  - {paper.abstract[:140]}..."
                lines.append(bullet)
        # Other sections placeholder
        remaining = [s for s in sections if s != "今週の Top Picks"]
        for section in remaining:
            lines.extend(
                [
                    "",
                    f"## {section} (Fallback)",
                    "- LLM 生成が期待どおりに完了しなかったため、このセクションは簡易記録のみです。",
                ]
            )
        lines.extend(
            [
                "",
                "_This issue was auto-generated without LLM summarization due to an upstream error._",
            ]
        )
        return "\n".join(lines)


__all__ = [
    "NewsletterGenerator",
    "NewsletterTemplate",
    "DEFAULT_TEMPLATE_PATH",
    "DEFAULT_REQUIRED_SECTIONS",
]
