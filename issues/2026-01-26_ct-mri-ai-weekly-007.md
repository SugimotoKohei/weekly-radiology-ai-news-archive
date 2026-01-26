## 今週の Top Picks

### HMC-transducer: hierarchical mamba-CNN transducer for robust liver tumor segmentation. (PMID: [41577985](https://pubmed.ncbi.nlm.nih.gov/41577985/))
*   **雑誌名**: NPJ digital medicine
*   **公開日**: 2026-01-23
*   **著者名**: Jiyun Zhu, Chao Xu, Chang Lei 他
*   **所属**: Department of Hepatopancreatobiliary Surgery, The First Affiliated Hospital of Ningbo University, Ningbo, Zhejiang, China. 他
*   **タスク**: CT画像からの肝腫瘍セグメンテーション
*   **データ**: LiTS17, MSD-liver, KiTS21 (複数の公開ベンチマーク)
*   **手法**: 階層型Mamba-CNNトランスデューサー (HMC-transducer)。3D volumetricデータ向けに設計された方向認識3D Mamba (DA3D-Mamba) ブロックと、ゲート付き融合メカニズムを持つMamba-CNNトランスデューサーブロックを統合。
*   **成果**: 最先端のセグメンテーション精度を達成し、既存のCNNおよびTransformerベースの手法と比較して優れた汎化性と計算効率を示した。
*   **新規性**: Mambaという新しいState Space Modelを3D医用画像セグメンテーションに適用し、CNNと融合させることで、局所特徴と長距離空間依存性の両方を効率的に捉えるハイブリッドアーキテクチャを提案した点。
*   **限界**: 特になし。

### Evaluating the impact of deep learning-based image denoising on low-dose CT for lung cancer screening. (PMID: [41579047](https://pubmed.ncbi.nlm.nih.gov/41579047/))
*   **雑誌名**: Journal of applied clinical medical physics
*   **公開日**: 2026-02
*   **著者名**: Shih-Sheng Chen, Hsiao-Hua Liu, Ching-Ching Yang
*   **所属**: Department of Medical Imaging, Dalin Tzu-Chi Hospital, Chiayi, Taiwan. 他
*   **タスク**: 低線量CT (LDCT) 肺がんスクリーニングにおける深層学習ベースの画像ノイズ除去の影響評価
*   **データ**: LDCTおよびProjection Dataコレクションからの胸部CTスキャン
*   **手法**: 7つの深層学習ベースの画像ノイズ除去手法を適用し、客観的な画像品質指標 (RMSE, PSNR, SSIM) と結節関連特徴 (サイズ、CT値、Lung-RADS分類) を用いて評価。
*   **成果**: ノイズ除去によりSSIMが51%から60-64%に向上し、RMSEが137.13HUから62.40-78.30HUに減少、PSNRが23.91dBから28.59-30.51dBに増加。結節径のパーセント差も減少した。
*   **新規性**: LDCTワークフローにおける深層学習ノイズ除去技術の統合が、放射線被曝を増やすことなく早期肺がん検出を強化する可能性を、客観的指標と臨床的特徴の両面から詳細に評価した点。
*   **限界**: 診断性能への影響に関するさらなる検証が必要。

### Performance validation of a closed loop fully automated AI model for lung nodule stratification in screening cases. (PMID: [41564843](https://pubmed.ncbi.nlm.nih.gov/41564843/))
*   **雑誌名**: Respiratory investigation
*   **公開日**: 2026-01-20
*   **著者名**: A Taha, M S Muneer, A Kalra 他
*   **所属**: Division of Pulmonary, Allergy, and Critical Care Medicine, Stanford Medicine, Stanford, CA, United States. 他
*   **タスク**: 肺がんスクリーニングにおける肺結節リスク層別化のための全自動AIモデルの性能検証
*   **データ**: 複数施設からの2358症例（悪性・良性結節）で学習、米国複数施設コホート (n=184, 8施設) で検証。
*   **手法**: 前処理、解析、結果生成を統合した閉ループの全自動ソフトウェア (Bronchosolve)。深層学習畳み込みニューラルネットワーク (CNN) を用いて肺結節をトリアージ。
*   **成果**: 全症例で100%自動処理に成功。AUC 0.898 [0.851-0.940] を達成し、Lung-RADS (pAUC 0.669) およびBrockモデル (AUC 0.783) を上回った。感度83.6%、特異度86.3%。スキャナータイプやスライス厚によらず性能は一貫していた。
*   **新規性**: 前処理からレポート生成まで、手動入力なしで完結する「閉ループ」かつ「全自動」のAIシステムを開発し、その高い診断性能と堅牢性を多施設データで検証した点。
*   **限界**: 特になし。

### UNISELF: A unified network with instance normalization and self-ensembled lesion fusion for multiple sclerosis lesion segmentation. (PMID: [41570473](https://pubmed.ncbi.nlm.nih.gov/41570473/))
*   **雑誌名**: Medical image analysis
*   **公開日**: 2026-01-20
*   **著者名**: Jinwei Zhang, Lianrui Zuo, Blake E Dewey 他
*   **所属**: Department of Electrical and Computer Engineering, Johns Hopkins University, Baltimore, MD, 21218, USA. 他
*   **タスク**: マルチコントラストMR画像からの多発性硬化症 (MS) 病変セグメンテーション
*   **データ**: ISBI 2015チャレンジ訓練データで学習。MICCAI 2016, UMCL, プライベート多施設データで検証。
*   **手法**: UNISELF (Unified Network with Instance Normalization and Self-Ensembled Lesion Fusion)。テスト時自己アンサンブル病変融合 (test-time self-ensembled lesion fusion) と、ドメインシフトおよび欠損コントラストに対応するためのテスト時インスタンス正規化 (test-time instance normalization, TTIN) を活用。
*   **成果**: ISBI 2015チャレンジテストデータセットで最高の性能を達成した方法の一つにランクイン。さらに、ドメインシフトや欠損コントラストのある多様なout-of-domainテストデータセットにおいて、同じISBI訓練データで学習した全てのベンチマーク手法を上回った。
*   **新規性**: 単一の訓練ドメインで高い精度を達成しつつ、テスト時インスタンス正規化と自己アンサンブル病変融合により、ドメインシフトや欠損コントラストがある多様なout-of-domainデータセットに対しても優れた汎化性を示す手法を提案した点。
*   **限界**: 特になし。

### A CT Dataset with RECIST Measurements and Comprehensive Segmentation Masks for Tumors and Lymph Nodes. (PMID: [41559108](https://pubmed.ncbi.nlm.nih.gov/41559108/))
*   **雑誌名**: Scientific data
*   **公開日**: 2026-01-20
*   **著者名**: Roberto Rojas-Pizarro, Constanza Vásquez-Venegas, Gonzalo Pereira 他
*   **所属**: Laboratory for Scientific Image Analysis SCIAN-Lab, Interdisciplinary Nucleus for Biology and Genetics, Institute of Biomedical Sciences ICBM, Faculty of Medicine, University of Chile, Av. Independencia 1027, Santiago, 8380453, Chile. 他
*   **タスク**: RECIST測定と包括的セグメンテーションマスク付きCTデータセットの公開
*   **データ**: チリ大学臨床病院の22名の癌患者から得られた58枚のCTスキャン、1,246個の手動セグメンテーション病変、82個のRECIST 1.1準拠のターゲット病変径測定値。
*   **手法**: データセットの構築と公開。
*   **成果**: RECIST 1.1プロトコルに準拠した直径測定値と包括的な病変アノテーションを含むCTデータセットを提供。自動RECISTツール検証、ラディオミクス研究、セグメンテーションアルゴリズムのベンチマーク、医用画像基盤モデルの進歩など、多様なAI応用をサポートする。
*   **新規性**: RECIST 1.1準拠の測定値と包括的な病変セグメンテーションマスクを組み合わせた、希少な公開CTデータセットを提供した点。特にラテンアメリカの施設からのデータを含めることで、AIツールの汎化性向上に貢献する。
*   **限界**: データセットの規模はまだ限定的。

## 総括・編集後記

今週は、CT/MRIにおけるAIの臨床応用を加速する技術革新とデータ基盤の重要性が目立ちました。特に、Mambaのような新しいモデルアーキテクチャの導入、低線量CTにおけるノイズ除去技術の進展、肺結節スクリーニングにおける全自動AIモデルの検証、そして多発性硬化症病変セグメンテーションにおける汎化性向上への取り組みが注目されます。これらの技術は、診断支援の精度向上やワークフロー効率化に直結するため、自施設でのPoCや既存システムへの統合可能性を検討する価値があるでしょう。
