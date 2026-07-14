# Jul 23 Final Presentation, Q&A Prep

Private prep. Short answers first; expand only if pressed. Numbers updated to the
2000-shuffle grid (`_latency_grid_2000.csv`) and the H3 run (`_h3_visual_onset.csv`).

---

## Main Result

### Q1: What is the main result?

**Short**: H1 is supported in the timing channel. Jitter strongly degrades zero-lag onset synchrony while loudness-envelope coupling stays flat.

**Backup**: Clean to Zoom-class drops at the 2000-shuffle null: 56.5% Dagstuhl, 65.1% ESMUC, 75.1% ChoralSynth, 70.7% across all 28 pieces, monotonic per piece.

**If pressed**: The contribution is the dissociation. A lag-tolerant envelope metric would have missed the latency effect entirely; onset timing is the physical channel latency damages.

### Q2: Why did the numbers change slightly from earlier meetings (57/66/76)?

**Short**: They did not change; they got more precise. Earlier decks rounded to whole percent from the 100-shuffle grid; the paper-grade 2000-shuffle rerun (2026-07-14) gives the same values at one decimal: 56.5 / 65.1 / 75.1.

**Backup**: Onset synchrony is deterministic; shuffles only sharpen the null distribution and p-values. The rerun changing nothing is itself a robustness check.

### Q3: Why did constant delay fail first?

**Short**: Envelope coupling searches over lags, so a constant shift is absorbed. Its own control caught it; we kept the null and moved to jitter plus onset synchrony, specified a priori.

---

## H2

### Q4: Is H2 supported?

**Short**: Partially. Human influence networks show weak but real leadership structure above a density-matched random null; the original latency-driven form is untestable with injected delay.

**Backup**: Observed corpus mean out-degree Gini 0.154 vs null 0.138 (1000 matched random digraphs per piece). Dagstuhl 3/5 significant, ESMUC 2/3, ChoralSynth 2/20 (chance).

**If pressed on 0.138 vs 0.139 in older docs**: rounding; the committed CSV mean is 0.1381. The deck cites the CSV.

### Q5: Why Gini of out-degree rather than eigenvector centrality?

**Short**: Out-degree captures the "who drives whom" asymmetry leadership means here, and a distribution-level measure is robust where top-node labels are not.

**Backup**: On near-complete graphs eigenvector centralities are near-tied and the top-node label flips with node ordering (observed Soprano/Alto near-tie at 0.53). Freeman degree centralization would rank the same graphs similarly and can be added in the report.

---

## H3

### Q6: You promised a visual-onset analysis. What happened?

**Short**: We ran it, and the result is null. 17 of 18 pose-usable videos analyzable; 1/17 significant at p < 0.05, which is chance; median max-lag r 0.068.

**Backup**: Method: pose-derived motion (sway + breathing channels) vs the audio onset envelope on a shared 10 Hz grid, best lag within ±2 s, 1000 circular-shift nulls per video, first-minute window. One video was excluded because its first 90 s are digitally silent; the exclusion is flagged in the CSV, not hidden.

**If pressed (is the method broken?)**: No. The estimator recovers known lags on synthetic coupled signals and rejects independent ones; those tests run in CI. The null is informative about the data configuration: one tracked body stream against a mixed audio track carries no detectable coupling.

### Q7: So is H3 falsified?

**Short**: No. The ΔR² claim was never tested, because no corpus piece has per-singer audio and video together. What the null adds: the cheap substitute (ensemble video vs mixed audio) demonstrably does not work, so the paired-corpus requirement is now evidence-backed, not an excuse.

### Q8: Why only the first minute of each video?

**Short**: That is the window the pose pipeline processed (600 frames per video at ~10 Hz effective rate); it is stated on the slide and in the limitations.

**Backup**: Extending pose extraction over full videos is future work; there is no reason to expect the first minute to be atypical for a performance video, though intros/silence are a real hazard, which is exactly what the silent-window exclusion documents.

---

## Dashboard / Demo

### Q9: Is the dashboard real?

**Short**: Real alpha: real E(t), real Granger GEXF graphs, real pose parquet overlays, real per-piece metadata. Local-first, no hosted backend.

### Q10: What if the live demo fails?

**Short**: Slide 11 is the same content as one frame (`wp4_dashboard_realdata.png`); we narrate it and move on. The demo path and the fallback were both rehearsed.

---

## Reproducibility

### Q11: Can the results be reproduced?

**Short**: Yes at the report level: `make reproduce` regenerates summary artifacts from committed outputs; 44 automated tests cover the pipeline; the 2000-shuffle grid protocol (SLURM array, merge, completeness check) is committed and was validated on NHR@FAU.

**Backup**: Full raw extraction depends on large gitignored media by design (legal + size); the committed layer is summaries, figures, and code.

### Q12: What went wrong on the cluster? (if asked about the rerun)

**Short**: Two infrastructure lessons, both fixed in the committed script: SLURM jobs must not inherit the submitter's PATH, and concurrent `uv run` invocations must not sync the environment (65 tasks failed when the venv was stripped mid-run; `uv run --no-sync` makes tasks read-only on the environment).

---

## Supervisors

### Q13: What do we want from Prof. Hacker?

**Short**: Whether the narrowed, operationalized H2 claim (out-degree Gini vs matched null) is the right level for the report, and whether the influence-graph figure should carry more of the final narrative.

### Q14: What do we want from Prof. Gloor?

**Short**: Whether the E(t) domain-transfer caveat is framed correctly: first music-domain test of an email-validated construct, supported in the timing channel, with the honest-signals visual channel now evidence-blocked rather than assumption-blocked.

### Q15: Biggest final-presentation risk?

**Short**: Demo reliability, mitigated by rehearsal on the presentation laptop and the fallback slide. The scientific results are stable and committed.
