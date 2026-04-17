---
title: Data Sourcing Policy — three-tier strategy for Project 8
type: concept
alchemy_stage: citrinitas
tags: [data, policy, ethics, gdpr, urhg, project-8, scraping, academic-datasets]
ingested_date: 2026-04-17
source_count: 2
related: ["[[Project_8_MOC]]", "[[entanglement_index]]", "[[Janine_Hacker]]"]
team_take: Tree Huggers — we deliberately forbid self-recording because the scientific gain (40 min of anecdote) is far outweighed by the IRB friction, privacy debt, and distraction from the scalable scrape-plus-academic strategy. Conscientious stance wins on means as well as ends.
---

# Data Sourcing Policy — three-tier strategy

**Role**: Citrinitas policy page governing all data acquisition for Project 8. Binding on all four WPs. Canonical version lives in `implementation_plan.md` §5 (v2.1, 2026-04-17) — this page is the vault-graph surface that cross-links it into the Obsidian network.

**Hard constraint**: **No self-recording.** No asking third-party choirs to perform for us. No human-subject research that would trigger ethics-board review. This is a deliberate scope choice by Zuraiz, logged in the v2.1 plan rejection of Gemini 3.1 Pro's Option C.

---

## 1. Three-tier architecture (v2.1)

| Tier | Role (v2.1) | Feeds hypotheses | N target |
|:---|:---|:---|:---|
| **Tier 0** | Prof. Hacker's curated YouTube URL list | anchor — prove minimum viability to supervisor | 5–20 |
| **Tier 1** | YouTube COVID-era virtual choir corpus (yt-dlp scrape) | **Visual-Primary** · H3 only | 150 (stretch 200) |
| **Tier 2** | Academic multitrack datasets (Dagstuhl, ESMUC) | **Audio+Network primary** · H2 | 30+ pieces |
| **Tier 3** | Controlled latency injection on Tier 2 | **Regime-discrimination primary** · H1 | 12× multiplier |

See [[entanglement_index]] §5 for hypothesis-to-tier mapping.

---

## 2. Tier 0 — Hacker's curated URLs

- **Action 2026-04-17**: Zuraiz emails [[Janine_Hacker]] requesting YT URL list. Store at `raw/hacker_url_list.csv`; digest at `wiki/sources/hacker_url_list.md` on receipt.
- **Go/no-go 2026-04-22 09:00 CET**: if silent → escalate + proceed on Tier 1 only; log in `log.md`.
- **Scientific role**: minimum-viable-product demonstration. Pipeline runs on these first; Apr 30 presentation uses them as the visible deliverable.

---

## 3. Tier 1 — YouTube COVID virtual-choir corpus

**Scientific role**: large-N **visual entanglement** study (V1–V9 primary + V2/V4/V5/V7 secondary) + ensemble-descriptive acoustic features (A1, A4, A5). Serves **H3** (Honest Signals predictive value). **Does not serve H1** — natural YouTube videos are not reliably regime-labelled, and mixed-stereo audio blocks per-singer pairwise analysis anyway (see [[entanglement_index]] §4).

### 3.1 Query design

yt-dlp's search API (no Google Data API quota):

- `"virtual choir"`
- `"zoom choir"`
- `"soundjack choir"`
- `"online choir performance"`
- `"distributed choir COVID"`
- `"SATB virtual"`
- `"Eric Whitacre virtual choir"` (reference anchor)

**Date filter**: 2020-03-01 to 2022-06-30.

### 3.2 Inclusion criteria

- Visible SATB composition.
- English title (for consistent entity resolution; not a language bias on the audio).
- Duration ≥ 3 min.
- License: Creative Commons **or** §60d UrhG fair use (see §5 legal basis).
- ≥ 4 visible singers.

### 3.3 Exclusion criteria

- Heavy post-production (reverb layering, visual effects obscuring posture).
- Single performer multitracked into "choir" (defeats the coordination question).
- Copyright-struck on retrieval.
- Private / unlisted / regionally blocked.

### 3.4 Manifest schema (`raw/corpus_manifest.csv`)

```
video_id, url, title, channel, upload_date, duration_s, license,
singer_count_est, latency_regime_label, satb_confirmed,
download_sha256, ingest_date
```

---

## 4. Tier 2 — Academic multitrack baselines

**Scientific role**: per-singer isolated audio streams enable A2 (pairwise DTW), A3 (pairwise F0 xcorr), A8 (breath alignment), A9 (consonant-onset drift), and all N1–N8 network science. Serves **H2** (network topology differs across conditions).

| Dataset | Citation | Access | Status |
|:---|:---|:---|:---|
| **Dagstuhl ChoirSet** | Rosenzweig et al., *TISMIR* 2020 · DOI [10.5334/tismir.48](https://doi.org/10.5334/tismir.48) | open | verified |
| **ESMUC Choral Singing Dataset** | Cuesta et al. · Zenodo record 1286570 (3 pieces · 16 singers · per-voice tracks) | open | verified |
| **Cairns 2024 York thesis** | *Immersive Audio & Network Music Performance* | university repository | SoundJack comparator |
| **DUST** | packet-loss trace corpus | verify access by 2026-04-24 | pending |
| **ChoralSynth** | synthetic SATB generator | open | for Tier 3 scaling |

---

## 5. Tier 3 — Controlled latency injection (v2.1 primary for H1)

**Scientific role**: primary ground-truth design for H1 regime discrimination. Take Dagstuhl/ESMUC multitrack recordings; programmatically apply latency profiles characterising each regime.

| Regime | RTT (ms) | Jitter σ (ms) | Packet loss % | Literature source |
|:---|:---|:---|:---|:---|
| **SoundJack-low** | 20–40 | 3 | 0 | Carôt & Werner 2007 NMP lit |
| **SoundJack-mid** | 40–80 | 8 | 0.5 | Lazzaro 2020 NMP |
| **Zoom-typical** | 150–250 | 30 | 1 | Zoom whitepaper + measurement studies |
| **Zoom-degraded** | 300–500 | 60 | 3 | COVID-era internet reports |

**Implementation**: `scipy.signal.delay` + random jitter draw + periodic zero-out samples. For each multitrack piece × 4 regimes × 3 jitter seeds → 12× effective N multiplier. Within-piece paired design gives high statistical power without self-recording.

**Why Tier 3 is better science than natural YouTube for H1**: we know the ground-truth latency profile. This is precisely the falsifiability standard that satisfies [[Janine_Hacker]]'s empirical-rigor expectations and aligns with [[Peter_Gloor]]'s measurement-first stance in *Cybernetic Alchemy*.

---

## 6. Legal basis

- **§60d UrhG** (German Copyright Act, 2021) — Text-and-Data-Mining exception for research.
- **EU DSM Directive 2019/790 Art. 3** — scientific TDM exception at EU level.
- **GDPR Art. 6(1)(f)** + Art. 89 — legitimate-interest processing + research-purpose safeguards + pseudonymisation. We store only derived feature vectors long-term; raw `.mp4` deleted after extraction; never redistributed.
- **Statutory > Platform ToS** (conflict resolution per `CLAUDE.md` §3). YouTube ToS cannot override statutory TDM rights in DE jurisdiction.

---

## 7. Prohibited practices

- ❌ **Self-recording** (user constraint, preserved across v2.0 → v2.1).
- ❌ **Asking any external choir to perform** for us.
- ❌ **Persisting PII** beyond public channel metadata.
- ❌ **Storing full-face imagery** beyond the feature-extraction window (landmarks only persisted).
- ❌ **Redistributing `raw/*.mp4`** — derived features only.

---

## 8. Directory discipline

```
raw/youtube/<video_id>/             # Nigredo · immutable
  ├── video.mp4
  ├── info.json
  └── sha256.txt
processed/<video_id>/                # Albedo
  ├── stems/{soprano,alto,tenor,bass}.wav
  └── pose/<singer_id>.parquet
features/<video_id>.parquet          # Citrinitas · 33 features
results/                             # Rubedo
  ├── Et.parquet
  ├── graphs/*.gpickle
  └── figures/*.svg
```

Every derived artefact must trace to `raw/youtube/<video_id>/` + SHA-256 via BagIt provenance. No exceptions.

---

## 9. Open Questions

1. Is DUST packet-loss corpus licensing compatible with open-source paper deposit? — resolve by 2026-04-24.
2. Should we invest in ChoralSynth-generated pieces beyond Dagstuhl+ESMUC to increase Tier-3 N? — decision gate at S1 end (2026-05-15), trigger R9 mitigation.
3. Is §60d UrhG applicable when the derivative work (the paper) is published on a non-DE-jurisdiction repository (e.g. arXiv)? — consult Uni Bamberg legal desk before v1 draft (2026-07-07).

## Backlinks

- [[Project_8_MOC]] (Rubedo parent)
- [[entanglement_index]] (Citrinitas sibling — tier usage detail)
- [[Janine_Hacker]] (Tier 0 gatekeeper)
