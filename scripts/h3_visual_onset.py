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
import pandas as pd

from choir_entanglement.audio.pipeline import HOP_LENGTH_SAMPLES, SAMPLE_RATE_HZ

GRID_HZ = 10.0
MAX_LAG_S = 2.0
N_SHUFFLES = 1000
AUDIO_WINDOW_S = 90.0
MOTION_COLUMNS = ("head_sway", "trunk_lean", "shoulder_rise")
MIN_VALID_PAIRS = 10

POSE_SUMMARY = Path("data/processed/tier1/_pose_summary.csv")
RAW_DIR = Path("data/raw/tier1")
PROCESSED_DIR = Path("data/processed/tier1")
OUT_CSV = PROCESSED_DIR / "_h3_visual_onset.csv"
FIGURE_OUT = Path("data/figures/h3_visual_onset.png")


def _zscore(x: np.ndarray) -> np.ndarray:
    sd = np.nanstd(x)
    if not np.isfinite(sd) or sd == 0:
        return np.zeros_like(x)
    return (x - np.nanmean(x)) / sd


def visual_motion_signal(
    pose: pd.DataFrame, grid_hz: float = GRID_HZ
) -> tuple[np.ndarray, np.ndarray]:
    """Motion-energy signal on a uniform grid from pose-derived features.

    Per singer stream: sum of z-scored |Δ| of the derived columns (sway +
    breathing proxies), linearly interpolated onto the grid; mean across
    streams. Frames where every component is NaN stay NaN.
    """
    t0 = float(pose["time_sec"].min())
    t1 = float(pose["time_sec"].max())
    grid = np.arange(t0, t1, 1.0 / grid_hz)
    per_stream: list[np.ndarray] = []
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


def audio_onset_envelope(y: np.ndarray, times_grid: np.ndarray) -> np.ndarray:
    """Librosa onset-strength envelope resampled onto ``times_grid``.

    Grid points outside the audio's time range become NaN and are dropped
    pairwise in the correlation.
    """
    env = librosa.onset.onset_strength(
        y=y, sr=SAMPLE_RATE_HZ, hop_length=HOP_LENGTH_SAMPLES
    )
    t_env = librosa.frames_to_time(
        np.arange(len(env)), sr=SAMPLE_RATE_HZ, hop_length=HOP_LENGTH_SAMPLES
    )
    return np.interp(times_grid, t_env, env, left=np.nan, right=np.nan)


def max_lag_correlation(
    audio_env: np.ndarray,
    visual_env: np.ndarray,
    grid_hz: float = GRID_HZ,
    max_lag_s: float = MAX_LAG_S,
) -> tuple[float, float]:
    """Max Pearson r over lags in ±``max_lag_s``; positive lag = visual leads.

    At lag k > 0 the audio sample at t+k is paired with the visual sample at t,
    so a positive best lag means the visual gesture anticipates the sung onset.
    NaN pairs are dropped per lag; lags with < MIN_VALID_PAIRS valid pairs skip.
    """
    a = np.asarray(audio_env, dtype=float)
    v = np.asarray(visual_env, dtype=float)
    n = min(len(a), len(v))
    a, v = a[:n], v[:n]
    max_shift = int(round(max_lag_s * grid_hz))
    best_r, best_lag = -np.inf, 0.0
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
        if r > best_r:
            best_r, best_lag = r, k / grid_hz
    return best_r, best_lag


def circular_null_p(
    audio_env: np.ndarray,
    visual_env: np.ndarray,
    grid_hz: float = GRID_HZ,
    max_lag_s: float = MAX_LAG_S,
    n_shuffles: int = N_SHUFFLES,
    seed: int = 0,
) -> float:
    """Empirical p for the max-lag r under circular shifts of the visual signal.

    Shift offsets follow the project null convention (rng.integers(2, n-2),
    preserving within-stream autocorrelation). Each null draw undergoes the
    SAME max-over-lags search as the observed statistic, so lag selection
    cannot inflate significance. p = (1 + exceedances) / (1 + n_shuffles).
    """
    r_obs, _ = max_lag_correlation(audio_env, visual_env, grid_hz, max_lag_s)
    v = np.asarray(visual_env, dtype=float)
    n = len(v)
    rng = np.random.default_rng(seed)
    exceed = 0
    for _ in range(n_shuffles):
        shift = int(rng.integers(2, n - 2))
        r_null, _ = max_lag_correlation(audio_env, np.roll(v, shift), grid_hz, max_lag_s)
        if r_null >= r_obs:
            exceed += 1
    return (1 + exceed) / (1 + n_shuffles)


def _load_mp4_audio(mp4: Path, max_seconds: float = AUDIO_WINDOW_S) -> np.ndarray:
    """Decode the first ``max_seconds`` of an MP4's audio to mono 22050 Hz."""
    import imageio_ffmpeg

    exe = imageio_ffmpeg.get_ffmpeg_exe()
    with tempfile.TemporaryDirectory() as td:
        wav = Path(td) / "audio.wav"
        cmd = [
            exe, "-y", "-v", "error",
            "-i", str(mp4),
            "-t", str(max_seconds),
            "-ac", "1",
            "-ar", str(SAMPLE_RATE_HZ),
            str(wav),
        ]
        subprocess.run(cmd, check=True, capture_output=True)
        y, _ = librosa.load(str(wav), sr=SAMPLE_RATE_HZ, mono=True)
    return y
