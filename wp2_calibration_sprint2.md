# WP2 Calibration Note — Sprint 2 Pilot (ouFyQKszE_Y)

**Source video**: Soundjack rehearsal Monday, 2021 June 7: Untraveled Worlds
**Channel**: New Jersey Gay Men's Chorus
**NMP regime**: NMP-SoundJack
**Duration**: 71.3 s (595 frames extracted)

## MediaPipe detection rates

| Component | Frames with detection | Notes |
|:---|:---:|:---|
| Pose (33-keypoint BlazePose) | 79.5% | nose visible across the video |
| FaceMesh (lip subset 40 indices) | 0.0% | upper + lower lip contour |

## Derived feature stability

| Feature | Std dev (normalised) | Interpretation |
|:---|:---:|:---|
| shoulder_rise (breath proxy) | 0.1374 | Higher = more breathing motion captured; should be non-zero for visible singer |

## Acceptance for WP2 milestone

The Apr 30 plan called for `head-sway Pearson correlation against a reference tool ≥ 0.70` as the calibration target. This pilot is a coverage check, not a reference-tool comparison. Reference-tool comparison (OpenPose or manual annotation) is the Sprint-3 next step before scaling to the full Tier-1 corpus.

## Sprint-3 follow-ups

1. Run extraction on the remaining 21 Tier-1 verified URLs (batch overnight, store per-video parquets).
2. Compare MediaPipe head-sway against an OpenPose reference run on 3 randomly sampled videos; report Pearson r.
3. If r < 0.70, fallback to OpenPose for the full corpus (R3 mitigation per PROJECT_GUIDE §9).
