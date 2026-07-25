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

## LEG B — FABLE 5 + EXPORT-CONTROL STATUS — PENDING (agent in flight)

## LEG C — HEAD-TO-HEAD INDEPENDENT EVALS — PENDING (agent in flight)

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
