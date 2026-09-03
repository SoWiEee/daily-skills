# QA Checklist

## Visual QA

- [ ] 所有 Slide 維持 1920×1080
- [ ] Safe Margin 內沒有被切掉的內容
- [ ] 沒有 Text Overflow、Panel Overlap 或意外 Scroll
- [ ] 中文最小字級仍可在投影環境閱讀
- [ ] Code Block 不需要縮到難讀
- [ ] Chart 的 Axis、Legend、Unit 完整
- [ ] Diagram 的 Node、Edge、Boundary 有清楚語意
- [ ] Citation 可讀且不搶主要內容
- [ ] Color Contrast 足夠
- [ ] 後半段沒有自行長出新 Font、Color、Radius、Shadow

## Semantic QA

- [ ] 一頁只有一個主要 Teaching Claim
- [ ] Layout 能說出對應的 Information Relation
- [ ] Bullet 真的是 List
- [ ] Table 用在 Lookup，不拿來教 Mechanism
- [ ] Code 都是課堂上會實際講解的部分
- [ ] Generated Image 沒有被當成 Evidence

## Deck QA

- [ ] 沒有多次出現超過 3 張連續 `dense`
- [ ] 連續 4 張同 Composition 有明確教學理由
- [ ] Section 開始與結束有清楚 Orientation
- [ ] Demo 核准後的 Design Lock 全程一致
- [ ] AI 味視覺檢查通過

## 文稿 QA

- [ ] 通過 `anti-ai-style.md`
- [ ] 沒有長破折號
- [ ] 沒有模糊歸因
- [ ] 沒有空泛企業話術
- [ ] 每個主要 Section 有具體 Example / Evidence / Trace
- [ ] Speaker Notes 沒有逐字重複投影片
