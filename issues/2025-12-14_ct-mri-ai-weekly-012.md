## 今週の Top Picks

### Application value of prostate-specific antigen density combined with multiparametric MRI in early diagnosis of prostate cancer. (PMID: [41389905](https://pubmed.ncbi.nlm.nih.gov/41389905/))
- **雑誌名**: Magnetic resonance imaging
- **公開日**: 2025-12-11
- **著者名**: Di Wu, Zhaobing Tang
- **所属**: Department of Urology, The First Affiliated Hospital of Chongqing Medical University, Chongqing, China.
- **タスク**: PSAグレーゾーン（4-10 ng/mL）およびPI-RADS 3症例における前立腺癌の早期診断。
- **データ**: 不明（mpMRI画像とPSAD）
- **手法**: 前立腺特異抗原密度（PSAD）とマルチパラメトリックMRI（mpMRI、T2WI, DWI, ADC）を統合する深層学習モデルを開発。クロスモーダルアテンションガイド（CM-AG）融合モジュールを用いてPSADとmpMRIの特徴を重み付け。
- **成果**: PSAグレーゾーンコホートでAUC=0.89、PI-RADS 3でAUC=0.83を達成し、単一モダリティMRIやPI-RADS単独評価を統計的に有意に上回った。前立腺体積が大きい患者では特異度が10.2%向上した。
- **新規性**: PSADとmpMRIをクロスモーダルアテンションを介して融合することで、特にPSAグレーゾーンやPI-RADS 3といった診断が困難なサブグループにおける診断性能を向上させた。
- **限界**: 抽象には明記されていないが、一般的に単施設での後方視的研究である可能性があり、外部バリデーションが今後の課題となる。

### Impact of vessel suppression AI on reading efficiency and nodule detection in CT chest. (PMID: [41390262](https://pubmed.ncbi.nlm.nih.gov/41390262/))
- **雑誌名**: Current problems in diagnostic radiology
- **公開日**: 2025-11-26
- **著者名**: Kevin T Chorath, Evan Jacobs, Ken Tharp 他
- **所属**: Department of Radiology, University of Washington, Seattle, WA, USA. 他
- **タスク**: 胸部CTにおける血管抑制（VS）AIソフトウェアが読影効率と肺結節検出に与える実世界での影響を評価。
- **データ**: 単一学術機関で解釈された8,835件の胸部CT検査（2023年1月～2024年2月）。
- **手法**: VS導入前後のレトロスペクティブ分析。読影時間と肺結節検出を自然言語処理（NLP）と手動検証で抽出。
- **成果**: 研修医の平均読影時間は19.1分から12.2分に短縮（p<0.001）、点状結節検出率が13.0%から24.2%に向上（p<0.001）。指導医も読影時間短縮（6.6分から5.2分、p<0.001）、点状結節検出率が26.0%から29.5%に向上（p=0.042）。
- **新規性**: 血管抑制AIソフトウェアが臨床ワークフローにおける読影効率と小結節検出に与える実世界での影響を、大規模な後方視的データで評価し、研修医と指導医の両方で効果を示した点。
- **限界**: 2mm未満の小結節検出の臨床的意義は不明であり、下流の臨床的影響と偶発的に検出された小結節の管理に関するさらなる研究が必要。

### Detection of phase-binning and interpolation artifacts in 4-dimensional computed tomography imaging using deep learning and rule-based approaches. (PMID: [41389065](https://pubmed.ncbi.nlm.nih.gov/41389065/))
- **雑誌名**: Medical physics
- **公開日**: 2025-12
- **著者名**: Jorge Cisneros, Nathan H Feldt, Yevgeniy Vinogradskiy 他
- **所属**: Department of Biomedical Engineering, University of Texas at Austin, Austin, Texas, USA. 他
- **タスク**: 4次元CT（4DCT）画像におけるフェーズビンニングおよび補間アーチファクトの検出。
- **データ**: 9つの異なる臨床4DCTデータセットから、アーチファクトのない呼吸相に合成アーチファクトを体系的に挿入して生成されたグラウンドトゥルースデータ。
- **手法**: 3D深層学習モデル（nnUNet, SwinUNETR）を開発し、合成データで訓練。補間アーチファクト検出にはヒューリスティックなルールベース手法も使用。
- **成果**: nnUNetとSwinUNETRモデルは、平均0.957の最先端のアーチファクト検出精度を達成。SwinUNETRモデルは高精度かつ高速な実行時間を示し、リアルタイムでのアーチファクト修正や再スキャン指示の可能性を秘める。
- **新規性**: 複数の臨床4DCTデータセットから合成アーチファクトを体系的に挿入するジェネレータを導入し、それを用いて3D深層学習モデルを訓練することで、4DCT画像のアーチファクト検出において最先端の精度を達成した点。
- **限界**: 合成データでの訓練が実世界データにどれだけ一般化できるか、リアルタイムでの再スキャン指示の実現性にはさらなる検証が必要。

### Long-Term Carotid Plaque Progression and the Role of Intraplaque Hemorrhage: A Deep Learning-Based Analysis of Longitudinal Vessel Wall Imaging. (PMID: [41386425](https://pubmed.ncbi.nlm.nih.gov/41386425/))
- **雑誌名**: Journal of cardiovascular magnetic resonance : official journal of the Society for Cardiovascular Magnetic Resonance
- **公開日**: 2025-12-10
- **著者名**: Yin Guo, Ebru Yaman Akcicek, Daniel S Hippe 他
- **所属**: Department of Bioengineering, University of Washington, Seattle, WA, USA. 他
- **タスク**: 頸動脈プラーク内出血（IPH）が頸動脈プラーク負荷の長期進行に与える影響を評価。
- **データ**: 頸動脈アテローム性動脈硬化症の無症候性被験者28名から、平均5.8±1.1年にわたる平均4.7±0.6回のマルチコントラスト磁気共鳴血管壁イメージング（VWI）スキャン。
- **手法**: 深層学習パイプラインを用いて頸動脈血管壁とIPHをセグメンテーション。線形混合効果モデルでIPHの発生、IPH体積とプラーク負荷（%WV）進行の関連を評価。
- **成果**: IPHの存在または発生は、罹患動脈のプラーク負荷（%WV）を平均2.3%絶対的に増加させ、IPH体積も%WV増加と正の関連があった（p=0.005）。IPHのない動脈では最小限の進行だったが、IPHの存在は長期プラーク成長を著しく加速させた。
- **新規性**: 深層学習ベースのセグメンテーションパイプラインを用いて、IPHの長期的な持続性と、それが頸動脈プラーク負荷の進行に与える影響を定量的に評価した点。
- **限界**: 被験者数が28名と比較的少ないため、より大規模なコホートでの検証が望まれる。

### The Applications of Spectral CT in Interventional Radiology: Innovations in Diagnosis and Intra-procedural Guidance. (PMID: [41381762](https://pubmed.ncbi.nlm.nih.gov/41381762/))
- **雑誌名**: Cardiovascular and interventional radiology
- **公開日**: 2025-12-11
- **著者名**: Milin Patel, Moaz M Choudhary, Patrick D Sutphin 他
- **所属**: Faculty of Medicine, University of Ottawa, 451 Smyth Rd, Ottawa, K1H 8L1, Canada. 他
- **タスク**: インターベンショナルラジオロジー（IR）におけるスペクトラルCTの臨床的有用性をレビュー。
- **データ**: 関連文献のナラティブレビュー。
- **手法**: スペクトラルCTのIRにおける応用を、術前計画、術中ガイダンス、術後評価のワークフロー全体で検討。
- **成果**: スペクトラルCTは、従来のCTと比較して、組織特性評価の強化、病変検出の改善、アーチファクト低減など、IRにおける診断精度と手技の安全性を向上させる大きな可能性を示す。将来的にAIやフォトンカウンティング技術との統合が期待される。
- **新規性**: スペクトラルCTのIRにおける応用を、術前計画、術中ガイダンス、術後評価のワークフロー全体で包括的にレビューし、将来的なAIやフォトンカウンティング技術との統合の可能性を強調した点。
- **限界**: レビュー論文であるため、具体的なAIモデルの性能評価やデータセットの詳細は含まれない。

## 総括・編集後記

今週は、AIがCTやMRIといった医用画像診断の効率化と精度向上に貢献する多様なアプローチが目立ちました。特に、血管抑制AIによる読影効率の改善や、mpMRIと臨床指標を統合した診断モデルは、日常臨床への導入やPoCを検討する価値があるでしょう。ただし、AIモデルの臨床的意義や外部バリデーションの必要性、そして新しい画像診断技術の標準化は、今後の運用において常に意識すべき課題です。
