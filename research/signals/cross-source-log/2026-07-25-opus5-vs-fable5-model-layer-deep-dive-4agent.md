# 2026-07-25 — Claude Opus 5 vs Fable 5: model-layer deep dive (4-agent, user-directed "don't assume, verify")

**Workflow:** MACRO-FIRST RESEARCH (#9) + Critical Rule #16 verification. User directive verbatim: *"run a deep dive into Opus 5 vs fable 5. dont assume, verify"*. 4 Opus-tier agents fired in parallel (specs/benchmarks; pricing economics; strategic/market reaction; adversarial compute-demand chain). ~436k+ subagent tokens, 158+ web tool-uses across the three returned at write time.

**Disclosure (standing, per 2026-07-02 precedent):** the parent model is Anthropic-built and holds **NO inside knowledge** of any item here. Every finding is public-source, web-verified, and tiered like any other claim. Where a source is a company self-claim it is labelled as such.

**Local primary cross-check:** the bundled `claude-api` skill reference (Anthropic's own model/pricing table, loaded this session) independently corroborates the pricing and capability rows below — used as a T1-equivalent second source against the agents' web fetches.

---

## 1. HEADLINE CORRECTION — there was no price cut

The aggregator framing (and my own 2026-07-24 restatement of it) implied Anthropic *cut* prices. **It did not.**

Per Anthropic's official pricing docs (platform.claude.com/docs/en/docs/about-claude/pricing, direct-fetched 2026-07-25, **T1**), the Opus-tier price point of **$5 input / $25 output per Mtok has been static since Opus 4.5 (Nov 2025)** — unchanged across Opus 4.5 → 4.6 → 4.7 → 4.8 → 5. Independently confirmed by tech-ish.com 2026-07-24 (**T2**): *"exactly what the model it replaces cost."*

**"Half the price of Fable 5" is a sibling-model comparison at a fixed price point, not a price reduction against history.** Capability rose; the number on the page did not move.

### Verified price table (T1, Anthropic docs 2026-07-25)

| Model | Input $/Mtok | Output $/Mtok | Cache read | Batch (in/out) | Notes |
|---|---|---|---|---|---|
| **Fable 5** | $10 | $50 | $1.00 | $5 / $25 | Public safety-gated GA flagship |
| **Mythos 5** | $10 | $50 | $1.00 | $5 / $25 | Same generation, restricted availability |
| **Opus 5** | $5 | $25 | $0.50 | $2.50 / $12.50 | Static price point since Nov 2025 |
| Opus 4.8 / 4.7 / 4.6 / 4.5 | $5 | $25 | $0.50 | $2.50 / $12.50 | Identical row |
| Sonnet 5 (intro → 2026-08-31) | $2 | $10 | $0.20 | $1 / $5 | Reverts to $3/$15 from Sep-1 |
| Haiku 4.5 | $1 | $5 | $0.10 | $0.50 / $2.50 | |

**Two structural differentiators competitors do not match (T1):** batch is a flat 50% off *both* directions, and there is **NO long-context surcharge** — a 900k-token request bills at the same per-token rate as a 9k one. Google's Gemini 3.1 Pro doubles above 200k ($2→$4 in / $12→$18 out, T1 ai.google.dev); OpenAI's GPT-5.6 Sol steps to $10/$45 above 272k (T2 aggregators; OpenAI's own page returned 403).

---

## 2. THE CONTRADICTION BETWEEN MY OWN AGENTS — and its resolution

Two agents returned findings that appear to conflict. Surfacing rather than reconciling silently (Critical Rule #18 / B46):

| Agent | Finding | Source |
|---|---|---|
| Compute-chain | Opus 5 hits benchmark performance using **~1/7th the reasoning tokens and under half the latency of Opus 4.8** | MarkTechPost 2026-07-24 (**T2**) |
| Strategic | Artificial Analysis + Vals both show a **cost INCREASE vs Opus 4.8 at higher effort settings**; HN commenters flagged "an insane increase for vals" | HN thread 49038571 + The Register 2026-07-25 (**T2**, direct fetch) |

**Resolution (my model, P~75%, mechanism-grounded):** both are true at different operating points, and the reconciling mechanism is documented in Anthropic's own API reference — **on Opus 5 thinking is ON BY DEFAULT**, whereas on Opus 4.8/4.7 omitting the `thinking` parameter meant no thinking at all. The migration guide flags this as a breaking change precisely because `max_tokens` caps thinking + response text together.

So: **at matched capability targets Opus 5 is far more token-efficient; at default and high-effort deployment settings it consumes MORE tokens than the model it replaces, because it now reasons where its predecessor did not.** Benchmark efficiency ≠ deployed cost.

**This is the single most investment-relevant fact in the whole pass**, because it means the naive "cheaper model → fewer tokens → less memory demand" bear chain and the naive "cheaper model → more volume" bull chain are BOTH reasoning from the wrong number.

### The number that settles it: weighted cost-per-task

Artificial Analysis weighted cost-per-task comparison (via The Register 2026-07-25, **T2** direct fetch):

| Model | Cost per task | vs Fable 5 |
|---|---|---|
| Kimi K3 (open-weight) | $0.95 | −65% |
| **Opus 5** | **$2.03** | **−26%** |
| **Fable 5** | **$2.75** | baseline |

**Opus 5 is ~26% cheaper per unit of work than Fable 5 — not 50%** (derived from the two cited figures). The gap between the 50% sticker claim and the 26% realised saving IS the extra thinking.

---

## 3. HYPOTHESIS BOARD — priors → posteriors

**Self-correction on my own hypothesis set:** I specified H1 and H3 as competing. They are not mutually exclusive — H1 is an *economics* claim (why the margin works) and H3 is a *product-architecture* claim (why the tier exists). Both can be true simultaneously, and the system card shows both are. Only H2 was ever a genuine rival. Logging the mis-specification rather than silently rescoring.

| # | Hypothesis | Prior | **Posterior** | Evidence that moved it |
|---|---|---|---|---|
| **H1** | **Cost breakthrough** — genuinely cheaper to serve, margin-neutral or accretive | P~40% | **P~70%** | SemiAnalysis models Anthropic inference gross margin **38% → >70%** in ~1yr, explicitly attributed to Trainium+Nvidia software efficiency, Hopper→Blackwell transition, and premium-tier mix — **explicitly NOT** compression or subsidy (T2, direct fetch). Flat sticker price across 4 generations corroborates. Anthropic's own framing is task-level cost-efficiency: on OSWorld 2.0 Opus 5 *"surpass[es] Fable 5's best result at just over a third of the cost"* (T1 blog). |
| **H2** | **Defensive land-grab / margin sacrifice** vs open-weight | P~40% | **P~10%** | Falsified twice: margins expanding not compressing; price never moved. Anthropic's own announcement contains **zero** competitor mentions (direct fetch). TechCrunch's piece likewise carries no pricing-strategy framing. |
| **H3** | **Tier restructuring** — Fable 5 remains the capability ceiling, Opus 5 is the volume workhorse | P~20% | **P~90% — effectively CONFIRMED** | Anthropic's own system card states it outright (**T1 verbatim**): *"Claude Opus 5 is **not more capable overall** than our most capable general-access model, Claude Fable 5."* Corroborated by Opus 5 **losing** to Fable 5 on four benchmarks (§3a). |

**Falsifier for H1 (pre-registered):** if Anthropic's next Opus-tier release moves the $5/$25 price point DOWN while margin commentary turns negative, H1 is wrong and H2 was right all along. Watch the next Opus print.

---

## 3a. BENCHMARKS — from the primary source, not the marketing copy

Agent 4 downloaded and full-text-searched the **193-page Claude Opus 5 System Card** (www-cdn.anthropic.com, 2026-07-24, **T1 primary**). Table 8.1.A, standard config (adaptive thinking, max effort, 5-trial average):

| Benchmark | Opus 5 | Opus 4.8 | **Fable 5** | Winner |
|---|---|---|---|---|
| SWE-bench Pro | 79.2 | 69.2 | **80.0** | **Fable 5** |
| DeepSWE v1.1 | 68.8 | 59.0 | **69.7** | **Fable 5** |
| FrontierCode 1.1 | 53.4 | 46.5 | **53.5** | **Fable 5** (by 0.1 — tied) |
| Humanity's Last Exam (no tools) | 56.3 | 49.8 | **56.5** | **Fable 5** (marginal) |
| SWE-bench Multilingual | **89.5** | 84.4 | 86.6 | Opus 5 |
| SWE-bench Multimodal | **59.4** | 38.4 | 54.1 | Opus 5 |
| FrontierBench v0.1 | **43.3** | 18.7 | 33.7 | Opus 5 (+9.6) |
| BrowseComp | **90.8** | 84.3 | 87.4 | Opus 5 |
| HLE (with tools) | **64.7** | 57.9 | 63.9 | Opus 5 |
| OSWorld 2.0 (computer use) | **70.6** | 55.7 | 66.1 | Opus 5 ("state of the art") |
| GDPval-AA v2 (Elo) | **1861** | 1593 | 1747 | Opus 5 |
| AA-Briefcase (Elo) | **1720** | 1346 | 1574 | Opus 5 |
| AutomationBench | **26.0** | 17.0 | 17.4 | Opus 5 |

### 3b. USER-SUPPLIED PRIMARY ARTIFACT — Anthropic's official benchmark chart (2026-07-25)

User supplied Anthropic's own published Opus 5 comparison chart. It **independently corroborates the agent's system-card extraction on 8 of 10 overlapping rows exactly** (GDPval-AA 1861/1747/1593/1736; ARC-AGI-3 30.2/—/1.5/7.8; BrowseComp 90.8/87.4/84.3/90.4; HLE 56.3/56.5/49.8 no-tools and 64.7/63.9/57.9 with-tools; OSWorld 70.6/66.1/55.7/62.6; DeepSWE 68.8/69.7/59.0/72.7; FrontierCode 53.4/53.5/46.5/47.5; AutomationBench 26.0/17.4/17.0/18.1). **Cross-source verification of the primary extraction: PASSED.**

**Three rows the agent did not extract, from the chart:**

| Benchmark | Opus 5 | Fable 5 | Opus 4.8 | GPT-5.6 Sol | Winner |
|---|---|---|---|---|---|
| **Legal Agent Benchmark (held-out)** | 11.7% | **13.3%** | 10.4% | 2.5% | **Fable 5 — a FIFTH loss** |
| HealthBench Professional | 59.8% | **66.0% (labelled Mythos 5)** | 57.4% | 60.5% | Mythos 5 |
| BioMysteryBench (hard / human-solved) | **49.4% / 90.1%** | 46.5% / 89.0% (Mythos) | 42.4% / 88.5% | — | Opus 5 |

**Correction to the count: Opus 5 loses to Fable 5 on FIVE benchmarks, not four** — SWE-bench Pro, DeepSWE, FrontierCode, HLE-no-tools, and Legal. The chart also **visually confirms** the agent's footnote catch that the HealthBench and BioMysteryBench comparison columns are labelled **Mythos 5, not Fable 5** — Anthropic swaps the comparator by domain.

**Two minor discrepancies between the chart and the system-card table** (both in FrontierBench comparison columns, not Opus 5's own score): chart shows Opus 4.8 at 21.1% where the card gave 18.7%, and GPT-5.6 Sol at 34.4% where the card gave 37.5% (annotated "Codex"). Most likely different harness/effort configurations. **Opus 5's own 43.3% is identical in both** — the headline is unaffected, but it is a reminder that Anthropic's marketing chart and system card are not the same measurement.

**Sub-observation worth logging:** absolute scores on the Legal Agent Benchmark are low across every model (11.7 / 13.3 / 10.4 / 2.5). Agentic legal work is not close to solved by any frontier model — relevant to any future professional-services-automation thesis, not to the current book.

---

**Opus 5 loses to Fable 5 on five of fourteen head-to-head benchmarks** (four in the system card table + Legal from the official chart). The "beats Fable 5" headline is not uniformly true, and Anthropic's own system card does not claim it is.

**The "within 0.5%" claim, scoped precisely (T1 raw HTML):** *"On **CursorBench 3.2**, at max effort, the model performs within 0.5% of Fable 5's peak score, but at half the cost per task."* **CursorBench does not appear anywhere in the 193-page system card** — it exists only in marketing copy, so its harness, trial count and effort levels are undisclosed. Treat the 0.5% figure as a single-benchmark marketing claim, not an aggregate intelligence statement.

**Notable absence:** GPQA, AIME and MMMU appear **nowhere** in the system card (full-text confirmed). Anthropic has replaced the classic academic suite with its own benchmarks (FrontierBench, FrontierCode, GDPval-AA, ARC-AGI 1-3, OSWorld 2.0, ArxivMath, BenchCAD). This is a **benchmark-comparability degradation** worth tracking: cross-lab comparison is getting harder by construction.

**Other primary-source results:** IMO 2026 **42/42, gold medal** (cutoff 29/42), no tools, judged by a 3-model panel plus human experts. ArxivMath 90.8% no-tools vs GPT-5.6 Sol 86.73% and Gemini 3.1 Pro 65.99%.

**No distillation lineage.** Full-text search returns **zero** parameter counts, FLOPs, or MoE disclosure — consistent with standing Anthropic practice. The system card frames Opus 5 as *"an upgrade to Claude Opus 4.8,"* its own prior generation — **not** a distilled Fable 5. Directly relevant to §9: **Fable 5 ships a classifier that blocks third parties from distilling its outputs** — an anti-distillation defence, which is a different thing entirely and a plausible source of confusion in the public dispute.

---

## 4. "PRICE WAR" IS PRESS-GENERATED — the timeline that made it plausible

**No lab said it about itself.** Verified: Anthropic's announcement (direct fetch) mentions no competitor. But the sequence is suggestive — four repricings/launches in 16 days (**T1/T2 triangulated across 4+ sources**):

| Date | Model | $/Mtok in-out | Type |
|---|---|---|---|
| 2026-07-08 | Grok 4.5 (xAI) | $2 / $6 | closed |
| ~2026-07-08/15 | GPT-5.6 Sol (OpenAI) | $5 / $30 | closed |
| **2026-07-16/17** | **Kimi K3 (Moonshot), WAIC Shanghai** | **$3 / $15** | **open-weight, 2.8T params, 1M ctx** |
| 2026-07-24 | **Opus 5 (Anthropic)** | $5 / $25 — *unchanged* | closed |

Altman on X 2026-07-15: OpenAI *could* go to a quarter of Anthropic's price (**T2**). Google's Gemini 3.5 Pro remained delayed through the window — **Google did not competitively respond**. No Mistral response found.

**Opus 5 sits almost exactly on GPT-5.6 Sol ($5/$25 vs $5/$30).** The two current value-flagships are priced within a rounding error.

**Developer reception is genuinely mixed — NOT PR echo** (a real datapoint against fast migration): Dan Shipper (Every) — *"a hard model to love… It argued with instructions, stopped before the work was finished"*; Lenny's Newsletter — *"brilliant but annoying,"* flagging verbosity. Both improved after deleting legacy prompt scaffolding. Distribution was immediate and measurable: live on OpenRouter same day, in GitHub Copilot for Pro+/Max/Business/Enterprise same day, default model on Claude Max.

---

## 5. NAMING RESOLVED — Fable 5 and Mythos 5 are twins, not a garble

Triangulated (The Register direct fetch + leaked system-prompt repo + others, **T2 N≥3**): **Fable 5 and Mythos 5 are the same training run.** Fable 5 is the public, safety-gated GA release; Mythos 5 is the same generation *without* the extra dual-use restrictions, available only to approved organisations. Identical pricing.

**This explains the benchmark asymmetry:** Opus 5 is compared to **Fable 5 on general capability** but to **Mythos 5 on cybersecurity/exploitation** — because Mythos is the un-gated sibling. The 2026-07-24 ingest logged this as a naming nuance; it is now resolved as a deliberate two-SKU safety architecture.

Confirmed at primary source: Mythos 5 *"shares the same underlying model/weights as Fable 5, with cyber/bio safeguards lifted in some areas"* (T1 anthropic.com/news/claude-fable-5-mythos-5). Anthropic's own family hierarchy: **Mythos → Fable → Opus → Sonnet → Haiku.**

### 5a. THE TRUST-TAX THREAD RESOLVES — Anthropic engineered around its own retention requirement

This is the finding that closes a live harness hypothesis. `meta/private-tracker.md` carries the **enterprise-trust-tax at H2 P~45%**, originating from the Mythos-class 30-day retention requirement that **overrode existing ZDR agreements** and triggered Microsoft pulling Fable 5 from internal Copilot use in June 2026.

**Opus 5 ships without that requirement.** Verbatim from the launch blog (**T1**): *"Consistent with prior Opus models, Opus 5 does not have data retention requirements for general access."* Fable 5 and Mythos 5 retain the 30-day Mythos-class policy.

**Read (my model, P~70%):** this does not falsify the trust tax — it **confirms it was commercially material enough to engineer around.** Anthropic shipped a near-frontier model at half the price *with the retention blocker removed*, which is precisely the product you build when the retention policy is costing you enterprise seats. The trust tax is real; Anthropic has now routed around it rather than absorbing it.

**Consequence for the pre-registered threshold:** the private-tracker set promotion-to-dominant at "a third named enterprise restriction." That threshold is now **less likely to be reached on the Fable line specifically**, because the affected demand can migrate to Opus 5 instead of leaving Anthropic. **H2 trust-tax: P~45% → P~30% (my model)** — the mechanism is confirmed but its revenue consequence is now mitigated by a product route. Re-eval gate: whether enterprise accounts actually migrate Fable→Opus 5 or leave entirely.

### 5b. Spec deltas that matter commercially

| Spec | Opus 5 | Fable 5 | Note |
|---|---|---|---|
| Context / max output | 1M / 128k | 1M / 128k | Identical (300k output via Batch beta on Opus 5) |
| **Knowledge cutoff** | **May 2026** | **Jan 2026** | **The cheaper tier is 4 months FRESHER** |
| Adaptive thinking | On by default; can be disabled at effort ≤high | **Always on, cannot be disabled** | Root cause of the §2 cost contradiction |
| Data retention (general access) | **None** | 30-day Mythos-class | §5a |
| Prompt-cache minimum | 512 tokens | 1,024 | Halved — more prompts become cacheable |
| Fast mode | Yes (~2.5×, 2× price, Claude API/Code only) | No | Not on Bedrock/Vertex/Foundry |
| Anthropic's own latency tier | "Moderate" | "Slower" | Qualitative only; no tok/s disclosed |

---

## 6. THE DEMAND CHAIN — what is established vs what is assumption

The adversarial pass was tasked to hunt disconfirmation as hard as confirmation. Its verdict, restated honestly:

| Link | Status |
|---|---|
| Opus 5 released 2026-07-24, unchanged Opus pricing, more token-efficient than 4.8 at matched capability | **ESTABLISHED** (T1 Anthropic + T2 trade press) |
| Hyperscalers did NOT cut capex after DeepSeek Jan-2025; capex rose ~77% over the following 18mo (~$410B 2025 → ~$700-725B 2026 guided, Big-4) | **ESTABLISHED** (T2 multi-source) |
| **Inference has crossed over training** as the dominant compute workload (~60-70% of AI compute, from ~33% in 2023) | **ESTABLISHED** — Micron Q3 FY2026 earnings call, 2026-06-24: *"Inferencing workloads have crossed over training workloads"* (**T1 quote**) |
| Decode is memory-bandwidth-bound; KV-cache can surpass model weights as dominant memory consumer at long context; HBM-per-accelerator rising generationally (H100 80GB → B200 180GB → B300 288GB) | **ESTABLISHED** (technical/hardware fact) |
| Quantization, MoE sparsity, speculative decoding, KV-cache quantization, distillation genuinely CUT memory per token | **ESTABLISHED** (technical fact — the counter-mechanism is real, not hypothetical) |
| Memory contract prices + HBM TAM still rising through Q3 2026 after 18 months of efficiency gains | **ESTABLISHED** (TrendForce / Micron / Samsung / SK Hynix, T1/T2) |
| **Net effect of cheaper+more-efficient models on AGGREGATE memory dollar demand** | **ASSUMPTION — GENUINELY CONTESTED.** Volume has won empirically twice (Jan-2025, Jul-2026), but that is N=2, not a law. |
| Whether Opus 5 *specifically* moves inference volume or memory demand | **NO DATA EXISTS** — one day old. Absent, not manufactured. |

**The harness's own U8/HU8b already prices this correctly and should not be revised upward on this pass:** the telecom-equipment analog (Ericsson revenue flat 2000-2024 despite 1,500-2,000× traffic growth; Cisco flat 6 years despite 5-6× traffic) sits at **45% weight** in `sector/where-we-are.md` — the largest single hypothesis weight there, not a dismissed tail. The **DDR5-over-HBM per-wafer-profitability crossover (Q1 2026)** remains the cleanest empirical crack in the bull case found anywhere, internal or external, in this pass.

### Current memory state (T1/T2, dated)

| Metric | Figure | Source |
|---|---|---|
| Q3-2026 DRAM contract | +13-18% QoQ (moderating) | TrendForce 2026-07-03 |
| Q3-2026 NAND contract | +10-15% QoQ (moderating) | TrendForce |
| ADATA channel check Q3 | DRAM +20-30% / NAND +35-40% | TrendForce 2026-07-08 (spot/channel, not contract) |
| HBM share of DRAM wafer starts | 18% (2025) → 22% (2026) → ~30% (2027) | TrendForce |
| Memory share of hyperscaler capex | ~8% (2023-24) → ~30% (2026) → 35-48% (2027, estimate range) | SemiAnalysis/CLSA |
| SK Hynix + Micron 2026 HBM | **Fully sold out** | Tom's Hardware |
| Samsung memory chief (Kim Jaejune, 2026-04-30) | Shortages through ≥2027, **"structural not cyclical"** | earnings call |
| Micron Q3 FY26 DRAM revenue | $31.3B record, 76% of total, +343% YoY, +67% QoQ; HBM TAM to cross **$100B in CY2027**, pulled forward from CY2028 | Futurum |

---

## 7. THE JUL-16/17 ROUT — mechanism found, and it inverts the bear read

The harness logged the Jul-16/17 systemic rout (Murata −23% / SUMCO −26% vs Jul-3) and adjudicated it **SYSTEMIC with zero falsifiers fired** (Principle #41, `2026-07-23-w11-wake-audit-3-17day-catchup.md`). This pass supplies the missing mechanism **and the resolution**:

- **2026-07-18 reaction (T2, TFTC):** Taiwan >−6%, Japan ~−4%, Nasdaq ~−1.5% on the Kimi K3 capex-doubt narrative — *"if capable AI is becoming cheap or free, the hundreds of billions spent building it may not pay back."*
- **Reversal within ~24-48h (T2, Yahoo Finance):** memory names rebounded **>10%**; Morgan Stanley, JPMorgan and UBS all recommended buying the dip.
- **BofA's stated counter-mechanism — the load-bearing insight:** *"every open-source model download means customers must deploy the model themselves, generating fresh demand for HBM, DRAM, NAND."*

**Open-weight proliferation is memory-BULLISH via self-deployment, not bearish via capex-doubt.** That mechanism was absent from the harness's Jul-17 framing and materially strengthens the HOLD adjudication made on 2026-07-23.

**L28 (Jevons) — N=4 CANDIDATE:** this is a fourth full cycle of the "efficiency reduces demand" read losing (N=1 DeepSeek-V1 Jan-2025, N=2 DeepSeek-V4/TurboQuant Apr-2026, N=3 enterprise rate-limiting Jun-2026, **N=4 Kimi K3 Jul-2026**). Flagged CANDIDATE, not promoted — the Jul-2026 instance resolved in 48h and one cycle's price action is not the same class of evidence as the multi-quarter capex confirmations behind N=1-3. Promotion gate: Q3 memory contract prints + the Jul-29/30 capex guides.

**Hard Jevons datapoint from the pricing pass (T1):** Google processed **3.2 quadrillion tokens/month as of May 2026, versus 480 trillion in 2025 — ~7× YoY** (Pichai, Google I/O keynote 2026-05-20, blog.google). Microsoft disclosed >250 Azure AI Foundry customers each on track to exceed 1 trillion tokens in FY26.

---

## 8. THE FUNDING-NODE SIGNAL — capex raises now read BEARISH

**Alphabet 2026-07-22 (T1, verified exactly):** raised FY26 capex to **$195-205B from $180-190B**, CFO Ashkenazi citing *"acceleration in the delivery of capacity to meet growing demand."* Revenue +24% YoY to $119.8B, Cloud +82% YoY — a beat. **Stock fell ~3.65-5% after hours.** The market punished the capex RAISE itself, not a miss.

**Microsoft guided FQ4 capex >$40B "reflecting elevated memory and component pricing"** — a hyperscaler explicitly attributing capex increase partly to **memory cost inflation**. Direct read-through to the held book's demand layer (nuance: this is about dollar cost, not proof of volume causation).

**Bear case, stated fairly (Rule #18):** Sequoia's David Cahn — 2026 AI infra spend ~$1.5T requires ~$3T revenue to justify; the gap widened from ~$200B three years ago to ~$3T now. Plus ~$662B in signed-but-not-commenced data-centre lease commitments (Moody's) — leverage that compounds if a cheap-model shock lands at a fragile moment.

**Dated adjudicators unchanged:** MSFT + Meta 2026-07-29, AMZN 2026-07-30.

---

## 9. NEW CROSS-DOMAIN THREAD — the open-weight letter was a RESPONSE, not an independent event

The 2026-07-24 ingest logged the 25-company open-weight letter and the Kimi K3 distillation dispute as **separate items. They are sequential.**

1. **Feb 2026:** Anthropic reportedly traced ~3.4M Claude exchanges to Moonshot (origin document not independently pinned).
2. **2026-07-22:** **White House OSTP Director Michael Kratsios publicly accused Moonshot of "large-scale, covert distillation" of Fable 5**, plus alleged illegal Nvidia GB300 access routed via Thailand (**T2, N≥4 convergent: The Hill, CyberScoop, SeekingAlpha**).
3. **2026-07-23:** Independent expert pushback — Braden Hancock via TechCrunch: *"I don't think you get a model this strong and this quickly on the heels of Fable doing strictly distillation."* SCMP: *"Global AI experts push back on US 'distillation' claims."*
4. **2026-07-24:** The 25-company letter opposing premature open-weight restrictions lands — **two days after the accusation.**

**The distillation claim itself remains UNPROVEN in both directions.** But the escalation is real: this moved from lab-vs-lab (Feb) to **state-vs-state with export-control reach** (Jul). **PC-14 (Universal Sovereign-AI Bifurcation) escalation tick — the mechanism now has a US-government actor and a chip-smuggling allegation attached.** TC-10 (N=10) gains a policy-layer entry.

### 9a. The precedent that matters more than the accusation: export control applied to a MODEL

Surfaced by the system-card agent and materially larger than the Moonshot dispute. **The US Commerce Department restricted, then cleared, wider access to Mythos 5 for "trusted partners"** (Bloomberg 2026-06-26; Fortune 2026-06-27, **T2 N=2 independent**). Mythos 5 is invitation-only via **Project Glasswing**, is not available on claude.ai at all, and requires application through Anthropic/AWS/Google Cloud account teams.

**This is a novel export-control-style review applied to an AI model rather than to hardware.** For a harness whose entire supply-chain framework is built on *chip* export controls, this is a category extension: the control surface has moved up the stack from silicon to weights-and-access. **PC-14 gains its strongest single datapoint to date** — sovereign bifurcation is no longer only about who can buy which GPU, but about who is permitted to invoke which model.

**2nd-order (P~40%, my model):** if model-access controls become routine, they raise the strategic value of *domestic* compute and *domestic* model capability in every jurisdiction that fears exclusion — which is directionally supportive of sovereign-AI capex, and therefore of the physical layer. **3rd-order (P~20%, my model):** it also strengthens the case for open-weight as a hedge, which is exactly what the 25-company letter argued two days later. Both legs point the same way for memory/wafer demand; neither is actionable yet.

---

## 10. ANTHROPIC BUSINESS STATE — private-tracker is stale

`meta/private-tracker.md` carries Anthropic at a $30B run rate and pre-2026 valuation. Verified this pass:

| Metric | Verified figure | Tier |
|---|---|---|
| Valuation | **$965B**, confidential IPO filing **2026-06-01** (up from $350B Nov-2025) | T2 N≥3 (Forbes + corroborating) |
| ARR | ~$47B (May 2026), from ~$9B (end-2025); $14B Feb-2026 → $47B mid-May = ~3× in 3 months | T2 estimate (Sacra/getlatka/Willison) — **not a filing** |
| Enterprise LLM share | **Anthropic 40%** (from 24% 2024, 12% 2023) vs **OpenAI 27%** (from 50% 2023) | T2, Menlo Ventures Dec-2025, named methodology, ~500 US decision-makers |
| Inference gross margin | 38% → >70% over ~1yr | T2 SemiAnalysis model — the ONLY credible quantitative lab-margin model verified |
| AWS | up to $25B Amazon investment; **$100B+/10yr AWS commitment; up to 5GW Trainium** | T1 anthropic.com 2026-04-20 |
| Google | **$200B/5yr; up to 1M TPUs; up to 5GW**; Google investing $10-40B | T2 N≥3 |
| Nvidia / Microsoft | NVDA up to $10B + 1GW; MSFT up to $5B + $30B Azure + 1GW | T2, CNBC 2025-11-18 |

**Physical-layer read-through:** ~5GW Trainium + ~5GW Google + 2GW Nvidia/Microsoft of *contracted* capacity for a single lab. This is the leg with genuine memory/wafer reach, and it is contractual rather than sentiment-driven.

---

## 11. HONEST GAPS (not papered over)

- **ASL level:** both Opus 5 and Fable 5 sit at **ASL-3** — the same tier (T1 system card: *"we apply the same ASL-3 protections as for Claude Opus 4.8"*; Opus 5 assessed CB-1, not CB-2). **The 85%-fewer-cyber-interventions claim is operational friction, not an RSP reclassification** — an important scoping correction to the 2026-07-24 ingest. Corroborating from a different metric on FrontierBench: Opus 5's classifiers flagged **5%** of API calls vs Fable 5's **42%** (≈88% relative reduction on that one eval — do not conflate with the 85% headline). What actually changed: Opus 5 permits **source-code** vulnerability discovery at all access levels but still blocks **compiled-binary** scanning.
- Fable 5's own ASL-3 designation is **secondary-sourced** — the agent could not pull the Fable 5 system card PDF directly this session.
- Microsoft Foundry model-ID string for Opus 5: **UNVERIFIED** — availability confirmed, exact string not located.
- No Opus-5-specific coverage located from The Verge, Ars Technica, The Information, or Stratechery despite targeted search.
- No hard OpenRouter usage-share shift data (before/after).
- No direct Dario/Daniela Amodei statement on Opus 5 pricing in the Jul-20/25 window.
- No verified equity-market reaction tied *specifically* to Opus 5.
- Epoch AI / a16z / Stanford HAI price-decline rates (10-50×/yr capability-adjusted) were **search-summary sourced, not direct-fetch confirmed** — do not use in a thesis without re-verification.
- The "closed labs ~80% margin vs open-serving 40-45%" figure circulating in search summaries is **UNVERIFIED** — the one candidate source, on direct fetch, covered downstream AI-*product* margins (a different layer). Do not propagate.

---

## 12. POSITION IMPLICATIONS

**MURATA (held, 336sh) — Position implication: 🟡 HOLD — no size change — no direct model-layer exposure; the read-through is 2nd-order via AI-server component demand, and the Jul-16/17 capex-doubt shock that hit the name now has a documented counter-mechanism (BofA: open-weight self-deployment generates fresh HBM/DRAM/NAND demand) plus a >10% memory-cohort rebound within 48h. Falsifier unchanged and unfired. Q1 FY3/27 print 2026-07-31 remains the adjudicator.**

**SUMCO (held, 626sh) — Position implication: 🟡 HOLD — no size change — wafer demand sits downstream of memory-bit demand, and every verified memory datapoint this pass (HBM sold out 2026, wafer-start share 18%→22%→~30%, Micron HBM TAM pulled forward to CY2027, Samsung "structural not cyclical") points the same direction. The genuine counter-risk is unchanged and unresolved: U8/HU8b at 45%, and the DDR5-over-HBM per-wafer-profitability crossover. LTA-lag adjudicator remains the Aug-6 print.**

**Book-level: 🟡 NO ACTION — the deep dive strengthens the demand-durability leg but produces zero falsifier events and zero sizing triggers. Critical Rule #8 binds.**

---

## 13. CASCADE (executed same commit)

- `meta/private-tracker.md` — Anthropic section: Opus 5 launch, valuation/IPO update, enterprise share, margin model, compute commitments, Kratsios thread.
- `companies/MURATA/thesis.md` + `companies/SUMCO/thesis.md` — back-reference + Position implication (Critical Rule #10 symmetric cascade).
- `meta/subagent-cost-yield-ledger.md` — 4-agent fire entry.
- **Deferred:** `sector/where-we-are.md` U8/HU8b weight — NOT revised this pass. The 45% weight survives contact with this evidence; revising it on a single news cycle would be exactly the recency error B45/B13 warn against. Re-eval gate: Q3 memory contract prints + Jul-29/30 capex guides.
- **Deferred:** L28 N=4 promotion — CANDIDATE only, gate as above.
