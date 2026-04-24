---
title: P-13 Human Synchronization Review
type: source
alchemy_stage: nigredo
tags: [review, synchronization, datasets, sms, fair_data, deep_read]
ingested_date: 2026-04-23
last_deep_read: 2026-04-23
source_count: 1
related: ["[[hyperscanning]]", "[[entanglement_index]]", "[[vocal_entrainment]]", "[[deep_read_audit]]"]
team_take: Authoritative catalog of 101 synchronization datasets. Explicitly flags the annotation and standardization gap Project 8 is trying to address. Musical-performance sub-cluster (26%) overlaps Project 8's Tier 2 target.
---

# P-13 A Review of Human Synchronization Datasets

**Citation**: Velletaz, T., Janaqi, S., Harispe, S., Lagarde, J., Guyot, P. (2025). *IEEE Access* 13, 67269 to 67285. [DOI:10.1109/ACCESS.2025.3560424](https://doi.org/10.1109/ACCESS.2025.3560424). CC BY-NC-ND 4.0. Received 10 Mar 2025, accepted 7 Apr 2025, published 14 Apr 2025.
**Affiliations**: EuroMov Digital Health in Motion, University of Montpellier, IMT Mines Alès; Tarbes STAPS Laboratory MEPS, Université Pau.
**Funding**: French ANR ModPuls project ANR-22-CE38-0006-01.
**GitHub resource**: [TheoPulse/Human_synchronization_datasets](https://github.com/TheoPulse/Human_synchronization_datasets.git) (compiled dataset table; open for contribution).
**raw path**: `raw/01_primary_sources/A_Review_of_Human_Synchronization_Datasets.pdf`

## 1. Scope and Methodology

- **Total datasets cataloged**: **101** [p. 67271, §III]
  - 45 raw datasets (Table 1, original data collection)
  - 56 experimental studies with reused data (Table 2)
- **Directly accessible**: **75** [p. 67271, §III]
- **Available on request**: 26
- **Methodology**: Google Scholar + Google Datasets search, keyword set "sensorimotor synchronization", "auditory-motor synchronization", "beat synchronization", "interpersonal synchronization", "interpersonal entrainment", "musical synchronization", "ensemble synchronization", each combined with "dataset". First 30 results per keyword. Extended via "similar articles" on Springer/Nature/Elsevier platforms [p. 67272, §II].
- **Excluded**: synchronization of complex networks in telecom / computing / real-time collaborative applications (i.e., non-human synchronization).

## 2. Four-Category Taxonomy

Approximately equal-volume partition [p. 67273 to 67275, §III, Fig. 2]:

| Category | Volume | Examples |
| :--- | :--- | :--- |
| Discontinuous SMS | **25%** | finger tapping, clapping, whispering to metronome/music; event-timeseries data |
| Continuous SMS | **19%** | walking, dancing, oscillating pendulums, mirror games, Tai Chi; kinematic / MoCap data |
| Social interactions | **30%** | dyadic conversations (22/31), speed-dating (3/31), board games (2/31); video + affective computing |
| Musical performance | **26%** | music interpersonal entrainment (jazz, classical, Indian raga, Malian jembe, Cuban son, Tunisian stambelli) + MIR/DIR datasets; audio + MoCap + annotated scores |

## 3. Core Definitions (§I-B)

**Entrainment** [p. 67270]: Physics formalism — coupled self-sustained oscillators synchronize phase and frequency under suitable coupling. Requires continuous energy input and natural frequency on a stable limit cycle. Human extension: human rhythmic motion synchronizing to external rhythmic stimulus (walking, finger-tapping to metronome).

**Sensorimotor Synchronization (SMS)** [p. 67270]: Human ability to synchronize rhythmic motion with rhythmic sensory stimuli (auditory, visual, tactile).

**Interpersonal Coordination (IC)** [p. 67270]: Interdependence of two or more people during social interactions. Two subcategories:

- **Interpersonal Synchrony (IS)**: dynamic, reciprocal adaptation of temporal structure between partners. Not about what but about timing. Operates at multiple levels: nonverbal behavior (facial expression, body movement, paralinguistic speech) and covert physiological/neural activity.
- **Behavioral Mimicry (BM)**: spontaneous imitation of gestures, postures, mannerisms, face-touching. Usually analyzed in 3-to-5-second temporal windows.

IS and BM overlap but are not mutually exclusive.

## 4. Acquisition Methods (§IV)

**Eight signal types** [p. 67275 to 67278, Fig. 6]:

1. Physiological (HR, skin conductance, respiration)
2. Event time-series (tapping onsets)
3. EEG / hyperscanning
4. Kinematic (accelerometers, potentiometers)
5. Audio
6. Simple video
7. Pose estimation (2D / 3D skeletal)
8. Motion capture (marker-based)

**Cross-tab (§IV)**:

- Social interactions → simple video dominant.
- Continuous motion and musical performance → motion capture dominant.
- Discontinuous SMS → event time-series (tapping devices: force-sensitive pads/keyboards recording MIDI, accelerometers, microphones; REPP platform for remote tapping via computer microphone).

## 5. Synchronization Measures (§V — heterogeneity documented)

Paper does not champion a single measure; it catalogs heterogeneity. Key observations:

- **Relative phase / PLV** [p. 67280]: works well in controlled SMS with well-defined target motion.
- **Different measures on same performance yield very different scores** [Bayd et al. ref 127, p. 67280]. Combining local and global measures is necessary.
- **Regularity index**, **Novotny & Bente [80] Tai Chi study**: different motion-synchrony measures all correlate positively with human perception, but which correlates best depends on task.
- **Cohen's d + surrogate data** (Bernieri & Rosenthal ref 134, Hudson et al. ref 125, p. 67280 to 67281): virtual pairing of non-interacting individuals creates baseline against pseudosynchrony. Used to distinguish true synchrony from chance.
- **"Pseudosynchrony"** [Bernieri & Rosenthal 134]: coincidental behavioral events that occur purely by chance during real interactions.
- **Mayo & Gordon [135]**: "more synchrony is not always beneficial"; moving in and out of synchrony may be adaptive. Disruption of synchrony is a key factor in individual and collective creative processes.

## 6. Raw Data Block (critical gap statistics)

| Fact | Value | Source |
| :--- | :--- | :--- |
| Total datasets cataloged | 101 | [p. 67271, §III] |
| Raw datasets (Table 1) | 45 | [p. 67271, §III] |
| Experimental studies reusing data (Table 2) | 56 | [p. 67271, §III] |
| Direct online access | 75 | [p. 67271, §III] |
| Available upon request | 26 | [p. 67271, §III] |
| **Datasets with explicit synchrony/coordination annotation** | **3** | [p. 67280] |
| Datasets evaluated by untrained participants (visual/auditory perception) | 3 | [p. 67280] |
| Categories | 4 (discontinuous SMS, continuous SMS, social, musical) | [p. 67273 to 67275] |
| Signal types | 8 | [p. 67275 to 67278] |

**Key gap**: only **6 of 101** datasets have any form of synchrony-quality annotation (3 expert, 3 perceptual). This is the paper's core finding on the annotation bottleneck for ML.

## 7. Limitations and Gaps (§VI, §VII)

**Stated**:

- **Annotation gap**: only 3 datasets have direct synchrony quality annotations, limiting supervised ML development [p. 67280].
- **Heterogeneity in measures**: different measures yield different scores on same performance; no agreed standard [p. 67280].
- **Complexity of real-world annotation**: in free improvisation or natural conversation, defining what/when to annotate is subjective; ambiguity in partial/gradual synchrony [p. 67281].
- **Pseudosynchrony vs. true synchrony**: distinguishing intentional coordination from chance is difficult without surrogate-data methods [p. 67281].
- **Cultural bias**: rhythmic synchronization quality varies across cultures; most datasets are Western-centric [p. 67281, §VII].
- **Privacy / FAIR tension**: real-world data is most meaningful but raises privacy concerns; anonymization protocols required.
- **Definition heterogeneity**: computational, behavioral neuroscience, motor control, and psychology fields use slightly different sync definitions; unified framework needed.

**Implicit**:

- Review published April 2025; future datasets are not captured.
- Only first 30 results per keyword searched; long-tail bias possible.
- Non-human synchronization explicitly excluded — no engineering / network / simulation datasets even though they contain formally related methods.

## 8. Relevance to Project 8 E(t)

**P-13 is load-bearing for**:

- **Literature-review scaffolding** in Project 8 paper §2 (Related Work): P-13 provides the canonical catalog. Project 8 should cite the four-category taxonomy when positioning "online choir entanglement" in the broader field.
- **Dataset discovery for Tier 2 enrichment**: the "musical performance" 26% subset (URMP, Solos, IEMP jazz/classical/raga/jembe/candombe/stambelli/string-quartet, Omega Ensemble via P-14, etc.) is the pool from which Project 8 could draw supplementary multitrack material if Tier 2 Jamulus/SoundJack data is insufficient.
- **Annotation gap evidence**: Project 8 can legitimately cite "only 3 of 101 datasets have synchrony-quality annotations" as justification for its own annotation protocol being a contribution.
- **Definition selection**: Project 8 should explicitly pick among the IS/BM/entrainment/SMS lineage. The "entanglement" term (from S-02) is not in P-13's definitional space; Project 8 must bridge.
- **Surrogate-data / pseudosynchrony** [p. 67281]: binds Project 8's null-model methodology. Circular-shift nulls, virtual-pairing nulls, and Cohen's d effect-size reporting are all standard-practice references here.

**P-13 is NOT**:

- A source for any specific measure's validity (PLV, Granger, RQA are named in Project 8 context but P-13 does not endorse them).
- A source for the "oscillator model explains why performers maintain rhythm despite jitter" claim (prior digest). P-13 states the oscillator formalism but does NOT apply it to network latency or jitter tolerance; that is a Project 8 extrapolation.
- A benchmark: P-13 is a review, not a primary empirical source.

## 9. Corrections Logged Against Prior Digest

See [[deep_read_audit]] for full table. Summary:

| Issue | Prior claim | Corrected reading |
| :--- | :--- | :--- |
| Total-count specificity missing | "101 human synchronization datasets" | 101 total = 45 raw + 56 experimental; 75 directly accessible, 26 on request; only **3** have synchrony quality annotations [p. 67271, 67280]. |
| Category percentages missing | "Discontinuous SMS (tapping), Continuous SMS (walking), Social Interactions (conversations), Musical Performance" | 25%, 19%, 30%, 26% respectively [p. 67273 to 67275]. Social interactions is largest. |
| "Measurement Taxonomy" over-reaches | "PLV, GCA, RQA are used as synchronization indices" | P-13 does NOT endorse these. It catalogs measure heterogeneity and documents that different measures yield different scores on the same performance [Bayd et al. 127, p. 67280]. Claiming P-13 justifies Project 8's specific measure choice is a misread. |
| "Oscillator model explains why performers can maintain a rhythm even when individual beats are slightly jittered by the network" | — | P-13 states the oscillator formalism (§I-B-1) but does NOT extend it to network jitter tolerance. This is Project-8 extrapolation. Moved to §8 labeled as such. |
| Missing pseudosynchrony / surrogate-data section | (no mention) | Bernieri & Rosenthal's "pseudosynchrony" concept, virtual-pairing surrogates, Cohen's d for sensitivity. Load-bearing for Project 8's null-model design [p. 67281]. |
| Missing Mayo & Gordon "disruption is adaptive" point | (no mention) | "More synchrony is not always beneficial"; moving in/out of synchrony may be adaptive; disruption is a key factor in creativity [p. 67281]. Reframes what high E(t) means. |
| Missing cultural-bias caveat | (no mention) | Most datasets are Western-centric; rhythmic synchronization varies cross-culturally [p. 67281, §VII]. Relevant to Project 8 scope (German university + Western choral repertoire). |
| Missing GitHub resource | (no mention) | [TheoPulse/Human_synchronization_datasets](https://github.com/TheoPulse/Human_synchronization_datasets.git) — open-contribution dataset registry. Project 8 should register its Tier 2 corpus here on publication. |
