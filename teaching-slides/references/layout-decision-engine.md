# Layout Decision Engine

版型由資訊關係決定。不要先挑漂亮版型，再把內容塞進去。

## 決策順序

1. 這頁學生要理解哪個主要命題？
2. 資訊單元之間是什麼關係？
3. 哪種 Visual Encoding 最快讓關係被看懂？
4. 哪個 Slide Grammar 最合適？
5. 哪種 Composition 能讓主要命題取得最大視覺權重？
6. 這頁在整份 Deck 要扮演 `anchor`、`dense` 或 `breathing`？

## 資訊關係與表示法

| 資訊關係 | 優先表示法 | 次選 | 避免 |
|---|---|---|---|
| A 與 B，同一組比較維度 | Matched Two-column | Comparison Table | 兩段各說各話 |
| Before → After | Transformation Diagram | Side-by-side | 純文字描述 |
| 3 到 7 個連續步驟 | Process Flow | Numbered Sequence | Generic Bullets |
| 條件分支 | Decision Flow | State Diagram | 一條直線箭頭 |
| Hierarchy | Tree / Layer Stack | Nested Blocks | Flat List |
| Containment / Boundary | Nested Regions | Layer Stack | 無關 Card |
| System Components + Connections | Architecture Diagram | Labeled Grid + Connector | Paragraph Wall |
| 因果鏈 | Causal Node-arrow Diagram | Timeline（只有時間真的重要時） | Isolated Cards |
| 精確 Attribute Lookup | Table / Matrix | Structured Comparison | 長篇 Prose |
| Code Behavior | Code + Trace | Code + State Diagram | 大型 Raw Code Block |
| 單一重要數值 | Big Number | Annotated Chart | 藏在句子裡 |
| 數值趨勢 | Chart | Sparkline + Annotation | Raw Value Table |
| Distribution | Histogram / Box Plot / Violin | Dot Plot | Pie Chart |
| Part-to-whole | Stacked Bar / Labeled Blocks | Simple Proportion | 多片 Pie |
| Concept + Explanation | Diagram + Short Text | 40/60 Visual/Text | Bullet Wall |
| Definition | Short Definition + Visual Anchor | Statement | Multi-card Grid |
| 時間歷程 | Timeline | Ordered Milestones | Table |
| 相互獨立的 Category | Asymmetric Grid / Cards | Columns | 硬畫箭頭 |
| Misconception | Wrong/Right Matched Comparison | Failure Example | 長篇說教 |
| Trade-off | Spectrum / Pareto / Matrix | Matched Comparison | False Binary |
| Resource Allocation | Block Allocation + Capacity Labels | Timeline | Paragraph |
| State-dependent Behavior | State Transition Diagram | Trace | Bullets |

## Composition 選擇

### 50/50

只在兩邊權重真的相同時使用，例如 Matched Comparison。

### 40/60 或 35/65

適合 Text + Diagram。Diagram 通常應該拿比較大的區域。

### Full-canvas

適合 Architecture、Process、Trace、Chart、Evidence Screenshot。文字改成短 Annotation，不在旁邊再塞一篇文章。

### Asymmetric Grid

適合獨立 Category 且有主次關係。不要自動生成三張一樣大的卡片。

## Bullet Router

看到 Bullet 前先問：

- 有順序嗎？有就改 Process / Timeline。
- 有層級嗎？有就改 Layer Stack / Tree。
- 有同維度比較嗎？有就改 Comparison / Table。
- 有因果嗎？有就改 Causal Diagram。
- 有 State 嗎？有就改 State Transition。
- 真的是互相獨立的項目嗎？這時才保留 Bullet。

## Table Router

Table 只在「查某一列與某一欄」有價值時使用。要教 Mechanism 時，優先用 Diagram、Trace 或 Worked Example。

## Code Router

- `< 8 lines`：完整 Code
- `8–20 lines`：節錄 + Highlight / Annotation
- `> 20 lines`：拆頁或只保留相關 Function
- 要解釋 Runtime：Code + Trace
- 要解釋資料流：Code + Data Flow
- 要解釋 Syntax：Code + 1 到 3 個 Callout

## 過載判斷

同一頁同時需要兩種以上主要 Grammar，通常代表應該拆頁。例外是 Code + Trace 這種本來就互相依賴的組合。
