# Jun 11 Status Meeting IV, Speaker Script (Hassan Ahmed)

**Project 8 · Entanglement in Online Choir · 2026-06-11 · 14:00 CET**

> Presenter: Hassan Ahmed (on behalf of the 4-person team). Target spoken time: 9 minutes. 8 slides following the coordinators' rubric: goals + plan recap, last-iteration progress, next-iteration plan, retrospective, problems/questions. Speak plainly, "we" and "the team" throughout, no DSP jargon unless asked. The project-context appendix at the bottom is private prep: read it once before the meeting.

---

## Slide 1: Title (15 sec)

Hello everyone. I'm Hassan Ahmed, presenting for the Project 8 team at status meeting four. I'll recap our goals briefly, walk through what we shipped this iteration, show the plan for the next one, share the retrospective, and close with three questions for the room.

---

## Slide 2: Goals and plan recap (75 sec)

Quick recap, since three weeks is long.

Our research question: when a choir sings together over the internet, can we put a number on how well they coordinate? That number is E(t), the Entanglement Index. It blends three signals: audio coupling, visual coupling from body movement, and the influence network of who-follows-whom. The formula card on the left is the whole metric in one line.

Three hypotheses, unchanged since April. H1: low-latency tools like Jamulus score higher than Zoom. H2: the influence network shifts from democratic to leader-dominated as latency rises. H3: body signals add at least ten points of explained variance over audio alone.

The timeline on the right shows where we are: status meeting four of six. Everything green is behind us; the two remaining status meetings and the final presentation are ahead.

One sentence on scope: same goals as April, no drift. This iteration had a single job, make E(t) real. Next slide shows whether we did.

---

## Slide 3: Headline, E(t) is operational (90 sec)

This is the core result of the iteration.

The Entanglement Index now runs end-to-end. We computed it on five multitrack choir pieces from the Dagstuhl ChoirSet, each singer on their own microphone. For every piece we also ran a null model: two hundred random time-shifts of each singer's audio, which preserves how each voice behaves on its own but destroys the coordination between voices. If our metric were measuring noise, the real recording would look like the shuffled ones.

It does not. The figure shows it: five red dots are the observed coordination per piece, five gray bars are what chance produces. Every red dot sits far above its gray bar. All five pieces, p below one in a thousand.

One more pattern worth noticing. The two pieces cluster by what the music is, not by how many singers there are. Locus Iste, a homophonic chant where everyone moves together, scores high, 0.74 to 0.80. Tu Pauper Es, polyphonic with independent voice entries, scores lower, 0.57 to 0.68. A four-singer quartet of Locus Iste sits with the eight-singer full choir of Locus Iste. The metric reacts to what the choir is actually doing, which is exactly what we want from it.

Bottom line: the number we promised in April exists, it's repeatable, and it's statistically defensible.

---

## Slide 4: The audio + network engine (75 sec)

What's underneath that headline.

The audio side scaled from one piece last iteration to all twenty-five musical takes in the Dagstuhl set, two hundred eighty-eight pairwise couplings between singers. The coupling pattern matches musical structure, which is our sanity check.

The network side is the influence graph, Professor Hacker's flagship. The grid shows directed who-leads-whom graphs for five pieces. New this iteration: every piece runs under two causality methods. Standard Granger, which is the classic parametric test, and an ordinal-pattern variant called COP-GC that only looks at the shape of changes, not their size.

The two methods agree on quartets and diverge on full choir: forty-two versus twenty-five significant edges out of fifty-six on the same recording. That gap is itself a finding. Roughly a third of the standard test's edges depend on loudness magnitude rather than timing pattern. We carry both methods forward and the contrast goes in the discussion section.

Also worth saying: last sprint's flagship result reproduces exactly under the new pipeline. Same edges, same density. That's our regression test.

---

## Slide 5: Video features + dashboard (75 sec)

The other two work packages.

Video: we ran pose extraction across ten YouTube videos, stratified across the four networked-performance regimes. Five of ten pass our quality floor; the best video tracks singers at ninety-eight and a half percent of frames. The five that fail are screen recordings of software interfaces, there's no body in frame for the model to find. Per the "try and iterate" decision from last meeting, the five passing videos are the working set and the limitation is documented.

Dashboard: the screenshot on the left is the real application running locally. React frontend, FastAPI backend, four panels: video, influence graph, E(t) timeline, metadata. It currently renders against mock data; wiring it to the real outputs is next iteration's work.

Twenty-three of twenty-three automated tests pass across the whole codebase.

Every work package moved this iteration. Nothing is blocked.

---

## Slide 6: Plan for the next iteration (60 sec)

Next iteration runs from tomorrow to status meeting five on June 25. Five tracks.

Audio: per-window Granger, so the network signal becomes time-varying instead of one value per piece.

Video: pose on the remaining YouTube videos, triaged by quality so we spend effort where singers are actually visible.

Network is the priority track: Tier-3 latency injection. We take the clean Dagstuhl audio and inject controlled jitter at four levels matching the regimes, then compute E(t) at each level. That is the first cross-regime test of hypotheses one and two.

Dashboard: swap mock data for the real pipeline outputs and add the pose overlay.

Data: we download ChoralSynth, which is openly licensed on Zenodo, and follow up on ESMUC, which is our first question later.

The hard milestone before status five: dashboard alpha on real data, plus the first cross-regime result.

---

## Slide 7: Retrospective (60 sec)

Three columns: what we keep, what went wrong, and what to watch.

Keep: one named, reviewable artefact per work package per iteration, and documentation synced at every milestone. Both are working; they stay.

Went wrong, two things. First, two planned datasets, ESMUC and ChoralSynth, didn't get pulled in. The fix is straightforward: ChoralSynth turns out to be an open download, scheduled for next iteration; ESMUC needs a license, which is a question for the room in a minute. Second, half our YouTube corpus turned out to be screen captures with no visible singers. The fix: future curation filters on "singers visible in tiles", not just on which tool the choir used.

Watch list, three honest limitations stated before anyone has to ask. The visual signal is absent from all current E(t) values because Dagstuhl has no video; the formula reallocates weight and the code is ready the moment multimodal data exists. All five pieces are zero-latency studio recordings, so cross-regime variation only arrives with Tier-3 next iteration. And our p-values mean zero of two hundred shuffles beat the real data, which is "below one in two hundred", not literally zero.

Nothing on this slide is news to us; it's all in the written results document too.

---

## Slide 8: Problems and questions (35 sec)

Two questions for the room.

Professor Hacker: do you have institutional access to the ESMUC multitrack dataset? ChoralSynth we can download ourselves, so ESMUC is the only dataset where we need help.

To the coordinators: is CPU time available on a Bamberg or HSLU cluster? To be clear, this is not a blocker; the planned scope runs overnight on our laptops. Cluster access would let us run a denser jitter grid and finer analysis windows, which strengthens the robustness checks on hypothesis one.

Thank you. Open for questions.

---

# Appendix: Project context for Hassan and Hammad (read once before the meeting)

This appendix is private prep, not part of the spoken script. Read it once and you will have enough context to handle the live Q&A confidently. **Both of you read everything**: Zuraiz is not in this meeting, so between the two of you, you cover the whole project.

## Role split for the meeting (Zuraiz absent)

- **Hassan presents** all 8 slides and owns every network/Granger/influence-graph question (that is your WP3 area).
- **Hammad is in the room as second voice.** You own every video/pose/MediaPipe question (your WP2 area), and you have the continuity: you presented at Status Meeting III, so anything referencing "what was said last time" (the DPIA decision, "try and iterate", the Virtual Mirror) is yours to confirm.
- E(t) integration, audio pipeline, and dashboard questions: answer from this appendix and the Q&A bank as far as they go. Anything deeper: *"Zuraiz built that part; we will follow up by email with the exact detail."* That is the agreed escape hatch, use it without hesitation.
- Logistics (ESMUC follow-up, cluster follow-up): note down whatever the supervisors answer; Zuraiz executes after the meeting.

## What the project actually is

We are building a single number, E(t), that captures how well a choir is coordinating at each moment in time. It is the average of three sub-numbers. A(t) is how synced the singers' voices are. V(t) is how synced their body movements are. N(t) is how the influence network between singers looks. The whole point is to give NMP tool makers (Jamulus, SoundJack, JackTrip) and music educators a number they can design against instead of designing by intuition.

## The binary we are testing

Either latency above some threshold breaks coordination (hard ceiling, NMP tools need new architectures) or human bodies compensate through visual cues like sway and breath (Honest Signals theory holds, design lesson flips to visual fidelity). Either finding is publishable.

## Three hypotheses

- H1: low-latency tools score higher on E(t) than high-latency tools.
- H2: the influence-network topology shifts from democratic to leader-dominated as latency rises.
- H3: visual signals add at least 10 percentage points of explained variance beyond audio alone.

## How E(t) is computed

`E(t) = (A(t) + V(t) + N(t)) / 3` in the published formula. The implementation uses `np.nanmean` over available signals so the score is defined even when one signal is missing. A(t) is pairwise audio coupling on RMS envelopes over 10-second windows. V(t) is the variance of pose-derived honest signals over the same window. N(t) is the influence graph density at piece level.

## Three tiers of data

- Tier 1: YouTube videos, mixed stereo audio, useful for video features only.
- Tier 2: academic multitrack datasets (Dagstuhl is the one we have), each singer on a separate microphone, useful for audio + network analysis.
- Tier 3: controlled latency injection, we synthetically delay one signal to simulate NMP regime variation.

## Four work packages

- WP1 audio: Zuraiz. Pyin pitch, onset detection, pairwise coupling.
- WP2 video: Hammad. MediaPipe pose and face, honest signal features.
- WP3 network: Hassan. Granger causality, influence graph, network metrics. **You.**
- WP4 dashboard: Kumaran. React frontend, FastAPI backend, paper figures.

## Why both Granger methods

Standard Granger looks at the actual values. COP-GC looks at the ordering only. Standard is parametric and well-understood, COP-GC is non-parametric and catches non-linear couplings the parametric test misses. Running both means we can report robust edges (significant under both) versus method-dependent edges (significant under one but not the other).

## Why the null model is circular-shift

An i.i.d. shuffle destroys within-stream autocorrelation, which would inflate the apparent significance because choir audio is strongly autocorrelated. Circular shift slides one stream relative to the other by a random offset, so within-stream structure stays intact and only cross-stream timing is broken. Standard practice per Stevens 2013.

## What you might get asked and how to deflect cleanly

If you are stumped, the safe escape hatch is: *"That is a good question. Let me check with the team and follow up by email."* Better than guessing wrong. Hacker and Gloor both prefer honest "I don't know" to fluent BS.

If asked anything DSP-specific (pyin internals, librosa specifics, Granger lag selection, optimisation choices), you can deflect: *"Zuraiz owns that one and can give you a more precise answer offline."*

If asked anything frontend-specific (D3, Plotly, Vite, React rendering): *"Kumaran owns the dashboard and can speak to that better than I can."*

If asked anything pose-specific (MediaPipe, OpenPose, calibration): *"Hammad owns that and we can loop him in."*

You own WP3 (Granger and influence graph), so don't deflect questions in that area. You are the right person to answer them.

## Final reminder

Speak slowly. Pause between slides. The deck is designed for 9 minutes inside the 8-10 minute window. Going under 7 minutes feels rushed. The pause for questions at the end is the most important moment, do not rush into it.
