# Diagram Ontology

先分類關係，再畫圖。Diagram 要能解釋機制，不能只當裝飾。

## D01 Relationship

兩個以上 Entity 互相影響、溝通或對應。方向有意義才加箭頭。

## D02 Containment

用在 Boundary、Ownership、Trust Zone、Namespace、Scope 或 Nested System。

## D03 Hierarchy / Tree

用在 Taxonomy、Ownership、Decomposition 或 Logical Hierarchy。

## D04 Layer Stack

用在 Protocol Stack、Abstraction Level、Defense Layer、Privilege Boundary。

## D05 Process Flow

有明確順序且主要路徑單一：`A → B → C → D`。

## D06 Decision Flow

條件會造成分支。Branch Label 要直接說明條件。

## D07 Data Flow

學生需要知道資料怎麼移動或被轉換。區分 Store、Transform 與 Transport。

## D08 Control Flow

用在 Controller、Worker、Callback、Scheduler 與 Feedback Control。Command 與 Response 必要時用不同 Edge Style。

## D09 State Transition

行為依賴 State 時使用。State 有名稱，Transition 有 Trigger 或 Condition。

## D10 Transformation

用在 Before/After、Representation Change、Compilation、Encoding、Migration 或 Resource Model Change。

## D11 Mapping

一個 Domain 對應到另一個 Domain，例如 `input → representation → output`。

## D12 Timeline

只有 Chronology 或 Elapsed Time 本身重要時使用。

## D13 Cycle

最後一個 Stage 會回到起點。

## D14 Feedback Loop

Output 會改變後續 Input。Feedback Edge 必須明確畫出。

## D15 Trade-off Spectrum

用在 latency ↔ throughput、simplicity ↔ control 這類競合目標。不要強迫所有問題變成二元對立。

## D16 Architecture

元件、介面、Boundary、Data / Control Channel 與 Ownership。每個 Box 要有角色，每條 Edge 要能解釋。

## D17 Resource Allocation

用 Block、Bar、Queue、Time Slice 或 Capacity Label 表示 CPU、GPU、Memory、Quota 與 Fractional Share。

## D18 Trace / Execution Walkthrough

用在 Algorithm、Packet、Scheduling、State Machine 或 Code Execution。重點是逐步 State，不是靜態 Architecture。

## Edge 語意

預設：

- Solid Arrow：主要方向、Command 或 Data Movement
- Dashed Arrow：Optional、Indirect 或 Inferred Path
- Double Arrow：Bidirectional Interaction
- Line Without Arrow：Association 或 Boundary Relation
- Accent Color：目前教學焦點，不是裝飾

同一頁有多種 Edge Meaning 時，要有 Legend 或很清楚的 Convention。

## Node 語意

- Process / Component：Rectangle
- State：Rounded Rectangle 或明確 State Node
- Decision：只有真的判斷 Condition 才用 Diamond
- Datastore / Resource Pool：Cylinder 或有清楚 Label 的 Container
- External Actor / System：Outlined External Node
- Boundary：Enclosing Region

## 密度

- 每頁 3 到 7 個主要 Node 通常最好讀
- 超過 9 個主要 Node，先 Aggregate 或拆頁
- Label 說明角色，不重複名字
- Secondary Detail 放 Callout 或下一張 Deep Dive

## 抽象概念 Router

- isolation → Containment / Boundary
- abstraction → Layer
- scheduling → Resource Allocation + Timeline / Trace
- backpressure → Feedback Loop
- dependency resolution → Graph / Process
- trust chain → Hierarchy / Flow
- representation learning → Mapping / Transformation

能用 Semantic Geometry 精確說明時，不用 Generated Image 取代 Diagram。
