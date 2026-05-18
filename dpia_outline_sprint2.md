# DPIA Outline — Project 8 Networked Choir Entanglement

**Document type**: Data Protection Impact Assessment (DPIA) outline per Art. 35 GDPR
**Project**: SNA-OSN-M Project 8 (Networked Choir Entanglement Platform)
**Controller**: Otto-Friedrich-Universität Bamberg (lead supervisor: Prof. Janine Hacker)
**Sub-processors**: none (all processing on team-owned hardware in DE)
**Filed by**: Zuraiz, on behalf of project team
**Date**: 2026-05-14
**Status**: Outline for DPO review (May-21 milestone), full DPIA before Jun-14 large-scale extraction.

---

## 1. Description of Processing

### 1.1 Data categories

| Category | Source | Volume | Sensitivity |
|:---|:---|:---|:---|
| Facial landmarks (MediaPipe FaceMesh, 468 points/face) | Tier-1 YouTube videos | ~25 videos × 5–20 singers × 5–30 min × 30 fps | **Art. 9 GDPR biometric** |
| Body pose keypoints (MediaPipe BlazePose, 33 joints/body) | Tier-1 YouTube videos | same as above | Art. 9 GDPR biometric |
| Pitch (F0) and onset time-series | Tier-2 academic datasets | Dagstuhl ChoirSet (5.1 GB), multitrack | Not personal data (acoustic features) |
| Aggregate Entanglement Index E(t) per video | Derived | scalar time-series per video | Not personal data |

Raw mp4 video and raw audio are **not retained** beyond the feature-extraction window.

### 1.2 Processing purposes

- Non-commercial academic research on the relationship between network latency and human coordination in online choir performance.
- Production of one Master's thesis paper (8–12 pages), one final 20-minute presentation, one open-source software package (`choir_entanglement`).
- No commercial use, no profiling of individuals, no automated decisions affecting subjects.

### 1.3 Processing operations

1. **Acquisition**: yt-dlp download of publicly listed YouTube videos under §60d UrhG TDM rights + EU DSM Directive 2019/790 Art. 3.
2. **Feature extraction**: MediaPipe FaceMesh/Pose + librosa pyin/onset run locally on team hardware. Per-frame landmarks written to parquet under `data/processed/`.
3. **Raw deletion**: mp4 files deleted within 72 h of feature extraction completion per `data_sourcing_policy.md §1`.
4. **Analysis**: cross-correlation, DTW, Granger causality on extracted features. Aggregate metrics only.
5. **Publication**: aggregate E(t) statistics, anonymised network diagrams, no individual singer identifiers.

---

## 2. Necessity & Proportionality

### 2.1 Lawful basis

- **Art. 9(2)(j) GDPR — Research exception**: processing of biometric data is necessary for scientific research purposes.
- **Art. 89 GDPR safeguards** in place: pseudonymisation at the per-video level (singer IDs replaced with `singer_01`, `singer_02`, …); aggregate-only reporting; no re-identification attempts.
- **§60d UrhG (DE)** + **EU DSM 2019/790 Art. 3** grant statutory text-and-data-mining rights on lawfully accessible sources for non-commercial scientific research, overriding YouTube ToS in DE jurisdiction.
- Open question: §60d UrhG applicability when paper is deposited on arXiv (non-DE-jurisdiction repository). Escalation to Bamberg legal desk requested.

### 2.2 Data minimisation

- Only the landmarks needed for body-sway and mouth-opening analysis are stored; raw RGB pixels are discarded.
- No demographic data (age, gender, ethnicity) collected, derived, or retained.
- Geographic identifiers (city, venue) not extracted from videos.

### 2.3 Storage limitation

- Raw mp4: ≤72 h post-extraction.
- Derived features: until project end (2026-07-31) + 6 months for paper revisions = 2027-01-31.
- After 2027-01-31: features deleted unless published as supplementary material under FAIR principles with a Zenodo DOI.

---

## 3. Risk Assessment

| Risk | Likelihood | Severity | Mitigation |
|:---|:---:|:---:|:---|
| Re-identification of singers from FaceMesh landmarks | Low | Medium | Aggregation only in publications; landmarks never released raw |
| Inadvertent inclusion of minors in YouTube videos | Low | High | Manual curation step excludes school-age choir performances |
| Re-identification via correlation with YouTube channel metadata | Medium | Low | Channel name and video title not stored alongside features |
| Feature parquet leaked from `data/processed/` | Low | Medium | `data/` gitignored; team laptops disk-encrypted (Win 11 BitLocker) |
| Sub-processor exposure | None | – | All processing local; no cloud APIs (MediaPipe runs on-device) |

---

## 4. Stakeholder Consultation

- **Bamberg DPO**: outline filed 2026-05-21 (this document). Awaiting review.
- **Supervisors**: Prof. Hacker (Bamberg) + Prof. Gloor (Köln/MIT) — informed at status meeting #3.
- **Data subjects**: not directly consulted (research exception applies; subjects are public-performance participants on public platforms).

---

## 5. Decision

- **Outline approved for May-21 status meeting**: yes/no [pending DPO]
- **Conditions before large-scale extraction (Jun-14)**: full DPIA filed; DPO sign-off; team-wide briefing on retention rules.
- **Outstanding items**: arXiv-jurisdiction question; minors-detection automated check (deferred to WP2 sub-plan).

---

## References

- GDPR Art. 9(2)(j), Art. 35, Art. 89
- §60d Urheberrechtsgesetz (DE)
- EU Directive 2019/790 on Copyright in the Digital Single Market, Art. 3
- Project data sourcing policy: `onsidian vault/OSN-M/wiki/07_legal_compliance/data_sourcing_policy.md`
- MediaPipe model cards: <https://developers.google.com/mediapipe/solutions/vision/face_landmarker>
