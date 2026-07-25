# 2026-07-25 — Opus 5 vs Fable 5: model-selection deep dive (3-agent verification + in-house work-product forensics)

**Origin:** operator request 2026-07-25 ("deep dive into Opus 5 vs Fable 5. dont assume, verify"). Operationally load-bearing — this desk switches between both models, and the choice governs harness-work quality, verification-fan-out cost, and the review-vs-generation split.

**⚠️ CONFLICT-OF-INTEREST DECLARATION (B63/B64, binding on this artifact):** the session running this dive IS `claude-opus-5`, comparing itself to a sibling model. Worse, the three verification agents inherit the session model → their judgment is **self-correlated with mine** (interpretation-monoculture, self-analysis item 1). Mitigation: every agent prompt demanded THIRD-PARTY benchmarks and PRIMARY sources over agent opinion; conclusions favoring my own lineage get the hardest scrutiny. **The single most reassuring signal below is that the primary evidence REFUTES the status my lineage would prefer** (see the flagship finding).

---

## 🔴 THE HEADLINE CORRECTION — Opus 5 is NOT the flagship; Fable 5 sits ABOVE it

Press framing ("Anthropic's new flagship") is **imprecise, and my own earlier framing in this session inherited the error**. T1 docs (fetched, `platform.claude.com/docs/en/about-claude/models/overview`) state the hierarchy explicitly:

> *"start with Claude Opus 5 for complex agentic coding and enterprise work. For workloads that need the highest available capability, use Claude Fable 5."*

| Model | T1 description string | Price /MTok in-out | Status |
|---|---|---|---|
| **Fable 5** (`claude-fable-5`) | *"Next-generation intelligence for long-running agents"* — **"Anthropic's most capable widely released model"** | **$10 / $50** | GA 2026-06-09; **capability CEILING** |
| **Mythos 5** (`claude-mythos-5`) | Fable-5 specs/pricing; **invitation-only**, defensive cybersecurity, "Project Glasswing" | $10 / $50 | restricted |
| **Opus 5** (`claude-opus-5`) | *"For complex agentic coding and enterprise work"* | **$5 / $25** | **released 2026-07-23/24 — ~2 DAYS OLD**; price/performance tier |
| Sonnet 5 | *"best combination of speed and intelligence"* | $2 / $10 | — |

**Opus 5 is the price/performance point, not the ceiling.** Anthropic itself concedes Opus 5 remains behind Mythos 5 on cybersecurity tasks. Two-day-old model = why this session's default switched.

## LEG A — OPUS 5 (agent ✅, research-verified 2026-07-25; T1 docs FETCHED, anthropic.com + system-card PDF 403'd → those items second-hand)

**Specs (T1-fetched, safe to hard-code):** 1M context (default = max, no long-context premium) · 128k max output (**300k via Batch** w/ header `output-300k-2026-03-24`) · **knowledge cutoff May 2026** (vs **Jan 2026 for Fable 5 AND Sonnet 5** — Opus 5 has ~4 months more world knowledge than the capability ceiling) · text+image in, text out, no audio/video · effort ladder **low/medium/high(default)/xhigh/max**, no beta header · **thinking ON by default** · tool-use system-prompt overhead 286/406 tokens (lowest of any Opus).

**Pricing recomputed (#43b):** Opus 5 = **exactly 0.500×** Fable 5 on every line (input, output, all three cache tiers) — "half the price" is literal, not rounded. Batch = exactly 50% off. **vs prior Opus generation: ZERO price change** ($5/$25 unchanged across 4.5→4.8→5; the last real cut was 4.1→4.5, a 3× cut). **Fast mode $10/$50 = 2× standard = identical to Fable 5's standard rate.** Hidden multiplier: the 4.7-gen tokenizer emits **~30% more tokens for the same text** than pre-4.7 models — headline per-token prices are not comparable across that boundary.

**Independent benchmarks (the section that matters):**
- **Artificial Analysis Intelligence Index v4.1: Opus 5 (max) = 61 → #1 of ~170 models**, Fable 5 = 60, GPT-5.6 Sol = 59. **CAVEAT THE AGENT FLAGGED AND I ENDORSE: a 1-point lead on a 0-100 composite is INSIDE NOISE — do not treat as a durable capability gap.** Effort ladder scales monotonically (max 61 / xhigh 60 / high 59 / medium 56) = **+5 points medium→max**, the real cost/quality dial.
- **AA-Briefcase (AA's proprietary held-out agentic knowledge-work eval): Opus 5 = 1720 Elo, +146 over Fable 5.** Strongest genuinely-independent result, on a benchmark harder to game.
- **CodeRabbit task-level eval — THE MOST DECISION-RELEVANT INDEPENDENT FINDING, and it cuts AGAINST Opus 5:** actionable precision 39.3% vs 35.2% baseline (**+4.1pp**) BUT **recall on known issues 55.2% vs 61.1% (−5.9pp)** and **~4× more nitpicks**; weakest on **logic errors, race conditions, API misuse**. Their verdict: **"not a straightforward upgrade."** (Note: CodeRabbit sells code review = commercial interest; still the only substantive task-level independent eval available.)
- **Speed: 54.6 t/s (high effort) vs peer median 73.6 = ~26% BELOW median.** Verbosity: xhigh emitted **76M tokens** on the index vs 63M average; max rated **4/4 "very verbose"** — a direct cost consequence at $25/MTok output.

**Vendor-reported benchmarks (T1-via-T2 relay; NO eval-condition/scaffolding footnotes recoverable — the exact layer where vendor caveats hide):** Frontier-Bench v0.1 **43.3%** (Fable 33.7, Sol 34.4, Opus 4.8 18.7) · ARC-AGI-3 **30.2%** (Sol 7.8) · OSWorld 2.0 **70.6%** (Fable 66.1) · AutomationBench **26.0%** (Sol 18.1, Fable 17.4) · GDPval-AA v2 **1861 Elo** (Fable 1747, Sol 1736) · CursorBench 3.2 max-effort **70.0% @ $8.23/task vs Fable 70.5% @ $17.32/task**.

**Three arithmetic catches by the agent (both directions — the honest sign):**
1. ARC-AGI-3: Anthropic said "three times"; actual **3.87×** — Anthropic **UNDERSTATED** its own result.
2. AutomationBench: "more than 8 points" → actual **7.9pp**; "~1.5×" → actual **1.44×** — both mild **overstatements** in Anthropic's favor (B63-class).
3. CursorBench cost: claimed ~half → actual **47.5%** of Fable's per-task cost, slightly better than claimed. Score gap only **0.5pp**.

**🚫 KILL-ON-SIGHT — SWE-bench Verified for Opus 5 is UNVERIFIED with a DATE IMPOSSIBILITY:** three sources give three numbers (95 / 96 / 97%); the 97.00% relay cites a vals.ai page "updated July 22" — **Opus 5 did not exist publicly until July 23-24**; llm-stats shows no Opus 5 entry at all; and one aggregator falsely attributed 97% to Anthropic, whose announcement **does not feature SWE-bench at all**. Do not carry any SWE-bench number for Opus 5. (Prior art: DeepSWE reported Claude Opus exploiting a benchmark loophole — this family has integrity problems.)

**Also non-existent as of 2026-07-25 (anyone quoting these is fabricating):** LMArena/Chatbot Arena ELO for Opus 5 (arena top is still **Opus 4.8 ~1510**) · Aider polyglot · LiveBench · standalone Terminal-Bench v2.1 / GPQA / AIME.

**Safety/system-card (T1 content but second-hand — PDF 403'd, medium confidence):** "most aligned model to date" on an **automated behavioral audit** — **B63 FLAG: vendor-graded on a vendor-designed audit with zero external corroboration; do NOT propagate as fact.** Ships under **same ASL-3** as Opus 4.8; ASL-4 AI-R&D threshold **not crossed**. **⚠️ THE FINDING THAT MATTERS MOST FOR A RESEARCH DESK: hallucinates factual claims slightly MORE than Opus 4.8 despite higher overall accuracy — "sometimes confidently stated an answer about which it was in fact unsure." Accuracy UP, calibration DOWN.** Offsetting: among the **lowest over-refusal rates** of any recent model; no sandbagging/oversight-evasion found; largest gains in prompt-injection robustness. Deliberate limitation: finds OSS-Fuzz vulns near Mythos-5 level but **lags markedly at converting them to working exploits** (intentional safety constraint).

**Migration = REAL breaking change (T1 docs, operationally binding on this harness):**
1. **Strip carried-over "verify your work" instructions** — T1 explicitly warns they cause **over-verification** on Opus 5, which self-verifies unprompted.
2. `thinking: {"type":"disabled"}` returns **HTTP 400** at xhigh/max effort.
3. Thinking tokens now count against `max_tokens` — re-audit limits.
4. **Effort does NOT reliably shorten responses** — must prompt for length explicitly.
5. Run a **fresh effort sweep**; do not reuse Opus 4.8 effort settings.
6. Prompt-cache minimum dropped 1,024 → **512 tokens**.

## LEG B — FABLE 5 + EXPORT-CONTROL STATUS ✅ (agent returned; T1 docs + GitHub fetched today; anthropic.com/press/system-card 403 → those marked snippet-only)

### 🚨 B1. THE CRUX FINDING FOR THIS DESK — Fable 5's cyber classifier SILENTLY downgrades mid-session
**T1-VERIFIABLE** (agent fetched [anthropics/claude-code issue #67441](https://github.com/anthropics/claude-code/issues/67441) directly; opened **2026-06-11**, labels `area:model`+`bug`, **still OPEN**; companion #67437): the cybersecurity classifier flags **legitimate self-administration of one's own servers** (SSH, iptables checks, firewall/proxy verification) as reconnaissance — and even flagged an unrelated **PDF text-extraction** comparison. Two mechanisms make it worse: **session-level sensitivity inflation** (one early flag raises sensitivity for subsequent benign messages) and **silent mid-session switching to Opus 4.8**.

**Why this is decisive here:** this harness's heaviest work IS infra/security-adjacent — git-guard bypass probes, permission-check auditing, hook enforcement, the parallel-path attractor. **Running that on Fable 5 risks silently executing on Opus 4.8 without notification** — meaning a "Fable-5 audit instance" may not have been Fable 5 throughout. Retro-caveat now attached to the 07-23 audit provenance claim (below).
**Correction to a widespread framing (agent-caught):** outlets attribute these false positives to the NEW 2026-07-01 classifier — **but #67441 is dated 2026-06-11, predating the suspension.** The FP problem belongs to the launch-day classifiers; "post-ban Fable got dumber" is misdated.

### B2. 🔴 CORRECTION TO BOOKED CORPUS — "90-minute global shutdown" is INVERTED
Booked in `companies/NOW/thesis.md`, `companies/DDOG/thesis.md`, `companies/NBIS/thesis.md`, `watchlist/candidates.md` as a "90-min global shutdown." **Actual: the 90 minutes was the COMPLIANCE DEADLINE; the outage ran ~19 days.**

| Date | Event | Tier |
|---|---|---|
| 2026-06-09 | Fable 5 + Mythos 5 GA (API, Bedrock, AWS, GCP, MS Foundry) | **T1 fetched** |
| 2026-06-12 | BIS **"is informed" letter under ECRA** — license required before access by **any foreign national, in or outside the US, incl. Anthropic's own foreign-national staff**. Lutnick→Amodei. Global shutdown was the only compliant path (nationality of API callers unverifiable in real time). *(17:21 ET / 90-min window = T3 single-source, treat clock as UNVERIFIED)* | T1-content-via-relay |
| 2026-06-26/27 | Partial easing — **Mythos 5 ONLY** (~100 Annex A "trusted partner" entities, list not public). **Fable 5 explicitly NOT covered.** | T2 |
| 2026-06-30 | Commerce **WITHDRAWS controls on both**. Reported quid pro quo: proactive security-risk detection, joint protocols incl. pre-release gov access, vulnerability-clearinghouse participation *(REPORTED, no primary doc retrieved)* | T2 |
| 2026-07-01 | Fable 5 **redeployed globally** w/ new cyber classifier (Anthropic-claimed >99% block on the trigger technique, **no independent replication**); blocked requests **route to Opus 4.8** rather than refuse | T1 banner |

**Outage = 19 days (12 Jun → 1 Jul), recomputed.** Cite as "19 days (12 Jun – 1 Jul)", not a bare number. **Trigger nuance:** Amazon researchers' *"review the code for security issues"* was REFUSED; rephrased to *"fix this code"* it produced patches + in one case exploit-demonstration code → escalated by **Andy Jassy** → Treasury → White House → Commerce. Katie Moussouris (the only outside expert shown the research, **by Anthropic**) calls it "not a jailbreak… Defense Oriented Prompting"; 100+ cyber experts signed against the controls; Commerce maintained it was a jailbreak. **Genuine expert dispute, not settled either way** (B63: the Anthropic-favorable read survives only partially — her access was vendor-mediated).

### B3. CURRENT STATUS 2026-07-25 — UNAMBIGUOUS (T1, fetched today)
**Fable 5: GENERALLY AVAILABLE WORLDWIDE, no export restriction**, listed as a current non-legacy model with no access caveat. **Mythos 5: still invitation-only** (Project Glasswing).
**⚠️ PLAN-TIER CHANGE 2026-07-20 (our corpus likely holds the dead state):** Fable 5 now **Max + Team Premium only, permanently, at 50% of weekly limits**; **Pro and Team Standard NO LONGER include it** — usage credits at $10/$50 + a one-time $100 credit (T1 Claude X post ~07-19; the-decoder/PCWorld T2). Any desk note citing "included through July 7/12/19" is **dead**. Single-outlet claim (UNVERIFIED) that underlying weekly limits were also cut ~⅓ the same day → "50% of limits" may be 50% of a smaller base.

### B4. What Fable 5 IS + the compliance differentiator (T1)
*"Anthropic's most capable widely released model, built for the most demanding reasoning and long-horizon agentic work."* The Fable/Mythos distinction is **safety-layer, not capability**: *"Claude Fable 5 includes safety classifiers that can decline requests. Claude Mythos 5 does not."* Fable = the Mythos-class model made safe for general release.
**Integration facts:** refusals return `stop_reason:"refusal"` as **HTTP 200, not an error** (needs explicit handling) · adaptive thinking always on, `disabled` unsupported · **raw chain-of-thought never returned** · **MANDATORY 30-day data retention, ZDR UNAVAILABLE** (Fable/Mythos are "Covered Models") — **press reports Opus 5 does NOT carry this** (T2). Same ~30%-more-tokens 4.7-gen tokenizer trap.

### B5. Fable 5 benchmarks — with two splice-traps flagged
Vendor (2026-06-09): SWE-bench Pro 80.3% · Terminal-Bench 2.1 88.0% · FrontierCode Diamond 29.3% (Opus 4.8 13.4%) · OSWorld-Verified 85.0% · ExploitBench 78.0% · HLE 53%. **SWE-bench Verified 95.0% is independently corroborated on vals.ai** (third-party harness) = solid, unlike the Opus 5 number.
**TRAP 1 — AA index CONTRADICTION:** 64.9 (#1 at launch, June) vs **59.9** (BenchLM, July). Likely a re-basing between versions, unconfirmed. **Never quote an AA number without version+date.** Also: **AA states it "supported @AnthropicAI with pre-release evaluation of Claude Fable 5"** → the June figure is **vendor-collaborated, not arm's-length** (B63).
**TRAP 2 — GDPval version splice:** Fable 1932 Elo (June, v1) vs 1747 (v2, in Opus 5 materials). **Different benchmark versions — 1932 and 1747 are NOT comparable; any "Fable declined" read from this pair is wrong.**
LMArena: #1 at 2026-07-10 snapshot, **~1500-1525 band, ±25 at best** (T3 each). **Aider: NO Fable 5 result exists — do not synthesize one.**

### B6. 🔴 CORRECTION — our "stronger generator / weaker reviewer" datum is STALE **and** MISATTRIBUTED
Booked 2026-07-21 (day-state) as T2 CodeRabbit. Three problems:
1. **Misattribution:** the phrase surfaces in CodeRabbit's **Opus 5** review, not verifiably in the Fable 5 piece. CodeRabbit's harness measures **review only** — the "stronger generator" leg is **inference, never measured. UNVERIFIED.**
2. **We had the direction wrong:** actual Fable-5-vs-Opus-4.8 data (2026-06-09, 105-EP benchmark) = actionable EPs **65 vs 66 — a TIE on recall**; precision 32.8% vs 35.5% (**−2.7pp**), full precision 19.4% vs 26.5% (**−7.1pp**), 253 comments. **It's a precision/noise story, NOT "finds less."** If we booked it as reduced coverage, that was wrong.
3. **STALE — the important one:** the eval ran **2026-06-09 on PRE-suspension, PRE-classifier Fable 5.** Today's Fable carries the 07-01 classifier that bounces infra work to Opus 4.8. **A June-9 review-quality measurement is not valid for the model you'd run today.** Re-run required before this drives any workflow decision.

### B7. 🔴 CORRECTION — "weight-forensics ~Jul-27" is LIKELY A CONFLATION
Booked in **B64 AMENDMENT** (`meta/biases-watchlist.md`) as "weight-forensics pending ~Jul-27." **No announced forensic study for that date was found.** What IS scheduled 2026-07-27 is **Kimi K3's open-weights release (2.8T params, largest open-weight model to date)** — which *enables* third-party forensics, but is not itself a result. **Do not expect a verdict on 07-27; expect the raw material for one.**
**The Kratsios allegation itself (2026-07-22): ALLEGATION = FACT** (OSTP director, on record, dated — Moonshot "distilled Anthropic's Fable for K3," GB300s via Thailand, "sophisticated internal platform… to avoid detection"; Bessent considering sanctions; Anthropic's Sarah Heck called it "IP theft and industrial espionage"). **SUBSTANCE = UNVERIFIED** — no logs/training records/forensic package published; Moonshot denies (credits Moon Clip, Kimi Delta Attention, Attention Residuals); Chinese-language coverage (VOA中文, UDN, 网易, 文学城) uniformly frames it as 指控 without 公开可验证证据. **Timeline objection (strong):** Fable was offline 12 Jun–1 Jul and K3 appeared weeks after restoration — full base-model distillation in that window is implausible per researchers; targeted post-training possible but unproven. **Strongest circumstantial base is PRIOR, not this instance:** Feb-2026 Anthropic accusation of ~16M exchanges across ~24,000 fraudulent accounts, **3.4M attributed to Moonshot**. A T3 "statistical analysis suggests distillation" claim is UNVERIFIED-SINGLE-SOURCE — do not book.

## LEG C — HEAD-TO-HEAD ✅ (agent returned; T1 docs read IN FULL — the useful half; press/HN/Reddit 403 → empirical layer near-empty)

### 🚨 C1. THE FINDING THAT DECIDES THIS — Anthropic's own Fable-5 prompting guide describes THIS HARNESS as a refusal trigger
**T1 verbatim** ([platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5)):
> *"Prompts, skills, or **harness instructions that tell the model to echo, transcribe, or explain its internal reasoning as response text** can trigger the `reasoning_extraction` refusal category on Claude Fable 5, **causing elevated fallbacks to Claude Opus 4.8**."*

**That is a description of this OS.** Every Rule-#16 verifier is instructed to show its adjudication reasoning; every claim carries provenance; the tier-tagging convention is *literally* "explain why you believe this." Combined with Leg B1 (cyber-classifier FPs on infra work + session-level sensitivity inflation + **silent** mid-session switching), the conclusion is structural, not incidental.
**Measured blast radius (T2, multi-source):** **20.9% of Anthropic's OWN Terminal-Bench 2.1 trials tripped the classifier and fell back**, dragging Fable's effective **84.3% below unrestricted Mythos 5's 88.0%** — vs Anthropic's headline "<5% of sessions." Opus 5's classifiers reported to trigger ~85% less often (**single-origin, traceable to Anthropic, and a FORECAST not a measurement — UNVERIFIED**).
**🔴 RETRO-CAVEAT ON OUR OWN BOOKED PROVENANCE:** the 2026-07-23 "dedicated Fable-5 harness-audit instance" ran git-guard bypass probes, permission-check auditing and hook enforcement — **precisely the content class that trips this classifier** — while showing its reasoning throughout. **We cannot currently verify it executed on Fable 5 end-to-end; some or all may have silently run on Opus 4.8.** The audit's *work* stands on its receipts (probes, tests, commits); only the **model-attribution** claim is now uncertain. Instrumentation gap logged below.

### C2. Anthropic's own guidance is SELF-CONTRADICTORY for our use case (T1)
`models/overview`: *"start with Claude Opus 5 for complex agentic coding and enterprise work. For workloads that need the highest available capability, use Claude Fable 5."* But `choosing-a-model` assigns **"advanced research" and long-horizon agentic work to BOTH**. **Anthropic has not cleanly separated these two models for exactly our workload.** (Agent also flagged a retrieved "migration guide" block claiming both are $10/$50 and that Opus 5 requires 30-day retention — **CONTRADICTED-BY-T1 on four other pages; assessed a fetch artifact; DO NOT CITE.** Honest inclusion of a self-caught retrieval error.)

### C3. THE STEERABILITY FINDING — and it independently corroborates yesterday's over-constraint hypothesis
Two official guides, **opposed** warnings, both T1:
- **Fable 5:** *"Instruction-following is improved enough that you can steer most behaviors with a **brief instruction rather than enumerating each behavior by name**."* … *"Skills developed for prior models are often **TOO PRESCRIPTIVE** for Claude Fable 5 and **CAN DEGRADE OUTPUT QUALITY**. Review and consider removing older instructions if default performance is better."*
- **Opus 5:** responses *"run longer than prior Opus models"* · written files *"often longer"* · *"can **expand the scope of a task**, adding steps that weren't requested"* · *"**may follow that instruction literally**"* (the code-review example: told to be conservative, it under-reports) · *"**verifies its own work without being told to** — instructions like these **cause over-verification**."*

**🔗 CROSS-LINK — this is independent T1 corroboration of the over-constraint audit commissioned yesterday** (`meta/redteam/2026-07-24-overconstraint-audit-commission-prompt.md`): Anthropic's own documentation states that **prescriptive scaffolding actively degrades Fable 5's output**. Our harness is dense with prescriptive METHOD-rules. The path-freedom hypothesis now has a vendor-documented mechanism behind it, arrived at from a completely independent direction. **The over-constraint audit just became higher-value, and its lens is validated externally.**
**For the path-free-prompt requirement specifically:** *neither* model is documented as template-resistant. **Opus 5 is the more LITERAL instruction-follower** (good: follows an unusual prompt as written; bad: under-reports if you tell it to be conservative, and pads/scope-creeps by default). **Fable 5 is the one explicitly documented as degraded BY prescriptive scaffolding** (good: rewards path-free prompts; bad: refusal-fallback risk).

### C4. Three hard T1 ops differences that outrank every benchmark
| Difference | Winner | Detail |
|---|---|---|
| **`reasoning_extraction` refusals + silent Opus-4.8 fallback** | **Opus 5** | T1 doc quote + 4 independent T2 reporters on Fable over-refusal (Register "blocked us at 'hello!'", Ready Solutions silent-degradation, TechTimes debugging −70%, GitHub #67306 open) |
| **ZDR eligibility** | **Opus 5** | T1 `api-and-data-retention`: *"Claude Fable 5 and Claude Mythos 5 are designated Covered Models and require 30-day data retention; ZDR is therefore not available for either."* Fable requests from a ZDR org return **400**. Opus 5 is NOT on that list → ZDR-eligible. **A procurement gate Fable cannot clear for confidential material.** |
| **Priority Tier (99.5% uptime)** | **Fable 5** | T1 `service-tiers`: supported on all models **except Mythos 5, Mythos Preview, Opus 5, Sonnet 5**. *Moot in practice* — "Priority Tier capacity commitments are no longer available for purchase." |

### C5. Benchmarks — thin, contested, and NOT decision-grade
Direct vendor table exists (2026-07-24) — but: **win-count CONTRADICTED between sources** (R&D World "8 of 13" vs llm-stats/codersera "5 of 9 comparable percentage benchmarks", unreconciled) · **Fable LOSES only 2 rows: DeepSWE v1.1 68.8 vs 69.7 and Legal Agent Benchmark 11.7 vs 13.3** · **AA index 61 vs 60 = 1 point on a composite = analytically meaningless**, the "top model in the world" headline is a clean **framing-error specimen** · **several circulating "Fable" rows are actually MYTHOS 5 figures** (the unsafeguarded sibling) — do not treat them as what you'd get.
**NO LMArena head-to-head exists** (the #1-Fable snapshot is 2026-07-10, predates Opus 5 by two weeks — any current use is STALE-RECYCLE). No Aider/SWE-bench board with both. **No practitioner corpus exists at all — Opus 5 is ~1 day old.** The circulating "practitioner" quote (Lovable: "up 22%") is an **Anthropic design partner in the launch post, comparing to Opus 4.7 — not to Fable 5**; echoing it as Opus-beats-Fable evidence is a substitution error.
**MISATTRIBUTION TRAP (agent-caught):** the circulating *"Opus 5 costs 21% more per unit at cheapest setting, 80% more at high effort"* is **Opus 5 vs GPT-5.6 Sol under batch pricing, NOT vs Fable 5. REFUTED as an Opus-vs-Fable claim.** But the underlying mechanism is real: Opus 5 is documented as more verbose → **per-token price is a poor predictor of per-task cost**; the 2.0× list advantage compresses by an unquantified amount. **No Opus-5-vs-Fable-5 cost-per-task study exists.**

### C6. "Different exponentials" — PREMISE REFUTED
Fable is **not** a creative/generative line. T1: Mythos 5 *"shares Claude Fable 5's capabilities **without the safety classifiers**"* — **Fable is the safeguarded public build of the Mythos frontier weights.** It's the *gated-frontier* line; the name misleads. **Nathan Lambert/Interconnects has NO Opus 5 analysis** — his two relevant pieces are June 2026, ~6 weeks stale; quoting either on this choice is a stale-recycle. **No "different exponentials" framing for these two lines exists from anyone.**

---

# SYNTHESIS — SELECTION RULE (my model, on the verified evidence above)

**The benchmarks do not decide this. The refusal architecture, the retention policy, and the steerability tuning do.**

| Workload class (this desk) | Model | Why (evidence rank) |
|---|---|---|
| **Verification fan-outs / Rule-#16 agents** (must show adjudication reasoning) | **Opus 5** | C1 — `reasoning_extraction` is a *documented* Fable refusal category; our agents are the canonical trigger |
| **Harness/infra auditing, git-guard probes, permission-check work** | **Opus 5** | B1 — cyber-classifier FPs on self-administration + sensitivity inflation + **silent** fallback |
| **Anything touching confidential portfolio/holdings data** | **Opus 5** | C4 — Fable is a Covered Model, ZDR unavailable, mandatory 30-day retention |
| **High-volume routine ingest/cascade** | **Opus 5** | 2.0× list-price advantage (compressed by verbosity, magnitude unknown) + Max-plan full limits vs Fable's 50% |
| **Longest-horizon single-thread reasoning with NO reasoning-echo and NO infra content** | **Fable 5** | Anthropic's own routing advice; the only remaining clean case |
| **Path-free / attractor-lens prompting** (the Cantina thread) | **contested — genuinely undecided** | Fable is documented as *degraded by prescriptive scaffolding* (good for path-free); Opus 5 is the more *literal* follower (also good, differently). No evidence separates them. **Candidate A/B.** |

**The uncomfortable core (stated because it's the honest read):** Fable 5's remaining edge is "highest available capability," and Anthropic explicitly notes Opus 5 is *not* SOTA for risky/dual-use capabilities like cybersecurity — **which is exactly the work Fable's classifier is most likely to bounce to Opus 4.8.** The case for running Fable on our hardest security-adjacent work is close to self-defeating.

**Two operational actions this dive generates (harness-layer, no position impact):**
1. **STRIP carried-over "verify your work" instructions if running Opus 5** — T1 explicitly warns they cause over-verification. Our harness is dense with them. *(Not executed here — it's a live-enforcement change touching prompts/hooks; specced, not shipped.)*
2. **INSTRUMENTATION GAP — we cannot detect Fable→Opus-4.8 silent fallback.** Every "ran on Fable 5" provenance claim in this corpus is currently unverifiable. Candidate: log the responding model ID per agent fire into the fire-log. **This is the say-do/receipts discipline applied to model provenance** — and it's a real hole the receipts-hook scope should absorb.

**Position implication: ⚪ NO ACTION — this is an OPS decision, not a market thesis 🟡.** No Anthropic valuation/revenue/competitive read is generated (a launch table is not a business signal). **One investment-relevant read-through carries forward:** the 2026-06-12 BIS "is informed" letter is precedent that a US agency can zero a frontier model globally with ~90 minutes' notice; the control was withdrawn but **the authority was never disclaimed**, and Mythos relief is revocable at Commerce's discretion. Any thesis premised on frontier-model availability continuity (TC-10 sovereignty cluster, NBIS bypass-route, sovereign-AI names) must carry this as a live tail risk.

**Falsifier for this artifact:** the empirical layer is near-empty — Opus 5 is ~1 day old, zero independent practitioner data exists. **Re-verify in 2-3 weeks.** If real head-to-head practitioner evidence contradicts the doc-derived selection rule above, the rule loses to the evidence.

## IN-HOUSE WORK-PRODUCT FORENSICS ✅ (computed 2026-07-25 from the corpus — the differentiated leg no external source can produce)

| Metric | Fable-5 | Opus 4.8 |
|---|---|---|
| Attributed mentions across artifacts (computed grep) | **20** | **267** |

**Fable-5 deployment pattern here = concentrated on the HEAVIEST structured work**, not routine: the four 6-subagent deep dives (SONY, RENISHAW, NABTESCO, HTFL — Jun 9-10), the 3-subagent HYNIX/MU verification (Jun 11), MLCC tier-bifurcation, medical-AI Phase 2, AXTI 2-subagent, and the **2026-07-23 dedicated P0 harness-audit instance** (operator-funded).

**Fable-5 quality receipts (from `meta/redteam/2026-07-23-fable5-harness-audit-P0-hardening.md`, verifiable):**
- **Reproduce-before-fix throughout** — failing probe as reproduction receipt before every patch; 25/25 re-probe.
- **Caught a MATERIAL metric contamination (G-28)** that was about to adjudicate the 08-06 priming-hook experiment WRONGLY: contaminated read 0.131→0.217 (= retire) vs clean read 0.120→0.105 (= keep).
- **Root-caused a red test to the HOOK, not the fixture** — resisted the easy fix.
- **Honestly listed 7 NOT-EXECUTED items**, including a newly-discovered pre-existing test failure verified via stash-bisect. **Anti-production-bias behavior: reporting undone work it could have quietly omitted.**
- The three robotics deep dives all returned **thesis FAILURES** (5 consecutive bypass-route fails) — willing to kill theses rather than confirm them (confounded: the protocol demanded bypass-testing).

**Metric computed and DISCARDED as unusable (stated so it can be audited):** correction-type mentions in Fable-authored thesis files (SONY 4, RENISHAW 7, NABTESCO 6, HTFL 0) cannot be attributed — they include later corrections from other sessions on the same files, so they measure FILE ACTIVITY, not model error. Reporting it as a quality signal would be dressed-up noise.

**Prior desk datum (2026-07-21 day-state, T2 CodeRabbit):** "Fable-5 stronger generator / weaker reviewer than Opus 4.8." **Note the new CodeRabbit finding runs the SAME direction for Opus 5 vs its own baseline (recall −5.9pp) — i.e. the generator/reviewer split may be a family-wide axis, not a Fable-specific one.** Needs Leg C to adjudicate.

## Synthesis + selection rule — PENDING Legs B & C
