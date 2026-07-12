# 2026-07-12 SUN EVE — AI Intelligence Brief (Jul-12 morning edition) routing + verification

**Source:** user-relayed aggregator brief (T3 chain: HN/ArXiv/Reddit/RSS, cites Tom's Hardware/The Register). Rule #16: 2 Opus verifiers fired on the thesis-relevant items; verdicts appended below on landing.

## Routing table
| Item | Claimed source | Thesis relevance | Action |
|---|---|---|---|
| **SK Hynix CEO: shortage peaks 2027, lasts to 2030** | Tom's Hardware | **HIGH — SKHY held (structural branch), TC-1, SUMCO/Nanya adjacents** | VERIFYING (agent 1: original venue/date/quotes, Korean sweep, B40.1 recycle check, TrendForce-moderation coherence check) |
| **Microsoft carbon +25% FY2025 (AI DCs)** | Tom's Hardware | MEDIUM — TC-3/TC-13 power-cascade color; annual-report recycle risk HIGH (near-identical headlines in prior years) | VERIFYING (agent 2a: which report edition, released when, scope breakdown) |
| Colibrì: 1.5TB model on 25GB RAM (consumer CPU) | Tom's Hardware | LOW-MEDIUM — L28 Jevons/efficiency watch; PoC ≠ demand signal without usable throughput | VERIFYING (agent 2b: what it actually is, real perf numbers) |
| xAI Grok CLI telemetry collection | The Register | color — dev-trust/privacy; no held-name contact | LOG ONLY |
| Mesh LLM on Iroh (P2P inference) / Qwen3.5-122B Mac Studio fixes | Iroh/MRZK | color — local/distributed-inference current (consumer-hardware inference trend, worldview consumer leg) | LOG ONLY |
| LingBot-Video sparse-MoE world model (13B/1.4B active, DeepSeek-V3-style routing) | r/ML | color — robotics/world-model research current | LOG ONLY |
| KV-cache tutorial (Raschka) / DINOv2 vs SigLIP / GRPO reasoning-RL survey | Ahead of AI / r/ML | none — educational/benchmark color | LOG ONLY |
| UK universities AI cognitive-decline hearings | The Register | none — policy color | LOG ONLY |
| Lab Watch: "nothing notable" | — | licensed negative from a T3 aggregator; weekend quiet consistent with our own Leg B sweep | NOTED |

**Pattern note (B60/B61 discipline):** the two potentially cascade-worthy items both run through the same single secondary outlet (Tom's Hardware) — single-outlet dependence heightens the garble prior; verdicts must pin the primary sources.

## Verification verdicts (appended post-landing)

### 1. SK Hynix CEO shortage claim — CONFIRMED-FRESH (T1)
- **Kwak Noh-jung, exclusive Reuters interview, Fri 2026-07-10 (Nasdaq debut day; wire L4N43B15I):** "We forecast that next year [2027] will be the worst year in the industry's history from the supply perspective"; "customer demand continues to go up, while our capacity has limitations"; demand to outstrip supply **BEYOND 2030** ("다음 10년까지" per Korean carriers) — the aggregator softened "beyond"→"through 2030" (directionally conservative garble, corrected here). Subject = **memory broadly, HBM/DRAM-driven; NAND was NOT the subject.** Customers signing long-term contracts in anticipation.
- **Freshness:** genuinely new (Jul-10) — but the THEME extends Chairman Choi's Mar-2026 "shortage to 2030" guidance; the new elements are the "2027 = worst year in history" specificity + Nasdaq-day venue.
- **Incentive flag (Rule #18/B63-adjacent):** dominant HBM vendor talking scarcity on listing day — carried with the datum. Survives refutation: on-record wire interview; echoed by Samsung/Micron exec commentary; directionally consistent with TrendForce Q3-26 prices still rising.
- **TrendForce coherence:** NON-CONFLICTING — TrendForce's +10-15% QoQ moderation note is a NAND consumer-price-tolerance story; Kwak's claim is HBM/DRAM supply-balance. Different product, different axis. The consumer-affordability-ceiling data actually supports the AI-concentrated character of the tightness.
- **NOT folded in:** Yongin Fab-1 "Feb-2027 early start, ~500k→~700k wpm" — attributed to a DIFFERENT exec (Ryu Seong-su, SK Hynix America) in a date-inconsistent fragment → REPORTED, date-unpinned, parked.
- **Cascades:** SKHY thesis (structural-branch supportive institutional signal, H3 nudge); TC-1 N+1 (fresh T1 CEO datum).

### 2. Microsoft emissions +25% — CONFIRMED-FRESH (T1 report Jul-9), with recycle-trap cleared + framing corrections
- **NEW report (Jul-9-2026 edition):** 20M t CO2e 2025 vs 16M 2024 = **+25% YoY** (computed, exact; ±1pt rounding). Multi-outlet cluster Jul-9/10 (Bloomberg/Fortune/Quartz). The lookalike May-2025 edition's "+23.4% vs 2020 baseline" is a DIFFERENT edition/denominator — recycle trap identified and cleared; next recurrence: check edition date + YoY-vs-2020-baseline.
- **Load-bearing datapoint for the power narrative:** electricity-related emissions rose **2% → 13% of total footprint** once paused REC purchases stopped masking datacenter electricity — the DC power signal becoming visible in corporate accounts. Scope 3 ≈ 97% of footprint; jump driven by DC construction embodied carbon + the REC pause.
- **"2030 carbon-negative at risk" = aggregator editorializing** — MSFT formally maintains the goal while conceding solutions "not scaling fast enough"; a sub-target (24/7 hourly matching) reportedly weighed for shelving. Carry as REPORTED interpretation, not fact. Tom's Hardware attribution unverified (primary = MSFT report + Bloomberg).
- **Rule #14 note:** segment = power-and-cooling color; direction (sustainability strain) ≠ TC-3's blocked-projects direction — logged here, no cluster promotion (auditable skip).

### 3. Colibrì — CONFIRMED-FRESH as a project; REFUTED as a demand signal (framing catch)
- Real: JustVugg/colibri (T1 repo; Tom's Hardware + GIGAZINE Jul-10) — ~2,400-line pure-C engine running **GLM-5.2 744B MoE** on ~25GB RAM + NVMe.
- **"1.5TB model" = notional fp16 size (744B×2B ≈ 1.49TB, computed); the actual artifact is a ~370GB int4 file streamed from SSD** (744B×0.5B = 372GB, computed) with ~10-20GB resident — weights-on-disk, not in-RAM.
- **Performance: 0.05-0.1 tok/s creator baseline; ~1 tok/s best community case** — unusable for production. **Does NOT feed L28 Jevons/demand-destruction in either direction**; capability curiosity only. Guard: do not let "frontier AI runs on a laptop" pass through verbatim.

**Cost-yield:** 2 Opus fires ≈ 45k tokens actual (25.2+19.8); both HIGH — 3 framing corrections that would have propagated ("through"→"beyond 2030"; 1.5TB→370GB-on-SSD-unusable; MSFT at-risk editorializing) + 1 recycle-trap cleared.

**Position implication: HOLD all three — no size change — the Kwak datum is structural-branch supportive for SKHY (H3-within-bull nudged 20→25, my model; bands unchanged, no tier change); Monday adjudicators unchanged (SKHY regular tape, TSMC June monthly).** 🟡

**Position implication: NO ACTION pending verification — if the SKH CEO claim confirms fresh + on-record, it cascades to SKHY thesis (structural-branch supportive institutional signal) + TC-1 in a follow-up commit; nothing else in the brief touches a falsifier.** 🟡
