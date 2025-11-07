from __future__ import annotations

from typing import Literal, Optional

import requests


BUTTONDOWN_API_URL = "https://api.buttondown.com/v1/emails"

EmailStatus = Literal["draft", "sent"]


class ButtondownClient:
    def __init__(self, api_key: str, *, api_url: str = BUTTONDOWN_API_URL) -> None:
        if not api_key:
            raise ValueError("BUTTONDOWN_API_KEY is required")
        self.api_key = api_key
        self.api_url = api_url

    def send_email(self, *, subject: str, body: str, status: EmailStatus = "sent") -> dict:
        payload = {
            "subject": subject,
            "body": body,
            "status": status,
        }
        headers = {
            "Authorization": f"Token {self.api_key}",
            "Content-Type": "application/json",
        }
        resp = requests.post(self.api_url, headers=headers, json=payload, timeout=60)
        resp.raise_for_status()
        return resp.json()


__all__ = ["ButtondownClient", "EmailStatus"]
