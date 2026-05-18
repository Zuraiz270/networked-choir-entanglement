"""Per-singer audio feature extraction for WP1.

Input: single-voice wav file (one microphone, one singer).
Output: parquet with per-frame F0, voicing, RMS, onset flags.

Schema frozen at WP1 — downstream WPs (network, dashboard) read this contract.
"""

from __future__ import annotations

import datetime as dt
from dataclasses import dataclass
from pathlib import Path

import librosa
import numpy as np
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

VOCAL_FMIN_HZ = 65.0
VOCAL_FMAX_HZ = 1000.0
SAMPLE_RATE_HZ = 22050
HOP_LENGTH_SAMPLES = 512
FRAME_LENGTH_SAMPLES = 2048


@dataclass(frozen=True)
class FeatureFrame:
    """One row of the per-singer feature parquet."""

    time_sec: float
    f0_hz: float
    voiced: bool
    voiced_prob: float
    rms: float
    onset: bool


def extract_features(wav_path: Path) -> pd.DataFrame:
    """Run pyin + RMS + onset detection on a single-voice wav. Return per-frame DataFrame."""
    y, sr = librosa.load(str(wav_path), sr=SAMPLE_RATE_HZ, mono=True)
    f0, voiced, voiced_prob = librosa.pyin(
        y,
        fmin=VOCAL_FMIN_HZ,
        fmax=VOCAL_FMAX_HZ,
        sr=sr,
        hop_length=HOP_LENGTH_SAMPLES,
        frame_length=FRAME_LENGTH_SAMPLES,
    )
    rms = librosa.feature.rms(
        y=y, frame_length=FRAME_LENGTH_SAMPLES, hop_length=HOP_LENGTH_SAMPLES
    )[0]
    onset_frames = librosa.onset.onset_detect(
        y=y, sr=sr, hop_length=HOP_LENGTH_SAMPLES, units="frames"
    )

    n_frames = len(f0)
    times = librosa.frames_to_time(np.arange(n_frames), sr=sr, hop_length=HOP_LENGTH_SAMPLES)
    onset_mask = np.zeros(n_frames, dtype=bool)
    onset_mask[onset_frames[onset_frames < n_frames]] = True

    return pd.DataFrame(
        {
            "time_sec": times.astype("float64"),
            "f0_hz": np.where(voiced, f0, np.nan).astype("float64"),
            "voiced": voiced.astype("bool"),
            "voiced_prob": voiced_prob.astype("float64"),
            "rms": rms[:n_frames].astype("float64"),
            "onset": onset_mask,
        }
    )


def write_parquet(df: pd.DataFrame, output_path: Path, source_wav: Path) -> None:
    """Write the feature DataFrame to parquet with provenance metadata."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    table = pa.Table.from_pandas(df, preserve_index=False)
    metadata = {
        b"source_wav": str(source_wav).encode(),
        b"sample_rate": str(SAMPLE_RATE_HZ).encode(),
        b"hop_length": str(HOP_LENGTH_SAMPLES).encode(),
        b"frame_length": str(FRAME_LENGTH_SAMPLES).encode(),
        b"librosa_version": str(getattr(librosa, "__version__", "unknown")).encode(),
        b"extraction_date": dt.datetime.now(dt.UTC).isoformat().encode(),
    }
    table = table.replace_schema_metadata({**(table.schema.metadata or {}), **metadata})
    pq.write_table(table, output_path)


def extract_to_parquet(wav_path: Path, output_path: Path) -> pd.DataFrame:
    """Convenience: extract features and write parquet in one call. Return the DataFrame."""
    df = extract_features(wav_path)
    write_parquet(df, output_path, wav_path)
    return df


def main() -> None:
    """CLI: python -m choir_entanglement.audio.pipeline INPUT.wav OUTPUT.parquet"""
    import argparse

    parser = argparse.ArgumentParser(description="Extract WP1 audio features to parquet.")
    parser.add_argument("input_wav", type=Path)
    parser.add_argument("output_parquet", type=Path)
    args = parser.parse_args()

    df = extract_to_parquet(args.input_wav, args.output_parquet)
    print(f"Wrote {len(df)} frames to {args.output_parquet}")
    print(f"  voiced fraction: {df['voiced'].mean():.2%}")
    print(f"  onset count: {int(df['onset'].sum())}")
    print(f"  duration: {df['time_sec'].iloc[-1]:.2f} s")


if __name__ == "__main__":
    main()
