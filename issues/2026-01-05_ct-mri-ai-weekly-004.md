## 今週の Top Picks

### A clinically validated 3D deep learning approach for quantifying vascular invasion in pancreatic cancer. (PMID: [41476122](https://pubmed.ncbi.nlm.nih.gov/41476122/))
*   **雑誌名**: NPJ digital medicine
*   **公開日**: 2025-12-31
*   **著者名**: Yajiao Zhang, Haoran Zhang, Yanzhao Yang 他
*   **所属**: Department of Radiology, Ruijin Hospital, Shanghai Jiao Tong University School of Medicine, Shanghai, China. 他
*   **タスク**: 造影CTスキャンからの膵癌血管浸潤の自動定量化。
*   **データ**: 2130症例で学習・内部検証、202症例で前向きテスト。
*   **手法**: PAN-VIQ (Pancreatic Vascular Invasion Quantifier) と呼ばれる深層学習フレームワークを開発し、膵腫瘍と5つの主要血管（腹腔動脈、総肝動脈、上腸間膜動脈、上腸間膜静脈、門脈）をセグメンテーションし、3D被包角度を定量化。
*   **成果**: 外部検証で90%を超える精度を達成。前向き評価では、ジュニア放射線科医を凌駕し、シニア放射線科医に匹敵する精度と再現率を示した。
*   **新規性**: 膵癌の血管浸潤を3Dで定量化する自動深層学習フレームワークを開発し、臨床的に検証された点で新規性がある。
*   **限界**: さらなる大規模多施設データでの検証が必要。

### A CT-based deep learning approach to differentiate multiple primary lung cancers, metastases, and benign nodules. (PMID: [41485033](https://pubmed.ncbi.nlm.nih.gov/41485033/))
*   **雑誌名**: BMC cancer
*   **公開日**: 2026-01-02
*   **著者名**: Yuling Liufu, Ruihua Su, Yanhua Wen 他
*   **所属**: Department of Radiology The Fifth Affiliated Hospital of Guangzhou Medical University, Guangzhou, China.
*   **タスク**: CT画像からの多発性原発性肺癌、肺内転移、多発性良性肺病変の鑑別。
*   **データ**: 260患者（MPLC=83, IPM=81, MBPL=96; 881軸CTスライス）。
*   **手法**: DenseNet-121, EfficientNet-B1, MambaOut-Kobe, ResNet-50, SwinV2-CR-Tiny-224, ViT-Tiny-Patch16-224の6つの事前学習済みアーキテクチャを比較し、MambaOut-Kobeを最終モデルとして採用。
*   **成果**: MambaOut-Kobeモデルは、マクロAUC 0.946±0.004、精度0.829±0.029を達成し、計算効率（低メモリ、低レイテンシ）も優れていた。
*   **新規性**: MambaOut-KobeモデルをCTベースの多発性肺病変鑑別に適用し、高精度かつ計算効率の良い診断支援システムを開発した点で新規性がある。
*   **限界**: より大規模な多施設データでの検証と、MPLCとIPM間の鑑別能力のさらなる向上が必要。

### Coronary artery segmentation in non-contrast calcium scoring CT images using deep learning. (PMID: [41483696](https://pubmed.ncbi.nlm.nih.gov/41483696/))
*   **雑誌名**: Computers in biology and medicine
*   **公開日**: 2026-01-02
*   **著者名**: Mariusz Bujny, Katarzyna Jesionek, Jakub Nalepa 他
*   **所属**: Graylight Imaging, Gliwice, Poland. 他
*   **タスク**: ECG同期非造影心臓CT画像からの冠動脈セグメンテーション。
*   **データ**: マルチベンダーの非造影CT画像。
*   **手法**: 画像レジストレーションを介した半自動Ground Truth (GT) 生成の新規フレームワークを利用し、AutoML駆動の深層学習モデルを開発。
*   **成果**: 提案モデルは、トレーニングに使用したGTよりも有意に正確に冠動脈をセグメンテーションし、DiceおよびclDice指標は評価者間変動に近い値を示した。
*   **新規性**: 非造影CT画像における冠動脈セグメンテーションの課題に対し、画像レジストレーションを用いた効率的な半自動GT生成とAutoMLモデルを組み合わせた点で新規性がある。
*   **限界**: モデルの汎化性能をさらに高めるための多様なデータセットでの検証が必要。

### Incorporating physicians' contouring style into auto-segmentation of clinical target volume for post-operative prostate cancer radiotherapy using a language encoder. (PMID: [41477361](https://pubmed.ncbi.nlm.nih.gov/41477361/))
*   **雑誌名**: Machine Learning. Health
*   **公開日**: 2025-12
*   **著者名**: Hengrui Zhao, Chien-Yi Liao, Daniel Yang 他
*   **所属**: Medical Artificial Intelligence and Automation Laboratory and Department of Radiation Oncology, University of Texas Southwestern Medical Center, Dallas TX, USA.
*   **タスク**: 術後前立腺癌放射線治療における臨床標的体積 (CTV) の自動セグメンテーションに、医師個別の輪郭描画スタイルを組み込む。
*   **データ**: 824患者のCT画像データセット（トレーニング699、バリデーション49、テスト76）。テストセットは4名の医師、トレーニングセットは7名の医師のデータを含む。
*   **手法**: Text-UNetを開発。テキストエンコーダを用いて医師固有の輪郭描画スタイルを潜在ベクトルにエンコードし、CT画像特徴と結合してセグメンテーションをガイドする。
*   **成果**: Text-UNetは平均Diceスコア85.1%を達成し、ベースラインUNet (82.0%) および既存の最先端モデルを上回った。医師固有の情報を組み込むことで、セグメンテーションの一貫性が向上し、手動での輪郭描画作業が削減される可能性を示した。
*   **新規性**: 医師の個別の輪郭描画スタイルを言語エンコーダを介して深層学習モデルに組み込むことで、医師間のばらつきに対応し、CTV自動セグメンテーションの精度を向上させた点で新規性がある。
*   **限界**: 医師のスタイルを表現するテキスト情報の標準化や、より多様な医師のデータでの検証が必要。

### Interpretable model based on multisequence magnetic resonance imaging radiomics for predicting the pathological grades of hepatocellular carcinomas. (PMID: [41480292](https://pubmed.ncbi.nlm.nih.gov/41480292/))
*   **雑誌名**: World journal of radiology
*   **公開日**: 2025-12-28
*   **著者名**: Yue Shi, Peng Zhang, Li Li 他
*   **所属**: Department of Radiology, Interventional Medical Center, Science and Technology Innovation Center, Affiliated Hospital of North Sichuan Medical College, Nanchong, China. 他
*   **タスク**: MRIラディオミクスと臨床特徴に基づき、肝細胞癌 (HCC) の病理学的グレードを術前に予測する。
*   **データ**: 125名のHCC患者のMRIおよび臨床データ。
*   **手法**: 脂肪抑制T2強調画像 (FS-T2WI)、動脈相 (AP)、門脈相 (PVP) 画像からラディオミクス特徴を抽出し、臨床的独立予測因子と組み合わせて、解釈可能な機械学習モデルを開発。SHapley Additive exPlanations (SHAP) 値分析で解釈可能性を評価。
*   **成果**: 統合されたラディオミクス・臨床モデル (RCモデル) が最高の性能を示し、検証グループでAUC 0.932を達成した。SHAP分析により、モデルへの各特徴の寄与が明らかになった。
*   **新規性**: マルチシーケンスMRIラディオミクスと臨床特徴を統合し、SHAP値分析によって解釈可能性を確保した機械学習モデルを開発し、HCCの病理学的グレードを非侵襲的に予測した点で新規性がある。
*   **限界**: 後ろ向き単施設研究であり、より大規模な前向き多施設データでの検証が必要。

## 総括・編集後記

今週は、CT/MRI画像を用いたAIによる診断・治療支援の多様な進展が目立ちました。特に、膵癌の血管浸潤の3D定量化や肺病変の精密鑑別、医師のスタイルを考慮した放射線治療計画支援など、臨床的意義の高い応用が注目されます。これらの技術は、診断の客観性向上や治療計画の最適化に貢献するため、自施設でのPoC（概念実証）やデータ収集の検討を進める良い機会となるでしょう。
