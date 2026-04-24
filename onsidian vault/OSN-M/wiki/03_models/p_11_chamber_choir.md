---
title: P-11 NMP for Chamber Choir
type: source
alchemy_stage: nigredo
tags: [nmp, architecture, latency, jamulus, deep_read, covid]
ingested_date: 2026-04-23
last_deep_read: 2026-04-23
source_count: 1
related: ["[[nmp_architecture]]", "[[latency_thresholds]]", "[[conductor_perceptual_bottleneck]]", "[[deep_read_audit]]"]
team_take: Most directly relevant existing NMP-for-choirs study. 20-member amateur choir, COVID-era deployment at single institution. Provides the primary empirical data for Project 8's Tier-2 Jamulus latency benchmarks.
---

# P-11 Architecture Design of a Networked Music Performance Platform for a Chamber Choir

**Citation**: Cychnerski, J., Mróz, B. (2022). In *ADBIS 2022 Short Papers, Doctoral Consortium and Workshops*, CCIS vol. 1652, pp. 437 to 449. Springer Cham. [DOI:10.1007/978-3-031-15743-1_40](https://doi.org/10.1007/978-3-031-15743-1_40).
**Affiliations**: Faculty of Electronics, Telecommunications and Informatics, Gdańsk University of Technology, Poland.
**Ensemble**: Academic Choir of Gdańsk University of Technology, 20 members, rehearsals during 2021 Polish COVID-19 restrictions.
**raw path**: `raw/01_primary_sources/Architecture Design of a Networked Music Performance Platform for a Chamber Choir.pdf`

## 1. Study Design (§2)

Three architectures deployed sequentially over ~2 months each. Each evaluated by in-choir survey and RTT measurements. Iterations used choir's real rehearsals, not controlled trials.

## 2. Raw Data Block (Table 1 + Results §3)

| Architecture | Connection | Audio RTT | Video latency | Inter-chorister timing (actual) | Features | N (survey) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Zoom@Home** | Any | **300-1000 ms** | 500-1000 ms | n/a (tutti impossible) | Conferencing; only solo singing or muted-mic tutti with piano | 8 |
| **Jamulus@Home** | Broadband, ASIO | **63-135 ms** | — (no video) | **83 ms ± 57 ms** | Semi-pro headset (Logitech PC 960 USB), intra-section feedback, one-way Zoom gateway for non-NMP members | 16 |
| **Jamulus@Univ** | LAN | **40-85 ms** | 25-100 ms (Jitsi server) | **47 ms ± 46 ms** | Professional audio + dedicated Jitsi video, on-site classrooms with plywood separators | 13 |

**Total survey**: 23 unique choristers (9 male / 14 female, aged 18-30). Some participated across iterations.

## 3. Statistical Analysis (§3.4)

**Software**: R 4.1.2. Ordinal logistic regression via Cumulative Link Mixed Model (CLMM). Helmert contrast coding on Platform categorical. Holm's sequential Bonferroni post-hoc. Weights by rehearsal count (1-2 = 1, 3-6 = 2, 7+ = 3).

**Rehearsing comfort** (7-point Likert):

- Unweighted: χ²(2, N=37) = 1.93, **n.s.**
- **Weighted**: χ²(2, N=86) = 10.84, **p < 0.01**
- Post-hoc (weighted): Jamulus@Home vs Jamulus@Univ Z = **−3.1**, p < 0.01 (significant). Other pairs n.s.

**Exercising difficulty** (7-point Likert):

- Unweighted: χ²(2, N=37) = **29.5**, p < 0.001
- Weighted: χ²(2, N=86) = **46.4**, p < 0.001
- Post-hoc: all three pairs significant. (Raw Z-values in PDF text appear affected by extraction artifacts but the paper reports all p < 0.001 after Holm correction.)

**Direction of effect** (paraphrased §3.4): Exercising is hardest on Zoom@Home; noticeably easier on both Jamulus platforms, with Jamulus@Univ slightly better than Jamulus@Home. Rehearsing comfort differs significantly only between the two Jamulus variants (favoring Univ).

## 4. Recommendations (§3.5)

Paper proposes optimal-architecture requirements:

1. NMP software with **RTT ≤ 100 ms**, dedicated server near performers
2. Low-latency video server (**≤ 100 ms**)
3. Conductor station: professional equipment, fast network, close to servers
4. Performer stations: professional audio, adjustable self-feedback + section amplification
5. Unified hardware to enable config scripts
6. One-way gateway to popular conferencing tools for passive non-NMP participants
7. Remote assistance available at all times, group connection testing

## 5. Limitations

**Stated** [§4 Summary]:

- Network and audio latencies still need further reduction via low-latency drivers.
- Entry threshold for NMP tools is too high; needs automatic configuration, volume control, intuitive UI.
- Future: P2P communication, VST plugins, ambisonics, VR.

**Implicit (binding on Project 8 citation)**:

- **n = 23 total**, single amateur ensemble, single institution, 2-month windows per iteration. No cross-ensemble or cross-institution replication.
- Student choristers aged 18-30; not representative of demographically diverse or professional choirs.
- Data is **self-report Likert** + RTT measurement. No objective performance quality measure (no onset sync, no intonation drift, no PLV).
- Observational design; no randomization or counterbalancing. Carry-over effects across iterations uncontrolled.
- COVID-era deployment; safety perception (§3.3) was a real confound.
- "100 ms RTT" design target is stated as heuristic, not empirically validated as a phase-transition threshold in the paper. The 63-135 ms Jamulus@Home and 40-85 ms Jamulus@Univ ranges both yielded workable rehearsals.
- Inter-chorister timing ±SD (83 ± 57 ms, 47 ± 46 ms) is large relative to the mean. Suggests high variability; paper does not model the tail.

## 6. Relevance to Project 8 E(t)

**P-11 is load-bearing for**:

- **Tier 2 Jamulus benchmark numbers**: 63-135 ms (home broadband) and 40-85 ms (LAN), plus the inter-chorister timing differences 83 ms ± 57 ms and 47 ms ± 46 ms. Project 8 can directly cite these as empirically measured Jamulus RTT bounds.
- **[[conductor_perceptual_bottleneck]]**: P-11 explicitly shows that **audio-only NMP fails at controlling tempo variations** (acceleration, fermatas, rubato) even at 63-135 ms RTT; visual conducting below 100 ms is required.
- **[[latency_thresholds]]**: the <100 ms design target is now source-backed to this paper (rather than unsourced). However, see caveat above: P-11 does not establish 100 ms as a phase transition, only as a practical working target.
- **v2.2 scope**: supports Project 8's Tier-2 focus as the primary latency-conclusion test bed.

**P-11 is NOT**:

- Source for 85 ms, 150 ms, 320 ms specific thresholds (P-09 covers 160-320 ms AR mismatch).
- Source for audio-coordination quantitative metrics (no onset sync or coupling measurement).
- Source for objective entanglement — only self-report and RTT data.
- Evidence of phase-transition behavior at specific latency values; it shows monotonic improvement across three well-separated design points.

## 7. Corrections Logged Against Prior Digest

See [[deep_read_audit]] for full table. Summary:

| Issue | Prior claim | Corrected reading |
| :--- | :--- | :--- |
| Missing inter-chorister timing numbers | "Enabled simultaneous singing and intra-section feedback" | Jamulus@Home: 83 ms ± 57 ms; Jamulus@Univ: 47 ms ± 46 ms inter-chorister note-onset differences [§3.2, §3.3]. These are primary Project-8 Tier-2 baseline numbers. |
| Missing statistical analysis | "Authors evaluated three distinct architectures" | χ² tests via CLMM (R 4.1.2): exercising difficulty unweighted χ²=29.5 p<.001; rehearsing comfort weighted χ²=10.84 p<.01 with only Jamulus@Home vs @Univ pair significant [§3.4]. |
| Missing n | (not stated) | 23 unique choristers (9M/14F, 18-30); 8 / 16 / 13 responses per architecture iteration [§3]. |
| "A significant jump... occurs when moving from >300ms to ~100ms, and another distinct leap when dropping below 85ms with visual feedback" | — | This is P-11's qualitative pattern but **the paper does not statistically establish phase-transition thresholds at 100 ms or 85 ms**. Both Jamulus variants enabled workable rehearsals; the Jamulus@Univ advantage is partly audio (40-85 vs 63-135 ms) and partly video (present vs absent). Cannot isolate which factor contributes. |
| Missing visual-conducting evidence strength | "Essential for controlling tempo variations" | Explicitly stated by authors: without video, "maintaining a steady performance was very difficult and unattainable without a conductor" [§2.3]; adding video "allowed the conductor to feasibly lead the choir in a real-time manner visually, which was previously inaccessible" [§2.3]. Strong qualitative claim, no quantitative metric. |
| Missing amateur + single-ensemble caveat | (no mention) | n=23 amateur students, single institution (Gdańsk UT), single 2-month COVID window per iteration. Generalizability not tested [§3.1]. |
| Missing design-target vs. empirical-threshold distinction | "100 ms RTT" | Paper presents 100 ms as a **design target** for recommended architecture [§3.5], not as an empirically validated phase transition. Project 8 must not cite P-11 as proof of a 100 ms perceptual cliff. |
