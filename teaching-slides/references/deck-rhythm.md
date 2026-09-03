# Deck Rhythm

單頁設計正確，整份簡報仍可能很累。Deck Rhythm 管的是跨頁的注意力與資訊負荷。

## `anchor`

功能：定位、換章、建立大 Mental Model、做大範圍 Recap。

常見頁型：

- Cover
- Section Divider
- Learning Objectives
- Architecture Overview
- Recap Map

特徵：主從清楚、競爭資訊少、結構容易記住。

## `dense`

功能：教 Mechanism、Evidence、Code、Comparison、Worked Reasoning。

常見頁型：

- Code Walkthrough
- Worked Example
- Table
- Detailed Diagram
- Matched Comparison
- Chart Analysis

特徵：資訊量高，但 Reading Order 受控。

## `breathing`

功能：重置注意力、提問、停頓、強調一個結論或轉換 Section。

常見頁型：

- Statement
- Check-your-understanding
- Misconception Reveal
- Key Takeaway
- Big Number
- Visual Pause

特徵：單一焦點、留白較多、掃讀成本低。

## 預設規則

1. 盡量不要超過 3 張連續 `dense`。
2. Major Section 優先用 `anchor` 或 `breathing` 開始。
3. 困難的 Worked Example 或 Code Sequence 後，安排 Check、Takeaway 或 Recap。
4. 不要機械插入空白頁，Reset 要有教學用途。
5. 即使內容不同，連續重複相同 Grammar 仍算 Rhythm 重複。
6. 連續 4 張使用相同 Composition 是警訊，除非 Step-by-step Trace 需要穩定位置。

## 常見節奏

Concept Section：

`anchor → dense → dense → breathing → dense → anchor`

Algorithm：

`anchor → breathing(Intuition) → dense(Algorithm) → dense(Trace) → breathing(Check) → dense(Comparison) → anchor(Recap)`

System：

`anchor(Architecture) → dense(Component) → dense(Flow) → breathing(Failure Question) → dense(Failure Mode) → dense(Mitigation) → anchor(Recap)`

Code Tutorial：

`anchor(Goal) → breathing(Mental Model) → dense(Code) → dense(Trace) → breathing(Common Mistake) → dense(Modification) → anchor(Takeaway)`

## Drift Control

Demo 核准後建立 Design Lock。整份 Deck 固定：

- Palette
- Typography Family / Scale
- Spacing
- Corner Radius
- Border Style
- Icon Style
- Code Style
- Diagram Edge Vocabulary
- Citation Style

中途不要自行加入新的 Color、Font 或 Effect。
