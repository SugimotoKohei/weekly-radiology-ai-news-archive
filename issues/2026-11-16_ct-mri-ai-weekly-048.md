## 今週の Top Picks

### Adaptive deep learning model with anatomical priors for 3D segmentation of fine hepatic vasculature on CT. (PMID: [43034797](https://pubmed.ncbi.nlm.nih.gov/43034797/))
*   **雑誌名**: Radiology advances
*   **公開日**: 2026-11
*   **著者名**: Zixuan Zhao, Kalyani Vyapari, Kyunghyun Sung 他
*   **所属**: Physics and Biology in Medicine Graduate Program, David Geffen School of Medicine at UCLA, Los Angeles, CA, United States. 他
*   **タスク**: CT画像からの肝臓門脈および肝静脈の3Dセグメンテーション、特に細い末梢枝の強調。
*   **データ**: 公開Medical Segmentation Decathlon (MSD) Task08-HepaticVesselデータセット (303腹部CTボリューム)。3DIRCADbで外部検証。
*   **手法**: PriM Fusion Netを開発。デュアルエンコーダアーキテクチャを採用し、Swin TransformerでCT画像を、並列畳み込みパスで最適化されたFrangi vesselness priorを処理。Gated multimodal unitsが2つの特徴ストリームを複数のスケールで融合し、ルールベースのSimpleMind後処理で解剖学的妥当性を向上。
*   **成果**: 平均Dice類似度係数(DSC) 77.68%、95パーセンタイルHausdorff距離(HD95) 11.55mmを達成し、全てのベースラインモデルを上回る性能を示した。特に細い末梢枝のセグメンテーションが改善された。
*   **新規性**: 最適化された解剖学的事前情報を適応的に統合するデュアルエンコーダ深層学習モデル（PriM Fusion Net）を開発し、CT画像からの肝臓細血管の3Dセグメンテーション精度を向上させた点。
*   **限界**: なし。

### Combined imaging of myocardial scar and fat using artificial intelligence-guided dual bright- and black-blood late gadolinium enhancement. (PMID: [43032887](https://pubmed.ncbi.nlm.nih.gov/43032887/))
*   **雑誌名**: European heart journal. Imaging methods and practice
*   **公開日**: 2026-10
*   **著者名**: Kalvin Narceau, Manuel Villegas-Martinez, Théo Richard 他
*   **所属**: IHU LIRYC, Heart Rhythm Disease Institute, Hôpital Xavier Arnozan, Université de Bordeaux-INSERM U1045, France. 他
*   **タスク**: 心筋症における心筋瘢痕と心臓内外脂肪の同時、共登録定量化。
*   **データ**: 36人の心臓磁気共鳴画像法（CMR）患者のプロスペクティブコホート。シミュレーション、ファントム実験も実施。
*   **手法**: SPOT-DIXONシーケンスを開発。連続する心拍でbright-bloodとblack-blood LGEを交互に取得し、Dixon水脂肪分離のためのデュアルエコーデータを収集。AIモデルがbright-blood水画像上で左心室壁を自動セグメンテーションし、瘢痕および脂肪画像に輪郭を伝播。
*   **成果**: AIベースのLV壁セグメンテーションは手動と優れた一致（グローバルDICE = 84.4 ± 4.0%）。SPOT-DIXONは参照シーケンスより高い瘢痕体積、負担、透過性を示し、LV壁体積は同等。AIベース解析により後処理時間を大幅に短縮（2.1 ± 0.7秒 vs 手動180分）。
*   **新規性**: 単一のLGE撮像で心筋瘢痕と脂肪を同時に、共登録で評価できるAI支援SPOT-DIXONシーケンスを開発し、既存のワークフローの主要な制限を克服した点。
*   **限界**: なし。

### Structural brain changes in age-related macular degeneration before and 6 months after Scharioth macula lens implantation: an exploratory MRI study. (PMID: [43033260](https://pubmed.ncbi.nlm.nih.gov/43033260/))
*   **雑誌名**: Neuroradiology
*   **公開日**: 2026-11-14
*   **著者名**: Jakub Bochnička, Juhana Hakumäki, Naďa Jirásková 他
*   **所属**: Faculty of Medicine Hradec Kralove, Charles University, Prague, Czech Republic. 他
*   **タスク**: 加齢黄斑変性（AMD）患者の脳構造変化（MRI）を特徴付け、Scharioth macula lens (SML) 移植後の縦断的変化を評価。
*   **データ**: ドライAMD患者10名（平均年齢78.8±5.6歳）の3T MRIデータ（SML移植前と6ヶ月後）。
*   **手法**: 全自動AI支援マルチアトラスセグメンテーションツール（cNeuro cMRI）を用いて、領域体積と年齢・性別・頭部サイズで正規化された規範パーセンタイルを生成。視覚ネットワーク内のベースライン偏差と縦断的変化を解析。
*   **成果**: ベースラインでは、左、全体、右後頭極および左舌状回で規範値からの有意な偏差を認めた。SML移植後の縦断的変化は、FDR補正後には有意な所見は得られなかった。
*   **新規性**: AI支援の自動セグメンテーションツールを用いて、加齢黄斑変性患者の脳構造変化を規範値と比較し、さらに視覚リハビリテーション（SML移植）後の縦断的変化を探索的に評価した点。
*   **限界**: 研究の感度が低く、構造変化がないことを証明するものではない。小規模コホートであり、縦断的変化は探索的所見に留まる。

### Influence of Deep Learning Reconstruction on the Detection of Susceptibility Effect by T2*WI. (PMID: [43035873](https://pubmed.ncbi.nlm.nih.gov/43035873/))
*   **雑誌名**: Nihon Hoshasen Gijutsu Gakkai zasshi
*   **公開日**: 2026
*   **著者名**: Takuma Daimaruya, Kazuhiko Oyu, Yohei Funato 他
*   **所属**: Division of Radiology, Department of Medical Technology, Hirosaki University Hospital. 他
*   **タスク**: T2*強調画像における深層学習再構成（DLR）がサセプティビリティ効果の検出に与える影響の評価。
*   **データ**: 不明（臨床画像データを使用）。
*   **手法**: T2*強調画像シーケンスを使用し、DLR適用画像と非適用画像を比較してサセプティビリティ効果の検出数を評価。スライス厚（1-5mm）とNEX（1 NEX）の条件で検討。
*   **成果**: スライス厚2-5mmではDLR使用によりサセプティビリティ効果の検出数が増加した。1mmスライス厚ではDLRによる差はなかった。1 NEXかつDLR使用時、3-5mmスライス厚で検出数が増加し、1mmスライス厚で減少した。
*   **新規性**: T2*強調画像におけるDLRの導入がサセプティビリティ効果の検出に与える影響を、スライス厚やNEXといった撮像条件と関連付けて具体的に評価した点。
*   **限界**: 従来の画像のSNRに依存する可能性があり、SNRが保証された条件下での撮像が必要。

### Artificial intelligence-enabled medical image analysis in photon-counting CT: A review of segmentation, detection, classification and characterization, and automated quantification. (PMID: [43023267](https://pubmed.ncbi.nlm.nih.gov/43023267/))
*   **雑誌名**: Journal of X-ray science and technology
*   **公開日**: 2026-11-13
*   **著者名**: Yimin Yin, Jinyi Zhou, Shaohan Yu 他
*   **所属**: School of Mathematics and Statistics, Hunan First Normal University, Changsha, China. 他
*   **タスク**: フォトンカウンティングCT (PCCT) におけるAI応用（セグメンテーション、検出、分類・特徴付け、自動定量化）の現状と課題をレビュー。
*   **データ**: 該当なし（レビュー論文）。
*   **手法**: 構造化されたナラティブ検索により、PCCT画像上のAI応用を評価した原著論文を特定。各分析設定をタスク、有効な入力、モデルの出所、開発戦略、参照標準、比較対象、テストの独立性、エビデンスの成熟度でコーディング。
*   **成果**: 全てのタスクで技術的実現可能性が示された。既存の従来型モデルはPCCTでも有用な性能を維持し、PCCTネイティブ研究では仮想単色画像、閾値画像、物質マップなどが探求された。
*   **新規性**: 次世代CTであるフォトンカウンティングCTにおけるAIの応用状況を包括的にレビューし、その技術的実現可能性と、エビデンスの成熟度、研究デザインの課題を明確にした点。
*   **限界**: 小規模コホート、非独立な繰り返し観察、限定的な外部テスト、PCCT-EID比較の不足、空間的・スペクトル的アブレーションの不足により、性能への因果的帰属が制限される。プロスペクティブなワークフローのエビデンスが不足。

## 総括・編集後記

今週は、CT/MRIの最新撮像技術とAIの融合が、診断精度向上や新たな臨床的知見の発見に貢献する論文が目立ちました。これらの技術はまだ研究段階のものが多いですが、自施設でのPoC（概念実証）や、既存のAIツールが新しい撮像プロトコルでどのように振る舞うか評価する良い機会となるでしょう。特に新しい撮像法とAIの組み合わせでは、外部バリデーションの不足や、特定の撮像条件に起因するバイアスに注意し、臨床導入には慎重な評価が不可欠です。
