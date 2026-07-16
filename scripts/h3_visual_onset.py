"""H3 first visual-onset attempt: audio-visual onset coupling on Tier-1 videos.

For each pose-usable Tier-1 video (quality_pass in _pose_summary.csv), correlates
the ensemble audio onset-strength envelope (from the MP4 audio track) with a
visual motion signal (from the pose parquet's derived sway/breathing columns),
at the best lag inside an anticipatory window, against a circular-shift null.

This is the analysis promised in PROJECT_GUIDE §11 Claim 3 ("pair pose onsets
with audio onsets on the 18 pose-usable Tier-1 videos"). It does NOT test the
H3 ΔR² claim, which stays data-blocked (no corpus piece has per-singer audio
and video together). Design: docs/superpowers/specs/
2026-07-14-h3-final-presentation-design.md.

Data reality (verified 2026-07-14): each pose parquet tracks ONE aggregate
person stream at ~8-10 Hz over the first 60-72 s of the video, so the analysis
window is that first minute and the visual signal is a single motion stream.

Usage:
    uv run python -m scripts.h3_visual_onset
"""

from __future__ import annotations

import subprocess
import tempfile
from pathlib import Path

import librosa
import numpy as np
import numpy.typing as npt
import pandas as pd

from choir_entanglement.audio.pipeline import HOP_LENGTH_SAMPLES, SAMPLE_RATE_HZ

GRID_HZ = 10.0
MAX_LAG_S = 2.0
N_SHUFFLES = 1000
AUDIO_WINDOW_S = 90.0
MOTION_COLUMNS = ("head_sway", "trunk_lean", "shoulder_rise")
MIN_VALID_PAIRS = 10

FloatArray = npt.NDArray[np.float64]

POSE_SUMMARY = Path("data/processed/tier1/_pose_summary.csv")
RAW_DIR = Path("data/raw/tier1")
PROCESSED_DIR = Path("data/processed/tier1")
OUT_CSV = PROCESSED_DIR / "_h3_visual_onset.csv"
FIGURE_OUT = Path("data/figures/h3_visual_onset.png")


def _zscore(x: FloatArray) -> FloatArray:
    sd = np.nanstd(x)
    if not np.isfinite(sd) or sd == 0:
        return np.zeros_like(x)
    return np.asarray((x - np.nanmean(x)) / sd, dtype=np.float64)


def visual_motion_signal(
    pose: pd.DataFrame, grid_hz: float = GRID_HZ
) -> tuple[FloatArray, FloatArray]:
    """Motion-energy signal on a uniform grid from pose-derived features.

    Per singer stream: sum of z-scored |Δ| of the derived columns (sway +
    breathing proxies), linearly interpolated onto the grid; mean across
    streams. Frames where every component is NaN stay NaN.
    """
    t0 = float(pose["time_sec"].min())
    t1 = float(pose["time_sec"].max())
    grid = np.arange(t0, t1, 1.0 / grid_hz)
    per_stream: list[FloatArray] = []
    for _, df in pose.groupby("singer_id"):
        df = df.sort_values("time_sec")
        t = df["time_sec"].to_numpy(dtype=float)
        parts = []
        for col in MOTION_COLUMNS:
            x = df[col].to_numpy(dtype=float)
            d = np.abs(np.diff(x, prepend=x[:1]))
            parts.append(_zscore(d))
        stack = np.vstack(parts)
        motion = np.nansum(stack, axis=0)
        motion[np.all(np.isnan(stack), axis=0)] = np.nan
        valid = np.isfinite(motion)
        if valid.sum() < MIN_VALID_PAIRS:
            continue
        per_stream.append(np.interp(grid, t[valid], motion[valid]))
    if not per_stream:
        return grid, np.full_like(grid, np.nan)
    return grid, np.nanmean(np.vstack(per_stream), axis=0)


def audio_onset_envelope(y: FloatArray, times_grid: FloatArray) -> FloatArray:
    """Librosa onset-strength envelope resampled onto ``times_grid``.

    Grid points outside the audio's time range become NaN and are dropped
    pairwise in the correlation.
    """
    env = librosa.onset.onset_strength(y=y, sr=SAMPLE_RATE_HZ, hop_length=HOP_LENGTH_SAMPLES)
    t_env = librosa.frames_to_time(
        np.arange(len(env)), sr=SAMPLE_RATE_HZ, hop_length=HOP_LENGTH_SAMPLES
    )
    return np.interp(times_grid, t_env, env, left=np.nan, right=np.nan)


def max_lag_correlation(
    audio_env: FloatArray,
    visual_env: FloatArray,
    grid_hz: float = GRID_HZ,
    max_lag_s: float = MAX_LAG_S,
) -> tuple[float, float]:
    """Max Pearson r over lags in ±``max_lag_s``; positive lag = visual leads.

    At lag k > 0 the audio sample at t+k is paired with the visual sample at t,
    so a positive best lag means the visual gesture anticipates the sung onset.
    NaN pairs are dropped per lag; lags with < MIN_VALID_PAIRS valid pairs skip.
    Returns (nan, nan) when no lag yields a defined correlation (e.g. a silent
    audio window makes the envelope constant).
    """
    a = np.asarray(audio_env, dtype=float)
    v = np.asarray(visual_env, dtype=float)
    n = min(len(a), len(v))
    a, v = a[:n], v[:n]
    max_shift = int(round(max_lag_s * grid_hz))
    best: tuple[float, float] | None = None
    for k in range(-max_shift, max_shift + 1):
        if k >= 0:
            a_seg, v_seg = a[k:], v[: n - k]
        else:
            a_seg, v_seg = a[:k], v[-k:]
        mask = np.isfinite(a_seg) & np.isfinite(v_seg)
        if mask.sum() < MIN_VALID_PAIRS:
            continue
        x, y = a_seg[mask], v_seg[mask]
        sx, sy = x.std(), y.std()
        if sx == 0 or sy == 0:
            continue
        r = float(np.mean((x - x.mean()) / sx * (y - y.mean()) / sy))
        if best is None or r > best[0]:
            best = (r, k / grid_hz)
    if best is None:
        return float("nan"), float("nan")
    return best


def circular_null_rs(
    audio_env: FloatArray,
    visual_env: FloatArray,
    grid_hz: float = GRID_HZ,
    max_lag_s: float = MAX_LAG_S,
    n_shuffles: int = N_SHUFFLES,
    seed: int = 0,
) -> FloatArray:
    """Null distribution of the max-lag r under circular shifts of the visual signal.

    Shift offsets follow the project null convention (rng.integers(2, n-2),
    preserving within-stream autocorrelation). Each null draw undergoes the
    SAME max-over-lags search as the observed statistic, so lag selection
    cannot inflate significance.
    """
    v = np.asarray(visual_env, dtype=float)
    n = len(v)
    rng = np.random.default_rng(seed)
    rs = np.empty(n_shuffles, dtype=np.float64)
    for i in range(n_shuffles):
        shift = int(rng.integers(2, n - 2))
        rs[i], _ = max_lag_correlation(audio_env, np.roll(v, shift), grid_hz, max_lag_s)
    return rs


def circular_null_p(
    audio_env: FloatArray,
    visual_env: FloatArray,
    grid_hz: float = GRID_HZ,
    max_lag_s: float = MAX_LAG_S,
    n_shuffles: int = N_SHUFFLES,
    seed: int = 0,
) -> float:
    """Empirical p for the max-lag r: (1 + exceedances) / (1 + n_shuffles).

    NaN when the observed statistic is undefined (degenerate input).
    """
    r_obs, _ = max_lag_correlation(audio_env, visual_env, grid_hz, max_lag_s)
    if not np.isfinite(r_obs):
        return float("nan")
    rs = circular_null_rs(audio_env, visual_env, grid_hz, max_lag_s, n_shuffles, seed)
    return float((1 + int(np.nansum(rs >= r_obs))) / (1 + n_shuffles))


def _load_mp4_audio(mp4: Path, max_seconds: float = AUDIO_WINDOW_S) -> FloatArray:
    """Decode the first ``max_seconds`` of an MP4's audio to mono 22050 Hz."""
    import imageio_ffmpeg

    exe = imageio_ffmpeg.get_ffmpeg_exe()
    with tempfile.TemporaryDirectory() as td:
        wav = Path(td) / "audio.wav"
        cmd = [
            exe,
            "-y",
            "-v",
            "error",
            "-i",
            str(mp4),
            "-t",
            str(max_seconds),
            "-ac",
            "1",
            "-ar",
            str(SAMPLE_RATE_HZ),
            str(wav),
        ]
        subprocess.run(cmd, check=True, capture_output=True)
        y, _ = librosa.load(str(wav), sr=SAMPLE_RATE_HZ, mono=True)
    return y


def _figure(results: pd.DataFrame, nulls: dict[str, FloatArray], out: Path) -> None:
    """Observed max-lag r per video against its circular-shift null distribution."""
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    results = results[results.usable_audio].reset_index(drop=True)
    order = results.sort_values("r_obs").reset_index(drop=True)
    fig, ax = plt.subplots(figsize=(9, 7))
    ax.boxplot(
        [nulls[v] for v in order.video_id],
        positions=range(len(order)),
        vert=False,
        widths=0.6,
        showfliers=False,
        medianprops={"color": "#999999"},
        boxprops={"color": "#999999"},
        whiskerprops={"color": "#999999"},
        capprops={"color": "#999999"},
    )
    sig = order.significant.astype(bool)
    ax.scatter(
        order.r_obs[sig],
        np.flatnonzero(sig),
        color="#d62728",
        zorder=3,
        label=f"observed r, p < 0.05 (n={int(sig.sum())})",
    )
    ax.scatter(
        order.r_obs[~sig],
        np.flatnonzero(~sig),
        facecolors="none",
        edgecolors="#d62728",
        zorder=3,
        label=f"observed r, n.s. (n={int((~sig).sum())})",
    )
    ax.set_yticks(range(len(order)))
    ax.set_yticklabels(order.video_id, fontsize=8)
    ax.set_xlabel("Max-lag Pearson r (audio onset envelope vs visual motion)")
    ax.grid(True, alpha=0.3, axis="x")
    ax.legend(fontsize=9, loc="lower right")
    fig.suptitle(
        f"H3 first visual-onset attempt: {len(order)} analyzable of 18 pose-usable "
        "Tier-1 videos\n"
        f"first-minute window, ±{MAX_LAG_S:.0f} s lag search, "
        f"{N_SHUFFLES} circular-shift nulls (grey boxes)",
        fontsize=12,
    )
    fig.tight_layout()
    out.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out, dpi=150, bbox_inches="tight")
    plt.close(fig)


def run() -> None:
    import time

    summary = pd.read_csv(POSE_SUMMARY)
    usable = summary[summary["quality_pass"]].sort_values("video_id").reset_index(drop=True)
    if len(usable) != 18:
        raise SystemExit(f"expected 18 quality-pass videos, found {len(usable)}")

    rows: list[dict[str, object]] = []
    nulls: dict[str, FloatArray] = {}
    for rec in usable.itertuples():
        vid = str(rec.video_id)
        t0 = time.perf_counter()
        pose = pd.read_parquet(PROCESSED_DIR / vid / "pose.parquet")
        grid, motion = visual_motion_signal(pose)
        y = _load_mp4_audio(RAW_DIR / vid / f"{vid}.mp4")
        audio_env = audio_onset_envelope(y, grid)
        # A silent pose window (e.g. VJ3TLIFHBGw: first 90 s digitally silent)
        # makes AV coupling undefined for this video; report it, don't fake it.
        usable_audio = bool(np.nanstd(audio_env) > 0)
        if usable_audio:
            r_obs, best_lag = max_lag_correlation(audio_env, motion)
            null_rs = circular_null_rs(audio_env, motion)
            p = float((1 + int(np.nansum(null_rs >= r_obs))) / (1 + len(null_rs)))
            nulls[vid] = null_rs
        else:
            r_obs = best_lag = p = float("nan")
        rows.append(
            {
                "video_id": vid,
                "singer_count_est": int(rec.singer_count_est),
                "pose_coverage": float(rec.pose_detection_rate),
                "analysis_window_s": round(float(grid[-1] - grid[0]), 1),
                "usable_audio": usable_audio,
                "r_obs": round(r_obs, 4) if usable_audio else r_obs,
                "best_lag_s": round(best_lag, 2) if usable_audio else best_lag,
                "p_null": round(p, 4) if usable_audio else p,
                "significant": bool(usable_audio and p < 0.05),
            }
        )
        note = "" if usable_audio else " [silent audio window, excluded]"
        print(
            f"{vid}: r={r_obs:.3f} lag={best_lag:+.1f}s p={p:.4f} "
            f"({time.perf_counter() - t0:.1f}s){note}"
        )

    results = pd.DataFrame(rows)
    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    results.to_csv(OUT_CSV, index=False)
    _figure(results, nulls, FIGURE_OUT)
    n_sig = int(results.significant.sum())
    n_analyzable = int(results.usable_audio.sum())
    print(
        f"\nWrote {OUT_CSV} ({len(results)} rows; {n_analyzable} analyzable; "
        f"{n_sig}/{n_analyzable} significant)"
    )
    print(f"Wrote {FIGURE_OUT}")


if __name__ == "__main__":
    run()
