## 今週の Top Picks

### Performance of AI vs radiology residents in the detection of intracranial hemorrhage on emergency CT: a real-world analysis. (PMID: [41721849](https://pubmed.ncbi.nlm.nih.gov/41721849/))
*   **雑誌名**: European radiology
*   **公開日**: 2026-02-21
*   **著者名**: Quentin Pedrini, Periktioni Crina Chrysostomou, Pierre-Alexandre Poletti 他
*   **所属**: Division of Radiology, Diagnostic Department, Geneva University Hospitals, Geneva, Switzerland 他
*   **タスク**: 救急CTにおける頭蓋内出血 (ICH) の検出
*   **データ**: 単一施設で3ヶ月間に実施された2153件の非造影頭部CTスキャン。ICHの有病率は15.4%。
*   **手法**: 市販のAIソフトウェアと、当直放射線科レジデントの診断性能を比較。ボード認定放射線科医の最終レポートをリファレンス標準とし、AIの結果は放射線科医には非公開とした。
*   **成果**: AIは全体で感度84%、特異度94.4%であったのに対し、放射線科レジデントは感度96.4%、特異度99.6%と有意に高い性能を示した (p < 0.001)。AIは複数の出血部位や出血タイプが存在する場合にのみ、非常に良好な診断性能を示した。
*   **新規性**: 実世界の救急ワークフロー条件下で、市販AIと放射線科レジデントのICH検出性能を直接比較し、AIがレジデントに劣るという結果を示した点。これはAI導入の慎重な検討を促す重要な知見です。
*   **限界**: 単一施設での評価であり、AIソフトウェアの一般化可能性や他の施設での性能は不明。

### Hallucination filtering in radiology vision-language models using discrete semantic entropy. (PMID: [41720937](https://pubmed.ncbi.nlm.nih.gov/41720937/))
*   **雑誌名**: European radiology
*   **公開日**: 2026-02-20
*   **著者名**: Patrick Wienholt, Sophie Caselitz, Robert Siepmann 他
*   **所属**: Lab for Artificial Intelligence in Medicine, Department of Diagnostic and Interventional Radiology, University Hospital RWTH Aachen, Aachen, Germany 他
*   **タスク**: 放射線画像ベースのVQA (Visual Question Answering) におけるブラックボックスVLM (Vision-Language Models) のハルシネーション検出と精度向上
*   **データ**: VQA-Med 2019ベンチマーク (500画像) と診断放射線データセット (206症例: CT, MRI, X線, アンギオグラム)
*   **手法**: GPT-4oとGPT-4.1を使用し、離散的意味エントロピー (DSE) を用いてハルシネーションを生成しやすい質問を拒否する戦略を評価。DSEは、高温度設定で複数回生成された回答の意味的矛盾を定量化する。
*   **成果**: DSEフィルタリング (DSE > 0.3) により、GPT-4oの精度は51.7%から76.3%に、GPT-4.1は54.8%から63.8%に向上した (両者ともp < 0.001)。精度向上は両データセットで観察され、統計的有意性を維持した。
*   **新規性**: ブラックボックスVLMにおけるハルシネーションを、意味的矛盾を定量化するDSEを用いて信頼性高く検出・フィルタリングする手法を提案し、診断回答精度を大幅に改善した点。これはAIの安全な臨床利用に不可欠な要素です。
*   **限界**: フィルタリングにより回答できる質問数が減少する。DSE閾値の設定が性能に影響を与える可能性がある。

### Self-supervised out-of-distribution detection-Metal implants and other anomaly. (PMID: [41719005](https://pubmed.ncbi.nlm.nih.gov/41719005/))
*   **雑誌名**: Medical physics
*   **公開日**: 2026-02
*   **著者名**: Gokul Ramasamy, Amara Tariq, Samuel J Fahrenholtz 他
*   **所属**: AI & Informatics, Mayo Clinic, Phoenix, Arizona, USA 他
*   **タスク**: 腹部骨盤CT検査における異常/分布外 (OOD) データの検出と識別
*   **データ**: Mayo Clinicの2850件以上の腹部骨盤CTボリューム (訓練)、2024年7月の544件のプロスペクティブテストセット、公開されているAbdominalCT-1kデータセット (外部テストセット)
*   **手法**: 2Dおよび3Dの生成アーキテクチャ (VQVAE, VIT-MAE) を用いた自己教師あり学習モデルを開発。L3スライスまたはシリーズ全体を入力とし、再構成画像を生成し、異常スコア計算ブロックで異常ピクセル/ボクセルを特定する。
*   **成果**: 提案モデルは、従来のメソッドよりも優れた結果を示し、偽陽性が無視できるレベルで、多様なOODサンプルを識別できた。プロスペクティブ分析では86.11%の真陽性率を達成。外部バリデーションでは75.26%の真陽性率を示した。
*   **新規性**: 医療CT画像におけるクラス内およびクラス間のOODデータを検出するための自己教師あり生成モデルを提案し、特に金属インプラントなどのアーチファクトや未文書化の異常に対応できることを示した点。これはAIのロバスト性向上に貢献します。
*   **限界**: 外部バリデーションにおける偽陽性率が24.7%とやや高く、主に体外の異常によって引き起こされた。

### Clinically oriented automatic 2D liver tumor segmentation: LCMambaNet with a state-space model and liver cancer-specific attention. (PMID: [41710673](https://pubmed.ncbi.nlm.nih.gov/41710673/))
*   **雑誌名**: Frontiers in oncology
*   **公開日**: 2026
*   **著者名**: Pengcheng Sun, Jing Yu, Qi Gu 他
*   **所属**: Department of Interventional Radiology, Suzhou Xiangcheng People's Hospital, Suzhou, China 他
*   **タスク**: 2D肝腫瘍の自動セグメンテーション
*   **データ**: LITS (CT) およびCirrMR160+ (MRI) データセット
*   **手法**: 選択的状態空間モデルに基づく効率的な2Dセグメンテーションフレームワーク「Liver Cancer Mamba Network (LCMambaNet)」を提案。スキャンパッチメカニズムと肝癌特異的注意モジュール (LCAM) を統合し、長距離依存性と連続的な特徴ダイナミクスを捉える。
*   **成果**: LITSデータセットでDiceスコア92.94 ± 3.12%、CirrMR160+データセットで92.08 ± 2.85%を達成し、既存のSOTA手法を上回った。特に2cm未満の小病変で統計的に有意な優位性を示した (p < 0.01)。
*   **新規性**: 選択的状態空間モデル (Mamba) を医療画像セグメンテーションに適用し、計算効率と高精度を両立させた点。特に小病変のセグメンテーション性能を向上させるための肝癌特異的注意モジュールを導入した点。
*   **限界**: 2Dセグメンテーションモデルであり、3Dコンテキストの利用は限定的。

### MedPTQ: a practical pipeline for real post-training quantization in 3D medical image segmentation. (PMID: [41709974](https://pubmed.ncbi.nlm.nih.gov/41709974/))
*   **雑誌名**: Journal of medical imaging (Bellingham, Wash.)
*   **公開日**: 2026-01
*   **著者名**: Chongyu Qu, Ritchie Zhao, Ye Yu 他
*   **所属**: Vanderbilt University, Department of Electrical and Computer Engineering, Nashville, Tennessee, United States 他
*   **タスク**: 3D医療画像セグメンテーションモデルの実用的な推論後量子化 (Post-Training Quantization, PTQ)
*   **データ**: BTCVデータセット (腹部13ラベル)、Whole Brain Dataset (全脳133ラベル)、TotalSegmentator V2 (全身104ラベル) を含む多様なCT/MRIデータセット
*   **手法**: MedPTQというオープンソースパイプラインを開発。TensorRTを用いて、U-Net, SegResNet, SwinUNETR, nnU-Net, UNesT, TransUNet, ST-UNet, VISTA3DといったSOTA 3Dセグメンテーションモデルに対し、8ビット (INT8) 量子化を実装。
*   **成果**: モデルサイズを最大3.83倍、推論レイテンシを最大2.74倍削減しつつ、FP32モデルとほぼ同等のDice類似係数 (mDSC) 性能を維持した。
*   **新規性**: 3D医療画像セグメンテーションモデルにおける、真の8ビット推論を実現する実用的な推論後量子化パイプラインを開発し、多様なアーキテクチャとデータセットでその有効性を示した点。これは計算資源が限られる臨床環境でのAI導入を加速させます。
*   **限界**: 量子化による精度低下が完全にゼロではない可能性があり、特定の臨床シナリオでの許容範囲の評価が必要。

## 総括・編集後記

今週は、AIの臨床応用における「実用性」と「信頼性」に焦点が当たった研究が目立ちました。AI導入を検討する際は、単一の性能指標だけでなく、実臨床でのロバスト性、不確実性評価、そして既存ワークフローとの整合性を多角的に評価するPoCが不可欠です。特に救急医療のような高リスク環境では、AIの限界を理解し、外部バリデーションや継続的な運用ログによる性能監視を通じて、安全な運用体制を確立することが重要となるでしょう。
