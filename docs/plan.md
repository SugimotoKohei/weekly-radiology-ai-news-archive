# 運用計画: CT/MRI×AI Weekly Archive（自動収集・要約・配信）

- Last updated: 2025-12-14

本リポジトリは **週刊ニュースレターを自動生成して送信する**ためのコード・設定・CI を管理する。
研究論文執筆やノートブック運用はスコープ外とする。

## 1. 目的
- PubMed から候補論文を収集する。
- Gemini API でニュースレター Markdown を生成する（失敗時はフォールバックで継続）。
- Buttondown へ送信（またはドラフト作成）する。
- 同一内容を `issues/` にアーカイブする。
  - ニュースレター本文は「今週の Top Picks」最大5本に絞る（量より質）。

## 2. 入力（Git 管理）
- `src/` / `scripts/`：実装
- `configs/base/newsletter_template.yaml`：ニュースレターのテンプレ（プロンプト・必須セクションなど）
- `.github/workflows/newsletter-buttondown.yml`：週次自動実行
- `pyproject.toml` / `uv.lock`：依存固定

## 3. 出力（Git 管理しない想定）
- 実行ログ、キャッシュ、途中生成物は原則 `output/` に出す（必要になったら追加）。
- 最終的なニュースレター本文は `issues/` に Markdown として残す（Git 管理）。

## 4. 実行パス
### ローカル
- `uv sync`
- `uv run python scripts/run_pipeline.py`
  - API キーなしで動作確認する場合: `uv run python scripts/run_pipeline.py --dry-run`

### CI（GitHub Actions）
- 週次スケジュール + 手動実行で `scripts/run_pipeline.py` を実行し、`issues/` 更新をコミットする。
  - まずは **ドラフト作成運用**（`BUTTONDOWN_STATUS=draft`）で運用し、内容確認後に Buttondown 側から手動送信する。
  - 誤送信防止のため、GitHub Actions 上では `BUTTONDOWN_STATUS` が `draft` 以外のときに失敗する（明示的な opt-in が必要）。

## 5. 環境変数
- `GEMINI_API_KEY`（必須）
- `GEMINI_MODEL`（任意、既定: `gemini-2.5-flash`）
- `PUBMED_API_KEY`（任意）
- `PUBMED_QUERY`（任意）
- `PUBMED_RELDAYS` / `PUBMED_RETMAX`（任意）
- `PUBMED_FALLBACK_RELDAYS`（任意）
- `NEWSLETTER_TEMPLATE_PATH`（任意、既定: `configs/base/newsletter_template.yaml`）
- `BUTTONDOWN_API_KEY`（必須）
- `BUTTONDOWN_STATUS`（任意、既定: `draft`）
- `BUTTONDOWN_ALLOW_ACTIONS_SEND`（任意、既定: false）
  - `true` のときのみ、GitHub Actions 上で `draft` 以外のステータスを許可する。
- `SUMMARY_IMAGE_ENABLED`（任意、既定: false）
  - `true` のとき、Gemini 画像モデル（通称 “nano banana”）でサマリー画像（PNG）を生成して `issues/` に保存する。
- `SUMMARY_IMAGE_MODEL`（任意、既定: `gemini-2.5-flash-image`）
- `SUMMARY_IMAGE_ASPECT_RATIO`（任意、既定: `16:9`）
- `SUMMARY_IMAGE_EMBED`（任意、既定: false）
  - `true` のとき、生成した画像を GitHub raw URL で本文先頭に埋め込む（Actions 実行時のみ推奨）。
