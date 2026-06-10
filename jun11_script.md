# Jun 11 Status Meeting IV, Speaker Script (Hassan Ahmed)

**Project 8 · Entanglement in Online Choir · 2026-06-11 · 14:00 CET**

> Presenter: Hassan Ahmed (on behalf of the 4-person team). Target spoken time: 9 minutes 0 seconds. 10 slides, ~54 seconds per slide average. Speak in plain language, "we" and "the team" throughout, no DSP jargon unless asked. The full project context appendix is at the bottom of this file for Hassan to read once before the meeting.

---

## Slide 1: Title (15 sec)

Hello everyone. I'm Hassan Ahmed, presenting on behalf of the Project 8 team for status meeting four. Today I'll walk through what we shipped in Sprint 3, what the headline result says, and the plan for Sprint 4.

---

## Slide 2: What we said we'd do, Sprint 3 plan recap (50 sec)

Quick recap of what we committed to three weeks ago at status meeting three.

Six deliverables. Four core: WP1 audio scale, WP2 video on 10 Tier-1 clips, WP3 influence graph on 5 pieces, WP4 dashboard scaffold. Two stretch: E(t) end-to-end with the null model, and the full-corpus WP3 metrics tabulation. The stretch items were officially due June 14 in the brief.

All six shipped. The two stretch items came in 23 days early. We will walk through each one in the next slides.

---

## Slide 3: Headline result (75 sec)

This is the slide that matters most. The Entanglement Index is now operational end-to-end.

We ran E(t) on all five Dagstuhl pieces with both audio and network signals, with a 200-shuffle circular-shift null model per piece. Every single piece beats its null at p less than one in a thousand.

The figure on the slide shows the result. Five red dots are the observed mean E(t) per piece. Five gray error bars are the 95% interval of the null distribution under random shuffling. Every red dot sits clearly above its gray bar.

The pattern splits cleanly by piece. Locus Iste pieces cluster at 0.74 to 0.80. Tu Pauper Es pieces cluster at 0.57 to 0.68. What's interesting is that the split is not by ensemble size. A four-singer quartet of Locus Iste sits with the eight-singer full choir of Locus Iste, not with the four-singer quartet of Tu Pauper Es. Piece identity dominates ensemble size. We interpret this as Locus Iste being a homophonic chant where everyone moves together, and Tu Pauper Es being more polyphonic with independent voice entries.

The takeaway: the number we have been promising since April is operational, repeatable, and significantly above chance.

---

## Slide 4: WP1 audio scale (50 sec)

WP1 went from one piece in Sprint 2 to 25 pieces in Sprint 3. That is every musical take in the Dagstuhl ChoirSet across Locus Iste and Tu Pauper Es. 130 newly extracted per-singer parquets, 288 pairwise audio couplings. Total runtime was 78 minutes on a Windows laptop.

The pipeline is resumable, so it survives interruptions, and it prefers the cleanest microphone per singer, dynamic first then head-mounted then larynx.

The per-piece coupling pattern matches musical structure. The basses singing alone couple very tightly, around 0.80. Full-choir polyphonic pieces drop closer to 0.45. This is exactly what you would expect.

---

## Slide 5: WP3 influence graph and COP-GC (60 sec)

This is Professor Hacker's flagship. The 2x3 grid on the slide shows directed influence graphs for the five Sprint-3 pieces, plus a comparison panel.

We shipped two methods. Standard parametric Granger as primary. And the COP-GC ordinal-pattern variant from Zanin 2021, which we had been promising since the implementation plan. Both methods run on all five pieces and produce Gephi-compatible graph files.

The Sprint-2 Hacker flagship reproduces exactly. 11 of 12 significant edges, density 0.917, soprano leads.

The most interesting finding is method-divergence on Tu Pauper Es full choir, the bottom-middle panel. Standard Granger flags 42 of 56 directed edges as significant. COP-GC flags 25. The bottom-right panel shows the COP-GC version of the same piece. Visually you can see the graph is noticeably sparser. The 17-edge gap represents couplings that depend on linear magnitude rather than pattern structure. We carry both methods forward and let the contrast inform the discussion section.

---

## Slide 6: WP2 pose on 10 Tier-1 videos (55 sec)

WP2 went from one Tier-1 video in Sprint 2 to 10 in Sprint 3, stratified across the four NMP regimes. Total runtime was 2.3 minutes.

5 of 10 videos pass the 50% pose-detection floor. The figure on the slide shows the best one, a Jamulus rehearsal with 6 singers and 98.5% detection.

The 5 failing videos are software-UI screen captures or dense low-resolution tile grids where MediaPipe finds no body. That is a property of the input, not of the pipeline.

This matches the "try and iterate" guidance we got from Status Meeting III. We document the limitation, define the 5 passing videos as our WP2 inclusion set for H1 testing, and proceed.

---

## Slide 7: WP4 dashboard scaffold and E(t) integration (60 sec)

Two pieces on one slide, both shipped this sprint.

On the left is the WP4 dashboard. React 18, Vite 5, TypeScript strict, FastAPI 0.111 backend. Four panels: video player placeholder, D3 force-directed influence graph, Plotly E(t) timeline, metadata strip. It runs against mock JSON right now. The screenshot on the slide is a Playwright capture of the four-panel layout rendering live in a browser.

On the right is the E(t) integration module that powers the timeline. It takes the audio, video, and network signals from the other work packages, aligns them on a common time grid, and emits the composite E(t). When one signal is missing, the formula reallocates weight to the available signals so the score is always defined. Right now V(t) is absent across the board because no piece in our corpus has both audio and video natively. The module is ready for V(t) the moment Tier-3 multimodal recordings exist.

23 of 23 tests pass.

---

## Slide 8: Sprint 4 plan (60 sec)

Sprint 4 runs from tomorrow until status meeting five on June 25.

WP1 audio adds per-window Granger to give us a time-varying N(t) signal that updates as the user scrubs the dashboard timeline. Due June 21.

WP2 video scales to all 21 remaining Tier-1 videos, with a quality-first triage so we keep what works and document what does not. Due June 30.

WP3 network is the big one. Tier-3 latency injection. We take the clean Dagstuhl audio, inject controlled jitter at four levels matching the NMP regimes, run E(t) at each level. This is the first time we get cross-regime variation in N(t). Due June 21.

WP4 dashboard swaps the mock JSON for real parquet readers and adds the pose overlay on the actual video. Due June 21.

The hard milestone is the dashboard alpha running real data by June 21.

---

## Slide 9: Retrospective and four limitations (60 sec)

What went well. We shipped six of six Sprint-3 deliverables. Two of the stretch items came in 23 days early. The doc-update discipline kept TEAM_BRIEF, PROJECT_GUIDE, and the vault wiki in sync after every phase, which means anyone joining the project can read three files and be current.

What did not go well. Two Tier-2 datasets, ESMUC and ChoralSynth, were planned in the implementation plan but did not get acquired this sprint. ESMUC is proprietary and requires a UPF license. ChoralSynth's access gate slipped. We will address both in Sprint 4 if the licensing path opens up.

Four limitations to flag explicitly so they are not surprises in Q&A.

One: V(t) is NaN in every current E(t) because Dagstuhl has no video. Two: the WP3 corpus is all studio recordings with no latency variation, so the cross-regime test is still ahead. Three: WP2 detection rate is 50%, and that defines the inclusion set we use going forward. Four: p_null reports as 0.0000 because none of the 200 nulls exceeded the observed, which means less than one in 200, not literal zero.

---

## Slide 10: Open questions for the room (40 sec)

Three questions. Two to the supervisors, one to everyone.

To Professor Hacker. Do you have direct access to ESMUC or ChoralSynth multitrack data that we could fold into Tier-2 before we pursue licensing ourselves in Sprint 4?

To Professor Gloor. For the final paper figure, do you prefer matplotlib-clean or Gephi-polished SVG for the alchemical-stage diagram?

To everyone. Is the July 23 final presentation in person at Bamberg or remote? Affects how the team coordinates travel.

Thank you. Open for questions.

---

# Appendix: Project context for Hassan (read once before the meeting)

This appendix is private prep for Hassan, not part of the spoken script. Read it once and you will have enough context to handle the live Q&A confidently.

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

Speak slowly. Pause between slides. The deck is designed for 9 minutes, but if you go 9:30 nobody will notice. Going under 7 minutes feels rushed. The pause for questions at the end is the most important moment, do not rush into it.
