interface Props {
  videoId: string | null;
}

export default function VideoPanel({ videoId }: Props) {
  return (
    <div className="flex flex-col rounded bg-slate-800 p-3">
      <h2 className="mb-2 text-sm font-semibold text-slate-300">
        Video playback (pose overlay placeholder)
      </h2>
      <div className="flex flex-1 items-center justify-center rounded border border-dashed border-slate-600 bg-slate-900 text-slate-500">
        {videoId ? (
          <div className="text-center">
            <div className="text-xs uppercase tracking-wide">video_id</div>
            <div className="mt-1 font-mono text-lg">{videoId}</div>
            <div className="mt-2 text-xs">
              HTML5 &lt;video&gt; + D3 skeleton overlay land in WP4 sub-plan
            </div>
          </div>
        ) : (
          <div>Loading…</div>
        )}
      </div>
    </div>
  );
}
