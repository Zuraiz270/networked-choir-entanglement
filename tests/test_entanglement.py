"""Smoke tests for the E(t) integration module."""

from __future__ import annotations

from pathlib import Path

import networkx as nx
import numpy as np
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import pytest

from choir_entanglement.entanglement import (
    compute_entanglement,
    compute_entanglement_null,
)

FRAME_RATE_HZ = 43.0  # matches the WP1 pipeline (sr=22050, hop=512)


def _write_audio_parquet(
    path: Path, time_sec: np.ndarray, rms: np.ndarray
) -> Path:
    df = pd.DataFrame({"time_sec": time_sec, "rms": rms})
    pq.write_table(pa.Table.from_pandas(df, preserve_index=False), path)
    return path


def _coupled_audio(tmp_path: Path, n_singers: int = 4, duration_sec: float = 30.0) -> dict[str, Path]:
    """Singers driven by a shared RMS envelope plus per-singer noise."""
    tmp_path.mkdir(parents=True, exist_ok=True)
    n = int(duration_sec * FRAME_RATE_HZ)
    time_sec = np.arange(n, dtype=np.float64) / FRAME_RATE_HZ
    rng = np.random.default_rng(42)
    shared = 0.4 + 0.2 * np.sin(2 * np.pi * 0.5 * time_sec) + 0.05 * rng.normal(size=n)
    parquets: dict[str, Path] = {}
    for i in range(n_singers):
        rms = shared + 0.05 * rng.normal(size=n)
        parquets[f"S{i}"] = _write_audio_parquet(tmp_path / f"S{i}.parquet", time_sec, rms)
    return parquets


def _independent_audio(tmp_path: Path, n_singers: int = 4, duration_sec: float = 30.0) -> dict[str, Path]:
    tmp_path.mkdir(parents=True, exist_ok=True)
    n = int(duration_sec * FRAME_RATE_HZ)
    time_sec = np.arange(n, dtype=np.float64) / FRAME_RATE_HZ
    rng = np.random.default_rng(7)
    parquets: dict[str, Path] = {}
    for i in range(n_singers):
        rms = 0.4 + 0.05 * rng.normal(size=n)
        parquets[f"S{i}"] = _write_audio_parquet(tmp_path / f"S{i}.parquet", time_sec, rms)
    return parquets


def _network_gexf(tmp_path: Path, density: float) -> Path:
    """Build a 4-node digraph with the requested density and write to GEXF."""
    g = nx.DiGraph()
    nodes = ["S0", "S1", "S2", "S3"]
    g.add_nodes_from(nodes)
    target = round(density * len(nodes) * (len(nodes) - 1))
    pairs = [(a, b) for a in nodes for b in nodes if a != b][:target]
    for a, b in pairs:
        g.add_edge(a, b, weight=1.0)
    path = tmp_path / "graph.gexf"
    nx.write_gexf(g, path)
    return path


def test_coupled_audio_yields_high_E(tmp_path: Path) -> None:
    audio = _coupled_audio(tmp_path)
    gexf = _network_gexf(tmp_path, density=0.83)
    df = compute_entanglement(audio, gexf, window_sec=5.0, step_sec=0.5)

    assert {"time_sec", "A", "V", "N", "E", "n_available"} == set(df.columns)
    assert df["V"].isna().all(), "V should be NaN when no video provided"
    assert df["N"].notna().all()
    assert df["A"].notna().mean() > 0.8, "audio coupling should compute on most windows"
    assert df["E"].mean() > 0.4, f"expected high mean E, got {df['E'].mean()}"


def test_independent_audio_yields_low_E_relative_to_coupled(tmp_path: Path) -> None:
    coupled_audio = _coupled_audio(tmp_path / "coupled")
    indep_audio = _independent_audio(tmp_path / "indep")
    gexf = _network_gexf(tmp_path, density=0.5)

    e_coupled = compute_entanglement(
        coupled_audio, gexf, window_sec=5.0, step_sec=0.5
    )["A"]
    e_indep = compute_entanglement(
        indep_audio, gexf, window_sec=5.0, step_sec=0.5
    )["A"]
    assert e_coupled.mean() > e_indep.mean() + 0.1, (
        f"coupled A({e_coupled.mean():.3f}) should exceed independent A({e_indep.mean():.3f})"
    )


def test_missing_signals_reallocate_E_weight(tmp_path: Path) -> None:
    audio = _coupled_audio(tmp_path, n_singers=2)
    df = compute_entanglement(audio, network_gexf=None, video_parquet=None,
                              window_sec=5.0, step_sec=0.5)
    # No N, no V -> E should equal A and n_available should be 1 wherever A is defined
    valid = df.dropna(subset=["A"])
    assert (valid["E"] == valid["A"]).all()
    assert (valid["n_available"] == 1).all()


def test_null_distribution_brackets_observed(tmp_path: Path) -> None:
    audio = _coupled_audio(tmp_path, duration_sec=20.0)
    gexf = _network_gexf(tmp_path, density=0.5)
    observed = compute_entanglement(audio, gexf, window_sec=5.0, step_sec=0.5)["E"].mean()
    null = compute_entanglement_null(
        audio, gexf, window_sec=5.0, step_sec=0.5, n_shuffles=25, seed=0
    )
    assert null.size == 25
    assert np.isfinite(null).all()
    # Coupled audio should exceed the bulk of the null
    p_null = float((null >= observed).mean())
    assert p_null < 0.20, f"observed should beat most of the null, got p_null={p_null}"


def test_duration_too_short_raises(tmp_path: Path) -> None:
    audio = _coupled_audio(tmp_path, duration_sec=4.0)
    gexf = _network_gexf(tmp_path, density=0.5)
    with pytest.raises(ValueError, match="shorter than window"):
        compute_entanglement(audio, gexf, window_sec=10.0)
