## 今週の Top Picks

### A clinically applicable and generalizable deep learning model for anterior mediastinal tumors in CT images across multiple institutions. (PMID: [41617892](https://pubmed.ncbi.nlm.nih.gov/41617892/))
-   **雑誌名**: Scientific reports
-   **公開日**: 2026-01-30
-   **著者名**: Chihiro Takemura, Mototaka Miyake, Kazuma Kobayashi 他
-   **所属**: Department of Thoracic Surgery, National Cancer Center Hospital, Tokyo, Japan. 他
-   **タスク**: CT画像における前縦隔腫瘍（胸腺腫、胸腺癌など）のセグメンテーションと検出。
-   **データ**: 136病院から収集された711枚のCT画像（病理学的に証明された前縦隔腫瘍患者）。外部テストセットは121の異なる施設からの164画像。
-   **手法**: 3D U-Netベースのモデルを訓練。
-   **成果**: 外部テストセットにおいて、腫瘍セグメンテーションで平均Diceスコア0.82、IoU 0.72、検出で高感度と低偽陽性率を達成。IoU閾値0.50でも感度0.87、スキャンあたり偽陽性0.61。
-   **新規性**: 希少疾患である前縦隔腫瘍に対し、121の異なる施設からのデータで広範な汎用性を実証した初の臨床応用可能な深層学習モデル。
-   **限界**: 記載なし。

### Slice-prompted HR-CTV interactive segmentation for cervical cancer brachytherapy: A multi-center study. (PMID: [41615195](https://pubmed.ncbi.nlm.nih.gov/41615195/))
-   **雑誌名**: Medical physics
-   **公開日**: 2026-02
-   **著者名**: Zhao Peng, Chunbo Liu, Du Tang 他
-   **所属**: Department of Oncology, Xiangya Hospital, Central South University, Changsha, China. 他
-   **タスク**: CTガイド下子宮頸がん密封小線源治療における高リスク臨床標的体積（HR-CTV）の対話型セグメンテーション。
-   **データ**: 640枚のCTスキャン（160患者）で訓練、160枚（40患者）で検証。3つのマルチセンターコホート（400枚、115枚、150枚）で外部テスト。
-   **手法**: スライスプロンプト型対話型セグメンテーション手法（SPSeg）を提案。3D U-Netアーキテクチャに、臨床医が主要スライスで手動でHR-CTVをアウトラインしたスパースなプロンプトをエンコード。
-   **成果**: わずか3枚のプロンプトスライスを追加するだけで、Diceスコアが0.83から0.95に、HD95が7.5mmから2.1mmに大幅改善（テストセット1）。臨床的受容性も高く、輪郭描画時間を大幅に短縮（11.7分から1.7分）。観察者間の一致度も向上。
-   **新規性**: 臨床医の専門知識と深層学習を効果的に統合し、CTガイド下子宮頸がん密封小線源治療におけるHR-CTV輪郭描画の精度と効率を大幅に向上させた対話型セグメンテーションフレームワーク。
-   **限界**: 記載なし。

### Benchmark White Matter Hyperintensity Segmentation Methods Fail on Heterogeneous Clinical MRI: A New Dataset and Deep Learning-Based Solutions. (PMID: [41612110](https://pubmed.ncbi.nlm.nih.gov/41612110/))
-   **雑誌名**: Journal of imaging informatics in medicine
-   **公開日**: 2026-01-29
-   **著者名**: Junjie Wu, Joshua D Brown, Ranliang Hu 他
-   **所属**: Department of Neurology, School of Medicine, Emory University, Atlanta, GA, USA. 他
-   **タスク**: 異種臨床MRIにおける白質病変（WMH）のセグメンテーション。
-   **データ**: 2006年から2022年にかけて71台の異なるスキャナーから取得された195枚のルーチン脳MRIスキャン。
-   **手法**: 既存のベンチマーク手法を評価後、新しいデータセットでnnU-Netを訓練したRobust-WMH-UNetと、MedSAMをファインチューニングしたRobust-WMH-SAMを開発。
-   **成果**: ベンチマーク手法は汎用性が低く、小さな病変の見落としや偽陽性が頻発。Robust-WMH-UNetは優れた精度（中央値Dice 0.768）と特異度を達成。Robust-WMH-SAMも限られた訓練で競争力のある性能（中央値Dice最大0.750）を達成。
-   **新規性**: 異種臨床MRIデータセット（71台のスキャナーからのデータを含む）を公開し、既存のWMHセグメンテーション手法の汎用性の低さを示した上で、nnU-NetとFoundation Model（MedSAM）の適応による堅牢な解決策を提示。
-   **限界**: 記載なし。

### Automated deep learning for detection and measurement of adrenal masses in contrast-enhanced abdominal CT. (PMID: [41609765](https://pubmed.ncbi.nlm.nih.gov/41609765/))
-   **雑誌名**: European radiology
-   **公開日**: 2026-01-29
-   **著者名**: Taek Min Kim, Yunna Lee, June Young Seo 他
-   **所属**: Department of Radiology, Seoul National University Hospital, Seoul, Korea. 他
-   **タスク**: 造影腹部CTにおける副腎腫瘤の完全自動検出と測定。
-   **データ**: 副腎腫瘤あり（155例）およびなし（260例）の415枚のCTスキャンでモデル開発。外部テストセット（995例）と内部テストセット2（50例）で検証。
-   **手法**: 事前学習済みセグメンテーションモデルで副腎マスクを自動生成し、U-Netベースのセグメンテーションネットワークを訓練。
-   **成果**: 内部テストセット1でAUC 0.99、平均Diceスコア0.812。外部テストセットでAUC 0.94、感度89.6%、特異度96.9%。内部テストセット2で50例中44例の副腎腫瘤を同定。予測直径のICCは0.848（CT測定値と比較）および0.855（病理測定値と比較）。
-   **新規性**: 放射線科医が見落としがちな副腎腫瘤を、造影腹部CTで高精度に自動検出・測定する深層学習モデルを開発し、実世界データでその有効性を検証。
-   **限界**: 記載なし。

### Evaluation of a Deep Learning Tool for Detecting Large Vessel Occlusion and Intracranial Hemorrhage on Noncontrast Computed Tomography Scans. (PMID: [41608726](https://pubmed.ncbi.nlm.nih.gov/41608726/))
-   **雑誌名**: Stroke (Hoboken, N.J.)
-   **公開日**: 2025-11
-   **著者名**: Xabier Urra, Ansaar Rai, Maria Hernandez 他
-   **所属**: Hospital Clínic de Barcelona Barcelona Spain. 他
-   **タスク**: 非造影CT（NCCT）スキャンにおける頭蓋内出血（ICH）または前循環大血管閉塞（LVO）の検出。
-   **データ**: 6つの脳卒中センターからの多施設国際レトロスペクティブコホート。ICH検出用に200患者、LVO検出用に382患者。
-   **手法**: 2つの自動AI深層学習モジュール（Methinks社製）を使用。
-   **成果**: NCCT-ICH検出モジュールは感度94.9%、特異度99.0%、AUC 0.974。NCCT-LVO検出モジュールは感度81.6%、特異度87.1%、AUC 0.915。
-   **新規性**: 脳卒中急性期において、NCCTのみでICHとLVOの両方を高精度に検出するAIモジュールを多施設で評価し、その臨床的有用性を示した。
-   **限界**: 記載なし。

## 総括・編集後記

今週は、CT/MRIを用いた診断支援AIの臨床応用可能性と汎用性向上に焦点を当てた研究が目立ちました。特に多施設データで検証されたモデルは、自施設でのPoCや導入を検討する際の有力な候補となり得るでしょう。ただし、AIモデルの導入に際しては、自施設のデータ特性との適合性や、継続的な性能監視が不可欠です。
