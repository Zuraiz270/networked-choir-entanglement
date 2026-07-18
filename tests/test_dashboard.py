from __future__ import annotations

from pathlib import Path

import pandas as pd
import pytest

from choir_entanglement.dashboard import app as dashboard_app


def test_dashboard_uses_published_envelope_only_entanglement(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    take_dir = tmp_path / "piece"
    take_dir.mkdir()
    (take_dir / "soprano.parquet").touch()
    captured: dict[str, object] = {}

    def fake_compute_entanglement(audio: object, gexf: object, **kwargs: object) -> pd.DataFrame:
        captured.update(kwargs)
        return pd.DataFrame(
            {"time_sec": [0.0], "A": [0.1], "V": [float("nan")], "N": [0.2], "E": [0.15]}
        )

    monkeypatch.setattr(dashboard_app, "DAGSTUHL_ROOT", tmp_path)
    monkeypatch.setattr(dashboard_app, "compute_entanglement", fake_compute_entanglement)
    dashboard_app._entanglement_cached.cache_clear()

    dashboard_app._entanglement_cached("piece")

    assert captured["include_onsets"] is False
