---
title: P-07 JackTrip Framework
type: source
alchemy_stage: nigredo
tags: [nmp, education, latency, jacktrip, deep_read]
ingested_date: 2026-04-23
last_deep_read: 2026-04-23
source_count: 1
related: ["[[sonic_imperialism]]", "[[nmp_on_the_edge]]", "[[nmp_hardware_requirements]]", "[[deep_read_audit]]"]
team_team: Very short paper (5 pages). Latency numbers are based on computed formulas and ping tests only, no end-to-end audio-pipeline measurement, no human ensemble evaluation, no actual Global South deployment.
---

# P-07 Bridging Cultural and Digital Divides: A Low-Latency JackTrip Framework for Equitable Music Education in the Global South

**Citation**: Zhou, T., Bidin, M. (2025). In *2025 7th International Conference on Computer Science and Technologies in Education (CSTE)*, 510 to 514. [DOI:10.1109/CSTE64638.2025.11092043](https://doi.org/10.1109/CSTE64638.2025.11092043).
**Affiliations**: School of Future Design, Beijing Normal University Zhuhai (T. Zhou); Dept. of Instrument Engineering, Xinghai Conservatory of Music Guangzhou (M. Bidin).
**raw path**: `raw/01_primary_sources/Bridging_Cultural_and_Digital_Divides_A_Low-Latency_JackTrip_Framework_for_Equitable_Music_Education_in_the_Global_South.pdf`

## 1. Setup (§IV Methodology)

- **2 computers** ~1000 km apart (physical separation; no Global South deployment)
- Network emulators: **Network Link Conditioner** (Mac OS) + **Clumsy** (Windows OS)
- Simulated parameters: uplink 5-10 Mbps, downlink 10-50 Mbps, packet loss 0-3%
- Emulates 3G/4G cellular profiles
- **Zero human participants** in the evaluation; no listening test; no MOS survey

## 2. Latency Computation (Eq. 1)

$$T_{total} = T_d + T_p + T_{proc}$$

With audio packet = 4096 bits and 5 Mbps bandwidth:

- **T_d** (transmission) = 4096 / 5×10⁶ = **0.819 ms**
- **T_p** (propagation) = 10⁶ m / (2×10⁸ m/s) = **5 ms**
- **T_proc** (processing, ping-measured): JackTrip 15-20 ms, Zoom 130-140 ms

**Reported totals**:

- JackTrip: 0.819 + 5 + 20 ≈ **26 ms**
- Zoom: 0.819 + 5 + 135 ≈ **141 ms**

## 3. Audio Fidelity Claim

- JackTrip: 1536 kbps, 20 Hz to 20 kHz preserved
- Zoom: 192 kbps, audio compression attenuates above 3 kHz

**Method**: Spectral analysis via Audacity on three sample types:

1. Short transients (<1 s)
2. Medium sustained notes (3-5 s)
3. Extended microtonal scales performed on Peruvian panpipes

Results presented as Audacity spectrograms (Figs. 2 and 3). **No quantitative spectral metrics** reported.

## 4. Limitations (stated + implicit)

**Stated** [§VI-D]:

- Raspberry Pi hardware subject to electricity, connectivity, maintenance skill constraints.
- Digital technology must supplement, not replace, community-based traditional learning.
- Future work: pilot tests in local communities, culturally-relevant pedagogy, longitudinal studies.

**Implicit (binding on citation)**:

- **No actual Global South deployment**. All evaluation is emulated from unspecified initial locations.
- **n = 0 human participants**. No listening test, no musician feedback, no ensemble performance.
- **Latency numbers are arithmetic sums**, not end-to-end audio-pipeline measurements. T_proc is ping RTT / 2, not audio-framework processing.
- Spectral comparison is visual Audacity inspection only; no SNR, THD, or objective fidelity metric.
- The 1536 kbps vs 192 kbps comparison is configuration (what JackTrip transmits vs what Zoom transmits), not a validated Quality of Experience improvement.
- "Sonic Imperialism" is a cultural argument; not empirically validated in the paper.
- Conference venue (CSTE) is an education-technology conference, not primarily a music / audio engineering venue.
- Paper is 5 pages; depth of technical analysis limited.
- **Compare to P-06 for context**: P-06's more thorough MOS study (n=15) found JackTrip and symbolic NMP essentially tied in normal network conditions (Scenarios 1-3, MOS differences ≤0.1). P-07's dramatic 26 vs 141 ms result therefore overstates practical JackTrip advantage when listener perception is accounted for.

## 5. Relevance to Project 8 E(t)

**P-07 is useful for**:

- **[[sonic_imperialism]]**: the "Sonic Imperialism" framing (non-Western music distorted by 12-TET-optimized platforms) is a legitimate conceptual contribution, though not empirically tested here.
- **JackTrip latency ballpark**: the 26 ms figure is in line with other sources (Bosi et al. 2021 JAES; Rottondi 2016 IEEE Access). Project 8 can cite it with P-11 and P-23 as corroborating.
- **Low-cost Raspberry Pi edge framing**: useful for Tier-2 deployment discussion.

**P-07 is NOT**:

- A source for actual Global South deployment outcomes (none performed).
- A source for human-perceivable QoE differences (no listening test).
- Primary empirical evidence for latency numbers in NMP — these should be sourced to the foundational JackTrip papers (Cáceres & Chafe 2010, Bosi et al. 2021) rather than this derivative study.
- Evidence for "Professional Flow" levels at specific latency values (paper makes no such claim).

## 6. Corrections Logged Against Prior Digest

See [[deep_read_audit]] for full table. Summary:

| Issue | Prior claim | Corrected reading |
| :--- | :--- | :--- |
| Missing n=0 participants caveat | (no mention) | Zero human participants; only arithmetic latency computation and Audacity spectrograms. No listening test, MOS, or ensemble evaluation [§IV]. |
| "Empirical evidence that E(t) can reach Professional Flow levels on decentralized UDP-based protocols" | — | Paper makes no empirical coordination / coupling / E(t) claim. This is Project-8 speculation, not P-07 finding. Moved to §5 as extrapolation. |
| Latency figures treated as measured | "JackTrip achieved ~26ms" | 26 ms is **computed** (T_d + T_p + T_proc), where T_proc is ping-derived, not audio-end-to-end measured. The processing delay 15-20 ms for JackTrip is ping-inferred [§V-A]. |
| Missing "computed not measured" caveat | (no mention) | Latency is Eq. 1 arithmetic sum, not measured on audio pipeline. |
| Over-cited as primary JackTrip source | "validates the 'Hardware-Optimized' Tier" | P-07 is derivative. Primary JackTrip sources: Cáceres & Chafe 2010 (JNMR), Bosi et al. 2021 (JAES) — both cited within P-07. |
| Missing conflict with P-06 evidence | (no mention) | P-06's human MOS survey (n=15) shows JackTrip and non-audio alternatives essentially tied in normal-network conditions, contradicting P-07's implied large advantage. P-07's dramatic 26 vs 141 ms number is not what listeners perceive. |
