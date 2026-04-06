## 今週の Top Picks

### A fully automated CT-based pelvimetry pipeline for quantifying mid-pelvic surgical workspace in rectal cancer. (PMID: [41936698](https://pubmed.ncbi.nlm.nih.gov/41936698/))
*   **雑誌名**: International journal of computer assisted radiology and surgery
*   **公開日**: 2026-04-06
*   **著者名**: Shih-Feng Huang, Hsin-Ping Tseng, Chao-Wen Hsu
*   **所属**: Division of Colorectal Surgery, Kaohsiung Veterans General Hospital, Taiwan 他
*   **タスク**: 直腸癌手術における中骨盤腔の術野（骨盤計測および軟部組織占有率）をCT画像から全自動で定量化するパイプラインの開発。
*   **データ**: 73名の直腸癌患者の造影CT画像（一部非造影CTとのペアデータも含む）。
*   **手法**: TotalSegmentatorを用いた自動臓器セグメンテーション後、解剖学的アンカーと谷検出戦略により棘間距離（ISD）を抽出し、後方骨盤三角を構築。この領域内の腸管および脂肪の占有率を定量化。
*   **成果**: パイプラインは造影CTで100%、非造影CTで95.8%のISD抽出に成功。自動計測のISDは手動計測との一致度（ICC=0.977）が読影者間信頼性（ICC=0.962）を上回り、骨盤三角由来の指標も良好な一致度を示した。造影・非造影間でも高い一致度を達成。
*   **新規性**: 日常的なCT画像から中骨盤腔の骨格と軟部組織の指標を全自動で、手動計測と同等以上の信頼性で抽出する標準化されたパイプラインを開発した点。
*   **限界**: レトロスペクティブな単施設研究であり、さらなる大規模な外部検証が必要。

### Application of transformer-enhanced convolutional neural network: multicenter MRI assessment of muscle invasion in bladder cancer. (PMID: [41934494](https://pubmed.ncbi.nlm.nih.gov/41934494/))
*   **雑誌名**: European radiology
*   **公開日**: 2026-04-04
*   **著者名**: Zhichang Fan, Ding Li, Wenjing Chen 他
*   **所属**: Department of Radiology, The First Hospital of Shanxi Medical University, China 他
*   **タスク**: 膀胱癌における筋層浸潤の術前MRI評価を、病変形態（有茎性/無茎性）に依存せず行う深層学習モデルの開発。
*   **データ**: 1374名の膀胱癌患者のマルチセンターMRIデータ。
*   **手法**: nnU-Netで病変をセグメンテーションし、その出力を2.5D ConvNeXt-tinyモデルに入力して筋層浸潤を評価。有茎性病変と無茎性病変でモデル性能を比較し、熟練・非熟練放射線科医とのヘッド・トゥ・ヘッド比較も実施。
*   **成果**: モデルは筋層浸潤の同定において0.915-0.925のAUCを達成し、病変形態による診断性能の有意な差はなかった。一方、放射線科医は無茎性病変で特異度が有意に低下した。モデルは無茎性病変において放射線科医よりも有意に高い特異度を示した。
*   **新規性**: 膀胱癌の筋層浸潤評価において、病変形態（特に無茎性病変での過剰診断）に起因する診断バイアスを深層学習モデルが克服できることを多施設データで示した点。
*   **限界**: レトロスペクティブ研究であり、前向き研究でのさらなる検証が必要。

### CEREBLEED: Automated Quantification and Severity Scoring of Intracranial Hemorrhage on Noncontrast CT. (PMID: [41930955](https://pubmed.ncbi.nlm.nih.gov/41930955/))
*   **雑誌名**: Neurosurgery
*   **公開日**: 2026-04-03
*   **著者名**: Santiago Cepeda, Olga Esteban-Sinovas, Murat Yüce 他
*   **所属**: Neurovascular Unit, Department of Neurosurgery, Río Hortega University Hospital, Spain 他
*   **タスク**: 非造影CT画像における頭蓋内出血（ICH）の自動セグメンテーション、体積定量化、および重症度スコアリングフレームワークの開発と外部検証。
*   **データ**: 2112件のNCCTスキャン（トレーニング/内部評価1110件、外部データ1002件）。
*   **手法**: nnU-Netベースの3つのセグメンテーションモデルを用いて、総出血、出血サブタイプ、脳構造をそれぞれセグメンテーション。出血サブタイプと脳構造の体積関係に基づき、定量的な重症度指数（Severity Index）を導出。
*   **成果**: 総出血モデルは内部データでDiceスコア0.90、外部データで0.70を達成。Severity Indexは専門家による視覚的評価と相関し（H=39.6, P<.001）、緊急神経外科的介入の必要性を予測（AUC=0.83）した。
*   **新規性**: 頭蓋内出血の自動定量化と、出血サブタイプおよび脳構造の体積関係に基づいた客観的で解釈可能な重症度指数を提案し、その臨床的有用性を外部データで検証した点。
*   **限界**: 外部データセットでのDiceスコアが内部データより低い傾向が見られた。

### Diagnostic assessment of artificial intelligence reconstruction on accelerated prostate MRI: a retrospective, paired, multi-reader multi-case study. (PMID: [41925836](https://pubmed.ncbi.nlm.nih.gov/41925836/))
*   **雑誌名**: European radiology
*   **公開日**: 2026-04-02
*   **著者名**: Quintin van Lohuizen, Stefan Johannes Fransen, George Yiasemis 他
*   **所属**: Department of Radiology, University Medical Center Groningen, The Netherlands 他
*   **タスク**: AI再構成を用いた高速化前立腺MRIが、従来の撮像時間でのMRIと同等の前立腺癌（PCa）検出性能を維持するかを評価。
*   **データ**: 120件のUMCGデータと312件のNYU公開データからなるT2強調前立腺MRIスキャン。
*   **手法**: NYUデータで訓練されたAIモデルを、UMCGスキャンをR=3およびR=6の加速因子でレトロスペクティブにアンダーサンプリングしたデータに適用し再構成。8名の経験豊富な放射線科医が多読影医多症例研究に参加し、PCa検出性能（AUROC）と画像品質を評価。
*   **成果**: R=6までのMRI加速において、PCa検出性能の統計的に有意な低下は認められなかった（p=0.08）。AUROCはR=1で0.86、R=3で0.82、R=6で0.80。R=3ではシャープネスとノイズが有意に改善し、R=6でも全体的な視覚的品質はR=1と同等であった。
*   **新規性**: AI駆動型再構成により、T2強調前立腺MRIの撮像時間を最大6倍短縮しても、診断性能を統計的に有意に低下させず、かつ画像品質を維持できることを多読影医による評価で示した点。
*   **限界**: 高加速率での診断性能の低下傾向が見られ、さらなる前向き評価が必要。

### X-LAT-Net: An Interpretable Lightweight Axial Transformer Network for Pancreatic CT Segmentation. (PMID: [41915536](https://pubmed.ncbi.nlm.nih.gov/41915536/))
*   **雑誌名**: IEEE journal of biomedical and health informatics
*   **公開日**: 2026-03-31
*   **著者名**: Jianxing Ma, Yalong Li, Ahmed Ibrahim Alutaibi
*   **所属**: 不明
*   **タスク**: CT画像における膵臓のセグメンテーションのための、効率的で正確かつ解釈可能な軽量Axial Transformerネットワーク（X-LAT-Net）の開発。
*   **データ**: NIH Pancreas-CTデータセット。
*   **手法**: U字型アーキテクチャを採用し、Axial Depthwise Convolutionモジュールで長距離空間依存性を捕捉。解釈可能なCross-scale Transformer (X-CATrans) モジュールを導入し、グローバルコンテキストモデリングと注意マップ生成を両立。Shift-enhanced MLPモジュールで不明瞭な境界を改善。
*   **成果**: X-LAT-Netは、わずか1.6Mのパラメータ数でDice係数82.34%を達成。既存の主要な手法と比較して、精度と推論速度の両方で優れ、視覚的な解釈可能性により臨床的信頼性を向上させた。
*   **新規性**: 膵臓CTセグメンテーションにおいて、軽量性、高精度、および臨床的解釈可能性を同時に実現する新しいハイブリッドネットワークアーキテクチャを提案した点。特に、Transformerベースの解釈可能な注意マップ生成が特徴。
*   **限界**: 単一の公開データセットでの評価であり、多様な臨床データでの汎化性能の検証が必要。

## 総括・編集後記

今週は、CTやMRIを用いたAIによる画像診断支援において、**自動定量化、診断バイアスの克服、高速化、そして解釈可能性**といった臨床応用を強く意識した研究が目立ちました。これらの進展は、放射線科医のワークフロー効率化や診断精度の向上に直結するため、各論文の手法や成果を自施設でのPoC（概念実証）や導入検討の参考にすることをお勧めします。特に、AIモデルの外部バリデーションや、モデルがどのような根拠で判断を下しているかを示す「解釈可能性」は、実際の臨床運用における信頼性確保の鍵となるため、今後の研究動向にも注目していきましょう。
