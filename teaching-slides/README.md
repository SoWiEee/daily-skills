# Teaching Slides Skill v3

這是一套給 Codex 與其他 Coding Agent 使用的技術教學簡報 Skill。預設用在可課後自讀的課程講義，也能支援現場授課。

## v3 新增內容

v3 把製作流程拉到簡報實作之前，新增完整的需求理解與教學文稿階段：

```text
多輪需求訪談
→ 教學架構
→ 簡報文稿與 Speaker Notes
→ 語意化 Visual Storyboard
→ 4 到 6 張代表性 Demo
→ Design Lock
→ 完整實作
→ Instructional / Visual / Deck QA
```

主要新增：

- `references/discovery-interview.md`：2 到 4 輪需求訪談與停止條件
- `references/teaching-manuscript.md`：renderer-neutral 的逐頁文稿與講稿規格
- `references/prototype-gate.md`：代表性 Demo 選頁與核准流程
- `references/instructional-qa.md`：Learning Goal、Example、Check、Recap 的覆蓋檢查
- `references/anti-ai-style.md`：依使用者提供的「AI 味避用詞庫」改寫成教學簡報可執行規則
- `scripts/ai_tone_lint.py`：檢查長破折號、AI 套話、空泛歸因與常見文風指紋
- `templates/*.yaml`：訪談、教學架構、文稿、Storyboard、Design Lock 與 QA 的中間產物格式

原本 v2 的功能全部保留：

- 27 種 Slide Grammar
- Layout Decision Engine
- Diagram Ontology
- `anchor / dense / breathing` Deck Rhythm
- assertion-style title 原則
- Code、Table、Diagram 使用規則
- Design Drift 控制
- open-slide optional adapter

## 安裝

放進專案內的 Agent Skill：

```bash
mkdir -p .agents/skills
cp -R teaching-slides-skill-v3 .agents/skills/teaching-slides
```

或執行：

```bash
./scripts/install-local.sh
```

## 建議提示詞

```text
請使用 teaching-slides Skill，把 notes/week03.md 做成可課後自讀的技術課程簡報。
先進行需求訪談，不要直接寫完整投影片。
訪談完成後依序產出教學架構、文稿與 Speaker Notes、Visual Storyboard。
我確認後請製作 4 到 6 張代表性 Demo，通過後再完整實作。
如果專案有 open-slide 就使用 open-slide。
```

如果希望 Agent 自主完成：

```text
請使用 teaching-slides Skill 自主完成整份簡報。缺少的資訊可以合理推定，但要把 assumptions 留在 project-brief.yaml，並保留每個階段的中間產物。
```
