---
title: P-15 5G IoMT Analysis
type: source
alchemy_stage: nigredo
tags: [5g, iomust, latency, reliability, nmp, deep_read]
ingested_date: 2026-04-23
last_deep_read: 2026-04-23
source_count: 1
related: ["[[iomust_paradigm]]", "[[latency_spikes_burst_errors]]", "[[nmp_on_the_edge]]", "[[deep_read_audit]]"]
team_take: Rigorous network-layer 5G benchmark. No human listening test, no actual musicians. 4 Elk LIVE devices co-located in one room, same base station — a radio interference worst case. Results must be compounded with WAN latency for realistic NMP.
---

# P-15 Latency and Reliability Analysis of a 5G-Enabled Internet of Musical Things System

**Citation**: Turchet, L., Casari, P. (2024). *IEEE Internet of Things Journal* 11(1), 1228 to 1240. [DOI:10.1109/JIOT.2023.3288818](https://doi.org/10.1109/JIOT.2023.3288818). CC-BY 4.0.
**Affiliations**: Department of Information Engineering and Computer Science, University of Trento, Italy.
**Funding**: European Space Agency Grant 4000132621/20/NL/AF.
**raw path**: `raw/01_primary_sources/Latency_and_Reliability_Analysis_of_a_5G-Enabled_Internet_of_Musical_Things_System.pdf`

## 1. Setup (§III)

- **Private 5G Standalone (SA) network**
- Up to **4 Elk LIVE NMP devices** as endpoints
- Customer premise equipment: **ZTE MC801A1** per device
- RAN: ZTE V9200 BBU + ZTE QCell R8149 antenna
- Band: **3GPP n78** (3.3 to 3.4 GHz), TDD, 30 kHz subcarrier spacing, 5G NR numerology 1, 500 µs radio frame
- Core network + MEC server, all fiber-linked
- Background traffic: 2 ZTE Axon 10 Pro 5G smartphones + iperf3
- **Peer-to-peer NMP topology**
- **Jitter buffer: ~10.66 ms** (included in all reported latencies)

**Nine conditions**:

- C1-C4: 1 to 4 boxes, no background traffic
- C5-C6: 4 boxes + UDP / TCP background traffic
- C7: 4 boxes no traffic (repeat baseline)
- C8-C9: 4 boxes + UDP / TCP traffic (repeats)

**Measurement protocol**: 3 recordings × 10 min per condition per box. First 30 s discarded. **1.35 million packets per box per condition** analyzed. Windows of 2.33 s (1750 packets of 64 samples).

## 2. Raw Data Block

| Metric | All Conditions Mean | Limits Observed | Source |
| :--- | :--- | :--- | :--- |
| Average one-way latency (includes 10.66 ms jitter buffer) | **< 24 ms** | max never > 29 ms | [§V Discussion] |
| Packet loss probability | **< 10⁻² (0.01)** | — | [§V] |
| Block Error Ratio (BLER) on radio | 0.08 | expected 0.05 per ZTE trials | [§V Discussion] |
| Max consecutive packet loss bursts | — | up to **151 packets** observed | [§V] |
| Pearson r (latency vs. loss) | **< 0.3**, p < 0.01 | weak, different root causes | [§IV Results] |

**CDF highlights (4-box conditions)** [§IV, Fig. 7]:

- 4 boxes (no traffic): 99.3% packets ≤ 24 ms
- 4 boxes + UDP bg: 92.8% packets ≤ 24 ms
- 4 boxes + TCP bg: 98.1% packets ≤ 24 ms

**Statistical findings** [§IV, Fig. 4]:

- **Latency significantly increases** with number of boxes (all relevant pairs p < 0.001)
- **Latency significantly increases** with presence of background traffic (UDP and TCP, p < 0.001)
- **Reliability metrics NOT significantly different** across conditions (proportional-fair scheduler allocates bandwidth fairly; errors span both NMP and background packets)

**Design target (from §II, literature)**: end-to-end 20-30 ms latency corresponds to ~8-10 m air propagation, considered maximum for traditional musical interplay.

## 3. Limitations

**Stated** [§V Discussion, §VI Conclusions]:

- 4 endpoints **co-located in same room, same base station** — a radio-interference worst case vs. typical distributed NMP.
- **No WAN component** in test; results must compound with WAN delays for realistic deployment.
- CN optimized for uplink/downlink, not peer-to-peer — imposes transit delays on P2P.
- BLER 0.08 slightly higher than 0.05 expected because transport blocks configured for throughput maximization, not interference resilience.
- Other ZTE QCells in the same research area may sporadically interfere.
- **UR-LLC not used**; retransmission and audio redundancy not activated.
- Future 5G network designs need to "improve in terms of latency and reliability" for NMP.
- Slicing and MEC mechanisms "yet to be properly explored for the case of musical interactions."

**Implicit (binding on Project 8 citation)**:

- Single equipment manufacturer (ZTE), single 5G band (n78 mid-band). mmWave and low-band 5G not tested.
- Single endpoint model (Elk LIVE). Software NMP on commodity hardware not benchmarked.
- No human listener or musician in loop; no MOS, no perceptual metric, no ensemble performance.
- No objective audio-quality metric (paper flags that PEAQ is not appropriate for packet-loss evaluation but proposes no alternative).
- Private 5G deployment; public 5G operator network behavior may differ.
- No correlation of burst-error length with musical-perception impact.

## 4. Relevance to Project 8 E(t)

**P-15 is relevant for**:

- **5G latency benchmark numbers**: average <24 ms, max <29 ms for 4 endpoints, no WAN. Key data for WP3 discussion of network-transport budget.
- **Burst-error failure mode**: up to 151 consecutive lost packets observed [[latency_spikes_burst_errors]].
- **Proportional-fair scheduler claim**: 5G RAN handles mixed NMP + background traffic without reliability degradation (ΔAUC-like statement for reliability).
- **Packet loss and latency uncorrelated**: supports treating them as independent failure modes in [[limitations_register]].

**P-15 is NOT**:

- Evidence that 5G enables "professional-grade entanglement." P-15 measures network, not entanglement, not E(t).
- Evidence of human-perceivable audio quality (no listening test).
- Evidence for any network topology other than P2P-via-5G with no WAN.
- Evidence that 5G is "ready" for NMP — authors explicitly state current 5G "need[s] to improve in terms of latency and reliability" for NMP.

## 5. Corrections Logged Against Prior Digest

See [[deep_read_audit]] for full table. Summary:

| Issue | Prior claim | Corrected reading |
| :--- | :--- | :--- |
| Missing experimental design specifics | "Up to four nodes" | 4 × Elk LIVE + ZTE 5G SA equipment, n78 band, co-located in same room (worst-case radio interference) [§III]. |
| Missing exact measurement results | "Under 24ms total (including 10.66ms jitter buffer)" | Average <24 ms, max <29 ms. 4-box CDF: 99.3% ≤24ms (no traffic), 92.8% (UDP bg), 98.1% (TCP bg). BLER 0.08. Bursts up to 151 consecutive packet losses [§IV, §V]. |
| Missing "latency increases with nodes/traffic" statistical finding | "Reliability did not significantly vary" | Latency DID significantly increase with both (p < 0.001). Reliability did NOT (different root causes) [§IV]. |
| "5G is a viable carrier for professional-grade entanglement E(t) ≈ 1 if MEC is used" | — | Over-reach. Paper does NOT measure entanglement or E(t). Authors explicitly say current 5G needs to improve in latency and reliability for NMP [§VI]. MEC contribution is discussed as future work, not validated in this paper. Moved to §4 as extrapolation. |
| Missing WAN caveat | (no mention) | Results are **wireless-link only**. For realistic NMP deployment, WAN latency/reliability must compound. Authors emphasize this as key scope limit [§I, §V]. |
| Missing "co-located in same room" caveat | (no mention) | 4 endpoints in same room, same base station — worst-case radio interference. Distributed NMP may perform differently [§V]. |
| Missing "UR-LLC not used" | (no mention) | UR-LLC explicitly not activated. Retransmission and audio redundancy not activated. These are future-work items [§V]. |
| Missing BLER discussion | (no mention) | BLER = 0.08, higher than expected 0.05 from ZTE trials. Due to transport-block config optimizing throughput not resilience [§V]. |
| Missing "current 5G insufficient for NMP" conclusion | "Confirms that 5G is a viable carrier" | Authors' own conclusion [§VI]: current 5G "need[s] to improve in terms of latency and reliability in order to properly support NMPs, especially when involving a WAN between the end users." Prior digest reverses this. |
