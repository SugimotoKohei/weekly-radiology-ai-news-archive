## 今週の Top Picks

### A deep learning-based algorithm for the automatic detection of focal liver lesions on multisequence enhanced MRI. (PMID: [42928023](https://pubmed.ncbi.nlm.nih.gov/42928023/))
*   **雑誌名**: Chinese medical journal
*   **公開日**: 2026-10-23
*   **著者名**: Jiahui Jiang, Lixue Xu, Xiaolan Zhang 他
*   **所属**: Department of Radiology, Beijing Friendship Hospital, Capital Medical University, Beijing 100050, China. 他
*   **タスク**: マルチシーケンス造影MRIにおける限局性肝病変の自動検出。
*   **データ**: 不明
*   **手法**: ディープラーニングベースのアルゴリズム。
*   **成果**: 不明
*   **新規性**: マルチシーケンス造影MRI画像から限局性肝病変を自動検出するディープラーニングアルゴリズムを提案。
*   **限界**: 不明

### Myocardial infarction detection framework using cardiac motion estimation with deformable registration field. (PMID: [42926307](https://pubmed.ncbi.nlm.nih.gov/42926307/))
*   **雑誌名**: International journal of computer assisted radiology and surgery
*   **公開日**: 2026-10-24
*   **著者名**: Ryosuke Sasaki, Yusuke Kurose, Junichi Iho 他
*   **所属**: Research Center for Advanced Science and Technology, The University of Tokyo, Tokyo, Japan. 他
*   **タスク**: 心臓CT画像からの心筋梗塞検出。
*   **データ**: 院内心臓CTデータセット。
*   **手法**: MambaMorph-Motion Infarction Detector (MMMID) フレームワーク。セマンティックセグメンテーション、MambaMorphを用いた逐次変形レジストレーション、DenseNetベースの分類モジュールを統合。
*   **成果**: 91.92%の精度、AUC 0.9335を達成。逐次モーションフィールドの統合によりリコールが向上し、解剖学的情報に補完的な診断情報を提供。
*   **新規性**: 心臓CT画像から心筋の解剖学的情報と推定されたモーション情報を統合することで心筋梗塞を検出するディープラーニングフレームワークを提案。
*   **限界**: 院内データセットのみでの評価。

### Multiple instance learning for differentiating neoplastic and non-neoplastic brain lesions using MR spectroscopy. (PMID: [42927027](https://pubmed.ncbi.nlm.nih.gov/42927027/))
*   **雑誌名**: Neuroimage. Reports
*   **公開日**: 2026-12
*   **著者名**: Iskra Gacheva, Diyuan Lu, Gerhard Kurz 他
*   **所属**: Institute for Neuroradiology, University Hospital Frankfurt, Frankfurt am Main, 60528, Germany. 他
*   **タスク**: MRスペクトロスコピー (MRS) を用いた脳病変の腫瘍性・非腫瘍性鑑別。
*   **データ**: 422患者 (7442スペクトル) のMRSデータ。
*   **手法**: Multiple Instance Learning (MIL) 問題として定式化。畳み込みニューラルネットワーク (CNN) と3Pool集約、データ拡張 (CNN-3Pool + DA) を組み合わせ。Attention-based MILも使用。
*   **成果**: 独立テストセットでAUC 0.82、感度 0.76、特異度 0.80を達成。経験豊富な神経放射線科医と比較して感度で優位。Attention機構により脂質やコリンピークなどの臨床的に確立されたスペクトル特徴が強調されることを可視化。
*   **新規性**: MRSベースの脳腫瘍分類をMIL問題として定式化し、不均一で弱くラベル付けされた臨床データからロバストな学習を可能にした。Attention機構による解釈可能性も提供。
*   **限界**: 不明

### Deep learning-based detection of pneumoperitoneum on computed tomography: performance and clinical feasibility. (PMID: [42911392](https://pubmed.ncbi.nlm.nih.gov/42911392/))
*   **雑誌名**: Abdominal radiology (New York)
*   **公開日**: 2026-10-22
*   **著者名**: Hyo Seon Ryu, Se Hoon Jung, Inhyeok Lee 他
*   **所属**: Division of Colon and Rectal surgery, Department of Surgery, Korea University Anam Hospital, Seoul, Korea, Republic of. 他
*   **タスク**: CT画像における気腹の自動検出。
*   **データ**: 単一三次医療センターの263患者 (外科的に確認された消化管穿孔) と78正常対照のCTスキャン。
*   **手法**: Segmentation-based deep learningモデル。no-new-Segment Anything Model (nnSAM) フレームワークを使用し、従来のnnUNetモデルと比較。
*   **成果**: 内部テストセットでnnSAMはnnUNetより高い検出率 (97.7% vs 90.7%) とDice係数 (0.739 vs 0.684) を達成。外部テストセットでも同様に高い検出率 (97.9% vs 85.4%) とDice係数 (0.863 vs 0.746) を示し、特に小容量の気腹で優位性を示した。
*   **新規性**: nnSAMフレームワークを気腹検出に適用し、従来のnnUNetと比較して特に小容量の気腹において高い精度とロバスト性を示した。
*   **限界**: 単一施設でのデータセット。

### Confidence-based classification of clinically significant prostate cancer on biparametric MRI using Monte Carlo dropout and Grad-CAM visualization. (PMID: [42908607](https://pubmed.ncbi.nlm.nih.gov/42908607/))
*   **雑誌名**: Frontiers in oncology
*   **公開日**: 2026
*   **著者名**: Cheng Hao, Yuze Meng, Yong Peng 他
*   **所属**: Department of Radiology, the Affiliated Hospital of Guizhou Medical University, Guiyang, China.
*   **タスク**: バイパラメトリックMRI (bpMRI) を用いた臨床的意義のある前立腺癌 (csPCa) の信頼度ベース分類。
*   **データ**: 410患者のbpMRIデータ。
*   **手法**: VGG-16ネットワークを用いた分類モデル。Grad-CAMによる視覚的解釈可能性、Monte Carlo Dropout (MC-Dropout) による不確実性推定、およびリジェクションメカニズムを組み込み。
*   **成果**: 全予測で79.3%の全体精度。信頼度閾値0.8で80.8%の予測が保持され、その選択的精度は94.6% (偽陽性99、偽陰性2)。上級放射線科医 (90.8%) よりも高い精度 (94.6%) を達成。Grad-CAMはcsPCa疑い領域に高い活性化を示すことを定性的に確認。
*   **新規性**: bpMRIからcsPCaを分類する際に、信頼度スコアと視覚的解釈可能性 (Grad-CAM) を提供し、不確実な予測を拒否するメカニズムを組み込んだモデルを提案。
*   **限界**: ピクセルレベルのアノテーションとの定量的空間一致は評価されていない。

## 総括・編集後記

今週は、CT/MRIにおけるAIを用いた診断支援の進展が目立ち、特に肝病変、心筋梗塞、脳病変、気腹、前立腺癌といった多岐にわたる疾患領域で、AIが診断精度向上に貢献する可能性が示されました。これらの研究は、AIが特定の診断タスクにおいて専門医のパフォーマンスに匹敵するか、あるいは補完する可能性を示唆しており、自施設でのPoCや既存ワークフローへの統合可能性を検討する良い機会となるでしょう。ただし、多くの研究が単一施設データや限られたデータセットでの評価に留まっており、外部バリデーションの重要性や、AIの誤分類パターン、倫理的側面、そして実際の臨床運用における影響を継続的に注視する必要があります。
