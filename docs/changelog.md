# 変更ログ

## 2025-12-14
- `docs/plan.md` を追加し、ニュースレター自動送信用途の運用計画（目的/入力/出力/実行パス/環境変数）を記載した。
- `docs/changelog.md` を運用変更ログとして整備した。
- `config/` を `configs/` に移行し、テンプレートを `configs/base/newsletter_template.yaml` に配置して参照先（`src/newsletter_generator.py` と `.github/workflows/newsletter-buttondown.yml`）を更新した。
- `.gitignore` を標準セットに更新し、`output/`・`data/`・`configs/local/` などの非Git管理領域を明示した。
- ルートの雛形 `main.py` を削除し、実行入口を `scripts/run_pipeline.py` に一本化した。
- `UV_CACHE_DIR=.uv-cache uv run pytest` を実行し、全テスト（6件）が通過することを確認した。
- notebook/marimo 前提の設定・記述を削除し、リポジトリの目的を「自動送信プログラム」に寄せた。
- `uv.toml` を追加し、`uv` のキャッシュをリポジトリ配下（`.cache/uv`）へ固定して `uv run` が素のまま動くようにした。
- GitHub Actions を `BUTTONDOWN_STATUS=draft` 固定にし、CI 上での誤送信をガードするため `BUTTONDOWN_ALLOW_ACTIONS_SEND` を導入した。
- `scripts/run_pipeline.py` に `--dry-run` を追加し、API キーなしで `issues/_dry_run_*.md` を生成して動作確認できるようにした。
- `issues/_dry_run_*.md` が誤ってコミットされないよう `.gitignore` に追加した。
- LLM 出力の必須セクション検証を、見出し表記ゆれ（例: `今週のTop Picks`, `Dataset/Benchmark`）に強くした。
- `configs/base/newsletter_template.yaml` の system prompt を修正し、固定見出しを `## ` 付きで出力するよう明示した。

## 2025-11-08
- `uv run pytest` を実行し、PubMed クライアントの既存テスト 2 件が通過することを確認した。
- `src/newsletter_generator.py` の `REQUIRED_SECTIONS` 文字化けを把握し、Gemini 出力バリデーションの不具合を確認した。
- README や当時の計画ドキュメントにも同様の文字化けが残っていたため、UTF-8 化と内容更新の必要性を整理した。
- Buttondown / Gemini 連携のモック化テストや E2E チェックが未着手のため、次タスク候補として優先度を検討した。
- `src/newsletter_generator.py` を UTF-8 で書き直し、システムプロンプトと必須セクションを正常化して `REQUIRED_SECTIONS` の検証を保守しやすい形にした。
- README / 計画ドキュメント / 変更ログを更新し、当時のアーキテクチャとルールを明文化した。
- `.gitignore` の誤記を修正し、ローカル実行手順との整合を取った。
- `tests/test_newsletter_generator.py` を追加し、セクション検証ロジックの正負ケースをカバーした。
- `src/pipeline.py` の `BUTTONDOWN_STATUS` 取り扱いを `EmailStatus` にキャストする形へ修正し、`type: ignore` を解消した。
- `uv run pytest` を再実行し、新規テストを含む 4 件が通過することを確認した。
- `config/newsletter_template.yaml` を新設し、system/user プロンプト・必須セクション・温度などを外部化して `NEWSLETTER_TEMPLATE_PATH` で差し替え可能にした。
- `src/newsletter_generator.py` をテンプレート読み込み対応へ刷新し、`NewsletterTemplate` dataclass を導入し、PyYAML 依存を追加した。
- `src/pipeline.py` でテンプレートファイルをロードしてからジェネレータを初期化するよう更新した。
- `tests/test_newsletter_generator.py` にテンプレ読込テストと定義チェックを追加し、設定ファイル破損を早期発見できるようにした。
- `uv run pytest` を再実行し、追加テストを含めて 5 件が通過することを確認した。
- GitHub Actions の workflow に `NEWSLETTER_TEMPLATE_PATH` を明示し、Secrets（GEMINI/PUBMED/BUTTONDOWN）を使って定期実行できる状態を確認した。
- GitHub Actions で `ModuleNotFoundError: src` が発生したため、`scripts/run_pipeline.py` にプロジェクトルートを `sys.path` へ追加する処理を挿入した。
- CI 実行時に `buttondown_client` モジュールが解決できなかったため、`scripts/run_pipeline.py` で `PROJECT_ROOT/src` も `sys.path` に追加するよう修正した。
- `src` 内モジュール参照の import エラー再発に対応するため、`src/pipeline.py` / `src/newsletter_generator.py` の参照形式を見直した。
- `.github/workflows/newsletter-buttondown.yml` の pipeline ステップで `PYTHONPATH` にリポジトリルートと `src` を追加し、GitHub Actions 実行時の import パスを固定した。
- CI 上の import 安定化のため、`src/pipeline.py` と `src/newsletter_generator.py` の内部参照を `from src.*` 形式の絶対インポートに変更した。
- PubMed E-utilities が 400 を返していた原因が Secrets の末尾タブ/改行であることを特定し、`PubMedClient` で `api_key.strip()` を行うよう修正した。
- Gemini API の失敗（例: 404）に備え、`NewsletterGenerator.generate` の再試行後にフォールバック Markdown を生成するよう変更した。
- `.env.sample` を削除し、API キーは GitHub Secrets / ローカル非公開 `.env.local` のみに保持する方針へ切り替えた。
- README と計画ドキュメントを更新し、ローカル実行手順から `.env.sample` への依存を除去した。
- `.gitignore` に `.env*` を追加し、誤ってコミットしないようにした。
- `GEMINI_MODEL` 環境変数でモデル名を切り替えられるようにし、デフォルトを `gemini-2.5-flash` に変更した（`src/newsletter_generator.py`）。
- `PUBMED_FALLBACK_RELDAYS`（既定30日）を導入し、直近期間で論文が0件でも期間を広げて再検索するよう `src/pipeline.py` を更新した。
- Buttondown API 失敗時のレスポンス本文を表示するよう `ButtondownClient` を更新した。
- `pipeline.py` は送信失敗時に例外を再送出し、必ずエラーとして検知できるようにした。
- Buttondown API の有効ステータスを Literal に反映し、デフォルトを `draft` に変更した。

## 2025-11-07
- リポジトリ初期化方針を確認し、計画ドキュメントを作成してフェーズ別タスクを整理した。
- 変更ログを開設し、以後の作業ログ格納場所を決定した。
- `UV_CACHE_DIR` をプロジェクト直下に設定し `uv init --python 3.11` を実行し、`pyproject.toml` / `.python-version` / `main.py` を生成した。
- `issues/` ディレクトリと README 骨子を用意し、開発方針と Secrets を記述した。
- 計画ドキュメントに詳細設計セクションを追記し、データ取得・Gemini 要件・Buttondown 配信・CI 設計を明文化した。
- `src/` と `scripts/` ディレクトリを追加して実装準備をした。
- `uv add requests python-dateutil markdown` を実行し、基礎依存を `pyproject.toml` / `uv.lock` に反映した。
- 計画ドキュメントに直近タスク一覧を追加し、次フェーズの実装順を固定した。
- `src/pubmed_client.py` を実装し、PubMed E-utilities から ID 検索・詳細取得・データ整形を実現した。
- フィクスチャ `tests/fixtures/pubmed_sample.xml` と `tests/test_pubmed_client.py` を追加し、スタブセッションによる単体テストが通過することを確認した（`uv run pytest`）。
- pytest を dev 依存に追加し、`uv lock` を更新した。
- `src/newsletter_generator.py` に Gemini 呼び出しとセクション検証ロジックを実装した。
- `src/buttondown_client.py` を追加し、`status` 切り替えと API 送信処理を定義した。
- `src/pipeline.py` / `scripts/run_pipeline.py` を実装し、PubMed→LLM→Buttondown→issues 保存の一連フローを構築した。
- GitHub Actions（`.github/workflows/newsletter-buttondown.yml`）を作成し、`uv sync`→`pytest`→パイプライン実行→自動コミットを設定した。
- README にローカル実行手順と Secrets を追記した。
