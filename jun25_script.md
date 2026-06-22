# Jun 25 Status Meeting V, Speaker Script

**Project 8 · Entanglement in Online Choir · 2026-06-25 · 14:00 CET**

> 8 slides, ~9 min spoken. Plain language, "we"/"the team". Presenters: Zuraiz and Kumaran Vasu. Appendix at the bottom is private prep.

---

## Slide 1: Title (15 sec)

Hello, we're Zuraiz and Kumaran, presenting for Project 8 at status meeting five. I'll recap our goals, walk through this iteration's main result on latency, show the dashboard now running on real data, give the next-iteration plan, and close with the retrospective and two questions.

## Slide 2: Recap (60 sec)

Our number is E(t), the Entanglement Index: one score per moment combining audio coupling, visual coupling, and the influence network. Three hypotheses, unchanged. H1: lower latency means better coordination. H2: the influence network gets more leader-dominated as latency rises. H3: visual signals add information.

We're at status meeting five of six. Last time, E(t) became operational. This iteration had one job: test H1 for the first time, by injecting controlled network latency.

## Slide 3: Headline, we found the latency signal (90 sec)

This is the main result, and it came with a twist worth telling honestly.

First we injected a constant delay into clean studio recordings. E(t) didn't move. The reason: our audio coupling searches over time lags to find who-leads-whom, so a constant delay just slides inside that search window and gets absorbed.

So we pivoted to realistic jitter, random timing noise, with the spread taken from the actual measured Jamulus numbers. The composite E(t) still stayed flat. The deeper reason: E(t)'s audio term is a ten-second loudness envelope, which is physically robust to timing noise of a few tens of milliseconds.

That told us we were measuring the wrong thing. So we added the measure that latency actually breaks: onset synchrony, do the singers attack notes at the same instant, measured at zero lag. And there the signal appears clearly: attack-timing synchrony drops by well over half, between 57 and 76 percent depending on the dataset, as latency rises to Zoom-class levels, on every piece. Loudness coupling barely moves.

The headline: latency degrades attack timing, not loudness coupling. A naive envelope metric would have told us "latency doesn't matter," which would have been wrong.

## Slide 4: The dissociation (45 sec)

This figure is the whole story in two panels. Left: onset synchrony, the attack-timing measure, falling steeply with jitter across all three datasets. Right: the loudness-envelope E(t), flat. Same recordings, two measures, opposite verdicts. The gap between these two panels is the finding.

And we're being upfront: the jitter levels are the measured values, not tuned; onset synchrony was chosen in advance as the physical target, not fished for; and we report the constant-delay dead end rather than hiding it.

## Slide 5: It replicates across datasets (60 sec)

We didn't want this to be a one-dataset fluke, so we ran it on three corpora, twenty-eight pieces total. Dagstuhl, real human multitrack: attack timing down 57 percent. ESMUC, a second independent human dataset: down 66 percent. ChoralSynth, fully synthetic: down 76 percent. Two independent human datasets plus synthetic, all showing the same monotonic degradation.

To do this we added both datasets this iteration, downloaded and checksum-verified, behind one unified data adapter, so the same pipeline now runs on all three.

## Slide 6: Dashboard alpha on real data (45 sec)

The dashboard now runs on real outputs, not mock data. The timeline shows the real E(t), the graph is the real who-leads-whom influence network, and the video panel plays a real rehearsal with the 33-point pose skeleton tracked on top. Each piece shows the signals it actually has: studio pieces show audio and network, the YouTube videos show video and pose. That meets the dashboard-alpha milestone.

## Slide 7: Next iteration (45 sec)

Next, to status meeting six on July 9: fold onset synchrony into the E(t) definition as its timing-sensitive component; finish the cross-dataset corpus and per-window networks; pose-process all the remaining Tier-1 videos; and start writing up the report. The hard milestone is a first report draft with this latency result written up.

## Slide 8: Retrospective and questions (45 sec)

Retrospective: the best thing this iteration was that a wrong first method, constant delay, was caught by its own control and turned into a sharper one. We also corrected a stale note that had wrongly flagged the ESMUC dataset as restricted, it's open, and we used it. Limitations, stated plainly: injecting latency into pre-recorded audio tests transmission timing, not a live singer's adaptation; and the envelope E(t) on its own is latency-blind, which is exactly why onset synchrony matters.

Two questions. To Professor Hacker: now that onset synchrony is the measure carrying the latency effect, should the report foreground it over the composite E(t)? To the coordinators: we've contacted ki-support about cluster access for the final full-scale run.

Thank you. Questions.

---

# Appendix: prep notes (private)

- **If asked why E(t) is flat but H1 holds**: E(t) here is dominated by the loudness-envelope term, which is lag-tolerant. The latency effect lives in attack timing (onset synchrony). Next iteration folds onset synchrony into E(t) so the composite becomes latency-sensitive too.
- **If asked "did you tune the jitter to get this"**: no. Jitter SDs are the measured P-11 inter-chorister timing SDs (46 ms LAN, 57 ms WAN). Onset synchrony was chosen a priori as the physical quantity latency breaks. The constant-delay null result is reported.
- **If asked about ChoralSynth being synthetic**: its absolute coupling is weaker (machine-rendered voices), but the relative degradation with latency is the strongest of the three (−76%), and two real human datasets bracket it (−57%, −66%).
- **If asked about p-values**: per-cell null is 100 circular-shift shuffles (p-resolution 0.01); the paper-scale run uses 2000 (the cluster request).
- **Deflect**: audio/integration internals → Zuraiz; pose/MediaPipe → Hammad; dashboard → Kumaran.
