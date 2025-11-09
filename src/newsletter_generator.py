from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List, Sequence

import requests
import yaml

from src.pubmed_client import PubMedPaper


GEMINI_ENDPOINT = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-pro-latest:generateContent"
DEFAULT_REQUIRED_SECTIONS = [
    "今週の Top Picks",
    "Method Spotlight",
    "Dataset / Benchmark",
    "Review & Big Picture",
    "総括・編集後記",
]
DEFAULT_TEMPLATE_PATH = Path(__file__).resolve().parents[1] / "config" / "newsletter_template.yaml"


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
        raise RuntimeError(f"Newsletter generation failed: {last_error}")

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
    def _has_required_sections(text: str, sections: Sequence[str]) -> bool:
        lowered = text.lower()
        return all(section.lower() in lowered for section in sections)


__all__ = [
    "NewsletterGenerator",
    "NewsletterTemplate",
    "DEFAULT_TEMPLATE_PATH",
    "DEFAULT_REQUIRED_SECTIONS",
]
