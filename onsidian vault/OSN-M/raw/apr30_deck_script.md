# APR 30 STATUS MEETING — FULL DECK SCRIPT
### Project 8: Entanglement in Online Choir · 14:00 CET · 5–10 minutes
### Presenter: Zuraiz

---

## SLIDE 1: TITLE + TEAM [0:00 to 0:45]

**Title slide**: "Entanglement in Online Choir — Measuring Coordination When You Can't See the Conductor"

Hi everyone. We're Project 8 — "Entanglement in Online Choir." Four members, all from Uni Bamberg.

| Member | Role | Background |
|:---|:---|:---|
| **Zuraiz** | Project Lead · WP1 Audio + Integration | B.Sc. CS · M.Sc. ISSS candidate |
| **Hammad Anwar** | WP2 Computer Vision | B.Sc. CS · M.Sc. ISSS candidate |
| **Hassan Ahmed** | WP3 Network Science | B.Sc. CS · M.Sc. ISSS candidate |
| **Kumaran Vasu** | WP4 Dashboard + Visualization | M.Sc. ISSS candidate |

We formed during the block course. Three of us presented Chapter 14 together, which was about Prof. Gloor's alchemical pipeline — how raw data becomes meaningful patterns. That directly feeds into what we're doing now.

---

## SLIDE 2: THE PROBLEM [0:45 to 2:00]

**Visual**: A split image — physical choir vs. Zoom-grid choir. Red "?" between them.

During COVID, millions of people sang together online. Every one of them felt the difference between "this feels like a room" and "this is fighting the network."

But there is **no number** that captures that difference.

NMP tool developers — SoundJack, Jamulus, JackTrip — design by intuition. Music educators plan remote programs by anecdote. Researchers can't compare one setup against another.

Why choirs specifically? Because coordination is **acoustically measurable**. Two singers either hit the same note at the same moment, or they didn't. The recording shows it in milliseconds. Choirs are the Drosophila of coordination science — clean, high-signal, and available on YouTube.

**The core question**: Is latency a hard ceiling on coordination, or do bodies compensate through visual cues?

---

## SLIDE 3: OUR GOAL — THE ENTANGLEMENT INDEX [2:00 to 3:15]

**Visual**: The E(t) formula with three colored components.

We're building a composite metric called the **Entanglement Index, E(t)**.

```
E(t) = ⅓ · A(t)  +  ⅓ · V(t)  +  ⅓ · N(t)
        Audio         Visual        Network
```

- **A(t)**: Are they singing in time? Onset synchronization, pitch alignment, tempo stability.
- **V(t)**: Are their bodies coordinating? Trunk sway, breathing rhythm, head movement.
- **N(t)**: Who is leading whom? Directed influence networks via Granger causality on note onsets.

The weights are deliberately frozen at equal thirds. At this sample size, complexity without validation is not science.

**Three testable claims:**

1. **H1**: E(t) distinguishes Zoom-class from SoundJack-class with Cohen's d ≥ 0.5.
2. **H2**: The network topology differs between the two regimes (p < 0.05 vs. null model).
3. **H3**: Visual features (Honest Signals) add ΔR² ≥ 0.10 beyond audio alone.

If any claim fails, we report the failure honestly. A negative result is still a contribution.

---

## SLIDE 4: DATA STRATEGY — THREE TIERS [3:15 to 4:30]

**Visual**: Three-tier pyramid diagram.

| Tier | What | N | Purpose |
|:---|:---|:---|:---|
| **Tier 0** | Prof. Hacker's 5 curated YouTube URLs (Jamulus live recordings) | 5 | Seed corpus — already received ✅ |
| **Tier 1** | Hand-curated YouTube virtual choir videos — no post-produced content | 20–30 | Visual analysis (H3). Ensemble audio descriptive only. |
| **Tier 2** | Academic multitrack: Dagstuhl ChoirSet (separate mic per singer) | ~10 pieces | Audio ground truth (H1, H2). Per-singer features possible. |
| **Tier 3** | Controlled latency injection on Tier 2 audio (4 regimes: 20ms → 500ms) | 12× Tier 2 | Clean H1 test. We *know* the injected latency — perfect ground truth. |

**Key design decision**: We do NOT use Tier 1 YouTube for the latency discrimination test (H1). Mixed stereo audio can't be separated into individual singers. Tier 3 controlled injection on multitrack gives us ground truth that natural YouTube never could.

**Legal basis**: §60d UrhG (German TDM research exception) + EU DSM Art. 3. We never redistribute video. Raw mp4s deleted after feature extraction.

---

## SLIDE 5: PROJECT PLAN [4:30 to 6:00]

**Visual**: Gantt-style timeline, Apr → Jul.

| Date | Milestone | Plain English |
|:---|:---|:---|
| **Apr 30** | This meeting | Present scope + plan |
| **May 1** | Tier 2 datasets downloaded | Academic multitrack on disk |
| **May 8** | Audio pipeline v1 | Feature extractor runs end-to-end on Dagstuhl |
| **May 15** | YouTube corpus curated | 20–30 videos selected + manifested |
| **May 21** | Virtual Mirror | WhatsApp communication analysis due |
| **May 22** | Video pipeline v1 | Pose + face coordinates for 10 videos |
| **May 31** | Network pipeline v1 | Directed influence graph for 5 videos |
| **Jun 11** | Virtual status #4 | Progress check-in |
| **Jun 14** | E(t) end-to-end | Full index computed, null model running |
| **Jun 25** | Virtual status #5 | Progress check-in |
| **Jun 30** | Full analysis complete | Numbers for the paper |
| **Jul 7** | Paper draft v1 | First complete draft |
| **Jul 9** | Virtual status #6 | Last check-in before final |
| **Jul 23** | **Final presentation** | 20 min + 60-second dashboard demo |
| **Jul 31** | **Final paper due** | 10 to 20 pages |

**Deliverables at end:**
1. `choir_entanglement` Python package (reproducible in < 15 min via Docker)
2. 8–12 page paper (IEEE/LNCS format)
3. 20-minute presentation with live demo

**Professor-specific outputs:**
- **For Prof. Hacker**: A directed influence graph — who leads whom in the choir.
- **For Prof. Gloor**: An alchemical-stage Honest-Signals diagram — raw signal → meaning.

---

## SLIDE 6: PLAN FOR NEXT ITERATION (May 1–8) [6:00 to 7:00]

**Visual**: Checklist with owner assignments.

What we will deliver by May 8:

| Task | Owner | Status |
|:---|:---|:---|
| Download + verify Dagstuhl ChoirSet | Zuraiz | Starting this week |
| Download Hacker's 5 Tier-0 URLs + metadata | Zuraiz | Starting this week |
| MediaPipe smoke test (Win 11 + Py 3.11) | Zuraiz | By Apr 25 |
| Audio pipeline prototype (librosa pyin on Dagstuhl) | Zuraiz (WP1) | By May 8 |
| Video pipeline prototype (MediaPipe on 1 Tier-0 video) | Hammad (WP2) | By May 8 |
| DPIA outline (GDPR Art. 35 — FaceMesh = biometric) | Zuraiz | By Apr 29 |
| Ingest 6 critical papers into wiki | Zuraiz | By Apr 28 |
| Set up WhatsApp group for team + virtual mirror | All | This week |

**Blockers**: None critical. DUST dataset access still pending — fallback is synthesizing our own latency traces from published distributions.

---

## SLIDE 7: WAY OF WORKING [7:00 to 8:00]

**Visual**: Diagram showing the 4 WPs as a pipeline.

**Evidence-Based Software Engineering (EBSE)**. Every technical decision is documented with an evidence trail — source, confidence level, applicability rating.

**Four Work Packages** feeding into one pipeline:

```
WP1 (Audio)  ──→  A(t)  ──┐
WP2 (Vision) ──→  V(t)  ──┤──→  E(t) ──→  Dashboard (WP4)
WP3 (Network)──→  N(t)  ──┘         └──→  Paper (WP1)
```

**Communication & Tools:**
- **Git** — atomic commits, conventional commits, branched per WP.
- **Obsidian wiki** — every source ingested, every claim traceable to a raw PDF.
- **WhatsApp** — daily coordination (also feeds virtual mirror on May 21).
- **Weekly iteration reports** to Prof. Hacker.

**Iteration cadence:** 6 iterations (Apr 17 → Jul 23). Each ends with a deliverable, not a status update.

---

## SLIDE 8: OPEN ITEMS + GDPR POSITION [8:00 to 8:45]

**Visual**: Three-item list with traffic-light status.

We want to be transparent about what's open:

| Item | Status | Action |
|:---|:---|:---|
| **GDPR / FaceMesh biometric** | 🟡 Position drafted | FaceMesh landmarks are Art. 9 biometric data. We rely on Art. 9(2)(j) research exception + Art. 89 safeguards. DPIA outline by Apr 29. Bamberg DPO consult request filed. |
| **DUST dataset access** | 🟡 Pending | Needed for realistic packet-loss traces. Fallback: synthesize from Carôt & Werner 2007 published distributions. |
| **Cuesta 2020 multi-f0** | 🟠 Stretch only | Per-section F0 from YouTube mixes — not on the critical path. If it works, bonus. If not, we have Tier 2. |

GDPR is on the critical path, not an afterthought. We're raising it now so we can proceed with data work cleanly.

---

## SLIDE 9: CLOSING [8:45 to 9:15]

To summarize:

We're measuring something everyone felt during COVID but nobody quantified. The Entanglement Index gives us a number. Three data tiers give us scientific rigor. And either outcome — hard ceiling or body compensation — is publishable.

We're looking forward to your feedback on the scope and plan.

Thank you.

---
---

# Q&A PREP (internal — not on slides)

**"How is this different from just measuring latency?"**

Latency is one input. Our contribution is showing that coordination is multi-dimensional — audio timing alone doesn't capture whether bodies are compensating. The E(t) index combines audio, visual, and network signals. Latency is the independent variable; E(t) is the dependent variable.

---

**"Why not just record yourselves singing?"**

Three reasons: (1) human subjects ethics — we'd need IRB approval, (2) self-selection bias — we're not trained singers, and (3) the scope instruction explicitly prohibits self-recording. We use publicly available YouTube + published academic datasets instead.

---

**"Isn't 20–30 YouTube videos too few?"**

For the visual analysis (H3), it's sufficient — we're looking for signal, not statistical power on Tier 1. The statistical power for H1 comes from Tier 3, where we generate 12× observations per Tier 2 piece by injecting 4 latency regimes × 3 jitter seeds. Our power analysis shows n = 156 paired observations — well-powered for d ≥ 0.5.

---

**"What's the alchemical connection to Cybernetic Alchemy?"**

Direct lineage. Prof. Gloor's book defines the pipeline from raw data (Nigredo) to meaning (Rubedo). Our system literally follows this: raw video (Nigredo) → extracted features (Albedo) → computed metrics (Citrinitas) → E(t) interpretation + influence graph (Rubedo). The alchemical diagram is one of our two flagship figures.

---

**"Can you actually separate individual singers from YouTube audio?"**

Honestly, no. YouTube gives us a mixed stereo track. Demucs separates instruments, not singers. That's exactly why our H1/H2 tests use Tier 2 multitrack + Tier 3 injection, not YouTube. We document this limitation explicitly in our paper (DSP Reality Correction, §11.6 of our project guide).

---

## TIMING CHEAT SHEET

| Slide | Time | What to do |
|:---:|:---:|:---|
| 1 | 0:00–0:45 | Title + team intro |
| 2 | 0:45–2:00 | Problem framing — "nobody measured it" |
| 3 | 2:00–3:15 | E(t) formula + three hypotheses |
| 4 | 3:15–4:30 | Data tiers + legal basis |
| 5 | 4:30–6:00 | Timeline + deliverables + professor-specific outputs |
| 6 | 6:00–7:00 | Next iteration plan (May 1–8) |
| 7 | 7:00–8:00 | Way of working — WPs + tools + cadence |
| 8 | 8:00–8:45 | Open items + GDPR position |
| 9 | 8:45–9:15 | Closing |

> Total: ~9 minutes. If you're running long, compress Slide 4 (data tiers) to 45 seconds by pointing at the pyramid and saying "three tiers, increasing scientific rigor."
> If audience asks questions during, let them — it counts toward the 10 minutes.
