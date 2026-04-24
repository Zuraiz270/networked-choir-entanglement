---
title: Entanglement Index E(t)
type: concept
alchemy_stage: citrinitas
tags: [metrics, entanglement, coupling, audio-visual, deep_read]
ingested_date: 2026-04-23
last_updated: 2026-04-24
source_count: 2
related: ["[[s_02_entanglement]]", "[[Project_Overview]]", "[[limitations_register]]", "[[p_22_augmented_granger_causality]]", "[[coin_framework]]", "[[honest_signals]]", "[[deep_read_audit]]"]
---

# The Entanglement Index E(t)

The Entanglement Index, denoted as $E(t)$, is the **proposed** metric we are developing to quantify "group flow" or coordination in Networked Music Performance (NMP). It is **not an empirically validated metric** for music; H1-H3 (see [[Project_Overview]]) are the first test of E(t) on musical data.

## Origin

The term borrows from two disciplines:

1. **Social Entanglement (Gloor):** Quantifies synchronized communication patterns in Collaborative Innovation Networks (COINs) (see [[s_02_entanglement]]).

   > **Provenance caveat (2026-04-24 deep-read):** S-02 validated its formula on **email data with 7-day windows** across four knowledge-work organizations (n=111-113 per case). Every case reports modest effect sizes (Pearson r = .522-.707 where significant; Case A r=.615, p=.045). Adaptation to continuous music-domain streams (seconds-scale windows, audio + pose + breath signals) is a **novel domain transfer with no prior validation**. See [[limitations_register]] §4.

2. **Physical Entrainment (P-13):** The behavior of coupled **self-sustained oscillators** that synchronize phase and frequency (see [[p_13_human_sync_review]]).

   > **Provenance caveat:** [[p_13_human_sync_review]] catalogs 101 human-synchronization datasets; only **3 carry explicit synchrony annotations**, and P-13 documents measurement heterogeneity (PLV, GCA, RQA) rather than endorsing any single operationalization.

## Adaptation for NMP

In the context of online choirs, asynchronous communication is replaced by real-time, synchronous performance. $E(t)$ must therefore be a composite score derived from multiple time-series streams rather than email frequency:

1. **Audio Coupling ($A(t)$, a.k.a. $E_a$)**: How well note onsets, pitch (F0), and tempo align between singers.
2. **Visual Coupling ($V(t)$, a.k.a. $E_v$)**: How well body sway, posture, and facial landmarks (MediaPipe) synchronize. Operationalizes Pentland-style [[honest_signals]] for choir video.
3. **Network Topology ($N(t)$, a.k.a. $E_n$)**: The Granger-causal influence graph showing "who leads whom" based on audio/visual onset predictions. Per [[p_22_augmented_granger_causality]], run both standard Granger and ordinal-pattern (COP-GC) variants and compare.

## Hypothesis

If $E(t)$ is a valid measure of musical coordination:

1. It should distinguish high-latency (Zoom) from low-latency (SoundJack) performances.
2. It should correlate with the honest signals of the singers (visible breathing and sway).
3. The topology of influence will shift from dense/democratic (low latency) to sparse/leader-dominated (high latency).

**Epistemic status**: these are **hypotheses under test**, not settled findings. A negative result (E(t) does not discriminate the regimes, or H3's ΔR² ≥ 0.10 is not achieved) is a valid scientific outcome and does not invalidate the metric formulation — it only bounds the claim.

## Corrections Logged Against Prior Digest (2026-04-24)

| Issue | Prior framing | Corrected reading |
| :--- | :--- | :--- |
| Missing S-02 domain caveat | E(t) "borrows from Social Entanglement (Gloor)" | S-02 is **email-only**, n=111-113 cases, 7-day windows. Adaptation to music is novel. |
| Implicit "E(t) is validated" framing | "The Entanglement Index ... quantify 'group flow'" | E(t) is a **proposed** metric. H1-H3 are its first empirical test on music. |
| Missing honest-signals provenance | "facial landmarks (MediaPipe)" | V(t) operationalizes Pentland's [[honest_signals]] framework ([[Alex_Pentland]], 2008 MIT Press). |
| Missing Granger robustness note | "Granger-causal influence graph" | Per [[p_22_augmented_granger_causality]], run both standard GC and COP-GC in parallel. |
