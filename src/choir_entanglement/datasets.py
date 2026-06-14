"""Dataset adapters: map heterogeneous raw corpora to one processed layout.

Each Tier-2 dataset stores per-singer audio under its own naming/dir scheme.
An *adapter* is a pure function ``(raw_root: Path) -> list[PieceManifest]`` that
discovers the per-singer wav/mp3 files and groups them by piece, so that the
existing WP1/WP3/E(t) pipeline can consume any dataset through the single
``data/processed/{dataset}/{piece_id}/{singer}.parquet`` contract.

Adapters were written against the REAL inspected file trees (see
``data/raw/_dataset_inventory.md``), not paper/web descriptions.

Datasets:
- ``dagstuhl``: flat dir, ``DCS_{piece}_{section}_{take}_{singer}_{mic}.wav``,
  canonical mic per singer DYN>HSM>LRX (logic moved verbatim from the
  original ``scripts/wp1_dagstuhl_batch.py`` so outputs stay byte-identical).
- ``esmuc``: flat dir, ``{song}_{setting}_{take}_{track}.wav``; per-singer
  tracks match ``^[SATB][0-9]$``; room mics AB/ORTF excluded; unit = singer.
- ``choralsynth``: ``Dataset/{piece}/voices/*.mp3``; one mp3 per voice part;
  section derived from the part name; unit = voice part.
"""

from __future__ import annotations

import re
from collections import defaultdict
from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path

PROCESSED_ROOT = Path("data/processed")

# --- Dagstuhl (verbatim from the original wp1_dagstuhl_batch) ---
_DAGSTUHL_RE = re.compile(
    r"^DCS_(?P<piece>[A-Z]+)_(?P<section>[A-Za-z]+)_(?P<take>[A-Za-z0-9]+)_"
    r"(?P<singer>[SATB]\d)_(?P<mic>DYN|HSM|LRX)\.wav$"
)
_DAGSTUHL_MIC_PRIORITY = {"DYN": 0, "HSM": 1, "LRX": 2}

# --- ESMUC per-singer track token (S1-5, A1-3, T1-3, B1-2) ---
_ESMUC_SINGER_RE = re.compile(r"^[SATB][0-9]$")

# --- ChoralSynth: map a voice-part name to an SATB section letter ---
_CS_SECTION_BY_PREFIX = {
    "cantus": "S", "soprano": "S", "superius": "S", "discantus": "S",
    "altus": "A", "alto": "A", "contratenor": "A",
    "tenor": "T",
    "bassus": "B", "bass": "B",
}


@dataclass(frozen=True)
class PieceManifest:
    """One analysable piece: a set of per-voice source audio files."""

    dataset: str
    piece_id: str
    singer_wavs: dict[str, Path]  # singer/part id -> source audio path
    unit: str = "singer"  # "singer" (physical) or "part" (synthetic voice)

    @property
    def out_dir(self) -> Path:
        return PROCESSED_ROOT / self.dataset / self.piece_id


def dagstuhl_adapter(raw_root: Path) -> list[PieceManifest]:
    """Group Dagstuhl wavs by (piece, section, take); pick canonical mic per singer."""
    audio_dir = raw_root / "DagstuhlChoirSet_V1.2.3" / "audio_wav_22050_mono"
    if not audio_dir.is_dir():
        # allow raw_root to point straight at the audio dir
        audio_dir = raw_root
    by_take: dict[tuple[str, str, str], dict[str, list[tuple[int, Path]]]] = defaultdict(
        lambda: defaultdict(list)
    )
    for wav in sorted(audio_dir.glob("*.wav")):
        m = _DAGSTUHL_RE.match(wav.name)
        if not m:
            continue
        key = (m["piece"], m["section"], m["take"])
        by_take[key][m["singer"]].append((_DAGSTUHL_MIC_PRIORITY[m["mic"]], wav))
    manifests: list[PieceManifest] = []
    for (piece, section, take), singers in by_take.items():
        canonical = {
            s: min(cands, key=lambda pair: pair[0])[1] for s, cands in singers.items()
        }
        if len(canonical) < 2:
            continue
        manifests.append(
            PieceManifest("dagstuhl", f"{piece}_{section}_{take}", canonical, unit="singer")
        )
    return sorted(manifests, key=lambda mf: mf.piece_id)


def esmuc_adapter(raw_root: Path) -> list[PieceManifest]:
    """Group ESMUC wavs by {song}_{setting}_{take}; keep per-singer tracks only."""
    by_piece: dict[str, dict[str, Path]] = defaultdict(dict)
    for wav in sorted(raw_root.glob("*.wav")):
        parts = wav.stem.split("_")
        track = parts[-1]
        if not _ESMUC_SINGER_RE.match(track):
            continue  # skip AB / ORTF / mixed room mics and malformed names
        piece_id = "_".join(parts[:-1])
        # first occurrence wins; ESMUC has one wav per (piece, singer)
        by_piece[piece_id].setdefault(track, wav)
    manifests = [
        PieceManifest("esmuc", pid, singers, unit="singer")
        for pid, singers in by_piece.items()
        if len(singers) >= 2
    ]
    return sorted(manifests, key=lambda mf: mf.piece_id)


def _choralsynth_section(voice_name: str) -> str:
    """Map a ChoralSynth voice filename stem to an SATB section letter."""
    first = re.split(r"[ _\-]", voice_name.strip())[0].lower()
    return _CS_SECTION_BY_PREFIX.get(first, first[:1].upper() or "X")


def choralsynth_adapter(raw_root: Path) -> list[PieceManifest]:
    """One manifest per ChoralSynth piece; per-voice mp3 mapped to S/A/T/B ids."""
    dataset_dir = raw_root / "Dataset"
    if not dataset_dir.is_dir():
        dataset_dir = raw_root
    manifests: list[PieceManifest] = []
    for piece_dir in sorted(p for p in dataset_dir.iterdir() if p.is_dir()):
        voices = sorted((piece_dir / "voices").glob("*.mp3"))
        if len(voices) < 2:
            continue
        section_counts: dict[str, int] = defaultdict(int)
        singer_wavs: dict[str, Path] = {}
        for mp3 in voices:
            section = _choralsynth_section(mp3.stem)
            section_counts[section] += 1
            singer_wavs[f"{section}{section_counts[section]}"] = mp3
        manifests.append(
            PieceManifest("choralsynth", piece_dir.name, singer_wavs, unit="part")
        )
    return manifests


Adapter = Callable[[Path], list[PieceManifest]]

ADAPTERS: dict[str, Adapter] = {
    "dagstuhl": dagstuhl_adapter,
    "esmuc": esmuc_adapter,
    "choralsynth": choralsynth_adapter,
}

DEFAULT_RAW_ROOTS: dict[str, Path] = {
    "dagstuhl": Path("data/raw/dagstuhl"),
    "esmuc": Path("data/raw/esmuc"),
    "choralsynth": Path("data/raw/choralsynth"),
}


def build_manifests(dataset: str, raw_root: Path | None = None) -> list[PieceManifest]:
    """Dispatch to the registered adapter; fail fast on an unknown dataset."""
    if dataset not in ADAPTERS:
        raise ValueError(f"unknown dataset {dataset!r}; known: {sorted(ADAPTERS)}")
    root = raw_root if raw_root is not None else DEFAULT_RAW_ROOTS[dataset]
    return ADAPTERS[dataset](root)
