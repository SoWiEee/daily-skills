# Generic HTML / React Adapter

open-slide 不可用時使用。

- Slide Authoring Size 固定 1920×1080
- Canvas 等比例縮放到 Viewport
- Slide 內不使用 Responsive Reflow
- 使用 Semantic HTML + CSS + SVG
- Multi-page Demo 至少支援方向鍵切換
- 全 Deck 共用同一份 Design Token
- 保留 `data-slide-type`、`data-rhythm` 等 Metadata
- Speaker Notes 可以存成 JSON、HTML data attribute 或獨立 Markdown
