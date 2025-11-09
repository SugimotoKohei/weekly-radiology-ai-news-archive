# 実験ノート

## 2025-11-07
- リポジトリ初期化方針を確認し、`docs/studyplan.md` を作成してフェーズ別タスクを整理。
- `docs/studynote.md` を開設し、以後の作業ログ格納場所を決定。

### 2025-11-07 追加
- `UV_CACHE_DIR` をプロジェクト直下に設定し `uv init --python 3.11` を実行。`pyproject.toml` / `.python-version` / `main.py` を生成。
- `issues/` ディレクトリと README 骨子を用意し、開発方針と Secrets を記述。
- `docs/studyplan.md` に詳細設計セクション (8.x) を追記。データ取得・Gemini 要件・Buttondown 配信・CI 設計を明文化。
- `src/` と `scripts/` ディレクトリを追加して実装準備。
- `uv add requests python-dateutil markdown` を実行し、基礎依存を `pyproject.toml` / `uv.lock` に反映。
- `docs/studyplan.md` に直近タスク一覧 (Section 9) を追加し、次フェーズの実装順を固定。

### 2025-11-07 実装
- `src/pubmed_client.py` を実装し、PubMed E-utilities から ID 検索・詳細取得・データ整形を実現。
- フィクスチャ `tests/fixtures/pubmed_sample.xml` と `tests/test_pubmed_client.py` を追加し、スタブセッションによる単体テストを通過 (`uv run pytest`)。
- pytest を dev 依存に追加し、`uv lock` を更新。

### 2025-11-07 進捗
- `src/newsletter_generator.py` に Gemini 呼び出しとセクション検証ロジックを実装。
- `src/buttondown_client.py` を追加し、`status` 切り替えと API 送信処理を定義。
- `src/pipeline.py` / `scripts/run_pipeline.py` を実装し、PubMed→LLM→Buttondown→issues 保存の一連フローを構築。
- GitHub Actions (`.github/workflows/newsletter-buttondown.yml`) を作成し、uv sync→pytest→パイプライン実行→自動コミットを設定。
- README にローカル実行手順と Secrets 追記。

## 2025-11-08
- `uv run pytest` を実行し、PubMed クライアントの既存テスト 2 件が通過することを確認。
- `src/newsletter_generator.py` の `REQUIRED_SECTIONS` 文字化けを把握し、Gemini 出力バリデーションの不具合を確認。
- README や `docs/studyplan.md` などドキュメントにも同様の文字化けが残っていたため、UTF-8 化と内容更新の必要性を整理。
- Buttondown / Gemini 連携のモック化テストや E2E チェックが未着手のため、次タスク候補として優先度を検討。
### 2025-11-08 実装
- `src/newsletter_generator.py` を UTF-8 で書き直し、システムプロンプトと必須セクションを正常化。`REQUIRED_SECTIONS` の検証を保守しやすい形にした。
- README / `docs/studyplan.md` / `docs/studynote.md` を全面的に書き直し、現在のアーキテクチャとルールを明文化。
- `.gitignore` の誤記（`.DS_Store__pycache__/`）を修正し、`.env.sample` を追加してローカル実行手順と整合させた。
- `tests/test_newsletter_generator.py` を追加し、セクション検証ロジックの正負ケースをカバー。
- `src/pipeline.py` の `BUTTONDOWN_STATUS` 取り扱いを `EmailStatus` にキャストする形へ修正し、`type: ignore` を解消。
- `uv run pytest` を再実行し、新規テストを含む 4 件が通過することを確認。
- `config/newsletter_template.yaml` を新設し、system/user プロンプト・必須セクション・温度などを外部化。`NEWSLETTER_TEMPLATE_PATH` で差し替え可能にした。
- `src/newsletter_generator.py` をテンプレート読み込み対応へ刷新し、`NewsletterTemplate` dataclass を導入。PyYAML 依存を追加。
- `src/pipeline.py` でテンプレートファイルをロードしてからジェネレータを初期化するよう更新。
- `.env.sample` に `NEWSLETTER_TEMPLATE_PATH` を追記し、README/plan にテンプレ構成の説明を反映。
- `tests/test_newsletter_generator.py` にテンプレ読込テストと定義チェックを追加し、設定ファイル破損を早期発見できるようにした。
- `uv run pytest` を再実行し、追加テストを含めて 5 件が通過することを確認。
- GitHub Actions の workflow に `NEWSLETTER_TEMPLATE_PATH` を明示し、Secrets（GEMINI/PUBMED/BUTTONDOWN）を使って定期実行できる状態を確認。
### 2025-11-08 Actions対応
- GitHub Actions で `ModuleNotFoundError: src` が発生したため、`scripts/run_pipeline.py` にプロジェクトルートを `sys.path` へ追加する処理を挿入し、CI/ローカルの双方で同一エントリポイントを利用可能にした。
- 修正後 `uv run pytest` を再実行し、全テスト成功を確認。
### 2025-11-08 再修正
- CI 実行時に `buttondown_client` モジュールが解決できなかったため、`scripts/run_pipeline.py` で `PROJECT_ROOT/src` も `sys.path` に追加するよう修正。
- `uv run pytest` を再実行し、すべてのテストが成功することを確認。
