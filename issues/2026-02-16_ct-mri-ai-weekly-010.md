## 今週の Top Picks

### Automated Classification of Kidney Tumours Using Deep Convolutional Neural Networks. (PMID: [41691614](https://pubmed.ncbi.nlm.nih.gov/41691614/))
- **雑誌名**: The international journal of medical robotics + computer assisted surgery : MRCAS
- **公開日**: 2026-02
- **著者名**: Miaolin Guo, Shan Lin, Yuxuan You 他
- **所属**: The School of Clinical Medicine, Fujian Medical University, Fuzhou, China. 他
- **タスク**: CT画像を用いた腎腫瘍の自動検出および分類。
- **データ**: CT Kidneyデータセット。
- **手法**: EfficientNetV2-B3とResNet50をデュアルバックボーンとして特徴抽出し、デュアル効率チャネルアテンションモジュール (DECA) を用いてクロスモデル特徴融合を行う深層学習モデル。
- **成果**: CT Kidneyデータセットにおいて98.80%の精度と98.28%のF1スコアを達成し、他の特徴融合戦略と比較して優れた性能を示した。
- **新規性**: デュアルバックボーンとDECAを統合した強力なネットワークを提案し、腎腫瘍CT画像の分類タスクで優れた性能を達成した点が新しい。
- **限界**: 特定のデータセットでの評価であり、異なる施設や人種間での汎用性についてはさらなる検証が必要。

### Feasibility of BMI-based sub-milliSievert low-dose CT in individualized detection of lung nodules. (PMID: [41691132](https://pubmed.ncbi.nlm.nih.gov/41691132/))
- **雑誌名**: European radiology
- **公開日**: 2026-02-14
- **著者名**: Siqi Qu, Qiuxing Chen, Shulin Li 他
- **所属**: Postgraduate cultivation base of Guangzhou University of Chinese Medicine, Panyu Central Hospital, Guangzhou, China. 他
- **タスク**: BMIベースのサブミリシーベルト低線量CT (LDCT) プロトコルにおける画質と肺結節評価の性能評価。
- **データ**: 214名の参加者（標準線量CTとLDCT）。LDCTは高線量群 (0.57-1.15 mSv) と低線量群 (0.33-0.63 mSv) に層別化され、BMIベースの4つのサブグループに分けられた。
- **手法**: 深層学習画像再構成 (DLIR-H, DLIR-M)、適応統計的逐次近似再構成 (ASIR-V-50%)、フィルタ補正逆投影 (FBP) の複数の再構成アルゴリズムを使用し、画質、結節検出、サイズ測定精度、Lung-RADS v2022の一致性を分析した。
- **成果**: LDCTにおいてDLIR-Hは優れた画質と最高の結節検出率 (99.04%) を示し、特に6mm未満の結節で優位であった。BMIサブグループ間での検出率に有意差はなく、DLIRは被曝量を大幅に削減しつつ、診断性能を維持した。
- **新規性**: BMIベースのサブミリシーベルトLDCTプロトコルと複数の再構成アルゴリズム（特にDLIR）を組み合わせ、画質と肺結節検出（特に6mm未満）の性能を評価した点が新しい。
- **限界**: 単一施設での前向き研究であり、外部バリデーションが必要。

### A multi-level segmentation-guided diffusion model for streak artifact reduction in routine non-contrast chest CT. (PMID: [41689727](https://pubmed.ncbi.nlm.nih.gov/41689727/))
- **雑誌名**: Medical & biological engineering & computing
- **公開日**: 2026-02-14
- **著者名**: Jingxin Liu, Xinran Zhu, Zhangzhen Shi 他
- **所属**: Department of Radiology, China-Japan Union Hospital of Jilin University, Changchun, China. 他
- **タスク**: 非造影胸部CT (NCCT) におけるストリークアーチファクトの低減。
- **データ**: 4種類のCTスキャナーから得られた96,641スライス (763シリーズ) のCT画像。アーチファクトあり/なしのサンプルを含む。
- **手法**: マルチレベルの解剖学的セグメンテーションをガイドとして使用する新規拡散モデル (guided diffusion method)。トレーニング中にアーチファクトフリーCTスライスとセグメンテーションマップ、関心領域 (ROI) をチャネル結合で統合し、推論時にアーチファクト影響サンプルからアーチファクトフリー出力を生成する。
- **成果**: 提案手法は、SNRとCNRを大幅に改善し、既存の4つの研究と比較して優れたPSNR (36.952)、SSIM (0.863)、DSC (0.959) を達成した。適切なセグメンテーションガイダンス (Level-2) が構造制約とアーチファクト低減効率のバランスを最適化することを示した。
- **新規性**: マルチレベルの解剖学的セグメンテーションをガイドとして組み込んだ拡散モデルを開発し、非造影胸部CTのストリークアーチファクトを効果的に低減した点が新しい。
- **限界**: 提案モデルの汎用性や、異なるアーチファクトの種類への適用性についてはさらなる検証が必要。

### Quantitative fat-fraction analysis of the rotator cuff muscles on clinical sagittal and coronal T1-weighted MRI using deep learning algorithms. (PMID: [41688617](https://pubmed.ncbi.nlm.nih.gov/41688617/))
- **雑誌名**: Scientific reports
- **公開日**: 2026-02-13
- **著者名**: Hanspeter Hess, Alexandra Oswald, Keivan Daneshvar 他
- **所属**: Department of Orthopaedic Surgery and Traumatology, Inselspital, Bern University Hospital, University of Bern, Bern, Switzerland. 他
- **タスク**: 標準的なT1強調MRIから回旋筋腱板の定量的ボクセル単位脂肪分画 (FF) を予測。
- **データ**: 75名の患者のT1強調MRIと2点Dixon MRIのペアデータでトレーニング。24名の患者で検証。
- **手法**: 深層学習ベースのアルゴリズムを開発し、ボクセル単位の5クラスシステムでFFを自動予測。回旋筋腱板は冠状面と矢状面でセグメンテーションされた。
- **成果**: 提案アルゴリズムは、二値脂肪分類アプローチよりも有意に高精度であり、Dixon MRIと比較して筋肉全体の平均FF計算誤差は-0.5±2.2%から2.3±3.9%の範囲であった。T1強調MRIから正確なボクセル単位FF定量化を可能にし、筋肉FF分布分析を提供することで、予後分析と治療計画の最適化に貢献する可能性を示した。
- **新規性**: 標準的なT1強調MRIから深層学習を用いて回旋筋腱板のボクセル単位の定量的脂肪分画を正確に予測し、従来の定性的なGoutallier分類の限界を克服した点が新しい。
- **限界**: データセットの規模が比較的小さく、異なるMRIプロトコルやスキャナーでの汎用性についてさらなる検証が必要。

### Artificial intelligence-assisted reading of non-contrast prostate MRI: application and concordance with expert interpretation in a screening population within the PROSA trial. (PMID: [41686238](https://pubmed.ncbi.nlm.nih.gov/41686238/))
- **雑誌名**: European radiology
- **公開日**: 2026-02-13
- **著者名**: Emanuele Messina, Antonella Borrelli, Francesca Mezzapesa 他
- **所属**: Department of Radiological Sciences, Oncology and Pathology, Sapienza University/Policlinico Umberto I, Rome, Italy. 他
- **タスク**: 非造影前立腺MRI (bpMRI) におけるAIベースソフトウェアの臨床的に有意な前立腺癌 (csPCa) スクリーニングにおける有効性評価、特に経験の浅い読影医の支援。
- **データ**: PROSA試験からの499件のbpMRI。
- **手法**: 専門医、経験の浅い読影医、AI単独、AI支援下の経験の浅い読影医による独立した評価を実施。ROC曲線とCohenのkappa係数で診断性能と読影医間の一致度を評価した。
- **成果**: AI支援下の経験の浅い読影医が最高の診断性能 (感度 76.5%, 特異度 97.2%, 精度 95.8%, AUC 0.969) を達成し、AI単独およびAIなしの経験の浅い読影医を上回った。AI支援により読影医間の一致度も向上 (κ=0.64から0.84)。PI-RADS 3の曖昧な症例が減少し、専門医との正確な一致率が向上した。
- **新規性**: 非造影前立腺MRIスクリーニングにおいて、AIが経験の浅い読影医の診断性能と一貫性を向上させることを実証し、特に曖昧な症例の解釈を改善した点が新しい。
- **限界**: 単一施設での後向き分析であり、外部バリデーションが必要。

## 総括・編集後記

今週は、CTの低線量化と画質向上、MRIの定量的評価、そしてAIによる診断支援といった、医用画像AIの臨床応用における具体的な進展が目立ちました。これらの技術は、被曝低減、診断精度向上、ワークフロー効率化に貢献する一方で、成人向けAIモデルの小児への適用における性能劣化など、実用化に向けた重要な課題も浮き彫りになっています。読者の皆様には、自施設でのPoCや外部バリデーションを通じて、これらのAIツールの有効性と安全性を慎重に評価し、特に小児患者への適用においては年齢層に応じた性能検証が不可欠であることを認識していただきたいと思います。
