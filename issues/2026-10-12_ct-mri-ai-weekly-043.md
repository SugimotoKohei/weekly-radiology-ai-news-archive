## 今週の Top Picks

### A Volumetric Anatomy-Aware, Prompt-Guided Adaptation Framework for the Segment Anything Model in Head and Neck Radiotherapy (PMID: [42845693](https://pubmed.ncbi.nlm.nih.gov/42845693/))
*   **雑誌名**: Cureus
*   **公開日**: 2026-10
*   **著者名**: Yuqing Xia, Samer Jabor, Parker New 他
*   **所属**: Department of Radiation Oncology, University of Texas Health Science Center at San Antonio, San Antonio, USA. 他
*   **タスク**: 頭頸部放射線治療計画におけるリスク臓器 (OARs) の自動セグメンテーション、特に小臓器の精度向上。
*   **データ**: 211患者の頭頸部CTデータセット (23 OARsの手動アノテーション)。
*   **手法**: Volumetric SAM (SAM-Med3D) をベースに、解剖学的知識に基づくプロンプト生成、粗密パイプライン、ROIガイドによる小臓器強調、臓器特異的閾値キャリブレーションを統合したSAM-FT-HNフレームワーク。
*   **成果**: 大OARsでnnUNetに匹敵する性能 (平均Dice 0.814 vs 0.791)、小OARsでSAM-Med3Dを大幅に改善 (平均Dice 0.300から0.669へ)。全体でnnUNetと同等 (平均Dice 0.770 vs 0.769)。
*   **新規性**: Foundation ModelであるSAMを、解剖学的知識に基づく自動プロンプト生成と適応的閾値処理を組み合わせることで、頭頸部放射線治療における小臓器セグメンテーションの課題を克服した点。
*   **限界**: 小臓器のDiceスコアはnnUNetにわずかに及ばない。

### Multi-Dimensional Feature Adaptive Gating Network for Multi-View and Whole-Brain Magnetic Resonance Imaging-Based Alzheimer's Disease Classification (PMID: [42858061](https://pubmed.ncbi.nlm.nih.gov/42858061/))
*   **雑誌名**: Journal of visualized experiments : JoVE
*   **公開日**: 2026-10-09
*   **著者名**: Yipeng Zhou, Lin Zhu, Zhenqiao Liu 他
*   **所属**: Research Centre for Agri-Product Quality Traceability, Beijing Technology and Business University. 他
*   **タスク**: 構造MRI (sMRI) を用いたアルツハイマー病 (AD)、軽度認知障害 (MCI)、正常対照 (NC) の分類。
*   **データ**: Alzheimer's Disease Neuroimaging Initiative (ADNI) データセットから842症例。
*   **手法**: 多次元特徴適応ゲーティングネットワーク (MDFAG-Net)。Vision Transformerバックボーンで矢状・冠状・軸状の2Dスライスレベル特徴を抽出し、3D CNNで全脳特徴を抽出。Enhanced Sparse Multiple Instance Learningで情報量の多いスライスを特定し、適応ゲーティングモジュールでマルチビューと全脳特徴を動的に融合。
*   **成果**: 競合モデルを上回る分類性能 (AUC 0.798)。Grad-CAMとDeepSHAPにより、海馬、扁桃体、後部帯状回、傍海馬回、脳室系などAD進行に関連する解剖学的領域を特定。
*   **新規性**: 2Dスライスレベル特徴と3D全脳特徴を組み合わせ、さらに適応ゲーティングモジュールで動的に融合する多次元特徴適応ゲーティングネットワーク (MDFAG-Net) を提案し、解釈可能性も高めた点。
*   **限界**: 記載なし。

### Subtraction iodine maps combined with deep learning reconstruction for improved evaluation of bony invasion in temporal bone lesions (PMID: [42855533](https://pubmed.ncbi.nlm.nih.gov/42855533/))
*   **雑誌名**: European radiology
*   **公開日**: 2026-10-09
*   **著者名**: Tong Su, Zhe Zhang, Xu Tian 他
*   **所属**: Department of Radiology, Peking Union Medical College Hospital, Chinese Academy of Medical Sciences & Peking Union Medical College, Beijing, China. 他
*   **タスク**: 側頭骨病変における骨浸潤の評価を、Subtraction iodine map (SIM) とDeep Learning Reconstruction (DLR) を組み合わせて改善。
*   **データ**: 77患者の側頭骨増強CTスキャン。
*   **手法**: 前後造影CT画像からSIMを生成し、DLRで再構成。Enhanced-HIR、Enhanced-DLR、SIM-HIR、SIM-DLRの4グループで定性的・定量的に比較。
*   **成果**: SIM-DLRはEnhanced-HIRと比較してノイズを大幅に低減し、病変のCNRを増加 (p < 0.001)。全体的な画像品質、病変検出の信頼性、輪郭描出能力、骨浸潤の視覚化においてSIM-DLRが有意に高いスコア (p < 0.001)。
*   **新規性**: Subtraction iodine mapとDeep Learning Reconstructionを組み合わせることで、側頭骨病変の骨浸潤評価における画像品質と診断精度を向上させた点。
*   **限界**: 記載なし。

### MRI-derived radiomics for prostate cancer active surveillance: a systematic review (PMID: [42858633](https://pubmed.ncbi.nlm.nih.gov/42858633/))
*   **雑誌名**: European journal of radiology
*   **公開日**: 2026-10-07
*   **著者名**: Eimear T Kyle, Kevin J Sweeney, Devin H McCabe 他
*   **所属**: School of Medicine, Trinity College Dublin, College Green, Dublin 2 D02 PN40, Ireland. 他
*   **タスク**: 前立腺癌の活動性監視 (AS) におけるMRI由来ラジオミクスおよびAIモデルの予後予測能力を系統的にレビュー。
*   **データ**: PubMed, Scopus, Embase, Web of Science (2000年～2026年9月) から抽出された17研究 (12ユニークコホート、2703症例)。
*   **手法**: PRISMA 2020ガイドラインに従ったシステマティックレビュー。QUADAS-2、PROBAST、METRICSを用いてバイアスリスクと方法論的品質を評価。
*   **成果**: 17研究中16研究でバイアスリスクが高いか不明。METRICSスコアの中央値は32.3%。進行の定義が5通りあり、定量的統合は不可能。外部バリデーションやキャリブレーションを報告した研究はなし。
*   **新規性**: 前立腺癌の活動性監視におけるMRIラジオミクスおよびAIモデルの現状を系統的にレビューし、その方法論的課題（エンドポイントの異質性、外部バリデーションの欠如、バイアスリスク）を明確に指摘した点。
*   **限界**: 進行の定義が異質であり、臨床的関連性が限定的。外部バリデーションやキャリブレーションの報告がない。

### Deep Learning-driven Segmentation of Breast Cancer MR Imaging Using a Hybrid ResNet-Transformer Architecture and Cross-dataset Validation (PMID: [42844165](https://pubmed.ncbi.nlm.nih.gov/42844165/))
*   **雑誌名**: Magnetic resonance in medical sciences : MRMS : an official journal of Japan Society of Magnetic Resonance in Medicine
*   **公開日**: 2026
*   **著者名**: Yongjian Sui, Peiru Li, Jiacheng Li 他
*   **所属**: Department of Radiology, Yongkang First People's Hospital, Yongkang, Zhejiang, China. 他
*   **タスク**: 2D動的造影MRI (DCE-MRI) における乳癌病変の自動セグメンテーション。
*   **データ**: BC MRI Segmentation Benchmark (BC-MRI-SEG) の4つの独立した公開データセットから20434枚の乳癌MRI画像。
*   **手法**: ResNet50エンコーダ (局所特徴抽出) とTransformerモジュール (大域的文脈モデリング) を統合したU-Netベースのハイブリッドモデル。leave-one-dataset-outクロスデータセット外部バリデーション戦略で評価。
*   **成果**: 評価されたデータセット全体で安定したセグメンテーション性能 (患者レベルDSC 0.75-0.79、IoU 0.61-0.66)。固定された比較コホートではDSC 0.82、IoU 0.70を達成し、ベースラインモデルを上回った (P ≤ 0.021)。
*   **新規性**: ResNet-TransformerハイブリッドU-Netアーキテクチャを提案し、複数の公開データセットを用いたクロスデータセット外部バリデーションにより、乳癌MRIセグメンテーションにおける汎化性能と堅牢性を示した点。
*   **限界**: 記載なし。

## 総括・編集後記

今週は、Foundation Modelの医用画像応用、マルチモーダルAI、そしてAI研究の信頼性と汎化性に関する議論が目立ちました。読者の皆様には、これらの最新技術を自施設でのPoCや既存ワークフローへの導入可能性を検討する上で、特に外部バリデーションやデータセットの多様性に注目して論文を読み解くことをお勧めします。AIモデルの臨床導入においては、単なる性能指標だけでなく、その解釈可能性や実臨床での堅牢性、そして既存の診断基準との整合性を常に意識し、慎重な評価が不可欠です。
