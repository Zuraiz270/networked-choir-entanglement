---
title: Latency Thresholds in NMP
type: concept
alchemy_stage: citrinitas
tags: [latency, synchronization, perception, deep_read]
ingested_date: 2026-04-23
last_updated: 2026-04-24
source_count: 4
related: ["[[p_11_chamber_choir]]", "[[p_09_how_late]]", "[[s_04_ar_latency_perception]]", "[[entanglement_index]]", "[[p_23_immersive_nmp_qoe]]", "[[deep_read_audit]]"]
---

# Latency Thresholds in NMP

Latency is the primary physical constraint in Networked Music Performance (NMP). Understanding human perceptual thresholds is critical for both the design of NMP platforms and our formulation of the Entanglement Index $E(t)$.

> **Important framing (2026-04-24 deep-read cascade):** The round numbers below (100 ms, 85 ms, 150 ms) circulate as common wisdom in the NMP community, but **none of them is a statistically validated phase transition in the primary literature we have audited**. Where a number came from a specific paper, we cite it with its measured mean ± SD; where it is engineering-design rationale, we say so. See `## Provenance` at the end.

## The Jamulus Inter-Chorister Timing Regime (measured, P-11)

[[p_11_chamber_choir]] reports the only controlled measurement we have of inter-chorister onset timing in a choral-NMP system:

| Condition | Inter-chorister timing (mean ± SD) |
| :--- | :--- |
| Home (Jamulus, WAN) | **83 ms ± 57 ms** |
| University (Jamulus, LAN) | **47 ms ± 46 ms** |

P-11 did **not** perform a phase-transition analysis. The authors describe a qualitative pattern (subjective quality jump around Jamulus university setups), but do not fit a threshold model or test one statistically.

**100 ms as a design target, not a cliff**: Jamulus literature and the Cychnerski-Mróz platform are *designed to stay under* 100 ms one-way where possible. Treating 100 ms as an empirical coordination cliff conflates a design specification with a measured human perceptual threshold — those are different claims.

## The "Impossibility" Regime (Zoom-class, 300-1000 ms)

At the latencies typical of consumer video-conferencing (Zoom, Teams, etc.), human musicians abandon synchronous performance strategies and shift to a "wait-and-see" or echo-like behavior. This is consistent across all NMP audit sources. [[s_03_choirathome_tools]] catalogues the Zoom-class tools; no primary source in our audit reports successful synchronous music-making at these latencies without a rigid external tempo source.

## Audio-Visual Mismatch (AR, P-09 / S-04 — same study)

> **Same-study note**: [[p_09_how_late]] (IEEE VRW 2022 workshop abstract, 2 pages) and [[s_04_ar_latency_perception]] (ISMAR 2022 full paper, Hopkins et al.) are **the same study** at two venues. S-04 is the full report with statistics.

S-04 / P-09 report a Task × Latency interaction F=2.61, p=.014, η²=.10 on AR remote musical task performance. The frequently quoted "1200 ms tolerance" is **an artifact of a cyclic-rhythm confound** at the 1200 ms test condition, not a real perceptual ceiling — at 1200 ms the delayed beat aligns with the next cycle of a repeating rhythm, making the delay appear less disruptive than it would on a free-rhythm task.

Useful from the full S-04 paper:

- **Noticeable range for AR audio-visual desync**: ~160 ms to ~320 ms (reported qualitatively).
- **Discrete perception boundary**: > 320 ms (audio and visual parsed as separate events).
- Focus-shift is a non-monotonic effect, not a simple "players noticed less because they prioritized audio" story.

## Impact on E(t)

Our analysis of Tier 2 (Jamulus / SoundJack multitrack) and Tier 3 (controlled latency injection) data will test whether [[entanglement_index]] sub-scores degrade across the measured regimes above. We do **not** assume a specific numeric threshold exists; H1 is formulated as a regime-discrimination hypothesis (d ≥ 0.5), not a cliff-location hypothesis.

## Provenance (2026-04-24)

| Claim | Numeric | Source | Status |
| :--- | :--- | :--- | :--- |
| Jamulus home inter-chorister timing | 83±57 ms | [[p_11_chamber_choir]] | **Measured** |
| Jamulus LAN inter-chorister timing | 47±46 ms | [[p_11_chamber_choir]] | **Measured** |
| AR audio-visual desync Task×Latency | F=2.61, p=.014, η²=.10 | [[s_04_ar_latency_perception]] | **Measured** |
| "100 ms phase transition" | — | Common-wisdom / Jamulus design spec | **Not a measured cliff; correction logged** |
| "85 ms fluidity threshold" | — | Cychnerski-Mróz design target | **Design target, not measured** |
| "Zoom impossibility at 150 ms" | — | Qualitative across sources | **Qualitative consensus, no single measured cliff** |
| [[p_23_immersive_nmp_qoe]] XR-vs-baseline | 74 ms vs 144 ms | [[p_23_immersive_nmp_qoe]] | **Measured — confound: QoE advantage is confounded with latency reduction** |

## Corrections Logged Against Prior Digest (2026-04-24)

| Issue | Prior claim | Corrected reading |
| :--- | :--- | :--- |
| "85 - 150 ms Metronome Threshold" | Presented as a perceptual range in the literature | P-11's measured inter-chorister timing is 83±57 / 47±46 ms; 85-150 ms is not a validated regime boundary. |
| "100 ms phase transition" | Implied coordination cliff | **Design target** for Jamulus, not an empirical phase transition. P-11 ran no phase-transition analysis. |
| "P-09 AR latency research" | Cited as sole source | P-09 and S-04 are the **same study**; S-04 is the full ISMAR paper with F-statistics; P-09 is the 2-page VRW abstract. |
| "1200 ms tolerance" | Reported as perceptual ceiling | **Cyclic-rhythm-confound artifact** at the 1200 ms test condition; not a ceiling on free-rhythm tasks. |
