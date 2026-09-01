# daily-skills README 設計規格

## 目標

為 `daily-skills` repository 撰寫一份以一般使用者為主要讀者的繁體中文 README，讓讀者能：

1. 迅速理解這 6 個 skills 各自解決的問題。
2. 依照目前的情境選擇合適的 skill。
3. 看懂每個 skill 的使用時機、限制與預期產出。
4. 將 skills 安裝到 Codex、Claude Code 或 OpenCode。
5. 透過示範案例理解輸入與結果的關係。

## 讀者與語氣

- 主要讀者是第一次接觸這個 repository 的一般使用者，不假設讀者熟悉 YAML、CLI 或 agent skills。
- 使用台灣繁體中文，先講用途，再補充技術細節。
- 將示範案例明確標示為「示範」，不把虛構對話描述成真實使用紀錄。
- 保持實用與低門檻，避免把各個 `SKILL.md` 的完整內部流程複製到 README。

## README 結構

### 1. 專案簡介

說明這是一組以 `SKILL.md` 為入口的可重複使用 AI 工作流程，涵蓋自我整理、關係與溝通，以及電腦科學論文調研。

### 2. 快速選擇

用表格將使用者的問題對應到 skill：

- 想整理當下情緒或日記：`reflective-journal`
- 想處理反覆自責、焦慮、完美主義或內耗：`ease-inner-conflict`
- 想處理具體關係互動、界限或回覆：`relational-anxiety-support`
- 想預演、復盤或練習一場對話：`dialogue-practice`
- 想重新盤點人生方向、目標或卡住的問題：`life-reset-audit`
- 想深入拆解一篇電腦科學論文：`paper-survey`

### 3. 六個 skill 詳介

每個 skill 都用固定欄位介紹：

- 用途
- 適合什麼時候使用
- 不適合什麼情況
- 會協助整理或產出什麼
- 入口檔案連結

其中四個相近的對話型 skills 需要特別呈現分工，避免使用者在 `reflective-journal`、`ease-inner-conflict`、`relational-anxiety-support` 與 `dialogue-practice` 之間選錯。

### 4. 示範案例

至少提供下列類型的案例，格式為「使用者輸入 → 適合的 skill → 預期結果」：

- 明天要和主管談工作分配：對話準備與腳本骨架。
- 因為對方沒有回訊息而反覆自責：辨認內耗與一個低耗下一步。
- 想拒絕家人的臨時要求：釐清界限與可直接修改的回應說法。
- 想每天記錄心情：短篇自我覺察日記與給未來自己的小紙條。
- 有目標但一直沒有行動：把模糊卡住的地方轉成可驗證的小實驗。
- 需要讀懂一篇 CS 論文：研究問題、方法、證據、限制與口頭說明。

案例結果只描述 skill 的預期產出，不宣稱保證特定心理或研究成果。

### 5. 安裝與使用

先說明共同格式：每個 skill 是一個資料夾，必須保留 `SKILL.md` 與其同層的 `references/` 等支援檔案。

提供三種平台的專案級與個人級安裝方式：

| 平台 | 專案級 | 個人／全域 |
| --- | --- | --- |
| Codex | `.agents/skills/<name>/SKILL.md` | `~/.agents/skills/<name>/SKILL.md` |
| Claude Code | `.claude/skills/<name>/SKILL.md` | `~/.claude/skills/<name>/SKILL.md` |
| OpenCode | `.opencode/skills/<name>/SKILL.md` | `~/.config/opencode/skills/<name>/SKILL.md` |

示範以完整資料夾複製為主，並提供 Windows PowerShell 與 macOS/Linux 的複製範例。另補充 OpenCode 可讀取 `.claude/skills` 與 `.agents/skills`，但使用 `.opencode/skills` 最能表達平台專屬設定。

使用方式需說明：

- Codex 可用 `$skill-name` 或 `/skills` 檢查與明確呼叫。
- Claude Code 可用 `/skill-name` 呼叫，也可能依 description 自動載入。
- OpenCode 會列出可用 skills，並依權限與設定透過 `skill` 工具載入。
- 如果新增後沒有出現，重新啟動對應工具；Codex 與 Claude Code 的行為依版本可能不同。

### 6. 安全與邊界

說明心理支持類 skills 不提供診斷、治療、醫療建議，也不取代危機支援；遇到自傷、他傷、暴力、威脅或立即危險時，應優先聯絡當地緊急服務與專業支援。`paper-survey` 需以使用者提供的論文、預印本、PDF 或完整文字作為分析依據。

### 7. 目錄與延伸閱讀

列出根目錄下的 6 個 skill 資料夾，說明 `SKILL.md` 是主要入口，`references/` 是按需讀取的輔助內容，並連結到各自檔案。

## 非目標

- 不修改任何 skill 的行為或 `SKILL.md` 內容。
- 不建立安裝腳本、套件管理器或跨平台自動化工具。
- 不把 README 寫成完整的心理諮詢指南或論文分析教科書。
- 不新增未存在於 repository 的 skill。

## 驗收條件

1. README 以繁體中文撰寫，且一般使用者可在快速選擇表中找到對應 skill。
2. 6 個 skills 全部被介紹，且每個都有用途、使用時機、限制與預期產出。
3. 至少 6 個示範案例清楚標示輸入、skill 與預期結果。
4. Codex、Claude Code、OpenCode 都有專案級與個人級安裝位置及可複製的安裝命令。
5. 安裝範例保留整個 skill 資料夾，不會遺漏 references 檔案。
6. 所有 README 內部連結都指向目前存在的檔案或資料夾。
7. README 不把示範案例或平台行為描述成未經確認的保證。

## 參考來源

- [OpenAI：Build skills](https://developers.openai.com/codex/skills/)
- [Claude Code：Extend Claude with skills](https://code.claude.com/docs/en/slash-commands)
- [OpenCode：Agent Skills](https://opencode.ai/docs/skills)
