## 今週の Top Picks

### Development and validation of a versatile foundation model for cine cardiac magnetic resonance image analysis. (PMID: [42129472](https://pubmed.ncbi.nlm.nih.gov/42129472/))
*   **雑誌名**: Communications medicine
*   **公開日**: 2026-05-13
*   **著者名**: Yunguan Fu, Wenjia Bai, Weixi Yi 他
*   **所属**: UCL Hawkes Institute, University College London, London, UK 他
*   **タスク**: Cine心臓MRI画像解析のための多用途基盤モデル「CineMA」の開発と検証。
*   **データ**: 74,916研究からの1500万枚のcine心臓MRI画像で事前学習し、8つの独立したデータセットでファインチューニングと評価。
*   **手法**: マルチビューconv-transformer masked autoencoder基盤モデルを開発。セグメンテーション、ランドマーク局所化、疾患診断、予後予測のタスクで性能を評価。
*   **成果**: CineMAは、nnUNetに匹敵する心室セグメンテーションと駆出率推定性能を示し、繰り返しスキャンでの一貫性が向上。心血管疾患検出ではCNNベースラインを上回り、特異度が顕著に改善。全身性疾患や生存転帰の予測にも可能性を示した。
*   **新規性**: 7万件以上の大規模データで事前学習された、心臓MRI解析初の多用途基盤モデルであり、幅広いタスクで高い性能と汎用性を示した。
*   **限界**: 不明

### TOPOS: target organ prediction on scout views for automated CT scan planning. (PMID: [42135580](https://pubmed.ncbi.nlm.nih.gov/42135580/))
*   **雑誌名**: European radiology
*   **公開日**: 2026-05-14
*   **著者名**: Sebastian Ziegelmayer, Tristan Lemke, Markus Graf 他
*   **所属**: Department of Diagnostic and Interventional Radiology, Klinikum rechts der Isar, Technical University of Munich, School of Medicine and Health, TUM University Hospital, Munich, Germany 他
*   **タスク**: CTスカウトビューにおける解剖学的構造のセグメンテーションによるスキャン範囲の最適化と被曝低減。
*   **データ**: 2022年から2025年までの1146人のCT患者データ（内部データセット）、36件の外部胸部CT。
*   **手法**: 深層学習モデルを26のターゲット構造のセグメンテーションに訓練し、スカウトビューに転送。自動スキャン計画と手動計画を比較。
*   **成果**: モデルは高いセグメンテーション精度（平均DSC 0.93）を達成。自動計画により、内部コホートでスキャン長が11-25%減少し、DLPも同様に減少。外部コホートでもスキャン長が28.7%減少し、DLPも減少。診断品質を損なうことなく被曝を低減した。
*   **新規性**: スカウトビューからターゲット臓器を自動セグメンテーションし、CTスキャン範囲を最適化することで、過剰スキャンと被曝を効果的に削減する実用的な深層学習モデルを開発した。
*   **限界**: 不明

### MedNext-Insight Model for Automated Metabolic Tumor Volume Delineation on Computed Tomography and Prognostic Value in Nasopharyngeal Carcinoma. (PMID: [42144163](https://pubmed.ncbi.nlm.nih.gov/42144163/))
*   **雑誌名**: International journal of radiation oncology, biology, physics
*   **公開日**: 2026-05-16
*   **著者名**: Meng-Yu Hao, Yu-Xi Xiong, Yu-Li 他
*   **所属**: State Key Laboratory of Oncology in South China, Guangdong Key Laboratory of Nasopharyngeal Carcinoma Diagnosis and Therapy, Guangdong Provincial Clinical Research Center for Cancer, Sun Yat-sen University Cancer Center, Guangzhou, P. R. China 他
*   **タスク**: PETなしでルーチンCT画像から代謝腫瘍体積(MTV)を自動描出し、鼻咽頭癌(NPC)におけるその予後予測価値を検証。
*   **データ**: 392人のNPC患者の放射線治療前CT画像。
*   **手法**: 深層学習モデル「MedNext-Insight」を開発し、MTV描出に適用。描出されたMTVに基づくラジオミクス特徴の予後予測性能を評価。
*   **成果**: MedNext-Insightは高いMTV描出DSC（0.808）を達成し、感度を向上。CTのみで得られたMTVに基づくラジオミクスは、PET-MTVに匹敵する予後予測性能（C-index 0.712 vs 0.744）を示し、臨床変数と組み合わせることでさらに向上（C-index 0.809）。
*   **新規性**: PET画像なしでルーチンCT画像から代謝腫瘍体積を正確に自動描出し、その予後予測価値を鼻咽頭癌で検証した点で、リソース効率の高いリスク層別化アプローチを提示した。
*   **限界**: 不明

### Artificial intelligence denoising in cardiac photon-counting CT: mitigating BMI-related noise degradation while maintaining clinical interchangeability. (PMID: [42142519](https://pubmed.ncbi.nlm.nih.gov/42142519/))
*   **雑誌名**: European journal of radiology
*   **公開日**: 2026-05-05
*   **著者名**: Lisa Urban, Josephine Berger, Jan M Brendel 他
*   **所属**: Department of Diagnostic and Interventional Radiology, Eberhard-Karls University, Tuebingen, Germany 他
*   **タスク**: 心臓PCD-CTにおけるAIベースのノイズ低減(AID)アルゴリズムが、BMIに関連するノイズ劣化を効果的に軽減しつつ、量子反復再構成(QIR)と比較して厳密な定量的診断的同等性と臨床的互換性を維持できるかを評価。
*   **データ**: 100人の患者の非造影冠動脈石灰化(CAC)スコアリングおよび造影冠動脈CTアンギオグラフィー(CCTA)のデュアルソースPCD-CT画像。
*   **手法**: 標準QIRとPCD-CT重み付けAIDアルゴリズムで画像を再構成。主観的・客観的画質、BMIとの相互作用、診断的同等性（Agatstonスコア、CAD-RADSなど）を評価。
*   **成果**: AIDは主観的画質を大幅に改善し、CACで約64%、CCTAで78%のノイズを低減。BMIによるノイズ増加をCACで44%、CCTAで78%抑制。空間分解能は維持。QIRとAIDの間で厳密な診断的同等性（Agatstonスコア、CAD-RADS分類、プラーク組成）が証明された。
*   **新規性**: PCD-CTに特化したAIベースのノイズ低減アルゴリズムが、BMIによるノイズ劣化を効果的に抑制しつつ、既存のQIRと診断的同等性を保ち、画質とワークフロー効率を向上させることを示した。
*   **限界**: 不明

### Assessing the suitability of automated registration and segmentation for dosimetry calculations in SIRT treatment planning. (PMID: [42143172](https://pubmed.ncbi.nlm.nih.gov/42143172/))
*   **雑誌名**: EJNMMI physics
*   **公開日**: 2026-05-17
*   **著者名**: Félix Quinton, Romain Popoff, Fabrice Meriaudeau 他
*   **所属**: Université Bourgogne Europe, CNRS, ICMUB UMR 6302, Dijon, France 他
*   **タスク**: SIRT治療計画における自動レジストレーションとセグメンテーション技術が線量計算に与える影響を評価。
*   **データ**: 肝細胞癌患者90人の治療前データ（造影T1強調MRI、SPECT/CT）。
*   **手法**: 半自動と自動レジストレーション、手動と深層学習ベースの自動セグメンテーションを比較。線量計算の精度を平均吸収線量、D70、累積線量体積ヒストグラムで評価。
*   **成果**: 半自動と自動MRI-CT肝臓レジストレーションは同等のDiceスコア（92%）を達成。腫瘍レジストレーションは方法間で差があり、平均Diceスコアは79%。自動セグメンテーションは、約40%の患者で腫瘍Diceスコアが80%を超え、臨床的に許容される線量計算の差を避けるにはDiceスコア80%以上が必要と判明。
*   **新規性**: SIRT治療計画において、自動レジストレーションと深層学習ベースの自動セグメンテーションが線量計算に与える影響を定量的に評価し、特に腫瘍セグメンテーションの精度が線量計算の正確性に不可欠であることを示した。
*   **限界**: 自動腫瘍セグメンテーションは30%の症例で依然として課題があり、線量計算の精度向上のためにはさらなる改良が必要。

## 総括・編集後記

今週は、医用画像AIが診断支援だけでなく、治療計画、画像再構成、ワークフロー最適化といった多岐にわたる臨床プロセスに深く統合されつつあることが顕著でした。特に、CTの自動スキャン計画やPETフリーの腫瘍体積描出など、効率化と被曝低減に貢献する技術は、早期のPoCや評価を検討する価値があるでしょう。基盤モデルのような汎用性の高いAIの登場は期待されますが、各施設での外部バリデーションや、特定の患者群における性能の検証が引き続き重要となります。
