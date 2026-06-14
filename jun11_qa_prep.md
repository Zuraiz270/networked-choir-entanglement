# Jun 11 Status Meeting IV, Q&A Prep

**Private prep document for Hassan** (presenter). Three categories: Hacker-flavored (network science, trust, engagement), Gloor-flavored (signals, alchemy, framework), General (project management, scope, methodology). Sprint-3 specific questions added 2026-05-22.

Each question has 3 layers:

- **Short answer**: one sentence Hassan can read aloud cold and sound competent
- **Backup detail**: 2 to 3 sentences with concrete numbers if asked to elaborate
- **If pressed**: deepest defensible answer with project-specific data

If Hassan blanks on a deep technical question, the escape hatch is always: *"I'll check with the team and follow up by email."* Better than guessing wrong.

Sprint-3 specific deflection rule: if asked anything outside WP3 (Granger and influence graph), name the owner and offer to loop them in. Zuraiz owns audio + integration, Hammad owns video pose, Kumaran owns the dashboard.

---

## Category 1: Hacker-flavored (network science, trust, engagement)

### Q-H1: What does the headline 5/5 p<0.001 result actually prove?

**Short answer**: That mean E(t) on each Dagstuhl piece is significantly higher than what you would get from shuffling the singer streams against each other, so the coordination signal we measure is not a statistical artifact.

**Backup detail**: The null model is 200 circular-shift permutations per piece. Each shuffle preserves within-stream autocorrelation but breaks cross-stream timing. Across the five pieces the observed mean E(t) sits between 14 and 45 standard deviations above the null distribution mean (weakest: TP_QuartetA at 14.6, strongest: LI_FullChoir at 45). That is well outside chance.

**If pressed**: This is a single-condition test. It proves the metric responds to real coordination, not that E(t) discriminates between low-latency and high-latency regimes (H1) or that visual signals add explanatory power (H3). Those are Sprint-4 and Sprint-5 tests. We are being explicit that Sprint 3 validated the metric, not the hypotheses.

### Q-H2: Why is p_null reported as zero?

**Short answer**: It is not literally zero, it means none of our 200 shuffles exceeded the observed value, so the correct interpretation is p less than 1 in 200.

**Backup detail**: With 200 shuffles, the smallest reportable p_null is 0.005. We can bump to 2000 shuffles for a finer p-value at a cost of about 30 minutes runtime per piece. Happy to do that for the paper if reviewers ask.

**If pressed**: For the deck we round to "p < 0.005" rather than "0.0000" to avoid the literal-zero misinterpretation. Standard practice in coordination science.

### Q-H3: Why are LI pieces clustering above TP pieces in mean E(t)?

**Short answer**: Locus Iste is a homophonic chant where the four voices move together, Tu Pauper Es is more polyphonic with independent voice entries, so we expect LI to score higher on pairwise audio coupling.

**Backup detail**: The split tracks musical structure, not coordination quality and not ensemble size. A four-singer quartet of Locus Iste sits with the eight-singer full choir of Locus Iste, not with the four-singer quartet of Tu Pauper Es. Piece identity dominates.

**If pressed**: This is a useful methodological finding because it means E(t) is sensitive to musical content, not just to whether singers are present. For H1 we will pair pieces against themselves under different latency regimes to control for piece identity.

### Q-H4: What does COP-GC add over standard Granger?

**Short answer**: Standard Granger is parametric and assumes the relationship between cause and effect is linear, COP-GC operates on ordinal patterns and catches non-linear monotonic couplings that the parametric test misses.

**Backup detail**: On Tu Pauper Es full choir, standard found 42 of 56 directed edges significant. COP-GC found 25. The 17-edge gap is edges that depend on linear-magnitude structure rather than pattern structure. We report both, and edges significant under both methods are the robust ones.

**If pressed**: Implementation uses an order-3 Lehmer-code transform per Zanin 2024 (Communications in Nonlinear Science and Numerical Simulation 128, 107606). The ordinal-pattern transform is invariant under monotonic transformations of the input, which is the key property. Mathematically: same null model (circular shift), same F-statistic, only the input series is the difference.

### Q-H5: Why density 0.917 on Locus Iste Quartet A Take 02 and not higher?

**Short answer**: 11 of 12 possible directed edges came back significant against the null. The one missing edge is one ordered pair (cause to effect) that did not beat the null shuffle.

**Backup detail**: For a 4-node directed graph there are 12 possible edges. Density 0.917 means 11 of 12 are significant. That edge density is what we expect from a co-located in-person quartet with no network latency. The interesting question is what density looks like for Zoom-only choir performances, which is the H2 test we still need to run.

**If pressed**: We will report density distributions across pieces, not single-piece point estimates. With 5 pieces in the Sprint-3 corpus (standard method), the LI cluster averages density 0.97 and the TP cluster 0.83, which is consistent.

### Q-H6: Where does H2 stand?

**Short answer**: H2 is testable in Sprint 4 once we have Tier-3 latency injection running. The current N(t) values are all from studio recordings with no latency variation.

**Backup detail**: We have piece-level density and modularity for 5 Dagstuhl pieces. The H2 hypothesis is that topology shifts from democratic to leader-dominated as latency rises, which requires the same piece at different latency levels. Tier-3 controlled injection on Dagstuhl audio gives us that.

**If pressed**: Sprint-4 work plan includes synthetic jitter at four levels matching the NMP regimes, and running E(t) at each level. First Tier-3 numbers expected by June 21.

---

## Category 2: Gloor-flavored (signals, alchemy, framework)

### Q-G1: How does E(t) sit in the alchemical framework?

**Short answer**: A(t), V(t), N(t) are the Albedo stage outputs (purified features from raw signal). The composite E(t) is the Citrinitas stage (illumination, cross-feature synthesis). The full corpus comparison is Rubedo (top-level wisdom).

**Backup detail**: Raw choir mp4s are Nigredo, prima materia. WP1, WP2, WP3 feature extractors are Albedo, purifying raw signal into per-singer streams. E(t) integration is Citrinitas, where the three signals illuminate each other. The cross-piece comparison and eventually the cross-regime comparison are Rubedo, the magnum opus.

**If pressed**: We have an alchemical-pipeline figure at `data/figures/wp4_alchemical_stages.png` from Sprint 2. Kumaran is polishing the SVG version for the paper.

### Q-G2: Why are visual signals absent from current E(t)?

**Short answer**: Because Dagstuhl is audio-only and Tier-1 YouTube is video-only with mixed stereo audio, no single piece in our corpus carries all three signals natively today.

**Backup detail**: The integration code handles this with weight reallocation. When V(t) is NaN, the composite becomes `(A + N) / 2` instead of `(A + V + N) / 3`. This is a deliberate design choice because partial composites are the realistic case for our corpus. The code is ready for V(t) the moment Tier-3 multimodal recordings exist.

**If pressed**: We considered pairing Tier-1 pose extraction with synthetic per-singer audio as a stopgap. Decided against it because the synthetic pairing would not be defensible as scientific evidence. Sprint 4 plan is to either acquire ChoralSynth, which is synthetic SATB with controlled audio, or to record a small multimodal pilot ourselves.

### Q-G3: How do you separate the visual signal from the audio signal in V(t)?

**Short answer**: The visual signal in our V(t) is the variance of three pose-derived honest signals over each 10-second window: shoulder rise as breath proxy, head sway, and trunk lean.

**Backup detail**: MediaPipe Pose gives us per-frame keypoints. We compute three derived features per frame, take their standard deviation over a 10-second window, and combine via tanh-normalized mean. The signal is intentionally about movement energy, not movement content.

**If pressed**: For H3, we need to add visual signals to a model that already has audio signals and check whether the visual signal adds 10 percentage points of explained variance. This is a ridge regression test, not part of E(t) itself.

### Q-G4: Where does the framework go from here?

**Short answer**: Sprint 4 brings cross-regime variation. Sprint 5 brings the paper. The final presentation is a 60-second live dashboard demo.

**Backup detail**: The Jul 23 final presentation includes a working dashboard with the user clicking play and watching E(t) update in real time over a real choir recording with the three overlays. That is the magnum opus.

---

## Category 3: General (project management, scope, methodology)

### Q-T1: Why didn't you also use ESMUC and ChoralSynth?

**Short answer**: Both are openly downloadable from Zenodo; we simply kept the Sprint-3 WP3 corpus at the 5 Dagstuhl pieces and scheduled both for Sprint 4. Not a deliberate exclusion.

**Backup detail**: ESMUC Choir Dataset (Cuesta & Gómez, Zenodo DOI 10.5281/zenodo.5848990) is open, CC BY 4.0, 12 singers, 3 pieces, 2.3 GB, released Jan 2022. ChoralSynth (Narang et al. 2023, MTG/UPF, arXiv 2311.08350) is synthetic SATB, 20 pieces, ~3.8 hours, Zenodo DOI 10.5281/zenodo.10137883. Both fold into Tier-2 the same way Dagstuhl did.

**If pressed**: Our power calculation assumes Dagstuhl (~10) + ESMUC (3) × 4 regimes × 3 jitter seeds = 156 within-piece paired observations for H1. With all three datasets in hand we hit that target; Dagstuhl alone (120) is already well-powered for Cohen's d ≥ 0.50. **Correction note**: an earlier version of this answer wrongly called ESMUC license-restricted. That label was carried over from the P-02 multi-f0 paper's 2019-era dataset table; Cuesta released ESMUC openly on Zenodo in Jan 2022. We verified the open access on 2026-06-11.

### Q-T2: Why is the dashboard showing mock data?

**Short answer**: This is the scaffold deliverable for Sprint 3. The four-panel layout, the data contract, and the end-to-end fetch through Vite proxy to FastAPI are real. Swapping mock data for real parquet readers is the WP4 sub-plan landing by June 21.

**Backup detail**: React 18 + Vite 5 + TypeScript strict + D3 + Plotly. Backend is FastAPI 0.111. Three endpoints stubbed with mock JSON. We verified the end-to-end rendering with a Playwright screenshot. TypeScript strict passes.

**If pressed**: We could have shipped real-data wiring in Sprint 3 instead of mock, but the time budget was better spent on the E(t) integration module and the full-corpus null model run. Tradeoff was deliberate.

### Q-T3: Tests 23/23, what is actually being tested?

**Short answer**: Pipeline correctness on synthetic and real inputs, plus regression coverage for every public function in the package.

**Backup detail**: 4 audio-coupling tests, 4 video-pose tests, 7 network-Granger tests including the COP-GC variant, 5 entanglement integration tests, plus 3 smoke tests for librosa, mediapipe, and the package import. Synthetic inputs cover bounds and edge cases. Real inputs cover the actual corpus.

**If pressed**: The synthetic-coupled-pair test fixture for E(t) has 4 singers driven by a shared RMS envelope plus per-singer noise. Mean E should be high. Independent fixture has 4 singers with no shared signal. Mean E should be at the null. Both tests pass.

### Q-T4: Is the Sprint-2 reference still valid?

**Short answer**: Yes on the substance: the re-run reproduces 11 of 12 significant edges and density 0.917 on the same piece.

**Backup detail**: We re-ran Locus Iste Quartet A Take 02 under the new Sprint-3 batch pipeline with the same parameters and got the same edge count and density. One label changed: "most central voice" is a near-tie at eigenvector centrality 0.53 between Soprano and Alto, and the tie resolves differently depending on node ordering (Sprint 2 reported Soprano, the batch run reports Alto). We treat edge count and density as the regression check and flag the centrality label as tie-sensitive.

**If pressed**: The honest statement is that in a 4-node graph with 11 of 12 edges present, the network is nearly complete and the voices are close to interchangeable by centrality. Single-voice "leader" labels only become meaningful on sparser graphs, like the TP full-choir COP-GC graph at density 0.45. A full edge-by-edge F-statistic comparison is queued for the report.

### Q-T5: Why pull forward the Jun-14 deliverables to May 22?

**Short answer**: Because the E(t) module was the prerequisite for everything else and we had the runtime budget. Phase D and Phase E ran in 8 minutes total once the Pearson-windowed optimization landed.

**Backup detail**: The original brief had E(t) full-corpus as a Jun-14 stretch goal because we feared the 200-shuffle null would be slow. We swapped the full cross-correlation kernel for windowed Pearson, dropped per-shuffle runtime from minutes to seconds, and the full 5-piece corpus run with null came in under 5 minutes.

**If pressed**: That optimization gives us back about 8 hours of compute budget for Sprint 4 if we want to do per-window Granger for time-varying N(t). Net positive.

### Q-T6: Do you need university cluster compute?

**Short answer**: It is a nice-to-have, not a requirement. The planned Sprint-4 scope runs overnight on our laptops; cluster access would let us run denser jitter grids and finer analysis windows for robustness.

**Backup detail**: The Sprint-3 full-piece Granger pass (5 pieces, 2 methods, 200-shuffle null each) took 69 minutes on one Windows laptop. The planned Tier-3 grid (4 jitter levels, 3 seeds, 5 pieces, full-piece Granger) is roughly 60 runs, about 12 to 15 laptop-hours, one overnight run. Nothing in the committed Sprint-4 scope is blocked by compute.

**If pressed**: Where a cluster genuinely helps is the stretch configuration: per-window Granger at fine step sizes with a full null per window scales the cost by an order of magnitude or more, which is where laptop runtimes become days. If cluster time is cheap to grant we would use it for those robustness sweeps; CPU multi-core only, no GPU needed, and the work parallelises trivially across windows and pieces. If not, we constrain the sweep density and the science still happens.

### Q-T7: What if a supervisor asks something only Zuraiz/Hammad/Kumaran would know?

This is for Hassan's reference only.

- DSP-specific, audio pipeline internals, librosa, optimization: *"Zuraiz owns the audio + integration code, he can speak to that more precisely offline."*
- Pose, MediaPipe, OpenPose calibration: *"Hammad owns WP2 and can give you a more precise answer."*
- Frontend, React, D3, Plotly: *"Kumaran owns the dashboard. He can speak to that better than I can."*

Don't deflect questions in your own area (WP3 Granger, influence graph). You own those.

---

## Category 4: Hard questions (read once, do not panic if asked)

### Q-X1: Could your 5/5 p<0.001 result be a multiple-comparisons artifact?

**Short answer**: No, because each piece has its own independent null distribution and we report per-piece p-values, not a corpus-level FWER claim.

**Backup detail**: Each piece's null is 200 independent shuffles of that piece's audio. The p-value per piece is the fraction of shuffles that exceed the observed mean E. We are not running 5 comparisons on a single null and asking "did at least one beat", we are running 5 independent tests with 5 independent nulls.

**If pressed**: If we wanted a family-wise error rate, we would Bonferroni-correct. With 5 pieces at p < 0.005 each, FWER would be approximately 0.025. Still well below 0.05. Happy to report this in the paper.

### Q-X2: Why is N(t) constant per piece in the integration?

**Short answer**: Because per-window Granger multiplies the cost of the Granger pass by the number of windows; the full Sprint-3 pass (5 pieces, 2 methods, nulls) already took about 70 minutes, so a per-window version with fine steps is an order of magnitude more. We use piece-level density as a constant for now.

**Backup detail**: Sprint-4 plan includes per-window Granger to give us a time-varying N(t). The current implementation broadcasts the piece-level density across all windows. This is a documented limitation in `sprint3_results.md`.

**If pressed**: For Sprint 3 the constant N(t) is fine because A(t) is the time-varying signal and dominates the E(t) timeline variance. For the Sprint-4 dashboard alpha we will swap this in.

### Q-X3: Why use density and not some other graph metric for N(t)?

**Short answer**: Density is the simplest network-level scalar that captures "how connected is the influence graph", and it has a natural [0, 1] range so it composes cleanly with the [0, 1] audio coupling and visual variance.

**Backup detail**: Alternatives we considered: average clustering coefficient (less stable for sparse graphs), modularity (only meaningful for >4 nodes), eigenvector centrality of the most-central node (loses information about the rest). Density is the right tradeoff for N(t) as a piece-level scalar.

**If pressed**: For per-window N(t) we may switch to a weighted average of edge significance levels rather than a binary density. That is a Sprint-4 decision.

### Q-X4: Your COP-GC implementation: did you re-validate it against Zanin's paper?

**Short answer**: We tested it against three fixtures: a linear coupled pair (should detect, did), a cubic-monotone non-linear coupled pair (should detect, did), and an independent pair (should not detect, did not).

**Backup detail**: The cubic-monotone fixture is the canonical test case for COP-GC because cube of a stationary AR series is strongly non-linear but monotonic. Ordinal patterns are invariant under monotonic transforms, so COP-GC should still detect coupling there. Our test confirms it does, with the same null model as standard.

**If pressed**: We validated against our own synthetic fixtures rather than re-running the paper's simulation studies; that level of replication was out of scope for Sprint 3. We will revisit if reviewers ask.

### Q-X5: Why not use IDTxl or PyEDM for transfer entropy as a robustness check?

**Short answer**: IDTxl is our documented fallback if standard Granger fails the stationarity test on more than 30% of windows, but we have not hit that threshold in Sprint 3.

**Backup detail**: Decision 4 in our evidence trail (`PROJECT_GUIDE.md` §11.4) explicitly names IDTxl as the transfer-entropy fallback. It is slower and harder to justify a null model for, but it is non-parametric. We will switch if stationarity becomes a problem.

**If pressed**: PyEDM is convergent cross-mapping, which is a different paradigm. Not our planned fallback. If a reviewer specifically asks for CCM we will add a separate evidence section.

---

## Pre-meeting checklist for Hassan

- [ ] Read this Q&A document twice. Once for content, once for tone.
- [ ] Read the script appendix once for project context. Do not memorize the script word-for-word; aim for fluency, not recall.
- [ ] Have `sprint3_results.md` open in a second tab during the meeting for reference.
- [ ] Have `data/figures/et_corpus_comparison.png` open in another tab for the headline slide.
- [ ] Test Zoom 5 minutes before 14:00 CET. Audio on, video on, screen-share tested.
- [ ] If asked a question you don't know, say "I'll check with the team and follow up by email." Do not guess.

Good luck. The team is rooting for you.
