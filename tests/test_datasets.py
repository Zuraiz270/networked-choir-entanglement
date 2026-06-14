"""Tests for the dataset adapters (synthetic trees; no audio decoded)."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from choir_entanglement.datasets import (
    ADAPTERS,
    PROCESSED_ROOT,
    build_manifests,
    choralsynth_adapter,
    dagstuhl_adapter,
    esmuc_adapter,
)


def _touch(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(b"")


def test_dagstuhl_adapter_groups_by_take_and_picks_canonical_mic(tmp_path: Path) -> None:
    audio = tmp_path / "DagstuhlChoirSet_V1.2.3" / "audio_wav_22050_mono"
    # one singer with all three mics; another with only LRX
    for mic in ("DYN", "HSM", "LRX"):
        _touch(audio / f"DCS_LI_QuartetA_Take02_S2_{mic}.wav")
    _touch(audio / "DCS_LI_QuartetA_Take02_A1_LRX.wav")
    manifests = dagstuhl_adapter(tmp_path)
    assert len(manifests) == 1
    mf = manifests[0]
    assert mf.piece_id == "LI_QuartetA_Take02"
    assert mf.unit == "singer"
    assert mf.singer_wavs["S2"].name.endswith("S2_DYN.wav")  # DYN beats HSM/LRX
    assert mf.singer_wavs["A1"].name.endswith("A1_LRX.wav")


def test_dagstuhl_adapter_skips_solos(tmp_path: Path) -> None:
    audio = tmp_path / "DagstuhlChoirSet_V1.2.3" / "audio_wav_22050_mono"
    _touch(audio / "DCS_LI_Solo_Take01_S1_DYN.wav")  # only one singer
    assert dagstuhl_adapter(tmp_path) == []


def test_esmuc_adapter_groups_and_excludes_room_mics(tmp_path: Path) -> None:
    for track in ("S1", "S2", "A1", "T1", "B1", "AB", "ORTF"):
        _touch(tmp_path / f"DG_FT_take1_{track}.wav")
    # malformed name must not crash or count
    _touch(tmp_path / "DG_FT_take1S1.wav")
    manifests = esmuc_adapter(tmp_path)
    assert len(manifests) == 1
    mf = manifests[0]
    assert mf.piece_id == "DG_FT_take1"
    assert set(mf.singer_wavs) == {"S1", "S2", "A1", "T1", "B1"}  # AB/ORTF excluded
    assert "AB" not in mf.singer_wavs and "ORTF" not in mf.singer_wavs


def test_choralsynth_adapter_maps_parts_to_satb(tmp_path: Path) -> None:
    piece = tmp_path / "Dataset" / "08_Anima_nostra"
    for voice in ("CANTUS", "ALTUS", "TENOR I", "TENOR II", "BASSUS"):
        _touch(piece / "voices" / f"{voice}.mp3")
    (piece / "info.json").write_text(json.dumps({"parts": []}))
    manifests = choralsynth_adapter(tmp_path)
    assert len(manifests) == 1
    mf = manifests[0]
    assert mf.unit == "part"
    # Cantus->S, Altus->A, Tenor I/II->T1/T2, Bassus->B
    assert set(mf.singer_wavs) == {"S1", "A1", "T1", "T2", "B1"}


def test_piece_manifest_out_dir_layout(tmp_path: Path) -> None:
    audio = tmp_path / "DagstuhlChoirSet_V1.2.3" / "audio_wav_22050_mono"
    for s in ("S1", "S2"):
        _touch(audio / f"DCS_LI_QuartetA_Take01_{s}_DYN.wav")
    mf = dagstuhl_adapter(tmp_path)[0]
    assert mf.out_dir == PROCESSED_ROOT / "dagstuhl" / "LI_QuartetA_Take01"


def test_build_manifests_unknown_dataset_raises() -> None:
    with pytest.raises(ValueError, match="unknown dataset"):
        build_manifests("nonexistent", Path("."))


def test_all_adapters_registered() -> None:
    assert set(ADAPTERS) == {"dagstuhl", "esmuc", "choralsynth"}
