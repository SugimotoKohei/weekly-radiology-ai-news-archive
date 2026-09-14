## 今週の Top Picks

### Deep learning-based CT model for non-invasive prediction of tertiary lymphoid structures in pancreatic cancer: a multicenter study with prospective validation in an immunochemotherapy cohort. (PMID: [42731878](https://pubmed.ncbi.nlm.nih.gov/42731878/))
*   **雑誌名**: Journal for immunotherapy of cancer
*   **公開日**: 2026-09-12
*   **著者名**: Haopeng Yu, Xiaoying Li, Xuan Cheng 他
*   **所属**: Department of Radiology, West China Hospital of Sichuan University, Chengdu, Sichuan, China. 他
*   **タスク**: 膵管腺癌 (PDAC) における三次リンパ構造 (TLS) の非侵襲的予測、および免疫化学療法における予後・予測的価値の評価。
*   **データ**: 223名のPDAC外科切除患者（モデル開発）、82名の非外科患者（臨床検証）、44名の前向き免疫化学療法試験患者（病理学的検証、転帰評価）の術前造影CT。
*   **手法**: ResNet50ベースの深層学習ネットワーク (DLN)。
*   **成果**: 訓練、内部、外部検証コホートでAUC 0.987, 0.937, 0.853。非外科コホートでDLN予測TLS陽性患者はOSが有意に延長 (中央値19 vs 7ヶ月)。前向きコホートで病理学的検証AUC 0.929。DLN-high患者は客観的奏効率、PFS、OSが優れていた。DLNスコアはPD-L1発現と直交し、機能的TLS構造のバイオマーカーと相関。
*   **新規性**: 膵癌におけるTLSの非侵襲的予測モデルを開発し、多施設かつ前向きコホートで免疫化学療法における予後・予測的価値を検証した初の研究。
*   **限界**: 特定の免疫化学療法コホートでの検証であり、他の治療レジメンや異なる人種集団での汎化性はさらなる検証が必要。

### MRICombo: a deep-learning-based framework for universal volumetric segmentation grading-staging and malignancy detection across heterogeneous MRI. (PMID: [42722659](https://pubmed.ncbi.nlm.nih.gov/42722659/))
*   **雑誌名**: Nature communications
*   **公開日**: 2026-08-08
*   **著者名**: Zhuoneng Zhang, Luyi Han, Dengqiang Jia 他
*   **所属**: Faculty of Applied Sciences, Macao Polytechnic University, Rua de Luis Gonzaga Gomes, Macao, China. 他
*   **タスク**: 9種類の異なるMRIシーケンスに対応する、汎用的な体積セグメンテーション、グレーディング、ステージング、悪性度検出。
*   **データ**: 2,354人から7,380シーケンスのMRIデータで開発。4つの独立した外部データセット（734人から1082シーケンス）で外部検証。
*   **手法**: MRIComboと名付けられた統一されたマルチエキスパート深層学習フレームワーク。
*   **成果**: 14の重要解剖構造のセグメンテーションで平均Dice 0.836、11の主要腫瘍タイプのラベリングで平均Dice 0.625。膠芽腫のグレーディング、膀胱癌・鼻咽頭癌のステージング、乳癌・肝腫瘍の悪性度検出で平均AUROC 0.920を達成。欠損シーケンスでの柔軟な推論も可能。
*   **新規性**: 複数の異なるMRIシーケンス、多臓器、多タスク（セグメンテーション、グレーディング、ステージング、悪性度検出）に統一的に対応する汎用的な深層学習フレームワークを提案し、高い性能と堅牢な汎化性を示した。
*   **限界**: 開発データセットの多様性は高いものの、さらなる大規模・多施設での検証が必要。モデルの解釈性向上の余地。

### Cross-fraction prior learning for scalable organ-at-risk segmentation in abdominal MR-guided radiotherapy. (PMID: [42725420](https://pubmed.ncbi.nlm.nih.gov/42725420/))
*   **雑誌名**: Medical physics
*   **公開日**: 2026-09
*   **著者名**: Chengyin Li, Doris Rusu, Rafi Ibn Sultan 他
*   **所属**: Department of Radiation Oncology, Henry Ford Health, Detroit, Michigan, USA. 他
*   **タスク**: 腹部MRガイド下適応放射線治療 (MRgRT) におけるリスク臓器 (OAR) のセグメンテーション。
*   **データ**: 104名の膵癌患者、520治療フラクションの腹部MRIデータ。4つの腹部臓器（結腸、十二指腸、小腸、胃）。
*   **手法**: AdaptSegと名付けられた、クロスフラクション解剖学的事前情報（以前の治療フラクションの画像-マスク情報）を活用するデュアルパスニューラルアーキテクチャ。3D UNetとSwinUNETRをバックボーンとして使用。
*   **成果**: クロスフラクション事前情報によりセグメンテーション性能が向上。3D UNetで平均Dice 83.78%から87.22%へ、SwinUNETRで82.49%から85.19%へ改善。特に変形しやすい小腸で最大7.0ポイントのDice向上 (77.8%から84.8%)。推論時間は1.6秒未満。
*   **新規性**: MRgRTのワークフローにおけるOARセグメンテーションのボトルネックに対し、過去の治療フラクションからの時系列情報を活用するスケーラブルなフレームワークを提案し、性能向上と高速推論を両立させた。
*   **限界**: 膵癌患者に限定されたデータセットでの検証であり、他の腹部癌種や異なるMRgRTプロトコルでの汎化性はさらなる検証が必要。

### Validation of Artificial Intelligence-based Non-gated Chest CT for Coronary Artery Calcium Scoring Across Multiple CT Scanners. (PMID: [42722952](https://pubmed.ncbi.nlm.nih.gov/42722952/))
*   **雑誌名**: Journal of imaging informatics in medicine
*   **公開日**: 2026-09-10
*   **著者名**: Ying Liu, Wanxue Xin, Lin Wang 他
*   **所属**: Department of CTMR, Ningcheng County Central Hospital, Chifeng, 024200, Inner Mongolia, China. 他
*   **タスク**: AIベースの非同期胸部CTによる冠動脈石灰化 (CAC) スコアリングの定量化とリスク層別化。
*   **データ**: 冠動脈CTアンギオグラフィー (CCTA) と非同期単純胸部CTを1ヶ月以内に両方受けた患者のレトロスペクティブデータ。複数のCTスキャナーからのデータ。
*   **手法**: AIベースの非ECG同期胸部CT画像解析。ECG同期CAC測定結果をゴールドスタンダードとして比較。
*   **成果**: 全体集団で、AI支援非ECG同期胸部CTとECG同期検査間の石灰化体積、等価質量、石灰化スコアのICC値はそれぞれ0.975, 0.886, 0.972と良好な一致を示した。異なるスキャナー間でも相関係数は0.8以上、体積とスコアは0.95以上。リスク層別化の一致度 (Kappa) も良好から優れていた。
*   **新規性**: 複数のCTスキャナーからの非同期胸部CTデータを用いて、AIベースのCACスコアリングの定量化とリスク層別化の性能を大規模に検証し、その実用性を示した。
*   **限界**: 高い石灰化負荷では比例バイアスが観察された。レトロスペクティブ研究であり、前向き研究でのさらなる検証が必要。

### Externally validated explainable 3D CNN ensemble model for non-invasive prediction of IDH and MGMT status in gliomas. (PMID: [42718428](https://pubmed.ncbi.nlm.nih.gov/42718428/))
*   **雑誌名**: Frontiers in oncology
*   **公開日**: 2026
*   **著者名**: Rafail C Christodoulou, Georgios Vamvouras, Rafael Pitsillos 他
*   **所属**: Department of Radiology, Stanford University School of Medicine, Stanford, CA, United States. 他
*   **タスク**: 膠芽腫におけるIDH変異およびMGMTプロモーターメチル化状態の非侵襲的予測。
*   **データ**: UCSF-PDGMおよびUPENN-GBMコホート（訓練・テスト）、MU-Glioma-Postデータセット（独立外部検証）からの多施設MRIデータ。
*   **手法**: 説明可能な3D畳み込みニューラルネットワーク (CNN) アンサンブルモデル。Integrated Gradients saliency mapとShapley値を用いてモデルの解釈性を評価。
*   **成果**: IDH変異分類でテストAUC 0.94、外部検証AUC 0.77。MGMTプロモーターメチル化分類でテストAUC 0.68、外部検証AUC 0.57。IGマップは生物学的に妥当な領域（IDHは腫瘍周囲FLAIR高信号、MGMTはT1CEの増強腫瘍コア）を強調。Shapley分析でIDH分類はFLAIRが64%、T1CEが36%寄与。MGMT分類はT1CEが60.6%、FLAIRが30.8%寄与。
*   **新規性**: 膠芽腫のIDH変異およびMGMTメチル化状態をルーチンMRIから非侵襲的に予測する説明可能な3Dアンサンブル深層学習フレームワークを開発し、外部検証を行った。
*   **限界**: MGMTメチル化状態の予測性能は外部検証で汎化性が低く、画像のみからの予測は依然として課題。データセットの多様性や規模のさらなる拡大が必要。

## 総括・編集後記

今週は、CT/MRIを用いたAIによる診断・予後予測、セグメンテーション、画像再構成といった幅広い臨床応用において、多施設検証や前向き検証、汎用性、説明可能性を重視した研究が目立ちました。これらの進展は、AIモデルの臨床導入を検討する上で、多施設検証済みモデルのPoC（概念実証）から始めることの重要性を示唆しています。ただし、外部バリデーションにおける性能低下や、異なる施設・スキャナー・患者集団間でのバイアスに留意し、モデルの限界を理解した上で継続的な運用ログ評価が不可欠となるでしょう。
