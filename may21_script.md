# May 21 Status Meeting III, Speaker Script (Hammad Anwar)

**Project 8 · Entanglement in Online Choir · 2026-05-21 · 14:00 CET**

> Presenter: Hammad Anwar (on behalf of the 4-person team). Target spoken time: 9 minutes 15 seconds. 10 slides, ~54 seconds per slide average. Speak in plain language, "we"/"the team" throughout, no DSP jargon unless asked.

---

## Slide 1: Title (15 sec)

Hello everyone. I'm Hammad Anwar, presenting on behalf of the Project 8 team for status meeting three. Today I will walk through what we built in Sprint 2, what we found in our team's own Virtual Mirror analysis, and the plan for Sprint 3.

---

## Slide 2: What we are building (70 sec)

Quick recap, because three weeks is long and we covered a lot.

Our research question is simple: when a choir sings together over the internet, can we put a number on how well they are coordinating? We are building that number. We call it E(t), the Entanglement Index. It blends three signals: audio synchrony, body movement, and a network of who-influences-whom. The formula is on the slide: E(t) equals the average of A(t) audio, V(t) visual, and N(t) network.

Three hypotheses. First, low-latency tools like Jamulus and SoundJack should score higher than Zoom. Second, the influence network should shift with latency, from democratic to leader-dominated. Third, body-movement signals should add meaningful predictive power on top of audio alone.

Where we are today: phase one of three is done, phase two is what we are reporting now, phase three is the paper and final presentation in July.

---

## Slide 3: Sprint 2 progress — Audio + Video (60 sec)

This slide shows two of the four work packages.

On the left, WP1 audio. The pipeline ran end-to-end on a real choir recording, the Locus Iste Quartet A Take 02 from the Dagstuhl ChoirSet. All four SATB singers, 143 seconds. Pitch extraction puts each voice in its expected range. Pairwise audio coupling between adjacent voices comes in between 0.72 and 0.77, which is what you would expect from singers in the same room.

On the right, WP2 video. MediaPipe Pose and FaceMesh ran on a Tier-1 SoundJack rehearsal, 595 frames, 79.5% pose detection rate. Per-singer body coordinates plus three derived honest-signal features came out clean: shoulder rise as breath proxy, head sway, and trunk lean.

Both pipelines are end-to-end, both produce parquet outputs, all smoke tests pass.

---

## Slide 4: Sprint 2 progress — Network influence (60 sec)

This is the first draft of Prof. Hacker's flagship figure.

We ran Granger causality on the SATB audio envelopes from that same Quartet A Take 02 recording. The null model is a 200-shuffle circular shift, which preserves within-stream autocorrelation. 11 of the 12 possible directed edges came back significant at p_null less than 0.05. Graph density is 0.92, which is what we would expect from an in-person quartet where everyone is listening to everyone.

Soprano is the most central voice by eigenvector centrality at 0.53. That makes musical sense for the piece. The lag-1 temporal coupling tells us this is short-window prediction, not long-range structure.

This is n=1 so far. Sprint 3 scales it to 5 pieces with both standard Granger and the COP-GC variant for robustness.

---

## Slide 5: Sprint 2 progress — Dashboard and alchemical pipeline (50 sec)

This is Prof. Gloor's flagship figure. WP4 owns the human-facing layer of the project.

The figure on the slide shows our 4-stage pipeline mapped onto the alchemical framework from Cybernetic Alchemy chapter 14. Nigredo is raw choir files. Albedo is feature extraction. Citrinitas is cross-singer pattern emergence. Rubedo is the quantified entanglement score plus regime contrast.

The dashboard itself is at the wireframe stage. The React and FastAPI scaffold lands in Sprint 3 with the parquet readers wired to the live data.

---

## Slide 6: Sprint 2 progress — Data (60 sec)

This slide is the data foundation.

Tier-2 is the Dagstuhl ChoirSet. 5.1 gigabytes of multitrack choir recordings, MD5 verified against Zenodo. 13 singers in SATB sections plus full choir plus quartet groupings. This is our latency-free ground truth.

Tier-1 is the YouTube corpus we curated this sprint. 29 videos, all downloaded and SHA-256 hashed for reproducibility, 1.3 gigabytes on disk. The metadata is captured in a manifest CSV. The stratification by network regime is on the slide: 11 Jamulus, 5 Jamulus+Zoom hybrid, 4 SoundJack, and 9 Zoom-only. The Zoom-only stratum started thin at 2 videos but we ran a supplementary curation this week and brought it up to 9, which gives us the statistical power we need for the H1 latency-contrast hypothesis.

The DPIA outline was filed with the Bamberg data protection officer this morning. Feature extraction on all 29 videos runs in Sprint 3 against the signed DPIA.

---

## Slide 7: Sprint 3 plan, May 21 to June 11 (70 sec)

Sprint 3 runs from today until status meeting four on June 11. Four parallel tracks, one per work package.

WP1 audio scales the pipeline from one Dagstuhl piece to all of them. Output is A(t) feature parquet for the full multitrack collection. Due June 4.

WP2 video runs MediaPipe pose and face extraction on the first 10 Tier-1 YouTube videos, with a one-page calibration note comparing against an OpenPose reference. Due June 11.

WP3 network builds the directed influence graph for five Dagstuhl pieces, with both standard Granger causality and the ordinal-pattern variant from Zanin 2021 for robustness. Due June 11.

WP4 legal converts today's DPIA outline into the full document and gets DPO sign-off. This must complete before June 14, because Tier-3 controlled latency injection at scale starts on the 14th, and we cannot do biometric extraction without the signed DPIA.

One technical reminder: Tier-1 YouTube stays visual-only. Mixed-stereo audio cannot be separated per-singer using current open-source DSP, so all per-singer audio features come from the Tier-2 multitrack data.

---

## Slide 8: Sprint 2 retrospective (65 sec)

Three quick sub-sections.

What worked. Tier-1 corpus criteria we agreed on re-discovered 4 of Prof. Hacker's 5 seed URLs unprompted, which validated our inclusion-rule prompt. All 4 WPs shipped Sprint-2 milestones, including draft flagship figures for both supervisors. The WP1 audio numbers matched musical theory on first run, which gave us confidence in the measurement stack.

What slipped, and why. Intermediate dates slipped 9 to 17 days. Root cause: the Sprint-2 timeline assumed parallel WP execution, but in practice the work ran serially because most engineering tasks share the same Tier-2 data dependency. We caught the slip late, around May 17 instead of May 8, which we should have done.

One process change for Sprint 3. We are adding a weekly 15-minute Monday async check-in on WhatsApp. Each work package posts shipping, stuck, need. Light-touch, no meetings, structured thread. Goal: surface blockers earlier.

---

## Slide 9: Virtual Mirror, team dynamics and communication (65 sec)

This is the part the seminar specifically asks for. We exported our team WhatsApp group on May 18 and ran it through SC Chat Analyzer, the same tool we used in the introductory block course.

On the slide, the People List shows 5 participants. Zuraiz drives volume with 28 messages, tagged "Bigger sender". Hassaan responds fastest at 3.5 minutes average, tagged "Fast responder". Hammad sits at 26 minutes, Kumaran at 1.41 hours.

The chat character: HIGH on Meaning, LOW on Emotion, MEDIUM on Relationship. We are a task-focused research group with moderate social bonding.

Personality archetypes: all four human members classified as Tree Hugger as their primary archetype. That confirms the conscientious stance we self-stated in the team brief from the start.

The insight for Sprint 3: we coordinate around tasks, not around bonding. The process change on the previous slide is the direct response. Lift Relationship score, reduce response-time variance.

---

## Slide 10: Active risks and closing (40 sec)

Two active risks we are tracking, both with plans.

First, DPO sign-off on the DPIA is pending. We are following up weekly until the Jun 14 large-scale extraction deadline.

Second, MediaPipe pose accuracy on the kind of micro-sway we care about has not yet been validated against a reference tool. Sprint 3 calibration study against OpenPose will quantify the error and trigger a fallback to OpenPose if needed.

Thank you. Open to your questions.

---

## Timing budget

| Slide | Target | Cumulative |
|:---|:---:|:---:|
| 1 Title | 0:15 | 0:15 |
| 2 What we are building | 1:10 | 1:25 |
| 3 Audio + Video | 1:00 | 2:25 |
| 4 Network (WP3) | 1:00 | 3:25 |
| 5 Dashboard (WP4) | 0:50 | 4:15 |
| 6 Data | 1:00 | 5:15 |
| 7 Sprint 3 plan | 1:10 | 6:25 |
| 8 Retrospective | 1:05 | 7:30 |
| 9 Virtual Mirror | 1:05 | 8:35 |
| 10 Risks + closing | 0:40 | 9:15 |
| **Buffer to 10 min** | 0:45 | **10:00** |

Target spoken time: 9:15. Hard ceiling: 10:00.

---

## Delivery tips for Hammad

- Slow down on slides 4 and 5 (the flagship figures). Supervisors will look at the figure while listening; give them time to read.
- For slide 6, if Prof. Hacker asks about the stratification, the answer is in slide 6 itself: 20 low-latency vs 9 high-latency gives us the H1 contrast.
- If anyone asks "did you build this yourselves or use a library", the answer is: we built the pipeline code; we use librosa, MediaPipe, statsmodels, and networkx as standard scientific Python libraries.
- If you blank on a number, the cheat sheet is in `may21_qa_prep.md` at the bottom.
- If you do not know an answer, say "I will check with the team and get back to you" rather than guessing.
