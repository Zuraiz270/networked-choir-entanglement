# Jul 23 Final Presentation, Speaker Script

> Two voices: **Hammad** speaks slides 1-5, **Zuraiz** speaks slides 6-14 and drives the demo.
> Word budget ~2200 spoken words for ~18 minutes, leaving buffer for the 60-second demo inside slide 10.
> Rehearse on the presentation laptop with the dashboard already warm (backend + frontend running, both demo pieces preloaded).

---

## Slide 1: Title (Hammad)

Hello everyone. We are presenting Project 8, Entanglement in Online Choir. I am Hammad, and I will walk you through the question, the data, and the method. Zuraiz will then present the results, run the live demo, and close. Hassan and Kumaran contributed across the network and data work packages.

## Slide 2: The question (Hammad)

Here is the core idea in one sentence: when a choir sings together over the internet, the network becomes part of the instrument, and we measured what it does to togetherness.

Our central metric is E of t, an entanglement index. It blends three channels into one coordination score over time: how coupled the voices are, how coupled the influence network is, and, where video exists, how coupled the bodies are.

We fixed three hypotheses before running anything, each with an operational metric and a predicted direction. H1: higher latency reduces coordination, measured as zero-lag onset synchrony. H2: influence networks show leadership structure, measured as out-degree centralization against a random null. H3: visual body signals add information beyond audio. We committed to reporting whatever the data said, including nothing.

## Slide 3: Data (Hammad)

We used three tiers of data, and one constraint shaped everything.

Tier 1 is twenty-nine virtual-choir videos from YouTube, of which eighteen have usable pose tracking. They give us visual signals: body sway and breathing gestures. Tier 2 is real multitrack choir recordings, Dagstuhl and ESMUC, plus ChoralSynth as a synthetic control, twenty-eight pieces in total, where every singer has their own microphone. Tier 3 is not a dataset but an operation: we inject controlled latency into the clean Tier 2 recordings.

The honest constraint: no piece anywhere has audio, video, and network signals together. Tier 2 has per-singer audio but no video. Tier 1 has video but only a mixed audio track. Every claim tonight respects that boundary.

## Slide 4: Method (Hammad)

The latency grid works like this. Each clean piece is degraded through five regimes, from the in-person threshold at twenty-five milliseconds, through two Jamulus settings, up to a Zoom-class regime with one hundred fifty milliseconds delay, eighty milliseconds jitter, and eight percent dropout. Then every metric is recomputed for every piece in every regime. Because the same piece appears in all regimes, each piece is its own control.

Statistics: every coordination number is tested against a circular-shift null. We rotate each stream against the others, which preserves each stream's internal structure but destroys the alignment between them. The final grid uses two thousand shuffles per cell; that rerun finished on the Erlangen cluster last week.

## Slide 5: Reproducibility (Hammad)

Before results, one slide on trust. One command regenerates the summary results from committed data. Forty-four automated tests cover every pipeline stage. The cluster submission script for the two-thousand-shuffle grid is committed and validated. And every number on the next slides traces to a committed CSV file. Zuraiz takes it from here.

## Slide 6: H1 result (Zuraiz)

Thank you, Hammad. Here is the headline.

When we push clean recordings toward Zoom-class conditions, onset synchrony, whether singers land their notes together, collapses. Minus fifty-six point five percent on Dagstuhl. Minus sixty-five point one on ESMUC. Minus seventy-five point one on the synthetic corpus. Across all twenty-eight pieces, about minus seventy-one percent, and the fall is monotonic: every step of added jitter costs timing.

Loudness coupling, in contrast, barely moves. On Dagstuhl it is flat to within half a percent.

So H1 is supported, and it is supported in a specific channel: latency breaks when you sing, not how loud you sing.

## Slide 7: The dissociation (Zuraiz)

I want to be transparent about how we got there, because the detour is part of the result.

Our first attempt used constant delay and envelope coupling, and it showed nothing. The control caught why: envelope coupling tolerates lags, and constant delay is precisely a lag. So we specified, in advance, the physical quantity jitter should break, zero-lag onset synchrony, and reran. The effect appeared in every single piece.

We kept the null result in the report. The dissociation itself, timing collapses while loudness holds, is the finding. An envelope-only study would have concluded latency is harmless. It is not.

## Slide 8: H2 result (Zuraiz)

H2 asks whether choir networks have leaders. Prof. Hacker pushed us in May to define leader dominance operationally, and this slide is that answer. Leader dominance is the Gini coefficient of out-degree in the Granger-causal influence graph: zero means democratic, one means a single driver.

Human choirs sit measurably above a density-matched random null: observed mean zero point one five four against zero point one three nine. Three of five Dagstuhl pieces and two of three ESMUC pieces are individually significant. The synthetic corpus sits at chance, two of twenty.

That contrast matters: leadership shows up in human singing and not in synthetic renderings of the same kind of music. So it is a human coordination signal, not an artifact of our pipeline. H2 is partially supported; its original latency-driven form cannot be tested with injected delay, and we say so.

## Slide 9: H3 result (Zuraiz)

H3 is the honest one. We promised at the June review a first visual-onset experiment on the eighteen pose-usable videos, and we ran exactly that: pose-derived motion against the audio onset envelope, best lag within two seconds, one thousand circular-shift nulls per video.

The answer is null. Seventeen of eighteen videos were analyzable, one turned out to have a digitally silent first ninety seconds. One of seventeen came out significant, which is what chance predicts. Median correlation zero point zero seven.

The measurement is not broken: on synthetic coupled signals it recovers known lags reliably; those tests are in the suite. So the null is informative. Ensemble-level motion of one tracked body does not couple to a mixed audio envelope. If you want visual entanglement, you need per-singer audio and video together. H3 stays data-blocked, and now that requirement is demonstrated rather than assumed.

## Slide 10: Live demo (Zuraiz)

Now sixty seconds of the platform itself.

[Demo choreography: dashboard already open. Piece 1, Dagstuhl quartet: press play, let E(t) draw for ~20 seconds, point at the influence graph edges. Switch to the Tier-1 piece: play video, pose overlay tracks the singer, ~20 seconds. Close with the metadata panel showing per-piece signal availability.]

What you saw is real committed data, running locally, no mock content. The metadata panel is the honesty layer: it shows which signals each piece truly has.

## Slide 11: Fallback (Zuraiz, only if demo fails)

[If the live demo cannot run: show this screenshot, narrate the same two-piece story, and move on without apology.]

## Slide 12: Limitations (Zuraiz)

Five limitations, stated plainly. Injected latency models transmission, not how singers would adapt live. No piece has all three signal types, so full E(t) has never run with all channels at once. The visual analysis covers one tracked stream over each video's first minute. A minority of individual grid cells are not significant on their own; the claims ride on corpus-level trends. And the entanglement formula comes from email-network research; this is its first music-domain test.

## Slide 13: Contributions (Zuraiz)

Four things we hand over. A latency signature for online choirs, timing collapse between fifty-six and seventy-five percent at a paper-grade null. An operational leadership measure that separates human from synthetic choirs. A demonstrated, no longer hypothetical, data requirement for visual entanglement. And a reproducible pipeline: one command, forty-four tests, every claim traceable.

## Slide 14: Close (Zuraiz)

Next steps are two recordings away: real latency-varied live sessions for H1 and H2 in their strong forms, and a small paired audio-video corpus for H3. The final report is due July thirty-first; draft one has been complete since June.

Thank you. We are happy to take questions.
