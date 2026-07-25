# 2026-07-25 — Korea–US $950B memory supply deals + CXMT structural-threat assessment (2-agent)

**Workflow:** INGEST (Workflow #1) + Critical Rule #16 verification, on the 2026-07-25 morning-edition aggregator brief (77 sources, T3). Korean- and Chinese-language searches fired **in parallel** with English per Principle #36, not as fallback — and that is what produced the result: the English aggregator was ~24h stale on the load-bearing item.

**Dedup note:** the user also re-shared the **2026-07-24 evening edition, which was fully ingested yesterday** (`2026-07-25-evening-brief-jul24-ingest-2leg.md`, commit f48e95b). No re-spend. Only the morning edition was new.

**Macro anchor (first-principles read as of 2026-07-25):** the memory/wafer complex is the physical layer the model-layer commoditisation of the last fortnight has NOT invaded (per `2026-07-25-opus5-vs-fable5-model-layer-deep-dive-4agent.md`). The two items below are the first genuine tests of that statement from the supply side — one confirming, one probing.

---

## ITEM 1 — Korea–US memory deals: 🟢 **ANNOUNCED, not "set to announce"**

The brief (via Tom's Hardware) framed this as *"expected to announce."* **That framing was already stale.** Korean primary press carried confirmed figures the same morning.

**The visit is real and dated:** President **Lee Jae-myung** began a 7-night/11-day trip on **2026-07-24**, with San Francisco AI Summit events 2026-07-24/25 (MBC 실리콘밸리 순방; 파이낸셜뉴스 2026-07-24). Attending: Samsung chairman Lee Jae-yong, SK chairman Chey Tae-won, Hyundai's Chung Euisun, Naver's Lee Hae-jin — alongside Jensen Huang, Sam Altman, Dario Amodei and Hock Tan.

| Deal | Value | Term / structure | Source (T1-adjacent Korean primary) |
|---|---|---|---|
| **TOTAL long-term memory supply agreements** | **~$950B (1,375조원)** | multi-year | 전자신문/ETNews; 머니투데이, 2026-07-25 |
| **Samsung – Broadcom** | **$200B (293조원)** | **5-year MOU** — advanced memory supply + foundry capacity for AI chip production | 뉴시스; 디일렉/THE ELEC, 2026-07-25 |
| **SK Group – Nvidia-led consortium** | **$750B** | of which **~$500B is the SK Hynix–Nvidia leg**; further ~$250B layer reported involving Microsoft/Anthropic | 블로터; 뉴시스, 2026-07-25 |

**Cascade-quality note:** presidential policy chief **Kim Yong-beom pre-confirmed the scale** ("very large sums," possibly exceeding the prior $880B framing) *before* the summit (Bloomberg via Korea Herald; 한국일보, 2026-07-24), and company-level figures firmed within ~24h. That is a clean **government-briefing → company-confirmation cascade**, not press speculation.

### N-th order trace — Korea–US memory deals

- **1st order (P>80%):** Samsung and SK Hynix lock multi-year, multi-hundred-billion demand from Broadcom and Nvidia. Direct, now-confirmed.
- **2nd order (P~65%, my model):** demand visibility extends **past the 2027 "normalisation" date** some sell-side (TrendForce among them) had pencilled in. The supercycle's duration risk — the harness's central worry, not its existence — is materially reduced. **This is the leg that matters for a 6-24 month holding horizon.**
- **3rd order (P~50%, my model):** locked memory demand pulls forward **wafer-capacity commitments**, because bits cannot ship without substrate. **SUMCO supplies both Samsung and SK Hynix** — this is the direct held-name link, and it is a volume-and-visibility effect rather than a price effect.
- **4th order (P~25%, my model):** if this much demand is contracted at the memory layer, the binding constraint migrates *upstream* — to wafer capacity, advanced packaging and power. That is the harness's standing bottleneck-forecast question and this is a datapoint for it, not an answer.

**Ties to macro:** consistent with the first-principles read — the physical layer is where contracted, multi-year, non-commoditising value is accruing while the model layer prices compress.

**Signal-density check (Critical Rule #14):** segment = **memory-and-storage**. Same-segment same-direction signals inside 90 days: TrendForce Q3 reaffirmations (+13-18% DRAM / +10-15% NAND), SK Hynix + Micron 2026 HBM sold out, Samsung "structural not cyclical" (Kim Jaejune 2026-04-30), Micron HBM TAM pulled forward to CY2027, MSFT FQ4 capex citing "elevated memory pricing." **N≥5, same segment, same direction — this clears the promotion bar.** Flagged for a `triangulation.md` entry on next register touch rather than promoted mid-ingest (single-brief discipline, Rule #6).

---

## ITEM 2 — CXMT: 🟡 **real commodity threat, NOT an HBM threat** — and the standing falsifier has NOT fired

The brief's framing was directionally right but oversold on one number.

**Correction to the aggregator (B40.2-class):** **8200 MT/s is an overclock, not CXMT's rated spec.** CXMT officially rates these parts to **8000 MT/s**; 8200 is what Gigabyte's AGESA 1.3.0.1c BIOS unlocks *above* spec across its AM5 600/800-series and Intel 700/800-series boards (Gigabyte official press release; Tom's Hardware; VideoCardz; TechPowerUp, all ~2026-07-24). MSI made a parallel China-market announcement.

### The two-sided assessment (Rule #18 — strongest case both ways)

| Dimension | Threat is REAL | Threat is OVERSOLD |
|---|---|---|
| **Capacity** | ~265-350K wspm by end-2026, closing on Micron's ~385K; targeting 500K wspm / ~17% of global DRAM by 2028 (SemiAnalysis) | Still well behind Samsung ~720K and SK Hynix ~595K (same source) |
| **Share** | Global DRAM share **3% → 8% in one year**; now #4 globally | SemiAnalysis: **bit**-share growth is modest (9%→12% by 2027); most of the ~$50B 2026 revenue jump is **price**, not share |
| **DDR5** | 80% yield achieved 2H2025; matches the DDR5-8000 tier of all three incumbents; HP and Dell reportedly qualifying | **CXMT DDR5 is NOT cheap** — vendors report pricing now *matches* Samsung/SK Hynix/Micron amid the shortage, which guts the "cheap Chinese substitute" thesis entirely |
| **HBM — the decisive column** | HBM3 samples delivered to Huawei; targeting mass production 2026 (Chinese sources: 腾讯新闻, 經濟日報) | **HBM3 8-hi combined yield ~25%**; only **~5K wafers/month (<2% of its own capacity)** on HBM, rising to only ~55K by 2027; targeting **HBM3E, not HBM4**; slipped 1H26→2H26 on yield/materials. **HBM investment was NOT in the IPO prospectus.** |
| **Capital** | $4.3-4.4B STAR Market IPO (subscription 2026-07-16), **212× retail oversubscription**; new Shanghai fab 2-3× the Hefei HQ | Shanghai volume production only 2027; fresh capital is not being pointed at HBM |

**Converging independent verdict:** SemiAnalysis concludes CXMT is **"not a structural threat to the oligopoly"** near-term, precisely because this supercycle is HBM/server-DRAM-driven where CXMT's own exposure is <2% of capacity at ~25% yield. Independent analyst Ray Wang: *"already a very serious player"* (~10% share) but **~4 years behind SK Hynix specifically on HBM.** Seoul Economic Daily converges. **No source found in this pass puts CXMT into HBM contention inside the 2026-2028 window.**

### FALSIFIER CHECK — the standing condition has NOT fired

`sector/where-we-are.md` (2026-06-08 entry) pre-registered: *"if CXMT achieves DDR5-8400 / LPDDR5X-12000+ within 18 months, HYNIX commodity-tier ASP power weakens."*

**NOT FIRED.** Actual: DDR5 **8000 official spec** (8200 overclock ≠ spec), LPDDR5X ceiling **10667**, no 12000+ report located. **Directionally trending toward the threshold** — the trajectory over twelve months is 6800 → 8000 → 8200-oc — but the bar as written is not met. Re-check gate: next quarter, tightened cadence given that pace.

### N-th order trace — CXMT

- **1st order (P>80%):** CXMT gains a Western consumer-platform validation point. Low investment content.
- **2nd order (P~60%, my model):** commodity/consumer DRAM is where Chinese domestic supply substitutes first, eroding incumbent pricing power **at the low end only**.
- **3rd order (P~45%, my model):** that **decouples** commodity DRAM from HBM/server DRAM rather than dragging both down. If incumbents respond by reallocating capacity toward HBM, **total wafer demand holds while consumer ASPs fall** — which is directionally *supportive* of SUMCO, and contradicts the naive first-order "Chinese memory = bearish memory complex" read. **Verified this pass: the 25% HBM yield and <2% capacity allocation are the mechanism that makes this decoupling hold.**
- **4th order (P~20%, my model):** credible CXMT HBM inverts the whole calculus. **That, not the AM5 headline, is the thing to watch** — and every independent source puts it 4-5 years out.

**Self-check:** this cascade was written *before* the agent returned and survived verification unchanged. Logging that as a calibration datapoint, not a victory lap — one instance.

---

## OTHER MORNING-BRIEF ITEMS (logged, no agent spend)

| Item | Verdict | Why no spend |
|---|---|---|
| The Register: Opus 5 *"added benefit of not requiring data retention"* | 🟢 **INDEPENDENT CORROBORATION** of the trust-tax finding committed hours earlier from the system card | Already primary-verified |
| Kimi K3 distillation skepticism (TechCrunch) | ⚪ DEDUP | Same Braden Hancock piece already in yesterday's artifact |
| UK AISI preliminary cyber assessment of Kimi K3 | 🟡 **PC-14 TICK** — a *second* government now running capability review on a Chinese model, following the US Commerce Dept's Mythos 5 review. The model-access control surface is generalising across jurisdictions. | Log-only; register tick deferred |
| Meta Superintelligence struggling / Scale AI 49% at ~$30B (SemiAnalysis) | 🔴 **B40 GARBLE — see §3** | Agent fired; caught a two-piece splice |
| AMD + Cerebras low-latency inference; Prentis AI ($100M, Hoffman/Pincus); OpenAI keypad + desktop voice; Qwen 3.6 35B on RTX 3090; Claude Code prompt −80%; SANA-Video 2.0; MIRROR; OpenForgeRL | ⚪ colour | No held-name reach |

---

## ITEM 3 — Meta Superintelligence: 🔴 **B40 GARBLE (two-piece splice)** — and the capex-doubt thread resolves

**The brief's item is a composite of two different SemiAnalysis pieces:**

| Piece | Date | What it actually says |
|---|---|---|
| *"Meta Superintelligence — Leadership, Compute, Talent, and Data"* | **2025-07-11** | Source of the "**$100B annual cashflow ad machine**" phrasing and the "**49% of Scale AI at ~$30B**" figure |
| *"The Future of Meta Superintelligence: A 1 Year Progress Update"* | **2026-07-09** | The genuinely recent piece — authors are explicitly **"overall bullish on the future of MSL"**, argue *"the slope, not the intercept"* matters, and project Meta will hold **more AI compute than OpenAI and Anthropic combined by end-2026** |

**The aggregator grafted the 2025 piece's language onto the 2026 piece's subject.** The 2026 analysis is **mixed-to-bullish**, not "struggling." **The Scale AI 49% / ~$30B item is stale by ~13 months** — Meta invested $14.3B for a 49% non-voting stake in June 2025; **no new 2026 Scale AI transaction exists.** New B40.1 instance.

**What IS documented (T2, named authors):** Muse Spark lagged DeepSeek V4 Pro and Kimi K2.6 at release and scores 52 on the Artificial Analysis Intelligence Index (5th); Yann LeCun departed Nov-2025; ~600 AI roles cut. **What is NOT supported:** "falling behind foundation labs" as a blanket verdict.

**Aggregator-hygiene ledger:** this is the **fourth** recycled/garbled item from this brief class inside eight days (Colossus-2 figures, Rubin CPX, Amazon-Anthropic Trainium, now Meta/Scale AI). The standing downweight on its Infrastructure and Lab-Watch sections holds and should now extend to **any SemiAnalysis-attributed item**, which this class evidently re-serves without date discipline.

### THE OPEN THREAD RESOLVES — nobody is cutting capex

The Kimi-K3 capex-doubt narrative has been the harness's #1 open thread since 2026-07-17, with MSFT/Meta (Jul-29) and AMZN (Jul-30) pre-registered as adjudicators. The agent was tasked adversarially to find deceleration evidence. **It found none on the spending side.**

| Company | Current FY2026 guide | Given | Direction |
|---|---|---|---|
| **Alphabet** | $195-205B (raised from $180-190B) | **2026-07-22** | ▲ RAISED |
| **Meta** | **$125-145B** (raised from $115-135B) | 2026-04-29 | ▲ RAISED — consensus into Jul-29 is **~$139B, above guide midpoint** |
| **Microsoft** | ~$190B calendar-2026, *"up 61% from 2025"* (Amy Hood) | 2026-04-29 | ▲ ~$35B above prior street consensus |
| **Amazon** | ~$200B — Jassy: *"largest single-year infrastructure bet in corporate history"* | 2026-02 | ▲ |

**Disconfirming evidence, stated fairly (Rule #18) — and why it does not carry:**
- **UBS:** hyperscaler capex +76% in 2026 to $673B, then **+25% (2027) and +6% (2028)**. That is a **growth-rate deceleration off a much larger base, not a spending decline** — arithmetic, not retreat.
- **BIS Annual Economic Report (2026-06-28):** warns of an AI "investment bust" if returns disappoint, likening it to railway and dot-com manias. **A risk warning, not a realised signal.**
- **Investor repositioning (Reuters 2026-07-17):** some managers trimming chip exposure ahead of out-year deceleration — explicitly anticipatory. **No hyperscaler executive is quoted planning to slow spending.**
- **The disconfirmation gets disconfirmed — TSMC, 2026-07-16:** raised 2026 capex to **$60-64B** and raised the full-year revenue growth guide to *"slightly above 40%."* CEO C.C. Wei: ***"The CapEx in the next three years will be even more significantly higher than the past three years."*** This is the freshest hard supply-chain datapoint in the window and it points **opposite** to deceleration.

**Read (my model): the capex-doubt thread is P~15% of producing an actual guide-down at the Jul-29/30 prints**, revised from genuinely uncertain on 2026-07-17. Bayesian basis: four consecutive raises, consensus positioned *above* Meta's guide midpoint, and a supply-chain raise from TSMC post-dating the Kimi K3 shock. **The prints still adjudicate — this lowers the prior, it does not close the thread.** Falsifier stands: any hyperscaler guiding FY26 capex down, or declining to reaffirm, on Jul-29/30.

**Ties to macro:** consistent with the first-principles read — the model layer is compressing on price while the physical layer's contracted spend keeps rising. Both this and the $950B Korea deals point the same way from opposite ends of the chain.

---

## POSITION IMPLICATIONS

**SUMCO (held, 626sh) — Position implication: HOLD — no size change — 🟢** *(tier upgraded from 🟡 on evidence quality, NOT on conviction or sizing)* — the $950B Korea–US supply agreements are the **strongest T1-tier demand-side confirmation the memory-supercycle thesis has received**, and they extend visibility past the 2027 normalisation date that was the thesis's main duration risk. The CXMT counter-signal was tested adversarially and resolves as a **commodity-tier threat that does not reach the HBM segment** where SUMCO's highest-value wafer exposure sits; the pre-registered falsifier explicitly did NOT fire. **No sizing change — the Aug-6 print and the P1 component-level self-prediction remain the gates, and Rule #11 keeps sizing user-gated regardless.**

**MURATA (held, 336sh) — Position implication: HOLD — no size change — 🟡** — no direct read-through; MLCC demand is levered to AI-server build volume rather than memory contracting specifically. The Korea–US deals are supportive at 3rd order (P~40%, my model) via total AI-server build-rate, not at 1st. Jul-31 print remains the adjudicator.

---

## CASCADE (executed same commit)

- `companies/SUMCO/thesis.md` — back-reference + Position implication (Critical Rule #10).
- `companies/MURATA/thesis.md` — back-reference + Position implication.
- `meta/subagent-cost-yield-ledger.md` — 2-agent fire entry.
- **Deferred, not skipped:** `signals/triangulation.md` memory-and-storage cluster promotion (N≥5 clears the bar — next register touch); `sector/where-we-are.md` CXMT-monitor re-check date; PC-14 register tick for the UK AISI datapoint. Deferrals are auditable here per the Rule #14 skip-rule.
