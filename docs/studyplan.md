# 実験計画: CT/MRI×AI Weekly 自動化リポジトリ

## 1. 目的
- PubMed 等から CT/MRI×AI 関連論文を自動収集し、Gemini API で週刊ニュースレターを生成する。
- Buttondown API でメール配信し、Markdown 版を GitHub `issues/` にアーカイブする。
- Python 3.11（uv 管理）と GitHub Actions を用いて運用コストを最小化する。

## 2. フェーズ別マイルストーン
| フェーズ | ゴール | 検証観点 |
| --- | --- | --- |
| P1 基盤整備 | ディレクトリ構成、uv/pyproject、README、ドキュメント整備 | ファイル構造・開発ルールが明文化されている |
| P2 データ取得 | PubMed クライアント実装とクエリ調整 | retmax / 日付範囲の挙動、メタデータ欠損耐性 |
| P3 生成パイプライン | Gemini プロンプト設計、Markdown バリデーション | セクション完備性、LLM 再試行戦略 |
| P4 配信統合 | Buttondown API 連携、Secrets 設計 | API キー管理、送信結果ログ |
| P5 CI/CD | GitHub Actions による週次実行 | 冪等性、失敗時リトライ |
| P6 QA/監視 | チェックリスト、モニタリング、拡張計画 | ログ可視化、フォールバック動作 |

## 3. タスクと依存関係
1. **基盤整備**: README テンプレ更新、docs 管理、uv プロジェクト初期化。
2. **データ取得**: `pubmed_client.py` 実装、サンプルレスポンス検証。
3. **要約生成**: Gemini プロンプトファイル、検証スクリプト、Markdown 構文チェック。
4. **配信モジュール**: Buttondown API ラッパー、ドラフト送信サポート。
5. **パイプライン統合**: `pipeline.py` で全処理を結合、設定ファイル化。
6. **CI/CD**: `.github/workflows/newsletter-buttondown.yml` 作成、Secrets 定義。
7. **QA/運用**: ログ整備、エラーアラート方針、拡張計画ドキュメント化。

## 4. 検証計画
- **機能テスト**: 各モジュールを pytest で単体検証、mock を用いて API 呼び出しを再現。
- **統合テスト**: Buttondown をモックするスクリプトで E2E 実行。Sandbox では実メール送信を制限。
- **回帰テスト**: クエリ／テンプレ変更時に regression data を `tests/fixtures` に保存。

## 5. 成果物
- `README.md`: コンセプト、アーキテクチャ、運用手順、Secrets 一覧。
- `docs/studynote.md`: 実験ログ（日時・操作・結果・課題）。
- 主要ソースコード（`src/`）、テスト（`tests/`）、スクリプト、ワークフロー。

## 6. リスクと対策
- **LLM 出力揺らぎ**: セクション検証ロジック＋リトライを実装。
- **API レート制限**: PubMed で retmax 調整、キャッシュ導入を検討。
- **Buttondown 無料枠超過**: `docs/studynote.md` に購読者推移を記録し、100人超で早期対応。
- **Secrets 漏えい**: API キーは GitHub Secrets またはローカルの非公開 `.env.local` に保持し、レポジトリには一切含めない。

## 7. 次アクション
- 本計画に基づき README 骨子および uv プロジェクト初期化を完了する。
- 実施内容・結果は `docs/studynote.md` に逐次記録する。

## 8. 詳細設計
### 8.1 データ取得モジュール要件
- **入力**: クエリ文字列、取得期間（日数）、最大件数、API キー（任意）。
- **処理**:
  - PubMed `esearch` で PMID を取得（既定: `reldate=7`, `retmax<=50`）。
  - `efetch` (XML) をパースし、`pmid`, `title`, `abstract`, `journal`, `pub_year`, `authors[<=3]`, `link` を抽出。
  - 欠損は空文字で許容し、致命的エラー以外は例外を投げない。
- **出力**: 上記フィールドを持つ dict のリスト（JSON シリアライズ可能）。
- **検証**: pytest でモックしたレスポンスを用いてユニットテスト（`tests/test_pubmed_client.py`）。

### 8.2 LLM ニュースレター生成要件
- **モデル**: `gemini-1.5-pro-latest`。API キーは `GEMINI_API_KEY`。
- **プロンプト**:
  - system: 役割・セクション構成・要素（Task/Data/Method/So what/Limitation）を固定。`config/newsletter_template.yaml` で集中管理。
  - user: 実行日と JSON 化した論文リストを渡す。テンプレート内の `{today}`, `{top_picks_max}`, `{papers_json}` プレースホルダで制御。
- **出力検証**:
  - Markdown 全体から Top Picks / Method / Dataset / Review / 編集後記の見出しを探索。
  - 不足時は最大2回まで再試行。失敗で例外→Actions を失敗させる。
- **設定**: `temperature=0.2`（テンプレートファイルで上書き可）。
- **モデル切替**: `GEMINI_MODEL` 環境変数で任意のモデル（例: `gemini-2.5-pro`）に変更可能。未設定時は `gemini-2.5-flash`。

### 8.3.1 PubMed フォールバック検索
- **目的**: 直近期間で論文が0件のときも Gemini 生成まで進める。
- **動作**: `PUBMED_FALLBACK_RELDAYS`（既定:30日）を参照し、最初の検索が空なら自動で期間を広げて再試行。
- **設定**: `PUBMED_RELDAYS` より小さい値が指定された場合は自動的に無視される。

### 8.3 Buttondown 配信要件
- **API**: `POST https://api.buttondown.com/v1/emails`
  - headers: `Authorization: Token $BUTTONDOWN_API_KEY`, `Content-Type: application/json`
  - body: `subject`, `body` (Markdown), `status`（既定 `sent`）
- **失敗対策**: ステータスコード 300 以上で例外。レスポンス本文をログ出力。
- **ステータス**: 新規メールでは `draft` / `about_to_send` / `scheduled` / `imported` / `transactional` が有効（既定: `draft`）。
- **未来拡張**: `status="draft"` + `/send-draft` をパラメータで切り替え可能にする。

### 8.4 パイプライン統合
- **ファイル**: `src/pipeline.py`
- **処理手順**:
  1. JST 現在日付を取得し `today_str` を生成。
  2. PubMed クライアントで論文リストを取得（0件なら終了）。
  3. LLM で Markdown を生成。
  4. `issues/` に `YYYY-MM-DD_ct-mri-ai-weekly-XXX.md` を保存。
  5. Buttondown API へ送信。
  6. stdout に件数・ファイルパス・送信結果を記録。
- **設定注入**: すべて環境変数経由。ローカルでは `.env.local`（Git 忽）やシェル `export` で設定し、Secrets をリポジトリに含めない。

### 8.5 GitHub Actions 設計
- **Workflow**: `.github/workflows/newsletter-buttondown.yml`
  - `schedule`: `0 0 * * MON`（UTC）＋ `workflow_dispatch`
  - Runner: `ubuntu-latest`
  - `uv run python pipeline.py` を想定
  - Secrets: `GEMINI_API_KEY`, `PUBMED_API_KEY`, `BUTTONDOWN_API_KEY`
  - 成果物: `issues/` の変更があればコミット `"[Automated] Update CT/MRI×AI Weekly archive"`

### 8.6 拡張ポイント
- arXiv / Semantic Scholar API を追加する際は `sources/` ディレクトリでモジュール分離。
- Buttondown 100人超を想定し、Mailchimp 等へ切り替え可能なアダプタを `services/` 以下に用意。
- Markdown 構文検証強化のため `markdown-it-py` 等の導入を検討。

## 9. 直近タスク
1. `pyproject.toml` の依存（requests / python-dateutil / markdown）を固定し `uv lock` を確定。
2. `src/pubmed_client.py` と `tests/test_pubmed_client.py` を整備し、XML→dict 変換をユニットテスト。
3. `src/newsletter_generator.py` に Gemini 呼び出し＋セクション検証を実装。
4. `src/buttondown_client.py` を実装し、`status` 切り替えと API 送信処理を定義。
5. `src/pipeline.py`（および `scripts/run_pipeline.py`）で PubMed→LLM→Buttondown→issues 保存を構築。
6. `.github/workflows/newsletter-buttondown.yml` を作成し、Secrets 受け渡しと `uv run` 実行を実装。
