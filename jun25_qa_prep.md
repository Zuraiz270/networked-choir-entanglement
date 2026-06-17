# Jun 25 Status Meeting V, Q&A Prep

Private prep. Each Q: short answer (read cold), backup detail, if-pressed depth. Escape hatch: "I'll confirm with the team and follow up by email." Deflect by owner: audio/integration → Zuraiz, pose → Hammad, dashboard → Kumaran.

---

## Headline / H1

### Q1: So does latency hurt coordination or not?
**Short**: Yes, but in attack timing, not loudness. Onset synchrony drops 57-76% from clean to Zoom-class jitter across three datasets; the loudness-envelope E(t) is flat.
**Backup**: Our composite E(t)'s audio term is a 10s loudness-envelope correlation, which is physically robust to tens-of-ms timing noise. The quantity latency actually breaks is whether singers attack notes together, measured zero-lag. That degrades strongly and monotonically.
**If pressed**: This is why metric choice matters: a loudness-only metric would have falsely concluded latency is harmless. The dissociation between the two measures on identical data is the contribution.

### Q2: Did you engineer onset synchrony to get the result you wanted?
**Short**: No. It was chosen a priori as the physical quantity latency breaks, and we report it regardless of outcome.
**Backup**: Jitter SDs are the *measured* P-11 inter-chorister timing SDs (46/57 ms), not tuned. We also report the failed constant-delay manipulation and the flat envelope result, the full journey, not just the win.
**If pressed**: Onset synchrony smooths each onset train with a ~70 ms tolerance (near the Ensemble Performance Threshold) and takes zero-lag correlation. Zero-lag is the key: it cannot absorb a shift the way the lag-searching coupling does.

### Q3: Why inject latency instead of using real networked recordings?
**Short**: We have no real per-singer audio recorded under controlled latency. Studio multitrack + controlled injection is the only way to vary latency while holding the performance fixed.
**Backup**: Tier-1 YouTube has real NMP regimes but mixed audio (no separable singers). Tier-2 is clean multitrack with ~zero latency. Injection bridges them.
**If pressed**: Limitation, stated openly: injection models transmission delay, not a live singer's behavioural adaptation to hearing others late. That's a genuine ceiling on this design; real low-latency-vs-high-latency recordings would be the gold standard.

### Q4: Is the network/topology hypothesis (H2) supported?
**Short**: Not cleanly yet. Granger density rose under injection, but that's partly an artifact of fixed-lag testing on delayed streams, so we're cautious.
**Backup**: We report density but flag the artifact. A latency-robust topology measure is next-iteration work.
**If pressed**: H2 needs per-window networks and a delay-aware Granger formulation; queued.

## Data / method

### Q5: Why these three datasets, and is ESMUC/ChoralSynth legit?
**Short**: Dagstuhl + ESMUC are real human multitrack (open on Zenodo, CC BY); ChoralSynth is open synthetic SATB (CC BY-SA). All downloaded and MD5-verified against Zenodo.
**Backup**: 28 pieces total. ESMUC turned out to be 7 songs / 48 multitrack groups (not the "3 pieces" the paper implies), we verified the real structure on disk before using it.
**If pressed**: ChoralSynth's absolute coupling is weaker (machine-rendered), but it's a useful third corpus; the two human datasets are the primary evidence.

### Q6: What does "p < 0.01" mean here?
**Short**: Per cell, observed mean E vs 100 circular-shift permutations; none exceeded observed in the strong cells. The paper-scale run uses 2000 shuffles.
**If pressed**: Circular shift preserves within-stream autocorrelation; it's the standard coordination null.

## Scope / logistics

### Q7: Where's the visual hypothesis (H3)?
**Short**: Still blocked, no piece has audio and video together. The integration code is ready for V(t) when multimodal data exists.

### Q8: Do you actually need the cluster?
**Short**: Not for what you've seen, that all ran on a laptop. The cluster is for the final paper-scale run (full corpus, per-window networks, 2000-shuffle null), roughly 1,500 core-hours. ki-support contacted, Prof. Hacker CC'd.

### Q9: Is the dashboard real or mock now?
**Short**: Real. Timeline = real E(t), graph = real Granger GEXF, video panel = real mp4 + real pose overlay. Each piece serves the signals it has.
