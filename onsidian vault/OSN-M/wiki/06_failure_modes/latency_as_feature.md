---
title: Latency as a Feature
type: concept
alchemy_stage: citrinitas
tags: [latency, design_patterns, nmp, deep_read]
ingested_date: 2026-04-23
last_deep_read: 2026-04-23
source_count: 1
related: ["[[p_12_exploiting_latency]]", "[[fake_time_approach]]"]
---

# Latency as a Feature

Traditional NMP design treats latency as a defect to minimize through codecs, hardware (ASIO drivers), or physical proximity (LAN). The "latency as a feature" paradigm inverts this: latency is admitted into the musical and interaction design and becomes load-bearing rather than residual cost.

## Prior Art (sourced via [[p_12_exploiting_latency]] §2.3)

Per [p. 3, §2.3], most prior work that "exploits" latency maps network delay onto musically adjacent timescales on the order of milliseconds:

- Pitch mapping (Chafe, Wilson, Walling 2002)
- Spatial diffusion parameter mapping (Chafe 2003)
- Short echo effects around 100 ms (Rebelo & King 2010)

The [[p_12_exploiting_latency]] paper's own contribution is to scale latency up to multi-second timescales by mapping it onto avatar positions on a 2D grid. A hit marker crossing the full grid diagonal takes 4 measures at default δ=16 and Λ=3500 ms [p. 5, §4.4, §4.6.1].

## Role Architecture in [[p_12_exploiting_latency]]

Three role classes (Composer, Performer, Listener) are introduced for UI clarity and musical responsibility [p. 3, §3.1; p. 3-4, §3.3]. The system does impose **asymmetric client-side display delays** [p. 5, §4.6.2]:

- Actions requiring responses from another user: delayed by 2·Λ
- Other messages: delayed by Λ
- Own drum hits: displayed immediately, then reconciled against broadcast confirmation (client-side prediction pattern imported from video games)

These asymmetric delays exist to preserve visual agency and apparent responsiveness across the hit-marker propagation pipeline. The role split itself (Composer/Performer/Listener) is driven by UI and musical-responsibility considerations, not primarily by latency enforcement.

## Domain Boundary

"Latency as a feature" in [[p_12_exploiting_latency]] is demonstrated for:

- Percussive, cyclical, drum-based music.
- Informal improvisation (n=3, one session, no quantitative evaluation).
- Output is MIDI files used for asynchronous post-production composition.

It is **not** demonstrated for:

- Choral or sustained-tone performance.
- Formal ensemble art-music.
- Any quantitative interpersonal coordination measurement.

Project 8 cites this paper as a **boundary-condition reference** (multi-second latency is survivable for jamming with heavy visual compensation and rigid tempo scaffolding), not as evidence that choral entanglement survives multi-second latency.

## Corrections Logged (prior digest)

Prior version listed "Spatialization: Using delays of 50-100ms to simulate acoustic reflections in a large virtual room" and "Forced Asymmetry: Using latency to enforce specific roles, such as separating 'Composers' (who initiate signals) from 'Performers' (who react to delayed signals)."

The first conflated spatial-diffusion parameter mapping (Chafe 2003) with generic reverb simulation. The second overstated the causal role of latency in the Composer/Performer split: in [[p_12_exploiting_latency]], the roles exist for UI and musical reasons, and the asymmetric 2·Λ / Λ display delays are the actual latency-driven mechanism, applied within and across roles. See [[deep_read_audit]].
