## 今週の Top Picks

### Improved visualization of perivascular spaces on T2-weighted imaging with deep learning-based denoising and super-resolution reconstruction. (PMID: [42000915](https://pubmed.ncbi.nlm.nih.gov/42000915/))
*   **雑誌名**: Scientific reports
*   **公開日**: 2026-04-18
*   **著者名**: Yuya Hirano, Noriyuki Fujima, Hiroyuki Kameda 他
*   **所属**: 北海道大学病院 放射線技術部、診断・IVR放射線科、北海道大学 歯学研究科 放射線科、Philips Japan
*   **タスク**: T2強調画像における血管周囲腔 (PVS) の可視化改善
*   **データ**: 健常ボランティア10名の脳MRI (T2WI)
*   **手法**: 深層学習ベースのデノイズと超解像 (SR-DL) を用いて、異なるボクセルサイズで取得されたT2WI画像を再構成。PVSの検出数、コントラスト比、自動セグメンテーション性能、定性的可視性を評価。
*   **成果**: SR-DLは、CS-SENSEと比較して、PVSの検出数、コントラスト比、自動セグメンテーション性能、定性的可視性を有意に向上させた。取得時間を延長することなくPVSの検出性と可視性を改善。
*   **新規性**: 取得時間を延長することなく、深層学習ベースのデノイズと超解像を組み合わせることで、T2強調画像におけるPVSの定量的検出性と定性的可視性を大幅に向上させた。
*   **限界**: 健常ボランティアのみを対象とした小規模研究であり、疾患患者での有効性や汎用性は今後の課題。

### DiSCNet: Directional Split Convolution for compute-efficient brain tumor diagnosis. (PMID: [42000653](https://pubmed.ncbi.nlm.nih.gov/42000653/))
*   **雑誌名**: Computational biology and chemistry
*   **公開日**: 2026-04-12
*   **著者名**: Shahid Mohammad Ganie, Ishak Pacal
*   **所属**: King Faisal University, Igdir University, Nakhchivan State University, Fenerbahçe University
*   **タスク**: MRIからの脳腫瘍（グリオーマ、髄膜腫、下垂体腫瘍、非腫瘍）の分類
*   **データ**: 5つの公開MRIリポジトリから構築された統一ベンチマークデータセット（17,888画像、4クラス）
*   **手法**: InceptionNeXtに着想を得た階層的設計と、新しいDirectional Split Convolution (DiSC) ブロックを中心とした軽量アーキテクチャDiSCNetを提案。Global Response NormalizationとEfficient Channel Attentionを組み込み、特徴の安定性とチャネル選択性を向上。
*   **成果**: DiSCNetは、71の既存モデルと比較して最高の全体性能（精度0.9922、F1スコア0.9923）を達成し、かつ2.78Mパラメータと非常に軽量であった。Grad-CAMにより病変関連領域に焦点を当てていることが示された。
*   **新規性**: 脳腫瘍MRI分類において、Directional Split Convolution (DiSC) ブロックを核とする軽量アーキテクチャDiSCNetを提案し、大幅に少ないパラメータ数で既存の大型モデルを凌駕する性能と高い汎化性能を示した。
*   **限界**: 公開データセットでの評価であり、多様な臨床プロトコルやスキャナーの違いに対するロバスト性のさらなる検証が必要。

### Towards interpretable AI in personalized medicine through a radiological-biological radiomics dictionary linking semantic Lung-RADS and imaging radiomics features. (PMID: [41997262](https://pubmed.ncbi.nlm.nih.gov/41997262/))
*   **雑誌名**: Journal of biomedical informatics
*   **公開日**: 2026-04-15
*   **著者名**: Ali Fathi Jouzdani, Shahram Taeb, Mehdi Maghsudi 他
*   **所属**: Technological Virtual Collaboration (TECVICO Corp.), Hamadan University of Medical Sciences, Guilan University of Medical Sciences, BC Cancer Research Institute, University of British Columbia
*   **タスク**: CTベースの肺がんスクリーニングにおけるAIの解釈可能性向上
*   **データ**: The Cancer Imaging Archive (TCIA) の12コレクションから977患者の画像および臨床データ
*   **手法**: Lung-RADSのセマンティック特徴とRadiomics特徴を関連付ける「放射線学的-生物学的Radiomics辞書」を開発。半教師あり学習フレームワークとSHAP解析を用いて、特徴の重要性とLung-RADS記述子との対応を評価。
*   **成果**: 開発された辞書は、Lung-RADSの10のセマンティック特徴を対応するRadiomics特徴に変換。半教師あり学習パイプラインは平均検証精度0.79を達成し、SHAP解析によりRadiomics特徴がLung-RADS記述子（例：減衰、辺縁不整、スピキュラ）に対応することが確認された。
*   **新規性**: Lung-RADSのセマンティックな記述子と定量的Radiomics特徴を関連付ける辞書を開発し、AIの予測が臨床医にとって解釈可能となるフレームワークを提案した。
*   **限界**: 辞書の開発は文献レビューと専門家レビューに基づくものであり、網羅性や普遍性の検証が必要。半教師あり学習の精度はまだ改善の余地がある。

### Deep learning image reconstruction optimizes coronary artery calcium quantification. (PMID: [41987920](https://pubmed.ncbi.nlm.nih.gov/41987920/))
*   **雑誌名**: Frontiers in cardiovascular medicine
*   **公開日**: 2026
*   **著者名**: Tao Zhou, Ming Liu, Ting Wu 他
*   **所属**: 山東第一医科大学附属人民病院 放射線科、煙台毓璜頂病院 放射線科、Canon Medical System (China)、煙台山病院 放射線科
*   **タスク**: 冠動脈石灰化 (CAC) 定量化における深層学習再構成 (DLR) の効果評価
*   **データ**: カルシウムスコアリングおよび冠動脈CTアンギオグラフィ検査を受けた患者の画像
*   **手法**: フィルタ補正逆投影 (FBP)、ハイブリッド反復再構成 (HIR)、深層学習再構成 (DLR) の3つのアルゴリズムで画像を再構成。画像ノイズ、SNR、CNR、主観的画質、Agatstonスコア、カルシウム体積・質量、リスク分類を比較。
*   **成果**: DLRはFBPおよびHIRと比較して、画像ノイズを大幅に低減し、SNRとCNRを改善した。CAC定量化の一貫性が向上し、HIRと比較してリスク再分類が減少した。
*   **新規性**: 深層学習再構成 (DLR) が、従来の再構成法と比較して、冠動脈石灰化の定量化における画像品質と一貫性を有意に改善し、リスク分類の再分類を低減することを示した。
*   **限界**: レトロスペクティブな単施設研究であり、異なるCTスキャナーやプロトコルでのDLRの汎用性や、長期的な臨床アウトカムへの影響は不明。

### Commercial AI Model Diagnostic Accuracy for Intracranial Large- and Medium-Vessel Occlusion in Emergency CT Angiography. (PMID: [41983922](https://pubmed.ncbi.nlm.nih.gov/41983922/))
*   **雑誌名**: Radiology. Artificial intelligence
*   **公開日**: 2026-04-15
*   **著者名**: Henrik Andersson, Björn Hansen, Johan Wassélius
*   **所属**: Skåne University Hospital 医用画像・生理学部門、Lund University 臨床科学部門 脳卒中画像研究グループ
*   **タスク**: 緊急CTアンギオグラフィ (CTA) における頭蓋内大・中血管閉塞 (LVO/MeVO) の自動検出
*   **データ**: 10病院地域で2024年3月～7月に取得された3,031例の成人頭頸部CTA
*   **手法**: 市販AIツールAIDOC-VOの診断精度を、臨床放射線科医のレポートと比較して評価する前向き診断精度研究。AIモデルまたはレポートで陽性/疑いとされた症例は、参照標準確立のために盲検下で再読影された。
*   **成果**: 2,804例の有効なAI出力のうち、224例（8.0%）に血管閉塞が認められた。AIモデルは、意図された使用範囲内での血管閉塞検出において、感度81.7%（178/218）を達成し、臨床レポート（81.2%）と同等の性能を示した。
*   **新規性**: 頭蓋内大・中血管閉塞検出のための市販AIツールAIDOC-VOの、多施設緊急設定における前向き診断精度を評価した初の研究。
*   **限界**: AIモデルが有効な出力を得られなかった症例（92.5%）が存在し、その原因や影響についてはさらなる分析が必要。

## 総括・編集後記

今週は、医用画像AIにおける「実用性」と「効率性」に焦点が当たった論文が目立ちました。特に、深層学習を用いたMRIの画質向上や、CT画像再構成の最適化、そして市販AIの緊急診断における多施設での性能評価など、臨床現場への導入を意識した研究が進展しています。これらの進展は、日常臨床へのAI導入を加速させる可能性を秘めており、特に既存のCT/MRIデータから新たな情報を引き出す研究は、PoC（概念実証）や既存ワークフローへの統合を検討する上で参考になるでしょう。
