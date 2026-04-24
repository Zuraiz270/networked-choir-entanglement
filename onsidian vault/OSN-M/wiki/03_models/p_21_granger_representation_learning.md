---
title: P-21 Granger Representation Learning
type: source
alchemy_stage: nigredo
tags: [causality, mcca, lstm, group_dynamics, representation_learning, deep_read]
ingested_date: 2026-04-23
last_deep_read: 2026-04-23
source_count: 1
related: ["[[granger_influence_index]]", "[[hierarchical_group_mapping]]", "[[p_22_augmented_granger_causality]]", "[[deep_read_audit]]"]
team_take: Load-bearing for Project 8's "SATB section → group-level influence graph" pipeline. Method is validated on synthetic Lorenz-96 and rs-fMRI, not music. Needs T ≥ 500 to fit RNN properly, which constrains minimum Project-8 phrase length.
---

# P-21 Granger Causal Representation Learning for Groups of Time Series

**Citation**: Cai, R., Wu, Y., Huang, X., Chen, W., Fu, T.Z.J., Hao, Z. (2024). *Science China Information Sciences* 67(5):152103, 1 to 13. [DOI:10.1007/s11432-021-3724-0](https://doi.org/10.1007/s11432-021-3724-0). Received 12 Nov 2021, accepted 7 Mar 2023, published online 1 Apr 2024.
**Authors & affiliations**: Ruichu Cai, Yunjin Wu, Xiaokai Huang, Wei Chen (corresponding) at Guangdong University of Technology; Tom Z.J. Fu at Peng Cheng Laboratory; Zhifeng Hao at Shantou University.
**Funding**: National Key R&D Program of China 2021ZD0111501; NSFC 62122022, 61876043, 61976052, 62206064; PCL2021A12.
**raw path**: `raw/01_primary_sources/Granger Causal Representation Learning for Groups.pdf`

## 1. Claim

"We propose a Granger causal representation learning method [HGCRM] ... First, we use the multiset canonical correlation analysis method to learn the Granger causal representation of each group of time series. Then, we model the Granger causal relationships among the learned Granger causal representations using a recurrent neural network with temporal information. Finally, we formulate the above two stages into one unified optimization problem" [p. 152103:1, Abstract].

HGCRM targets settings where many low-level time series are grouped into high-level entities (fMRI voxels → ROIs; image pixels → objects; potentially singers → SATB sections) and the causal question is at the group level.

## 2. Method (exact)

**Step 1: MCCA representation** [p. 152103:4, §4.1, Eqs. 3 to 5]:

$$Y_i(t) = A_i^T X_i(t)$$

where $A_i$ is a $p_i$-dim vector solving:

$$\{A_1, ..., A_m\} = \arg\max \sum_{i=1}^{m} \sum_{j=i+1}^{m} W_{i,j} A_i^T \Sigma_{X_i X_j} A_j, \quad \text{s.t. } \|A_i\|_2 = 1$$

$W_{i,j}$ is a binary mask on the causal structure (learned jointly). $\Sigma_{X_i X_j}$ is the cross-group correlation matrix.

**Step 2: Causal structure among representations** [p. 152103:5 to 6, §4.2, Eqs. 6 to 16]:

Granger causal model $Y_i(t) = g_i(q_i(Y^{(<t)})) + E_i(t)$ where $g_i$ is an LSTM-modeled function and $q_{ij}(Y_j^{(<t)}) = W_{i,:j} Y_j^{(<t)}$ if $Y_j$ causes $Y_i$, else 0.

Optimization minimizes prediction error + lasso penalty on $W$:

$$\min_{\theta} \sum_{t=2}^{T} \sum_{i=1}^{m} (Y_i(t) - g_i(q_i(Y^{(<t)})))^2 + \lambda \sum_{i=1}^{m} \sum_{j=1}^{m} \|W_{i,:j}\|_1$$

**Proposition 1** [p. 152103:6]: $W_{i,:j} = 0 \Leftrightarrow Y_j \nrightarrow Y_i$ in the Granger sense.

**Step 3: Joint augmented Lagrangian** [p. 152103:7 to 8, §5, Eqs. 17 to 22]:

Both MCCA vectors $A$ and causal weights $\theta$ optimized simultaneously. Hyperparameters: $\beta = 1.1$, $\gamma = 0.9$, $\lambda$ fine-tuned per case.

## 3. Raw Data Block (synthetic validation)

**Data generator**: Lorenz-96 system with forcing $F = 10$ [p. 152103:8, Eq. 23]:

$$\frac{dY_i(t)}{dt} = (Y_{i+1} - Y_{i-2}) Y_{i-1} - Y_i + F$$

with $X_i = B_i Y_i$ for variable groups.

**Three experimental sweeps** [p. 152103:9]:

1. Number of groups $m \in \{8, 10, 12, 14, 16\}$; avg 4 vars/group; $T = 1500$.
2. Avg vars/group $\in \{2, 3, 4, 5, 6\}$; $m = 12$; $T = 1500$.
3. $T \in \{500, 1000, 1500, 2000, 2500\}$; avg 4 vars/group; $m = 12$.

**Baselines** [p. 152103:9]: MVGC, PCMCI, DYNOTEARS, TiMINo — each run with both Mean-prefix (group mean as representation) and MCCA-prefix (canonical correlation as representation). TiMINo failed in both variants because sample size was too small for its regression + independence tests.

**Metrics**: Precision, Recall, F1. Averaged over 10 runs per case.

**Results** [p. 152103:9 to 10, Figs. 3 to 5]:

| Setting | HGCRM Precision/F1 | Baseline best | Source |
| :--- | :--- | :--- | :--- |
| m = 8-16 groups | Precision **highest** across sweep; F1 stable as m increases | Mean-GC / MCCA-GC F1 drops with increasing m | [Fig. 3] |
| Avg 2-6 vars/group | HGCRM precision highest (slight drop at high vars); Mean-/MCCA-GC precision stuck ~0.72 | — | [Fig. 4] |
| T = 500-2500 | HGCRM precision grows faster than baselines; **underperforms baselines at T=500** | — | [Fig. 5] |

**Ablation** [p. 152103:10 to 11, Figs. 6 to 8]: HGCRM > Mean-HGCRM > MCCA-HGCRM (approximately). Both MCCA representation AND causal-constraint weighting in MCCA are necessary.

## 4. Real-World Validation

**Dataset** [p. 152103:11 to 12, §6.2]:

- Resting-state fMRI (rs-fMRI), subset of enhanced NKI Rockland sample
- TR = **645 ms**, $T = 895$ timepoints
- **1258 voxels** grouped into **7 ROIs**:
  - PCC (116 voxels), LACC (167), LMTG (183), LAG (171), RACC (191), RMTG (188), RAG (242)
- Preprocessed via NiLearn, Destrieux parcellation on Freesurfer fsaverage5 template

**Finding**: HGCRM identifies PCC as cortical hub causing AG, MTG, LACC. Consistent with prior literature (Cao 2014, Tan 2019). Baseline methods produce over-dense graphs that obscure the hub structure.

## 5. Limitations

**Stated** [p. 152103:12, §7 Conclusion]:

- Assumes group memberships are given. Automatic clustering of variables into groups is future work.

**Implicit (binding on Project 8 citation)**:

- All validation is on **synthetic Lorenz-96** and **resting-state fMRI**. No music, no audio, no pose data, no NMP context.
- Method requires $T \geq 500$ samples to fit the LSTM reliably. At $T = 500$ HGCRM underperforms baselines. **For Project 8, this constrains minimum phrase/segment length for group-level Granger analysis.**
- Group dimension reduced to 1 (scalar representation Y_i per group per timestep) by design choice. Multi-dimensional representations not explored.
- Hyperparameter $\lambda$ (lasso) requires fine-tuning per case; no general selection rule given.
- Reported baseline metrics (Mean-/MCCA- variants) are authors' own modifications of published methods, not as-published baselines. Direct comparison against SOTA neural-Granger methods (Tank et al. 2022, Löwe et al. 2022) is not run head-to-head.
- Bi-directional edges (e.g., LAG ↔ LMTG) are resolved by examining time-lag structure, but the paper does not rigorously distinguish genuinely mutual causation from lag-ambiguity artefacts.

## 6. Relevance to Project 8 E(t)

**P-21 is load-bearing for**:

- **SATB section-level influence graph**: each SATB section (soprano/alto/tenor/bass) is a group of singers; their low-level pose/F0/breath timeseries become $X_i$; HGCRM yields a 4-node directed Granger graph. Directly supports Project 8's [[granger_influence_index]] and [[hierarchical_group_mapping]] concepts.
- **N(t) at the section level**: with SATB granularity, we get interpretable "Alto section leads Soprano section at phrase X" edges rather than 50+ individual singer nodes.
- **Combination with P-22**: HGCRM uses standard Granger internally. [[p_22_augmented_granger_causality]]'s COP preprocessing could in principle be swapped in, but this is not tested in P-21.

**P-21 is NOT**:

- Evidence that HGCRM works on audio / pose / musical data specifically.
- Evidence for any specific group granularity in a choir setting (4 SATB sections? 6 stands? 12 voice pairs?).
- A substitute for running standard Granger on individual singers when the research question is about individual leadership, not section-level coordination.
- A solution for variable-group automatic clustering (paper assumes group memberships known).

**Constraint for Project 8**: minimum analysis window ≥ 500 samples (the paper's lower bound for HGCRM reliability). At 30 Hz video sampling this is ~17 s; at 100 Hz audio onset rate this is ~5 s. Relevant for phrase-level vs. performance-level granularity decisions in WP3.

## 7. Corrections Logged Against Prior Digest

See [[deep_read_audit]] for full table. Summary:

| Issue | Prior claim | Corrected reading |
| :--- | :--- | :--- |
| Missing method equations | "Uses MCCA ... A Recurrent Neural Network models the temporal dependencies" | MCCA: $Y_i(t) = A_i^T X_i(t)$ with constraint $\|A_i\|_2 = 1$, maximizing causally-masked cross-group correlation [Eq. 5]. LSTM learns $g_i$ with indicator function $q_{ij}(Y_j^{(<t)}) = W_{i,:j} Y_j^{(<t)}$ [Eqs. 6 to 16]. Joint augmented Lagrangian [Eqs. 17 to 22]. |
| Missing experimental design | (no detail) | Synthetic: Lorenz-96 with F=10, three sweeps (m=8-16, vars=2-6, T=500-2500), 10 runs each, compared vs. MVGC/PCMCI/DYNOTEARS/TiMINo in Mean- and MCCA- variants. Real: NKI rs-fMRI, 1258 voxels, 7 ROIs, T=895 [p. 152103:9, §6.1 and 6.2]. |
| Missing sample-size floor | "Recurrent Neural Network" | **HGCRM underperforms baselines at T = 500**; needs T ≥ 500 minimum to fit reliably [p. 152103:9 to 10, Fig. 5]. Constrains Project 8 phrase granularity. |
| Missing music-validation caveat | "By applying HGCRM to the pitch/pose trajectories of SATB sections..." | Paper has zero music data. Project 8 transfer to audio/pose is plan, not paper finding. Moved to §6 as labeled extrapolation. |
| Missing "Influence Map → prioritize bandwidth" over-reach | "allowing the platform to dynamically prioritize bandwidth for the most influential nodes" | This is a Project 8 speculative application, not in P-21. Removed to avoid reader conflation. |
| Missing authors' Chinese-institution affiliation | "Cai, R., et al. (2024)" | Cai, Wu, Huang, Chen, Fu, Hao — Guangdong University of Technology + Peng Cheng Lab + Shantou University. Funding from Chinese national programs. |
| Missing TiMINo-failure context | (no mention) | Both Mean-TiMINo and MCCA-TiMINo failed because of sample size requirements for regression + independence tests [p. 152103:9]. This is a baseline-comparison caveat. |
