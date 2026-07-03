# Jul 9 Status Meeting VI, Q&A Prep

Private prep for Status Meeting VI. Use short answers first; only expand if pressed.

---

## Main Result

### Q1: What is the main result now?

**Short**: H1 is supported in the timing channel. Simulated jitter strongly degrades zero-lag onset synchrony, while loudness-envelope coupling stays flat.

**Backup**: Clean to Zoom-class drops are 57% for Dagstuhl, 66% for ESMUC, and 76% for ChoralSynth. The result is replicated across 28 pieces and three datasets.

**If pressed**: The contribution is the dissociation. A lag-tolerant envelope metric would have missed the latency effect. Onset timing is the physical channel latency actually damages.

### Q2: Does this mean E(t) works?

**Short**: It works as an integration framework, but the Sprint-4 result shows the audio component must include onset timing, not only loudness envelope.

**Backup**: The code now supports onset synchrony as part of the audio component when onset columns are available. The report presents both the old envelope-flat finding and the corrected onset-sensitive interpretation.

### Q3: Why did constant delay fail?

**Short**: Because the old audio coupling searches over lags, so a constant shift is absorbed.

**Backup**: Constant delay is not a realistic enough coordination disturbance for an already recorded studio choir. Jitter is more relevant because it scrambles relative timing frame by frame.

---

## H2

### Q4: Is H2 supported?

**Short**: The original latency-driven H2 is not testable with this design. The corrected H2 is partially supported: human influence networks show weak leadership structure above a random null.

**Backup**: Dagstuhl has 3/5 significant pieces, ESMUC has 2/3, and ChoralSynth has 2/20, approximately chance.

**If pressed**: We should not claim that latency creates hierarchy. Injected delay cannot create a behavioral leader in pre-recorded audio.

### Q5: Why not keep the original H2?

**Short**: Because it would overclaim. Fixed-lag Granger can create density artifacts under delay, but that is not the same as a singer becoming a leader.

**Backup**: The report reframes H2 to the part the data can test: whether clean human choir networks contain leadership structure beyond a density-matched random graph.

---

## H3

### Q6: Is H3 failed?

**Short**: No. It is data-blocked, not falsified.

**Backup**: H3 requires a piece with both separable per-singer audio and usable video. The current corpora split those signals: Tier-2 has audio/network; Tier-1 has video/pose.

### Q7: Should we still mention H3 in the final presentation?

**Short**: Yes, but as an open data-availability issue and future visual-onset analysis path.

**Backup**: Overclaiming H3 would weaken the project. The stronger final story is H1 supported, H2 partially supported, H3 blocked by data availability.

---

## Dashboard

### Q8: Is the dashboard real or just mock?

**Short**: Real alpha. It serves real E(t), real GEXF influence graphs, real pose parquet overlays, and real metadata.

**Backup**: The honest limitation is signal split: no single piece has A, V, and N together. The demo should show one audio/network piece and one video/pose piece.

### Q9: What must be rehearsed before Jul 23?

**Short**: Dependency install, backend start, frontend start, selected demo path, and fallback screenshots.

**Backup**: We should rehearse on the exact laptop used for the final presentation and keep `wp4_dashboard_realdata.png` as a fallback.

---

## Reproducibility

### Q10: Can the results be reproduced?

**Short**: The lightweight report-stage artifacts can be regenerated from committed processed outputs. Full raw extraction depends on large gitignored media and is not appropriate for a normal status-meeting rerun.

**Backup**: `make reproduce` now regenerates the H2 centralization table, the H1 corpus figure, and the Status VI deck.

### Q11: What is still weak before the final?

**Short**: Final verification on a clean machine. In this local checkout, `uv` and Python were not on PATH, frontend dependencies were not installed, and Git safe-directory protection blocked normal status.

**Answer if challenged**: That is environment setup, not evidence against the committed code. But it must be fixed before the final presentation.

---

## Supervisors

### Q12: What do we need from Prof. Hacker?

**Short**: Feedback on whether the narrowed H2 claim is strong enough and how prominently the influence graph should appear in the final.

### Q13: What do we need from Prof. Gloor?

**Short**: Feedback on the final narrative: latency breaks attack timing, and the dashboard/alchemical pipeline shows how raw signals become coordination evidence.

### Q14: What is the final-presentation risk?

**Short**: Demo reliability. The scientific result is stable; the live-dashboard path must be rehearsed and backed by screenshots.
