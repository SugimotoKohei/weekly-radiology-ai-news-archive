## 今週の Top Picks

### Multimodality Multimask and Multitask Auto-Segmentation Network for Organs-at-Risk in Head and Neck Radiation Therapy. (PMID: [42472264](https://pubmed.ncbi.nlm.nih.gov/42472264/))
*   **雑誌名:** Advances in radiation oncology
*   **公開日:** 2026-11
*   **著者名:** Xiaochen Ni, Tianci Tang, Shengwei Li 他
*   **所属:** Department of Radiotherapy, Eye & ENT Hospital of Fudan University, Shanghai, China. 他
*   **タスク:** 頭頸部放射線治療におけるリスク臓器 (OAR) のマルチモダリティ（CT/MRI）自動セグメンテーション。
*   **データ:** 200例のレトロスペクティブ症例（専門家レビュー済み輪郭）、10例のプロスペクティブ症例で臨床検証。
*   **手法:** M3-Net (multimodality multimask and multitask auto-segmentation network) を提案。CT密度マップとMRI軟部組織コントラスト間の注意機構付き特徴再校正を行うクロスモダリティ融合モジュール、階層的マルチマスク生成器、セグメンテーションと変形可能画像レジストレーションを組み合わせたデュアルタスク学習機構を特徴とする。
*   **成果:** 推論時間を63.6%削減し、輪郭作成時間を75%短縮。線量計測的に重要な精度を維持し、適応放射線治療プロトコルへの迅速な導入を可能にする。
*   **新規性:** CTとMRIのマルチモダリティ画像を相乗的に統合し、計算効率を最適化する、トリプルインターロック型深層学習アーキテクチャを提案した点。
*   **限界: ** 特定の疾患群や解剖学的バリエーションに対するさらなる検証が必要。

### Diagnostic performance of an artificial intelligence algorithm for detecting pneumoperitoneum on abdominal CT scans. (PMID: [42471462](https://pubmed.ncbi.nlm.nih.gov/42471462/))
*   **雑誌名:** Insights into imaging
*   **公開日:** 2026-07-18
*   **著者名:** Yuwan Hu, Zhigang Sun, Haoyu Li 他
*   **所属:** Department of Radiology, China-Japan Friendship Hospital, Beijing, China. 他
*   **タスク:** 腹部CTスキャンにおける気腹の検出、セグメンテーション、体積定量化。
*   **データ:** 2072例の多施設CT画像シリーズ（トレーニング/テストセット）、214例の救急CTスキャン（外部バリデーションセット）。診断レポートをリファレンス標準とした。
*   **手法:** 深層学習ベースモデルを開発し、検出、セグメンテーション、体積定量化の性能を評価した。
*   **成果:** テストセットで感度91.4%、特異度93.1%、AUC 0.97。外部バリデーションコホートで感度84.3%、特異度89.6%。微量遊離ガス（<1mL）を除外すると感度96%に向上。AI由来の体積はリファレンス標準と強い一致（ICC 0.996）。
*   **新規性:** 腹部CTにおける気腹の検出、セグメンテーション、体積定量化を統合したAIアルゴリズムを開発し、多施設データと外部バリデーションでその性能を評価した点。
*   **限界: ** 微量遊離ガスの検出は依然として課題。臨床的影響を確認するには前向き研究が必要。

### Real-world multimetric comparison of four commercial artificial intelligence solutions for intracranial hemorrhage detection. (PMID: [42464524](https://pubmed.ncbi.nlm.nih.gov/42464524/))
*   **雑誌名:** Diagnostic and interventional radiology (Ankara, Turkey)
*   **公開日:** 2026-07-17
*   **著者名:** Jimin Kim, Ha Young Lee, Jin Eun 他
*   **所属:** Eunpyeong St. Mary's Hospital, College of Medicine, The Catholic University of Korea, Department of Radiology, Seoul, Republic of Korea. 他
*   **タスク:** 急性脳内出血 (AIH) 検出のための4つの市販CTベースAIソリューションのリアルワールド多指標性能評価。
*   **データ:** 436例の非造影頭部CTスキャン（救急室でAIH疑いのため実施）。3名の神経放射線科医がグラウンドトゥルースを設定。
*   **手法:** 4つの市販AIソリューションのAUROC、AUPRC、Brierスコア、感度、特異度、精度、F1スコア、および体積一致度（Bland-Altman分析）を評価した。
*   **成果:** 全てのソリューションでAUROC (0.96-0.99) と感度 (0.85-0.92) は高かったが、確認性能と体積一致度には有意な差が見られた。
*   **新規性:** 実際の救急医療現場において、複数の市販AIソリューションの脳内出血検出における多角的な性能（検出、確認、体積定量）を比較評価した点。
*   **限界: ** 単一施設での評価であり、異なる患者集団やCTプロトコルでの一般化可能性は不明。

### Myocardial Scar Assessment Using Artificial Intelligence-Powered Contrast-Free MRI: A Prospective Multicenter Study of Virtual Native Enhancement. (PMID: [42455101](https://pubmed.ncbi.nlm.nih.gov/42455101/))
*   **雑誌名:** Journal of the American College of Cardiology
*   **公開日:** 2026-07-07
*   **著者名:** Qiang Zhang, Di Zhou, Patrick Thompson 他
*   **所属:** Division of Cardiovascular Medicine, Radcliffe Department of Medicine, University of Oxford, Oxford, United Kingdom. 他
*   **タスク:** 造影剤不要MRI（AIによる仮想ネイティブエンハンスメント, VNE）を用いた心筋瘢痕検出の診断性能評価。
*   **データ:** 2施設（リーズ、阜外）から前向きに収集されたCMRデータセット。
*   **手法:** AIが前造影シネおよびT1マップ画像のみからVNE画像を生成。VNE画像とLGE（遅延ガドリニウム増強）画像を比較し、心筋梗塞の診断精度、瘢痕定量化、梗塞領域の一致度を評価。4名の臨床読影医がVNE画像を盲検で評価した。
*   **成果:** VNEによる心筋梗塞診断は、確信度の高い画像で94.4%の精度、全画像で87.5%の精度を達成。瘢痕定量化はLGEと強く相関 (R=0.90)。臨床読影医は69.7%の患者でVNEのみでLGEに進む必要がないと判断し、これらのケースでのVNEの平均診断精度は93.7%でLGEと同等。
*   **新規性:** 造影剤を使用せずにAIが生成する仮想ネイティブエンハンスメント（VNE）画像を用いて心筋瘢痕を検出・定量化する手法を、多施設前向き研究で臨床的に検証した点。
*   **限界: ** 高品質で明瞭なVNE画像でのみ高い診断精度が得られる。全ての患者でLGEを不要にするわけではない。

### Automated MRI Liver Segmentation For Accurate Quantification Of Hepatic Steatosis. (PMID: [42457498](https://pubmed.ncbi.nlm.nih.gov/42457498/))
*   **雑誌名:** Academic radiology
*   **公開日:** 2026-07-15
*   **著者名:** Xiaodie Wei, Shi Qi, Sitong Chen 他
*   **所属:** Beijing Youan Hospital, Capital Medical University, Beijing, China. 他
*   **タスク:** 肝脂肪症の組織学的グレーディングのためのAIベース全肝臓セグメンテーション (WLS) モデルの診断性能評価、および手動ROIベースPDFF測定との一致度検証。
*   **データ:** 538例のMRI-PDFF検査患者。トレーニングコホート372例、検証コホート166例（肝生検実施）。組織学的脂肪肝グレーディングをリファレンス標準とした。
*   **手法:** VBB-Netセグメンテーションモデルを開発。AI-WLS-PDFFと手動ROI-PDFFの診断性能（AUROC）と一致度（ICC）を評価した。
*   **成果:** トレーニングコホートでDice係数0.94、検証コホートで0.93。AI-WLS-PDFFのS0-S3診断におけるAUROCは0.995、0.951、0.928。手動ROI-PDFFとAI-WLS-PDFFは優れた一致度 (ICC 0.996)。
*   **新規性:** MRI-PDFFを用いた肝脂肪症の組織学的グレーディングにおいて、AIによる全肝臓セグメンテーションとPDFF定量化の診断性能と手動測定との高い一致度を大規模コホートで示した点。
*   **限界: ** 提案されたカットオフ値は探索的であり、さらなる検証が必要。

## 総括・編集後記

今週は、CTとMRIを用いたAIによる診断支援、セグメンテーション、治療計画支援に関する研究が目立ち、特にマルチモダリティやリアルワールドでの検証が進んでいる点が注目されます。これらの進展は、日常診療におけるAIの導入可能性を示唆しており、特に緊急性の高い疾患や治療計画の効率化に貢献するAIソリューションのPoC（概念実証）や評価を検討する良い機会となるでしょう。ただし、商用AIの性能差や、AIが既存の検査（例：MRI）を完全に代替できないケースも示されており、導入に際しては多角的な性能評価と外部バリデーションの重要性を忘れてはなりません。
