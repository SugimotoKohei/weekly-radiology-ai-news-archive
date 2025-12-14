from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Optional

import markdown as md


@dataclass(frozen=True)
class EmailRenderContext:
    subject: str
    date_str: str
    issue_no: int
    preheader: Optional[str] = None


def render_newsletter_html(markdown_body: str, *, ctx: EmailRenderContext) -> str:
    """Render newsletter Markdown into a simple, email-friendly HTML."""
    html_body = md.markdown(
        markdown_body,
        extensions=[
            "extra",
            "sane_lists",
        ],
        output_format="html5",
    )

    preheader = (ctx.preheader or "CT/MRI×AI の注目論文を要約しました。").strip()

    # Email clients vary widely; keep the layout simple and mostly inline styles.
    return f"""\
<!doctype html>
<html lang="ja">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta name="x-apple-disable-message-reformatting" />
    <title>{_escape_html(ctx.subject)}</title>
    <style>
      body {{ margin: 0; padding: 0; background: #F3F4F6; color: #111827; }}
      a {{ color: #2563EB; text-decoration: none; }}
      a:hover {{ text-decoration: underline; }}
      .container {{ width: 100%; background: #F3F4F6; padding: 24px 12px; }}
      .card {{ max-width: 720px; margin: 0 auto; background: #FFFFFF; border: 1px solid #E5E7EB; border-radius: 12px; overflow: hidden; }}
      .header {{ background: #111827; color: #FFFFFF; padding: 18px 20px; }}
      .header-title {{ margin: 0; font-size: 18px; font-weight: 700; line-height: 1.3; }}
      .header-meta {{ margin: 6px 0 0 0; font-size: 12px; color: #D1D5DB; }}
      .content {{ padding: 18px 20px 10px 20px; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Noto Sans JP', 'Hiragino Sans', 'Helvetica Neue', Arial, sans-serif; }}
      h2 {{ margin: 18px 0 10px; font-size: 16px; border-bottom: 1px solid #E5E7EB; padding-bottom: 6px; }}
      h3 {{ margin: 16px 0 8px; font-size: 14px; }}
      p {{ margin: 10px 0; line-height: 1.6; }}
      ul {{ margin: 10px 0 10px 18px; padding: 0; }}
      li {{ margin: 6px 0; line-height: 1.5; }}
      hr {{ border: 0; border-top: 1px solid #E5E7EB; margin: 16px 0; }}
      img {{ max-width: 100%; height: auto; border-radius: 10px; }}
      .footer {{ padding: 14px 20px; font-size: 12px; color: #6B7280; background: #F9FAFB; border-top: 1px solid #E5E7EB; }}
      .preheader {{ display: none; font-size: 1px; color: #F3F4F6; line-height: 1px; max-height: 0px; max-width: 0px; opacity: 0; overflow: hidden; }}
    </style>
  </head>
  <body>
    <div class="preheader">{_escape_html(preheader)}</div>
    <div class="container">
      <div class="card">
        <div class="header">
          <p class="header-title">{_escape_html(ctx.subject)}</p>
          <p class="header-meta">Issue #{ctx.issue_no:03d} · {ctx.date_str}</p>
        </div>
        <div class="content">
          {html_body}
        </div>
        <div class="footer">
          <div>Generated automatically · {datetime.now().strftime("%Y-%m-%d %H:%M")}</div>
        </div>
      </div>
    </div>
  </body>
</html>
"""


def _escape_html(value: str) -> str:
    return (
        value.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
        .replace("'", "&#39;")
    )

