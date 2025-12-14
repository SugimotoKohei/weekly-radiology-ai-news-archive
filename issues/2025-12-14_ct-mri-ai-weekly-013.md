## 今週の Top Picks

### Application value of prostate-specific antigen density combined with multiparametric MRI in early diagnosis of prostate cancer. (PMID: [41389905](https://pubmed.ncbi.nlm.nih.gov/41389905/))
*   **雑誌名**: Magnetic resonance imaging
*   **公開日**: 2025-12-11
*   **著者名**: Di Wu, Zhaobing Tang
*   **所属**: Department of Urology, The First Affiliated Hospital of Chongqing Medical University, Chongqing, China.
*   **タスク**: PSAグレーゾーン (4-10 ng/mL) およびPI-RADS 3の前立腺癌の早期診断
*   **データ**: mpMRI (T2WI, DWI, ADC) とPSAD (Prostate-specific antigen density)
*   **手法**: ディープラーニングモデルを開発し、Cross-modal attention-guided (CM-AG) fusion moduleを用いてPSADとmpMRIの特徴を統合。
*   **成果**: PSAグレーゾーンコホートでAUC=0.89、PI-RADS 3でAUC=0.83を達成し、単一モダリティMRIやPI-RADS単独を上回る診断性能を示した。前立腺体積が大きい患者では特異度が10.2%向上した。
*   **新規性**: 臨床指標であるPSADとmpMRI画像をクロスモーダルアテンション機構で統合するディープラーニングモデルを開発し、特に診断が困難なサブグループ（PSAグレーゾーン、PI-RADS 3）での診断性能向上を実証した。
*   **限界**: 記載なし。

### Impact of vessel suppression AI on reading efficiency and nodule detection in CT chest. (PMID: [41390262](https://pubmed.ncbi.nlm.nih.gov/41390262/))
*   **雑誌名**: Current problems in diagnostic radiology
*   **公開日**: 2025-11-26
*   **著者名**: Kevin T Chorath, Evan Jacobs, Ken Tharp 他
*   **所属**: Department of Radiology, University of Washington, Seattle, WA, USA. 他
*   **タスク**: 胸部CTにおける血管抑制 (VS) AIソフトウェアの読影効率と肺結節検出への実臨床での影響評価
*   **データ**: 単一施設で解釈された8,835件の胸部CT検査（2023年1月～2024年2月）
*   **手法**: VSソフトウェア導入前後の読影時間と肺結節検出率を比較。結果は自然言語処理と手動検証で抽出された。
*   **成果**: 研修医の平均読影時間は19.1分から12.2分に短縮し、点状結節検出率は13.0%から24.2%に向上した。指導医も読影時間短縮と点状結節検出率のわずかな向上を示した。
*   **新規性**: 血管抑制AIソフトウェアの実臨床導入が、研修医と指導医の両方で読影効率を改善し、特に小さな結節の検出率を向上させることを大規模な実世界データで示した。
*   **限界**: 2mm未満の結節検出の臨床的意義は依然として不明である。

### Detection of phase-binning and interpolation artifacts in 4-dimensional computed tomography imaging using deep learning and rule-based approaches. (PMID: [41389065](https://pubmed.ncbi.nlm.nih.gov/41389065/))
*   **雑誌名**: Medical physics
*   **公開日**: 2025-12
*   **著者名**: Jorge Cisneros, Nathan H Feldt, Yevgeniy Vinogradskiy 他
*   **所属**: Department of Biomedical Engineering, University of Texas at Austin, Austin, Texas, USA. 他
*   **タスク**: 4DCT画像における位相ビンニングおよび補間アーチファクトの検出
*   **データ**: 9つの異なる臨床4DCTデータセットから系統的に合成された位相ビンニングおよび補間アーチファクトを含むグラウンドトゥルースデータ
*   **手法**: 3Dディープラーニングモデル (nnUNet, SwinUNETR) を位相ビンニングアーチファクト検出に、ヒューリスティックなルールベース手法を補間スライス検出に適用。合成データで学習。
*   **成果**: nnUNetとSwinUNETRモデルは平均0.957の検出精度を達成し、最先端の性能を示した。SwinUNETRは高速な実行時間も持ち、リアルタイムでのアーチファクト検出に貢献する可能性を示唆した。
*   **新規性**: 複数の臨床データセットから生成された合成データを用いて、3Dディープラーニングモデルとルールベース手法を組み合わせることで、4DCT画像の位相ビンニングおよび補間アーチファクトをボクセルレベルで高精度に検出する手法を開発した。
*   **限界**: 合成データでの学習であり、実データでの汎化性能のさらなる検証が必要である。

### Enhanced Spinal Cord Lesion Detection in MS Using White-Matter-Nulled 3D MPRAGE with Deep Learning Reconstruction. (PMID: [41381352](https://pubmed.ncbi.nlm.nih.gov/41381352/))
*   **雑誌名**: AJNR. American journal of neuroradiology
*   **公開日**: 2025-12-11
*   **著者名**: Fanny Munsch, Amaury Ravache, Takayuki Yamamoto 他
*   **所属**: Institut de Bio-imagerie IBIO, Université Bordeaux, Bordeaux, France. 他
*   **タスク**: 多発性硬化症 (MS) における脊髄病変の検出
*   **データ**: MSまたは臨床的孤立症候群患者38名の3T脊髄MRIデータ (2D T2-weighted FSE, 2D STIR, 3D MPRAGE, 3D WMn)
*   **手法**: 新しい3D white-matter-nulled (WMn) MPRAGEシーケンスにディープラーニングによるノイズ除去を適用し、従来のシーケンスと比較。4名の神経放射線科医が病変数、検出確信度、画像品質を評価した。
*   **成果**: 3D WMnシーケンスは、従来の2D T2強調FSE (+62%)、2D STIR (+42%)、3D MPRAGE (+34%) よりも有意に多くの病変を検出した。
*   **新規性**: ディープラーニングベースのノイズ除去を組み合わせた3D white-matter-nulled (WMn) MPRAGEシーケンスが、従来のMRIシーケンスを上回り、多発性硬化症における脊髄病変検出を大幅に改善することを示した。
*   **限界**: 比較的小規模な単一施設データでの評価である。

### Quantum AI for psychiatric diagnosis: enhancing dementia classification with quantum machine learning. (PMID: [41383998](https://pubmed.ncbi.nlm.nih.gov/41383998/))
*   **雑誌名**: Frontiers in psychiatry
*   **公開日**: 2025
*   **著者名**: Javaria Amin, Muhammad Umair Ali, Muhammad Zubair Islam 他
*   **所属**: Department of Computer Science, Rawalpindi Women University, Rawalpindi, Pakistan. 他
*   **タスク**: MRI画像を用いた認知症の分類 (AD, MCI, NC)
*   **データ**: ADNI-1, ADNI-2, OASIS-2 MRIデータセット
*   **手法**: ハイブリッド量子古典畳み込みニューラルネットワーク (QCNN) を提案。MRI画像からROIを抽出し、ピクセル値を量子ビットとしてエンコード。量子回路で量子特徴マップを生成し、古典CNNに入力。汎化性能向上のため知識蒸留 (KD) フレームワークも導入。
*   **成果**: KDなしでADNI-1で0.9523、ADNI-2で0.9611、OASIS-2で0.9412の精度を達成。KDありでは最大0.9978の精度を達成し、既存手法を上回る性能を示した。
*   **新規性**: MRI画像からの認知症分類において、量子機械学習と古典ディープラーニングを組み合わせたハイブリッド量子古典畳み込みニューラルネットワーク (QCNN) を提案し、さらに知識蒸留を適用することで、高い精度と効率を実現した。
*   **限界**: 量子コンピューティングのハードウェアの制約があり、実臨床への導入にはさらなる検証と技術発展が必要である。

## 総括・編集後記

今週は、AIが診断精度向上、ワークフロー効率化、そして最先端技術の応用という多岐にわたる側面で医用画像診断に貢献していることが目立ちました。特に、実臨床データで効果が示された血管抑制AIや、新しいMRIシーケンスとDLの組み合わせは、自施設での導入やPoCを検討する価値があるでしょう。量子AIのような新技術は将来性が高いものの、実用化には外部バリデーションや倫理的側面、計算資源の課題を継続的に注視する必要があります。
