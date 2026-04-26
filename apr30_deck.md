# Apr 30 Status Meeting — Deck

**Project 8 · Entanglement in Online Choir · 2026-04-30 · 14:00 CET**

> Format: 10 slides. Aim for 7-8 minutes of speaking, leave 7-8 minutes for Q&A. The companion file [apr30_script.md](apr30_script.md) carries the speaker notes, three pacing variants, and the full Q&A bank.

---

## Slide 1 — Title and team

**Title**: Entanglement in Online Choir — Measuring Coordination When You Can't See the Conductor

**Status meeting #2** · Project 8 · SNA-OSN-M Summer 2026 · Uni Bamberg × Uni Köln × HSLU

**Team (all Uni Bamberg)**:

| Member           | Lead area                                                        | Primary deliverable                                                                                        |
| :--------------- | :--------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------- |
| **Zuraiz** | Project lead · Audio (WP1) · Integration · Paper first author | `choir_entanglement` end-to-end pipeline, E(t) timeline, paper, today's and Jul 23 presentations         |
| Hammad Anwar     | Computer vision (WP2)                                            | Per-singer pose parquet + MediaPipe calibration study (due May 22)                                         |
| Hassan Ahmed     | Network science (WP3)                                            | **Directed influence graph for Prof. Hacker** (slide 7) — due May 31, publication-polished by Jul 7 |
| Kumaran Vasu     | Dashboard and figures (WP4)                                      | **Alchemical-stage diagram for Prof. Gloor** (slide 8) + 60-second live demo on Jul 23               |

**Supervisors**: Prof. Janine Hacker (Uni Bamberg). Prof. Peter Gloor (Uni Köln).

> *Full role definitions and onboarding for each teammate: `TEAM_BRIEF.md` in the repo root.*

---

## Slide 2 — The problem

**Visual**: side-by-side photo. Left: an in-person choir in a hall. Right: a Zoom-grid of singers. Big red question mark between them.

Millions of people sang together over the internet during COVID. Every one of them felt the difference between "this feels like the same room" and "this is fighting the network."

**There is no number that captures that difference.** NMP tool developers (SoundJack, Jamulus, JackTrip) design by intuition. Music educators plan remote programs by anecdote. Researchers cannot compare one setup against another.

**Why choirs?** Because coordination is acoustically measurable. Two singers either hit the same note at the same moment, or they did not. Choirs are the *Drosophila* of coordination science: clean, high-signal, and available on YouTube at scale.

**The binary we are testing**: is latency a hard ceiling on human coordination, or do bodies compensate through visual cues?

---



## Slide 3 — E(t), the proposed metric

**Visual**: the formula in large type, three colour-coded components.

```text
E(t) = (1/3) · A(t)  +  (1/3) · V(t)  +  (1/3) · N(t)
        Audio              Visual            Network
```

- **A(t)** — onset synchronisation, pitch (F0) alignment, tempo stability.
- **V(t)** — trunk sway cross-correlation, breath-envelope sync, mouth-aperture sync (the Honest Signals operationalisation).
- **N(t)** — Granger-causal influence graph on per-singer note onsets; density, modularity, centrality.

**Provenance caveat (we want to be upfront about this)**: Gloor's entanglement formula in the original paper was validated on email patterns over 7-day windows, n = 111 to 113 per case, modest effect sizes. **Our application to choir audio is a novel domain transfer.** H1, H2, H3 below are the first empirical test of this metric on music. We are not claiming pre-existing validation we do not have.

**Three falsifiable hypotheses**:

1. **H1** — E(t) distinguishes Zoom-class from SoundJack-class with Cohen's d ≥ 0.5.
2. **H2** — Network topology differs between the two regimes at p < 0.05 vs. a 200-permutation circular-shift null.
3. **H3** — Visual Honest Signals features add ΔR² ≥ 0.10 over audio-alone models.

**Either outcome is publishable.** Hard ceiling reshapes NMP-tool architecture priorities. Body compensation gives Honest Signals theory its cleanest external test.

---

## Slide 4 — Three data tiers

**Visual**: a pyramid. Wide base (Tier 1) → narrow top (Tier 3). Annotation: rigour increases as we ascend.

| Tier             | What                                                            | N           | Used for                                                 |
| :--------------- | :-------------------------------------------------------------- | :---------- | :------------------------------------------------------- |
| **Tier 0** | Prof. Hacker's 5 curated YouTube URLs (Jamulus live recordings) | 5           | Seed corpus, already received                            |
| **Tier 1** | Hand-curated YouTube virtual choirs, no post-produced content   | 20-30       | Visual analysis (H3), ensemble-acoustic descriptive only |
| **Tier 2** | Academic multitrack: Dagstuhl ChoirSet, ESMUC, ChoralSynth      | ~10 pieces  | Audio ground truth (H1, H2), per-singer features         |
| **Tier 3** | Controlled latency injection on Tier 2 (4 regimes, 20-500 ms)   | 12× Tier 2 | Clean H1 test, perfect ground truth                      |

**Key design choice**: Tier 1 mixed-stereo YouTube cannot yield per-singer audio (Demucs separates instruments not voices; pyin is monophonic). H1 therefore runs on Tier 3 controlled injection, **better science than natural YouTube comparisons** because the latency profile is known exactly.

**Legal basis**: §60d UrhG (German TDM research exception) + EU DSM Directive Art. 3. Raw mp4s deleted after feature extraction. GDPR DPIA in progress (FaceMesh landmarks are Art. 9 biometric).

---

## Slide 5 — Where we are today

**Visual**: green/yellow/red status bars across four tracks.

| Track                    | Status                                                                                                                                                                                     |
| :----------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Evidence layer** | Done. 27 primary and secondary sources deep-read re-ingested against the original PDFs, replacing prior shallow digests. Audit log committed.                                              |
| **Repo scaffold**  | Done.`pyproject.toml`, `uv.lock` (166 packages, numpy 1.26.4 pinned), Makefile, GitHub Actions CI, three canary smoke tests passing. uv-only, no Docker, < 12 min cold-clone-to-smoke. |
| **Documentation**  | PROJECT_GUIDE.md v1.1 committed (single source of truth). Obsidian wiki has 27 source digests, a live audit log, and Citrinitas/Rubedo concept cascade.                                    |
| **Feature code**   | Zero lines yet. WP1 audio pipeline lands May 8 on Dagstuhl ChoirSet.                                                                                                                       |

We are on schedule. No critical blockers.

---

## Slide 6 — What we will deliver

**Visual**: two-column layout side by side.

**Left — Directed influence graph** *(CIN / network lens)*

Mock-up directed graph. Eight nodes labelled S1, S2, A1, A2, T1, T2, B1, B2 (SATB). Coloured edges with arrowheads. Edge thickness encodes Granger F-statistic. One node (T1) drawn larger to indicate high eigenvector centrality. Caption: "MOCK — synthetic data. Real graph from Dagstuhl by 2026-05-31."

- **Arrow A → B** means A's note onsets Granger-cause B's onsets (10 s sliding window, AIC-selected lag).
- **Edge thickness** = Granger F-statistic. **Node size** = eigenvector centrality.
- We will report density, modularity (Q), centrality Gini — all against a 200-shuffle circular-shift null.
- If the graph collapses from democratic (low latency) to leader-dominated (high latency), that topology shift is the network signature of H2.

**Right — Alchemical pipeline** *(Honest Signals lens)*

Four-stage horizontal flow, colour-coded:

- **Nigredo (black)** — raw inputs: mp4 video, multitrack wav.
- **Albedo (white)** — extracted: pose keypoints (parquet), Demucs stems, pyin F0, FaceMesh landmarks.
- **Citrinitas (yellow)** — computed: A(t), V(t), N(t) sub-indices. Pairwise DTW. Granger graphs.
- **Rubedo (red)** — interpreted: E(t) timeline, influence graph, regime classification, paper figures.

Caption: "MOCK — synthetic example. Real pipeline output by 2026-06-14."

V(t) operationalises three of Pentland's four Honest Signals dimensions (mimicry, activity, consistency); the fourth (influence) lives in N(t).

---

## Slide 7 — Roadmap to Jul 17

**Visual**: Gantt-style horizontal timeline.

| Date                     | Milestone                                                                |
| :----------------------- | :----------------------------------------------------------------------- |
| **Apr 30** (today) | Status #2: this meeting                                                  |
| **May 1**          | Tier 2 datasets on disk (Dagstuhl, ESMUC, ChoralSynth)                   |
| **May 8**          | WP1 audio pipeline runs end-to-end on Dagstuhl, feature parquet produced |
| **May 15**         | Tier 1 YouTube corpus curated (20-30 videos), manifest + SHA-256         |
| **May 21**         | Status #3 + Virtual Mirror (own-team WhatsApp analysis)                  |
| **May 22**         | WP2 video pipeline produces pose parquet for 10 videos                   |
| **May 31**         | WP3 directed influence graph for 5 Tier 2 pieces                         |
| **Jun 14**         | E(t) computed end-to-end on full corpus, null model running              |
| **Jun 21**         | WP4 dashboard alpha (60-second demo target)                              |
| **Jul 7**          | Paper draft v1                                                           |
| **Jul 23**         | Final 20-min presentation + live demo                                    |
| **Jul 31**         | Final paper due                                                          |

Six iterations between Apr 17 and Jul 23. Each ends with a deliverable, not a status update.

---

## Slide 8 — Open items and asks

**Visual**: three-row table with status traffic lights.

| Item                                                           | Status        | Ask                                                                                                                           |
| :------------------------------------------------------------- | :------------ | :---------------------------------------------------------------------------------------------------------------------------- |
| **GDPR DPIA — FaceMesh landmarks are Art. 9 biometric** | In progress   | Who is the right Bamberg DPO contact for our Art. 9(2)(j) + Art. 89 research-exception filing?                                |
| **DUST dataset access (packet-loss traces)**             | Pending       | Do you have a contact at the host institution? Fallback: synthesise from Carôt and Werner 2007 published distributions.      |
| **Tier 1 corpus size — 20 to 30 hand-curated videos**   | Open question | Is this calibration appropriate for H3, or would you rather we expand or contract? Quality over quantity is our current bias. |

**Two specific asks for today**:

1. Any virtual-choir YouTube URLs you would recommend we include or exclude in Tier 1?
2. Any feedback on the two-lens framing (Hacker COIN + Gloor Honest Signals) before we lock it for the paper?

Thank you. Open to questions.
