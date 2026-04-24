---
title: Audio Sync Streams
type: concept
alchemy_stage: citrinitas
tags: [metrics, audio-processing, synchronization, dsp]
ingested_date: 2026-04-23
source_count: 5
related: ["[[p_14_husync]]", "[[p_18_audio_guided_mocap]]", "[[entanglement_index]]"]
team_take: "The primary high-fidelity channel for measuring coordination. On Tier 2/3 data, this represents the 'ground truth' for synchronization."
---

# Audio Sync Streams

**Audio Sync Streams** refer to the per-singer audio channels used to calculate the acoustic components of the [[entanglement_index]].

## Key Components
- **Onset Detection**: Pinpointing the exact start of musical notes (spectral flux vs. manual annotation).
- **Pitch (F0) Contours**: Tracking the fundamental frequency over time to check for melodic coupling.
- **Breath Envelopes**: Extracting the amplitude modulation associated with respiratory preparation.

## Tier-Specific Extraction
- **Tier 1 (YouTube)**: Only ensemble-level statistics (spectral flux) are reliably extracted due to the mixed-stereo nature of the source.
- **Tier 2/3 (Multitrack)**: Full per-singer extraction using `librosa.pyin` and `demucs` (where applicable).

## Related
- [[p_14_husync]]
- [[p_18_audio_guided_mocap]]
- [[entanglement_index]]
