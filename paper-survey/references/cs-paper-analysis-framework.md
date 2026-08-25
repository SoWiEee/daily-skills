# Computer Science Paper Analysis Framework

## 何時讀取

在已取得論文全文或足以分析的指定章節後讀取本文件，用來選擇研究類型、建立研究地圖、重建技術模型與執行批判檢查。若使用者只要摘要或翻譯，不必讀取整份文件。

## 一、研究類型路由

先選一個主要類型；若論文混合多種方法，標示主類型與次類型，不要強迫所有欄位都套用同一種研究語言。

| 類型 | 主要分析對象 | 需要特別檢查 |
| --- | --- | --- |
| Algorithm / ML | 演算法、model、representation、training objective | task definition、data split、baseline、metric、ablation、generalization |
| Systems / Software | 架構、runtime、compiler、database、distributed system、software process | workload、environment、throughput、latency、resource cost、failure mode、deployment fit |
| Theory / Formal | 定義、假設、lemma、theorem、proof、complexity | assumptions、proof validity、boundary conditions、guarantee scope、counterexample |
| Dataset / Benchmark | 資料集、標註、benchmark、evaluation protocol | provenance、sampling、annotation quality、contamination、split、representativeness |
| HCI / Human-centered | interface、interaction、user behavior、qualitative or quantitative study | participants、task、protocol、construct validity、coding、ethics、external validity |
| Security / Privacy | threat model、attack、defense、privacy mechanism | attacker capability、security property、attack surface、adaptive attack、realistic setting |
| Mixed | 多個主要方法共同回答一個問題 | 每個子方法與同一個 claim 的對應，不把不同證據混成一種結果 |

## 二、研究地圖欄位

建立地圖時，優先填寫以下欄位；找不到就寫「作者沒有明確說明」，不要以領域常識補齊。

### 身分與範圍

- Title、authors、year、venue、paper type。
- Subfield、task、application scenario、problem setting。
- 論文處理的是 prediction、generation、retrieval、optimization、verification、measurement、interaction 或其他任務。
- Input、output、assumptions、target users 或 deployment context。

### 研究邏輯

- Background、existing practice、problem、gap、purpose。
- Explicit RQ、hypothesis、design goal、theorem 或 central claim。
- 作者認為 novelty 在 problem、method、system、data、evaluation、theory 或 application 的哪一層。
- 這個 claim 的必要證據是什麼，論文是否真的提供。

### 技術與實證

- Method、model / system components、algorithm steps、objective。
- Dataset、data source、version、size、label、preprocessing、split。
- Baselines、comparison conditions、hyperparameter policy、compute budget。
- Metrics、evaluation protocol、random seeds、repetitions、uncertainty reporting。
- Main findings、negative results、failure cases、efficiency trade-offs。

### 產出與限制

- Theoretical、algorithmic、empirical、systems、dataset、methodological、practical contributions。
- Code、data、model、configuration、appendix、artifact availability。
- 作者明確承認的 limitations。
- 閱讀後發現的 validity threat、scope mismatch 與 overclaim。

## 三、技術模型的選擇

### 演算法或機器學習

```text
Data / Task → Representation → Model Components
→ Training Objective → Prediction / Generation → Evaluation Metric
```

檢查每個 component 是否真的被 ablation 或其他 evidence 支持。分開記錄模型設計、訓練策略、資料因素與評估因素；不要因為結果變好就直接宣稱某個 component 造成改善，除非設計能排除替代解釋。

### 系統或軟體工程

```text
Workload / Input → Architecture / Implementation
→ Runtime Behavior → Performance, Reliability, Cost, or User Outcome
```

檢查 workload 是否代表目標場景、硬體與軟體環境是否足以解釋結果、baseline 是否使用相同資源，以及平均值是否掩蓋 tail latency、failure cases 或成本。

### 理論或形式化方法

```text
Definitions + Assumptions → Lemmas / Proof Steps
→ Theorem / Proposition → Guarantee, Complexity, or Boundary
```

檢查 conclusion 是否只在假設成立時有效、定理是否覆蓋作者聲稱的範圍、proof 是否依賴未說明的條件，以及是否存在簡單 counterexample。

### 資料集或 benchmark

```text
Data Source → Collection / Annotation → Split / Task
→ Baselines / Protocol → Measurement of Benchmark Quality
```

檢查資料是否洩漏、測試集是否被反覆調參、標註規則是否一致、benchmark 是否偏向某一類方法，以及結果是否能代表實際任務。

### HCI 或使用者研究

```text
User / Context → Interface or Intervention → Task Behavior
→ Measurement / Coding → User or System Outcome
```

此類論文才適合詳細使用 participants、sampling、consent、between-subjects、within-subjects、qualitative coding、inter-rater reliability 等欄位。仍需確認 procedure 和 measurement 是否真的由論文提供。

### 資安與隱私

```text
Threat Model → Attack / Defense Mechanism → Security Property
→ Attack Success, Leakage, Robustness, or Utility
```

檢查 attacker capability 是否合理、攻擊是否適應防禦、評估是否涵蓋 strongest relevant baseline、security claim 是否超出測試環境，以及 utility / privacy trade-off 是否被量化。

## 四、方法與評估檢查表

### 資料與任務

- 任務定義是否清楚，輸入與輸出是否可操作？
- 資料來源、版本、篩選、標註與前處理是否可追溯？
- train / validation / test 是否分離？是否有 leakage、duplicate、contamination 或 temporal leakage？
- 測試資料是否與作者要外推的場景一致？

### Baseline 與比較公平性

- baseline 是否足夠強、相關、最新或代表主要方法家族？
- 所有方法是否使用相同資料、split、preprocessing、compute budget 與 tuning effort？
- 作者是否報告 negative results、failure cases 或只挑最好的一次結果？
- ablation 是否一次只移除一個關鍵因素，還是同時改變多個條件？

### 指標與數據

- metric 是否真的對應研究目標，而不是容易最佳化但不代表實際價值的 proxy？
- 是否報告 absolute improvement、relative improvement、variance、confidence interval 或 effect size？
- p-value 若存在，檢定單位、假設、multiple comparisons 與 statistical power 是否清楚？
- 統計顯著是否被錯誤解讀為實務重要、普遍有效或因果成立？
- 效率、記憶體、能源、延遲、成本與 accuracy 之間的 trade-off 是否被納入？

### 可重現性

- 是否提供 code、data、model、configuration、random seed、hardware、software version 與完整 command？
- 是否能由論文內容重建資料流程、訓練 / 建置流程與評估流程？
- 缺少的資訊會影響可重現性、結果解釋或公平比較到什麼程度？

## 五、Claim-to-Evidence Matrix

對每個重要 claim 建立以下對照，不要只在結論段落重述它：

| Claim | 論文證據 | 回查位置 | 支持範圍 | 未支持或替代解釋 |
| --- | --- | --- | --- | --- |
| 作者聲稱的問題或 novelty | Introduction / Related Work | section / page | 本文直接說明的範圍 | 是否只是比較少或定義較窄 |
| 方法有效 | table / figure / theorem / case study | figure / table / theorem | 哪些 task、data、baseline、metric | data、tuning、split、randomness 或 confound |
| 理論或機制成立 | proof、ablation、analysis | section / appendix | 論文明確證明或觀察的部分 | 未被隔離的因素與未測試條件 |
| 可泛化或可部署 | multiple datasets / workload / environment | table / appendix | 實際測試覆蓋的範圍 | domain shift、cost、failure mode、security assumption |

## 六、批判性評估順序

用以下順序批判，先檢查研究是否完成自己設定的任務，再檢查是否能外推：

1. Gap：問題是否真實存在，且後文有處理？
2. Alignment：problem、task、method、evaluation、claim 是否對齊？
3. Validity：資料、測量、實驗、proof 或 study protocol 是否足以支持結果？
4. Fairness：baseline、resource、tuning、split 與 metrics 是否公平？
5. Robustness：結果是否跨資料、環境、seed、參數、攻擊或使用者群體穩定？
6. Scope：結論是否超過測試條件、理論假設或資料支持範圍？
7. Reproducibility：別人是否有足夠資訊重建關鍵步驟？

每一項都同時寫出：做得好的地方、主要風險、對結論的實際影響，以及如果重新研究最值得改善的地方。
