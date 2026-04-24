---
title: P-22 Augmented Granger Causality
type: source
alchemy_stage: nigredo
tags: [causality, ordinal_patterns, non_linear, reservoir_computing, signal_processing, deep_read]
ingested_date: 2026-04-23
last_deep_read: 2026-04-23
source_count: 1
related: ["[[ordinal_synchrony_pattern]]", "[[non_linear_causal_leakage]]", "[[p_21_granger_representation_learning]]", "[[deep_read_audit]]"]
team_take: Load-bearing method for Project 8's non-linear N(t). Single-author paper; all validation is synthetic or air-transport, not music. Zanin explicitly recommends using BOTH standard GC and COP-GC in parallel.
---

# P-22 Augmenting Granger Causality through Continuous Ordinal Patterns

**Citation**: Zanin, M. (2024). *Communications in Nonlinear Science and Numerical Simulation* 128, 107606. [DOI:10.1016/j.cnsns.2023.107606](https://doi.org/10.1016/j.cnsns.2023.107606). Elsevier. CC BY-NC-ND 4.0. 9 pages. **Single author.** Received 15 June 2023, accepted 9 October 2023.
**Author**: Massimiliano Zanin (Instituto de Física Interdisciplinar y Sistemas Complejos CSIC-UIB, Palma de Mallorca, Spain).
**Funding**: ERC grant 851255 (H2020); María de Maeztu CEX2021-001164-M.
**raw path**: `raw/01_primary_sources/Augmenting Granger Causality through Ordinal Patterns.pdf`

## 1. Claim

COP (Continuous Ordinal Patterns) preprocessing "allows to efficiently detect non-linear causality relations without the need of a priori assumptions" and "can seamlessly be integrated into existing data analysis pipelines" because it outputs transformed real-valued time series on which standard GC runs unchanged [p. 107606, Abstract; p. 107606 to 3, §2.3].

## 2. Method (exact)

**Continuous ordinal pattern definition** [p. 2, §2.1, Eq. 1]:

Given time series X of length N, sub-window x_i of size D starting at time i, normalized to [-1, 1]. Predefined pattern π of D values also in [-1, 1]. Distance:

$$d_\pi(x_i) = \frac{1}{2D} \sum_{j=0}^{D-1} \left| \bar{x}_{i+j} - \pi_j \right|$$

d_π is in [0, 1]. 1 − d_π(x_i) quantifies how well pattern π describes the sub-window. When averaged over all windows, 1 − d_π is how well π describes the entire series.

**Pattern selection** [p. 2, §2.2]:

- **Simulated Annealing (SA)**: optimize π to maximize KS-test p-value between d_π(X) and d_π(Y). Pattern values constrained to [−1, 1], at least two pattern values fixed at −1 and 1.
- **Random patterns**: surprisingly competitive; Reservoir Computing analogy.

**Causality assessment** [p. 3, §2.3]: Apply standard Granger Causality test to (d_π(X), d_π(Y)) pair. Same F-test and p-value structure as classical GC; the only difference is input preprocessing. Statistical threshold α = 0.01 used throughout.

## 3. Raw Data Block (key validation results)

| Experiment | Setup | GC Accuracy | COP Accuracy | Source |
| :--- | :--- | :--- | :--- | :--- |
| Linear coupled logistic maps (Eq. 2) | γ ≥ 0.15 | ~100% | marginally better, D=3 > D=4 | [p. 3, Fig. 1a] |
| Non-linear sinusoid × logistic (Eq. 3) | γ = 0.05 | **fails (near 0%)** | **~100%** at D=3 and D=4 | [p. 3, Fig. 1b] |
| Random pattern (Eq. 3, D=3, γ=0.05) | histogram of 10³ realizations | — | mean **0.828**, median **0.833** | [p. 4, Fig. 2a] |
| Parallel random patterns with Bonferroni (Eq. 3, γ=0.05) | ~10 random π | — | near-perfect detection | [p. 4, Fig. 2b] |
| Synthetic fMRI (VAR + HRF + downsample 10) | ε = 2.0, N = 10⁴ | modest | substantially better at D=3, D=5 (D=4 anomaly) | [p. 5, Fig. 4a] |
| Synthetic fMRI vs. time-series length | fixed coupling, downsampling | — | matches GC with ~1 order of magnitude shorter series | [p. 5, Fig. 4c] |
| Air transport delay propagation | 50 largest EU airports, Sep 2019, 20-min windows, max lag 6 h | N links detected | More links, different topology (different transitivity, efficiency, modularity Z-scores) | [p. 7 to 8, Fig. 5] |

**Independent realizations throughout synthetic experiments**: 10³. Time series length: 10³ (except synthetic fMRI which used 10⁴).

## 4. Key Findings

1. **Linear case**: COP offers no benefit; may even slightly reduce GC accuracy [p. 3, Fig. 1a; p. 8, §4].
2. **Non-linear case**: COP dramatically outperforms GC (0% → 100% detection on Eq. 3 at γ=0.05) [p. 3, Fig. 1b].
3. **Random patterns suffice**: expensive SA optimization not required. ~10 random patterns with Bonferroni correction recovers near-perfect detection. Reservoir Computing analogy [p. 4, §3.2].
4. **Noise and missing values**: COP on nonlinear systems is **more sensitive** to both than GC [p. 5, Fig. 3a, 3c].
5. **Complementarity** [p. 7 to 8, §3.5, §4]: In real-world air-transport case, GC and COP detect largely **different** link sets. Recommended approach is to run **both** and report linear-only, non-linear-only, and common links separately.

## 5. Limitations (§4 and implicit)

**Stated** [p. 8, §4]:

- "Not an 'one-fits-all' approach."
- Large number of random patterns required for stable results; long time series make this expensive.
- Pattern π interpretation is non-trivial (unlike linear GC coefficients, which have direct dynamical meaning).
- If the true causality is already linear, COP may **reduce** accuracy relative to standard GC.
- If causality is not encoded in the dynamics (e.g., two series related by a time-shifted independent noise draw), COP yields no additional information.
- COP on non-linear systems is more sensitive to observational noise and missing values than GC.

**Implicit**:

- Single-author paper; no independent replication within the paper.
- Bonferroni correction was **abandoned** for the air-transport analysis on the grounds that "tests for a given pair of airports are not independent" [p. 7 to 8, §3.5]. The sanity check used (shuffled-series false-positive rate) is informal, not formally derived. This is a methodological caveat for any Project 8 application: we cannot replicate Zanin's air-transport analysis structure for singer-pair causality without rigorously justifying the loss of multiple-test correction.
- D=4 performs worse than D=3 and D=5 on synthetic fMRI; reason unclear [p. 5, §3.4]. Embedding-dimension selection is therefore not monotonic, and choosing D requires empirical validation per use case.
- No music, no ensemble, no singer application in the paper. Relevance to Project 8 is by methodological transfer, not by direct empirical validation.

## 6. Relevance to Project 8 E(t)

**P-22 is load-bearing for**:

- **[[non_linear_causal_leakage]]**: this failure mode exists precisely because linear GC misses non-linear influence structures. P-22 quantifies the failure (e.g., Eq. 3 system: GC detects ~0% of causal links at γ=0.05 while COP detects ~100%).
- **N(t) network construction**: Project 8 should run BOTH standard GC and COP-GC per Zanin's §4 recommendation, report linear-only, non-linear-only, and common edge sets separately. Using only standard GC would leave non-linear entrainment invisible.
- **[[ordinal_synchrony_pattern]]**: COP's ordinal preprocessing is conceptually adjacent (both derive from Bandt-Pompe 2002). Worth cross-referencing during that concept page's future deep-read cascade.

**P-22 is NOT**:

- Evidence that COP works on music data (paper has none).
- Evidence for any specific embedding dimension D choice for audio/pose timeseries (paper shows D=3,4,5 all behave differently and D=4 is anomalous on fMRI).
- A substitute for standard GC (paper explicitly recommends running both).

**Implementation note for Project 8**: the reference implementation (from cited [6], Zanin 2023 Chaos) must be located or implemented. Python library implementing COP is not specified in the paper. This is a WP1 validation task for the N(t) pipeline.

## 7. Corrections Logged Against Prior Digest

See [[deep_read_audit]] for full table. Summary:

| Issue | Prior claim | Corrected reading |
| :--- | :--- | :--- |
| Missing formula | "distance metric between a predefined pattern and the data window" | Eq. 1: $d_\pi(x_i) = (1/2D) \sum \lvert x_{i+j} - \pi_j \rvert$ [p. 2, §2.1]. |
| Missing numerics | "even a small set of random ordinal patterns can effectively expand the feature space" | ~10 random patterns with Bonferroni correction → near-perfect detection on Eq. 3 at γ=0.05. Mean 0.828, median 0.833 at a single random pattern [p. 4, §3.2]. |
| Missing complementarity recommendation | (no mention) | Zanin explicitly recommends applying **both** standard GC and COP-GC to separately detect linear and non-linear relationships [p. 8, §4]. |
| Missing limitations | No caveats stated | COP is **worse** than GC when causality is linear; sensitive to noise and missing values; pattern interpretation complex; single-author paper; no music validation [p. 5, Fig. 3; p. 8, §4]. |
| Over-reach in "Relevance to E(t)" | "We can detect these 'hidden' causal links in the OSN-M, providing a much richer view of the social network than simple linear correlation." | P-22 does not test audio-pitch data; any Project 8 claim about P-22 on pitch salience maps is methodological transfer, not evidence. Reframed in §6 as Project-8 plan, not P-22 finding. |
| Missing Bonferroni-abandonment caveat | (no mention) | Zanin drops Bonferroni correction for air-transport case; Project 8 must either keep the correction or rigorously justify dropping it. [p. 7 to 8, §3.5]. |
| Missing single-author caveat | "Zanin, M." | Single-author paper; no internal replication; independent reproduction needed before committing Project 8 to the method. |
