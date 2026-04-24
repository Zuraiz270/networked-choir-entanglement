---
title: Phase-Locking Value (PLV)
type: concept
alchemy_stage: citrinitas
tags: [metrics, synchronization, husync, fft]
ingested_date: 2026-04-23
source_count: 1
related: ["[[p_14_husync]]", "[[entanglement_index]]"]
---

# Phase-Locking Value (PLV)

The Phase-Locking Value (PLV) is a mathematical metric used to quantify the degree of synchronization between two oscillating signals. It is heavily utilized in neuroimaging (EEG/MEG) and has been successfully adapted for interpersonal body motion analysis.

## Computational Pipeline (as used in huSync)
1. **Kinematic Extraction:** Obtain motion trajectories (e.g., Euclidean distance of a nose key-point over time) using pose estimation.
2. **Frequency Domain Transformation:** Apply a sliding-window Fast Fourier Transform (FFT) to extract phase angles for each frequency bin.
3. **Relative Phase Angle:** Calculate the phase difference $\Delta\phi(t) = \phi_1(t) - \phi_2(t)$ between two performers in a dyad.
4. **PLV Calculation:**
   $$ PLV = \left| \frac{1}{N} \sum_{n=1}^{N} e^{i(\phi_1(t) - \phi_2(t))} \right| $$
   This yields a complex unit-length vector. The absolute value of the mean represents the PLV magnitude.

## Interpretation
- **Range:** $[0, 1]$.
- **0** indicates a completely random phase relationship (no synchronization).
- **1** indicates a constant phase difference (perfect synchronization/locking).

## Application to NMP
Unlike simple frame-differencing (Motion Energy Analysis), PLV is directional and can capture the underlying periodic entrainment between musicians, serving as a critical mathematical foundation for our own $E(t)$ Entanglement Index mapping.
