# 簡報文稿與 Speaker Notes

這一層負責教學內容，先不碰 React Component、CSS Grid 或 SVG 座標。

## 每頁必填欄位

```yaml
slide: 8
teaching_claim: "SJF 在已知 burst time 時能降低平均等待時間"
learner_question: "短工作先跑，為什麼會讓整體平均等待時間下降？"
on_slide_message:
  title: "短工作先執行會減少後續工作的累積等待"
  supporting_content:
    type: "annotations"
    items:
      - "Jobs: 8, 4, 2"
      - "FCFS total wait: 0 + 8 + 12"
      - "SJF total wait: 0 + 2 + 6"
speaker_notes:
  - "先請學生只看三個 burst time，不先講公式。"
  - "依序算兩種排程的等待時間，再問差異來自哪一個 Job。"
worked_example:
  scenario: "P1=8, P2=4, P3=2"
source_refs: []
```

## `supporting_content.type`

可以使用：

- `annotations`：少量註解或 Callout
- `paragraph`：一小段需要完整語句的說明
- `list`：真正互相獨立的清單
- `table_rows`：後續會成為精確查表資訊
- `code_lines`：後續會做 Code Walkthrough
- `labels`：Diagram Node 或 Region 名稱
- `formula`：公式與符號定義
- `none`：視覺本身就足夠

不要預先把所有內容寫成 Bullet。

## Title 規則

一般解釋頁優先使用能直接說出教學命題的 Title。Section Divider、Code Demo、Reference 或純定義頁可以用描述式 Title。

Title 要短、具體、可驗證。避免「全面解析」、「一次掌握」、「完整攻略」、「關鍵洞察」這類沒有新增資訊的字。

## Speaker Notes 規則

Speaker Notes 補上投影片沒有放的推理、節奏與提問方式。不要逐字重複 on-slide copy。

好的 Notes 會記錄：

- 前一頁怎麼接過來
- 這頁先看哪裡
- 要問學生什麼
- 哪個錯誤直覺要攔住
- Example 算到哪一步停一下
- 哪個細節留到下一頁

## 文稿樣稿

完整文稿開始前，先挑 3 到 5 張代表頁：

1. 一張 Concept / Definition
2. 一張 Mechanism / Diagram-heavy 頁
3. 一張 Worked Example
4. 有 Code 時加入 Code Walkthrough
5. 一張 Check 或 Recap

使用者確認語氣與深度後，再完成其餘頁。

## 具體錨點

每個主要 Concept Section 至少要有一個具體錨點，依主題可以是：

- 明確數字
- 真實 Command
- 一段可執行 Code
- 一組 Input / Output
- 一個 State
- 一個真實產品或系統名稱
- 一筆資料或 Benchmark
- 一個有來源的事件

抽象名詞連續出現時，要回到具體動作或可觀察狀態。
