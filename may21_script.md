# May 21 Status Meeting III, Speaker Script

**Project 8 · Entanglement in Online Choir · 2026-05-21 · 14:00 CET**

> Solo presenter (Zuraiz). Target 9 minutes spoken, 1 minute buffer. ~80 seconds per slide. Plain language, no DSP jargon. Audience assumed to remember the project broadly but not the details.

---

## Slide 1: Title (15 sec)

Hello everyone. I'm Zuraiz, presenting on behalf of the Project 8 team. Today is status meeting three for our work on measuring coordination in online choirs.

---

## Slide 2: Recap — Goals and Plan (75 sec)

A quick recap, because three weeks is a long time and we covered a lot in iteration two.

Our research question is simple to state: when a choir sings together over the internet, can we put a number on how well they are coordinating? We are building that number. We call it E(t), the Entanglement Index. It combines three signals: audio synchrony, body movement, and a network of who-influences-whom.

We have three hypotheses. First, low-latency tools like Jamulus and SoundJack should score higher than Zoom. Second, the influence network should change shape with latency, from democratic to leader-dominated. Third, body-movement signals should add meaningful predictive power on top of audio alone.

The project has three phases. Phase one was scope and scaffold, finished on April 30. Phase two is build and analyse, running from May to early July. We are now four weeks into phase two. Phase three is paper and final presentation, July.

---

## Slide 3: Last Iteration — What Shipped, What Slipped (105 sec)

Now the honest part: what we got done in the last three weeks, and what we did not.

**What shipped, across all four work packages**:

The Dagstuhl ChoirSet is on disk. That is our Tier-2 ground-truth dataset, 5 gigabytes of multitrack choir recordings, MD5-verified against Zenodo. The Tier-1 YouTube corpus is curated to 29 verified videos: 4 of Prof. Hacker's 5 Tier-0 seed URLs re-confirmed plus 25 new ones. The breakdown by network regime came out balanced (11 Jamulus, 5 Jamulus+Zoom, 4 SoundJack, 9 Zoom-only); the Zoom-only stratum started thin at 2 videos but we ran a supplementary search this week and brought it up to 9, which gives us the statistical power we need for the H1 latency-contrast hypothesis.

WP1 audio: pipeline running end-to-end on the Locus Iste Quartet A Take 02 recording, all four SATB singers, 143 seconds. Pitch extraction puts each voice in its expected range. Pairwise audio coupling between adjacent voices comes in between 0.72 and 0.77, which is what you would expect from singers in the same room. Figure on the slide.

WP2 video: MediaPipe Pose and FaceMesh ran end-to-end on a Tier-1 SoundJack rehearsal video, 595 frames, 79.5% pose detection rate. Per-singer body coordinates plus three derived honest-signal features (shoulder rise as breath proxy, head sway, trunk lean) are landing in parquet. Calibration against a reference tool is the Sprint-3 next step.

WP3 network: Granger causality with a 200-shuffle circular-shift null, applied to the SATB audio envelopes. 11 of 12 directed edges came back significant at p_null less than 0.05. Graph density is 0.92, which is what you would expect from an in-person quartet where everyone listens to everyone. Soprano is the most central voice by eigenvector centrality. This is the first draft of Prof. Hacker's flagship figure.

WP4 dashboard: the wireframe and design doc are committed; the React and FastAPI scaffold lands Sprint 3. And the alchemical-stage pipeline diagram is drafted as Prof. Gloor's flagship: it shows how raw video moves from Nigredo through Albedo, Citrinitas, and Rubedo into quantified group flow.

Quality gates: 15 of 15 smoke tests pass, ruff clean, mypy strict clean.

The DPIA outline was filed with the Bamberg data protection officer this morning.

**What slipped**: timing on intermediate dates. Tier-2 datasets were supposed to be on disk by May 1; they landed May 17. The audio pipeline first run was scheduled for May 8; it landed May 17. Corpus curation was due May 15; that landed May 17. All milestones landed before today, but 9 to 17 days later than the original Sprint-2 schedule.

**The honest read**: the intermediate dates slipped, but the overall deliverable scope expanded. WP2, WP3 and WP4 milestones that were originally scheduled for May 22 and May 31 were brought forward and shipped in draft form so this presentation has cross-WP coverage, not just audio.

---

## Slide 4: Plan for the Next Iteration (90 sec)

Sprint 3 runs from today until status meeting four on June 11.

**WP1 audio**: scale the pipeline from one Dagstuhl piece to all of them. Output is A(t) feature parquet for the full Dagstuhl multitrack collection by June 4.

**WP2 video**: run MediaPipe pose and face extraction on the first 10 Tier-1 YouTube videos. Calibrate against a published ground truth so we know our error bars. One-page calibration note plus the parquet files by June 11.

**WP3 network**: build the directed influence graph for five Dagstuhl pieces. We run two variants: standard Granger causality and the ordinal-pattern variant, so we can compare and report both. Due June 11.

**WP4 legal**: convert today's DPIA outline into a full document, get DPO sign-off. This must complete before June 14, because Tier-3 latency injection at scale starts on the 14th and we cannot do biometric extraction without the signed DPIA.

One technical reminder: the YouTube videos remain visual-only. Mixed-stereo audio cannot be separated per-singer using current open-source DSP, so all per-singer audio features come from the Tier-2 multitrack data.

---

## Slide 5: Retrospective Output (75 sec)

We held a team retrospective on {DATE}. Four members participated.

**What worked**: {bullet}. {bullet}.

**What slipped and why**: {root cause one}. {root cause two}.

**One process change for Sprint 3**: {single agreed change}.

We are committing to that one change. Adding more would dilute it.

---

## Slide 6: Virtual Mirror Results (75 sec)

This is the part the seminar specifically asks for. We exported our team WhatsApp group on {DATE} and ran it through SC Chat Analyzer and Symbiont, the same tools we used in the introductory block course.

Our team archetype came out as {ARCHETYPE}. The communication topology is {SHAPE}. Top contributors by message volume are {NAMES}. Reciprocity index is {VALUE}.

What this means for our COIN dynamics: {1-2 sentence interpretation}. The lesson we are taking into Sprint 3 is {ACTION}.

---

## Slide 7: Problems and Questions (60 sec)

Three open problems we are working on.

First, the DPIA turnaround. Bamberg DPO sign-off has to happen before June 14, which is tight. Outline went in this morning.

Second, the arXiv jurisdiction question. Our text-and-data-mining rights under section 60d of German copyright law apply in DE jurisdiction. arXiv is US-hosted. Bamberg legal desk is reviewing.

Third, MediaPipe pose accuracy on micro-sway has not been validated for the choir use case. The calibration note in Sprint 3 will quantify the error.

Three questions for the room.

Does Prof. Hacker have access to additional Tier-2 datasets — ESMUC or ChoralSynth — beyond Dagstuhl?

For the influence-graph deliverable, do supervisors prefer minimalist matplotlib aesthetic or a more polished Cytoscape look?

And is the final presentation on July 23 in-person or remote?

Thank you. I am happy to take questions.

---

## Timing budget

| Slide | Target | Cumulative |
|:---|:---:|:---:|
| 1 Title | 0:15 | 0:15 |
| 2 Recap | 1:15 | 1:30 |
| 3 Progress | 1:45 | 3:15 |
| 4 Next iteration | 1:30 | 4:45 |
| 5 Retrospective | 1:15 | 6:00 |
| 6 Mirror | 1:15 | 7:15 |
| 7 Problems/Q | 1:00 | 8:15 |
| Buffer + setup | 1:45 | 10:00 |

Target spoken time: 8:15. Hard ceiling: 10:00.
