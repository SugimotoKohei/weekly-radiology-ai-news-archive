## 今週の Top Picks

### Deep learning-based automated segmentation of intracerebral haemorrhage, intraventricular haemorrhage and perihaematomal oedema on non-contrast CT. (PMID: [41792040](https://pubmed.ncbi.nlm.nih.gov/41792040/))
*   **雑誌名**: European stroke journal
*   **公開日**: 2026-03-01
*   **著者名**: Floor N H Wilting, Jules P J Douwes, Ajay Patel 他
*   **所属**: Department of Neurology, Donders Institute for Brain, Cognition and Behaviour, Radboud University Medical Center, Nijmegen, The Netherlands 他
*   **タスク**: 非造影CT画像からの脳内出血 (ICH)、脳室内出血 (IVH)、血腫周囲浮腫 (PHO) の同時自動セグメンテーション。
*   **データ**: 2つの多施設前向き研究からの301名のベースラインNCCT（学習・内部検証）、別の多施設研究からの141名のベースラインNCCT（外部検証）。
*   **手法**: 3D U-netモデルを5分割交差検証で学習。
*   **成果**: ICHセグメンテーションで高い性能 (Dice 0.93, ICC 0.98) を達成。IVH (Dice 0.75, ICC 0.97) とPHO (Dice 0.53, ICC 0.60) はより困難であった。ICHの体積バイアスは-0.48 mL。
*   **新規性**: 自発性ICH患者のNCCTにおけるICH, IVH, PHOの同時セグメンテーションモデルを開発し、多施設データで外部検証を行った点で新規性がある。
*   **限界**: IVHとPHOのセグメンテーションはICHに比べて精度が低く、研究用途では前処理として有用だが、臨床適用には視覚的評価と修正が必要。

### Minimum Clinically Achievable Dose for Detecting Liver Lesions Using Deep Learning Image Reconstruction: A Phantom and Patient Study. (PMID: [41781262](https://pubmed.ncbi.nlm.nih.gov/41781262/))
*   **雑誌名**: Academic radiology
*   **公開日**: 2026-03-03
*   **著者名**: Zhijie Pan, Min Xu, Tingting Qu 他
*   **所属**: Radiology Department, Shanghai General Hospital, Shanghai Jiao Tong University School of Medicine, Shanghai, China 他
*   **タスク**: 深層学習画像再構成 (DLIR) を用いた超低線量CTにおける肝病変 (FLLs) 検出性能の評価。
*   **データ**: ファントム研究（Gammex CTファントム）、前向き患者研究（100名のFLLs疑い患者）。
*   **手法**: DLIR (4.5 mGy) と適応統計的繰り返し再構成-V (ASIR-V) (10-15 mGy) の比較。定量的指標（ノイズ、NPS、CNR）と定性的評価（2名の放射線科医による5段階評価）。
*   **成果**: ファントム研究ではDLIR (4.5 mGy) がASIR-V (10 mGy) を全ての定量的指標で上回り、ASIR-V (15 mGy) のノイズとNPSを凌駕。患者研究ではDLIR (4.5 mGy) がASIR-V (10 mGy) と同等の定性的評価と診断精度を達成し、ASIR-V (15 mGy) と比較して非劣性を示した。
*   **新規性**: 超低線量 (約4.5 mGy) のCTにおいて、DLIRが標準線量ASIR-Vと同等以上の肝病変検出性能を持つことをファントムと患者の両方で実証し、被ばく低減の可能性を示した。
*   **限界**: 患者数が限定的であり、さらなる大規模な検証が必要。

### CTP-Free Method for Automated Lesion Water Uptake in Acute Ischemic Stroke. (PMID: [41781175](https://pubmed.ncbi.nlm.nih.gov/41781175/))
*   **雑誌名**: AJNR. American journal of neuroradiology
*   **公開日**: 2026-03-04
*   **著者名**: Laura M van Poppel, Lucas de Vries, Mahsa Mojtahedi 他
*   **所属**: Department of Biomedical Engineering and Physics, Amsterdam UMC, University of Amsterdam, the Netherlands 他
*   **タスク**: 急性虚血性脳卒中患者におけるCTPフリーの自動病変水分摂取量 (NWU) 測定法の開発と評価。
*   **データ**: MR CLEAN RegistryおよびMR CLEAN-LATE試験からの90名の虚血性脳卒中患者（NCCT, CTA, CTPデータ）。
*   **手法**: 深層学習を用いてNCCTとCTA画像から梗塞コアと低灌流領域を自動セグメンテーション。NWUをこれらの領域と対側領域の密度相対差として計算し、従来のCTP-NCCTベースのアプローチと比較。
*   **成果**: CTA-NCCTベースのNWU測定法は、従来のCTP-NCCTベース法と梗塞コア (ICC 0.81) および低灌流領域 (ICC 0.93) で良好な一致を示した。発症4.5時間以内の患者識別において、両アプローチは同等の精度 (AUC 0.77 vs 0.79) を達成した。
*   **新規性**: 虚血性脳卒中におけるNWUを、CTPを必要とせず、NCCTとCTAのみで自動測定する深層学習ベースの手法を開発し、従来のCTPベース法と同等の性能を示した点で新規性がある。
*   **限界**: 外部バリデーションが必要。

### Microstructure-informed deep learning improves thalamic atrophy segmentation and clinical associations in multiple sclerosis and related neuroimmunological diseases. (PMID: [41795481](https://pubmed.ncbi.nlm.nih.gov/41795481/))
*   **雑誌名**: NeuroImage. Clinical
*   **公開日**: 2026-03-02
*   **著者名**: Omar Angelo Ibrahim, Henri Trang, Qianlan Chen 他
*   **所属**: Experimental and Clinical Research Center (ECRC), A Cooperation Between Max Delbrück Center for Molecular Medicine in the Helmholtz Association and Charité - Universitätsmedizin Berlin, Berlin, Germany 他
*   **タスク**: 多発性硬化症 (MS) および関連神経免疫疾患における視床萎縮のMRIセグメンテーション精度向上と臨床的関連性の評価。
*   **データ**: 単一スキャナーコホート (ベースラインn=321; 1年フォローアップn=234) のMS患者/関連疾患患者および健常対照者のT1強調画像。50名のMS患者のT1wおよびFLAIRスキャンに手動GTラベル。
*   **手法**: 既存のAtlasベース (FreeSurfer, FIRST) と深層学習ベース (DBSegment, MindGlide) の4つのアルゴリズムを比較。MindGlideに定量的R1マップを追加入力した場合の性能も評価。
*   **成果**: MindGlideが最も正確な体積推定を示し、DBSegmentがボクセル単位のGT一致で最高 (Dice)。MindGlideの体積は、横断的および縦断的に障害度および認知スコアと最も一貫して関連していた。R1マップの追加はGT一致にわずかな改善またはなしだったが、縦断的関連性を強化した。
*   **新規性**: MSに特化した深層学習モデルMindGlideが、視床萎縮のセグメンテーションにおいて既存のAtlasベースおよび汎用深層学習モデルよりも高い精度と臨床的関連性を示すことを実証。定量的R1マップの追加が縦断的関連性を強化する可能性を示唆した。
*   **限界**: R1マップの追加によるGT一致の改善は限定的。より高解像度のqMRIやマルチコントラスト深層学習アーキテクチャの検討が必要。

### Efficient cardiac MRI multi-structure segmentation for cardiovascular assessment with limited annotation by integrating data-level and network-level consistency. (PMID: [41794927](https://pubmed.ncbi.nlm.nih.gov/41794927/))
*   **雑誌名**: NPJ digital medicine
*   **公開日**: 2026-03-07
*   **著者名**: Sicong Guo, Xinyi Zhao, Junhong Ren 他
*   **所属**: Department of Cardiology, Shengjing Hospital of China Medical University, Shenyang, Liaoning, China 他
*   **タスク**: 限られたアノテーションデータを用いた心臓MRIのマルチ構造セグメンテーション。
*   **データ**: 限られたラベル付きデータと豊富なラベルなしデータを使用。具体的なデータセットの規模や疾患内訳は不明。
*   **手法**: データレベルとネットワークレベルの一貫性を統合した相互アンサンブルフレームワークを提案する半教師あり学習。
*   **成果**: 提案手法はラベルなしデータを活用して性能を向上させ、既存のセグメンテーション手法を上回った。
*   **新規性**: 限られたラベル付きデータと豊富なラベルなしデータを効率的に利用するため、データレベルとネットワークレベルの一貫性を統合した相互アンサンブルフレームワークを提案し、心臓MRIのマルチ構造セグメンテーションの課題を解決した。
*   **限界**: 具体的なデータセットの規模や疾患内訳、定量的な性能指標が抽象的な記述に留まっている。

## 総括・編集後記

今週は、CT/MRIにおけるAIのセグメンテーションと定量化の進展が目立ち、特に、限られたデータや特殊な臨床ニーズに対応する工夫が見られました。これらの進歩は、診断効率の向上や被ばく低減、治療計画の最適化に貢献するため、自施設でのPoCや既存ワークフローへの統合可能性を検討する良い機会となるでしょう。ただし、モデルの外部バリデーションや、特定の疾患・プロトコルにおける限界を理解し、慎重な導入と継続的な性能評価が不可欠です。
