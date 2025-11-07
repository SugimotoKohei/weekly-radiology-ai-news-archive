# 実験ノート

## 2025-11-07
- リポジトリ初期化方針を確認。`docs/studyplan.md` を作成し、フェーズ別タスクを整理。
- `docs/studynote.md` を開設。以後の作業ログと検証結果は本ファイルに追記する。
### 2025-11-07 追加
- `UV_CACHE_DIR` をプロジェクト直下に指定して `uv init --python 3.11` を実行。`pyproject.toml` / `.python-version` / `main.py` を生成。
- `issues/` ディレクトリと README 骨子を用意し、開発方針と Secrets を明文化。
- `docs/studyplan.md` に詳細設計セクション (8.x) を追記。データ取得・Gemini 要約・Buttondown 配信・CI 設計の要件を明確化。
- `src/` と `scripts/` ディレクトリを作成し、実装着手準備を整備。
- `uv add requests python-dateutil markdown` を実行し、基礎依存を pyproject/uv.lock に反映（Buttondown/Gemini クライアント実装の前準備）。
- `docs/studyplan.md` に直近タスクリスト (Section 9) を追加し、次フェーズでの実装順序を固定。
### 2025-11-07 実装
- `src/pubmed_client.py` を実装し、PubMed E-utilities から ID 検索・詳細取得・データ整形をカバー。
- フィクスチャ `tests/fixtures/pubmed_sample.xml` と `tests/test_pubmed_client.py` を追加し、スタブセッションで単体テスト（uv run pytest）を通過。
- pytest を dev 依存に追加し、`uv lock` を再生成。
### 2025-11-07 進捗
- `src/newsletter_generator.py` に Gemini 呼び出し＋セクション検証を実装。
- `src/buttondown_client.py` を追加し、`status` 切替と API 送信処理を定義。
- `src/pipeline.py` / `scripts/run_pipeline.py` を実装し、PubMed→LLM→Buttondown→issues 保存の一連フローを構築。
- GitHub Actions (`.github/workflows/newsletter-buttondown.yml`) を作成し、uv sync→pytest→パイプライン実行→自動コミットを設定。
- README にローカル実行・テスト・Secrets 追加情報を追記。
