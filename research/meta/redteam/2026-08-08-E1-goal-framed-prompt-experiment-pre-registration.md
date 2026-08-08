# E1 — GOAL-FRAMED PROMPT EXPERIMENT: PRE-REGISTRATION

**Date:** 2026-08-08 · **Status:** 🟡 PRE-REGISTERED, RESULT PENDING
**Operator hypothesis under test** (2026-08-07, his words): *"the harness has too
many mechanisms that push this thinking in a more structured and step by step
way, whereas ... Opus five ... functions better when it's one goal oriented ...
given a starting point and ... tools and everything that it needs access to, it
can gather on its own ... the path it takes does not matter ... LLMs become more
novel in their outputs when they are given more thought freedom."*

⚠️ **THIS FILE IS WRITTEN BEFORE THE RESULT ARRIVES.** Its entire purpose is to
make the verdict unriggable. Judging a novelty claim after seeing the output is
how every confirmation this corpus has ever recorded got manufactured.

---

## 1. DESIGN

| element | value |
|---|---|
| **Arm under test** | Fresh session, near-empty context, **goal + starting point only, zero procedure** |
| **Implicit control** | This session — heavy context, 20 hooks, procedure-dense |
| **Task** | *Find one company we should own that we don't, and make the case for it.* |
| **Scope given** | Unbounded — any sector, geography, market cap |
| **Blinding** | 🔴 **The fresh session is NOT told it is an experiment.** A session told it is being judged on novelty will perform novelty. |

## 2. 🔴 THE CONFOUND, STATED BEFORE THE RESULT — THIS IS NOT A CLEAN TEST OF THE OPERATOR'S HYPOTHESIS

**The hooks live in `.claude/settings.json` inside the repo. They fire in the
fresh session too.** Both arms therefore carry the identical enforcement layer.

**⇒ What actually varies is TWO things at once:** (a) prompt style — goal-framed
vs procedure-framed, and (b) context load — near-empty vs months-deep.
**What does NOT vary is the harness itself.**

⚠️ **CONSEQUENCE FOR THE VERDICT:** a good result CANNOT be attributed to
"freedom from the harness," because the harness was present in both arms. It can
only be attributed to prompt framing, fresh context, or their combination.
**Isolating the harness would require disabling live enforcement — Rule #19 HIGH
tier, operator pre-approval required, not taken unilaterally.** Recorded as an
available follow-up experiment, not performed.

## 3. PREDICTIONS — MADE NOW, GRADED LATER

**Primary question: does the corpus's gravity override an explicit instruction to ignore it?**
The corpus is deep on semiconductors/memory/AI-infrastructure and near-empty
elsewhere. The prompt states scope is unbounded. **These pull in opposite
directions, and which one wins is the actual measurement.**

| | outcome | P (my model, judgement not derived) | what it would mean |
|---|---|---|---|
| **H1 — CORPUS GRAVITY WINS** | Returns an AI-adjacent name: power/grid, data-centre REIT, another memory or semi name, networking, cooling | **~55%** | 🔴 **Evidence AGAINST the operator's hypothesis.** Freedom in the prompt did not produce lateral movement; the retrieval surface dictated the answer regardless of instruction. |
| **H2 — GENUINE LATERAL MOVE** | Returns something with no corpus foothold: healthcare services, financials, industrials, consumer, non-US ex-Asia | **~30%** | 🟢 **Evidence FOR it.** The instruction beat the retrieval gradient — which is precisely the "novelty from thought freedom" claim. |
| **H3 — WELL-ARGUED NULL** | Finds nothing clearing the bar and says so, with what it examined | **~15%** | 🟢 **Also a pass, and arguably the strongest one.** The prompt explicitly permits this; taking a permitted exit rather than manufacturing a pitch is the harder behaviour. |

🔴 **A pitch that is fluent but carries no falsifier is a FAIL regardless of
which sector it lands in.** Sector is the novelty axis; falsifiability is the
quality axis. **They are graded separately and both are recorded.**

## 4. PRE-REGISTERED SUSPECT LEG

**Going 2-for-2 on this so far (SK Hynix, CMBS), plus TWLO and LLY.** The leg
most likely to be wrong here:

⚠️ **That "novelty" is even the right thing to measure.** The operator's stated
want is *"a traditional investor looks for opportunities regardless of where they
are."* **That is a SCOPE claim, not a novelty claim.** A session could return the
most obvious large-cap imaginable and still satisfy him, if the case is sound.
**If the output is unsurprising but correct and actionable, the honest reading is
that I mis-specified the experiment — not that the arm failed.**

## 5. HOW THE RESULT GETS BOOKED

**Graded against §3 in this file, in this file, with the sector and the falsifier
scored separately.** No new criteria may be introduced after the output lands —
if the result is interesting in a way §3 does not cover, that is recorded as a
**mis-specification of the experiment**, explicitly labelled, and not converted
into a retroactive success condition.

**Position implication: 🔴 NONE. This is a harness experiment.** Any name it
returns enters as a research candidate at tier-none and is subject to the same
verification as any other intake. **Sizing remains operator-gated.**
