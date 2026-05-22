import type { VideoMeta } from "../types";

interface Props {
  meta: VideoMeta | null;
}

export default function MetadataPanel({ meta }: Props) {
  if (!meta) {
    return (
      <div className="rounded bg-slate-800 p-3 text-sm text-slate-400">
        Loading metadata…
      </div>
    );
  }
  return (
    <div className="grid grid-cols-4 gap-3 rounded bg-slate-800 p-3 text-sm">
      <Field label="video_id" value={meta.video_id} mono />
      <Field label="regime" value={meta.regime} />
      <Field label="singers" value={String(meta.n_singers)} />
      <Field label="duration" value={`${meta.duration_s} s`} />
    </div>
  );
}

function Field({
  label, value, mono = false,
}: {
  label: string;
  value: string;
  mono?: boolean;
}) {
  return (
    <div>
      <div className="text-xs uppercase tracking-wide text-slate-400">{label}</div>
      <div className={`mt-1 ${mono ? "font-mono" : ""}`}>{value}</div>
    </div>
  );
}
