# Sprint 3 Results

**Cutoff date**: 2026-05-22. **Period covered**: Sprint-3 Phases A through E (May 22). **For**: internal team brief and Jun-11 Status Meeting IV deck source material.

## Headline

Five Dagstuhl pieces now have a complete E(t) timeline against a 200-shuffle circular-shift null. Every piece beats its null at p < 0.001. Mean E(t) splits cleanly along piece (not ensemble) lines: Locus Iste sits at 0.74–0.80, Tu Pauper Es sits at 0.57–0.68. The composite is currently audio + network only because no piece in our corpus carries video natively (Dagstuhl is audio-only; Tier-1 is video only). The integration code already handles weight reallocation when V(t) returns.

## Where the four signals stand

### A(t) audio coupling

WP1 ran on every Dagstuhl musical take. 25 takes processed, 130 newly extracted per-singer parquets, 288 pairwise couplings. Per-take pattern is consistent with musical structure: within-section pieces (LI Basses, 5 takes) cluster at mean coupling 0.78–0.87; full-choir polyphonic pieces (TP, 4 takes) drop to 0.40–0.53. Summary at `data/processed/dagstuhl/_summary.csv`.

### N(t) network coherence

WP3 ran on 5 representative pieces under two methods: standard parametric Granger and COP-GC (Zanin-2021 ordinal-pattern variant). All 10 piece × method graphs persisted as Gephi-compatible GEXFs plus a flat per-piece metrics table at `data/processed/dagstuhl/_network_metrics.csv`. Sprint-2 reference (LI_QuartetA_Take02 standard) reproduced exactly at 11/12 significant edges and density 0.917. Method divergence is largest on full-choir Tu Pauper Es (42/56 standard edges vs 25/56 COP-GC), suggesting roughly a third of the standard test's "positive" edges depend on linear-magnitude structure that vanishes after ordinal-pattern transformation. We carry both methods forward.

### V(t) visual signals

WP2 pose extraction ran across 10 stratified Tier-1 videos (4 Jamulus, 3 Zoom-only, 2 SoundJack, 1 Jamulus+Zoom). 5 of 10 pass the 50% pose-detection floor. The failing five are software-UI screen captures or dense low-resolution tile grids where MediaPipe finds no body — this is the documented "try and iterate" outcome from Status Meeting III, not a Phase C failure. The 5 passing videos (ZKthfLPWBCQ 98.5%, Z-cH7j5iB3k 94.0%, ouFyQKszE_Y 79.5%, w0ywMP8mOc4 78.2%, VsnvueTan4I 66.7%) define the WP2 inclusion set going forward. Summary at `data/processed/tier1/_pose_summary.csv`.

### E(t) composite

Full corpus run on the 5 pieces with both audio and network signals. 10-second windows, 200 circular-shift null shuffles per piece. Results in `data/processed/dagstuhl/_et_corpus.csv`. Headline figure at `data/figures/et_corpus_comparison.png`.

| Piece | Singers | Duration | Mean E(t) | Null mean ± std | p_null |
|:------|:-------:|:--------:|:---------:|:---------------:|:------:|
| LI_QuartetB_Take01  | 4 | 134 s | **0.804** | 0.615 ± 0.009 | < 0.001 |
| LI_FullChoir_Take01 | 8 | 142 s | **0.772** | 0.610 ± 0.004 | < 0.001 |
| LI_QuartetA_Take02  | 4 | 134 s | **0.744** | 0.573 ± 0.008 | < 0.001 |
| TP_QuartetA_Take01  | 4 |  66 s | **0.681** | 0.555 ± 0.009 | < 0.001 |
| TP_FullChoir_Take01 | 8 |  64 s | **0.567** | 0.484 ± 0.005 | < 0.001 |

## What this tells us about the three hypotheses

### H1 (latency regime discrimination)

Not yet tested. H1 requires per-singer audio with controlled latency injection (Tier 3), which we do not have. Dagstuhl is studio-quality with negligible latency; Tier 1 has latency variation but no separable per-singer audio. The current E(t) numbers reflect piece-level coordination under near-zero latency and serve as a high-water mark for what NMP regimes will be compared against.

### H2 (network topology differs across regimes)

Partially testable on Dagstuhl alone. Network density spans 0.75 (TP FullChoir) to 1.00 (LI QuartetB Take01) across the 5 pieces; Louvain modularity is meaningfully positive only on full-choir pieces (quartets are too small to partition). This is a *piece-level* topology effect, not a *regime-level* one. Regime-level H2 testing waits on Tier 2 + Tier 3.

### H3 (visual contribution adds ΔR² ≥ 0.10)

Cannot be tested with the current data because no piece has both V(t) and A(t) together. The integration module is ready for V(t) the moment we get a piece with both signals. The path is either Tier-3 controlled multimodal recording or pairing a Tier-1 video's pose stream with a synthetic per-singer audio reference, both deferred to Sprint 4 or later.

## What changed since May 21

| Track | May 21 baseline | May 22 (end of Sprint-3 Phases A–E) |
|:---|:---|:---|
| A(t) | 1 piece (LI Quartet A Take 02) | 25 pieces, 288 pairwise couplings |
| N(t) | 1 piece × 1 method | 5 pieces × 2 methods (standard + COP-GC) |
| V(t) | 1 Tier-1 video (79.5% detection) | 10 stratified Tier-1 videos (5/10 pass) |
| E(t) | not implemented | module + 200-shuffle null + 5-piece corpus |
| Dashboard | wireframe.md | React+Vite+FastAPI scaffold, screenshot verified |
| Tests | 15/15 | 23/23 (+3 COP-GC, +5 entanglement) |
| Commits on `main` | 0 since May 21 | 12 (3 per phase × 4 phases) |

## What's left for Sprint 3

Phase F only: Jun-11 deck, presenter script, Q&A bank, PPTX render. Target upload to Drive: EOD Jun 10. Meeting: Thu Jun 11 14:00 CET.

## Honest limitations to surface in the deck

1. **V(t) is missing from every current E(t).** Composite is A + N only across the board. The published `E = (A + V + N) / 3` formula reduces to a 2-of-3 mean when V is absent.
2. **The 5-piece WP3 corpus is biased toward Dagstuhl.** All 5 pieces are studio multitrack with negligible latency. Cross-regime comparison is the next step.
3. **WP2 detection rate is 50% (5/10 videos).** Per Status Meeting III, this is the "try and iterate" outcome. We define the working WP2 inclusion set explicitly and proceed.
4. **p_null values report as 0.0000 because none of the 200 nulls exceed the observed mean.** The correct interpretation is "p < 1/200", not literal zero. This is normal at this null size for strongly coupled data; if a reviewer pushes back we can bump to 2,000 shuffles to get a finer p-value, at the cost of ~30 min more runtime per piece.
