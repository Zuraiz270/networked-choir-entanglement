# Apr 30 Status Meeting II, Q&A Prep Bank

**Project 8 · Entanglement in Online Choir · 2026-04-30**

> Private Zuraiz prep document. Companion to [apr30_deck.md](apr30_deck.md) and [apr30_script.md](apr30_script.md). Holds the terminology cheat sheet, the predicted-question playbook, methodology challenges, and presenter doubts. The deck and script intentionally drop this material to stay within Prof. Gloor's 5 to 10 minute rubric; the value still lives here for prep.

---

## Terminology cheat sheet

You do not need to memorise the math. You need to be able to say what each term *does* and *why it matters* in one sentence.

| Term | Plain English | One-line answer if asked |
| :--- | :--- | :--- |
| **E(t)** | The project's proposed main output. A single score, 0 to 1, that says how "in sync" a group of singers is at any moment. | "A proposed composite coordination index: audio coupling, visual coupling, and network influence, equal-weighted as the first testable baseline." |
| **A(t)** | The audio component. Whether singers hit notes at the same time and in tune. | "Onset timing, pitch alignment, and tempo stability from the audio track." |
| **V(t)** | The visual component. Whether singers' bodies move together. | "Honest Signals operationalised from video: mimicry, activity, consistency." |
| **N(t)** | The network component. Who influences whom, based on note-timing patterns. | "A Granger-causal influence graph on per-singer note onsets." |
| **Granger causality** | A statistical test. If A's past helps predict B's future beyond what B's own past tells you, A Granger-causes B. | "Predictive influence, not philosophical causation." |
| **F-statistic** | The number that comes out of a Granger test. Higher = stronger predictive influence. | "It quantifies the strength of influence between two singers." |
| **Eigenvector centrality** | A node's importance weighted by how important its neighbours are. | "Not just how many connections, but how important those connections are." |
| **Modularity (Q)** | How clustered the network is. High Q = tight subgroups. Low Q = everyone connected to everyone. | "How cliquey the network is. High Q means subgroups, low Q means democratic." |
| **Louvain community detection** | An algorithm that finds natural groupings in a network automatically. | "An algorithm that finds natural clusters; we use it to colour-code the graph layout." |
| **Circular-shift null model** | Our random baseline. Shifts one singer's time series forward by a random amount, destroys cross-singer timing, keeps each singer's own pattern. Repeated 200 times. | "It tells us what the graph would look like if cross-singer timing was random. Our real result has to beat this baseline." |
| **DTW (Dynamic Time Warping)** | Measure of similarity between two sequences even if slightly out of phase. | "Like measuring how similar two singers' sway patterns are, even if one starts a little later." |
| **pyin** | An algorithm that listens to audio and extracts the pitch (musical note) being sung. | "It extracts the note from the audio: which pitch, and how stable." |
| **F0 (fundamental frequency)** | The actual musical pitch of a sound, in Hz. Middle C = 261 Hz. | "The pitch: which musical note is being sung, measured in Hz." |
| **Demucs** | An AI model that separates a mixed audio track into instrument stems. Does NOT separate individual voices in a choir. | "AI audio separation: works for instruments, not for individual choir singers." |
| **FaceMesh** | Google's face-tracking tool. Maps 468 points on a face from video. | "It tracks 468 facial landmarks from video so we can measure mouth-opening and sync." |
| **MediaPipe Pose** | Google's body skeleton tracker. Extracts 33 body keypoints from video. | "It extracts a stick-figure skeleton from video so we can measure body sway." |
| **Honest Signals** | Pentland's 2008 MIT framework. Four unconscious body-language signals predicting team coordination: mimicry, activity, consistency, influence. | "Pentland's four measurable body-language dimensions, all involuntary, all predictive of team performance." |
| **Alchemical stages** | Gloor's metaphor from Cybernetic Alchemy. Raw → Albedo → Citrinitas → Rubedo. | "Raw, extracted, computed, interpreted. Each stage refines the data without losing it." |
| **CIN / CLN** | Collaborative Innovation (or Learning) Network. Hacker's framework. Self-organising, shared goal, transparent contribution. | "A self-organising creative network: no boss, shared goal, transparent participation." |
| **NMP** | Networked Music Performance. Software for real-time music collaboration over the internet. | "Latency is the enemy. Zoom is around 300 ms; Jamulus and SoundJack are around 50 ms." |
| **Cohen's d** | A measure of effect size. d = 0.2 small, 0.5 medium, 0.8 large. | "How meaningful the difference is, not just whether it is statistically real. We target d ≥ 0.5." |
| **ΔR²** | Additional variance explained by adding visual features to an audio-only model. | "How much extra prediction power the visual signals add on top of audio alone." |
| **ADF test** | Augmented Dickey-Fuller. Checks whether a time series has a trend (non-stationary). Granger requires stationary data. | "A stationarity check; if data drifts, we use IDTxl transfer entropy instead." |
| **IDTxl / transfer entropy** | A more general measure of information flow that does not require stationary data. | "Our backup for influence measurement if the data has trends Granger cannot handle." |
| **Dagstuhl ChoirSet** | Academic multitrack choir dataset. Each singer on their own microphone. CC-BY 4.0. | "Published academic choir recordings, one mic per singer, our ground-truth audio data." |
| **§60d UrhG** | German copyright exception for text-and-data mining in research. | "The German research copyright exception, covers our YouTube use." |
| **DPIA** | Data Protection Impact Assessment. Required under GDPR for biometric data. | "The legal document we file before processing facial-landmark data." |
| **Parquet** | File format for storing large structured data efficiently. | "Our data storage format: like a spreadsheet but much faster for large datasets." |

---

## Highest-priority likely questions

Use this section first if Prof. Gloor asks about dataset, formula provenance, or where the research questions came from.

### Q-P1: "What dataset are you using?"

**Core**: "We have a seed set plus three real data tiers. Tier 0 is what we already have: five seed URLs from Prof. Hacker, mostly Jamulus / Choir@Home examples. Tier 1 is real-world but messy: 20 to 30 public YouTube virtual-choir videos, mainly for visual signals because the audio is mixed stereo. Tier 2 is clean but academic: Dagstuhl ChoirSet plus ESMUC and ChoralSynth, where each singer has a separate track; that is where per-singer audio and influence graphs come from. Tier 3 is controlled and experimental: latency injection on Tier 2, which gives us known ground truth for H1."

**Short version**: "Tier 1 is real-world video, Tier 2 is clean per-singer audio, Tier 3 is our controlled latency experiment."

### Q-P2: "What do you already have, and what will you do to get the dataset?"

**Core**: "Already in hand: Prof. Hacker's five seed URLs and the dataset plan. Not yet collected: the analysis corpus. Next steps are concrete: download Tier 2 academic datasets starting May 1, build the SHA-256 manifest, hand-curate Tier 1 YouTube videos by May 15 with inclusion/exclusion reasons, and file the DPIA outline before face-mesh feature extraction. After Tier 2 is usable, we generate Tier 3 by injecting low-latency and Zoom-class conditions into those clean tracks."

**Do not overclaim**: "We should not say we have already analysed the data. We have the strategy and seed URLs; the corpus construction starts in the next iteration."

### Q-P3: "Is the Entanglement Index formula taken from a research paper, or did you make it up?"

**Core**: "It is a proposed adaptation, not a formula copied directly from an online-choir paper. The conceptual lineage comes from Gloor's entanglement metric for team communication and from Pentland's Honest Signals. But Gloor's original entanglement formula was validated on email data over 7-day windows, not on continuous music streams. So our A(t), V(t), N(t) decomposition is our operationalisation for choirs, deliberately simple and equal-weighted so it can be tested. H1-H3 are the validation tests."

**If pressed**: "We should cite Gloor for the entanglement concept, Pentland for Honest Signals, and be honest that the choir-domain formula is novel."

### Q-P4: "Where did the research questions and hypotheses come from?"

**Core**: "The main research question comes from a gap: NMP literature studies latency and tools, while coordination and team-flow literature studies human synchrony, but there is no simple quantitative coordination metric for online choirs. H1 follows from NMP latency literature; H2 follows from Prof. Hacker's network/trust lens, asking whether leadership topology changes; H3 follows from Pentland/Gloor Honest Signals, asking whether body movement adds explanatory power beyond audio."

**Short version**: "They are not arbitrary. Each hypothesis maps to one literature stream: latency, network topology, and Honest Signals."

---

## Predicted Hacker questions

### Q-H1: "Is this a Choir@Home extension? Are you replicating R2.2?"

She wrote R2.2 (the *Choir@Home Tools Survey*).

**Core**: "We have read R2.2 and cite it as the canonical NMP-tool landscape. Our project is adjacent, not replicating. R2.2 is a tool survey; ours is a measurement contribution. We use Jamulus and SoundJack as regimes to discriminate, not as tools to evaluate."

**Fallback**: "Where R2.2 ends (ranking tools qualitatively) is exactly where E(t) starts: a quantitative discriminator the survey did not have data for."

### Q-H2: "Show me the directed influence graph."

You can pull up an old conceptual sketch. The real graph from Dagstuhl is due May 31.

**Core**: "We will have the first real graph from Dagstuhl by May 31. I can send you the SVG the moment it lands."

### Q-H3: "How are you measuring trust empirically?"

Trust is her core research interest. Be honest.

**Core**: "We are not measuring trust as a psychological construct. We are measuring its observable behavioural correlates: timing alignment, mutual prediction (Granger causality), visual mirroring. The hypothesis is that those behavioural patterns covary with trust, but we are not making the trust claim ourselves; the published Honest Signals literature is."

**Fallback**: "If you would like us to include a trust-construct survey instrument from the literature in the discussion section, we can. We had scoped that out for time, but it is not architecturally hard."

### Q-H4: "What about the May 21 Virtual Mirror requirement?"

**Core**: "On track. We will export our team WhatsApp group, run it through SocialCompass, classify the team archetype, and write up the result for VS#3 on May 21."

### Q-H5: "Are you doing qualitative interviews?"

She likes mixed methods.

**Core**: "Out of scope for this iteration. The decision is recorded in our limitations register. Reasons: ethics overhead for a 14-week project, sample-size limits on qualitative claims, and our hypotheses are operationalisable on existing audio-visual signals. We cite published interview-derived survey instruments (Group Environment Questionnaire, Flow State Scale-2) in the discussion to frame our quantitative results, but we administer none."

**Fallback if pressed**: "If the timeline opens, we are open to revisiting. Easiest add would be a structured post-hoc interview with a single virtual-choir director already in our corpus."

### Q-H6: "What is the COIN structure of the choirs you are studying?"

**Core**: "Each curated YouTube choir is a CIN: volunteer participation, shared creative goal, transparent self-organisation, no central command. Some are CLNs at the editing stage if the producer is an alumnus or a returning collaborator. We document the CIN/CLN classification in the corpus manifest."

**Fallback**: "We have not coded each video by COIN type yet. That would be a one-pass annotation exercise; we can include it in the May 15 manifest deliverable."

### Q-H7: "Why not use the Choir@Home network for data?"

**Core**: "We considered it. Tier 0 already includes your URLs, which is the strongest possible Choir@Home signal. Asking the network for additional contributions would be a second data-collection step with its own ethics review and timeline cost. We chose hand-curated YouTube and academic multitrack to keep the timeline tight. If you would like to recommend specific Choir@Home outputs to add, we will."

### Q-H8: "What is your power analysis at n = 20 to 30?"

**Core**: "For H1, the statistical power comes from controlled latency injection on the academic multitrack data, not from the YouTube corpus. Twelve paired observations per piece (4 latency regimes by 3 jitter seeds) times 10 pieces is 120 paired observations: well-powered for d ≥ 0.5 at α = 0.05. For H3, n = 20 to 30 with ΔR² ≥ 0.10 is a demanding effect size we may or may not detect; we report the confidence interval honestly either way."

### Q-H9: "What if the academic datasets do not include leader / follower labels?"

**Core**: "They do not. Dagstuhl provides per-singer audio with mic crosstalk characterised but no leadership annotation. We infer the leader-follower structure from the data; that is the contribution. The Granger graph is not validated against ground truth labels because no such labels exist; we report graph structure and let the patterns be the empirical finding."

**Fallback**: "If you want a sanity check, the Dagstuhl piece labelled HSM-DYN has a piano accompanist; we can verify the influence graph correctly identifies the piano as a hub."

### Q-H10: "Why are you running the Virtual Mirror on yourselves and not on the choirs you are studying?"

**Core**: "Two different deliverables. The Virtual Mirror is a seminar requirement on team self-reflection. The choir analysis is the project deliverable. They share the SocialCompass tooling but answer different questions: archetype classification of *us*, coordination index of *them*."

---

## Predicted Gloor questions

### Q-G1: "How does this map to the alchemical stages?"

**Core**: "Direct mapping. Nigredo is the raw mp4 and wav. Albedo is extracted pose, separated stems, F0, landmarks. Citrinitas is computed sub-indices and pairwise alignments. Rubedo is E(t), the influence graph, the regime classification, and the paper figures. The transformation between stages is the contribution; the data is not lost, it is refined."

**Fallback if he wants more**: "Chapter 14, *Data as Prima Materia*, framing. The data itself becomes prima materia in the alchemical sense: same data goes through repeated transformations and the meaning emerges in the final stage."

### Q-G2: "Have you read Cybernetic Alchemy in full?"

Be honest.

**Core**: "Chapter 14 in detail and the prologue in full. I have skimmed the rest. The directly Project-8-relevant content is Chapter 14 and the introduction's positioning of cybernetic alchemy as the framework. I will read the rest as the paper draft approaches."

He will respect this more than "yes, all of it."

### Q-G3: "What honest signals exactly are you measuring?"

**Core**: "Three of Pentland's four canonical dimensions sit in V(t): mimicry as pairwise cross-correlation of trunk-sway and mouth-aperture; activity as the amplitude of those movements; consistency as the variance of inter-singer cross-correlation over time. The fourth, influence, sits in N(t) as Granger causality on note onsets."

**Fallback**: "All four dimensions are covered, just split across V and N because of the data substrate. Pentland used badge sensors with all four signals on one device; we use video for activity and audio for influence. Methodological difference, same conceptual space."

### Q-G4: "How is this different from Pentland's own Sociometer work?"

**Core**: "Sociometer was a hardware badge in a face-to-face setting, four people in one room. We are operating on remote video and audio, on choirs rather than business meetings. The biggest methodological difference: the coordination outcome in choirs is acoustically measurable, which Pentland's settings did not have. We have a ground truth he did not."

### Q-G5: "Have you considered using SocialCompass on the team?"

**Core**: "Yes. That is the Virtual Mirror requirement on May 21. We will export our team WhatsApp, run it through SocialCompass, classify the archetype, and report the result at VS#3."

### Q-G6: "What is your team archetype: Bee, Ant, Butterfly, Capybara, or Leech?"

**Core (honest)**: "All four of us classify as Tree Hugger / Ant on SC Chat, with scores between 63 and 75 percent Ant. Symbiont was more varied: Hammad came out as Capybara at 49 percent, Hassan and I leaned Ant in the 38 to 40 percent range, and Kumaran, our newest member, came in at 80 percent Ant, the strongest signal of the team on both tools."

### Q-G7: "Why is this not just NMP engineering?"

**Core**: "The NMP literature treats latency as the independent variable and asks whether music can happen at all. We are treating coordination dynamics as the dependent variable and asking what the network and visual signatures of that coordination are. Different question. NMP work is necessary infrastructure; ours is the measurement contribution on top of it."

### Q-G8: "Have you reached out to Pentland?"

**Core**: "No, and we have not planned to. Pentland's framework is well-published; the operationalisation choices we are making sit within it without needing his direct input. If you think a short outreach would be productive, that is a conversation to have."

---

## Methodology challenges (could come from either supervisor)

### Q-M1: "n = 20 to 30 is small. Is this defensible?"

Same as Q-H8. The substantive answer: H1 is powered by the controlled latency injection on academic multitrack, not by the YouTube corpus.

### Q-M2: "What if results are null?"

**Core**: "Null is publishable in this framing. If H1 fails, E(t) does not discriminate the regimes; that itself is informative because it means the latency dichotomy is too crude or our metric is mis-specified. If H3 fails, the Honest Signals visual contribution is below our resolvable threshold at this sample size. Both are real findings."

### Q-M3: "Why MediaPipe over OpenPose or DWPose?"

**Core**: "MediaPipe has Pearson 0.80 to 0.91 vs. Vicon for limb keypoints in the published validation, runs natively on Win 11 (our team's platform) without WSL2, and has a stable Python API. OpenPose requires CUDA and Linux for production use. DWPose is technically stronger but the published Project-8-relevant work uses MediaPipe. Trade-off: MediaPipe's head-sway accuracy is unvalidated in the literature, so we calibrate it against a reference tool in WP2 by May 22."

### Q-M4: "How do you handle stationarity in Granger causality?"

**Core**: "We test stationarity with the ADF test on the onset-delay residuals. If non-stationary on more than 30 percent of windows, we fall back to IDTxl transfer entropy, which does not require stationarity. We also run Zanin's COP-GC variant in parallel; ordinal-pattern Granger captures non-linear coupling that standard Granger misses."

### Q-M5: "What is your null model?"

**Core**: "200-shuffle circular shift on the per-singer streams. Circular shift preserves within-stream autocorrelation while destroying cross-stream timing, the right null for coordination versus independent structure. An i.i.d. shuffle would over-reject; a block shuffle would under-reject."

### Q-M6: "Why not the YouTube Data API?"

**Core**: "API ToS prohibits research scraping at scale and does not give us audio-only download. yt-dlp plus per-video license capture is the canonical academic approach and is covered by §60d UrhG. We document this decision in PROJECT_GUIDE with the legal basis and reproducibility notes."

### Q-M7: "How do you address selection bias in the YouTube corpus?"

**Core**: "Honestly? Imperfectly. YouTube discovery is biased towards popular videos. We mitigate by hand-curating across multiple search queries (virtual choir, Zoom choir, SoundJack choir, distributed choir COVID, SATB virtual, Eric Whitacre virtual choir) and explicitly excluding heavily post-produced content, which is a known editorial confound. The corpus is small enough that hand-curation is feasible. We document each rejection in the manifest."

### Q-M8: "Why no human-rater validation of E(t)?"

**Core**: "Out of scope, recorded in §12 limitations. Adding human raters would require a panel of trained musicians (recruitment, payment, ethics) and would not fit the 14-week timeline. We argue the falsifiable hypotheses against the latency-regime ground truth are a sufficient first-pass validation; full human-rater calibration is future work."

---

## Scope and logistics

### Q-S1: "Who is first author on the paper?"

**Core**: "I am, as project lead and audio-pipeline owner. The team contributes substantially across all work packages and is co-authored. Authorship order is documented in PROJECT_GUIDE."

### Q-S2: "What is the GDPR position?"

**Core**: "FaceMesh landmarks are Art. 9 biometric data. We rely on Art. 9(2)(j) research exception plus Art. 89 safeguards. DPIA outline drafted, full DPIA in progress, Bamberg DPO consult requested. mp4s are deleted after feature extraction. Compliance is on the critical path."

### Q-S3: "Why no self-recording?"

**Core**: "Three reasons. Ethics: we would need IRB approval, lengthening the timeline. Self-selection bias: we are not trained singers. Original scope instruction at project outset explicitly forbade self-recording. We use publicly available YouTube and published academic datasets instead."

### Q-S4: "Where is the dashboard hosted?"

**Core**: "Local-first; runs on your laptop after `make all`. We do not plan to host publicly during the project. If a stable hosting target is needed for the July 23 demo, we will deploy to a personal Hetzner instance for the day; about €5 cost."

### Q-S5: "What is the licensing on the academic datasets?"

**Core**: "Dagstuhl ChoirSet is CC-BY 4.0 with attribution. ESMUC is CC-BY-NC, non-commercial; we are non-commercial. ChoralSynth is MIT-equivalent for synthetic data. All compatible with academic redistribution of derived features. None are compatible with redistributing the audio itself; we do not."

---

## Curveballs

### Q-U1: "Have you considered EEG hyperscanning?"

**Core**: "It is in the literature ([[hyperscanning]] in our wiki). Out of scope: our project is non-invasive on remote video. Hyperscanning would require lab-recruited dyads. We discuss it in the limitations as a comparator and note that pose-based behavioural sync is the open-data analogue of EEG hyperscanning."

### Q-U2: "What about cross-cultural variation?"

**Core**: "Important and out of scope at n = 20 to 30. The corpus will skew Western (English-language search queries, popular YouTube). We acknowledge this in the discussion and flag it as the most important external-validity limitation."

### Q-U3: "What if YouTube takes down videos mid-project?"

**Core**: "We download and SHA-256 fingerprint each video at corpus-curation time. Extracted features are persisted in parquet. If a video is taken down later, we still have the features; we cannot re-extract but we do not need to. The corpus manifest records original URL, license, and SHA-256 for reproducibility."

### Q-U4: "What if a music theorist would say your timing definitions are wrong?"

**Core**: "Onset detection is a librosa primitive with documented limitations on legato vocal lines. We cross-validate against pyin-derived F0 transitions. Where the two disagree, we flag the segment and exclude it from cross-stream alignment. We are not claiming a music-theoretical onset definition; we are claiming an operational one."

### Q-U5: "Are you including conducting gestures?"

**Core**: "Where present in the video, MediaPipe Pose extracts the conductor's keypoints alongside the singers. We treat the conductor as a node in the influence graph. In most virtual choirs the click-track is the leader, so the conductor signal is sparse. Academic ensembles have conductors; we will look at conductor-led centrality patterns."

---

## Audience confusion (other students may be in the room)

For these, give a one-sentence definition then return to the supervisor question.

- **"What is E(t)?"** "Composite coordination score combining audio sync, body movement, and influence networks."
- **"What is Granger causality?"** "Statistical test: if A's past helps predict B's future beyond B's own past, A Granger-causes B."
- **"Why alchemy metaphors?"** "Prof. Gloor's framework. Raw data progresses through stages, raw to refined to illuminated to integrated, toward meaning."
- **"What is NMP?"** "Networked Music Performance. Software that lets musicians play together over the internet."
- **"What is the difference between Zoom and Jamulus?"** "Zoom is consumer video, around 300 ms latency. Jamulus is purpose-built for music, around 50 ms latency."

---

## Presenter doubts (your safety net)

### "What if I do not know an answer?"

Say so. Word for word: **"That is a good question and I have not tested it yet. Let me come back to you in the next iteration with a real answer rather than a guess."** Pull out a pen, write the question down visibly. The act of writing it down signals respect.

This is the most powerful move you have. Senior researchers will trust you more for one honest "I do not know" than for ten confabulated answers.

### "What if Gloor wants to ride the alchemy metaphor for five minutes?"

Let him. Listen, take notes, occasionally ask a clarifying question. If he is enjoying himself and you have already covered the slides, that *is* the meeting going well.

If you must steer back: "That maps directly onto our Citrinitas stage in slide 4, should I show that again?" gives you a graceful return.

### "What if Hacker challenges the team composition?"

You are presenting; the team is set. **"Team composition was finalised at the project-phase signup; it is in `Project_Phase_Roster.md` in our vault. Happy to discuss specific role allocations if you have concerns."** If she pushes for a swap, do not commit live. **"Important point. Let me bring this back to the team and respond by Friday."**

### "What if Hacker pushes for qualitative interviews?"

This is the most likely scope-expansion request. See Q-H5. If she insists, **do not commit on the call**. **"That is a real expansion of scope; let me cost it out and come back to you with two options, minimum viable (one director interview) and full (panel of five). I will have that to you by Friday."**

### "What if I run out of time?"

Have the 5-minute compressed map memorised. The transition from the 7-minute to the 5-minute path is at slide 3: compress E(t) to 60 sec, skip status calendar verbally, spend 30 sec on slide 5 total. The compressed path still hits all 7 slides.

### "What if the screen-share fails?"

Pull up the backup PDF. If that fails, hold up the printed one-pager and read from it. If that fails, just talk; you know the deck inside out.

### "What if I freeze?"

It happens. **"Sorry, give me a moment."** Drink water. The room will wait. Then continue from where you left off; do not start the slide over.

If your mind goes blank: **"Let me pull up slide [N] to ground us."** Pulling up a slide gives you 5 seconds to recover.

### "What if they want to fundamentally change the scope?"

You came with a v2.1 plan. They are giving you input, which is the entire point of this meeting. **Do not commit on the call.** Take notes verbatim. **"This is exactly the kind of input we wanted today. Let me bring this back, weigh it against the timeline, and come back with two options by next iteration."**

The exception: if both supervisors agree on a specific scope change, you can acknowledge agreement on the call without committing to a delivery date.

### "What if they ask for a deliverable I forgot about?"

**"Yes, we have that planned for [iteration N]. I will send you the artefact when it lands."** If you cannot remember when, **"Let me check the iteration plan and get back to you."** Never promise a date you cannot keep.

### "What if there is awkward silence after slide 7?"

Hold the silence for five seconds. Researchers process before they speak. If silence persists past five seconds: **"Anything you would like me to expand on, or any aspect you would like us to deprioritise?"**
