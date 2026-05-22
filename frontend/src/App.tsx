import { useEffect, useState } from "react";
import VideoPanel from "./components/VideoPanel";
import GraphPanel from "./components/GraphPanel";
import TimelinePanel from "./components/TimelinePanel";
import MetadataPanel from "./components/MetadataPanel";
import type { VideoMeta } from "./types";

export default function App() {
  const [videos, setVideos] = useState<VideoMeta[]>([]);
  const [selected, setSelected] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    fetch("/api/videos")
      .then((r) => (r.ok ? r.json() : Promise.reject(r.statusText)))
      .then((data: VideoMeta[]) => {
        setVideos(data);
        if (data.length > 0) setSelected(data[0].video_id);
      })
      .catch((e) => setError(String(e)));
  }, []);

  const currentMeta = videos.find((v) => v.video_id === selected) ?? null;

  return (
    <div className="flex h-full flex-col gap-3 bg-slate-900 p-3 text-slate-100">
      <header className="flex items-center justify-between rounded bg-slate-800 px-4 py-2">
        <h1 className="text-lg font-semibold">Choir Entanglement Dashboard</h1>
        <div className="flex items-center gap-2">
          <label className="text-sm text-slate-400">Video</label>
          <select
            className="rounded bg-slate-700 px-2 py-1 text-sm"
            value={selected ?? ""}
            onChange={(e) => setSelected(e.target.value)}
          >
            {videos.map((v) => (
              <option key={v.video_id} value={v.video_id}>
                {v.video_id}
              </option>
            ))}
          </select>
        </div>
      </header>

      {error && (
        <div className="rounded bg-red-900/50 px-3 py-2 text-sm">
          Backend unreachable: {error}. Run{" "}
          <code className="rounded bg-slate-800 px-1">
            uv run uvicorn choir_entanglement.dashboard.app:app --port 8000
          </code>
          .
        </div>
      )}

      <div className="grid flex-1 grid-cols-2 gap-3">
        <VideoPanel videoId={selected} />
        <GraphPanel videoId={selected} />
      </div>

      <TimelinePanel videoId={selected} />
      <MetadataPanel meta={currentMeta} />
    </div>
  );
}
