# Feature Schema

Project 8 uses parquet feature tables as the boundary between work packages. This file documents the current contracts used by `src/choir_entanglement/` and the batch scripts.

## WP1 Audio Feature Frame

One parquet per singer or part.

Path pattern:

```text
data/processed/<dataset>/<piece>/<singer_or_part>.parquet
```

Required columns:

| Column | Type | Unit | Used by |
|:--|:--|:--|:--|
| `time_sec` | float64 | seconds | E(t), latency injection, dashboard |
| `rms` | float64 | normalized amplitude | A(t), Granger, E(t) |
| `onset` | bool | frame-level note attack flag | onset synchrony, Tier-3 H1 |

Optional columns:

| Column | Type | Unit | Used by |
|:--|:--|:--|:--|
| `f0_hz` | float64 | Hz | audio diagnostics |
| `voiced` | bool | frame-level voicing | latency injection |
| `voiced_prob` | float64 | probability | audio diagnostics |

Contract notes:

- `time_sec` must be monotonic.
- `rms` must be finite wherever a frame is valid.
- `onset` is filled with `False` when missing values appear after latency/dropout simulation.
- When `onset` exists, `compute_entanglement` folds zero-lag onset synchrony into the audio component `A`.

## WP2 Pose Feature Frame

One parquet per video.

Path pattern:

```text
data/processed/tier1/<video_id>/pose.parquet
```

Required columns:

| Column | Type | Unit | Used by |
|:--|:--|:--|:--|
| `time_sec` | float64 | seconds | dashboard, V(t) windows |
| `shoulder_rise` | float64 | normalized pose distance | V(t) |
| `head_sway` | float64 | normalized pose distance | V(t) |
| `trunk_lean` | float64 | normalized pose distance | V(t) |

Overlay columns:

```text
pose_<landmark>_x
pose_<landmark>_y
```

The dashboard reads all columns matching `pose_*_x` and `pose_*_y` and returns them as a per-frame keypoint map.

Contract notes:

- Missing keypoints are encoded as null/NaN, not zero.
- Coordinates are normalized to the source video frame.
- Current Tier-1 videos are video+pose only; they do not provide per-singer audio streams.

## WP3 Influence Graph

One GEXF per piece and method.

Path pattern:

```text
data/processed/<dataset>/<piece>/influence_graph_<method>.gexf
```

Current methods:

| Method | Meaning |
|:--|:--|
| `standard` | Parametric Granger causality |
| `cop_gc` | Continuous ordinal-pattern Granger variant |

Required edge attributes:

| Attribute | Type | Used by |
|:--|:--|:--|
| `weight` | float | dashboard edge weight |
| `lag` | int | dashboard tooltip / diagnostics |

## Derived Tables

| File | Contract |
|:--|:--|
| `data/processed/dagstuhl/_et_corpus.csv` | Sprint-3 E(t) corpus summary for Dagstuhl pieces |
| `data/processed/tier3/_latency_grid.csv` | H1 latency grid across datasets, pieces, and regimes |
| `data/processed/tier3/_h2_centralization.csv` | H2 centralization test against a density-matched random null |
| `data/processed/tier1/_pose_summary.csv` | Tier-1 pose extraction quality summary |

## Current Limitation

No current corpus item has all three native signals together. Dagstuhl/ESMUC/ChoralSynth provide audio and network signals; Tier-1 videos provide visual pose signals. `E(t)` therefore averages the available components and records the count in `n_available`.
