import { useEffect, useRef, useState } from "react";
import type { PoseResponse, VideoMetaFull } from "../types";

interface Props {
  videoId: string | null;
  meta: VideoMetaFull | null;
}

// MediaPipe pose keypoint coordinates are normalised to [0,1] in image space.
const NORM = 1.0;

export default function VideoPanel({ videoId, meta }: Props) {
  const videoRef = useRef<HTMLVideoElement | null>(null);
  const svgRef = useRef<SVGSVGElement | null>(null);
  const [pose, setPose] = useState<PoseResponse | null>(null);

  const isVideo = meta?.kind === "video_pose";

  useEffect(() => {
    setPose(null);
    if (!videoId || !isVideo) return;
    fetch(`/api/pose/${videoId}`)
      .then((r) => (r.ok ? r.json() : Promise.reject(r.statusText)))
      .then((d: PoseResponse) => setPose(d))
      .catch(() => setPose(null));
  }, [videoId, isVideo]);

  // Draw the nearest pose frame's keypoints onto the SVG overlay as the video plays.
  useEffect(() => {
    const video = videoRef.current;
    const svg = svgRef.current;
    if (!video || !svg || !pose) return;

    const draw = () => {
      const t = video.currentTime;
      let nearest = pose.frames[0];
      for (const f of pose.frames) {
        if (Math.abs(f.time_sec - t) < Math.abs(nearest.time_sec - t)) nearest = f;
      }
      const w = svg.clientWidth;
      const h = svg.clientHeight;
      const pts: string[] = [];
      const kp = nearest?.keypoints ?? {};
      const names = new Set(
        Object.keys(kp).map((k) => k.replace(/_x$|_y$/, "")),
      );
      for (const name of names) {
        const x = kp[`${name}_x`];
        const y = kp[`${name}_y`];
        if (x == null || y == null) continue;
        pts.push(
          `<circle cx="${(x / NORM) * w}" cy="${(y / NORM) * h}" r="3" fill="#22d3ee" opacity="0.85" />`,
        );
      }
      svg.innerHTML = pts.join("");
      if (!video.paused && !video.ended) requestAnimationFrame(draw);
    };

    const onPlay = () => requestAnimationFrame(draw);
    video.addEventListener("play", onPlay);
    video.addEventListener("seeked", draw);
    video.addEventListener("timeupdate", draw);
    return () => {
      video.removeEventListener("play", onPlay);
      video.removeEventListener("seeked", draw);
      video.removeEventListener("timeupdate", draw);
    };
  }, [pose]);

  return (
    <div className="flex flex-col rounded bg-slate-800 p-3">
      <h2 className="mb-2 text-sm font-semibold text-slate-300">
        Video playback {isVideo ? "(33-keypoint pose overlay)" : ""}
      </h2>
      <div className="relative flex flex-1 items-center justify-center overflow-hidden rounded border border-slate-700 bg-slate-900">
        {videoId && isVideo && meta?.has_video ? (
          <>
            <video
              ref={videoRef}
              src={`/api/video/${videoId}`}
              controls
              className="max-h-full max-w-full"
            />
            <svg
              ref={svgRef}
              className="pointer-events-none absolute inset-0 h-full w-full"
            />
          </>
        ) : (
          <div className="px-4 text-center text-slate-500">
            <div className="font-mono text-lg">{videoId ?? "Loading…"}</div>
            <div className="mt-2 text-xs">
              {meta?.kind === "audio_network"
                ? "Audio + network piece (Dagstuhl): no video. See timeline + influence graph."
                : meta?.has_video
                  ? "Select a Tier-1 video to see the pose overlay."
                  : "Pose data is available, but the MP4 file is missing on this machine."}
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
