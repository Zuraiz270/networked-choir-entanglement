---
title: Fake Time Approach (FTA)
type: concept
alchemy_stage: citrinitas
tags: [latency, compensation, synchronization, nmp, deep_read]
ingested_date: 2026-04-23
last_deep_read: 2026-04-23
source_count: 1
related: ["[[p_12_exploiting_latency]]", "[[latency_thresholds]]", "[[nmp_platform_comparison]]"]
---

# The "Fake Time" Approach (FTA)

FTA is a latency handling strategy for Networked Music Performance (NMP) systems built around cyclical music. It originates in the M.A.S. (Mutual Anticipated Session) protocol of Obu, Kato, and Yonekura (2003), is implemented in NINJAM and the Global Drum Circle (GDC), and is re-used in the prototype described by [[p_12_exploiting_latency]] (Liloia & Dannenberg, NIME 2025).

## Mechanism (per [[p_12_exploiting_latency]])

FTA does **not** minimize jitter or latency. It **extends latency** so that jitter becomes irrelevant within the scheduled transmission slot [[p_12_exploiting_latency]] [p. 2, §2.2.1].

Four requirements [p. 2, §2.2.1]:

1. Impose a rigid global tempo.
2. Synchronize local clocks across clients.
3. Estimate worst-case end-to-end latency Λ (in ms).
4. Schedule every transmitted message to execute at a future time T such that (T − send_time) ≥ Λ **and** (T − send_time) is an integer multiple of one musical cycle.

Inside that scheduled slot, network jitter is absorbed invisibly. The receiver sees a rhythmically quantized event, not a jitter-smeared one.

In the [[p_12_exploiting_latency]] prototype, default Λ = 3500 ms, the beat-align factor ν = 4 beats per cycle, and the resulting maximum tempo is approximately 68 BPM [p. 5, §4.6.1].

## Domain of Validity

FTA works because percussive, loop-based, or cyclical music tolerates one-cycle-ahead playback without perceptible coordination breakdown. The receiver hears what peers played one (or more) musical cycles ago, which aligns rhythmically with the current local cycle.

FTA does **not** generalize to:

- Sustained-pitch polyphonic ensembles (choirs, string quartets) where held tones span many beats and cannot be rhythmically quantized.
- Through-composed music without a repeating cycle.
- Real-time conversational musical exchange (call and response, improvised counterpoint at short timescales).

## Implications for Project 8 E(t)

In a system that uses FTA, audio-level onset synchronization A(t) will appear artificially tight because software enforces the quantization. This is not evidence of interpersonal entrainment; it is evidence of software scheduling. Project 8 must therefore treat FTA-mediated sessions as a latency-handling regime distinct from unmediated acoustic coupling, and must rely on visual and breath-based coupling channels (V(t), N(t)) rather than audio onsets to detect genuine performer coordination inside an FTA envelope.

This is a **Project-8 extrapolation**. [[p_12_exploiting_latency]] does not measure interpersonal coupling or E(t) at any latency regime; it describes a design and one informal n=3 session.

## Open Questions

- Is there a sustained-tone analogue of FTA that works for choral music? No evidence found in current sources.
- Does FTA-induced rhythmic rigidity suppress the micro-timing variation that [[phase_locking_value]] needs to detect synchrony? Empirical question, not addressed in [[p_12_exploiting_latency]].

## Corrections Logged (prior digest)

Prior version claimed FTA applies "when network delay exceeds the threshold for natural human synchronization (typically > 150ms)". This 150 ms figure is **not sourced to [[p_12_exploiting_latency]]**. The paper cites 75 ms as the audio-only two-way upper bound for unadjusted play [p. 2, §2.2.1]; it does not cite a 150 ms threshold for FTA applicability. See [[deep_read_audit]] for the corrections table.
