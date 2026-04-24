---
title: Limitations Register
type: synthesis
alchemy_stage: rubedo
tags: [risks, limitations, ebse, science, deep_read]
ingested_date: 2026-04-23
last_updated: 2026-04-24
source_count: 9
related: ["[[p_13_human_sync_review]]", "[[p_22_augmented_granger_causality]]", "[[entanglement_index]]", "[[s_02_entanglement]]", "[[p_11_chamber_choir]]", "[[p_23_immersive_nmp_qoe]]", "[[deep_read_audit]]"]
team_take: "The 'Honesty' file. Every research project has cracks; we document ours here to ensure our claims are scientifically robust."
---

# Limitations Register

The **Limitations Register** tracks the known boundaries and potential failure modes of the SNA-OSN-M research methodology. Paper-specific correction entries (§4-§5) were added 2026-04-24 from the deep-read audit cascade; see [[deep_read_audit]] for full per-paper tables.

## 1. Technical Limitations (Audio/DSP)

- **Crosstalk/Bleed**: High-sensitivity microphones in ensemble settings may capture adjacent singers, confounding F0 extraction.
- **Polyphonic Mixing**: YouTube stereo mixes prevent per-singer audio analysis; ensemble spectral flux is used as a proxy.

## 2. Statistical Limitations (Causality)

- **Stationarity**: Granger causality requires stationary time-series; musical phrasing (crescendo/diminuendo) often violates this.
- **Sample Size**: While Tier 3 provides 150+ observations, natural Tier 2 data remains limited (Dagstuhl N ≈ 10).

## 3. Computer Vision Limitations

- **Occlusion**: Overlapping singers or instrument placement may break joint visibility.
- **Biometric Noise**: Low webcam resolution may mask subtle respiratory micro-motions (breathing).

## 4. Domain-Transfer Limitations (deep-read cascade, 2026-04-24)

- **L-4.1 — S-02 entanglement formula validated on email, not music**: [[s_02_entanglement]] case studies (A-D) all used **email data with 7-day windows**, n=111-113 per case, modest effect sizes (Pearson r .522-.707 where significant). Our adaptation to continuous choir audio + pose + breath streams at seconds-scale windows is a **novel domain transfer with no prior validation**. Affects: [[entanglement_index]] provenance claims.
- **L-4.2 — P-18 / P-19 false causal-audiovisual analogy**: [[p_18_audio_guided_mocap]] and [[p_19_viopose_4d]] guide pose estimation for **string instruments** where visible limb motion and audio have a direct geometric-contact mapping. For voice, the sound source (vocal folds) is internal and not visible. A "Vocal F0 refines mouth/larynx tracking" pipeline does not generalize. Affects: any V(t) design tempted to use audio as a pose prior.
- **L-4.3 — P-16 respiration requires structured-light projector**: [[p_16_structured_light_respiration]] method requires **projector hardware** on bare chest and does not support webcam-only breath detection. Our shoulder-rise proxy for breathing remains unvalidated against any peer-reviewed breath-detection standard.
- **L-4.4 — P-20 sign-language-to-choir domain transfer is limited**: [[p_20_mediapipe_preprocessing]] dominant-hand identification (0.96 / 0.94 accuracy) relies on articulated hand motion; choir singers have minimal hand motion. Only the interpolation and handedness concepts generalize; the core pipeline does not.
- **L-4.5 — P-17 copyright paper is a China-policy paper**: [[p_17_copyright_tdm]] is 4 pages in a non-IP venue analyzing Chinese TDM exceptions. It is **not an authority on §60d UrhG or EU DSM Art. 3**, which is Project 8's actual statutory basis. Use [[data_sourcing_policy]] for German-jurisdiction compliance reasoning.

## 5. Experimental Confound Limitations (deep-read cascade, 2026-04-24)

- **L-5.1 — P-23 XR QoE confounded with latency**: [[p_23_immersive_nmp_qoe]] reports baseline Audio-to-Speaker (A2S) latency 144 ms vs XRE latency 74 ms. The reported immersion / social-presence advantages for the XR condition (Immersion F=11.56, Social Presence F=9.819, p<.001) are **confounded with a 70 ms latency reduction**. We cannot cite P-23 as evidence that XR improves QoE at equal latency.
- **L-5.2 — P-11 "100 ms" is a design target, not a phase transition**: [[p_11_chamber_choir]] measures inter-chorister timing at 83±57 ms (home) and 47±46 ms (university); the authors do not run a phase-transition analysis. 100 ms is Jamulus's engineering design target, not an empirical coordination cliff. Affects: [[latency_thresholds]].
- **L-5.3 — P-09 / S-04 "1200 ms tolerance" is a cyclic-confound artifact**: The 1200 ms test condition happens to align with the repeating-rhythm task cycle, making delay appear non-disruptive. This is not a ceiling on free-rhythm tasks.
- **L-5.4 — P-10 "remote" framing misleading**: [[p_10_vrchoir_system]] n=11, median participant-pair distance 0.29 km — not a true remote test; single-song (Amazing Grace); Likert medians only, no inferential stats.

## Related

- [[p_13_human_sync_review]]
- [[latency_thresholds]]
- [[non_linear_causal_leakage]]
- [[deep_read_audit]]
- [[s_02_entanglement]]
- [[p_11_chamber_choir]]
- [[p_23_immersive_nmp_qoe]]
