"""Smoke test for WP1 audio pipeline using synthesized sine waves.

Validates: feature schema, voicing detection, F0 accuracy, parquet round-trip,
and pairwise coupling lag detection. No external data required.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pyarrow.parquet as pq
import pytest
import soundfile as sf

from choir_entanglement.audio.coupling import (
    compute_pairwise_coupling,
    load_feature_parquet,
)
from choir_entanglement.audio.pipeline import (
    SAMPLE_RATE_HZ,
    extract_features,
    extract_to_parquet,
)

EXPECTED_COLUMNS = {"time_sec", "f0_hz", "voiced", "voiced_prob", "rms", "onset"}
TEST_F0_HZ = 220.0
TEST_DURATION_SEC = 5.0


def _synth_sine_wav(
    path: Path,
    freq_hz: float,
    duration_sec: float,
    delay_sec: float = 0.0,
    freq_end_hz: float | None = None,
) -> None:
    """Write a sine (or glissando) wav with optional leading silence."""
    n_silence = int(delay_sec * SAMPLE_RATE_HZ)
    n_tone = int(duration_sec * SAMPLE_RATE_HZ)
    t = np.arange(n_tone) / SAMPLE_RATE_HZ
    envelope = 0.5 * (1 - np.cos(2 * np.pi * 1 * t))  # 1 Hz AM creates onsets without aliasing test lag
    if freq_end_hz is None:
        phase = 2 * np.pi * freq_hz * t
    else:
        inst_freq = freq_hz + (freq_end_hz - freq_hz) * (t / duration_sec)
        phase = 2 * np.pi * np.cumsum(inst_freq) / SAMPLE_RATE_HZ
    tone = 0.5 * envelope * np.sin(phase)
    audio = np.concatenate([np.zeros(n_silence, dtype=np.float32), tone.astype(np.float32)])
    sf.write(str(path), audio, SAMPLE_RATE_HZ)


def test_extract_features_schema_and_voicing(tmp_path: Path) -> None:
    wav = tmp_path / "tone.wav"
    _synth_sine_wav(wav, TEST_F0_HZ, TEST_DURATION_SEC)

    df = extract_features(wav)

    assert set(df.columns) == EXPECTED_COLUMNS
    assert len(df) > 100
    assert df["voiced"].mean() > 0.5, "Sine wave should be detected as voiced for most frames"
    voiced_f0 = df.loc[df["voiced"], "f0_hz"].median()
    assert abs(voiced_f0 - TEST_F0_HZ) < 5.0, f"Expected ~{TEST_F0_HZ} Hz, got {voiced_f0}"
    assert df["onset"].sum() > 0, "Modulated sine should produce at least one onset"


def test_parquet_round_trip(tmp_path: Path) -> None:
    wav = tmp_path / "tone.wav"
    parquet = tmp_path / "features.parquet"
    _synth_sine_wav(wav, TEST_F0_HZ, TEST_DURATION_SEC)

    df_written = extract_to_parquet(wav, parquet)
    df_read = load_feature_parquet(parquet)

    assert df_read.equals(df_written)
    metadata = pq.read_metadata(parquet).schema.to_arrow_schema().metadata
    assert b"source_wav" in metadata
    assert b"librosa_version" in metadata


def test_pairwise_coupling_detects_known_lag(tmp_path: Path) -> None:
    wav_a = tmp_path / "singer_a.wav"
    wav_b = tmp_path / "singer_b.wav"
    known_lag_sec = 0.2
    long_duration_sec = 12.0

    _synth_sine_wav(wav_a, 220.0, long_duration_sec, delay_sec=0.0, freq_end_hz=440.0)
    _synth_sine_wav(wav_b, 220.0, long_duration_sec, delay_sec=known_lag_sec, freq_end_hz=440.0)

    df_a = extract_features(wav_a)
    df_b = extract_features(wav_b)
    result = compute_pairwise_coupling(df_a, df_b, max_lag_sec=1.0, signal="f0_hz")

    assert abs(result.peak_correlation) > 0.5
    assert abs(abs(result.peak_lag_sec) - known_lag_sec) < 0.15, (
        f"Expected lag near {known_lag_sec}s, got {result.peak_lag_sec}s"
    )
    assert result.overlap_sec > 0


def test_coupling_raises_on_no_overlap(tmp_path: Path) -> None:
    df_a = extract_features(_make_tiny_wav(tmp_path / "a.wav", duration_sec=0.05))
    df_b = extract_features(_make_tiny_wav(tmp_path / "b.wav", duration_sec=0.05))

    with pytest.raises(ValueError, match="Insufficient overlap"):
        compute_pairwise_coupling(df_a, df_b)


def _make_tiny_wav(path: Path, duration_sec: float) -> Path:
    _synth_sine_wav(path, TEST_F0_HZ, duration_sec)
    return path
