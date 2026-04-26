# Apr 30 Status Meeting — Speaker Script and Q&A Playbook

**Project 8 · Entanglement in Online Choir · 2026-04-30 · 14:00 CET**

> Companion to [apr30_deck.md](apr30_deck.md). One presenter (Zuraiz). The supervisors are Prof. Janine Hacker (primary, Uni Bamberg) and Prof. Peter Gloor (second grader, Uni Köln, ex-MIT). The script is yours; speak from it, do not read it.

## Before the meeting (T-30 min checklist)

- [ ] Slide deck open and on the right screen (use the rendered version, not the raw markdown).
- [ ] Backup PDF of the deck on a USB stick or in a local folder (if Wi-Fi or screen-share fails).
- [ ] One-page text summary printed on paper (last-resort fallback).
- [ ] Camera on, mic tested. Battery > 50% or charger plugged in.
- [ ] PROJECT_GUIDE.md open in another tab (you will reference §11.5 verification tests, §12 limitations register, and the §11.4 evidence trails).
- [ ] `onsidian vault/OSN-M/wiki/00_overview/deep_read_audit.md` open (you will reference deep-read corrections if a source is challenged).
- [ ] Glass of water within reach. Phone on silent.
- [ ] Slide 6 (the two-column deliverables slide) open in a second tab so you can pull it up if either professor asks about their figure.
- [ ] Read the closing line out loud once before joining the call. The first words are the most fragile.

## Tone

Confident, not cocky. You have done the homework. Acknowledge what is missing, frame open questions as asks for input rather than gaps. You are presenting a plan to two senior researchers; their feedback **is** the deliverable today.

You do not need to convince them. You need to show them you understand both their lenses and that you have made deliberate, defensible choices. Honesty about what you have not yet done is a strength here, not a weakness. They have seen too many decks that overclaim.

---

## Terminology cheat sheet — study this before the meeting

You do not need to memorise the math. You need to be able to say what each term *does* and *why it matters* in one sentence. Everything below is yours.

| Term | What it is in plain English | What to say if asked |
| :--- | :--- | :--- |
| **E(t)** | Your project's main output. A single score (0–1) that says how "in sync" a group of singers is at any moment in time. | "It is a composite coordination index — audio coupling, visual coupling, and network influence, equal-weighted." |
| **A(t)** | The audio part of E(t). Measures whether singers hit notes at the same time and in tune. | "Onset timing, pitch alignment, and tempo stability from the audio track." |
| **V(t)** | The visual part of E(t). Measures whether singers' bodies move together — swaying, breathing, mouth opening. | "Honest Signals operationalised from video: mimicry, activity, consistency." |
| **N(t)** | The network part of E(t). Measures who is influencing whom based on note timing patterns. | "A Granger-causal influence graph on per-singer note onsets." |
| **Granger causality** | A statistical test. If knowing A's past helps you predict B's future *beyond* what B's own past tells you, then A Granger-causes B. It is not philosophical causation — it is predictive causation. | "If A's past note onsets help predict B's, A Granger-causes B. Not correlation — predictive influence." |
| **F-statistic** | The number that comes out of a Granger test. Higher F = stronger predictive influence. | "It quantifies the strength of influence between two singers." |
| **Eigenvector centrality** | A node's importance weighted by how important its neighbours are. A singer is central if they influence other central singers. Think of it as 'who influences the influencers.' | "Not just how many connections, but how important those connections are." |
| **Modularity (Q)** | How clustered the network is. High Q = the network splits into tight groups. Low Q = everyone is equally connected to everyone. | "How cliquey the network is. High Q means you have sub-groups, low Q means it is democratic." |
| **Louvain community detection** | An algorithm that finds natural groupings in a network automatically. We use it to lay out the graph. | "An algorithm that finds natural clusters — we use it to colour-code the graph layout." |
| **Circular-shift null model** | Our random baseline. We shift one singer's time series forward in time by a random amount, then re-run the analysis. This destroys cross-singer timing relationships while keeping each singer's individual patterns intact. We do this 200 times to build a 'chance' distribution. | "It tells us what the graph would look like if timing between singers was random. Our real result has to beat this baseline." |
| **DTW (Dynamic Time Warping)** | A way to measure how similar two sequences of movements are, even if they are slightly out of phase. | "Like measuring how similar two singers' sway patterns are, even if one starts a little later." |
| **pyin** | An algorithm that listens to audio and extracts the pitch (musical note) being sung. | "It extracts the note from the audio — which pitch, and how stable." |
| **F0 (fundamental frequency)** | The actual musical pitch of a sound in Hz. Middle C = 261 Hz. This is 'the note being sung.' | "The pitch — which musical note is being sung, measured in Hz." |
| **Demucs** | An AI model that separates a mixed audio track into instrument stems. It can separate piano from drums, for example. It does NOT separate individual voices in a choir. | "AI audio separation — works for instruments, not for separating individual choir singers." |
| **FaceMesh** | Google's face-tracking tool. It maps 468 points on a face in real-time from video — mouth corners, eyes, nose, etc. | "It tracks 468 facial landmarks from video so we can measure mouth-opening and sync." |
| **MediaPipe Pose** | Google's body skeleton tracker. It extracts 33 body keypoints (shoulders, hips, wrists, etc.) from video. | "It extracts a stick-figure skeleton from video so we can measure body sway." |
| **Honest Signals** | Pentland's 2008 MIT framework. Four unconscious body-language signals that predict team coordination outcomes: mimicry (copying), activity (energy level), consistency (regularity), influence (who shapes whom). | "Pentland's four measurable body-language dimensions — all involuntary, all predictive of team performance." |
| **Alchemical stages** | Gloor's metaphor from Cybernetic Alchemy. Raw data is 'prima materia' and goes through four transformation stages: Nigredo (raw), Albedo (extracted), Citrinitas (computed), Rubedo (interpreted meaning). | "Raw → extracted → computed → interpreted. Each stage refines the data without losing it." |
| **CIN / CLN** | Collaborative Innovation Network (or Learning Network) — Hacker's framework. A CIN is a self-organising group with a shared creative goal, transparent contribution, and no central command. Online choirs are CINs. | "A self-organising creative network — no boss, shared goal, transparent participation." |
| **NMP** | Networked Music Performance. Software that lets musicians play together in real-time over the internet. Zoom is bad at it (~300 ms delay). Jamulus/SoundJack are purpose-built (~50 ms). | "Real-time music collaboration over the internet. Latency is the enemy." |
| **Cohen's d** | A measure of effect size — not whether a difference exists, but how big it is. d = 0.2 is small, 0.5 is medium, 0.8 is large. | "It tells us how meaningful the difference is, not just whether it is statistically real. We are targeting d ≥ 0.5." |
| **ΔR²** | The additional variance explained by adding visual features to a model that already has audio features. If ΔR² = 0.10, visual adds 10 percentage points of explanatory power. | "How much extra prediction power the visual signals add on top of audio alone." |
| **ADF test** | Augmented Dickey-Fuller test. Checks whether a time series has a trend or drift (non-stationary). Granger causality requires stationary data. | "A stationarity check. If data drifts over time, standard Granger is unreliable, so we test first." |
| **Transfer entropy / IDTxl** | A more general measure of information flow that does not require the data to be stationary. Our fallback if ADF fails. | "Our backup for influence measurement if the data has trends that Granger cannot handle." |
| **Dagstuhl ChoirSet** | An academic multitrack choir dataset. Each singer was recorded on their own microphone. CC-BY 4.0. | "Published academic choir recordings, one microphone per singer — our ground-truth audio data." |
| **§60d UrhG** | German copyright law exception for text-and-data mining in research. Allows us to download and analyse YouTube videos for academic purposes. | "The German research copyright exception. We are legally covered to use this data." |
| **DPIA** | Data Protection Impact Assessment. Required under GDPR when processing biometric data. FaceMesh landmarks count. | "The legal document we file before processing facial biometric data." |
| **Parquet** | A file format for storing large structured data efficiently. Think of it as a fast, compressed spreadsheet. | "Our data storage format — like a spreadsheet but much faster for large datasets." |

---

## Speaker notes per slide (full 10-minute version)

### Slide 1 — Title and team (0:00 to 0:45)

> "Good afternoon. Project 8, Entanglement in Online Choir. I am Zuraiz, presenting on behalf of the team. Four members, all from Uni Bamberg. Two of us, Hammad and Hassan, are from the chapter group that presented Chapter 14 during the block course, *Data as Prima Materia*. Kumaran joined us at the project-phase signup."

Look at Hacker first (she is your primary supervisor and ran the block course; she will recognise the chapter reference). Then briefly at Gloor (his framework is the chapter material).

When you point at the table, **gesture at Hassan's row and Kumaran's row specifically**:

> "Each teammate owns one piece of the pipeline. Hassan owns your flagship figure, Prof. Hacker — the directed influence graph. Kumaran owns yours, Prof. Gloor — the alchemical-stage diagram. Hammad owns the computer-vision pipeline that feeds both. I integrate across all four work packages and first-author the paper."

This does three things at once: it (1) signals the distribution is real and accountable, (2) flags each supervisor's flagship figure is assigned to a specific teammate for follow-up conversations, and (3) positions you as the integrating lead without understating teammate work.

Do not over-narrate the rest of the table. Move to slide 2.

> "Full role definitions are in our team brief, linked from the bottom of this slide, if anyone wants to see what each of us is doing week by week."

### Slide 2 — The problem (0:45 to 2:15)

This is your strongest slide. Slow down here.

> "Millions of people sang together over the internet during COVID. Every one of them felt the difference between a Zoom choir and an in-person choir. There is no number that captures that difference."

Pause. Let the silence sit.

> "Tool developers design by intuition. Music educators plan remote programs by anecdote. Researchers cannot compare one setup against another. **We are building that number.**"

> "Why choirs? Coordination is acoustically measurable in choirs in a way it is not in meetings or negotiations. Two singers either hit the same note at the same moment, or they did not. The recording shows it in milliseconds. That is what makes choirs the *Drosophila* of coordination science."

The Drosophila phrase lands with both supervisors. Hacker because it sounds rigorous; Gloor because he likes pattern-spotting metaphors.

> "And the binary we are testing is genuinely binary. Either latency is a hard ceiling on coordination, in which case NMP tools need fundamentally new architectures and remote-music-education programs over the threshold are wasting public money. Or bodies compensate through visual cues, in which case Honest Signals theory gets its cleanest external test and the design lesson flips to prioritising visual fidelity. Both findings are publishable."

### Slide 3 — E(t) (2:15 to 3:45)

The most important slide for credibility. Slow down for the caveat.

> "Entanglement Index, E(t). Composite of three sub-indices: audio coupling, visual coupling, and a network coherence term. Equal-weight baseline; we are not learning the weights. At this sample size, complexity without validation is not science."

> "Audio captures onset synchronisation, pitch alignment, tempo stability. Visual captures trunk sway, breath rhythm, mouth-aperture sync; that is where the Honest Signals operationalisation lives. Network is a Granger-causal influence graph on per-singer note onsets, with density, modularity, and centrality as features."

Now the caveat. **Do not skip this**. Both supervisors will respect you more for surfacing it.

> "I want to be upfront about provenance. Gloor's entanglement formula in the original 2022 paper was validated on email patterns over 7-day windows, with modest effect sizes and small case studies. **Our application to choir audio is a novel domain transfer.** H1, H2, H3 are the first empirical test of E(t) on music. We are not claiming pre-existing validation we do not have."

If Gloor reacts to this (he might smile — it shows you actually read his paper), let him say something. If he does not, push on.

> "Three falsifiable hypotheses. H1, regime discrimination at Cohen's d ≥ 0.5. H2, network topology shift at p < 0.05. H3, visual features add ΔR² ≥ 0.10 over audio alone. If any fails, we report it honestly. A negative result is a contribution."

### Slide 4 — Three data tiers (3:45 to 5:00)

> "Three tiers of data, each filling a specific job. Hacker's five Jamulus URLs are Tier 0; we have those. Tier 1 is hand-curated YouTube virtual-choir videos, twenty to thirty pieces, no post-produced material. Tier 2 is academic multitrack: Dagstuhl ChoirSet, ESMUC, ChoralSynth — separate microphone per singer. Tier 3 is controlled latency injection on the Tier 2 audio."

> "One key design decision worth flagging. We do not use Tier 1 YouTube to test the latency hypothesis. Mixed-stereo audio cannot be separated into per-singer streams; Demucs separates instruments, not voices, and pyin is monophonic. So H1 runs on Tier 3 controlled injection. That is actually **better science** than natural YouTube comparisons would be, because we know the latency profile we injected. There is no hidden ground truth to argue about."

> "Legal basis: §60d UrhG and EU DSM Article 3, the German and EU statutory text-and-data-mining research exceptions. Mp4s are deleted after feature extraction. GDPR DPIA in progress because FaceMesh landmarks are Article 9 biometric data."

### Slide 5 — Where we are today (5:00 to 5:45)

> "Status today. Evidence layer is done: I re-ingested all 27 primary and secondary sources full-text against the original PDFs over the last two days, replacing prior shallow digests. The audit log lives in the vault and traces every claim to a page citation."

> "Repo scaffold landed yesterday: pyproject, lockfile with 166 packages and numpy 1.26.4 pinned, GitHub Actions CI, three smoke tests passing. uv-only setup, no Docker. A teammate can clone and reach a green smoke test in under twelve minutes."

> "Documentation: PROJECT_GUIDE.md v1.1 is the single source of truth. Zero feature code yet. WP1 audio pipeline lands May 8 on Dagstuhl. We are on schedule. No critical blockers."

This slide is the credibility slide. You have done real work. State it once and move on; do not dwell.

### Slide 6 — What we will deliver (5:45 to 7:00)

This is a two-column slide. Left is the network graph (Hacker's lens). Right is the alchemical pipeline (Gloor's lens). Walk left to right.

> "Slide 6 shows our two flagship deliverables side by side."

**Left column — directed influence graph:**

> "On the left, the directed influence graph. Eight nodes for eight singers — soprano, alto, tenor, bass pairs. An arrow from singer A to singer B means A's note onsets statistically predict B's onsets in a ten-second sliding window. That is Granger causality: not correlation, predictive influence. Edge thickness is the F-statistic — how strong that influence is. Node size is eigenvector centrality, meaning who influences the most influential people."

> "We will report four numbers on this graph: density, modularity, centrality Gini, and count of bidirectional edges — all tested against a 200-shuffle circular-shift null model. The H2 prediction is that at low latency the graph is democratic — everyone influences everyone. At high latency it collapses to a hub-and-spoke: one leader, everyone else following. **That collapse is the network signature of the regime shift.**"

Brief eye contact with Hacker. Pause one beat.

**Right column — alchemical pipeline:**

> "On the right, the alchemical pipeline. Four stages from raw to meaning. Nigredo — raw inputs, the mp4 files and audio. Albedo — what we extract: body keypoints, separated audio stems, pitch tracks, face landmarks. Citrinitas — what we compute from those: the three sub-indices, pairwise timing alignments, Granger graphs. Rubedo — what we interpret: the E(t) timeline, the influence graph, regime classification, and paper figures."

> "The mapping is direct from Cybernetic Alchemy Chapter 14. Each stage refines the data; nothing is thrown away, it becomes higher-order meaning. That transformation is itself the methodological contribution."

> "On Honest Signals: V(t) covers three of Pentland's four dimensions — mimicry, activity, consistency. The fourth, influence, is in N(t). All four are accounted for across the two sub-indices."

Brief eye contact with Gloor. If he wants to riff on alchemy, let him. That is the meeting going well.

### Slide 7 — Roadmap (7:00 to 7:45)

> "Twelve weeks to July 17. Six iterations. Tier 2 datasets on disk by May 1. Audio pipeline end-to-end by May 8. Tier 1 corpus curated by May 15. Virtual Mirror on May 21 with our own team's WhatsApp data. Video pipeline by May 22. Network pipeline May 31. Full E(t) end-to-end by June 14. Dashboard alpha June 21. Paper draft July 7. Final presentation July 23, paper July 31."

> "Each iteration ends with a deliverable, not a status update. We will keep weekly check-ins with Prof. Hacker."

### Slide 8 — Open items and asks (7:45 to 8:15)

> "Three open items I want to flag transparently. First, GDPR. FaceMesh landmarks are Article 9 biometric data; we are filing under the Article 9(2)(j) research exception with Article 89 safeguards. The DPIA outline is drafted; we need a contact at the Bamberg DPO. That is ask number one."

> "Second, the DUST dataset for realistic packet-loss traces is access-pending. Fallback is to synthesise traces from Carôt and Werner's 2007 published distributions; not as good but adequate for H1."

> "Third, the Tier 1 corpus size. We have set this at twenty to thirty hand-curated videos rather than hundreds, with quality-over-quantity bias. We would like your read on whether this calibration is appropriate for H3."

> "Two specific asks today. Any URLs you would recommend we include or exclude. And any feedback on the two-lens framing before we lock it for the paper. Thank you. I am happy to take questions."

---

## Pacing variants

If you are running long, this is your compress map. The Q&A is what matters; do not steal time from it.

### 5-minute compressed (if they want a quick brief and lots of Q&A)

| Slide | Action |
| :--- | :--- |
| 1 | Title + team in 20 seconds. "Four-person team, Bamberg, Hacker primary, Gloor second grader." |
| 2 | "No metric exists for online-choir coordination. We are building it. Choirs are *Drosophila* of coordination science." 30 sec. |
| 3 | Most of your time. Show formula, name caveat, three hypotheses. 90 sec. |
| 4 | "Three data tiers; H1 runs on Tier 3 controlled injection because mixed YouTube cannot be separated. Legal basis §60d UrhG." 30 sec. |
| 5 | "Scaffold and audit done; zero feature code; on schedule." 20 sec. |
| 6 | Walk left column in 20 sec, right column in 20 sec. "Graph for Hacker, pipeline for Gloor, both delivering July 17." |
| 7 | Skip; say "twelve weeks, six iterations" verbally. |
| 8 | Read the three asks. 30 sec. |

### 7-minute standard (default; assumes ~8 min Q&A in the 15-min slot)

Cover all 8 slides as written. Compress slide 7 (roadmap) to 30 seconds; the timeline is on screen, you do not need to read it.

### 10-minute full

Cover all 10 slides as written. Most likely if Q&A is light or supervisors join late.

---

## Q&A playbook

The structure of an answer in this room: 30-second core answer, then a fallback if pressed, then an honest "we have not tested that" if pushed past your evidence. Never pretend. The supervisors will respect "we have not tested that yet, that is a great prompt for the next iteration" far more than a confabulated answer.

### Predicted questions from Prof. Hacker

#### Q-H1: "Is this a Choir@Home extension? Are you replicating R2.2?"

She wrote R2.2 (the *Choir@Home Tools Survey*). She knows it well.

**Core**: "We have read R2.2 and cite it as the canonical NMP-tool landscape. Our project is adjacent, not replicating. R2.2 is a tool survey; ours is a measurement contribution. We use Jamulus and SoundJack as regimes to discriminate, not as tools to evaluate."

**Fallback if pressed**: "Where R2.2 ends — ranking tools qualitatively — is exactly where E(t) starts: it gives those tools a quantitative discriminator that the survey did not have data for."

#### Q-H2: "Show me the directed influence graph."

You already did, on slide 6 (left column). If she asks again, pull up the slide and walk it again. If she wants more detail, show how the F-statistic is computed.

**Fallback**: "By May 31 we have the first real graph from Dagstuhl. I can send you the SVG the moment it lands."

#### Q-H3: "How are you measuring trust empirically?"

Trust is her core research interest. We are not measuring trust directly. Be honest.

**Core**: "We are not measuring trust as a psychological construct. We are measuring its observable behavioural correlates: timing alignment, mutual prediction (Granger causality), visual mirroring. The hypothesis is that those behavioural patterns covary with the trust state, but we are not making the trust claim ourselves; the published Honest Signals literature is."

**Fallback**: "If you would like us to include a trust-construct survey instrument from the literature in the discussion section, we can. We had scoped that out for time, but it is not architecturally hard."

#### Q-H4: "What about the May 21 Virtual Mirror requirement?"

**Core**: "On track. We will export our team WhatsApp group, run it through SocialCompass, classify the team archetype, and write up the result in the iteration #3 report."

**Fallback**: "We have not started the export yet but the seminar requirement is documented. I will own this."

#### Q-H5: "Are you doing qualitative interviews?"

She likes mixed methods.

**Core**: "Out of scope for this iteration of the project. The decision is recorded in our limitations register. Reasons: ethics overhead for a 12-week project, sample-size limits on qualitative claims, and our hypotheses are operationalisable on existing audio-visual signals. We cite published interview-derived survey instruments — Group Environment Questionnaire, Flow State Scale-2 — in the discussion to frame our quantitative results, but we administer none."

**Fallback if pressed**: "If the timeline opens, we are open to revisiting. Easiest add would be a structured post-hoc interview with a single virtual-choir director already in our Tier-0 corpus."

#### Q-H6: "What is the COIN structure of the choirs you are studying?"

**Core**: "Each Tier 1 choir is a CIN — Collaborative Interest Network. Volunteer participation, shared creative goal, transparent self-organisation, no central command. Some are CLNs at the editing stage if the producer is an alumnus or a returning collaborator. We document the CIN/CLN classification in the corpus manifest."

**Fallback**: "We have not coded each Tier 1 video by COIN type yet. That would be a one-pass annotation exercise; we can include it in the May 15 manifest deliverable."

#### Q-H7: "Why not use the Choir@Home network for data?"

**Core**: "We considered it. Tier 0 already includes your URLs, which is the strongest possible Choir@Home signal. Asking the network for additional contributions would be a second data-collection step with its own ethics review and timeline cost. We chose hand-curated YouTube and academic multitrack to keep the timeline tight, but if you would like to recommend specific Choir@Home outputs to add, we will."

#### Q-H8: "What is your power analysis at n = 30?"

**Core**: "For H1, the statistical power comes from Tier 3, not Tier 1. Tier 3 generates 12 paired observations per Tier 2 piece (4 latency regimes × 3 jitter seeds). With ~10 Tier 2 pieces, that is ~120 paired observations; well-powered for d ≥ 0.5 at α = 0.05. For H3, n = 20 to 30 Tier 1 videos with ΔR² ≥ 0.10 is a demanding effect size we may or may not detect; we will report the confidence interval honestly either way."

**Fallback**: "If your reading is that we should aim for a smaller effect size and therefore expand Tier 1, we can. Quality of curation is the bottleneck, not raw sample-count."

#### Q-H9: "What if the Tier 2 datasets do not include leader/follower labels?"

**Core**: "They do not. Dagstuhl provides per-singer audio with mic crosstalk characterised but no leadership annotation. We infer the leader-follower structure from the data, that is the contribution. The Granger graph is not validated against ground truth labels because no such labels exist; we report graph structure and let the patterns be the empirical finding."

**Fallback**: "If you want a sanity check, the Dagstuhl piece labelled HSM-DYN has a piano accompanist; we can verify the influence graph correctly identifies the piano as a hub."

#### Q-H10: "Why are you running the Virtual Mirror on yourselves and not on the choirs you are studying?"

**Core**: "Two different deliverables. The Virtual Mirror is a seminar requirement on team self-reflection (May 21). The choir analysis is the project deliverable. They share the SocialCompass tooling but answer different questions: archetype classification of *us*, coordination index of *them*."

### Predicted questions from Prof. Gloor

#### Q-G1: "How does this map to the alchemical stages?"

**Core**: "Direct mapping. Slide 6 right column shows it. Nigredo is raw mp4 and wav. Albedo is extracted pose, stems, F0, landmarks. Citrinitas is computed sub-indices and pairwise alignments. Rubedo is E(t), the influence graph, the regime classification, and paper figures. The transformation between stages is the contribution; the data is not lost, it is refined."

**Fallback if he wants more**: "I have read Chapter 14, *Data as Prima Materia*. The framing that the data itself becomes prima materia in the alchemical sense is what we are operationalising — the same data goes through repeated transformations and the meaning emerges in the final stage."

#### Q-G2: "Have you read Cybernetic Alchemy in full?"

**Core**: Be honest. "I have read Chapter 14 in detail and the prologue in full. I have skimmed the other chapters. The directly Project-8-relevant content is Chapter 14 and the introduction's positioning of cybernetic alchemy as the framework. I will read the rest as the paper draft approaches."

He will likely respect this more than "yes, all of it."

#### Q-G3: "What honest signals exactly are you measuring?"

**Core**: "Three of Pentland's four canonical dimensions are in V(t): mimicry as pairwise cross-correlation of trunk-sway and mouth-aperture; activity as the amplitude of those movements; consistency as the variance of inter-singer cross-correlation over time. The fourth, influence, is in N(t) as Granger causality on note onsets."

**Fallback**: "All four dimensions are covered, just split across the V and N sub-indices because of the data substrate. Pentland's original work used badge sensors with all four signals on one device; ours uses video for activity and audio for influence, which is a methodological difference but covers the same conceptual space."

#### Q-G4: "How is this different from Pentland's own Sociometer work?"

**Core**: "Sociometer was a hardware badge in a face-to-face setting, four people in one room. We are operating on remote video and audio, and on choirs rather than business meetings. The biggest methodological difference is that the coordination outcome in choirs is acoustically measurable, which Pentland's settings did not have. We have a ground truth he did not."

#### Q-G5: "Have you considered using SocialCompass on the team?"

**Core**: "Yes. That is the Virtual Mirror requirement on May 21. We will export our team WhatsApp, run it through SocialCompass, classify the archetype, and report the result in the next iteration."

#### Q-G6: "What is your team archetype — Bee, Ant, Butterfly, Capybara, or Leech?"

**Core (honest)**: "We have not run the analysis yet, but my intuition is the team operates closest to a Bee pattern: distributed contribution, shared product, low hierarchy, clear specialisation. That is a hypothesis we will test on May 21, not a claim today."

#### Q-G7: "Why is this not just NMP engineering?"

**Core**: "The NMP literature treats latency as the independent variable and asks whether music can happen at all. We are treating the *coordination dynamics* as the dependent variable and asking what the network and visual signatures of that coordination are. Different question. The NMP work is necessary infrastructure; ours is the measurement contribution on top of it."

#### Q-G8: "Have you reached out to Pentland?"

**Core**: "No, and we have not planned to. Pentland's framework is well-published; the operationalisation choices we are making sit within it without needing his direct input. If you think a short outreach would be productive, that is a conversation to have."

### Predicted methodology challenges (could come from either)

#### Q-M1: "n = 20 to 30 is small. Is this defensible?"

Same as Q-H8. The substantive answer is that H1 is powered by Tier 3, not Tier 1.

#### Q-M2: "What if results are null?"

**Core**: "Null is publishable in this framing. If H1 is null, that says E(t) does not discriminate the regimes, which itself is informative — it means the conventional latency-dichotomy is too crude or our metric is mis-specified. If H3 is null, that says the Honest Signals visual contribution is below our resolvable threshold at n = 20-30. Both are real findings."

#### Q-M3: "Why MediaPipe over OpenPose or DWPose?"

**Core**: "MediaPipe has Pearson 0.80 to 0.91 vs. Vicon for limb keypoints in the published validation, runs natively on Win 11 (our team's platform) without WSL2, and has a stable Python API. OpenPose requires CUDA and Linux for production use. DWPose is technically stronger but the published Project-8-relevant work uses MediaPipe. Trade-off: MediaPipe's head-sway accuracy is unvalidated in the literature, so we calibrate it against a reference tool in WP2 by May 22."

#### Q-M4: "How do you handle stationarity in Granger causality?"

**Core**: "We test stationarity with the Augmented Dickey-Fuller test on the onset-delay residuals. If non-stationary on more than 30% of windows, we fall back to IDTxl transfer entropy, which does not require stationarity. We also run Zanin's COP-GC variant in parallel; ordinal-pattern Granger captures non-linear coupling that standard Granger misses, and Zanin explicitly recommends running both."

#### Q-M5: "What is your null model?"

**Core**: "200-shuffle circular shift on the per-singer streams. Circular shift preserves within-stream autocorrelation while destroying cross-stream timing, which is the right null for coordination versus independent structure. An i.i.d. shuffle would over-reject; a block shuffle would under-reject."

#### Q-M6: "Why not the YouTube Data API?"

**Core**: "API ToS prohibits research scraping at scale and does not give us audio-only download. yt-dlp + per-video license capture is the canonical academic approach and is covered by §60d UrhG. We document this decision in PROJECT_GUIDE §11.4 with the legal evidence trail."

#### Q-M7: "How do you address selection bias in Tier 1?"

**Core**: "Honestly? Imperfectly. YouTube discovery is biased towards popular videos. We mitigate by hand-curating across multiple search queries (virtual choir, Zoom choir, SoundJack choir, distributed choir COVID, SATB virtual, Eric Whitacre virtual choir) and explicitly excluding heavily post-produced content, which is a known editorial confound. The corpus is small enough that hand-curation is feasible. We document each rejection in the manifest."

#### Q-M8: "Why no human-rater validation of E(t)?"

**Core**: "Out of scope, recorded in §12 limitations. Adding human raters would require a panel of trained musicians (recruitment, payment, ethics) and would not fit the 12-week timeline. We argue the falsifiable hypotheses against the latency-regime ground truth are a sufficient first-pass validation; full human-rater calibration is future work."

### Scope and logistics

#### Q-S1: "Who is first author on the paper?"

**Core**: "I am, in my capacity as project lead and WP1 owner. The team contributes substantially across all WPs and is co-authored. Authorship order is documented in PROJECT_GUIDE."

#### Q-S2: "What is the GDPR position?"

**Core**: "FaceMesh landmarks are Art. 9 biometric data. We rely on Art. 9(2)(j) research exception plus Art. 89 safeguards. DPIA outline drafted, full DPIA in progress, Bamberg DPO consult requested. mp4s are deleted after feature extraction. The compliance posture is on the critical path; it is a slide-10 ask today."

#### Q-S3: "Why no self-recording?"

**Core**: "Three reasons. Ethics: we would need IRB approval, lengthening the timeline. Self-selection bias: we are not trained singers. Original scope instruction at project outset explicitly forbade self-recording. We use publicly available YouTube and published academic datasets instead."

#### Q-S4: "Where is the dashboard hosted?"

**Core**: "WP4 dashboard is local-first; it runs on your laptop after `make all`. We do not plan to host publicly during the project. If a stable hosting target is needed for the Jul 23 demo, we will deploy to a personal Hetzner instance for the day; ~€5 cost."

#### Q-S5: "What is the licensing on Dagstuhl?"

**Core**: "Dagstuhl ChoirSet is CC-BY 4.0 with attribution required. ESMUC is CC-BY-NC, non-commercial; we are non-commercial. ChoralSynth is MIT-equivalent for synthetic data. All compatible with academic redistribution of derived features. None are compatible with redistributing the audio itself; we do not."

### Unexpected curveballs

#### Q-U1: "Have you considered EEG hyperscanning?"

**Core**: "It is in the literature ([[hyperscanning]] in our wiki). Out of scope: our project is non-invasive on remote video. Hyperscanning would require lab-recruited dyads. We discuss it in the limitations section as a comparator and note that pose-based behavioural sync is the open-data analogue of EEG hyperscanning."

#### Q-U2: "What about cross-cultural variation?"

**Core**: "Important and out of scope at n = 20 to 30. Tier 1 corpus will skew Western (English-language search queries, popular YouTube). We acknowledge this in the discussion and flag it as the most important external-validity limitation."

#### Q-U3: "What if YouTube takes down videos mid-project?"

**Core**: "We download and SHA-256 fingerprint each video at corpus-curation time. The features we extract are persisted in parquet. If a video is taken down later, we still have the features; we cannot re-extract but we do not need to. The corpus manifest records the original URL, license, and SHA-256 for reproducibility."

#### Q-U4: "What if a music theorist would say your timing definitions are wrong?"

**Core**: "Onset detection is a librosa primitive with well-documented limitations on legato vocal lines. We cross-validate against pyin-derived F0 transitions. Where the two disagree, we flag the segment and exclude it from cross-stream alignment. We are not claiming a music-theoretical onset definition; we are claiming an operational one."

#### Q-U5: "Are you including conducting gestures?"

**Core**: "Where present in the video, MediaPipe Pose extracts the conductor's keypoints alongside the singers. We treat the conductor as a node in the influence graph. In Tier 1 most virtual choirs are leaderless (or the click-track is the leader), so we expect the conductor signal to be sparse. Tier 2 ensembles have conductors; we will look at conductor-led-by-conductor centrality patterns."

### Audience confusion (other students may be in the room)

For these, give a one-sentence definition then return to the supervisor question.

- **"What's E(t)?"** "Composite coordination score combining audio sync, body movement, and influence networks."
- **"What's Granger causality?"** "Statistical test: if A's past helps predict B's future beyond B's own past, A Granger-causes B."
- **"Why alchemy metaphors?"** "Prof. Gloor's framework. Raw data progresses through stages — raw, refined, illuminated, integrated — toward meaning."
- **"What's NMP?"** "Networked Music Performance. Software that lets musicians play together over the internet."
- **"What's the difference between Zoom and Jamulus?"** "Zoom is consumer video, ~300 ms latency. Jamulus is purpose-built for music, ~50 ms latency."

---

## Presenter doubts (your safety net)

### "What if I do not know an answer?"

Say so. Word for word: **"That is a good question and I have not tested it yet. Let me come back to you in the next iteration with a real answer rather than a guess."** Pull out a pen, write the question down visibly. The act of writing it down signals respect.

This is the most powerful move you have. Senior researchers will trust you more for one honest "I do not know" than for ten confabulated answers.

### "What if Gloor wants to ride the alchemy metaphor for five minutes?"

Let him. Listen, take notes, occasionally ask a clarifying question. If he is enjoying himself and you have already covered the slides, that *is* the meeting going well. Do not steer back to the slide deck unless the time slot is genuinely closing.

If you must steer back: "That maps directly onto our Citrinitas stage in slide 8 — should I show that again?" gives you a graceful return.

### "What if Hacker challenges the team composition?"

You are presenting; the team is set. **"Team composition was finalised at the project-phase signup; it is in `Project_Phase_Roster.md` in our vault. Happy to discuss specific role allocations if you have concerns."** If she pushes for a swap, do not commit live. **"Important point. Let me bring this back to the team and respond by Friday."**

### "What if Hacker pushes for qualitative interviews?"

This is the most likely scope-expansion request. See Q-H5.

If she insists, **do not commit on the call**. **"That is a real expansion of scope; let me cost it out and come back to you with two options — minimum viable (one director interview) and full (panel of five). I will have that to you by Friday."**

### "What if I run out of time?"

Have the 5-minute compressed map memorised. The transition from the 7-minute path to the 5-minute path is at slide 3: compress E(t) to 60 sec, skip roadmap verbally, spend 40 sec on slide 6 total. The compressed path still hits all 8 slides.

### "What if the screen-share fails?"

Pull up the backup PDF. If that fails, hold up the printed one-pager and read from it. If that fails, just talk; you know the deck inside out.

### "What if I freeze?"

It happens. **"Sorry, give me a moment."** Drink water. The room will wait. Then continue from where you left off; do not start the slide over.

If your mind goes truly blank: **"Let me pull up slide [N] to ground us."** Pulling up a slide gives you 5 seconds to recover.

### "What if they want to fundamentally change the scope?"

You came with a v1.1 plan. They are giving you input, which is the entire point of this meeting. **Do not commit on the call.** Take notes verbatim. **"This is exactly the kind of input we wanted today. Let me bring this back, weigh it against the timeline, and come back with two options by next iteration."**

The exception: if both supervisors agree on a specific scope change, you can acknowledge agreement on the call without committing to a delivery date.

### "What if they ask for a deliverable I forgot about?"

**"Yes, we have that planned for [iteration N]. I will send you the artefact when it lands."** If you cannot remember when, **"Let me check the iteration plan and get back to you."** Never promise a date you cannot keep.

### "What if they are visibly bored?"

You are still presenting. Their boredom is information; do not mistake it for permission to slow down. Push through to slide 10, which is the asks slide. Most people perk up when the floor is opened to them.

### "What if there is awkward silence after slide 10?"

Hold the silence for five seconds. Researchers process before they speak. If silence persists past five seconds: **"Anything you would like me to expand on, or any aspect you would like us to deprioritise?"**

---

## After the meeting (T+30 min)

- [ ] Take five minutes immediately to write down every question they asked, before you forget. Save in `onsidian vault/OSN-M/raw/apr30_meeting_notes.md`.
- [ ] Send a 3-line follow-up email to both supervisors within 2 hours: thank them, list the asks they made of you with deadlines, attach the deck PDF.
- [ ] Update `wiki/log.md` with a `query` entry summarising decisions and follow-ups.
- [ ] Update `PROJECT_GUIDE.md` §4 status if the meeting changed any project state.
- [ ] If any open item moved (URL list expanded, qualitative interviews scoped in, etc.), update `PROJECT_GUIDE.md` §12 limitations register and §12.9 Pre-Apr-30 Watch List.
- [ ] If they assigned new work, add to the WP1-4 plans and the next iteration deliverable list.

## A reminder

You have done the homework. The vault has 27 deep-read source digests, the scaffold runs green, the corrections are documented. The deck reflects the v1.1 corrections honestly. The mock figures show you understand both lenses.

This meeting is not the project succeeding or failing. It is the supervisors' input *on* the project. Walk in with that frame and you will be fine.
