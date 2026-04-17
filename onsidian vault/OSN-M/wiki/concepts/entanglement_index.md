---
title: Entanglement Index E(t) — operational definition
type: concept
alchemy_stage: citrinitas
tags: [entanglement, metric, audio, video, network, honest-signals, project-8]
ingested_date: 2026-04-17
source_count: 2
related: ["[[Project_8_MOC]]", "[[data_sourcing_policy]]", "[[Peter_Gloor]]", "[[Janine_Hacker]]"]
team_take: Decomposing "entanglement" into three equal-weight sub-signals (audio · visual · network) keeps the claim falsifiable — each sub-score is individually reportable, ablated, and null-modelled.
---

# Entanglement Index E(t)

**Role**: Citrinitas synthesis of Project 8's central scientific contribution — a reproducible, falsifiable operationalisation of "entanglement" for online choir performance. Backlinked from [[Project_8_MOC]]; detailed in `implementation_plan.md` §3.

**Owner**: WP1 (Zuraiz, PI).
**Inputs**: `features/<video_id>.parquet` (33 features).
**Outputs**: `results/Et.parquet`, `results/graphs/*.gpickle`, `results/figures/*.svg`.

---

## 1. Definition

Per-second composite z-score of three equal-weight components (ablation-tested):

```
E(t) = (1/3)·A(t) + (1/3)·V(t) + (1/3)·N(t)
```

Reported as **z-score against a 200× time-shuffled null model** (singer streams independently time-permuted). `|z| > 2` is the discrimination threshold.

### 1.1 A(t) — Acoustic coupling

```
A(t) = 0.4 · (1 − DTW_cost_norm)                 # librosa.sequence.dtw
     + 0.3 · mean_pairwise_F0_xcorr(|lag|<50ms)  # pyin
     + 0.3 · onset_sync_kappa(50 ms bins)        # Fleiss κ on onsets
```

### 1.2 V(t) — Visual coupling

```
V(t) = 0.5 · trunk_sway_xcorr(|lag|<500ms)       # MediaPipe Pose lm 11,12,23,24
     + 0.3 · breath_envelope_xcorr                # shoulder-rise proxy
     + 0.2 · mouth_aperture_sync                  # FaceMesh lm 13,14,78,308
```

### 1.3 N(t) — Network coherence

```
G_t = digraph; edge i→j weight = Granger F-stat on onset-delay
      (window 10 s, stride 2 s, lag AIC-selected)

N(t) = 0.4 · (1 − |density_dev_from_null|)
     + 0.3 · inverse_Gini(eigenvector_centrality) # → collective leadership
     + 0.3 · modularity_Q(Louvain)
```

---

## 2. Theoretical lineage

- **Audio coupling** (A): DTW for warping costs (Müller 2015, *Fundamentals of Music Processing*, Springer) · pyin monophonic F0 (Mauch & Dixon 2014, ICASSP) · onset concordance via Fleiss κ as inter-rater agreement generalised to timing.
- **Visual coupling** (V): Honest Signals framework — Pentland 2008, *Honest Signals* (MIT Press). Trunk-sway is V1 primary (MediaPipe validated Pearson 0.80–0.91 vs Vicon for limb landmarks). Mouth-aperture via FaceMesh (Kartynnik et al. 2019).
- **Network coherence** (N): Granger causality (Granger 1969, *Econometrica*; statsmodels implementation); Louvain modularity (Blondel et al. 2008, J. Stat. Mech.); eigenvector centrality inverse-Gini operationalises [[Peter_Gloor]]'s COINs "collective leadership" principle.

See `implementation_plan.md` §2 for full citation ladder and §8 for EBSE evidence trails on library selection (Decisions 3 & 4).

---

## 3. Null model

200 independent permutations. Each singer stream is circularly time-shifted by an i.i.d. uniform offset in `[0, T)`. All three sub-scores recomputed per permutation. Reported statistic: (observed − μ_null) / σ_null.

**Why circular-shift (not i.i.d. shuffle)**: preserves autocorrelation structure within each stream; destroys only cross-stream timing. This is the correct null for testing coordination vs independent structure.

---

## 4. DSP reality check (v2.1)

**Hard constraint**: A(t) and N(t) both require *per-singer* audio streams. These are **not** available in:

- **Tier 1 mixed-stereo YouTube** (see [[data_sourcing_policy]]) — Demucs v4 separates *instrument classes* (vocals/drums/bass/other), not individual singers; `librosa.pyin` is strictly monophonic and returns garbage on polyphonic vocal mixes.

Therefore, on Tier 1 the A(t) slot is filled by a reduced **ensemble-acoustic variant** `A_ens(t)`:

```
A_ens(t) = 0.4 · collective_tempo_stability
         + 0.3 · global_onset_density
         + 0.3 · spectral_flux_consistency
```

`A_ens(t)` feeds descriptive statistics and H3 hierarchical regression, but **does not participate in the H1 Cohen's-d regime-discrimination claim**. H1 is tested on Tier 3 (controlled latency injection on Tier 2 multitrack) where true per-singer streams exist.

Multi-f0 SATB estimation (Cuesta, Gómez, Bittner 2020, ISMIR) is a **Tier 1 stretch** experiment for *per-section* (S/A/T/B, not per-singer) F0 extraction.

---

## 5. Hypothesis mapping

| Hypothesis | Tier | Sub-scores active | Design |
|:---|:---|:---|:---|
| **H1** regime discrimination | Tier 3 | A · V · N | Paired within-piece; 4 regimes × 3 jitter seeds |
| **H2** network topology differs | Tier 2 + Tier 3 | N (N1–N4, N6) | Mann-Whitney U on density vs null |
| **H3** Honest-Signals ΔR² | Tier 1 (visual) + Tier 2 (audio) | V + A_ens | Hierarchical regression; ΔR² ≥ 0.10 threshold |

See [[data_sourcing_policy]] for tier definitions.

---

## 6. Ablations (planned)

- Equal-weight baseline (1/3, 1/3, 1/3) vs learned weights (ridge regression).
- A-only / V-only / N-only marginals.
- Window size sensitivity (5 s vs 10 s vs 30 s).
- Lag tolerance sensitivity for A(t) F0 xcorr (|lag|<25/50/100 ms).
- Granger vs transfer-entropy (IDTxl) fallback for N(t) (Decision 4 fallback path).

---

## 7. Open Questions

1. Should `A_ens(t)` be reported alongside the main E(t) or strictly separated in the paper? — Leaning "separated" to avoid muddying H1. Decide by v1 paper draft (2026-07-07).
2. Does trunk-sway vs. head-sway validity degrade on webcam-framed Zoom videos where only head+shoulders are visible? — WP2 calibration study scheduled (`wiki/concepts/pose_validity.md` expected 2026-05-22).
3. Granger stationarity failure rate on Dagstuhl pilot — if > 30 %, activate IDTxl fallback (Decision 4 R1-level evidence trail).

## Backlinks

- [[Project_8_MOC]] (Rubedo parent)
- [[data_sourcing_policy]] (Citrinitas sibling — tier definitions)
- [[Peter_Gloor]] (COINs framework provides N(t) interpretation)
- [[Janine_Hacker]] (supervisory rigor — evidence-trail standard)
