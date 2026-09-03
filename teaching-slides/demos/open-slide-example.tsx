// Structural example only. Adapt imports to the open-slide scaffold in the active project.
import React from "react";

const C = {
  bg: "#221C34",
  text: "#F7F4FF",
  soft: "#C8C0D8",
  line: "#4A415F",
  accent: "#FF595A",
  violet: "#8E73FF",
  cyan: "#24C7D9",
};

function SlideShell({ children }: { children: React.ReactNode }) {
  return (
    <section style={{ width: 1920, height: 1080, background: C.bg, color: C.text, padding: "110px 140px", position: "relative" }}>
      {children}
    </section>
  );
}

function FlowNode({ step, title, body, color }: { step: string; title: string; body: string; color: string }) {
  return (
    <div style={{ border: `1px solid ${C.line}`, padding: 36, minHeight: 245 }}>
      <div style={{ fontFamily: "JetBrains Mono, monospace", color, fontWeight: 700 }}>{step}</div>
      <h3 style={{ fontSize: 34, margin: "14px 0" }}>{title}</h3>
      <p style={{ fontSize: 22, lineHeight: 1.5, color: C.soft }}>{body}</p>
    </div>
  );
}

export default function ExampleDeck() {
  return (
    <SlideShell>
      <h1 style={{ fontSize: 56, margin: 0 }}>Scheduler 的兩階段 Mental Model</h1>
      <div style={{ width: 90, height: 6, background: C.accent, marginTop: 18 }} />
      <div style={{ display: "grid", gridTemplateColumns: "1fr 100px 1fr", alignItems: "center", marginTop: 130 }}>
        <FlowNode step="01 / FILTER" title="Feasibility" body="排除不符合硬性限制的候選節點。" color={C.cyan} />
        <div style={{ height: 3, background: C.accent }} />
        <FlowNode step="02 / SCORE" title="Preference" body="在剩餘候選中比較偏好與效用。" color={C.violet} />
      </div>
      <a href="https://kubernetes.io/docs/concepts/scheduling-eviction/kube-scheduler/" style={{ position: "absolute", bottom: 48, left: 140, color: "#8E849F", fontSize: 18 }}>
        Source: Kubernetes Scheduler documentation
      </a>
    </SlideShell>
  );
}
