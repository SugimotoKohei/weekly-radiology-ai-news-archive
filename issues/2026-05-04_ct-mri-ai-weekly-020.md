## 今週の Top Picks

### Segmentation of spinal rootlets across MRI contrasts with RootletSeg. (PMID: [42069899](https://pubmed.ncbi.nlm.nih.gov/42069899/))
-   **雑誌名**: Scientific reports
-   **公開日**: 2026-05-02
-   **著者名**: Kateřina Krejčí, Jiří Chmelík, Sandrine Bédard 他
-   **所属**: Department of Biomedical Engineering, FEEC, Brno University of Technology, Brno, Czechia. 他
-   **タスク**: C2-T1脊髄神経根の自動セグメンテーション。
-   **データ**: 50名の健常成人から得られた93件のMRIスキャン（3T T2強調画像、7T MP2RAGE T1強調画像など）。
-   **手法**: 深層学習モデル「RootletSeg」を開発。
-   **成果**: T1w-INV2でDiceスコア0.67、T2wで0.64など、複数のMRIコントラストでC2-T1脊髄神経根を正確にセグメンテーションし、MRI画像から直接脊髄レベルを決定可能とした。
-   **新規性**: 複数のMRIコントラストに対応し、C2-T1脊髄神経根の自動セグメンテーションを可能にするオープンソースの深層学習モデルを開発した点。
-   **限界**: なし

### A multicenter-validated interpretable transformer model for pituitary microadenoma detection on non-contrast multiparametric MRI. (PMID: [42069529](https://pubmed.ncbi.nlm.nih.gov/42069529/))
-   **雑誌名**: BMC medical imaging
-   **公開日**: 2026-05-02
-   **著者名**: Siru Kang, Wenxia Yang, Yijun Yu 他
-   **所属**: Department of Magnetic Resonance, The Second Hospital & Clinical Medical School, Lanzhou University, Lanzhou, China. 他
-   **タスク**: 非造影マルチパラメトリックMRIを用いた下垂体微小腺腫の検出。
-   **データ**: 3つの病院から収集された590名の患者の非造影マルチパラメトリックMRI鞍部スキャン。
-   **手法**: Transformer深層学習モデルを開発し、Grad-CAMとSHAPを用いて解釈可能性を向上。
-   **成果**: TransformerモデルはAUC 0.985と優れた性能を示し、内部および2つの外部テストセットでも高い診断性能（AUC 0.874, 0.829, 0.819）を維持した。
-   **新規性**: 非造影マルチパラメトリックMRIデータにTransformerモデルを適用し、多施設で検証された高い診断性能と解釈可能性を両立させた点。
-   **限界**: なし

### AI-Powered Gradient Echo Plural Contrast Imaging (AI-GEPCI)-A Comprehensive Neurological Protocol From a Single MRI Scan. (PMID: [42068292](https://pubmed.ncbi.nlm.nih.gov/42068292/))
-   **雑誌名**: Journal of magnetic resonance imaging
-   **公開日**: 2026-05-02
-   **著者名**: Jeramy Lewis, Manu S Goyal, Gregory F Wu 他
-   **所属**: Mallinckrodt Institute of Radiology, Washington University in St. Louis, St. Louis, Missouri, USA. 他
-   **タスク**: 単一のGradient Echo Plural Contrast Imaging (GEPCI) 撮像から、臨床品質のFLAIR, MPRAGE, R2*マップおよび派生コントラストを生成。
-   **データ**: 多発性硬化症患者43名のMRIスキャン。3T MRI, 3D GEPCI, MPRAGE, FLAIR。
-   **手法**: Attention-based Convolutional Neural Networks (ACNNs) を訓練。
-   **成果**: AI生成FLAIRとMPRAGEは平均SSIM 0.923と0.935、R2*マップは平均SSIM 0.996を達成。医師による臨床画像品質評価も4.0の臨床基準を上回った。病変量・病変数も高い一致度を示した。
-   **新規性**: 単一のGEPCI撮像から複数の臨床的に関連性の高いMRIコントラストを生成し、高い類似性と臨床品質を達成した点。これによりスキャン時間の短縮とワークフローの効率化が期待される。
-   **限界**: 2段階。

### Construction and validation of a multimodal MRI-based deep learning model for early differential diagnosis of prostate cancer in the PSA gray zone: a retrospective cohort study. (PMID: [42063732](https://pubmed.ncbi.nlm.nih.gov/42063732/))
-   **雑誌名**: Frontiers in oncology
-   **公開日**: 2026
-   **著者名**: Zuliang Xu, Dabin Ren, Guoyu Wang 他
-   **所属**: Department of Radiology, Taizhou Central Hospital (Taizhou University Hospital), Taizhou, Zhejiang, China. 他
-   **タスク**: PSAグレーゾーン（4-10 ng/mL）における臨床的に有意な前立腺癌の早期鑑別診断。
-   **データ**: マルチパラメトリックMRIと生検確認を受けたPSAレベル4-10 ng/mLの患者305名のレトロスペクティブコホート。
-   **手法**: T2強調画像、拡散強調画像、ADCマップ、臨床パラメータを統合する修正U-NetとResNet-50バックボーンに基づく新規マルチモーダルCNNアーキテクチャ。
-   **成果**: 提案モデルはAUC 0.913、感度85.3%、特異度90.9%、全体精度88.5%を達成し、PSA単独やPI-RADS評価を大幅に上回った。不必要な生検を40-50%削減する可能性を示唆。
-   **新規性**: PSAグレーゾーンという臨床的課題に対し、マルチモーダルMRIと深層学習を組み合わせることで、不必要な生検を大幅に削減しつつ高い診断精度を達成した点。
-   **限界**: なし

### Radiologist-AI Collaboration for Ischemia Diagnosis in Small-Bowel Obstruction: Multicentric Development and External Validation of a Multimodal Deep Learning Model. (PMID: [42056618](https://pubmed.ncbi.nlm.nih.gov/42056618/))
-   **雑誌名**: Journal of imaging informatics in medicine
-   **公開日**: 2026-04-29
-   **著者名**: Quentin Vanderbecq, Wen Fan Xia, Emilie Chouzenoux 他
-   **所属**: Department of Radiology, AP-HP.Sorbonne, Saint Antoine Hospital, Paris, France. 他
-   **タスク**: 小腸閉塞に合併する虚血の検出。
-   **データ**: 2つのセンターから収集された1350件のCT検査（うち771件がSBO確定）。3つ目のセンターからの66件の独立した外部テストセット。
-   **手法**: 3D CTデータとルーチンの臨床検査マーカー（C反応性タンパク、好中球数）を組み合わせたマルチモーダルAIモデル（MViT, ResNet-101, DaViTベース）。
-   **成果**: 画像と臨床検査値を組み合わせたモデルが外部テストで最高の性能（AUC 0.69、感度0.89、特異度0.44）を示した。AI支援により放射線科医のAUCは一貫して改善したが、統計的に有意ではなかった。
-   **新規性**: 小腸閉塞合併虚血という緊急性の高い病態に対し、CT画像と臨床検査値を組み合わせたマルチモーダル深層学習モデルを多施設で開発・外部検証し、放射線科医の読影支援ツールとしての可能性を示した点。
-   **限界**: AI支援による放射線科医の性能改善は統計的に有意ではなかった。

## 総括・編集後記

今週は、MRIとCTにおけるAIの応用が多岐にわたり、特に診断精度向上とワークフロー効率化に焦点を当てた研究が目立ちました。単一のMRI撮像から複数のコントラストを生成する技術や、マルチモーダルAIによる前立腺癌や小腸閉塞合併虚血の診断支援は、今後の臨床現場に大きな変革をもたらす可能性を秘めています。これらの新しいAI技術は、導入を検討する価値があり、特にPoC（概念実証）を通じて自施設での有用性を評価することが次のステップとなるでしょう。
