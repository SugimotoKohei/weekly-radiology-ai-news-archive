## 今週の Top Picks

### Agatston-2.0: A next-generation AI-based coronary calcium quantification approach to improve risk stratification among individuals with zero Agatston scores - Part I: An AI-CVD Study within the Multi-Ethnic Study of Atherosclerosis and Framingham Heart Study. (PMID: [42828238](https://pubmed.ncbi.nlm.nih.gov/42828238/))
*   **雑誌名**: American journal of preventive cardiology
*   **公開日**: 2026-12
*   **著者名**: Morteza Naghavi, Amir Azimi, Kyle Atlas 他
*   **所属**: HeartLung.AI, Houston, TX 77021, USA. 他
*   **タスク**: 従来のAgatstonスコアで冠動脈石灰化ゼロとされた個人の心血管リスク層別化を、AIベースの新しい冠動脈石灰化定量化手法「Agatston-2.0」を用いて改善する。
*   **データ**: Multi-Ethnic Study of Atherosclerosis (MESA) および Framingham Heart Study (FHS) から、ベースラインCAC=0の参加者3,965人のCTデータ。
*   **手法**: AIフレームワークAgatston-2.0を開発し、冠動脈の自動セグメンテーションと、固定閾値なしの連続的なボクセル単位の石灰化定量化を行った。Cox比例ハザードモデルを用いて、CHD発生との関連を評価した。
*   **成果**: CAC=0の参加者の21.7%でAI-CAC>0を検出し、AI-CAC>0の群はAI-CAC=0の群より20年CHD発生率が有意に高かった（7.7% vs. 3.8%, p<0.0001）。従来の危険因子調整後もAI-CAC>0はCHD発生と独立して関連（HR 1.71）した。
*   **新規性**: 従来のAgatstonスコアでは見逃されていた微細な冠動脈石灰化をAIが検出し、CAC=0の患者群における心血管リスク層別化を改善する新しいアプローチを提示した。
*   **限界**: 追加コホートでの検証が必要である。

### Multicenter, Multivendor Development and Validation of Automated Liver Prescription. (PMID: [42827325](https://pubmed.ncbi.nlm.nih.gov/42827325/))
*   **雑誌名**: Journal of magnetic resonance imaging : JMRI
*   **公開日**: 2026-10-02
*   **著者名**: Garrett C Fullerton, Jitka Starekova, Collin J Buelo 他
*   **所属**: Department of Radiology, University of Wisconsin-Madison, Madison, Wisconsin, USA. 他
*   **タスク**: 肝臓MRIの自動処方モデルを開発・検証し、オペレーター間変動の低減と検査時間の短縮を目指す。
*   **データ**: 3つの施設、3つのベンダー（GE HealthCare, Philips Healthcare, Siemens Healthineers）から収集された11,012人の肝臓MRIデータ。
*   **手法**: YOLOv8オブジェクト検出モデルを訓練し、ローカライザー画像上で肝臓、体幹、腕を検出した。自動処方精度は3次元Intersection-over-Union (IoU) で評価した。
*   **成果**: 単一のマルチベンダーモデルが正確な肝臓MRI自動処方を達成し、ベンダー、磁場強度、ローカライザーシーケンス、患者因子による臨床的に意味のある性能差はなかった（中央値IoU 0.90-0.91）。
*   **新規性**: 既存研究が単一ベンダーに限定される中、大規模なマルチセンター・マルチベンダーデータセットを用いて、肝臓MRIの自動処方モデルの汎用性と堅牢性を実証した。
*   **限界**: 記載なし。

### Unsupervised high-resolution 3D MRI motion correction via physics-informed implicit neural representations. (PMID: [42822185](https://pubmed.ncbi.nlm.nih.gov/42822185/))
*   **雑誌名**: Medical image analysis
*   **公開日**: 2026-09-29
*   **著者名**: Haoyuan Le, Qing Wu, Bowen Li 他
*   **所属**: School of Biomedical Engineering, Shanghai Jiao Tong University, Shanghai, China. 他
*   **タスク**: 高分解能3D MRIにおけるモーションアーチファクトを、外部ナビゲーターや教師なしで補正する。
*   **データ**: シミュレーションされた摂動データと、実際のin-vivo高分解能ラジアルスキャンデータ。
*   **手法**: 物理情報に基づくImplicit Neural Representation (INR) を提案。微分可能な剛体モーション演算子をINRの順モデルに組み込み、生k空間データからモーション軌跡とモーションフリーボリュームを同時に最適化する。
*   **成果**: 提案手法は、モーション推定精度、構造保存、下流のセグメンテーションを改善し、被験者やプロトコル間で汎用性を示した。kooshball撮像において、モーションが10°/20mmの重度でもナビゲーターベースの手法を約2dB上回った。
*   **新規性**: 外部ナビゲーターや教師データなしで、物理情報に基づくINRを用いて3D MRIのモーション補正を可能にする統一的なフレームワークを確立し、高分解能3D撮像の主要なボトルネックを解決する。
*   **限界**: 記載なし。

### Artificial intelligence for evaluation of magnetic resonance imaging-detected extramural vascular invasion in rectal cancer. (PMID: [42821531](https://pubmed.ncbi.nlm.nih.gov/42821531/))
*   **雑誌名**: PLOS digital health
*   **公開日**: 2026-10
*   **著者名**: Haitao Huang, Lili Feng, Min-Er Zhong 他
*   **所属**: Department of Radiology, Guangdong Provincial People's Hospital (Guangdong Academy of Medical Sciences), Southern Medical University, Guangzhou, China. 他
*   **タスク**: 直腸癌におけるMRI検出壁外血管浸潤（mrEMVI）をAIで自動評価し、予後予測に活用する。
*   **データ**: 2,501人の直腸癌患者の多施設レトロスペクティブMRIデータ（トレーニング1,830人、外部テスト671人）。
*   **手法**: nnUNetベースのセグメンテーションモデルを訓練し、mrEMVIのボクセルレベルでの局在化と可視化を自動化。Diceスコア、Cohenのκ、Kaplan-Meier生存分析、多変量Cox回帰で評価した。
*   **成果**: モデルは内部検証で良好なセグメンテーション性能（腫瘍Dice 0.850）を示し、外部テストコホートで81.5%および84.7%の分類精度を達成。上級放射線科医との実質的な一致（κ=0.713-0.736）を示した。AI-mrEMVI+患者はAI-mrEMVI-患者よりも3年無病生存率および5年全生存率が有意に低かった。
*   **新規性**: mrEMVIの主観性と観察者間変動を克服するため、ボクセルレベルのセグメンテーションに基づく客観的かつスケーラブルなAIフレームワークを確立し、その予後予測価値を大規模多施設データで検証した。
*   **限界**: 記載なし。

### Automated Aortic Valve Calcification Scoring: Multicenter External Validation of a Deep Learning Algorithm. (PMID: [42820889](https://pubmed.ncbi.nlm.nih.gov/42820889/))
*   **雑誌名**: JACC. Advances
*   **公開日**: 2026-09-23
*   **著者名**: Jimmy Zheng, Eren Alkan, Aniruddha Deshpande 他
*   **所属**: Division of Cardiovascular Medicine, Department of Medicine, Stanford University, California, USA. 他
*   **タスク**: 非ゲート非造影胸部CT画像から大動脈弁石灰化（AVC）を自動定量化し、大動脈弁狭窄症（AS）の機会的スクリーニングに活用する。
*   **データ**: 米国とブラジルの8つの医療システム、33施設から収集された非ゲート非造影胸部CTデータ。トレーニング1,446人、検証361人、独立したホールドアウトテスト239人。
*   **手法**: 畳み込みニューラルネットワーク（CNN）を開発。専門家による手動セグメンテーションを基準として、Agatstonスコアの相関、Bland-Altman分析、AS重症度分類の感度・特異度を評価した。
*   **成果**: アルゴリズムは専門家の基準と高い相関（r=0.99）を示し、バイアスは最小限（平均差5.2 AU）。中等度から重度のASに対する感度0.92、特異度0.98を達成。性能は人口統計学的サブグループやCT技術パラメータ間で一貫していた。
*   **新規性**: 大規模なマルチセンター外部検証を通じて、非ゲート非造影胸部CTからAVCを自動定量化するAIアルゴリズムが、専門家と同等の性能を持つことを実証し、ASの機会的スクリーニングの可能性を強く示唆した。
*   **限界**: 臨床転帰改善の検証には前向き研究が必要である。

## 総括・編集後記

今週は、CT/MRIにおけるAIの応用が多岐にわたり、特に診断支援、ワークフロー改善、画像品質向上、予後予測といった臨床的価値の高い領域で、マルチセンター・マルチベンダーでの検証や、従来の診断基準の限界を超えるAIの可能性が示された論文が目立ちました。臨床現場でのAI導入を検討する際は、マルチベンダー対応や大規模な外部検証がなされたモデルに注目し、PoCを通じて自施設での性能評価を行うことが推奨されます。AIモデルの性能は、開発環境と異なるドメイン（患者集団、撮像システム、ワークフロー）で低下する可能性があるため、外部バリデーションの重要性を常に意識し、AIの出力は批判的に評価する必要があります。
