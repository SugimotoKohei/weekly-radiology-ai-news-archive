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
      /* Color-blind friendly palette (Okabe-Ito inspired) */
      /* Blue: #0072B2, Orange: #E69F00, Green: #009E73, Purple: #CC79A7 */
      body {{ margin: 0; padding: 0; background: #EEF2FF; color: #111827; }}
      a {{ color: #0B62B3; text-decoration: underline; text-underline-offset: 2px; }}
      a:hover {{ color: #084E8E; }}
      .container {{ width: 100%; background: #EEF2FF; padding: 26px 12px; }}
      .card {{ max-width: 720px; margin: 0 auto; background: #FFFFFF; border: 1px solid #D6E1F0; border-radius: 14px; overflow: hidden; box-shadow: 0 6px 18px rgba(17, 24, 39, 0.08); }}
      .header {{ background: #0B1F3A; color: #FFFFFF; padding: 18px 20px; }}
      .header-accent {{ height: 4px; background: #0072B2; }}
      .header-title {{ margin: 0; font-size: 18px; font-weight: 800; line-height: 1.3; letter-spacing: 0.2px; }}
      .header-meta {{ margin: 8px 0 0 0; font-size: 12px; color: #D1E9FF; }}
      .badge {{ display: inline-block; padding: 2px 10px; margin-left: 8px; border-radius: 999px; background: #E6F4FF; color: #0B62B3; font-weight: 700; font-size: 11px; }}
      .content {{ padding: 18px 20px 10px 20px; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Noto Sans JP', 'Hiragino Sans', 'Helvetica Neue', Arial, sans-serif; }}
      h2 {{ margin: 18px 0 12px; font-size: 16px; padding: 10px 12px; background: #F3F4F6; border-left: 4px solid #E69F00; border-radius: 10px; }}
      h3 {{ margin: 16px 0 8px; font-size: 14px; }}
      h3 a {{ text-decoration: underline; }}
      p {{ margin: 10px 0; line-height: 1.65; }}
      ul {{ margin: 10px 0 12px 18px; padding: 0; }}
      li {{ margin: 6px 0; line-height: 1.55; }}
      li strong {{ color: #0B1F3A; }}
      hr {{ border: 0; border-top: 1px solid #D6E1F0; margin: 16px 0; }}
      img {{ max-width: 100%; height: auto; border-radius: 12px; border: 1px solid #D6E1F0; }}
      .footer {{ padding: 14px 20px; font-size: 12px; color: #374151; background: #F8FAFC; border-top: 1px solid #D6E1F0; }}
      .preheader {{ display: none; font-size: 1px; color: #F3F4F6; line-height: 1px; max-height: 0px; max-width: 0px; opacity: 0; overflow: hidden; }}
    </style>
  </head>
  <body>
    <div class="preheader">{_escape_html(preheader)}</div>
    <div class="container">
      <div class="card">
        <div class="header">
          <p class="header-title">{_escape_html(ctx.subject)}</p>
          <p class="header-meta">Issue #{ctx.issue_no:03d} · {ctx.date_str}<span class="badge">Draft</span></p>
        </div>
        <div class="header-accent"></div>
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
