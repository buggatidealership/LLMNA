# Competitive Map — Who Competes With Whom

**Last updated:** 2026-07-22

## 📌 [2026-07-22] RACK-SCALE BATTLE UPDATE — first at-scale non-NVDA hyperscaler rack (per `signals/cross-source-log/2026-07-22-wed-tue-catchup-14screenshot-batch.md`)
Microsoft deploys AMD Helios racks on Azure AT SCALE for its OWN frontier-model inference (T1, Jul-20-2026) — MSFT is the 4th Helios customer (OpenAI 1GW Oct-25, Oracle 50K MI450 Oct-25, Meta), but the FIRST hyperscaler running its own frontier models on non-NVDA rack architecture. NVDA held ~95% DC-GPU share per the relayed commentary (T3, unverified precision). The counter-datum keeping this a WATCH not a shift: NVDA's wafer allocation (>half of TSMC's ~85%+-locked '26-'27 leading edge, T2) and CPO commitment via the OCI consortium.
**Two-branch pre-registration (Anthropic, B64-guarded — adjudicate at today's Advancing AI keynote):** (a) Anthropic named GW-level Helios customer today → NVDA-moat-erosion counter-thesis gains its 3rd independent leg (MSFT-at-scale + wafer-secured roadmap + frontier-lab second-sourcing) → open a named watch item; (b) NOT named → per press read, ROCm software-maturity concerns unresolved → the moat holds at the software layer, log and hold. Either branch books a datum; neither is a position trigger.


## TL;DR

The AI sector has multiple parallel competitive battles. Same companies are partners in some battles and rivals in others. This map identifies the key battles for portfolio sizing.

## Battle 1 — AI compute silicon

| Combatant | Position | Share (est) | Strategy |
|---|---|---|---|
| NVDA | Dominant | ~80% DC AI | Full-stack (GPU + networking + software) |
| AMD | Challenger | ~5% | MI series for inference; EPYC for CPU side |
| Google TPU (via AVGO) | Hyperscaler in-house | ~5% inference | Cost-optimized custom for Google workloads |
| AWS Trainium (via MRVL) | Hyperscaler in-house | ~3% inference | AWS-specific cost optimization |
| Microsoft Maia | Hyperscaler in-house | <2% | Early innings |
| Meta MTIA | Hyperscaler in-house | <2% | Early innings, ranking/ads workloads |
| Intel Gaudi | Niche | <1% | Unproven |
| Specialized (Groq, Cerebras, etc.) | Niche/pilot | <1% | Workload-specific advantages |

**Battle dynamics:** NVDA holds training + premium inference. Custom Si tries to take cost-sensitive inference. Battle is most active in the inference layer.

## Battle 2 — Hyperscaler AI infrastructure

| Combatant | Position | Strategy |
|---|---|---|
| MSFT Azure | Co-dominant | OpenAI partnership; enterprise reach |
| AWS | Co-dominant | Scale + Trainium + Bedrock; sovereign AI partner |
| Google Cloud | Strong third | TPU + Gemini stack; differentiated |
| Oracle Cloud (ORCL) | Niche but growing | Stargate partner; large contract focus |
| Meta | Internal-use focused | Llama + in-house infra; not selling externally |

**Battle dynamics:** Top 3 are roughly co-equal in AI infra spending. Oracle is the wild card via Stargate. Meta is a buyer not a seller.

## Battle 3 — Foundry

| Combatant | Position | Notes |
|---|---|---|
| TSMC | Monopoly on advanced AI node | Single source for Blackwell, Rubin, all custom Si |
| Samsung Foundry | Distant second | Memory + some logic; not the AI node |
| Intel Foundry | Strategic option | Long ramp; sovereign / strategic interest |

## Battle 4 — Memory (HBM)

| Combatant | Position | Share (est) |
|---|---|---|
| SK Hynix | Leader | ~50%+ HBM |
| Samsung | Catching up | ~35% |
| Micron (MU) | Ramping | ~10–15% |

**Battle dynamics:** SK Hynix has the technology lead. Samsung is fighting on price + scale. Micron is the smaller, US-based, geopolitically-clean option.

## Battle 5 — Networking (AI back-end)

| Combatant | Position | Strategy |
|---|---|---|
| Arista (ANET) | Leader in AI ethernet | Standard ethernet at scale |
| NVDA Spectrum-X | Full-stack integration | Sold as part of NVDA system |
| MRVL | Custom silicon | DPUs, networking ASICs for hyperscalers |
| Cisco (CSCO) | Incumbent | Legacy ethernet, less AI-relevant |
| COHR, LITE | Optical components | CPO transition winners |

**Battle dynamics:** Arista vs Spectrum-X for who owns the AI back-end. Hyperscalers play both sides.

## Battle 6 — Power (firm generation)

| Combatant | Position | Edge |
|---|---|---|
| VST (Vistra) | Largest IPP with nuclear + gas | ERCOT exposure |
| CEG (Constellation) | Largest nuclear pure-play in US | ESG-friendly |
| TLN (Talen) | Smaller IPP, high leverage | Volatility |
| NEE (NextEra) | Regulated utility + renewables | Larger pipeline |
| GEV (GE Vernova) | Turbine supplier | Wins on new gas builds + SMR roadmap |

**Battle dynamics:** Different vehicles for the same theme (power supply for AI). VST/CEG most direct; GEV for the building-it-out angle.

## Battle 7 — Enterprise AI software

| Combatant | Position | Strategy |
|---|---|---|
| MSFT (Copilot, Azure AI) | Co-dominant | Embed AI into Office + Azure |
| GOOG (Workspace AI, Gemini) | Co-dominant | Gemini + Google Cloud AI |
| PLTR | Defense/gov leader | Agentic-native architecture |
| NOW | Workflow automation | Agentic-adjacent |
| Specialized vertical AI | Niche | Industry-specific moats |

## Partnerships that matter (cross-battle alliances)

- NVDA + TSMC (compute → foundry)
- NVDA + Anet (lukewarm — Spectrum-X is competitive, but ANET is preferred ethernet partner)
- AVGO + Google (custom TPU)
- MRVL + AWS (Trainium)
- MRVL + Meta (MTIA components)
- CEG + Microsoft (nuclear PPA, Three Mile Island restart)
- VST + Amazon (nuclear PPA, Susquehanna)
- Oracle + everyone (Stargate consortium)

## Strategic recurring patterns

1. **Hyperscalers as dual customers** — they buy NVDA AND build custom Si. Their leverage grows over time.
2. **NVDA's full-stack moat erodes if any layer cracks** — most vulnerable layer is networking (ANET competition) and the custom-Si threat.
3. **Power is the equalizer** — efficient silicon wins as power constraint tightens, helping NVDA Blackwell efficiency over commodity alternatives.
4. **Vertical software wins late** — competitive landscape becomes interesting only after agentic infra is established.
