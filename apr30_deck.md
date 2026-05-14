
# Apr 30 Status Meeting II, Deck

**Project 8 · Entanglement in Online Choir · 2026-04-30 · 14:00 CET**

> Format: 8 slides for a 5 to 10 minute presentation (target 8 minutes spoken), per the Apr 14 email from Prof. Peter Gloor. Email rubric covered: Team (slide 2), Goals/Scope (slide 3), Dataset Strategy (slide 4), Overall Project Plan (slide 5), Plan for Next Iteration (slide 6), Way of Working (slide 7). Speaker notes live in [apr30_script.md](apr30_script.md). The Q&A prep bank is in [apr30_qa_prep.md](apr30_qa_prep.md).

---

## Slide 1: Title

**Status Meeting II**

Project 8: Entanglement in Online Choir

SNA-OSN-M Summer 2026 · Uni Bamberg × Uni Köln × HSLU

Presented by Zuraiz, on behalf of the team

Supervisors: Prof. Janine Hacker (Uni Bamberg), Prof. Peter Gloor (MIT, COIN seminar lead)

---

## Slide 2: The Team

**Visual**: 4 portrait circles in a row. Below each portrait, a horizontal bar showing the SC Chat archetype (mirrors the COIN sibling team's slide 2).

| Member       | SC Chat archetype     | Symbiont archetype     |
| :----------- | :-------------------- | :--------------------- |
| Zuraiz       | Tree Hugger (73% Ant) | Ant 38% / Capybara 38% |
| Hammad Anwar | Tree Hugger (64% Ant) | Capybara 49%           |
| Hassan Ahmed | Tree Hugger (63% Ant) | Ant 40%                |
| Kumaran Vasu | Tree Hugger (75% Ant) | Ant 80%                |

All four members are M.Sc. students at Uni Bamberg. Three members continued from the chapter team; Kumaran joined at the project signup. The archetype results are included because the May 21 Virtual Mirror requires us to analyse our own team communication, not because they are the scientific contribution today.

---

## Slide 3: Goals (Scope)

**Visual**: side by side image. Left: an in-person choir in a hall. Right: a Zoom-grid choir. A question mark in the gap.

**Research question**: When a choir sings together over the internet, can we put a number on how well coordinated they are?

We are building a proposed coordination index, called E(t), that combines three measurable signals: audio synchrony, body movement, and a network of who influences whom.

**Where this comes from**

- **Research question**: from the gap between NMP tool studies, which focus on latency/tool quality, and coordination research, which rarely has an objective acoustic outcome.
- **E(t) formula**: inspired by Gloor's entanglement work on team communication and Pentland's Honest Signals, but adapted by us for choir audio/video. The original entanglement formula was validated on email rhythms, not music, so H1-H3 are our validation tests.

**Three falsifiable hypotheses**

1. **H1**: low-latency tools (Jamulus, SoundJack) score higher on E(t) than high-latency tools (Zoom).
2. **H2**: the "who influences whom" network shifts shape between low and high latency, from democratic to leader-dominated.
3. **H3**: adding body-movement signals on top of audio improves how well E(t) tracks coordination, by at least 10 percentage points of explained variance.

Either way the result is publishable. A null finding tells us the latency dichotomy is too crude; a positive finding gives the field its first quantitative coordination meter.

---

## Slide 4: Dataset Strategy

**Visual**: three-tier data pyramid. Bottom: YouTube video. Middle: academic multitrack. Top: controlled latency injection.

**Mental model**: Tier 1 is real-world but messy. Tier 2 is clean but academic. Tier 3 is controlled and experimental.

| Tier | What it is | What we do with it | What it can prove |
| :--- | :--------- | :----------------- | :---------------- |
| **Tier 0: seed URLs** | 5 Jamulus / Choir@Home URLs from Prof. Hacker | Use as examples to guide search terms and inclusion rules | Nothing by itself; it starts the corpus search |
| **Tier 1: YouTube virtual choirs** | 20 to 30 public videos, hand-curated by May 15 | Extract pose, mouth movement, visible synchrony, and ensemble-level audio | Visual coordination and H3 sanity check |
| **Tier 2: academic multitrack** | Dagstuhl ChoirSet, ESMUC, ChoralSynth | Use separate singer tracks for pitch, onset timing, and Granger influence | Per-singer audio, A(t), N(t), directed graph |
| **Tier 3: latency injection** | Artificial Zoom-class / low-latency versions of Tier 2 | Add delay, jitter, and packet loss, then recompute E(t) | Clean H1 test because latency is known |

**Important limitation**: Tier 1 YouTube audio is mixed stereo, so it cannot support per-singer Granger networks. That is why H1 and the influence graph rely on Tier 2 and Tier 3.

**Guardrail**: no self-recording and no third-party choir recruitment in this project phase. We use public videos and published datasets, then keep only derived features after extraction.

---

## Slide 5: Overall Project Plan

**Visual**: Gantt-style horizontal timeline with three coloured phase bands and 7 status-meeting markers. Today's marker (VS#2) shown with a red triangle.

**Three phases**

| Phase                                 | Window           | Goal                                             |
| :------------------------------------ | :--------------- | :----------------------------------------------- |
| **Phase 1: Scope and Scaffold** | Apr 16 to Apr 30 | Scope, dataset strategy, repo scaffold           |
| **Phase 2: Build and Analyse**  | May 1 to Jul 7   | Audio, video, network pipelines; E(t) end-to-end |
| **Phase 3: Synthesise**         | Jul 8 to Jul 31  | Paper, dashboard, final presentation             |

**Status meeting calendar**

VS#1 Apr 16 (kick-off) · **VS#2 Apr 30 (today)** · VS#3 May 21 (Mirror Session) · VS#4 Jun 11 · VS#5 Jun 25 · VS#6 Jul 9 (pre-final review) · Final Jul 23 · Paper due Jul 31.

**Phase-based milestones (status dots: green done, amber in progress, grey not started)**

| Milestone                                            | Phase | Status |
| :--------------------------------------------------- | :---: | :----: |
| Research question, hypotheses, and data tiers defined |   1   | green |
| Repo scaffold ready (package, CI, smoke tests)        |   1   | green |
| Current data state recorded: seed URLs only           |   1   | green |
| Tier 2 academic datasets on disk with manifest        |   2   | amber |
| Tier 1 YouTube corpus curated with inclusion log      |   2   |  grey  |
| Video pipeline producing per-singer pose data         |   2   |  grey  |
| Network pipeline producing influence graph            |   2   |  grey  |
| E(t) computed end-to-end on full corpus               |   2   |  grey  |
| Dashboard alpha (60-second live demo target)          |   2   |  grey  |
| Paper draft v1                                        |   3   |  grey  |
| Final presentation and final paper submitted          |   3   |  grey  |

---

## Slide 6: Plan for the Next Iteration

**Sprint 2: Apr 30 to May 21 (3 weeks, ending at VS#3 Mirror Session)**

**Visual**: 4-row table with phase colour stripe on the left (matches the COIN sibling team's Sprint 2 slide).

| Work Package                                   | Next Step                                                                                                                                                                                                     | Output                                                                      |
| :--------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :-------------------------------------------------------------------------- |
| **Audio pipeline**                       | Pull academic multitrack datasets to disk (Dagstuhl ChoirSet, ESMUC, ChoralSynth). Run pitch tracking and onset detection.                                                                                    | Per-singer feature parquet for 5 multitrack pieces, by May 8.               |
| **Video pipeline**                       | Run MediaPipe Pose and FaceMesh on the first 10 YouTube virtual-choir videos. Calibrate against a published pose ground truth.                                                                                | Per-singer pose parquet plus a 1-page calibration note, by May 22.          |
| **Curated corpus and GDPR**              | Hand-curate 20 to 30 YouTube virtual-choir videos (no post-production edits). File the GDPR DPIA outline with the Bamberg data-protection officer (face-mesh landmarks are biometric data under Art. 9 GDPR). | Corpus manifest with SHA-256 hashes by May 15. DPIA outline by May 21.      |
| **Virtual Mirror (seminar requirement)** | Export the team WhatsApp chat. Run it through the SocialCompass tools (SC Chat, Symbiont, Beecome). Classify the team archetype with all 4 members.                                                           | Mirror write-up with archetype classification, presented at VS#3 on May 21. |

Each row ends in a defined deliverable, not a status update.

Dataset construction in Sprint 2: Tier 2 on disk first, Tier 1 curated second, Tier 3 generated from Tier 2 after the audio pipeline can run.

---

## Slide 7: Way of Working

**Visual**: 3 side-by-side columns, each with a heading icon and 4 bullet pairs (mirrors the COIN sibling team's slide 5).

| **Cadence**                                             | **Sync**                                          | **Toolstack**                                                                    |
| :------------------------------------------------------------ | :------------------------------------------------------ | :------------------------------------------------------------------------------------- |
| **Format**: 3-week sprints aligned to status meetings   | **Weekly**: 30-minute team sync                   | **Code and CI**: Python, Git, GitHub Actions  |
| **Sync**: pre-VS review 1 to 2 days before each meeting | **Daily**: async status post per person           | **Docs**: Markdown source of truth, plus method notes in Obsidian |
| **Delivery**: each sprint ends in a defined artefact    | **Channels**: WhatsApp group, GitHub Issues       | **Quality**: pre-commit hooks (ruff, mypy), peer review via PR                   |
| **Meeting**: VS with supervisors per sprint             | **Supervisor**: weekly check-in with Prof. Hacker | **Meetings**: Zoom for VS, screen-share for live demos                           |

The team WhatsApp group, set up per Prof. Gloor's Apr 14 instruction, is also our input data for the Virtual Mirror on May 21.

---

## Slide 8: Thank you

**Visual**: clean closing slide. Project name in large type, presenter name, contact email, a thin red accent line.

Thank you for listening. Open to your questions.
