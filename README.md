# daily-skills

<img width="1192" height="298" alt="圖片" src="https://github.com/user-attachments/assets/95f90de5-7a3f-471b-a9ae-8f69757d0548" />

一組以台灣繁體中文撰寫的 AI skills，協助你整理內在狀態、處理關係與溝通、重新盤點人生方向，以及深入閱讀電腦科學論文。

每個 skill 都是一個包含 `SKILL.md` 的資料夾。AI 工具會先根據 `name` 和 `description` 判斷何時適合使用，再按需要讀取完整指引與 `references/` 裡的輔助資料。

本 repository 不是需要編譯或執行的程式；安裝的重點是把完整的 skill 資料夾放到你使用的 AI 工具能搜尋的位置。

想直接看「實際用了 skill 之後會得到什麼」，請參考 [`conversation.md`](conversation.md)。裡面記錄了六個 skill 各自一次的 subagent 演練、使用者情境、對話摘錄與整理後的結果。

## 快速選擇

不知道該使用哪一個時，先從你現在想處理的事情開始：

| 你現在比較想處理什麼？ | 建議使用 | 主要會得到什麼？ |
| --- | --- | --- |
| 想整理今天的心情、混亂思緒或一段時間的變化 | [`reflective-journal`](reflective-journal/SKILL.md) | 一段有對話感的自我覺察與給未來自己的小紙條 |
| 一直反覆想、自責、比較、拖延、完美主義或過度負責 | [`ease-inner-conflict`](ease-inner-conflict/SKILL.md) | 白話的內在理解、可使用的內心對話與一個低耗行動 |
| 因家人、伴侶、朋友或同事的具體行為而焦慮，想拒絕、設界限或回訊息 | [`relational-anxiety-support`](relational-anxiety-support/SKILL.md) | 事實與責任的整理，以及較能說出口的回應骨架 |
| 想預演、復盤、角色扮演或準備一場重要對話 | [`dialogue-practice`](dialogue-practice/SKILL.md) | 對話目標、可能反應、關鍵問句與腳本骨架 |
| 明明有目標卻一直卡住，或想重新設計人生方向 | [`life-reset-audit`](life-reset-audit/SKILL.md) | 行為證據、競爭假設、可逆實驗與回顧迴圈 |
| 想完整拆解一篇電腦科學論文或預印本 | [`paper-survey`](paper-survey/SKILL.md) | 研究地圖、方法與證據分析、限制、批判性評估與口頭說明 |

最簡單的判斷方式是：

- **事情發生在你心裡**，先看 `reflective-journal` 或 `ease-inner-conflict`。
- **事情發生在一段具體互動裡**，先看 `relational-anxiety-support` 或 `dialogue-practice`。
- **事情關於人生方向與行動系統**，看 `life-reset-audit`。
- **事情關於研究論文與證據**，看 `paper-survey`。

## 六個 skills

### 1. `reflective-journal`｜自我覺察日記

#### 用途

提供一個溫和、有對話感的空間，讓你整理今天的心情、腦中的混亂、卡住的事情，或回頭看看一段時間裡發生了什麼。

#### 適合什麼時候使用

- 「我不知道自己怎麼了，只想先整理一下。」
- 「今天發生很多事，我想寫日記但不知道從哪裡開始。」
- 「我最近一直很緊，想慢慢看清楚自己的感覺。」
- 「我想回顧這一週，看看自己有沒有反覆出現什麼模式。」

#### 不適合什麼時候使用

- 你主要想準備一場與他人的對話，使用 `dialogue-practice`。
- 你要處理具體的關係互動、拒絕、界限或安全問題，使用 `relational-anxiety-support`。
- 你主要陷在反覆自責、比較、完美主義或拖延，想理解這個反應為什麼一直出現，使用 `ease-inner-conflict`。

#### 實際演練結果

Skill 會依你的狀態，從「卡住」、「焦慮」、「整理今天」或「回顧一段時間」開始。收尾通常會留下：

- 今天最重要的看見。
- 一句可以帶走的話。
- 給未來自己的小紙條，以及下次可以接續的方向。

完整案例：[`conversation.md`｜Case 4: reflective-journal](conversation.md#case-4-reflective-journal)。

它不會把普通的低落、焦慮或疲累直接當成危機，也不會進行心理診斷。若出現明確的自傷、他傷或立即危險，會先把安全與專業支援放在日記流程之前。

詳細指引：[`reflective-journal/SKILL.md`](reflective-journal/SKILL.md)

### 2. `ease-inner-conflict`｜內耗陪伴與轉化

#### 用途

陪你慢慢看懂反覆思考、自責、關係焦慮、自我懷疑、比較、拖延、完美主義或過度負責背後正在保護什麼，以及這些做法長期帶來的代價。

#### 適合什麼時候使用

- 「對方只是一段時間沒回，我卻一直重看訊息。」
- 「我知道事情不一定是我的錯，但還是一直怪自己。」
- 「我一直修改計畫，卻始終沒有真的開始。」
- 「我不敢只做到 80 分，總覺得還要再多做一點。」
- 「我想理解為什麼這類反應總是出現，而不是只處理眼前這一次。」

#### 不適合什麼時候使用

- 眼前有明確的人、事件或訊息，你要先知道怎麼回、怎麼拒絕或是否安全，先使用 `relational-anxiety-support`。
- 你只是想做一般日記，使用 `reflective-journal`。
- 你要求診斷、治療或藥物判斷，應尋求合格專業協助。
- 有自傷、他傷、暴力威脅或立即危險時，先處理安全，不進行一般內省流程。

#### 實際演練結果

在理解足夠後，通常會整理成三個部分：

1. 一段白話說明，指出發生了什麼、你在怕什麼，以及原本的反應想保護什麼。
2. 一段貼近你語氣的內心對話。
3. 一個小、具體、可停止的低耗行動，例如暫停重讀訊息、把任務縮成 5～10 分鐘，或先做 80 分版本。

完整案例：[`conversation.md`｜Case 2: ease-inner-conflict](conversation.md#case-2-ease-inner-conflict)。

它不會把一次回答變成固定的人格分類，也不會把自我檢視的結果當成診斷。

詳細指引：[`ease-inner-conflict/SKILL.md`](ease-inner-conflict/SKILL.md)

### 3. `relational-anxiety-support`｜關係焦慮陪伴

#### 用途

處理一段正在發生或剛發生的具體關係互動，先分開事實、害怕、責任與安全，再協助你找出界限或下一句比較能說出口的話。

#### 適合什麼時候使用

- 「家人臨時要我答應一件事，我不知道怎麼拒絕。」
- 「伴侶不開心時，我會立刻覺得自己做錯了。」
- 「同事把工作丟給我，我想回覆但怕關係變差。」
- 「我想知道這段互動是不是已經超過我的界限。」
- 「我和對方吵完後一直反覆想，想先整理這次發生了什麼。」

#### 不適合什麼時候使用

- 具體互動已經處理完，你想理解自己為什麼長期反覆自責、比較或完美主義，轉到 `ease-inner-conflict`。
- 你要的是完整的對話預演、對方可能反應與多輪角色扮演，使用 `dialogue-practice`。
- 有持續威脅、暴力、跟蹤、控制或立即危險時，安全優先，不能只靠溝通技巧處理。

#### 實際演練結果

Skill 會協助你：

- 說出對方實際做了什麼，而不是先替對方貼標籤。
- 分清楚你的責任、對方的情緒，以及你無法控制的部分。
- 釐清你想保住的是時間、關係、尊重還是安全。
- 產生一至三種回應骨架，例如「承認對方在意的事＋說明自己的狀態＋說清楚能做與不能做的部分＋提出下一步」。
- 用一個小實驗觀察新界限或新回應的實際結果。

完整案例：[`conversation.md`｜Case 3: relational-anxiety-support](conversation.md#case-3-relational-anxiety-support)。

詳細指引：[`relational-anxiety-support/SKILL.md`](relational-anxiety-support/SKILL.md)

### 4. `dialogue-practice`｜對話陪練室

#### 用途

這是一個給成年使用者的溝通策略分析工具，適合準備、復盤或角色扮演工作與生活中的重要對話。

#### 適合什麼時候使用

- 「明天要和主管談工作分配，我想先預演。」
- 「剛才的會議沒有談好，我想復盤自己哪裡可以調整。」
- 「我有一件事一直沒開口，想先想好第一句。」
- 「我想理解對方可能怎麼聽到這句話，再準備幾種回應。」
- 「我想用角色扮演練習一次談判或工作溝通。」

#### 不適合什麼時候使用

- 本 skill 以 18 歲以上成年使用者為對象。
- 不用於醫療、健康諮詢或需要專業協助的個人狀況。
- 不會評論對方的人格、不替你判斷誰對誰錯，也不會把內容寫成一定要照念的逐字稿。
- 如果你現在主要需要情緒安頓，而不是研究怎麼說，先使用 `reflective-journal` 或 `ease-inner-conflict`。

#### 實際演練結果

依你的需求，可能得到：

- 對話的情境、核心訴求與最希望得到的結果。
- 對方可能的反應，以及你可以採取的回應方向。
- 開口的第一句、關鍵問句、應對方式與對話中的提醒。
- 一份保留彈性的「腳本骨架」，方便你用自己的語氣說出來。

完整案例：[`conversation.md`｜Case 1: dialogue-practice](conversation.md#case-1-dialogue-practice)。

詳細指引：[`dialogue-practice/SKILL.md`](dialogue-practice/SKILL.md)

### 5. `life-reset-audit`｜人生重啟審視

#### 用途

把「我不想再這樣下去」、「我有目標但一直卡住」或「我不知道自己真正重視什麼」，整理成暫定方向、可觀察的行動與能持續修正的回饋迴圈。

#### 適合什麼時候使用

- 「我想重新盤點目前的生活方向。」
- 「我知道想轉職，但一直改目標、沒有行動。」
- 「我想知道一個反覆卡點到底是策略問題、環境問題還是執行問題。」
- 「我想把大方向拆成一年結果、一個月專案、這週和明天的行動。」
- 「我做過一次計畫，想比較預測與實際結果。」

#### 四種模式

| 模式 | 適合的情況 | 主要產出 |
| --- | --- | --- |
| `full-reset` | 想完整盤點目前的生活與方向 | 現況、暫定方向、Vision、目標層級與下一步 |
| `stuck-problem` | 只有一個反覆出現的卡點 | 行為證據、2～4 個競爭假設、一次低成本實驗與回顧條件 |
| `goal-design` | 已知道想去哪裡，只需要設計走法 | 方向、限制、目標層級、daily levers 與 feedback rules |
| `review` | 已執行過一輪計畫，想看落差 | 預測與實際差異，以及保留、調整、暫停或停止的決定 |

#### 實際演練結果

一次 `stuck-problem` 演練會把「一直改題目」拆成幾個可檢驗的假設，再安排一個 90 分鐘、只產出一頁粗版本的測試，而不是直接下結論說你缺乏自律。

完整案例：[`conversation.md`｜Case 5: life-reset-audit](conversation.md#case-5-life-reset-audit)。

#### 不適合什麼時候使用

- 如果你現在被強烈自責、羞愧或焦慮淹沒，先使用 `ease-inner-conflict`。
- 不把拖延或執行失敗直接解讀成懶惰、人格缺陷或人生定論。
- 不把暫定假設包裝成事實，也不承諾一天就能改變人生。
- 若涉及自傷、他傷、立即危險、嚴重失眠或長期無法正常生活，先尋求專業支援。

詳細指引：[`life-reset-audit/SKILL.md`](life-reset-audit/SKILL.md)

### 6. `paper-survey`｜電腦科學論文調研助手

#### 用途

把一篇電腦科學論文重建成一條可檢查的研究論證鏈，而不只是把摘要改寫一次。它會協助你看懂研究問題、方法、資料、baseline、metrics、證據、貢獻、限制與領域定位。

#### 適合什麼時候使用

- 你提供一篇論文、預印本、PDF 或完整文字，想做完整研究地圖。
- 你正在讀演算法、機器學習、系統、軟體工程、理論、benchmark、資安或 HCI 論文。
- 你想檢查作者的 claim 是否真的由資料、模型、實驗或形式化結果支持。
- 你想準備 seminar、讀書會、課堂討論或口頭報告。

#### 不適合什麼時候使用

- 只想要很短的摘要、逐段翻譯、文法潤稿或引用格式整理。
- 只提供論文標題，卻要求判斷具體方法和結果。
- 想直接執行論文程式、重現實驗或做一般除錯。
- 論文沒有提供的資料、baseline、超參數或實驗結果，不會被自行補寫。

#### 實際演練結果

完整分析通常包含：

- `Evidence Boundary`：目前有哪些材料、能回查哪些頁碼或 section、哪些內容無法確認。
- `Research Map`：問題、方法、資料、baseline、metrics、主要 findings 與 contributions。
- 方法、資料、系統、實驗設定與可重現性檢查。
- 結果與作者解釋的區分，以及 alternative explanations。
- 作者聲稱的貢獻、論文實際支持的部分與限制。
- 一句話、30 秒、3 分鐘與課堂討論版本的口頭說明。

它會把「作者主張」、「論文結果」、「文本分析」、「無法確認」與「外部脈絡」分開，避免把推論當成論文已證明的事實。

完整案例：[`conversation.md`｜Case 6: paper-survey](conversation.md#case-6-paper-survey)。案例使用虛構的 PatchWise 論文片段，示範如何從「單一合成 benchmark 有改善」收斂到較窄、而且證據支持得住的結論。

詳細指引：[`paper-survey/SKILL.md`](paper-survey/SKILL.md)

## 實際演練案例

以下六個案例整理自本次讓 subagent 各使用一次對應 skill 的演練。情境與論文材料是為了示範而設定的，不是真實個案或真實研究結果；對話摘錄與回答則保留了這次演練中實際產出的內容。完整版本請看 [`conversation.md`](conversation.md)。

### 案例一：準備和主管談工作分配

**使用者輸入**

> 這週有三項工作同時到期：客戶簡報、內部報告和新流程測試。我想和主管討論優先順序與範圍，但不想聽起來像是在推卸工作。

**適合的 skill**：`dialogue-practice`

**這次演練的結果**

先釐清你想守住的重點與希望得到的結果，再整理開場句、關鍵問句，以及主管可能回應時的接話方向。例如：

> 主管，我整理了三項工作的進度和時間估算，想先和你確認優先順序與範圍。我的建議是先完成客戶簡報，內部報告縮小範圍，流程測試先做基本版本。

也可以接著問：「這週如果只能先完成 2 項，您會建議我排哪兩項？」

最後會給你一份腳本骨架，而不是要求你逐字背誦。

### 案例二：對方沒有回訊息而反覆自責

**使用者輸入**

> 他四個小時沒回我，我一直重看自己上一句是不是說錯了。

**適合的 skill**：`ease-inner-conflict`

**這次演練的結果**

協助你分開「對方四小時沒回」這個事實，和「他一定是因為我說錯話才不理我」這個推測。接著可能整理出一句內心話：

> 我現在很不安，是因為我在乎這段關係，不是因為我已經確定自己做錯了。

以及一個低耗行動，例如先在 30 分鐘內不重讀訊息，再決定是否需要傳一則單純確認的訊息。

### 案例三：想拒絕家人的臨時要求

**使用者輸入**

> 我媽突然叫我今晚回家整理房間，還說明天親戚要來。我今天上班已經累到不行，但又不敢拒絕，怕她覺得我很自私、很失望。

**適合的 skill**：`relational-anxiety-support`

**這次演練的結果**

先確認家人實際提出了什麼、是否有安全或急迫性，再釐清你想保住的界限。可能產生這樣的回應骨架：

> 我知道你很急，但我今天真的累到沒辦法再回去做事。今晚我先休息，週六早上我回去幫忙整理一段時間；如果還有沒弄完的，再一起想辦法。

這不是唯一正確的答案，會再依你的說話方式調整。

### 案例四：每天整理自己的狀態

**使用者輸入**

> 我今天沒有發生什麼大事，只是覺得整個人很累，想寫一點日記。

**適合的 skill**：`reflective-journal`

**這次演練的結果**

這次演練先請使用者選擇「整理今天」，再記下三件小事：早上喝到熱豆漿、同事幫忙留電梯、下班後沒有繼續工作而直接回家。收尾整理成：

> 我的力氣有限時，可以先停下來。好好回家，也是一件值得記下來的事。

並留下可以在下一次對話接續的小紙條。

### 案例五：有目標卻一直沒有行動

**使用者輸入**

> 我想做一個研究作品，但每次開始前都重新改題目，兩個月過去了還沒有第一個版本。

**適合的 skill**：`life-reset-audit`，使用 `stuck-problem` 模式

**這次演練的結果**

不急著把問題定義成缺乏自律，而是整理最近 2～8 週的行為證據，提出幾個競爭假設，例如：題目不夠清楚、害怕作品被評價，或任務範圍太大。接著設計一次低成本測試：

> 接下來 48 小時先不改題目，安排一次 25 分鐘的非正式製作測試：寫 5 個粗略訪談問題，並記錄修改題目的衝動。

如果又想換題，先延後 48 小時再決定，避免把短期不安直接當成方向不對。

測試結果是實際寫了 25 分鐘、完成 5 個問題，修改題目的衝動約 7/10，但仍然比原本更清楚自己想問什麼。

### 案例六：深入閱讀一篇 CS 論文

**使用者輸入**

> 這是論文 PDF。請幫我看它到底解決什麼問題、用了什麼方法、實驗是否真的支持作者的 claim，最後給我一個 30 秒口頭說明。

**適合的 skill**：`paper-survey`

**這次演練的結果**

本次演練使用一段虛構的 PatchWise 論文材料：在合成 SteelDefect-XS 資料集上，AUROC 為 92.1%，高於三個 baseline；移除局部重建分支後降到 89.5%。但缺少資料切分、洩漏控制、變異、信賴區間、完整 baseline 與跨工廠測試，因此結果只支持「這組實驗觀察到初步改善」，不能直接說成「已證明能泛化到真實工廠」。完整研究地圖與 30 秒版本見 [`conversation.md`｜Case 6](conversation.md#case-6-paper-survey)。

## 安裝前先知道這件事

每個 skill 都是完整資料夾，至少包含：

```text
skill-name/
├── SKILL.md                 # 必要，主要指引與 YAML metadata
└── references/              # 可選，該 skill 需要時才讀取的輔助資料
```

安裝時請複製整個資料夾，不要只複製 `SKILL.md`。這樣相對路徑引用的 `references/` 才會保留。

你可以只安裝一個 skill，也可以一次安裝全部 6 個。以下指令都假設你已經在這個 repository 的根目錄執行。

如果希望 skill 跟著專案走、讓團隊成員共用，使用「專案級」路徑；如果希望在所有專案都能使用，使用「個人／全域」路徑。

## 安裝到 Codex

### 放置位置

目前 Codex 的本機 skill discovery 位置如下：

| 範圍 | 路徑 | 適合用途 |
| --- | --- | --- |
| 專案級 | `.agents/skills/<name>/SKILL.md` | 只有目前專案或 repository 使用 |
| 個人級 | `~/.agents/skills/<name>/SKILL.md` | 你所有專案都能使用 |

Codex 也支援 symlink。若只是本機開發或測試，可以使用複製；若想讓 repository 直接反映原始資料夾的更新，也可以改用 symlink。

### Windows PowerShell：安裝到目前專案

在 repository 根目錄執行：

```powershell
$skillNames = @(
  "dialogue-practice",
  "ease-inner-conflict",
  "life-reset-audit",
  "paper-survey",
  "reflective-journal",
  "relational-anxiety-support"
)

$target = ".agents\skills"
New-Item -ItemType Directory -Force -Path $target | Out-Null

foreach ($skillName in $skillNames) {
  Copy-Item -Path ".\$skillName" -Destination $target -Recurse -Force
}
```

### macOS／Linux：安裝到目前專案

在 repository 根目錄執行：

```bash
skill_names=(
  dialogue-practice
  ease-inner-conflict
  life-reset-audit
  paper-survey
  reflective-journal
  relational-anxiety-support
)

target=".agents/skills"
mkdir -p "$target"
cp -R "${skill_names[@]}" "$target/"
```

### 安裝到 Codex 個人／全域位置

把上面指令中的目標改成：

```text
Windows PowerShell：$env:USERPROFILE\.agents\skills
macOS／Linux：       ~/.agents/skills
```

例如 Windows PowerShell：

```powershell
$skillNames = @(
  "dialogue-practice",
  "ease-inner-conflict",
  "life-reset-audit",
  "paper-survey",
  "reflective-journal",
  "relational-anxiety-support"
)

$target = Join-Path $env:USERPROFILE ".agents\skills"
New-Item -ItemType Directory -Force -Path $target | Out-Null

foreach ($skillName in $skillNames) {
  Copy-Item -Path ".\$skillName" -Destination $target -Recurse -Force
}
```

例如 macOS／Linux：

```bash
mkdir -p "$HOME/.agents/skills"
cp -R dialogue-practice ease-inner-conflict life-reset-audit \
  paper-survey reflective-journal relational-anxiety-support \
  "$HOME/.agents/skills/"
```

### 使用與確認

- 在 Codex CLI 或 IDE extension 中輸入 `/skills`，查看可用 skills。
- 也可以在提示中明確提及，例如：`$dialogue-practice`。
- 直接用自然語言描述任務時，Codex 也可能依照 `description` 自動選擇合適的 skill。
- 新增後若沒有出現，重新啟動 Codex。

## 安裝到 Claude Code

### 放置位置

| 範圍 | 路徑 | 適合用途 |
| --- | --- | --- |
| 專案級 | `.claude/skills/<name>/SKILL.md` | 只有目前專案使用，適合提交給團隊 |
| 個人級 | `~/.claude/skills/<name>/SKILL.md` | 你所有專案都能使用 |

Claude Code 會把資料夾名稱當成 skill 名稱。這裡的 `dialogue-practice` 會對應到 `/dialogue-practice`。

### Windows PowerShell：安裝到目前專案

```powershell
$skillNames = @(
  "dialogue-practice",
  "ease-inner-conflict",
  "life-reset-audit",
  "paper-survey",
  "reflective-journal",
  "relational-anxiety-support"
)

$target = ".claude\skills"
New-Item -ItemType Directory -Force -Path $target | Out-Null

foreach ($skillName in $skillNames) {
  Copy-Item -Path ".\$skillName" -Destination $target -Recurse -Force
}
```

### macOS／Linux：安裝到目前專案

```bash
mkdir -p .claude/skills
cp -R dialogue-practice ease-inner-conflict life-reset-audit \
  paper-survey reflective-journal relational-anxiety-support \
  .claude/skills/
```

### 安裝到 Claude Code 個人位置

把目標改成：

```text
Windows PowerShell：$env:USERPROFILE\.claude\skills
macOS／Linux：       ~/.claude/skills
```

例如 Windows PowerShell：

```powershell
$skillNames = @(
  "dialogue-practice",
  "ease-inner-conflict",
  "life-reset-audit",
  "paper-survey",
  "reflective-journal",
  "relational-anxiety-support"
)

$target = Join-Path $env:USERPROFILE ".claude\skills"
New-Item -ItemType Directory -Force -Path $target | Out-Null

foreach ($skillName in $skillNames) {
  Copy-Item -Path ".\$skillName" -Destination $target -Recurse -Force
}
```

### 使用與確認

- 啟動 Claude Code 後輸入 `/dialogue-practice`、`/reflective-journal` 等名稱，測試指定 skill。
- 你也可以直接描述任務，Claude Code 會依 `description` 判斷是否自動載入。
- 如果新 skill 沒有出現在清單，重新啟動 Claude Code；已存在的 skill 資料夾通常會被即時監看，但不同版本的行為可能不同。

## 安裝到 OpenCode

### 放置位置

| 範圍 | 路徑 | 適合用途 |
| --- | --- | --- |
| 專案級 | `.opencode/skills/<name>/SKILL.md` | OpenCode 專案專屬 skills |
| 個人級 | `~/.config/opencode/skills/<name>/SKILL.md` | 你所有 OpenCode 專案都能使用 |

OpenCode 也能讀取 Claude Code 相容的 `.claude/skills`，以及 agent 相容的 `.agents/skills`。如果你希望清楚表達這是 OpenCode 專屬設定，建議使用 `.opencode/skills`。

### Windows PowerShell：安裝到目前專案

```powershell
$skillNames = @(
  "dialogue-practice",
  "ease-inner-conflict",
  "life-reset-audit",
  "paper-survey",
  "reflective-journal",
  "relational-anxiety-support"
)

$target = ".opencode\skills"
New-Item -ItemType Directory -Force -Path $target | Out-Null

foreach ($skillName in $skillNames) {
  Copy-Item -Path ".\$skillName" -Destination $target -Recurse -Force
}
```

### macOS／Linux：安裝到目前專案

```bash
mkdir -p .opencode/skills
cp -R dialogue-practice ease-inner-conflict life-reset-audit \
  paper-survey reflective-journal relational-anxiety-support \
  .opencode/skills/
```

### 安裝到 OpenCode 個人位置

把目標改成：

```text
Windows PowerShell：$env:USERPROFILE\.config\opencode\skills
macOS／Linux：       ~/.config/opencode/skills
```

例如 Windows PowerShell：

```powershell
$skillNames = @(
  "dialogue-practice",
  "ease-inner-conflict",
  "life-reset-audit",
  "paper-survey",
  "reflective-journal",
  "relational-anxiety-support"
)

$target = Join-Path $env:USERPROFILE ".config\opencode\skills"
New-Item -ItemType Directory -Force -Path $target | Out-Null

foreach ($skillName in $skillNames) {
  Copy-Item -Path ".\$skillName" -Destination $target -Recurse -Force
}
```

例如 macOS／Linux：

```bash
mkdir -p "$HOME/.config/opencode/skills"
cp -R dialogue-practice ease-inner-conflict life-reset-audit \
  paper-survey reflective-journal relational-anxiety-support \
  "$HOME/.config/opencode/skills/"
```

### 使用與確認

- OpenCode 會把可用 skills 放進 skill catalog，並在需要時透過原生 `skill` 工具載入。
- 若你的版本啟用 slash catalog，也可以使用 `/dialogue-practice` 這類命令。
- 確認 `SKILL.md` 的檔名必須完全大寫，且 YAML frontmatter 至少包含 `name` 與 `description`。
- 如果看不到 skill，檢查目錄名稱是否唯一、權限是否允許載入，再重新啟動 OpenCode。

## 三個工具共用同一份 skills

如果你同時使用三個工具，可以依需求選擇共用或分開放置：

| 目的 | 建議做法 |
| --- | --- |
| Codex + OpenCode 共用 | 放到 `.agents/skills/`；OpenCode 支援 agent-compatible skills |
| Claude Code + OpenCode 共用 | 放到 `.claude/skills/`；OpenCode 支援 Claude-compatible skills |
| 三者都要穩定使用 | 按各自的專案級路徑複製：`.agents/skills/`、`.claude/skills/`、`.opencode/skills/` |
| 所有專案都要使用 | 分別複製到三個工具的個人／全域路徑 |

若三個工具同時掃描多個位置，請避免同名版本互相覆蓋。更新時也要同步更新整個資料夾，包含 `references/`。

## 常見問題

### 為什麼不能只複製 `SKILL.md`？

因為這些 skills 會依相對路徑讀取 `references/` 裡的輔助手冊。只複製入口檔會讓後續引導缺少資料。

### Skill 沒有自動啟動怎麼辦？

先用平台的明確呼叫方式測試，例如 Codex 的 `$dialogue-practice` 或 Claude Code 的 `/dialogue-practice`。如果明確呼叫也沒有作用，依序檢查：

1. `SKILL.md` 是否放在正確的 scope 路徑。
2. 檔名是否完全是大寫的 `SKILL.md`。
3. 資料夾名稱是否與 `SKILL.md` 的 `name` 一致。
4. `SKILL.md` 開頭是否有有效的 YAML frontmatter。
5. 平台是否因權限設定而禁止 skill。
6. 重新啟動工具後再試一次。

### 該用 `reflective-journal` 還是 `ease-inner-conflict`？

如果你只是想把今天的感覺說清楚、回顧一天或一段時間，先用 `reflective-journal`。如果你已經看見自己在反覆重播、自責、比較、拖延或完美主義裡打轉，想理解這個模式並找一個低耗行動，使用 `ease-inner-conflict`。

### 該用 `relational-anxiety-support` 還是 `dialogue-practice`？

如果你正在面對一段讓你焦慮的具體互動，重點是安全、責任、拒絕、界限或下一句怎麼回，先用 `relational-anxiety-support`。如果你要的是一場工作、協商或生活對話的預演、復盤、角色扮演與策略準備，使用 `dialogue-practice`。

### `paper-survey` 可以只靠論文標題分析嗎？

不行。至少要提供論文、預印本、PDF 或完整文字。只有標題或摘要時，最多只能做材料範圍內的暫定研究地圖，不能補寫缺失的方法與結果。

## 目錄結構

```text
daily-skills/
├── dialogue-practice/
│   ├── SKILL.md
│   └── references/
├── ease-inner-conflict/
│   ├── SKILL.md
│   └── references/
├── life-reset-audit/
│   ├── SKILL.md
│   └── references/
├── paper-survey/
│   ├── SKILL.md
│   └── references/
├── reflective-journal/
│   ├── SKILL.md
│   └── references/
├── relational-anxiety-support/
│   ├── SKILL.md
│   └── references/
├── LICENSE
└── README.md
```

各 skill 的詳細參考檔案會依需要載入，包含對話手冊、問題庫、研究分析框架、生命重啟流程與安全邊界等內容。建議先從對應的 `SKILL.md` 開始，再按其中的連結閱讀 `references/`。

## 安全與使用邊界

`reflective-journal`、`ease-inner-conflict`、`relational-anxiety-support` 與部分 `life-reset-audit` 情境涉及情緒、自我理解或關係壓力，但它們不是醫師、心理師或危機支援服務：

- 不提供心理疾病、人格、創傷或依附類型診斷。
- 不提供醫療、藥物或治療判斷。
- 不替你決定是否分手、斷絕關係、離職或做其他重大人生決定。
- 遇到自傷、他傷、暴力、威脅或立即危險，先聯絡當地緊急服務、危機支援、醫療機構或可信任的人。
- 若長期失眠、無法正常生活或情緒持續影響工作與日常，也應考慮尋求合格專業協助。

`paper-survey` 的安全邊界則是證據邊界：它會忠實區分論文裡的主張、實際結果與閱讀分析，不捏造缺失資訊，也不把單一資料集或 benchmark 結果擴大成普遍結論。

## 官方安裝規則與延伸閱讀

平台的 skill discovery 與格式可能隨版本更新。以下是本 README 參考的官方文件：

- [OpenAI：Build skills](https://developers.openai.com/codex/skills/)
- [Claude Code：Extend Claude with skills](https://code.claude.com/docs/en/slash-commands)
- [OpenCode：Agent Skills](https://opencode.ai/docs/skills)

## License

本 repository 的授權條款請參閱 [`LICENSE`](LICENSE)。
