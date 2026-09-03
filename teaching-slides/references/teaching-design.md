# 教學流程設計

不同教材要用不同的教學順序。以下是預設骨架，依使用者受眾與時間調整。

## 一般概念課

`問題情境 → Intuition → Mechanism → Worked Example → 限制或 Failure Mode → Check → Recap`

## Algorithm

`問題 → Intuition → Algorithm → Trace → Complexity / Assumptions → Failure Case → Comparison → Check`

Trace 優先使用 G26 Worked Example，方法比較可用 G12 Matched Comparison 或 G15 Trade-off。

## System / Architecture

`問題 → Architecture Overview → Component Roles → Data / Control Flow → Deep Dive → Failure Mode → Operational Example → Recap`

先給一張 G19 Architecture 當 Mental Model，再拆 Component Detail。不要第一張就放滿 20 個 Node。

## Code Tutorial

`目標 → Mental Model → Minimal Code → Annotated Walkthrough → Runtime Behavior → Common Mistake → Modification Exercise → Takeaway`

不要用大型 Code Dump 當開場。

## Paper Walkthrough

`Research Question → 既有方法限制 → Method Intuition → Method Diagram → Experiment Design → Key Result → Limitation → Implication`

保留論文原本 Claim、數值、條件與不確定性。講者自己的解讀要和來源結論分開。

## Case Study

`Context → Incident / Problem → Sequence / Evidence → Mechanism / Root Cause → Response → Lessons → Check`

涉及 Screenshot、Timeline、新聞、官方報告或事件資料時，Evidence 優先用可信來源。

## Reading-first 原則

Reading-first 代表支持資訊比較完整，不代表可以增加互不相關的主要命題。學生應該能在每頁快速找出「這頁要我懂什麼」。
