#!/usr/bin/env python3
"""Teaching Slides 文稿的輕量 AI 味檢查器。

用法：
    python scripts/ai_tone_lint.py manuscript.yaml

只做可機械偵測的文字警示，不替代人工判斷。
"""
from __future__ import annotations
import re
import sys
from pathlib import Path

BANNED_TERMS = [
    "賦能", "賦予", "深入探討", "深入研究", "凸顯", "突顯", "闡述", "涵蓋",
    "落地", "接軌", "格局", "版圖", "藍圖", "解方", "賦能機制", "增長引擎",
    "不可或缺", "不可磨滅", "不容忽視", "值得注意的是", "重要的是要記住",
    "需要強調的是", "顯而易見的是", "不可否認的是", "綜上所述", "由此可知",
]
VAGUE_ATTRIBUTIONS = ["研究顯示", "研究指出", "專家指出", "許多人認為", "業界普遍認為", "觀察家指出"]
GENERIC_ENDINGS = ["總結來說", "整體來看", "綜合以上", "讓我們一起", "在這個快速變化的時代"]


def main() -> int:
    if len(sys.argv) != 2:
        print("用法: python scripts/ai_tone_lint.py <text-or-yaml-file>")
        return 2
    p = Path(sys.argv[1])
    text = p.read_text(encoding="utf-8")
    issues: list[str] = []

    if "——" in text or "—" in text:
        issues.append("發現長破折號，請改成句號、逗號、冒號或括號。")

    for term in BANNED_TERMS:
        count = text.count(term)
        if count:
            issues.append(f"避用詞「{term}」出現 {count} 次，請確認是否為必要術語或來源原文。")

    for phrase in VAGUE_ATTRIBUTIONS:
        if phrase in text:
            issues.append(f"模糊歸因「{phrase}」需要具體來源。")

    for phrase in GENERIC_ENDINGS:
        if phrase in text:
            issues.append(f"套語「{phrase}」請改成具體內容。")

    emoji = re.findall(r"[🚀📘✨💡🎯🔥✅❌🌟]", text)
    if emoji:
        issues.append(f"發現 {len(emoji)} 個常見裝飾 Emoji，正式教學文稿預設不用。")

    weak = ["可以說", "某種程度上", "一定程度上"]
    for term in weak:
        if text.count(term) >= 2:
            issues.append(f"弱化詞「{term}」重複出現，請改成明確條件或直接判斷。")

    if issues:
        print(f"AI 味檢查：{len(issues)} 個警示")
        for i, issue in enumerate(issues, 1):
            print(f"{i}. {issue}")
        return 1

    print("AI 味檢查：未發現可機械偵測的警示。")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
