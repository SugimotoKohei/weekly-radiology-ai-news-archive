## 今週の Top Picks

### Validation of artificial intelligence-assisted CBCT analysis for predicting inferior alveolar nerve proximity to impacted mandibular third molars: a diagnostic accuracy study. (PMID: [42603807](https://pubmed.ncbi.nlm.nih.gov/42603807/))
*   **雑誌名**: BMC oral health
*   **公開日**: 2026-08-15
*   **著者名**: Huan Hu, Jiahang Wu, Hongji Pu 他
*   **所属**: Department of Stomatology, Qujing Central Hospital of Yunnan Province, Qujing, Yunnan, China. 他
*   **タスク**: 埋伏下顎第三大臼歯と下歯槽神経 (IAN) の空間的近接度予測
*   **データ**: 312患者 (486 M3部位) のCBCT画像。内部コホート。
*   **手法**: 修正U-Netアーキテクチャを用いた深層学習システムでIAN管とM3Mを自動セグメンテーションし、近接度を3カテゴリに分類。
*   **成果**: 全体精度90.1%、加重AUC 0.925、Cohen's κ 0.851を達成し、専門家評価とほぼ完璧な一致を示した。AI処理時間は専門家評価の約39.79分の1に短縮された。
*   **新規性**: AI支援CBCT分析システムが、埋伏下顎第三大臼歯と下歯槽神経の近接度予測において、高い診断精度と専門家との優れた一致を示し、処理時間を大幅に短縮した点。
*   **限界**: 参照標準が術中ではなく放射線学的評価であること、前向き多施設バリデーションが必要であること。

### Multiscale Multiparametric MRI Deep Learning for Short-Term Survival Assessment in Glioblastoma. (PMID: [42603108](https://pubmed.ncbi.nlm.nih.gov/42603108/))
*   **雑誌名**: Journal of magnetic resonance imaging : JMRI
*   **公開日**: 2026-08-15
*   **著者名**: Hongbo Zhang, Beibei Zhou, Xinzhu Zhao 他
*   **所属**: Medical Image Center, Shenzhen Hospital, Southern Medical University (Shenzhen School of Clinical Medicine, Southern Medical University), Shenzhen, Guangdong, China. 他
*   **タスク**: 膠芽腫患者の短期生存（9ヶ月以内）予測
*   **データ**: 728名の新規診断膠芽腫患者のマルチパラメトリックMRI (T1強調、T2強調、FLAIR、造影T1強調)。トレーニングコホート (n=290) と外部コホート1-3 (n=225/182/31)。
*   **手法**: マルチスケールMRIベースの深層学習モデル。全脳、3D腫瘍、2.5D腫瘍の入力を統合し、臨床データや従来のMRI形態計測と比較。
*   **成果**: 外部コホートでAUC 0.871, 0.828, 0.798を達成し、臨床-MRI形態計測ベースラインと比較してAUCが最大0.161向上した。モデル出力は免疫・炎症および細胞周期関連の転写プログラムと関連することが示された。
*   **新規性**: マルチスケールMRI深層学習モデルが膠芽腫の短期生存予測において良好な識別能力を示し、その出力が免疫および細胞周期関連の転写プログラムと関連していることを、外部バリデーションを通じて示した点。
*   **限界**: 外部コホート2でのAUC向上はFDR補正後有意ではなかった。

### Assessing CT-based volumetric analysis via deep learning for idiopathic normal pressure hydrocephalus. (PMID: [42603074](https://pubmed.ncbi.nlm.nih.gov/42603074/))
*   **雑誌名**: Brain communications
*   **公開日**: 2026
*   **著者名**: Meera Srikrishna, Woosung Seo, Anna Zettergren 他
*   **所属**: Wallenberg Centre for Molecular and Translational Medicine, University of Gothenburg, Gothenburg, Sweden. 他
*   **タスク**: 特発性正常圧水頭症 (iNPH) 患者における脳CTベースの脳室脳脊髄液 (VCSF) 体積測定
*   **データ**: 健常対照群の734 CTデータセット (T1強調MRIとペア)、iNPH患者の62 CTスキャン (Uppsala)、外部バリデーションとしてiNPH患者11名 (Rostock) と30名 (Alabama) のCTスキャン。
*   **手法**: 2段階アプローチ。まず2D U-Netモデルを健常対照群のMR-VCSFラベルでCT-VCSFセグメンテーションを予測するように訓練。次にiNPH患者の手動セグメンテーションCT-VCSFラベルでモデルを洗練。
*   **成果**: 脳室体積測定において、手動測定と強い相関を示し、iNPH診断における自動CT体積測定の性能を評価した。
*   **新規性**: MRIからの転移学習とiNPH患者のCTデータによる洗練を組み合わせた2段階深層学習アプローチにより、iNPH診断におけるCTベースの脳室脳脊髄液の自動体積測定の性能を向上させ、多様な患者集団での外部バリデーションを行った点。
*   **限界**: 抽象には具体的な数値成果が記載されていない。

### Diagnostic efficacy of deep learning-based denoising of low-field 0.55 T compared to conventional 3 T knee MRI. (PMID: [42594606](https://pubmed.ncbi.nlm.nih.gov/42594606/))
*   **雑誌名**: European journal of radiology
*   **公開日**: 2026-08-13
*   **著者名**: Sevtap Tugce Ulas, Madeline Hess, Zheren Zhu 他
*   **所属**: Department of Radiology and Biomedical Imaging, University of California - San Francisco, San Francisco, USA. 他
*   **タスク**: 低磁場0.55T膝MRIの深層学習 (DL) ベースノイズ除去による診断性能評価
*   **データ**: 膝痛患者26名 (33膝) の0.55Tと3Tの膝MRI。
*   **手法**: 0.55TデータにDLベースノイズ除去 (ImT-MRD) を適用。4名の放射線科医が画像品質、解剖学的ランドマークの視認性、病理検出の診断確信度を評価。コンセンサス読影を基準として診断精度を算出。
*   **成果**: 0.55T (DLあり) は感度0.97、精度0.98に向上し、従来の3T MRI (感度0.95、精度0.97) に匹敵する診断性能を示した。3Tとの一致度はDLありで0.94 (優良) であった。画像品質と診断確信度もDLにより有意に向上した。
*   **新規性**: 深層学習ベースのノイズ除去技術を低磁場0.55T膝MRIに適用することで、その診断性能を大幅に向上させ、従来の3T MRIに匹敵する結果を達成した点。これにより、低磁場MRIの臨床的有用性を高める可能性を示した。
*   **限界**: レトロスペクティブ研究であり、患者数が比較的少ない。

### Tumor-SAM: Segment Anything Model for Semi-automatic Lung Tumor Segmentation in CT. (PMID: [42592330](https://pubmed.ncbi.nlm.nih.gov/42592330/))
*   **雑誌名**: Proceedings of SPIE--the International Society for Optical Engineering
*   **公開日**: 2026
*   **著者名**: L Xie, Y Tong, C Wu 他
*   **所属**: Medical Image Processing Group, Department of Radiology, University of Pennsylvania, Philadelphia, PA, United States. 他
*   **タスク**: CT画像における肺腫瘍の半自動セグメンテーション
*   **データ**: 164のテストスキャン。
*   **手法**: 改善されたSegment Anything Model (Tumor-SAM) を提案。U-Netをベースとした画像エンコーダと、腫瘍の形状・位置をより良く捉える楕円プロンプトを統合。肺ROI検出で周囲組織の干渉を低減。
*   **成果**: 平均Dice係数0.84±0.13、平均Hausdorff距離7.25±6.24 mmを達成し、良好な肺腫瘍セグメンテーション精度を示した。
*   **新規性**: Segment Anything Model (SAM) を医療画像、特にCT肺腫瘍セグメンテーションに応用し、U-Netベースの画像エンコーダと、点やボックスよりも腫瘍形状を捉えやすい楕円プロンプトを導入することで、半自動セグメンテーションの精度と堅牢性を向上させた点。
*   **限界**: 評価データセットの規模や詳細（単一施設か否かなど）が不明。

## 総括・編集後記

今週は、AIによる画像診断支援の多様な進展、特にCT/MRIにおける診断精度向上と効率化が目立ちました。これらの技術は、診断の迅速化や低磁場MRIの活用、外科的計画の精度向上に貢献するため、各施設でのPoCや既存ワークフローへの統合可能性を検討する良い機会となるでしょう。ただし、多くの研究が外部バリデーションの必要性を指摘しており、実臨床導入には多施設での検証と堅牢性の評価が引き続き重要です。
