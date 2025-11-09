# CT/MRI×AI Weekly Archive

CT/MRI を扱う医用画像 AI（segmentation / detection / classification / reconstruction）の最新論文を自動収集し、Gemini API で週刊ニュースレターを生成して Buttondown から配信、Markdown を GitHub `issues/` ディレクトリに保存するリポジトリです。

## アーキテクチャ概要
1. **データ収集**: PubMed E-utilities（必要に応じて arXiv / RSS を将来追加予定）。
2. **要約生成**: Gemini 1.5 Pro API。`config/newsletter_template.yaml` でセクション構成・プロンプトを管理し、Markdown を生成。
3. **配信**: Buttondown REST API（`POST /v1/emails`）で即時送信またはドラフト作成。
4. **自動化**: GitHub Actions（cron + workflow_dispatch）で週次実行し、`issues/` の差分を自動コミット。

## 使用技術
- Python 3.11（uv で環境・依存を管理）
- requests / python-dateutil / markdown / PyYAML
- GitHub Actions
- Buttondown API / Gemini API / PubMed E-utilities

## ディレクトリ構成
```
.
├── config/
│   └── newsletter_template.yaml  # Gemini 用プロンプトとセクション定義
├── docs/
│   ├── studyplan.md              # 実験計画（本ファイルに従って作業）
│   └── studynote.md              # 進捗・検証ログ
├── issues/                       # 自動生成される週刊 Markdown
├── scripts/                      # ローカル実行エントリポイント
├── src/                          # 実装コード
└── .github/workflows/            # CI/CD（newsletter-buttondown.yml）
```

## Secrets / 環境変数
| 名前 | 用途 |
| --- | --- |
| `GEMINI_API_KEY` | Gemini API 呼び出し |
| `GEMINI_MODEL` | 利用するモデル名（既定: `gemini-2.5-flash`） |
| `PUBMED_API_KEY` | PubMed レート制限緩和（任意） |
| `BUTTONDOWN_API_KEY` | Buttondown メール送信 |
| `BUTTONDOWN_STATUS` | `sent` / `draft`（未設定時は `sent`） |
| `NEWSLETTER_TEMPLATE_PATH` | テンプレファイルのパス（既定: `config/newsletter_template.yaml`） |
| `PUBMED_QUERY` | デフォルトクエリの上書き（任意） |
| `PUBMED_RELDAYS` / `PUBMED_RETMAX` | 取得期間・件数の上書き（任意） |
| `PUBMED_FALLBACK_RELDAYS` | 0件時に再試行する日数（既定: 30） |

ローカル開発では、これらの変数をシェルで `export` するか、**Git 管理下に置かない** `.env.local` などのファイルから読み込んでください。API キーや Secrets をリポジトリに含めることは絶対に避けてください。

## 実行ルール
- すべての検証は `docs/studyplan.md` に沿って進め、結果や気付きは `docs/studynote.md` に追記します。
- Python 実行環境は uv + 3.11 固定。依存は `pyproject.toml` と `uv.lock` で管理します。
- Secrets や API キーは GitHub Secrets あるいはローカルの非公開 `.env.local` に保持し、リポジトリに直書きしません。

## ローカル実行手順
1. 必要な環境変数（`GEMINI_API_KEY`, `BUTTONDOWN_API_KEY` など）を `export KEY=value` で設定するか、`.env.local`（Git で無視）を `source` して読み込む。
2. 依存インストール: `uv sync`.
3. ニュースレター生成＋配信: `uv run python scripts/run_pipeline.py`.
   - ドラフト送信で止める場合は `BUTTONDOWN_STATUS=draft` を環境変数として渡す。

## テスト
- PubMed クライアントとニュースレタージェネレータの単体テストを `pytest` で提供（`uv run pytest`）。
- 今後 Gemini / Buttondown をモック化した統合テストも追加予定。

## CI/CD
- `.github/workflows/newsletter-buttondown.yml` が毎週月曜 00:00 UTC に実行:
  1. `uv sync --frozen`
  2. `uv run pytest`
  3. `uv run python scripts/run_pipeline.py`
  4. `issues/` の差分を自動コミット

## 今後のロードマップ
1. PubMed クエリ改善とレート制御
2. Gemini プロンプト／テンプレのチューニング
3. Buttondown API のドラフト運用とログ拡充
4. GitHub Actions のリトライ・監視整備
5. 追加データソース（arXiv / Semantic Scholar）の連携
