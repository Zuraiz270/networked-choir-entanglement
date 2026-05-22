import { useEffect, useRef, useState } from "react";
import Plotly from "plotly.js-dist-min";
import type { EntanglementResponse } from "../types";

interface Props {
  videoId: string | null;
}

const SERIES_COLOR: Record<string, string> = {
  A: "#1f77b4", V: "#ff7f0e", N: "#2ca02c", E: "#d62728",
};

export default function TimelinePanel({ videoId }: Props) {
  const divRef = useRef<HTMLDivElement | null>(null);
  const [data, setData] = useState<EntanglementResponse | null>(null);

  useEffect(() => {
    if (!videoId) return;
    fetch(`/api/entanglement/${videoId}`)
      .then((r) => r.json())
      .then((d: EntanglementResponse) => setData(d))
      .catch(() => setData(null));
  }, [videoId]);

  useEffect(() => {
    if (!data || !divRef.current) return;
    const traces = (["A", "V", "N", "E"] as const).map((key) => ({
      x: data.series.time_sec,
      y: data.series[key],
      name: `${key}(t)`,
      mode: "lines" as const,
      line: { color: SERIES_COLOR[key], width: key === "E" ? 2.5 : 1.2 },
    }));
    Plotly.react(
      divRef.current,
      traces,
      {
        margin: { l: 40, r: 10, t: 30, b: 35 },
        paper_bgcolor: "#1e293b",
        plot_bgcolor: "#0f172a",
        font: { color: "#e2e8f0", size: 11 },
        xaxis: { title: { text: "Time (s)" }, gridcolor: "#334155" },
        yaxis: { title: { text: "Coupling / coherence" }, gridcolor: "#334155" },
        legend: { orientation: "h", y: 1.15 },
        title: { text: `E(t) timeline · ${data.video_id} (mock data)`, font: { size: 12 } },
      },
      { responsive: true, displayModeBar: false },
    );
  }, [data]);

  return (
    <div className="flex h-64 flex-col rounded bg-slate-800 p-3">
      <div ref={divRef} className="flex-1" />
    </div>
  );
}
