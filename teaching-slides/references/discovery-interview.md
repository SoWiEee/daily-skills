# 多輪需求訪談

需求訪談的目的是找出教學決策需要的資訊，不要把它做成制式問卷。

## 訪談原則

1. 已經知道的資訊不再問一次。
2. 一輪以 3 到 5 個高價值問題為主。
3. 每一輪都根據上一輪答案改變下一輪問題。
4. 問題要能改變教學架構、資訊密度、Example、Interaction 或 Implementation。
5. 只有偏好差異會影響成果時才問偏好。
6. 必要欄位齊全就停止，不為了湊滿四輪繼續問。

## 第 1 輪：教學任務

優先確認：

- 這份簡報要用在哪種課程情境
- 受眾是誰
- 一次授課多久
- 目前有哪些教材或來源
- 課後是否要讓學生單獨閱讀

範例問題：

- 這堂課是正式課程、Tutorial、Workshop、複習課，還是論文導讀？
- 學生大概是什麼程度，已經修過哪些相關內容？
- 預計講多久，會不會拆成多個 Session？
- 你手上有完整教材、粗略筆記，還是只有主題？

## 第 2 輪：學習目標與困難點

根據第 1 輪答案追問：

- 課後最希望學生能做什麼
- 哪些地方常誤解
- 哪些推導或細節必須保留
- 哪些內容可以略過
- 需不需要 Worked Example

把 Learning Goal 寫成可驗證動詞，例如「能判斷」、「能解釋」、「能手算」、「能修改」、「能比較」。避免只寫「了解」。

## 第 3 輪：教學互動與技術深度

有需要才問：

- Code 比重與語言
- 是否安排 Check、Mini Exercise、Live Demo
- Citation 嚴謹度
- 公式與推導深度
- 是否允許補外部資料
- 要不要 Speaker Notes

## 第 4 輪：實作與交付限制

只有前面無法推定時才問：

- open-slide 是否已存在
- 是否要 generic HTML / React fallback
- 交付形式
- 品牌或固定視覺規範
- 是否有硬性頁數上限

## 停止條件

以下資訊已經足以做教學架構時就停止訪談：

```yaml
required:
  purpose: known
  audience: known
  prior_knowledge: known_or_reasonably_inferred
  duration: known_or_flexible
  learning_goals: known
  source_material: known
  reading_first: known
optional_but_useful:
  likely_gaps: known_or_inferred
  interaction: known_or_default
  code_depth: known_or_default
  renderer: known_or_auto_detect
```

## 訪談後摘要

訪談結束後先回報推定與未確定項目，請使用者確認。不要在同一則訊息偷跑進完整實作。
