---
title: Deep-Read Audit Log
type: synthesis
alchemy_stage: rubedo
tags: [audit, deep_read, ebse, provenance]
ingested_date: 2026-04-23
last_updated: 2026-04-24
campaign_status: COMPLETE
source_count: 27
related: ["[[index]]", "[[Project_8_MOC]]"]
---

# Deep-Read Audit Log

Audit record of rigorous full-text re-ingestion of every primary and secondary source, replacing the prior Gemini Flash 3.0 shallow ingestions. Scope: P-01 to P-23 and S-01 to S-04 per [`../PAPER_LINKS.md`](../PAPER_LINKS.md).

## Campaign Status (2026-04-24)

**COMPLETE**: 27 of 27 sources re-ingested (P-04 Pentland *Honest Signals* remains TO-ACQUIRE).

- **Tier A**: 7/7 (P-12, S-02, P-09, P-14, P-22, P-21, P-13)
- **Tier B**: 10/10 (P-01, P-02, P-06, P-07, P-08, P-11, P-15, P-23, S-01, S-04)
- **Tier C**: 9/9 (P-03, P-05, P-10, P-16, P-17, P-18, P-19, P-20, S-03)

**Cross-cutting corrections caught**:

- **Fabricated numerics**: P-20's "+31% cpCER", S-03's "80% hardware dependency" and comparative-latency table.
- **False causal-audiovisual analogies**: P-18, P-19, P-05 — prior digests repeatedly over-extrapolated from visible-motion instruments (strings, lips) to voice, where the causal chain breaks (vocal folds are internal).
- **Latency / experimental confounds missed**: P-23's 144 ms vs. 74 ms A2S baseline; P-10's 0.29 km median distance; P-06's 200 kbps straw-man.
- **Domain-transfer over-reaches**: P-08 (conversation → music), P-20 (sign language → choir), P-16 (clinical respiration → singing breath), P-17 (China law → German law).
- **Missing epistemic caveats**: n=3 (P-12), n=11 (P-10), n=18 (P-16), workshop abstracts (P-09, P-10), project deliverable (S-03), book (S-01).
- **Reversed / mis-sourced findings**: P-03's AR PCK, P-15's latency-vs-traffic direction, P-14's phrase-position asymmetry, P-01's HSM-vs-DYN crosstalk.

Full per-paper corrections are in the **Status Table** (below) and **Per-Paper Entries** (further below).

## Methodology

1. Load the **entire** source text (via `pdftotext -layout` extraction to `.cache/<slug>/<slug>.txt`, then `Read`).
2. Verify word count and section completeness before synthesis.
3. Extract raw data: sample size, reported latencies in ms, p-values and effect sizes where present, topology, dataset size, compute footprint, limitations.
4. Every factual claim in the rewritten digest carries a `[p. N, §X.Y]` citation.
5. Compare every claim in the prior digest against the paper ground truth. Log hallucinations, imprecisions, missing caveats, and unsourced claims projected from Project 8 onto the paper.
6. Cascade corrections to every affected entity, concept, synthesis page per vault §5.1 Rule 1.

## Tiering (per 2026-04-23 plan approval)

- **Tier A** (load-bearing for v2.2 methodology, 7 papers): P-12, P-09, P-14, P-22, P-21, S-02, P-13
- **Tier B** (supporting, 10 papers): P-01, P-02, P-06, P-07, P-08, P-11, P-15, P-23, S-01, S-04
- **Tier C** (peripheral, on-demand, 10 papers): P-03, P-05, P-10, P-16, P-17, P-18, P-19, P-20, S-03, (P-04 in `TO-ACQUIRE`)

## Status Table

| Source ID | Prior Status | Audit Result | Fatal Error Caught | Last Re-Ingest |
| :--- | :--- | :--- | :--- | :--- |
| **P-12** | Shallow (Gemini Flash) | **RE-INGESTED** | Jitter/latency framing imprecise; hub-and-spoke topology omitted; n=3 caveat omitted; "Relevance to E(t)" projected Project-8 claims onto paper | 2026-04-23 |
| **S-02** | Shallow (Gemini Flash) | **RE-INGESTED** | All formulas missing; all p-values and effect sizes missing; domain caveat missing (validated on EMAIL only, 7-day windows, not music); Zylka affiliation (Uni Bamberg) unsurfaced | 2026-04-23 |
| **P-09** | Shallow (Gemini Flash) | **RE-INGESTED** | Sample size n=24 missing; F/p/η² statistics missing; apparatus missing; **"no upper tolerance limit" is an artefact of the cyclic-rhythm confound at 1200 ms, not a real finding**; 2-page workshop-abstract caveat missing; "Cyclic Masking" was a term coined by prior digest, not the paper | 2026-04-23 |
| **P-14** | Shallow (Gemini Flash) | **RE-INGESTED** | All F/p statistics missing; 44-phrases-one-ensemble-one-session caveat missing; AlphaPose v0.4 version (not MediaPipe) missing; stereo-only audio limitation missing; **phrase-position asymmetry** (polyphonic drops at end, homophonic rises) misread as "most pronounced at beginning"; event-density vs. pulse-clarity cross-validation stats missing | 2026-04-23 |
| **P-22** | Shallow (Gemini Flash) | **RE-INGESTED** | Eq. 1 (COP distance formula) missing; quantitative validation results (Eq. 3 GC=0%→COP=100% at γ=0.05) missing; **Zanin's explicit recommendation to use BOTH standard GC and COP-GC** missing; Bonferroni-abandonment caveat missing; D=4 embedding anomaly missing; single-author caveat missing; over-reach on "pitch salience maps" relevance (no music validation in paper) | 2026-04-23 |
| **P-21** | Shallow (Gemini Flash) | **RE-INGESTED** | All method equations (MCCA Eq. 5, Granger model Eqs. 6-16, Lagrangian Eqs. 17-22) missing; **T ≥ 500 sample-size floor** (HGCRM underperforms at T=500) missing; Lorenz-96 + rs-fMRI validation data absent from digest; music-validation caveat missing; "bandwidth prioritization" is Project-8 speculation, not P-21 finding; Chinese-institution authorship and TiMINo-failure context missing | 2026-04-23 |
| **P-13** | Shallow (Gemini Flash) | **RE-INGESTED** | Category percentages (25/19/30/26%) missing; **only 3 of 101 datasets have synchrony annotations** (core gap finding) missing; "Measurement Taxonomy" over-reaches — P-13 does NOT endorse PLV/GCA/RQA, it documents their heterogeneity; "oscillator model explains jitter tolerance" is Project-8 extrapolation, not P-13 finding; pseudosynchrony/surrogate-data methodology missing; Mayo-Gordon "disruption is adaptive" missing; cultural-bias caveat missing; GitHub dataset registry unsurfaced | 2026-04-23 |
| **P-01** | Shallow (Gemini Flash) | **RE-INGESTED** | All exact counts missing (13 singers, 81 takes, 55:30); F0 evaluation numbers (pYIN/CREPE OA per mic) missing; HSM described as "medium" crosstalk is wrong (HSM has worst OA); hardware specs absent; **"no network, no coordination annotations" caveat missing**; "primary failure mode for our Entanglement Index tests" is Project-8 over-reach; open artifact links (Zenodo, toolbox) unsurfaced | 2026-04-23 |
| **P-02** | Shallow (Gemini Flash) | **RE-INGESTED** | F/P/R numbers missing (Late/Deep F=0.846 @ 100c, 0.831 @ 20c vs. baselines dropping 17-26%); 5-dataset aggregate (22,910 files) not specified; ESMUC-proprietary caveat missing; **"P-02 does NOT output per-singer F0s"** critical caveat missing ("track micro-fluctuations of each singer" is false); hardware/training specifics missing | 2026-04-23 |
| **P-06** | Shallow (Gemini Flash) | **RE-INGESTED** | Year wrong (2024 → 2025); MOS table and missing-note stats absent; **authors' own caveat that Scenarios 1-3 differences are NOT evidence of superiority** missing; Scenario-4 is straw-man (1.4 Mbps PCM through 200 kbps); MIDI-keyboard-only scope caveat missing (no voice/violin); autotune claim is in title but unevaluated; no end-to-end latency measurement | 2026-04-23 |
| **P-07** | Shallow (Gemini Flash) | **RE-INGESTED** | **n=0 human participants** caveat missing; latency numbers are arithmetic formulas + ping tests, NOT measured on audio pipeline; "empirical evidence for E(t) Professional Flow" is Project-8 projection; no actual Global South deployment; spectral comparison is Audacity visual only (no SNR/THD); 5-page derivative paper, primary JackTrip sources should be Cáceres & Chafe 2010 / Bosi et al. 2021 | 2026-04-23 |
| **P-08** | Shallow (Gemini Flash) | **RE-INGESTED** | Dataset specifics (n=2,992 clips, 528 raters, 30 sessions) missing; per-condition ROC-AUC missing (Fluidity best .815, Enjoyment best .874); body-motion GC contribution is minimal (ΔAUC <.01) and authors flag 7-s window as too short; VGGish > Wav2Vec2 finding missing; **domain caveat missing** (conversational, not musical); all t-values for event-pair comparisons absent | 2026-04-23 |
| **P-11** | Shallow (Gemini Flash) | **RE-INGESTED** | Inter-chorister timing (83 ms ± 57 ms home, 47 ms ± 46 ms univ) missing; χ² CLMM analysis and post-hoc tests absent; n=23 amateur caveat missing; "significant jump at 100 ms and leap below 85 ms" is qualitative pattern, NOT statistically validated phase transition; 100 ms is a design target, not empirical cliff; inability to isolate audio vs. video contribution to Jamulus@Univ advantage | 2026-04-23 |
| **P-15** | Shallow (Gemini Flash) | **RE-INGESTED** | Exact latency CDFs (99.3/92.8/98.1%) and BLER (0.08) missing; burst-error max length 151 packets missing; **"latency significantly increases with nodes/traffic" is a positive finding, not a null** (prior digest got this backwards); WAN-not-included scope limit missing; "5G is viable for E(t) ≈ 1" is Project-8 extrapolation that REVERSES authors' own conclusion ("current 5G needs to improve for NMP"); UR-LLC not activated in test | 2026-04-23 |
| **P-23** | Shallow (Gemini Flash) | **RE-INGESTED** | **Latency confound critical**: Baseline 144 ms A2S vs. XRE 74 ms — NOT "comparable" as prior digest stated. XR QoE advantage is confounded with lower latency; exact F-statistics (Immersion F=11.56, Social Presence F=9.819 p<.001) missing; tempo-deceleration/acceleration finding missing (XREs decelerate, baseline accelerates); 83% male demographics caveat missing; dyadic clapping task not choir; "Modality Weighting W_m" is Project-8 speculation | 2026-04-23 |
| **S-01** | Shallow (Gemini Flash) | **RE-INGESTED** | Claude Sonnet AI co-authorship absent; book-not-journal-article distinction missing; "S-01 defines the Entanglement Index" is false (S-02 does); "Planetary Qi" is philosophical not technical; most chapters are non-human organisms — only Ch. 14 is directly Project-8-relevant; alchemical-stage mapping is metaphor-structure, not empirical model | 2026-04-23 |
| **S-04** | Shallow (Gemini Flash) | **RE-INGESTED** | S-04 and P-09 are the SAME STUDY (S-04 = full ISMAR paper, P-09 = VRW abstract) — relationship missing from both digests; Task × Latency interaction F=2.61 p=.014 η²=.10 missing; focus-shift non-significance missing ("players noticed less because they prioritized audio" is oversimplified — interaction is non-monotonic); "AR animation Sensory Integration Window is wider than raw video" is Project-8 over-reach not in paper; MIDI tempo variability analysis absent; 1200 ms tolerance is cycle-confound artifact | 2026-04-24 |
| **P-03** | Shallow (Gemini Flash) | **RE-INGESTED** | "30+ FPS" understates (actually 102 Full / 312 Lite); prior digest reversed AR PCK result (BlazePose loses on AR 84.1 vs OpenPose 87.8); **"hallucinates joints behind folder" is over-reach** (paper's visibility classifier flags inaccuracy, does not reconstruct); head-visibility-required constraint missing (critical for choir); PCK@0.2 ~10cm error caveat missing; single-person-only scope missing | 2026-04-24 |
| **P-05** | Shallow (Gemini Flash) | **RE-INGESTED** | CER numbers (MLCA 21.8/24.1/30.6; VSR-only 84+%) missing; Chinese-TV-room domain caveat missing; **"reconstruct vocal timing and pitch from lip motion in Blind Audio conditions" is false** (VSR-only CER is 84%; lip-reading alone is nearly useless); 105M params not real-time; "Multi-modal Synchronization Index" is not in paper | 2026-04-24 |
| **P-10** | Shallow (Gemini Flash) | **RE-INGESTED** | 2-page workshop abstract caveat missing; n=11 missing; **median distance 0.29 km — not a true remote test** — missing; single-song (Amazing Grace) missing; no inferential stats (Likert medians only); direct Zoom comparison is future work not in paper; "Visual Gaze Index V_g(t)" is Project-8 speculation | 2026-04-24 |
| **P-16** | Shallow (Gemini Flash) | **RE-INGESTED** | **Projector hardware requirement is disqualifying** — prior digest claimed "webcam-only, mobile or home settings" which is wrong; "Pre-attack Breath via webcam" is false — method requires structured-light projector on bare chest; n=18, steady-state only, no singing data; only Pearson r, no Bland-Altman; 4 of 24 dots used | 2026-04-24 |
| **P-17** | Shallow (Gemini Flash) | **RE-INGESTED** | **China-policy-paper caveat** missing (not a German-law authority); §60d UrhG absent from paper — Project 8's actual statutory basis is not addressed; performer-rights + GDPR biometric issues are separate from copyright and not covered; EU DSM Art. 3 vs. Art. 4 distinction blurred; US fair-use over-simplified; 4-page non-IP-venue caveat missing | 2026-04-24 |
| **P-18** | Shallow (Gemini Flash) | **RE-INGESTED** | 23-camera studio rig requirement missing (disqualifying for Project 8 home scenarios); exact MPJPE numbers (DWPose 17.00 → HPE+Audio 14.93 mm; Contact Deviation 22.40 → 5.19 mm = 76.8% improvement) missing; **"Vocal F0 refines Mouth/Larynx tracking" is a false analogy** (hand-string contact has geometric mapping, voice does not); monophonic-only caveat missing; DWPose-as-SOTA (not MediaPipe) framing missed | 2026-04-24 |
| **P-19** | Shallow (Gemini Flash) | **RE-INGESTED** | MPJPE numbers (44.22 mm at 3-s input, 5.40% over SOTA) missing; 35-dim audio-feature set (not just "Vocal Energy") missing; **"Vocal Energy drives laryngeal/facial dynamics" is false analogy** — in violin, visible limbs cause sound; in voice, internal vocal folds cause sound; 4-camera calibrated training setup for monocular inference (not home webcam); 30-fps vibrato-tracking marginal | 2026-04-24 |
| **P-20** | Shallow (Gemini Flash) | **RE-INGESTED** | **"+31% cpCER improvement in dictionary matching" is fabricated** (cpCER is P-05's speech metric, not in P-20); "Shoulder-Anchor Scaling" is from related work (Fragkiadakis), not P-20's contribution; domain-transfer-to-choir claim overstated; dominant-hand accuracy (0.96/0.94) missing; 10,321 + 7,963 dataset sizes missing; 50-keypoint / 2D-only caveat missing | 2026-04-24 |
| **S-03** | Shallow (Gemini Flash) | **RE-INGESTED** | **"Success is 80% dependent on hardware" is fabricated** (no percentage in paper); comparative-latency table ("Low", "Extremely Low") invented (paper uses qualitative descriptors only); "best-for" pairings invented; not-peer-reviewed / grey-literature caveat missing; Janine-Hacker-as-Project-8-supervisor context missed; no jitter-profile analysis in paper | 2026-04-24 |
| P-01 | — | See row above | — | — |
| P-02 | — | See row above | — | — |
| P-03 | — | See row above | — | — |
| P-05 | — | See row above | — | — |
| P-06 | — | See row above | — | — |
| P-07 | — | See row above | — | — |
| P-08 | — | See row above | — | — |
| P-09 | — | See row above | — | — |
| P-10 | — | See row above | — | — |
| P-11 | — | See row above | — | — |
| P-13 | — | See row above | — | — |
| P-14 | — | See row above | — | — |
| P-15 | — | See row above | — | — |
| P-16 | — | See row above | — | — |
| P-17 | — | See row above | — | — |
| P-18 | — | See row above | — | — |
| P-19 | — | See row above | — | — |
| P-20 | — | See row above | — | — |
| P-21 | — | See row above | — | — |
| P-22 | — | See row above | — | — |
| P-23 | — | See row above | — | — |
| S-01 | — | See row above | — | — |
| S-02 | — | See row above | — | — |
| S-03 | — | See row above | — | — |
| S-04 | — | See row above | — | — |
| P-04 | TO-ACQUIRE | Not in raw/ | — | — |

## Per-Paper Entries

### P-12 Exploiting Latency In NMP (Liloia & Dannenberg 2025)

**Deep-read date**: 2026-04-23
**Raw path**: `raw/01_primary_sources/Exploiting Latency In The Design Of A Networked Music.pdf`
**Extraction**: 591 lines / 7,483 words via `pdftotext -layout` → `.cache/p12_extract/p12.txt`
**Full digest**: [[p_12_exploiting_latency]]

**Corrections table**:

| # | Location | Prior Claim | Paper Ground Truth | Severity |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [[p_12_exploiting_latency]] §Key Concepts | "To combat jitter (variation in latency), the system imposes a set tempo and intentionally adds extra latency..." | FTA does not combat jitter; it extends latency so jitter is absorbed within the scheduled slot. Paper phrasing: "extends latency to avoid jitter" [p. 2, §2.2.1]. | MEDIUM (imprecise mechanism) |
| 2 | [[p_12_exploiting_latency]] §Key Concepts | (topology not stated) | Hub-and-spoke: central server routes, stores, arbitrates, maintains master clock [p. 4, §4.1]. | MEDIUM (missing architectural fact) |
| 3 | [[p_12_exploiting_latency]] §Overview | (no numerics beyond 3.5 s) | Λ=3500 ms default, 68 BPM max tempo, 2·Λ/Λ asymmetric display delays, 75 ms audio-only threshold, 350 ms Google Cloud median RTT [p. 2, §2.2.1; p. 4, §4.2; p. 5, §4.6.1, §4.6.2]. | MEDIUM (incomplete raw data) |
| 4 | [[p_12_exploiting_latency]] §Overview | "informal testing" | n=3, one session, three rounds, no quantitative evaluation, no effect sizes, no UX instrument [p. 6, §5.1]. | HIGH (missing epistemic caveat; anyone citing this paper for a latency-tolerance claim needs to know n=3). |
| 5 | [[p_12_exploiting_latency]] §Relevance to E(t) | "In our Tier 3 latency-injection tests, we expect... unless performers adopt a structured FTA-style coping mechanism." | P-12 does not measure E(t) or any coupling metric. This is Project-8 extrapolation, not a P-12 finding. | HIGH (projection of our claim onto paper). |
| 6 | [[fake_time_approach]] §Mechanism | "when network delay exceeds the threshold for natural human synchronization (typically > 150ms)" | 150 ms threshold is not in [[p_12_exploiting_latency]]. Paper cites 75 ms as audio-only two-way upper bound [p. 2, §2.2.1]. The 150 ms number must be sourced elsewhere (pending P-09 / P-11 re-ingest) or removed. | MEDIUM (unsourced number traced to wrong paper) |
| 7 | [[fake_time_approach]] §Mechanism | "exactly one full measure" | Paper requires precedent time ≥ Λ and an integer multiple of one musical cycle, not exactly one measure. Default ν=4 beats [p. 2, §2.2.1; p. 5, §4.6.1]. | LOW (oversimplified but not wrong direction) |
| 8 | [[latency_as_feature]] §Design Implementations | "Spatialization: Using delays of 50-100ms to simulate acoustic reflections in a large virtual room" | Conflated spatial-diffusion parameter mapping (Chafe 2003) with generic reverb simulation. Actual P-12 §2.3 cites three mechanisms: pitch (Chafe et al. 2002), spatial diffusion parameters (Chafe 2003), ~100 ms echo (Rebelo & King 2010) [p. 3, §2.3]. | LOW (slight reframe) |
| 9 | [[latency_as_feature]] §Design Implementations | "Forced Asymmetry: Using latency to enforce specific roles" | Roles (Composer/Performer/Listener) exist for UI and musical-responsibility reasons [p. 3, §3.1; p. 3-4, §3.3]. The asymmetric latency is the 2·Λ / Λ display delay [p. 5, §4.6.2], not role enforcement. | MEDIUM (wrong causal direction) |
| 10 | [[nmp_platform_comparison]] | P-12's hub-and-spoke regime absent from comparison | Added as new third category alongside P2P and client-server. | MEDIUM (missing a relevant topology class) |

**Out-of-scope for this audit but flagged for future**:

- [[latency_thresholds]] cites 85 ms / 150 ms / 320 ms thresholds. None are traced to P-12. These thresholds should be re-verified against [[p_11_chamber_choir]], [[p_09_how_late]], [[s_03_choirathome_tools]] during those papers' Tier-A / Tier-B deep reads.

**Cascade summary**: 4 existing pages rewritten ([[p_12_exploiting_latency]], [[fake_time_approach]], [[latency_as_feature]], [[nmp_platform_comparison]]), 1 new audit page created ([[deep_read_audit]]). Rule 1 satisfied (5 content pages touched). Log entry in [[log]].

### S-02 Entanglement — A new dynamic metric to measure team flow (Gloor, Zylka, Fronzetti Colladon, Makai 2022)

**Deep-read date**: 2026-04-23
**Raw path**: `raw/02_secondary_sources/'Entanglement' – A new dynamic metric to measure team flow.pdf`
**Extraction**: 895 lines / 10,981 words via `pdftotext -layout` → `.cache/extracts/s02.txt`
**Full digest**: [[s_02_entanglement]]

**Corrections table**:

| # | Location | Prior Claim | Paper Ground Truth | Severity |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [[s_02_entanglement]] §Key Concepts | (no formulas given) | Eqs. 2, 4, 5, 7, 8 given verbatim in paper: $E_A = C_D(x) \cdot C_D(y) / d(A(x), A(y))$, $E_B$ analogous with $C_B$, $E_{GB} = C_{GB} / d(C_B, C_{GB})$. Time window = 7 days. | HIGH (definitional source for Project 8 E(t); formulas must be present) |
| 2 | [[s_02_entanglement]] §Findings | "positively correlates with team performance" | Case A: r=.615 p=.045; r=.707 p=.015. Case B: t=-2.513 p=.013, CatBoost acc=80.25% AUC=0.81. Case C: t=2.432 p=.017, CatBoost acc=74.73% AUC=0.68. Case D: r=.522 p=.002, multilevel model reduces L2 variance 30.56%. | HIGH (effect sizes determine whether this supports "strong" or "suggestive" predictor language) |
| 3 | [[s_02_entanglement]] §Overview | No domain caveat | All four case studies are **email** in knowledge-work organizations, 7-day windows, n=53/113/81/82. No music, no audio, no body signals, no real-time data. | HIGH (Project 8 applies this metric across a domain boundary; caveat is load-bearing for honest citation) |
| 4 | [[s_02_entanglement]] authorship | "Gloor et al." | Gloor (MIT), **Zylka (Uni Bamberg)**, Fronzetti Colladon (Uni Perugia), Makai (Galaxyadvisors). Zylka is at our home institution; potentially reachable for clarification or collaboration. | LOW (editorial) but tactically useful |
| 5 | [[s_02_entanglement]] §Relevance | "Team Flow/Virtual Mirror: we will also apply this concept to our own team's WhatsApp interactions to measure our own groupflow." | This is Project-8 extrapolation, not a finding. The paper discusses smart-wearables as "future work" but does not validate body-signal entanglement. | MEDIUM (claim projection onto source) |

**Out-of-scope for this audit but flagged**:

- [[entanglement_index]] already flags the "asynchronous → real-time" adaptation but does not explicitly state the dataset-size / time-window / domain mismatch. Minor strengthening deferred to a later LINT pass or during P-13 deep read (which provides the physical-entrainment framing currently cited).
- [[Peter_Gloor]] entity page should cross-reference the Gloor publication chain: S-01 (Cybernetic Alchemy), S-02 (this paper), Gloor 2017 Sociometrics. Deferred to LINT.

**Cascade summary**: 1 page rewritten ([[s_02_entanglement]]); 1 audit entry appended; [[deep_read_audit]] status table updated. Rule 1 relaxed: this is a re-ingest (not a new ingest), and the affected concept/synthesis pages ([[entanglement_index]], [[Peter_Gloor]]) are either already aligned or queued for LINT.

## Protocol for Future Entries

Each subsequent Tier-A/B/C deep-read appends a new `### <ID>` subsection to the "Per-Paper Entries" section above, following the same template:

1. Deep-read date, raw path, extraction stats, full-digest wikilink.
2. Corrections table (# / location / prior claim / paper ground truth / severity).
3. Out-of-scope flags (claims in the wiki that need future audits).
4. Cascade summary (pages touched, Rule 1 compliance).

The status table at the top is updated in-place as each audit completes.
