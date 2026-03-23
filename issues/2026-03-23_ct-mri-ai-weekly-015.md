## 今週の Top Picks

### Real-world unified denoising for multi-organ fast MRI: a large-scale prospective validation. (PMID: [41857225](https://pubmed.ncbi.nlm.nih.gov/41857225/))
*   **雑誌名**: NPJ digital medicine
*   **公開日**: 2026-03-19
*   **著者名**: Yuchen Shao, Hongyan Huang, Lingyan Zhang 他
*   **所属**: School of Biomedical Engineering and State Key Laboratory of Advanced Medical Materials and Devices, ShanghaiTech University, Shanghai, China. 他
*   **タスク**: マルチ臓器高速MRIにおけるノイズ除去
*   **データ**: 6つの臨床センター、4つの主要MRIベンダー、6つの臓器、96のMRIプロトコルから収集された148,930組のノイズあり/ノイズなし画像ペアで学習。20,143組の実世界画像ペアでテストし、4つの独立したコホートからの46,870枚の外部臨床画像で汎化性能を検証。
*   **手法**: 再構成された商用MRIシステム画像に直接作用する統一深層学習ベースのノイズ除去モデル。
*   **成果**: 既存の最先端ノイズ除去手法を一貫して上回り、組織セグメンテーションのDiceスコアを7.05%改善。加速係数3倍でも、診断性能はクリーン画像と同等であり、多くの撮像が1分以内に完了可能。
*   **新規性**: 大規模な実世界データ、多施設、多ベンダー、多臓器、多プロトコルにわたる統一モデルを前向きに検証し、その臨床的有用性を示した点。
*   **限界**: 論文抽象からは特になし。

### Interactive Deep Learning for Myocardial Scar Segmentation Using Cardiovascular Magnetic Resonance. (PMID: [41864346](https://pubmed.ncbi.nlm.nih.gov/41864346/))
*   **雑誌名**: Journal of cardiovascular magnetic resonance : official journal of the Society for Cardiovascular Magnetic Resonance
*   **公開日**: 2026-03-19
*   **著者名**: Aida Moafi, Danial Moafi, Simran Shergill 他
*   **所属**: Department of Cardiovascular Sciences, University of Leicester, the National Institute for Health and Care Research Leicester Biomedical Research Centre and British Heart Foundation Centre of Research Excellence, Glenfield Hospital, Leicester, UK. 他
*   **タスク**: 心臓MRI (LGE-CMR) を用いた心筋瘢痕のインタラクティブな深層学習セグメンテーションと定量化
*   **データ**: 慢性心筋梗塞患者348名のLGE-CMR画像（トレーニング244、バリデーション51、テスト53）。
*   **手法**: プロンプトガイド型セグメンテーションを組み込み、医用画像向けに調整されたビジョン基盤モデルを活用。臨床医向けインターフェースに統合し、リアルタイムでのインタラクションと自動定量化を実現。
*   **成果**: 専門家レベルのセグメンテーション性能（Dice 0.74±0.10）、優れた再現性（ICC 0.999）、セグメンテーション時間の大幅短縮（平均65±34秒/患者）。
*   **新規性**: 人間参加型（human-in-the-loop）設計により、高速、高精度、高再現性の心筋瘢痕定量化をLGE-CMRから可能にするフレームワークを提案した点。
*   **限界**: 論文抽象からは特になし。

### Clinical Utility of Deep Learning-based Multiple Arterial Phase MRI in Hepatocellular Carcinoma. (PMID: [41860367](https://pubmed.ncbi.nlm.nih.gov/41860367/))
*   **雑誌名**: Radiology. Imaging cancer
*   **公開日**: 2026-03
*   **著者名**: Kai Liu, Beixuan Zheng, Yunfei Zhang 他
*   **所属**: Department of Radiology, Zhongshan Hospital, Fudan University, No. 180 Fenglin Road, Xuhui District, Shanghai 200032, China. 他
*   **タスク**: 肝細胞癌 (HCC) 診断のための深層学習ベース超高速多動脈相MRIの臨床的有用性評価
*   **データ**: 2024年9月～2025年3月にECAまたはHBA造影MRIを受けたHCC疑い患者を対象とした前向き研究。
*   **手法**: 深層学習を用いて超高速多動脈相MRIを生成し、従来の単一動脈相画像と比較。
*   **成果**: 論文抽象が途中で切れているため、具体的な数値成果は不明だが、深層学習ベースの超高速多動脈相MRIがHCC診断において臨床的有用性を持つことを評価している。
*   **新規性**: 深層学習による超高速多動脈相MRIの生成と、HCC診断におけるその臨床的有用性を前向きに評価している点。
*   **限界**: 論文抽象が途中で切れており、具体的な成果や限界が不明。

### From Passive Sampling to Precision Intervention: A Standardized Radiomics-Driven Workflow for Molecularly Adequate Lung Biopsy. (PMID: [41865181](https://pubmed.ncbi.nlm.nih.gov/41865181/))
*   **雑誌名**: Cardiovascular and interventional radiology
*   **公開日**: 2026-03-21
*   **著者名**: Luca Marinelli, Vittorio Patanè, Riccardo Monti 他
*   **所属**: Department of Precision Medicine, University of Campania "Luigi Vanvitelli", 80138, Naples, Italy. 他
*   **タスク**: CTガイド下経胸壁針生検 (TTNB) における肺病変の分子学的診断の適切性を予測するフレームワークの開発と時間的検証
*   **データ**: 633患者における670件のCTガイド下TTNB手技。レトロスペクティブな2施設コホート（522手技）でモデル開発・内部検証、プロスペクティブな単施設コホート（148手技）で独立した時間的検証。
*   **手法**: 手技変数に基づく多変量モデルを開発し、その後、定量的画像特徴（ラジオミクス）を統合する探索的ラジオミクスサブスタディを実施。
*   **成果**: 分子学的診断の全体的な適切性は83.9%。標準化された手技フレームワーク下の前向きコホートでは91.2%と有意に高い適切率。手技モデルのAUCは0.86（開発コホート）/0.84（検証コホート）。ラジオミクス統合により識別能がさらに向上（AUC 0.88）。
*   **新規性**: 手技の標準化とラジオミクスを統合することで、CTガイド下肺生検の分子学的診断の適切性を向上させる標準化されたワークフローを提案した点。
*   **限界**: 論文抽象からは特になし。

### Impact of CT dose on AI performance: A comparison of radiomics, deep, and foundation models in a multicentric anthropomorphic phantom study. (PMID: [41846467](https://pubmed.ncbi.nlm.nih.gov/41846467/))
*   **雑誌名**: Medical physics
*   **公開日**: 2026-03
*   **著者名**: María Martín Asiain, Mohammadreza Amirian, Oscar Jimenez Del Toro 他
*   **所属**: Institute of Informatics, School of Management, HES-SO Valais-Wallis University of Applied Sciences and Arts Western Switzerland, Sierre, Switzerland. 他
*   **タスク**: CT線量レベルの変動に対するラジオミクスベース、深層学習ベース、および基盤モデルのロバスト性評価
*   **データ**: 3Dプリントされた人体ファントム（肝臓組織と異常をシミュレート）から1378シリーズの画像（13スキャナー、4メーカー、5線量レベル）。公開データセットCT-ORG（140CTスキャン）も使用。
*   **手法**: PyRadiomics、浅いCNN、SwinUNETR、CT基盤モデル（CT-FM）の4手法で特徴を抽出し、線量変動に対する安定性（ICC）、組織タイプの分離能（UMAP）、汎化性能を評価。
*   **成果**: ラジオミクス特徴と深層モデルは線量変動に対して限定的なロバスト性しか示さず、肝組織分類性能が低下。CT-FMは線量関連の変動を軽減し、最も高いロバスト性を示した。
*   **新規性**: 標準化された人体ファントムと実患者データを用いて、CT線量変動が異なるAIモデル（特に基盤モデル）の性能に与える影響を多角的に評価した点。
*   **限界**: 研究は初期実験段階であり、レトロスペクティブデータのみでテストされている。

## 総括・編集後記

今週は、MRIの高速化と画像品質向上、そしてAIモデルの臨床的ロバスト性に関する研究が特に注目されました。これらの進展は、AIを実臨床に導入する際の重要な考慮事項であり、特に高速撮像や線量低減とAIの組み合わせについて、自施設でのPoCや評価を進める良い機会となるでしょう。ただし、AIモデルの真の臨床的有用性を確立するためには、多様な環境下での外部バリデーションや、線量変動に対するさらなるロバスト性向上が引き続き重要な課題です。
