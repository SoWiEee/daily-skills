# open-slide Adapter

專案已安裝 open-slide 時優先使用，但教學架構與 Storyboard 維持 renderer-independent。

## 預期能力

- 固定 1920×1080 Canvas
- 任意 React Component
- Presenter Notes
- 可共用 Grammar Component
- Diagram 優先使用 inline SVG / React SVG

## 建議結構

```text
slides/<deck>/
  index.tsx
  components/
    SlideFrame.tsx
    SectionDivider.tsx
    Comparison.tsx
    Flow.tsx
    Architecture.tsx
    CodeWalkthrough.tsx
    Citation.tsx
  diagrams/
  data/
  manuscript/
  storyboard/
```

不要建立一個萬用 `CardGrid` 然後套滿整份 Deck。

Design Token 集中管理。open-slide 專案已有 Theme System 時，把 Design Lock 映射進現有 Theme，不另建一套互相衝突的 Token。
