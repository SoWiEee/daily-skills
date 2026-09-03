# 代表性 Demo 與核准流程

完整實作前先做 4 到 6 張代表性 Demo。Demo 的任務是暴露設計問題，不追求把整份簡報提前做完。

## 選頁原則

Demo 要覆蓋不同風險：

```yaml
demo_selection:
  - slide: 1
    reason: "Cover 與整體視覺語言"
  - slide: 6
    reason: "典型 Concept + Visual"
  - slide: 12
    reason: "Architecture / Diagram Edge 語意"
  - slide: 18
    reason: "Code Walkthrough 與中文註解"
  - slide: 24
    reason: "Comparison / Table / Chart"
  - slide: 31
    reason: "Check / Recap / Key Takeaway"
```

不要只挑最好做的頁面。要刻意包含最容易失敗的密集頁、Code 頁與 Diagram 頁。

## Demo 交付

優先用最終 renderer 產生：

- open-slide 專案：實際建立代表頁並啟動可瀏覽 Demo
- 既有 React：建立獨立 Demo route 或 story page
- generic HTML：輸出一個可用左右鍵切換的 Demo HTML

## Review Checklist

請使用者確認：

- 中文字體與斷行自然嗎
- Title 大小與內容密度合適嗎
- Diagram 是否第一眼就看出關係
- Annotation 是否太多
- Code Block 是否能在投影環境閱讀
- Source 是否可見但不搶畫面
- Color Accent 是否有語意
- Section 與 Content Page 的節奏差距夠不夠
- 有沒有像 AI Dashboard 的 Card Grid
- 文案有沒有套話、口號或過度工整的句型

## 核准後

把核准結果寫入 `design-lock.yaml`。完整實作只能讀 Design Lock 中已核准的值，不要在第 20 頁突然新增色彩、Font、Shadow 或 Diagram Style。
