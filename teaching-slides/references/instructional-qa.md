# Instructional QA

這份 QA 檢查「學生學不學得會」，不檢查 CSS 美觀。

## 1. Learning Goal Coverage

對每個 Learning Goal 建立 Coverage Map：

```yaml
learning_goal: "能比較 FCFS、SJF、RR 的排程行為"
covered_by:
  explanation: [12, 13, 14]
  worked_example: [15]
  check: [17]
  recap: [18]
status: "covered"
```

如果 Learning Goal 只出現在 Learning Objectives，後面沒有實際教學與 Check，就算未覆蓋。

## 2. 先備知識橋接

檢查每個新概念是否依賴未介紹的術語。缺少先備知識時，補一張 Bridge Slide 或在前一頁加入最小必要定義。

## 3. Example Quality

Worked Example 要做到：

- Input 明確
- 中間狀態可追蹤
- 每一步對應剛教過的規則
- 結果可驗證
- 至少一個地方能讓學生預測下一步

只給答案沒有推理過程不算 Worked Example。

## 4. Check Quality

Check-your-understanding 要測 Learning Goal，不問瑣碎記憶。

好的 Check 類型：

- 預測下一個 State
- 選出會失敗的條件
- 比較兩種方法的結果
- 修改一行 Code 後推測行為
- 解釋 Diagram 中一條 Edge 的意義

## 5. Recap Quality

Recap 要重新組織概念關係。只把前面 Title 再列一次，視為無效 Recap。

## 6. Reading-first 檢查

抽一張密集內容頁，假設沒有講者：

- Title 能不能知道這頁在回答什麼
- Diagram Label 是否完整
- Annotation 能不能補上關鍵推理
- Source 是否能查回去
- 是否需要 Speaker Notes 才能理解核心命題

最後一項如果答案是「需要」，就要補足 on-slide content。
