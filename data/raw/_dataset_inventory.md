# Tier-2 dataset inventory (verified on download, 2026-06-15)

Everything below was read from the actual extracted files, not from papers or web summaries. Where a web/paper claim was wrong, it is flagged. Checksums in `_dataset_checksums.csv` (both MD5-match upstream Zenodo).

## ESMUC Choir Dataset

- **Zenodo**: DOI `10.5281/zenodo.5848990`, file `EsmucChoirDataset_v1.0.0.zip` (2.34 GB). MD5 matches upstream.
- **License**: CC BY 4.0 (Zenodo metadata).
- **Layout**: flat directory, no subfolders. Filenames `{song}_{setting}_{take}_{track}.{wav|f0|lab}`.
- **Audio**: per-singer mono WAV (README states 44.1 kHz; our pipeline resamples to 22050 via librosa, confirmed loads, e.g. `DG_FT_take1_S1` = 173.2 s, 93% non-silent). Counts: 495 `.wav`, 300 `.f0` (pitch annotations), 276 `.lab` (note labels).
- **CORRECTION to web claim "3 pieces, 12 singers"**: the real tree has **7 song codes** — `DG` (20 groups), `DH1` (4), `DH2` (1), `SC1` (5), `SC2` (4), `SC3` (12), `WU` (2) — across **settings** `FT` (full take), `IS` (individual sections), `SE` (short excerpts), with multiple takes.
- **Per-singer tracks**: `S1-S5`, `A1-A3`, `T1-T3`, `B1-B2`. Non-singer tracks to EXCLUDE: `AB` (room mix), `ORTF` (stereo room pair), and `mixed` infix variants.
- **Analysis-relevant subset**: **48 per-singer multitrack groups**, of which **32 are full-ensemble** (≥4 singers spanning ≥3 sections). The cleanest are the `*_FT_take*` full takes, e.g. `DG_FT_take1..4` = 12 singers each (S1-4, A1-3, T1-3, B1-2). For the Tier-3 grid we select FT full-ensemble takes (a representative spread across songs), NOT all 48 groups, to keep compute sane.
- **Adapter note**: one malformed name observed (`SC1_FT_take3S1.f0`, missing underscore) — adapter must tolerate/skip gracefully, never assume clean names.

## ChoralSynth

- **Zenodo**: DOI `10.5281/zenodo.10137883`, file `Dataset.zip` (96 MB). MD5 matches upstream.
- **License**: CC BY-SA 4.0 (Zenodo metadata is authoritative; a GitHub page saying "NC/non-commercial" is contradicted by Zenodo — we record CC BY-SA 4.0).
- **Layout**: `Dataset/{piece}/voices/*.mp3` plus per-piece `score.musicxml`, `score.midi`, `beat_times.json`, `config.json`, `info.json` (the last lists voice `name`+`type`).
- **Audio**: per-voice **MP3** (not WAV). librosa decodes via libsndfile WITHOUT ffmpeg (confirmed: `08_Anima_nostra/CANTUS.mp3` = 158.9 s, 93% non-silent). 74 mp3, 20 musicxml, 20 midi, 60 json.
- **Pieces**: **20**. Voices-per-piece distribution: **5 voices ×10, 4 voices ×7, 8 voices ×2, 3 voices ×1**.
- **Voice naming is INCONSISTENT across pieces**: e.g. `CANTUS.mp3 / ALTUS.mp3 / TENOR I.mp3 / TENOR II.mp3 / BASSUS.mp3` in one piece; `Cantus Ch1-C1.mp3 / Altus Ch2-C3.mp3` (8-part Ch1/Ch2) in another. The adapter reads `info.json` for the part→type mapping rather than guessing from filenames.
- **Unit = voice PART, not physical singer.** All corpus rows carry `unit=part` for ChoralSynth (vs `unit=singer` for ESMUC/Dagstuhl).

## Consequences for the adapters (Phase 1)
- **ESMUC adapter**: parse `{song}_{setting}_{take}_{track}`; keep tracks matching `^[SATB][0-9]$`; group by `{song}_{setting}_{take}` as `piece_id`; drop `AB`/`ORTF`/`mixed`; require ≥2 singers.
- **ChoralSynth adapter**: iterate `Dataset/*/`; read `info.json` for parts; map each voice mp3 to a part-id; `piece_id` = directory name; `unit=part`.
- Both reuse the existing `extract_to_parquet` (sr-agnostic) and write to `data/processed/{dataset}/{piece_id}/{singer}.parquet`.
