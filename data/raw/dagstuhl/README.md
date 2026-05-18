# Dagstuhl ChoirSet — Provenance

## Source

- **Dataset**: Dagstuhl ChoirSet (DCS), version 1.2.3
- **DOI**: [10.5281/zenodo.4618287](https://doi.org/10.5281/zenodo.4618287)
- **Direct download**: <https://zenodo.org/records/4618287/files/DagstuhlChoirSet_V1.2.3.zip>
- **Size**: 5.1 GB
- **MD5**: `82b95faa634d0c9fc05c81e0868f0217`
- **License**: Creative Commons Attribution 4.0 International (CC-BY-4.0)
- **Published**: 2021-03-18

## Citation

Sebastian Rosenzweig, Helena Cuesta, Christof Weiß, Frank Scherbaum, Emilia Gómez, and Meinard Müller (2020). *Dagstuhl ChoirSet: A Multitrack Dataset for MIR Research on Choral Singing.* Transactions of the International Society for Music Information Retrieval, 3(1), pp. 98–110.

[Paper (open access)](https://transactions.ismir.net/articles/10.5334/tismir.48)

## What's in it

Amateur vocal ensemble (SATB quartet and full choir settings) performing two choir pieces. Per-singer close-up microphones (larynx, headset, dynamic) yield isolated multitrack audio, with beat annotations, time-aligned scores, and automatically extracted F0 trajectories for each track.

## Role in this project

Tier-2 ground-truth corpus for WP1 (audio coupling A(t)) and WP3 (Granger-causal influence networks N(t)). Multitrack isolation per singer is the prerequisite that Tier-1 YouTube mixed-stereo cannot provide (per Apr-17 DSP-blocker finding: librosa.pyin is monophonic, Demucs separates instrument classes not individual singers).

## Reproducibility

Re-download:

```bash
curl -L -o data/raw/dagstuhl/DagstuhlChoirSet_V1.2.3.zip \
  "https://zenodo.org/records/4618287/files/DagstuhlChoirSet_V1.2.3.zip?download=1"
```

Verify integrity:

```bash
md5sum data/raw/dagstuhl/DagstuhlChoirSet_V1.2.3.zip
# Expected: 82b95faa634d0c9fc05c81e0868f0217
```

Unzip:

```bash
unzip data/raw/dagstuhl/DagstuhlChoirSet_V1.2.3.zip -d data/raw/dagstuhl/
```

## Compliance notes

CC-BY-4.0 permits redistribution with attribution. We do **not** redistribute the raw audio in this repo (kept under `data/raw/` which is `.gitignore`d). Derived features (parquet under `data/processed/`) are stored separately and may be committed depending on size and the data sourcing policy at `onsidian vault/OSN-M/wiki/07_legal_compliance/data_sourcing_policy.md`.
