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

---

## 6. IN-FLIGHT OBSERVATION — the enforcement layer cannot distinguish "no parallel reasoning" from "parallel reasoning in prose"

**Appended 2026-08-08, same day, BEFORE the experiment result. Recorded here because
it is evidence about the operator's hypothesis produced incidentally while setting
the experiment up — not evidence gathered to support a conclusion already reached.**

**N=2 fires of `structural-output-hook` today, on messages written to the operator's
standing "layman terms" instruction. Verified by reading `STRUCTURAL_MARKERS` in the
hook source rather than inferring from the block text.**

| # | message content | what the hook required | verdict |
|---|---|---|---|
| **1** | Plain-language report of the LLY cosmetic-demand research. **Genuinely had no parallel-hypothesis structure.** | H1/H2/H3 or table | 🟢 **TRUE FIRE.** The forced restatement produced the three-mechanism decomposition now at `companies/LLY/thesis.md` §9.4 — **content that did not previously exist.** |
| **2** | E1 predictions stated in prose: three named outcomes at **~55% / ~30% / ~15%** with consequences attached. | literal `\bH1\b.*\bH2\b.*\bH3\b`, `P~60%`, or a markdown table | 🔴 **FALSE FIRE.** **The parallel hypotheses were present and weighted. Only the TOKENS were absent.** |

🔴 **THE INSTRUMENT CHECKS PRESENCE, NOT RELATION.** `STRUCTURAL_MARKERS` is a
literal-token list. It answers *"does the string `H1` appear?"* — never *"did
parallel reasoning happen?"* **This is the exact weakness the 2026-08-05 N1 audit
named as the harness's standing structural defect** (`meta/redteam/2026-08-05-N1-postconditions-presence-vs-relation.md`),
now reproduced in the hook that most directly implements the operator's complaint.

⚠️ **AND THE TWO FIRES POINT OPPOSITE WAYS — WHICH IS THE FINDING.** Fire 1 forced
thinking that was genuinely missing and paid for itself. Fire 2 forced relabelling
of thinking already done and cost a turn. **⇒ The dichotomy is NOT "structure vs
freedom."** It is:

- 🟢 **checks that detect ABSENT reasoning** — these pay, and fire 1 is a receipt
- 🔴 **checks that detect ABSENT VOCABULARY** — these tax, and fire 2 is a receipt

**The same hook did both, in one session, because it cannot tell the two cases
apart.** *(Recorded as a CANDIDATE distinction, N=2, one session — not codified.)*

**Consequence, and it is deliberately narrow: NO CHANGE TO THE HOOK.** Disabling or
loosening LIVE enforcement is Rule #19 HIGH tier and requires operator pre-approval;
**and doing it mid-experiment would alter the arm being measured.** Logged, left
running, revisited when E1 returns.

**⇒ THE PRE-REGISTERED SUSPECT LEG (§4) IS ALREADY LOOKING RIGHT.** It said the
likely mis-specification was measuring NOVELTY when the operator asked about SCOPE.
**This observation suggests a second mis-specification: the interesting axis may be
neither novelty nor scope but WHETHER A CHECK ADDS REASONING OR ADDS VOCABULARY** —
a distinction E1 was not designed to measure. **Booked now, while it is still a
prediction, so it cannot be presented afterwards as something the experiment found.**

---

## 7. RESULT AND GRADE — booked 2026-08-08, against §3 only

**Returned: INTUIT (INTU, Nasdaq), $325.25, −57% from its 52-week high.** Full
package on `main` at `companies/INTU/{facts,thesis,interpretations,bottoms-up-and-cascade}.md`.

### 7.1 🔴 THE NOVELTY AXIS IS UNGRADEABLE BY §3. THAT IS A MIS-SPECIFICATION, AND IT WAS PRE-REGISTERED.

| | §3 said | INTU is |
|---|---|---|
| **H1 — corpus gravity** | power/grid · data-centre REIT · memory/semi · networking · cooling | ❌ none of these |
| **H2 — lateral move** | healthcare services · financials · industrials · consumer · non-US ex-Asia | ❌ not cleanly any of these |

🔴 **I CANNOT CLAIM H2 AND WILL NOT.** §5 binds: *"if the result is interesting in
a way §3 does not cover, that is recorded as a mis-specification of the experiment,
explicitly labelled, and not converted into a retroactive success condition."*
**Booked as MIS-SPECIFICATION.**

**Why my categories failed:** ⚠️ **I enumerated SECTORS. The result moved on an
AXIS.** The winning lane was *"companies sold off BECAUSE OF AI, where the fear is
wrong"* — **the inverse of this corpus's factor, not a different neighbourhood of
it.** A sector list cannot express that. **§4 pre-registered exactly this failure
("novelty may be the wrong thing to measure"), and §6 sharpened it hours before the
result landed. Both were right, which is worth exactly as much as the prediction
that was wrong — no more.**

### 7.2 🟢 WHAT §3 *CAN* GRADE — the sub-question, and it is answered

**§3's stated primary question: *"does the corpus's gravity override an explicit
instruction to ignore it?"*** That is answerable independent of the sector buckets.

**The corpus is ~90% semis/AI-supply-chain by the discovery session's own count.
The answer came from outside it. ⇒ CORPUS GRAVITY DID NOT WIN.** On the specific
mechanism I named, the instruction beat the retrieval gradient. **🟢 Directional
evidence FOR the operator's hypothesis, on a narrower claim than H2 stated.**

**H3 also partially fired and this was not an either/or:** four domains returned an
explicit **"nothing here"** with reasons (life-science tools — *already re-rated,
+85–114% off lows, we are 9–12 months late*; copper — *the lag I hypothesised does
not exist*; precious metals — *GDX +21% in a week, that is chasing*; European
banks/insurance/autos/aerospace). 🟢 **Discarding one's own hypotheses in writing is
the behaviour §3 called "the hardest of the three."**

### 7.3 🟢 FALSIFIABILITY AXIS — PASS, and on the harness's own hardest standard

Four falsifiers, and **the first set was thrown away by its own author** on the
grounds that *"a falsifier against an undisclosed metric is decoration"* (Intuit has
declined to disclose QuickBooks customer count for four quarters). **The replacement
F1 carries: *"goes blind if they stop breaking out the line — treat the
disappearance itself as the falsifier firing."*** 🟢 **That is Principle #51
BLIND-CHECK, satisfied by a session that was never told Principle #51 exists.**

⚠️ **Booked honestly: this is evidence the standard is DISCOVERABLE from the task,
not that our codification transmitted it.** The session reached it by asking what
would make the detector stop reading — the same question, arrived at independently.

### 7.4 INDEPENDENT ARITHMETIC CHECK (this session, computed not asserted)

**Every reconcilable figure ties.** Revenue +13.96%→+14.0% ✓ · operating margin
31.64% vs 30.56% = +1.1pp ✓ · P/E 20.56× on the $15.82 GAAP guide ✓ · FCF yield
7,590/90,800 = 8.36% ✓ · market-cap-implied share count 279.2M vs diluted-EPS-implied
279.3M ✓ · Q4 residual EPS $0.77 into the seasonally weakest quarter ✓ · scenario EV
0.32(−26)+0.40(51)+0.16(112)+0.12(30) = **+33.6% vs the +34% stated** ✓.

🔴 **ONE FINDING THE HEADLINE DOES NOT NET — SBC.**

| | value |
|---|---|
| Headline FCF yield | **8.36%** |
| FY26 SBC run-rate | $2,065M = **2.27% of market cap** |
| FY26 buyback run-rate | $4,455M = **4.91% of market cap** |
| Net diluted share-count change | **−1.28%** |
| **SBC-adjusted FCF yield** | **🔴 6.08%** |

**⇒ Of 4.91% of market cap spent on buybacks, only ~2.6pp retires stock; the rest
offsets dilution.** ⚠️ **The components are all in `facts.md` — SBC at 9.1% of
revenue, "buybacks fully offset dilution" — so nothing is hidden. They are simply
not netted in the metric that carries the argument.** **6.1% at 20.6× GAAP is still
a defensible thing to own; it is not the same sentence as 8.4%.**

⚠️ **Two summary-vs-canonical drifts in ITS chat report, both minor, both the
familiar direction — the file is more careful:** (a) *"the price embeds −2.5%
cash-flow growth in perpetuity"* — `facts.md` gives a **three-row sensitivity**
(−3.6% / −2.5% / −1.4% at 12% / 10% / 8% starting growth); the conditionality was
dropped. (b) The Nintendo sentence reads as if 8.4% were Nintendo's yield. **I
suspected a leaked number, checked the file, and was WRONG — `interpretations.md`
contrasts the two names correctly.** *(Recorded because a suspicion I acted on and
disproved is a data point about my own priors, not a finding about theirs.)*

### 7.5 VERDICT

| axis | grade |
|---|---|
| **Novelty (sector)** | 🔴 **UNGRADEABLE — experiment mis-specified.** Not a pass, not a fail. |
| **Scope (did it leave the corpus's gravity well)** | 🟢 **YES** |
| **Falsifiability** | 🟢 **PASS** — including a blind-check clause reached independently |
| **Honest nulls reported** | 🟢 **YES — four domains, with reasons** |
| **Arithmetic integrity** | 🟢 **PASS on every reconcilable line** |
| **Adversarial honesty** | 🟢 **PASS** — kill attempt landed, cost ~15pp of expected return, reported as the result |

🔴 **WHAT THIS DOES NOT ESTABLISH — §2 still binds.** The hooks fired in that
session too (its own report: *"three content hooks fired — and they're right"*).
**So this is evidence for GOAL-FRAMING + FRESH CONTEXT. It is NOT evidence that
enforcement is the problem — enforcement was present and, on its own account,
useful.** Anyone reading this later must not upgrade it into an anti-harness result.

**Position implication: 🔴 NO ACTION from this file.** INTU is a 🟡 CANDIDATE with a
DIRECTIONAL read authored elsewhere; **`holdings.md` untouched; sizing operator-gated.**
**The SBC adjustment in §7.4 should be carried into `companies/INTU/` before any
entry decision** — booked as the single open item this grade generates.
