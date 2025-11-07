# 実験計画: CT/MRI×AI Weekly 自動化リポジトリ

## 1. 目的
- PubMed 等から CT/MRI×AI 論文を自動収集し、Gemini API で週刊ニュースレターを生成する。
- Buttondown API を用いてメルマガを自動配信し、Markdown を GitHub 上にアーカイブする。
- すべての処理を Python 3.11 (+ uv) と GitHub Actions で統合し、運用コストを最小化する。

## 2. フェーズ別マイルストーン
| フェーズ | ゴール | 検証観点 |
| --- | --- | --- |
| P1 基盤整備 | ディレクトリ構成、uv/pyproject、README、ドキュメント整備 | ファイル構造、開発ルールが明文化されているか |
| P2 データ取得 | PubMed E-utilities クライアント実装、クエリ調整 | retmax/日付範囲の挙動、メタデータ欠損耐性 |
| P3 生成パイプライン | Gemini プロンプト設計、Markdown バリデーション | セクション完全性、LLM 再試行戦略 |
| P4 配信統合 | Buttondown API 連携、Secrets 設計 | API キー管理、配信結果ログ |
| P5 CI/CD | GitHub Actions で週次実行、issues/ 自動コミット | 冪等性、失敗時リトライ | 
| P6 QA/監視 | テスト、モニタリング、今後の拡張計画 | ログ可視化、フォールバック動作 |

## 3. タスクと依存関係
1. **基盤整備**: README テンプレ更新、docs 管理、uv プロジェクト初期化。
2. **データ取得モジュール**: `pubmed_client.py` (予定) 作成、サンプルレスポンス検証。
3. **要約生成**: Gemini プロンプトファイル、検証スクリプト、Markdown 構文チェック。
4. **配信モジュール**: Buttondown API ラッパ、ドラフト送信テスト。
5. **パイプライン統合**: `pipeline.py` で全処理連結、設定ファイル化。
6. **CI/CD**: `.github/workflows/newsletter-buttondown.yml` 作成、Secrets 定義。
7. **QA/運用**: ログ整備、エラーアラート方針、拡張計画ドキュメント化。

## 4. 検証計画
- **機能テスト**: 各モジュールを pytest で単体検証。Mock を用い API 呼び出しを再現。
- **統合テスト**: Buttondown をモックするスクリプトで E2E 実行。Sandbox で実メール送信は制限付き実行。
- **回帰テスト**: クエリやテンプレ変更時に regression data を `tests/fixtures` に保存。

## 5. 成果物
- `README.md`: コンセプト、アーキテクチャ、運用手順、Secrets 一覧。
- `docs/studynote.md`: 実験ログ（日時、操作、結果、課題）。
- ソース群（後続フェーズで作成）。

## 6. リスクと対策
- **LLM 出力揺らぎ**: セクション検証ロジック＋リトライ。
- **API レート制限**: PubMed/Pipelines で retmax 調整、キャッシュ機構を将来導入。
- **Buttondown 無料枠超過**: `docs/studynote.md` に購読者推移を記録し、100人超で早期対応。
- **Secrets 漏えい**: `.env` 禁止、GitHub Secrets のみ使用し README で明文化。

## 7. 次アクション
- 本計画に基づき README 骨子および uv プロジェクト初期化を実施。
- 実施内容・結果は `docs/studynote.md` に逐次記録する。

## 8. 詳細設計（WIP）

### 8.1 データ取得モジュール要件
- **入力**: クエリ文字列、取得期間（日数）、最大件数、APIキー（任意）。
- **処理**:
  - PubMed E-utilities `esearch` で PMIDs を取得（`reldate=7`, `retmax<=50` を初期設定）。
  - `efetch` (XML) をパースし、以下のフィールドを抽出: `pmid`, `title`, `abstract`, `journal`, `pub_year`, `authors[<=3]`, `link`.
  - 欠損時は空文字で許容、呼び出し元に例外を投げない。
- **出力**: 上記フィールドを持つ dict のリスト。後段に渡すため JSON シリアライズ可能であること。
- **検証**: pytest でモックレスポンスを用いたユニットテストを作成（`tests/test_pubmed_client.py`予定）。

### 8.2 LLM ニュースレター生成要件
- **モデル**: `gemini-1.5-pro-latest`、Free Tier を想定。API キーは `GEMINI_API_KEY`。
- **プロンプト**:
  - system: 役割・セクション構成・必須要素（タスク/データ/手法/指標/So what/limitation）を固定。
  - user: 実行日と JSON 化した論文リストを渡す。
- **出力検証**:
  - Markdown 全文を受け取り、Top Picks / Method Spotlight / Dataset / Review / 編集後記のセクションが存在するか簡易チェック。
  - 不足時は最大 2 回まで再試行。失敗した場合は例外を raise し、Actions を失敗させる。
- **設定**: `temperature=0.2` で deterministic に寄せる。今後 `config/newsletter_template.yaml` で調整可能にする。

### 8.3 Buttondown 配信要件
- **API**: `POST https://api.buttondown.com/v1/emails`
  - headers: `Authorization: Token $BUTTONDOWN_API_KEY`
  - body: `subject`, `body` (Markdown), `status`（初期は `"sent"`）。
- **失敗対応**: ステータスコードが 300 以上の場合は例外を投げて停止。Logs で応答本文を確認できるよう出力。
- **未来対応**: `status="draft"` + `/send-draft` にも切り替えられるよう関数パラメータ化。

### 8.4 パイプライン統合
- **ファイル**: `pipeline.py`
- **順序**:
  1. JST 現在日付を取得し `today_str` を生成。
  2. データ取得モジュールで論文リスト作成（0 件なら終了）。
  3. LLM で Markdown 生成。
  4. `issues/` に `YYYY-MM-DD_ct-mri-ai-weekly-XXX.md` を保存。
  5. Buttondown API へ送信。
  6. stdout に件数・ファイルパス・送信結果を記録。
- **設定注入**: すべて環境変数経由。ローカルテスト用に `.env.sample` を将来追加予定（Secrets は記述しない）。

### 8.5 GitHub Actions 設計
- **Workflow**: `.github/workflows/newsletter-buttondown.yml`
  - `schedule`: `0 0 * * MON`（UTC）＋ `workflow_dispatch`.
  - ランナー: `ubuntu-latest`; Python セットアップ後 `uv run python pipeline.py` を想定。
  - Secrets: `GEMINI_API_KEY`, `PUBMED_API_KEY`, `BUTTONDOWN_API_KEY`.
  - 成果物: `issues/` の変更があればコミットメッセージ `[Automated] Update CT/MRI×AI Weekly archive`.
- **ログ方針**: 各ステップの `[INFO]` ログで追跡。失敗時は GitHub 通知をトリガ。

### 8.6 将来の拡張ポイント
- arXiv / Semantic Scholar API 追加時は `sources/` ディレクトリにモジュールを分離。
- Buttondown の購読者 100 人超過時に備え、Mailchimp 等への切り替えアダプタを `services/` 以下に実装予定。
- 出力検証を強化するため `markdown-it-py` などの構文解析導入を検討。

## 9. 直近タスクリスト
1. `pyproject.toml` へ基礎依存（requests / python-dateutil / markdown）を追加済み。次は `uv lock` を確定し、CI で再現性を確認。
2. `src/pubmed_client.py`（仮）と `tests/test_pubmed_client.py` を作成し、XML → dict 変換をユニットテスト。
3. `src/newsletter_generator.py` に Gemini 呼び出しラッパを実装し、Markdown セクション検証ヘルパを同ファイルに含める。
4. `src/buttondown_client.py` を実装し、`status=sent` と `status=draft` の両モードを引数で切り替えられるようにする。
5. `pipeline.py` を `src/` に移してモジュール構成を整理（例: `src/pipeline.py` で main 関数、`scripts/run_pipeline.py` でエントリポイント）。
6. `.github/workflows/newsletter-buttondown.yml` を作り、Secrets の受け渡しと `uv run` 実行を実装。
