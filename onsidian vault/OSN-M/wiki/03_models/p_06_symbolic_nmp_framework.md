---
title: P-06 Symbolic NMP Framework
type: source
alchemy_stage: nigredo
tags: [nmp, implementation, edge_computing, midi, synthesis, deep_read]
ingested_date: 2026-04-23
last_deep_read: 2026-04-23
source_count: 1
related: ["[[symbolic_transmission]]", "[[hanging_note_inference]]", "[[nmp_on_the_edge]]", "[[deep_read_audit]]"]
team_take: Symbolic NMP works well for MIDI keyboard instruments in bandwidth-constrained networks. NOT validated for continuous-pitch instruments (voice, violin). JackTrip comparison at Scenario 4 (200 kbps bottleneck) inflates apparent advantage.
---

# P-06 Reconstructing the Sound at the Edge: A Low-Latency Framework for NMP with Autotuned Local Synthesis

**Citation**: Borgianni, L., Bua, C., Adami, D., Giordano, S. (**2025**). In *IEEE 6th International Symposium on the Internet of Sounds (IS2) 2025*. [DOI:10.1109/IS264627.2025.11284618](https://doi.org/10.1109/IS264627.2025.11284618).
**Affiliations**: University of Pisa, Dept. of Information Engineering; CNIT.
**Funding**: EU NRRP "RESTART" (PE00000001), MUR FoReLab + CrossLab (Dept. of Excellence).
**Code**: [Borgianni/Recostruction Sound Edge](https://github.com/Borgianni/Recostruction%20Sound%20Edge)
**raw path**: `raw/01_primary_sources/Reconstructing_the_Sound_at_the_Edge_A_Low-Latency_Framework_for_NMP_with_Autotuned_Local_Synthesis.pdf`

## 1. Architecture (exact)

Three components [§III]:

1. **Client (Performer Node)**: Polls USB MIDI keyboard via `rtmidi` (Python) with 1 ms sleep. Outputs OSC messages via `python-osc` UDP to `/midi` address. Payload: `(on/off binary, MIDI note number)`.
2. **Network link**: UDP/OSC. No reliability layer — packet loss = lost note event.
3. **Server (Synthesis Node)**: SuperCollider script listens on `/midi`. Maps MIDI note n to frequency via 12-TET: `f = 440 × 2^((n−69)/12)`. ADSR envelope. **Hanging-note timeout = 2 seconds** (releases note envelope if no note-off arrives).

**State**: Server maintains two dictionaries: S (active synth instances by note) and T (timeout tasks).

**Scope limit** [§III, intro]: "Present study focuses exclusively on the MIDI-capture approach." Audio-based symbolic extraction (pitch from microphone via aubio or CREPE) is mentioned as future work, not evaluated.

## 2. Bandwidth Comparison (Table II)

| Approach | Edge processing | Added latency | Bandwidth/channel |
| :--- | :--- | :--- | :--- |
| PCM (raw) | No | <5 ms | **1.4 Mbps** (48 kHz, 16-bit mono) |
| Opus audio | No | <1-5 ms | 64-128 kbps |
| **MIDI/OSC + synth** | **Yes** | **<10 ms** | **<1 kbps** (up to 20-50 kbps in bursts) |
| DDSP embeddings | Yes | <20-30 ms | 10-30 kbps |
| Hybrid | Partial | 100-300 ms | — |

## 3. Evaluation

**Participants**: 15 (8 musicians + 7 non-musicians) [§IV-A].
**Scenarios** (emulated via Network Link Conditioner):

1. 0% loss, 0 ms delay
2. 5% loss, 20 ms delay
3. 15% loss, 40 ms delay
4. 200 kbps uplink cap, 0% loss, 0 ms delay

**Baseline**: JackTrip, fed the same MIDI events rendered to PCM at transmitter. Config: 48 kHz, 16-bit mono, frame 128 samples, default jitter buffer, no FEC.

**MOS 5-point scale** across 3 questions (Audio Quality, Delay, Overall).

### Raw Data Block (MOS comparison, Table III)

| Scenario | JackTrip Musicians | Ours Musicians | JackTrip Non-Musicians | Ours Non-Musicians | Avg Diff (Ours − JackTrip) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 (Ideal) | 4.9 | 4.7 | 4.7 | 4.5 | **−0.1** |
| 2 (5% loss, 20 ms) | 3.2 | 3.4 | 4.0 | 3.6 | **+0.1** |
| 3 (15% loss, 40 ms) | 2.6 | 2.8 | 3.4 | 3.0 | **+0.1** |
| 4 (200 kbps cap) | 1.1 | 3.9 | 1.5 | 3.7 | **+2.6** |
| Average | 2.95 | 3.7 | 3.4 | 3.7 | +0.425 |

**Critical caveat, authors' own words** [§IV-B]: "The small mean differences observed in Scenarios 1-3 (on the order of 0.1 on a 5-point scale) should therefore not be interpreted as evidence of superiority of one system over the other." The large +2.6 gap in Scenario 4 reflects that **JackTrip's 1.4 Mbps PCM cannot fit through a 200 kbps pipe** and "effectively behaves as a low anchor."

### Missing-Note Analysis (500 MIDI notes × 10 repetitions per scenario)

| Scenario | Mean missing notes | SD |
| :--- | :--- | :--- |
| 1 | **0.2** | 0.1 |
| 2 | **1.8** | 0.5 |
| 3 | **4.6** | 1.2 |
| 4 | **2.1** | 0.7 |

Scenario 4 still shows 2.1 mean missing notes despite "no loss" config — congestion-induced bursts during fast passages.

## 4. Limitations

**Stated** [§IV-A, §IV-B, §V]:

- **Instrument limited to MIDI keyboard**. Results "may differ for other instruments, particularly those producing continuous pitch (e.g., violin, voice) or complex timbral dynamics (e.g., drums, guitar)."
- Network emulation is i.i.d. loss, not burst-correlated. "Cannot capture all characteristics of real-world networks (e.g., correlated loss bursts, cross-traffic, or jitter variability)."
- PEAQ not used; MOS-based subjective evaluation only.
- Pitch tracking for continuous-pitch instruments "requires audio buffering for accurate frequency estimation, which may increase end-to-end latency beyond typical NMP requirements" — tradeoff acknowledged as future work.
- Autotune is "introduced only as an illustrative feature" — not evaluated quantitatively.

**Implicit (binding on Project 8 citation)**:

- **Not applicable to vocal NMP**. Choir singing is continuous-pitch, multi-timbral, formant-rich; P-06's MIDI-only evaluation is not evidence for vocal performance.
- JackTrip baseline in Scenario 4 is a straw-man: 1.4 Mbps PCM through 200 kbps pipe cannot work. +2.6 MOS gap in that scenario is an expected consequence of the bandwidth budget, not a measure of P-06's intrinsic quality.
- 15-participant subjective study is small for MOS statistics.
- Autotune claim in title is not backed by any experimental data in the paper.
- No end-to-end latency measurement (only "bandwidth" and "missing notes"). The <10 ms added-latency claim in Table II is a theoretical upper bound, not measured.

## 5. Relevance to Project 8 E(t)

**P-06 is relevant for**:

- **[[nmp_platform_comparison]]**: symbolic-transmission class distinct from P2P audio, client-server audio, and FTA regimes.
- **Bandwidth budget discussion** in Project 8 §11 (hardware / network requirements). The 1.4 Mbps → <1 kbps reduction is a strong argument for symbolic-first design in bandwidth-constrained contexts.
- **[[hanging_note_inference]]**: P-06's 2-second timeout mechanism for lost note-off messages is a concrete failure-mitigation pattern.

**P-06 is NOT**:

- Evidence that symbolic NMP works for choral performance. The paper's own caveats explicitly exclude continuous-pitch instruments.
- Evidence for autotune-driven QoE improvement (claim not evaluated).
- A reliable E(t) baseline — MOS measures perceived quality, not interpersonal coordination.
- Evidence that JackTrip is worse under realistic conditions — Scenarios 1-3 show ~equivalent performance; only the engineered bandwidth-bottleneck Scenario 4 shows a gap.

## 6. Corrections Logged Against Prior Digest

See [[deep_read_audit]] for full table. Summary:

| Issue | Prior claim | Corrected reading |
| :--- | :--- | :--- |
| Year wrong | "Borgianni, L., et al. (2024)" | Published 2025 in IEEE IS2 2025 (DOI:10.1109/IS264627.2025.11284618). |
| "1400x reduction vs PCM" oversimplified | — | 1.4 Mbps (PCM) vs <1 kbps (MIDI) = 1400× for note events but up to 20-50 kbps in fast-passage bursts, giving ~30-70× real-world [Table II]. |
| "Local synthesis avoids jitter buffer delays inherent in audio streaming" | — | P-06 does not measure end-to-end latency. The <10 ms figure in Table II is theoretical. No empirical latency comparison with JackTrip is in the paper. |
| "MIDI state dictionaries prevent 'stuck notes' even if network packets are dropped" | — | The 2-second timeout mechanism mitigates hanging notes, but missing-note analysis shows 1.8 / 4.6 / 2.1 missing notes across scenarios 2/3/4. Mitigation is partial, not prevention. |
| Scenario-4 inflated claim absent | "Maintains superior performance compared to solutions such as JackTrip in scenarios with packet loss or limited bandwidth" | Authors' own caveat [§IV-B]: Scenario 4 gap (+2.6 MOS) is an artifact of JackTrip's 1.4 Mbps PCM not fitting through a 200 kbps pipe. Scenarios 1-3 show ~0.1 MOS differences, which the authors explicitly state "should NOT be interpreted as evidence of superiority." |
| Missing caveat: instruments limited to MIDI keys | "Performer Node (Client): Captures MIDI (or pitch)..." | Paper tests MIDI keyboard ONLY. Continuous-pitch instruments (voice, violin) are future work [§IV-A, §V]. Not applicable to choral NMP. |
| Missing autotune-evaluation caveat | "Edge Enhancement: Includes local effects like Autotune" | Autotune is described but **not evaluated** in this paper. "Autotune is introduced only as an illustrative feature of the architecture." |
| Missing i.i.d. loss caveat | (no mention) | Network emulation uses i.i.d. loss, not burst-correlated. Real-world conditions may differ [§IV-A]. |
| Missing "Symbolic Coupling S(t)" is Project-8 extrapolation | "If the primary audio coupling A(t) fails... the system can switch to Symbolic Coupling S(t)" | P-06 does not propose "symbolic coupling" as an entanglement metric. This is Project-8 design. Moved to §5 as extrapolation. |
