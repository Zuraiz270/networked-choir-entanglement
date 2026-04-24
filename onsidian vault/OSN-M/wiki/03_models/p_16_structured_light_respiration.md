---
title: P-16 Structured Light Respiration
type: source
alchemy_stage: nigredo
tags: [respiration, structured_light, non_contact, computer_vision, choral_physiology, deep_read]
ingested_date: 2026-04-23
last_deep_read: 2026-04-24
source_count: 1
related: ["[[respiratory_synchrony]]", "[[breathing_desync]]", "[[vocal_entrainment]]", "[[deep_read_audit]]"]
team_take: 3-page short paper from National University of Mongolia. Requires a structured-light **projector** — not applicable to home webcam setups. n=18, steady-state breathing, NOT singing. Not directly usable for Project 8's webcam-only choir setup.
---

# P-16 A New Approach for Non-Contact Automated Measurement of Respiration Rate Using Structured Light

**Citation**: Dagdanpurev, S., Davaasuren, D., Enkhjargal, A., Renchin-Ochir, A. (2024). In *2024 IEEE 9th International Conference on Data Science in Cyberspace (DSC)*, pp. 798 to 801. [DOI:10.1109/DSC63484.2024.00120](https://doi.org/10.1109/DSC63484.2024.00120).
**Affiliation**: Department of Electronics and Communication Engineering, National University of Mongolia, Ulaanbaatar.
**raw path**: `raw/01_primary_sources/A_new_approach_for_non-contact_automated_measurement_of_respiration_rate_using_structured_light.pdf`

## 1. Method (§II)

Requires a **structured light projector** projecting 24 non-overlapping RGB dot patterns onto the participant's chest. Webcam records 10 seconds. MATLAB tracks dot centroids, extracts position signal, peak-detects breaths.

**Hardware**:

- Samsung SP-H03 Pico Projector
- Logitech C270 HD Webcam
- Lenovo ThinkPad X1 laptop
- MATLAB signal processing

**Pipeline** [§II-A, Fig. 3]:

1. Extract 150 frames from 10-s video (15 fps)
2. rgb2gray + threshold + regionprops → detect 24 white dots
3. Index and track centroid positions
4. Only **4 dots (indices 10, 11, 16, 17)** in abdominal area used
5. Peak detection → breaths/min = peaks × 6 (since 10 s window)

## 2. Evaluation

- **n = 18** participants, ages **5 to 45**
- Manual breath counting as reference (medical professional using counter)
- Steady-state breathing while seated
- Shirtless (Fig. 1 shows participants with bare chest or thin clothing)

## 3. Raw Data Block

| Metric | Value | Source |
| :--- | :--- | :--- |
| Correlation coefficient (proposed vs. manual) | **r = 0.91** | [§III, Conclusion] |
| p-value | **[NOT-REPORTED]** | — |
| Bland-Altman / MAE / RMSE | **[NOT-REPORTED]** | — |
| Sample size | 18 | [§III] |
| Recording window | 10 s | [§II-B] |
| Frames per video | 150 (15 fps) | [§II-B] |
| Dots projected | 24 | [§II-A] |
| Dots actually used | 4 (abdominal) | [§III] |

## 4. Limitations

**Stated** [§IV]:

- "In future, we will develop a method to detect pneumonia." (indicates intended use is clinical vital-sign monitoring, not music.)
- No other limitations explicitly stated.

**Implicit (binding on Project 8 citation)**:

- **Requires a physical projector** pointed at the chest. Home NMP setups have cameras but not projectors. **This hardware requirement is disqualifying for Project 8's webcam-only Tier 2/3 scenarios.**
- **Steady-state breathing** only, not singing. During choral performance, breathing is intentional, variable, and coordinated with musical phrases — the 10-second steady-state measurement model does not apply.
- **Shirtless / thin clothing** required for visible dot displacement; not feasible for clothed choir singers.
- **n = 18**, ages 5-45, single ethnic/demographic sample (Mongolian university population).
- **Only Pearson r = 0.91** reported. No Bland-Altman, MAE/RMSE, individual variance, or validation against gold-standard (belt / spirometer). r=0.91 can hide systematic bias.
- **10-second window** too short for phrase-level respiratory tracking in singing.
- Only 4 of 24 dots actually used — paper does not justify why the other 20 were discarded.
- No real-time implementation; MATLAB batch processing.
- No robustness analysis for ambient lighting, movement artefacts, or camera angle.
- Short 3-page conference paper; limited methodological depth.

## 5. Relevance to Project 8 E(t)

**P-16 is NOT directly useful for Project 8** because:

- Requires projector hardware unavailable to home singers.
- Measures resting respiration, not phrase-coordinated singing breath.
- Not validated on singers or any performance scenario.

**Alternative approaches Project 8 should consider**:

- **Remote photoplethysmography (rPPG)**: from RGB video alone, extracts subtle skin-color oscillations → respiration rate. Widely researched, webcam-compatible.
- **Pose-estimation-based chest tracking**: extract chest keypoint from MediaPipe Pose, track sub-cm vertical motion. No projector needed.
- **Audio-derived respiration**: inhalation phase detectable in breath noise before phrase onset.

**P-16 contribution to Project 8**:

- **Reference for [[respiratory_synchrony]]** conceptually — confirms that non-contact respiration measurement is tractable in principle.
- **[[breathing_desync]]** framing: the 4-dot abdominal-area tracking suggests that chest motion is rich in respiratory signal.
- **Not a source for any claim about choir breathing** specifically.

## 6. Corrections Logged Against Prior Digest

See [[deep_read_audit]] for full table. Summary:

| Issue | Prior claim | Corrected reading |
| :--- | :--- | :--- |
| **"Feasible for rapid, non-contact vital sign monitoring in mobile or home settings"** | — | **Wrong**. Requires a **structured light projector** (not standard in mobile or home setups). "Non-contact" does NOT mean "webcam-only" — the method explicitly needs a projector [§II-A]. |
| Missing hardware requirements | "a simple web camera and a structured light projector" is mentioned | The projector is **disqualifying** for Project 8 webcam-only scenarios. Prior digest did not flag this as a problem. |
| Missing evaluation caveats | "Correlation coefficient of 0.91 with manual reference counts" | n = 18, ages 5-45; single steady-state measurement; only Pearson r, no Bland-Altman, no MAE. r=0.91 can hide systematic bias. |
| **"P-16 allows us to track the 'Pre-attack Breath' — the synchronous inhalation of singers before a musical phrase — using only their webcams"** | — | **False**. Requires projector. Not webcam-only. Never tested on singers. Pre-attack breath dynamics are not steady-state; method is not designed for phrase-level events. Prior digest mis-represents both the hardware requirement and the applicable regime. |
| Missing "shirtless / thin clothing" constraint | (not stated) | Figures show bare-chest participants; dot pattern needs visible skin for displacement. Clothed choir singers would not work. |
| Missing small-sample / steady-state-only caveat | (not stated) | n=18, 10-s windows, no phrase-level resolution, no singing data [§II-B, §III]. |
| Missing alternative-method recommendation | — | Project 8 should use rPPG or pose-based chest tracking instead of P-16's projector method (added in §5). |
