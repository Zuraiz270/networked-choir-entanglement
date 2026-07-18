# Jul 23 Final Presentation, Speaker Script

> Hammad speaks slides 1-8. Zuraiz speaks slides 9-17 and drives the demo.
> Target: 10-12 minutes plus 3 minutes Q&A. The demo is limited to 60 seconds.

---

## Slide 1: Title (Hammad)

Hello everyone. We are presenting Project 8, Measuring Coordination in Online Choirs. I am Hammad. I will introduce our goals, prior work, project structure, data, method, and work process. Zuraiz will present the results, demonstrate the dashboard, and close with limitations and next steps.

## Slide 2: Goals and hypotheses (Hammad)

Our goal was to turn online-choir coordination into something measurable. We wanted to understand what network degradation changes, connect acoustic, visual, and influence-network signals, and make the complete analysis auditable.

We declared three hypotheses and their predicted directions at project start. H1 expects higher latency to reduce coordination. H2 expects influence networks to show leadership structure. H3 expects visual signals to add information beyond audio. The operational metrics were refined in dated revisions when controls exposed problems. We are showing that history rather than presenting the final metrics as if they never changed.

## Slide 3: Related work (Hammad)

The project connects three research areas. Entanglement research measures temporal alignment in organizational communication. Honest Signals treats activity, consistency, influence, and mimicry as evidence of group coordination. Choir and networked-music research provides multitrack recordings and well-known latency concerns.

The gap is that these sources do not give us one validated acoustic, visual, and influence measure for online choirs. Our contribution is a tested domain adaptation with clear limits, not a claim that an email-network measure automatically works for music.

## Slide 4: Whole-project structure (Hammad)

This diagram shows the full project from left to right. Tier 1 contains video with mixed audio. Tier 2 contains per-singer or per-part audio. Tier 3 is the controlled degradation derived from Tier 2. These sources feed separate audio, video, and influence-network pipelines. The integration layer then tests H1, H2, and the exploratory H3 experiment, and supplies the dashboard, report, figures, and presentation.

The important point is that the arrows preserve the data boundary. We never imply that Tier 1 has per-singer audio or that Tier 2 has video.

## Slide 5: Data (Hammad)

Tier 1 contains twenty-nine virtual-choir videos, with eighteen usable for pose tracking. Tier 2 contains five Dagstuhl pieces, three ESMUC pieces, and twenty ChoralSynth pieces. Tier 3 applies five controlled degradation regimes to all twenty-eight multitrack pieces.

No item provides synchronized per-singer audio and per-singer video. This is why H1 and H2 can use singer-level audio, while H3's full audio-plus-visual prediction test remains unavailable. The exploratory H3 run uses mixed audio and pose only, and we label it accordingly.

## Slide 6: Method (Hammad)

E of t combines whichever coordination components are available: acoustic A of t, visual V of t, and network N of t. For H1, every clean piece is processed through five regimes. The strongest regime combines one hundred fifty milliseconds delay, eighty milliseconds jitter, and eight percent dropout. Because delay, jitter, and dropout change together, we call this the Zoom-class regime and do not attribute the result to one parameter alone.

Envelope and network results use two thousand circular shifts per cell. The deterministic onset outcome uses a paired clean-to-Zoom sign test across pieces.

## Slide 7: Work process (Hammad)

We organized the work into acoustic and integration metrics, visual extraction, influence networks, and dashboard and report integration. Each iteration had to end in something reviewable: a schema, result table, test, figure, or presentation artifact.

The Virtual Mirror exercise found high shared meaning, low emotional exchange, and medium relationship intensity. That matched a team that was strongly task-focused. We added a short weekly asynchronous check-in so blockers and ownership changes appeared before the next meeting.

## Slide 8: Reproducibility (Hammad)

The final package is designed to be checked. One command regenerates the report-stage outputs. Fifty automated tests cover the scientific pipelines, report generation, figure definitions, and the dashboard's published E definition. The final latency grid contains all one hundred forty cells, and every number in the deck traces to a committed CSV. Zuraiz will now present the results.

## Slide 9: H1 result (Zuraiz)

The headline is that latency damages note timing. From clean to the Zoom-class regime, mean within-piece onset synchrony drops by fifty-six point five percent on Dagstuhl, sixty-five point one percent on ESMUC, and seventy-five point one percent on ChoralSynth. Across all twenty-eight pieces, the mean drop is seventy point seven percent. Every piece decreases, giving an exact one-sided sign-test p-value of three point seven three times ten to the minus nine.

Envelope coupling also falls, but an order of magnitude less: roughly eight percent on Dagstuhl and twelve percent across the corpus. The composite that also includes network density can rise because the density increase offsets the envelope decline. H1 is therefore supported specifically for attack timing.

## Slide 10: Measurement revision (Zuraiz)

Our first test used constant delay and lag-tolerant envelope coupling. It showed little effect because the metric could absorb the lag. We kept that null result. It demonstrated a mismatch between the manipulation and the outcome.

Zero-lag onset synchrony asks the physical question directly: do singers land note attacks together? It drops by fifty-six to seventy-five percent, while the pure envelope channel drops only about six to fourteen percent across corpora. The hypothesis direction did not change. The operational measure changed through a dated, documented revision, and that audit trail is part of the result.

## Slide 11: H2 result (Zuraiz)

H2 asks whether influence is concentrated in a small number of singers. We measure this with the Gini coefficient of out-degree in the Granger influence graph. The observed corpus mean is zero point one six two, compared with zero point one five five in matched random graphs.

One of five Dagstuhl pieces and one of three ESMUC pieces are individually significant. None of twenty synthetic pieces is significant. This is limited support only. Two significant results among twenty-eight tests are within chance expectation, and the human-versus-synthetic count contrast is suggestive rather than significant. We do not claim a general choir hierarchy.

## Slide 12: H3 result (Zuraiz)

For H3, we ran the exploratory experiment promised in the earlier status meeting. We compared pose-derived motion with the mixed-audio onset envelope over each video's recorded pose window, usually sixty to seventy-two seconds. The statistic is the maximum signed correlation within two seconds, tested against one thousand circular shifts.

Seventeen videos were analyzable. One of seventeen was significant, which is consistent with chance, and the median correlation was zero point zero six eight. Synthetic tests recover known coupling, so the estimator itself works. The result says that one pose stream plus mixed ensemble audio is not a useful substitute for synchronized per-singer audio and video.

## Slide 13: Live demo (Zuraiz)

Now I will show the implementation for sixty seconds.

[Open the preloaded Dagstuhl piece. Run the E(t) timeline and point to the influence graph for about twenty seconds. Switch to the preloaded Tier-1 video and show the pose overlay for about twenty seconds. End on the signal-availability metadata.]

The dashboard uses real local outputs and the same envelope-only E definition as the report. The metadata panel makes missing channels visible instead of filling them with invented values.

## Slide 14: Limitations (Zuraiz)

There are five main limits. First, injected latency models transmission but not how singers adapt live. Second, delay, jitter, and dropout co-vary, so their individual effects are not isolated. Third, no item has synchronized per-singer audio and video. Fourth, H2 has no corpus-level significance. Fifth, E of t is a proposed music-domain adaptation and has not yet been validated against perceived performance quality.

## Slide 15: Main results and implementation (Zuraiz)

The final outcome has four parts. H1 is supported for timing in all twenty-eight pieces. H2 has limited evidence in two human pieces. The exploratory H3 substitute is null and confirms the need for paired data. The implementation includes reproducible pipelines, a tested dashboard, figures, the final report, and this presentation package.

## Slide 16: Possible extensions (Zuraiz)

The strongest next study would record live singers under controlled network conditions, because that would include behavioral adaptation and could test latency-driven leadership. A synchronized per-singer audio-video corpus would unlock the planned H3 audio-only versus audio-plus-visual comparison. A factorial experiment could separate delay, jitter, and dropout, and external ratings could test whether E of t relates to perceived musical quality.

## Slide 17: Retrospective and close (Zuraiz)

What worked well was the use of controls, reproducible scripts, tests, and direct instructor questions about our definitions. Those checks improved the science. What could improve is securing paired multimodal data earlier, resolving work-package dependencies before parallel work, and confirming final format and metric expectations earlier in the course.

Thank you. We are ready for questions.

## Slide 18: Dashboard backup (only if needed)

[If the live demo fails, show the screenshot, describe the E(t) timeline, influence graph, pose overlay, and metadata panel, then continue.]

## Slide 19: Reproducibility backup (only if asked)

[Use this slide for questions about the exact sign test, matched-network null, H3 circular shifts, cluster grid, or locked environment.]
