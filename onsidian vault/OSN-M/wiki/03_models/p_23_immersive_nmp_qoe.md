---
title: P-23 Immersive NMP QoE
type: source
alchemy_stage: nigredo
tags: [nmp, immersive, xr, qoe, spatial_audio, irene, deep_read]
ingested_date: 2026-04-23
last_deep_read: 2026-04-23
source_count: 1
related: ["[[perceived_coherence_index]]", "[[perceptual_delay_masking]]", "[[p_10_vrchoir_system]]", "[[deep_read_audit]]"]
team_take: XR outperforms 2D video on subjective QoE but the comparison is confounded — baseline has 144 ms A2S latency vs. 74 ms for XREs, so the "XR advantage" may partly be a lower-latency advantage. Clapping-only task, 83% male, not choir.
---

# P-23 Immersive Networked Music Performance: Impact of Extended Reality on the Quality of Experience

**Citation**: Hupke, R., Preihs, S., Peissig, J. (2024). In *2024 IEEE 5th International Symposium on the Internet of Sounds (IS2)*. [DOI:10.1109/IS262782.2024.10704092](https://doi.org/10.1109/IS262782.2024.10704092).
**Affiliations**: Leibniz University Hannover (LUH), Institute of Communications Technology (IKT). Hupke also at Sennheiser.
**System**: IRENE (Immersive Room ExtensioN Environment).
**raw path**: `raw/01_primary_sources/Immersive_Networked_Music_Performance_Impact_of_Extended_Reality_on_the_Quality_of_Experience.pdf`

## 1. Setup (§II-A, Fig. 1, Table I)

**Hardware stack**:

- Motion capture: Motive tracking, 7 cameras per room
- Audio: analog wireless lavalier + open headphones (Sennheiser HD650)
- Rendering: Unreal Engine (visual) + Max/MSP (audio)
- Control/analysis: MATLAB, synchronized with audio via OSC/Dante
- Video: RTSP server/client for low-latency streaming

**4 XRE conditions**:

| Acronym | Description | Room acoustics | A2S latency | Audio mode |
| :--- | :--- | :--- | :--- | :--- |
| **VEFree** | Free-field | direct + 1 floor reflection | **74 ms** | binaural |
| **VEHall** | Concert hall | T30 = 2.05 s | **74 ms** | binaural |
| **VEIML** | Listening room | T30 = 0.46 s | **74 ms** | binaural |
| **Baseline** | Traditional video | — | **144 ms** | monaural |

**Audio one-way delays** (buffer 128 samples @ 48 kHz):

- Binaural: system 11 ms, remote 21 ms
- Monaural: system 700 µs, remote 10 ms

**Key confound**: Baseline has **higher A2S latency (144 ms)** but **lower audio OWD (10 ms vs. 21 ms)**. The two rendering modes are not latency-matched.

## 2. Participants

- **36 individuals = 18 pairs** [§II-B]
- **6 female / 30 male** (83% male, gender imbalance)
- Mean age: 29
- Mean musical experience: 11 years
- Recruited from IKT audio-enthusiasts + external musicians (≥5 years experience required)

## 3. Task

Complementary rhythm clapping: quarter + two eighth notes, Leader/Follower roles [Fig. 2]. 45+ seconds per trial. Each XRE completed in randomized order after 60 s exploration.

## 4. Raw Data Block

**Objective metrics** (F(3, df), linear mixed-effect with XRE fixed, participants random, Tukey post-hoc):

| Metric | Statistic | Finding |
| :--- | :--- | :--- |
| Asymmetry | n.s. main effect | No significant differences [§III-A] |
| Imprecision | n.s. main effect | No significant differences [§III-A] |
| **Mean Tempo Slope** | F(3, 45.296) = **8.048**, p < .001 | Baseline slight **acceleration**; all XREs **deceleration** [§III-A] |
| **Pacing** | F(3, 44.979) = **10.21**, p < .001 | Baseline higher than starting tempo; XREs lower [§III-A] |

**Subjective metrics** (F(3, 105), same model):

| Item | Statistic | Direction |
| :--- | :--- | :--- |
| Consistency | n.s. | Trend toward VEIML + VEHall > VEFree and Baseline |
| Social Presence | F = **9.819**, p < .001 | VEIML + VEHall > Baseline (p < .001) |
| Immersion | F = **11.56**, p < .001 | VEIML + VEHall > Baseline (p < .001); VEHall > VEFree (p < .05) |
| Naturalness | F = **6.687**, p < .001 | VEHall > VEFree + Baseline (p < .01); VEIML > Baseline |
| Responsiveness | F = **10.68**, p < .001 | VEIML + VEHall > Baseline; VEHall > VEFree (p < .01) |
| Localization | F = **10.09**, p < .001 | All 3 XREs > Baseline (p < .001, .001, .01) |
| Separation | F = **3.933**, p < .05 | All 3 XREs > Baseline |
| Delay | F = **6.021**, p < .001 | All 3 XREs perceived LESS delay than Baseline |

## 5. Limitations

**Stated** [§IV Discussion, §V Conclusion]:

- Inability to isolate visual vs. auditory rendering contributions; experimental design doesn't separate them [§IV].
- Tendency: longer reverberation time may negatively impact musical performance while improving perceived QoE (VEHall highest tempo deceleration).
- "Difficult to draw a conclusion about the influence of the individual components."
- Future work: separate visual and auditory components, test additional instruments and rhythmic complexities.

**Implicit (binding on Project 8 citation)**:

- **Latency confound**: Baseline has 144 ms A2S vs. 74 ms for XREs. All "XR > baseline" QoE differences are **confounded with lower latency** in the XRE conditions. Cannot attribute to XR specifically.
- **Gender imbalance**: 83% male. QoE and coordination effects may differ for female majority.
- **Music-enthusiast recruiting**: not general population.
- **Dyadic clapping task**: percussive, 2 people only. Does not generalize to choral singing, large ensembles, sustained tones.
- No comparison with audio-only low-latency baseline (e.g., Jamulus) — the "no video" condition is absent.
- No objective musical coordination metrics beyond rhythm-onset ones (no PLV, no phase coupling).
- Subjective Likert on continuous scale -5 to +5 is uncommon; interpretation may differ from standard Likert.
- Headphones are open-backed, allowing some acoustic leakage — may partially undermine spatial-audio isolation.

## 6. Relevance to Project 8 E(t)

**P-23 is relevant for**:

- **[[perceived_coherence_index]]**: provides subjective-rating precedent for "coherence" and "social presence" in NMP.
- **Effect size ballpark**: F-statistics for Immersion (F=11.56), Localization (F=10.09), Responsiveness (F=10.68) are large. If Project 8's VR/XR Tier yields similar magnitudes, results would be publishable.
- **Latency-perception insight**: "Perceived Delay" was lower in XREs, even though their A2S was 74 ms (vs. 144 ms Baseline). This supports [[perceptual_delay_masking]] — but see latency-confound caveat.
- **Tempo-deceleration finding**: XREs with reverberation induce deceleration relative to baseline. Relevant for [[latency_thresholds]] and tempo-stability discussions.

**P-23 is NOT**:

- Evidence that XR reduces **objective** performance impairment (objective asymmetry and imprecision were n.s. across all conditions).
- Evidence for any specific "Modality Weighting W_m" scheme (Project-8 extrapolation, not P-23 finding).
- Applicable to choral singing (dyadic clapping only).
- Clean test of XR independent of audio rendering — confounded design.

## 7. Corrections Logged Against Prior Digest

See [[deep_read_audit]] for full table. Summary:

| Issue | Prior claim | Corrected reading |
| :--- | :--- | :--- |
| Missing latency confound | "Latency Illusion: Participants perceived lower delay in XR environments than in 2D video, despite technical latencies being comparable" | **Baseline A2S = 144 ms, XREs = 74 ms** [Table I]. Latencies are NOT comparable. The lower perceived delay is confounded with actual lower latency. Only audio OWD (10 ms monaural vs. 21 ms binaural) goes the opposite direction. Cannot claim perceptual masking without latency-matched comparison. |
| Missing exact F-statistics | "XR significantly improves the 'Social Presence' and 'Naturalness'" | Social Presence: F(3, 105) = 9.819, p < .001; Immersion: F = 11.56, p < .001; Naturalness: F = 6.687, p < .001; Responsiveness: F = 10.68; Localization: F = 10.09; Separation: F = 3.933, p < .05 [§III-B]. Not just "significantly improves" — effect sizes are large. |
| Missing tempo-deceleration finding | "Objective rhythm metrics (Asymmetry, Imprecision) remained stable" | Asymmetry and Imprecision n.s., BUT Mean Tempo Slope F=8.048 p<.001 and Pacing F=10.21 p<.001 both significant: XREs **decelerate** while baseline **accelerates** [§III-A]. Objective outcome is NOT stable for tempo. |
| Missing n and demographics | (not stated) | 36 participants = 18 pairs; 83% male (6F/30M); mean age 29; mean 11 years music experience [§II-B]. |
| Missing dyadic clapping caveat | Implied choir-relevant | Task is dyadic clapping, not choral singing. No sustained tones, no ensemble >2, no SATB voices [§II-C]. |
| "Our entanglement metric should therefore include a Modality Weighting W_m" | — | This is Project-8 extrapolation, not a P-23 finding or recommendation. P-23 neither proposes nor validates weighting schemes. Moved to §6 as labeled application, not paper claim. |
| Missing "latency-matched comparison absent" | (no mention) | No audio-only low-latency baseline tested (e.g., Jamulus). Cannot separate XR contribution from latency contribution [§IV]. |
| Missing future-work: separate visual/auditory | (no mention) | Authors explicitly flag this as next step; their own design can't separate contributions [§IV, §V]. |
