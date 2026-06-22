## 今週の Top Picks

### MTA-Swin: A Multi-Token Attention Swin Transformer for Brain Tumor Classification with Leakage-Free MRI Benchmarking. (PMID: [42324433](https://pubmed.ncbi.nlm.nih.gov/42324433/))
*   **雑誌名**: Journal of medical systems
*   **公開日**: 2026-06-22
*   **著者名**: Dong Lu, Yu Zhang, Divya Chaudhary
*   **所属**: College of Engineering, Northeastern University, United States; Khoury College of Computer Sciences, Northeastern University, United States.
*   **タスク**: 脳腫瘍のMRI画像からの分類
*   **データ**: 広く使われている公開データセットから重複スキャンを除去した3,522件のMRIスキャン（漏洩フリーベンチマークデータセット）
*   **手法**: Swin TransformerにMulti-Token Attentionを組み込んだMTA-Swinを提案。ImageNet-1Kで事前学習後、漏洩フリーデータセットでファインチューニング。
*   **成果**: 98.57%の全体精度を達成し、13の既存ベースラインモデルを上回った。層別交差検証とGrad-CAM分析により、モデルのロバスト性と解釈性も支持された。
*   **新規性**: データリーク問題に対処するための自動データクリーニングパイプラインを開発し、漏洩フリーベンチマークデータセットを構築した上で、Multi-Token Attentionを導入したSwin Transformerの改良モデルMTA-Swinを提案した。
*   **限界**: 臨床現場でのさらなる検証が必要。

### Validation of aortic valve calcification quantification on contrast-enhanced computed tomography against ex vivo gravimetric analysis: comparison of fixed Hounsfield unit thresholds and deep learning segmentation. (PMID: [42323538](https://pubmed.ncbi.nlm.nih.gov/42323538/))
*   **雑誌名**: BMC cardiovascular disorders
*   **公開日**: 2026-06-20
*   **著者名**: Daisong Jiang, Wanting Zhang, Lulu Liu 他
*   **所属**: Department of Cardiovascular Surgery, West China Hospital, Sichuan University, China; Department of Cardiovascular Surgery, Union Hospital, Tongji Medical College, Huazhong University of Science and Technology, China; Department of Cardiovascular Surgery, Zhongshan Hospital, Fudan University, China; Department of Cardiovascular Surgery, Xijing Hospital, Air Force Medical University, China; Department of Cardiac Surgery, Beijing Anzhen Hospital, Capital Medical University, China.
*   **タスク**: 造影CTにおける大動脈弁石灰化（AVC）の定量化
*   **データ**: 400人の患者（AVCあり300人、正常100人）のCTデータ。50人のSAVR患者の摘出弁のex vivo gravimetric calcium weightを物理的グラウンドトゥルースとして使用。
*   **手法**: 2つの固定HU閾値（450 HU, 850 HU）と、自己構成型nnU-Net深層学習モデルを比較。
*   **成果**: nnU-Netがex vivo gravimetric weightと最も強い相関（Pearson r=0.967）を示し、バイアスとRMSEも最も低かった。850 HU閾値も450 HUより優れていた。
*   **新規性**: 造影CTにおけるAVC定量化の検証において、従来のAgatstonスコアではなく、ex vivoでの物理的なカルシウム重量を絶対的なグラウンドトゥルースとして用いた点で新規性が高い。
*   **限界**: レトロスペクティブな単一施設コホート研究であり、さらなる外部検証が必要。

### Segmenting with confidence through uncertainty quantification for brain tumor imaging. (PMID: [42321390](https://pubmed.ncbi.nlm.nih.gov/42321390/))
*   **雑誌名**: NPJ digital medicine
*   **公開日**: 2026-06-19
*   **著者名**: Yassine Guennoun, Pierre Nedelec, Mark McArthur 他
*   **所属**: Center for Intelligent Imaging (ci2), Department of Radiology & Biomedical Imaging, University of California San Francisco (UCSF), USA; Department of Radiology, Duke University Medical Center, USA.
*   **タスク**: 脳腫瘍（髄膜腫）のMRI画像からのセグメンテーションと不確実性推定
*   **データ**: 1655件の造影後T1強調MRI（788患者）で学習、68件のMRI（43患者）で内部テスト、353患者で外部検証。
*   **手法**: Evidential deep learningアンサンブルを用いて、アレアトリック不確実性（aleatoric-like uncertainty）とエピステミック不確実性（epistemic-like uncertainty）を捉える深層学習フレームワークを開発。
*   **成果**: 高い精度（Dice中央値0.93）を達成し、不確実性マップは放射線科医が曖昧と判断した領域と一致、体積の信頼区間も適切に較正されていた。外部検証でも汎化性（Dice中央値0.92）が確認された。
*   **新規性**: 脳腫瘍セグメンテーションにおいて、臨床導入の大きな障壁である自動セグメンテーションにおける不確実性の欠如を克服するため、較正された不確実性推定を生成する深層学習フレームワークを開発した。
*   **限界**: 髄膜腫に特化した研究であり、他の脳腫瘍タイプへの適用にはさらなる検証が必要。

### Clinical pathways matter for multimodal deep learning in early Alzheimer's disease detection. (PMID: [42324333](https://pubmed.ncbi.nlm.nih.gov/42324333/))
*   **雑誌名**: Scientific reports
*   **公開日**: 2026-06-21
*   **著者名**: Yao Lu, Solveig Kristina Hammonds, Alvaro Fernandez-Quilez
*   **所属**: Department of Computer Science and Electrical Engineering, University of Stavanger, Norway; Department of Computer Science, University of Putra Malaysia, Malaysia; SMIL, Department of Radiology, Stavanger University Hospital, Norway; Centre for Age-Related Medicine (SESAM), Stavanger University Hospital, Norway.
*   **タスク**: アルツハイマー病（AD）の早期リスク層別化
*   **データ**: ADNIコホートの416人（年齢72.73±6.7歳）の構造MRIと臨床変数。
*   **手法**: Zero-shotマルチモーダル特徴抽出フレームワークを提案。SigLIPを用いてMRI埋め込みと日常的に収集される臨床変数（MMSE、年齢、性別）のテキスト埋め込みを組み合わせ、4年以内のADリスク予測を行った。
*   **成果**: 1回の受診設定で、MRI埋め込みとMMSE、年齢、性別を組み合わせることでAUC 0.91±0.02を達成し、CSF Aβ42ベースモデル（AUC 0.73±0.08）やMMSEベースモデル（AUC 0.85±0.22）よりも高い性能を示した。2回の受診設定でも性能が維持または向上した。
*   **新規性**: 既存のマルチモーダルモデルがタスク固有のトレーニングや臨床でルーチンに利用できないバイオマーカーに依存する中、Zero-shotのSigLIPを用いて構造MRIと日常的に収集される臨床変数を組み合わせることで、タスク固有のトレーニングなしにAD早期リスク層別化を可能にした。
*   **限界**: ADNIコホートという特定のデータセットでの評価であり、他のコホートでの外部検証が必要。

### GPT-4.1 and Llama 3.3 70 fail to detect clinically relevant errors in radiology reports in zero-shot evaluation. (PMID: [42319406](https://pubmed.ncbi.nlm.nih.gov/42319406/))
*   **雑誌名**: European radiology
*   **公開日**: 2026-06-19
*   **著者名**: Tugba Akinci D'Antonoli, Lisa C Adams, Jannik Lübberstedt 他
*   **所属**: Division of Diagnostic and Interventional Neuroradiology, Department of Radiology, University Hospital Basel, Switzerland; Department of Pediatric Radiology, University Children's Hospital Basel, Switzerland; Institute of Diagnostic and Interventional Radiology, TUM University Hospital, Technical University of Munich, Germany; Department of Cardiovascular Radiology and Nuclear Medicine, German Heart Center Munich, Germany.
*   **タスク**: 放射線レポートにおける臨床的に重要なエラーの検出と分類
*   **データ**: CT（104件）、MRI（104件）、X線（48件）の256件のオリジナルレポートに対し、4種類のエラー（解剖学的誤表記、生理学的に不可能な所見、診断の不一致、不適切な推奨）を組み込んだ1024件のバリアントレポート。
*   **手法**: GPT-4.1とLlama 3.3 70BをZero-shot設定（ドメイン固有のトレーニングやプロンプト最適化なし）で評価。
*   **成果**: モデルの性能はエラータイプと画像モダリティによって異なり、生理学的に不可能なエラー（E2）で最も低く、GPT-4.1でCT 46.2%、MRI 33.7%だった。不適切な推奨（E4）ではGPT-4.1がX線で85.4%の検出率と高い分類精度を示した。
*   **新規性**: 大規模言語モデル（LLM）が放射線レポートにおける臨床的に重要なエラーを検出する能力を、パターンベースと推論ベースのエラータイプに分けて体系的に評価し、その性能ギャップを明らかにした。
*   **限界**: Zero-shot設定での評価であり、ドメイン固有のファインチューニングやプロンプト最適化によって性能が向上する可能性が残されている。また、評価データセットの規模も限定的。

## 総括・編集後記

今週は、医用画像AIの臨床応用における信頼性向上と、マルチモーダルデータ活用の進展が特に注目されました。特に、AIモデルの不確実性定量化や、物理的グラウンドトゥルースに基づく厳密な検証手法は、AI導入を検討する上で重要な評価指標となるでしょう。また、LLMのレポートエラー検出能力に関する研究は、AIの限界と、人間の専門家による最終確認の重要性を改めて示唆しており、今後のAIと人間の協調ワークフロー設計において考慮すべき点です。
