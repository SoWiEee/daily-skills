---
name: teaching-slides
description: 建立可獨立閱讀的技術課程簡報與教學講義。先透過多輪需求訪談釐清受眾、先備知識、時間、教學目標與教材限制，再完成教學架構、逐頁文稿與講稿、語意化視覺 Storyboard、4 到 6 張代表性 Demo、Design Lock、完整實作與三層 QA。內建 27 種 Slide Grammar、Layout Decision Engine、Diagram Ontology、Deck Rhythm、繁體中文寫作規則與避免 AI 味檢查。open-slide 可用時優先採用，也支援既有 React/HTML 專案。
version: 3.0.0
---

# Teaching Slides v3

這個 Skill 用來製作課程講義、技術教學簡報、Tutorial、Workshop、論文導讀與研究方法教學。預設成果要能讓學生課後單獨閱讀，也能支援現場授課。

設計順序固定為「先決定怎麼教，再決定怎麼畫，最後才寫 renderer 程式碼」。不要一拿到教材就直接生成整份 React slide。

## 必守原則

1. **Reading-first**：投影片離開講者後仍能重建主要概念、推理與限制。
2. **一頁一個主要教學命題**：可放完整的支持證據，但不要混入無關命題。
3. **允許重組教材**：可調整順序、拆頁、合併重複內容與補上必要橋接，但不得改掉來源事實、術語、數值、限制與不確定性。
4. **頁數不是目標函數**：內容太擠時先拆頁，不靠縮字硬塞。
5. **語意先於版型**：先判斷資訊關係，再選 Visual Encoding、Slide Grammar 與 Layout。閱讀 `references/layout-decision-engine.md`。
6. **關係優先畫圖**：流程、層級、因果、狀態、架構、資源分配、轉換與時間關係，優先用 Diagram。閱讀 `references/diagram-ontology.md`。
7. **Bullet 只表達真正的清單**：如果項目之間有順序、層級、比較、因果或空間關係，就改用更精確的表示法。
8. **控制整份簡報節奏**：每頁標記 `anchor`、`dense` 或 `breathing`。閱讀 `references/deck-rhythm.md`。
9. **繁體中文語境**：除術語、程式碼、API、Library、Framework、論文題名與專有名詞外，敘述採自然的台灣繁體中文。
10. **避免 AI 味**：文稿、講稿與投影片文字都要通過 `references/anti-ai-style.md`。
11. **固定 1920×1080 Canvas**：整張 slide 等比例縮放，手機畫面也不重新排版。
12. **Design Lock**：Demo 核准後才鎖定顏色、字體、間距、圖形語彙、Code Style、Citation Style 與跨頁節奏。
13. **證據可追查**：資料、論文圖、截圖、統計與外部主張要有簡短來源或超連結。
14. **Renderer 放在流程後段**：open-slide 只是實作工具，不能反過來決定教學架構。

## 預設教學元素

依內容選用，不要求每章全都出現：

- Learning objectives
- Intuition / analogy
- Worked example
- Simple code walkthrough
- Check-your-understanding
- Recap
- Key takeaway

## 互動模式與自主模式

預設使用互動模式。遇到下列 Gate 時先停下來讓使用者確認：

- Gate A：需求訪談摘要
- Gate B：教學架構
- Gate C：文稿與講稿樣稿
- Gate D：Visual Storyboard
- Gate E：4 到 6 張代表性 Demo
- Gate F：Design Lock

如果使用者明確要求「直接做完」、「自行判斷」或其他自主生成指示，就可以跳過等待，但仍要把推定條件寫在 `assumptions`，並照相同階段留下中間產物。

## 階段 0：多輪需求訪談

先讀 `references/discovery-interview.md`。

不要一次丟出十幾個問題。根據已知資訊，用 2 到 4 輪問答逐步補齊：

- `purpose`：課程講授、Tutorial、Workshop、複習、論文導讀等
- `audience`：年級、背景、角色
- `prior_knowledge`：已會什麼
- `likely_gaps`：最可能卡在哪
- `duration`：授課時間與是否分節
- `learning_goals`：課後要能解釋、判斷或實作什麼
- `source_policy`：可重組程度、是否允許補外部資料
- `reading_first`：是否需要課後自讀
- `interaction`：是否要問題、練習、Live Demo
- `code_depth`：Code 比重與語言
- `renderer`：open-slide、既有專案或 generic HTML/React
- `constraints`：頁數、品牌、來源、交付格式等

不要重問使用者已經提供的資訊。必要欄位齊全就停止訪談。

Gate A 的輸出是 `project-brief.yaml`。格式參考 `templates/project-brief.yaml`。

## 階段 1：教學架構

先決定整堂課的學習路徑，再決定逐頁內容。讀 `references/teaching-design.md`。

每個 Section 至少要有：

```yaml
section_id: S2
title: "GPU sharing 改變了什麼"
learning_goal: "學生能說明 MPS 為什麼讓 GPU 排程多出 share allocation 維度"
learner_gap: "學生可能只熟悉一張 GPU 一個 Job 的離散配置"
teaching_strategy:
  - "先用 exclusive allocation 當起點"
  - "再加入 50% + 50% 的具體配置"
  - "最後連回 scheduler action space"
estimated_slides: 5
```

依教材類型選用不同節奏，例如 Algorithm、System Architecture、Code Tutorial、Paper Walkthrough 或 Case Study。

Gate B：先讓使用者確認 Section 順序、範圍與預計頁數，再展開逐頁內容。

## 階段 2：簡報文稿與講稿

讀 `references/teaching-manuscript.md`。

這一階段保持 renderer-neutral，也先不決定 Layout。先回答每一頁「要教什麼、學生要看到什麼、講者要補什麼」。

逐頁至少包含：

```yaml
slide: 12
teaching_claim: "MPS 讓 GPU 配置從整張卡變成可分割的 share"
learner_question: "MPS 為什麼會讓排程問題多一個維度？"
on_slide_message:
  title: "MPS 讓 GPU 排程多出 share allocation"
  supporting_content:
    type: "annotations"
    items:
      - "原本：一個 Job 佔用一張 GPU"
      - "MPS：多個 Job 可以共用執行資源"
      - "Scheduler 同時決定 placement 與 share"
speaker_notes:
  - "先接回上一頁的 exclusive allocation 假設。"
  - "用兩個各 50% 的 Job 當例子，再問學生哪個決策是新增的。"
worked_example:
  scenario: "Job A 與 Job B 各使用 50%"
source_refs:
  - "NVIDIA MPS documentation"
```

`supporting_content.type` 可以是 `annotations`、`paragraph`、`list`、`table_rows`、`code_lines`、`labels`、`formula` 或 `none`。不要把所有頁都硬轉成 Bullet。

### 文稿樣稿 Gate

先挑 3 到 5 張不同教學角色做文稿樣稿，例如 Definition、Mechanism、Worked Example、Code Walkthrough、Check。使用者確認語氣、深度與資訊密度後，再完成其餘頁面。

Gate C：確認文稿與 Speaker Notes 後才進視覺設計。

## 階段 3：語意化 Visual Storyboard

逐頁執行：

`Teaching Intent → Information Relation → Visual Encoding → Slide Grammar → Layout → Deck Rhythm`

必讀：

- `references/layout-decision-engine.md`
- `references/diagram-ontology.md`
- `references/slide-grammar.md`
- `references/deck-rhythm.md`

每頁 Storyboard 至少包含：

```yaml
slide: 12
teaching_claim: "MPS 讓 GPU 配置從整張卡變成可分割的 share"
information_relation: "transformation + resource allocation"
visual_encoding:
  primary: "before/after resource allocation diagram"
  secondary: "3 個短註解"
slide_type: "G14 Transformation"
rhythm: "dense"
layout:
  composition: "40/60"
  text_region: "left"
  visual_region: "right"
visual_spec:
  before: "1 GPU, 1 Job, 100%"
  after: "1 GPU, 2 Jobs, 50% + 50%"
source: "NVIDIA MPS documentation"
```

只寫「Slide 12：MPS Architecture」不算完成 Storyboard。

Gate D：讓使用者確認整體視覺路由、代表版型與 Deck Rhythm。

## 階段 4：代表性 Demo

讀 `references/prototype-gate.md`。

從 Storyboard 選 4 到 6 張能覆蓋主要設計風險的頁面，通常包含：

- Cover 或 Section Divider
- Concept + Visual
- Diagram / Architecture
- Comparison / Table / Chart 中至少一種
- Code Walkthrough 或 Worked Example
- Check / Recap / Key Takeaway

真的產生可瀏覽的 HTML 或 open-slide Demo，不要只給文字描述。

Demo Review 要確認：

- Typography
- 中文斷行
- 資訊密度
- Visual Encoding 是否看得懂
- Diagram Edge / Node 語意
- Code Style
- Citation Style
- Deck Rhythm
- AI 味文字與 AI 味視覺

Gate E：等使用者確認 Demo 或提出修改。

## 階段 5：Design Lock

Demo 核准後建立 `design-lock.yaml`，格式參考 `templates/design-lock.yaml`。

至少固定：

- Canvas 與 Safe Margin
- Palette
- Typography
- Spacing
- Border / Radius
- Code Block
- Diagram Node / Edge Vocabulary
- Citation
- Section Numeral
- Deck Rhythm 限制
- 禁止使用的視覺套路

Gate F：Design Lock 確認後才全面生成。

## 階段 6：完整實作

Renderer 優先順序：

1. open-slide 已安裝或專案正在使用時採用 open-slide
2. 使用者既有 React/HTML Framework
3. generic fixed-stage HTML/React

依環境讀：

- `adapters/open-slide.md`
- `adapters/generic-html.md`

實作規則：

- 重複 Grammar 可以共用 Component，但每頁 Composition 仍要服從該頁語意
- Diagram 優先 inline SVG / React SVG
- 定量關係使用 Chart，不把數值塞進裝飾卡片
- 真實 UI、論文 Figure、歷史畫面與證據使用可信來源
- Speaker Notes 要能補上口頭推理，避免照念投影片
- 所有頁面讀取同一份 Design Lock
- 不為了維持頁數縮小文字
- 完成後要實際 Render 並檢查畫面

## Visual Representation 優先順序

在精確表達相同的前提下，預設順序：

1. Programmatic SVG / Chart
2. CSS 結構圖形與必要裝飾
3. Image Generation 或 Authoritative Source Image，依用途選擇
4. 純文字

真實性高於順序。產品介面、新聞畫面、Paper Figure、Benchmark Plot、歷史照片與紀錄型證據，優先用可信來源。

Generated Image 不得當作證據。

## Code 規則

- 少於 8 行：可顯示完整 Code Block
- 8 到 20 行：選出真正要講的行並加 Annotation
- 超過 20 行：拆頁或節錄
- 要講 Execution Behavior：Code 搭配 Trace / State Visualization
- 要講 Architecture Implication：Code 搭配 Architecture / Data Flow
- 要講 Syntax：保留 1 到 3 個 Callout
- 講者不會解釋的 Code 不放上投影片

## Table 規則

只有當學生需要精確做 row-by-column lookup 時才用 Table。

適合：比較 FCFS、SJF、RR 的 preemption、starvation、fairness、complexity。

不適合：解釋 SJF 為什麼降低平均等待時間。這種機制要改用 Timeline + Worked Example。

## 繁體中文與 AI 味規則

所有 on-slide copy、Speaker Notes、Section Title、Caption 與 Recap 都要讀 `references/anti-ai-style.md`。

幾個最高優先級限制：

- 不使用長破折號
- 不用企業話術與空泛形容詞撐內容
- 避免工整對仗式金句與機械三段排比
- 不用模糊歸因，外部主張要有具體來源
- 不用 Emoji 當 Bullet Icon
- 不讓每頁都變成三張或四張相同圓角卡片
- 不用裝飾性箭頭假裝 Diagram
- 抽象概念要配具體數字、狀態、案例、Command、資料或其他可驗證錨點

可執行時，對文稿執行：

```bash
python scripts/ai_tone_lint.py <manuscript.md-or-yaml>
```

## 階段 7：三層 QA

讀：

- `references/qa-checklist.md`
- `references/instructional-qa.md`
- `references/anti-ai-style.md`

QA 分成三層：

1. `instructional_qa`：Learning Goals 是否真的被內容、Example 與 Check 覆蓋
2. `visual_qa`：Overflow、Typography、Contrast、Diagram、Code、Citation
3. `deck_qa`：Rhythm、Style Drift、Layout 重複、AI 味、Section Pacing

只要有下列情況就不能交付：

- 一頁塞入多個互不相干的主要命題
- Layout 找不到明確的資訊關係理由
- 可以畫成 Diagram 的關係被退化成 Bullet Wall
- 多次出現超過 3 張連續 `dense`
- Code 長到課堂上無法逐段講解
- Table 被拿來教因果機制
- Diagram 的箭頭、邊界或 Node 沒有明確語意
- 字體過小、內容溢出或遮擋
- 後半段出現 Style Drift
- Generated Image 被當成證據
- 文稿有大量套話、空泛形容詞、無來源主張或固定 AI 修辭

最後輸出 QA Report，格式參考 `templates/qa-report.yaml`。
