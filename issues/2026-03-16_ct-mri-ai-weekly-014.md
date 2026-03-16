## 今週の Top Picks

### Beyond whole-image learning: anatomically partitioned deep learning models for superior sinonasal disease classification. (PMID: [41832258](https://pubmed.ncbi.nlm.nih.gov/41832258/))
*   **雑誌名**: European radiology
*   **公開日**: 2026-03-15
*   **著者名**: Song Li, Xiang-Hai Hu, Song Luo 他
*   **所属**: Department of Otorhinolaryngology, The First Affiliated Hospital with Nanjing Medical University, Nanjing, China. 他
*   **タスク**: 副鼻腔疾患のCT画像からの診断分類
*   **データ**: 2947件のCT検査（うち150件は手動セグメンテーション）、外部テストデータあり。
*   **手法**: nnU-Net v2による自動解剖学的分割後、13の副鼻腔サブ領域ごとに疾患特異的ネットワークを訓練。全画像分類器と比較。
*   **成果**: 解剖学的分割モデルは平均Dice係数0.739。外部テストコホートで平均AUC 0.801（全画像モデルは0.587）。73の診断ラベル中42でAUCが統計的に有意に改善（平均0.214増加）。
*   **新規性**: 解剖学的異質性を考慮し、CT画像を解剖学的に分割してから疾患特異的ネットワークを訓練することで、全画像学習よりも診断精度を大幅に向上させた。
*   **限界**: 手動セグメンテーションの労力、モデルの一般化可能性のさらなる検証。

### A Multicenter Study on Deep Learning Model-Assisted Detection of Brain Metastases in MR Images. (PMID: [41832083](https://pubmed.ncbi.nlm.nih.gov/41832083/))
*   **雑誌名**: Academic radiology
*   **公開日**: 2026-03-13
*   **著者名**: Meiqi Hua, Liyong Zhuo, Yu Zhang 他
*   **所属**: Department of Radiology, Affiliated Hospital of Hebei University/School of Clinical Medicine, Baoding, People's Republic China. 他
*   **タスク**: MRI画像における脳転移の検出
*   **データ**: 950人の患者データ（訓練・テスト）、423人の患者データ（バリデーション）。
*   **手法**: 深層学習ベースの脳転移検出モデル（BMDM）を開発。放射線科医のみ、BMDMのみ、BMDM支援下の3つの読影モードを比較。AFROC法で評価。
*   **成果**: BMDM支援により読影時間が30.87%短縮、AFROC-AUCが0.837から0.954に改善、感度が0.685から0.916に向上。経験の浅い放射線科医で感度改善が顕著（24.59% vs 22.03%）。3mm以下の病変で33.45%、島皮質病変で43.00%の感度向上。
*   **新規性**: 多施設データで深層学習モデルの脳転移検出における診断性能と時間効率の向上を検証し、特に経験の浅い医師や微小病変、特定の部位での改善を示した。
*   **限界**: レトロスペクティブ研究であること、モデルの汎用性に関するさらなる検証。

### Prognostic value of end-to-end deep learning assessment of myocardial scar and microvascular obstruction on late gadolinium enhancement cardiovascular magnetic resonance. (PMID: [41831720](https://pubmed.ncbi.nlm.nih.gov/41831720/))
*   **雑誌名**: Journal of cardiovascular magnetic resonance : official journal of the Society for Cardiovascular Magnetic Resonance
*   **公開日**: 2026-03-12
*   **著者名**: Pei Yang, Shuang Leng, Dexiang Zong 他
*   **所属**: Department of Radiology, The Second Affiliated Hospital, Jiangxi Medical College, Nanchang University, Nanchang, China. 他
*   **タスク**: LGE-CMR画像における心筋瘢痕および微小血管閉塞（MVO）の自動セグメンテーションと予後予測
*   **データ**: 567人のAMI患者からの3874枚のLGE画像（409人訓練/内部テスト、158人外部テスト）。
*   **手法**: LGE-CMRnetを開発。YOLOv8で心臓局在化、nnU-Netで心筋、瘢痕、MVOの同時セグメンテーション。Cox回帰でMACEの予後予測を評価。
*   **成果**: 迅速な処理（0.05秒/画像）と高いセグメンテーション精度。外部バリデーションで瘢痕の平均DSC 0.83、MVOの平均DSC 0.88。専門家との体積相関も良好（瘢痕: r=0.90; MVO: r=0.98）。予後予測性能は専門家分析に匹敵。
*   **新規性**: 心筋梗塞後のLGE-CMRにおける心筋瘢痕と微小血管閉塞の自動定量化をエンドツーエンドの深層学習パイプラインで実現し、その予後予測価値を専門家分析と同等レベルで示した。
*   **限界**: 単一施設での訓練データ、MACEイベントの多様性への対応。

### Automated CTA-Derived Collateral Grading and Morphologic Metrics for Enhanced Prediction of Post-Stroke Outcomes. (PMID: [41826063](https://pubmed.ncbi.nlm.nih.gov/41826063/))
*   **雑誌名**: AJNR. American journal of neuroradiology
*   **公開日**: 2026-03-13
*   **著者名**: Aditi Deshpande, Jing Wang, Krzysztof M Bochenek 他
*   **所属**: From the University of California, Riverside, CA; Division of Vascular Neurology and Neurocritical Care, Inova Neuroscience and Spine Institute, Inova Fairfax Medical Campus (IFMC), Falls Church, VA; 他
*   **タスク**: CTA画像からの側副血行路の自動定量化と脳卒中後転帰予測
*   **データ**: 230人のAIS患者（血管内血栓除去術施行）のプロスペクティブ収集データ。
*   **手法**: 深層学習U-Netセグメンテーションフレームワークを用いてCTAから3D血管ネットワークを抽出し、形態学的指標（血管長、分岐、フラクタル次元、蛇行度）を算出。自動定量側副血行路指数（qCI）を導出。CTPのみ、CTAのみ、CTA+CTPの3モデルで転帰予測を比較。
*   **成果**: 自動qCIは専門家評価と高い一致度（精度0.863、Pearson R=0.880）。90日mRS予測において、CTAのみモデルはCTPのみモデルを上回る（AUROC 0.730 vs 0.645）。CTA+CTP結合モデルが最高の性能（AUROC 0.781）。
*   **新規性**: CTAから深層学習を用いて側副血行路を自動定量化するqCIを開発し、CTPよりも優れた脳卒中後転帰予測性能を示し、CTPが利用できない環境での臨床的有用性を提示した。
*   **限界**: 単一施設での検証、より大規模な多民族コホートでの外部バリデーションが必要。

### Efficient Deep Ladle-Net for fast universal 3D lesion segmentation on chest-abdomen-pelvis computed tomography. (PMID: [41818858](https://pubmed.ncbi.nlm.nih.gov/41818858/))
*   **雑誌名**: Computerized medical imaging and graphics : the official journal of the Computerized Medical Imaging Society
*   **公開日**: 2026-03-11
*   **著者名**: Ching-Wei Wang, Ting-Sheng Su, Yu-Ching Lee
*   **所属**: Graduate Institute of Biomedical Engineering, National Taiwan University of Science and Technology, Taipei, Taiwan.
*   **タスク**: 胸腹骨盤CTにおける汎用3D病変セグメンテーション（10種類の病変）
*   **データ**: 11の公開3D CTデータセットと2つのプライベートデータセットからなる7151病変の大規模コホート。
*   **手法**: Deep Ladle-Netを提案。多種類の病変を同時にセグメンテーションするために設計された効率的な深層学習フレームワーク。
*   **成果**: 提案モデルは、5つの最先端手法を上回り、ULS23チャレンジで3位を獲得。拡張研究では10種類の病変で平均Dice 0.773±0.146を達成。特に腹部病変、腎臓病変、縦隔病変、肺結節でDice 0.78以上。処理時間は1ケースあたり2秒未満と高速。
*   **新規性**: 胸腹骨盤CTにおいて、10種類の異なる病変を単一フレームワークで高速かつ高精度に汎用的に3DセグメンテーションできるDeep Ladle-Netを開発し、大規模データセットでその有効性を示した。
*   **限界**: さらなるデータ正規化とデータ拡張による性能向上の余地、臨床現場での運用検証。

## 総括・編集後記

今週は、CT/MRI画像におけるAIの診断支援、セグメンテーション、予後予測への応用が多岐にわたり報告されました。特に、解剖学的知識の統合や多施設検証、汎用的な病変検出など、臨床導入に向けた実用性と信頼性を高める研究に注目し、自施設でのPoCや評価を検討する良い機会となるでしょう。AIモデルの性能評価においては、外部バリデーションの有無や、特定のサブグループにおける性能差（例：経験の浅い医師への効果）に留意し、今後の研究ではさらなる解釈可能性とバイアス評価が求められます。
