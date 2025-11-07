# CT/MRI×AI Weekly Archive (WIP)

## コンセプト
- CT/MRI を用いた医用画像 AI（segmentation / detection / classification / reconstruction 等）の新着論文を毎週自動収集。
- Gemini API で Weekly Kaggle News 風の日本語ダイジェストを生成し、Buttondown ニュースレターとして自動配信。
- 生成した Markdown を GitHub `issues/` ディレクトリに保存し、バックナンバーを検索可能にする。

## 目標アーキテクチャ
1. **データ収集**: PubMed E-utilities（必要に応じて arXiv / RSS を追加）。
2. **要約生成**: Gemini 1.5 Pro API。テンプレ（Top Picks / Method / Dataset / Review / 編集後記）固定。
3. **配信**: Buttondown REST API (`POST /v1/emails`) で即時送信 or ドラフト作成。
4. **自動化**: GitHub Actions (cron + workflow_dispatch) で週次実行、`issues/` の diff を自動コミット。

## 使用技術
- Python 3.11（uv 管理）
- requests / python-dateutil / markdown
- GitHub Actions
- Buttondown API / Gemini API / PubMed E-utilities

## ディレクトリ方針
```
.
├── docs/
│   ├── studyplan.md   # 実験計画（本ファイルに従って作業）
│   └── studynote.md   # 進捗・検証ログ
├── issues/            # 自動生成される各号の Markdown
├── scripts/           # ローカル実行用スクリプト（予定）
├── src/               # 実装コード（予定）
└── .github/workflows/ # CI/CD（newsletter-buttondown.yml 予定）
```

## Secrets / 設定 (予定)
| 名前 | 用途 |
| --- | --- |
| `GEMINI_API_KEY` | Gemini API 呼び出し |
| `PUBMED_API_KEY` | PubMed レート制限緩和（任意） |
| `BUTTONDOWN_API_KEY` | Buttondown メール送信 |
| `BUTTONDOWN_STATUS` | `sent` / `draft`（任意。未設定時は `sent`） |
| `PUBMED_QUERY` | 既定クエリを上書きする場合（任意） |
| `PUBMED_RELDAYS` / `PUBMED_RETMAX` | 取得期間 / 件数の上書き（任意） |

## 実験ルール
- すべての検証は `docs/studyplan.md` に沿って進め、結果・気付きは `docs/studynote.md` に追記。
- Python 実行環境は uv + 3.11 固定。依存は `pyproject.toml` / `uv.lock` で管理。
- 外部 API キーやシークレットは GitHub Secrets のみで扱い、リポジトリに平文保存しない。

## ローカル実行
1. 環境変数を設定（例: `cp .env.sample .env` を将来追加予定 / 直接 `export` でも可）。
2. 依存インストール: `uv sync`.
3. ニュースレター生成＆配信: `uv run python scripts/run_pipeline.py`.
   - Buttondown をドラフトで止めたい場合は `BUTTONDOWN_STATUS=draft` を指定。

## テスト
- PubMed クライアント中心のユニットテストを `pytest` で提供。`uv run pytest` で実行。
- 今後は Gemini/ Buttondown をモック化した統合テストも追加予定。

## CI/CD
- `.github/workflows/newsletter-buttondown.yml` で週次（月曜00:00 UTC）に以下を実施:
  1. uv で依存解決
  2. `pytest`
  3. `scripts/run_pipeline.py` を実行（APIキーは GitHub Secrets から注入）
  4. `issues/` の差分を自動コミット

## 今後のロードマップ
1. uv で Python プロジェクト初期化、基本依存を追加。
2. PubMed クライアント実装とユニットテスト。
3. Gemini プロンプトテンプレ設計＆検証。
4. Buttondown API 連携スクリプト実装。
5. GitHub Actions ワークフロー作成。
6. モニタリング・拡張計画（追加データソース、ランキング、アナリティクスなど）。
