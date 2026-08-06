# 2026-08-05 — ROOT-CAUSE: 33 hook fires, 8 errors, 0 overlap. The enforcement layer checks the FORM of output, never the COMPARABILITY of operands.

**Origin:** operator question, 2026-08-05, verbatim-adjacent: *"why do you keep making mistakes… Is it a misdesign? Is there too many rules? Is there too many hooks? Or are too many rules not hooks? Identify the core root issue."*

**Answer: none of those three.** Not too many rules, not too few hooks, not the wrong rules/hooks ratio. **Every enforcement object in the harness validates the shape of the output text. Not one validates whether two numbers being compared were measured on the same basis.** That is where all the errors live.

---

## §1 — The counts (computed 2026-08-05, not recalled)

| | Count | Method |
|---|---|---|
| Codified items (Critical Rules + Lessons + Biases + Principles) | **164** | grep over CLAUDE.md / lessons.md / biases-watchlist.md / methodology.md |
| Hook scripts | **21** | `ls research/meta/hooks/*.py` |
| **Hook fires, 2026-08-05** | **33** | `grep -c "2026-08-05" meta/hook-fire-log.md` |
| **Errors made, 2026-08-05** | **8** | enumerated §2 |
| **Errors caught by any hook** | 🔴 **0** | — |

⚠️ The 164 is a grep count and over-counts where sub-clauses match the header pattern (Critical Rules greps 44 against a nominal 19). **The order of magnitude is the point, not the digit.**

**`grep -l "basis\|comparable\|like-for-like\|same-basis\|seasonal" research/meta/hooks/*.py` returns NOTHING.** No hook mentions basis, comparability, or seasonality.

## §2 — The eight errors, and why they are one error

| # | What happened | The two things compared | Basis mismatch |
|---|---|---|---|
| 1 | Counted Kioxia in an "N=3 beat-and-fall" list | a **miss**-and-fall vs **beat**-and-falls | **category** |
| 2 | Called AMD's drop −8.8% | after-hours price vs a close that had risen +7.00% that day on unrelated sector news | **reference price** |
| 3 | Built a grading annotation on a semis "bear market" | 08-03 state (−22.01%) vs the actual 08-04 state (−16.90%) | **date** |
| 4 | Told the operator the corpus held SpaceX as private | my recall vs `private-tracker.md`, which said the opposite | **retrieval — the one that is NOT a basis error** |
| 5 | Logged Infineon as pointing *opposite* to the "good news isn't enough" story | an *instance* of a pattern vs a *counterexample* to it | **category** |
| 6 | Called the guide "re-based" on +0.82% → +7.31% | a **Q1** guide vs a **Q2** guide, across a seasonal break (Q1 mean +4.16%, Q2/Q3/Q4 ~+7%) | **season** |
| 7 | Cited "RPO +51% YoY" twice as bullish corroboration | a four-quarter figure of which **one quarter carried 57%** ($673.6m of $1,175.4m) | **time window** |
| 8 | Ran the whole guide-vs-actual series un-normalised | quarters of **90, 91 and 92 days** treated as equal — worth ~3.3pp of a 6.5pp "anomaly" | **denominator** |

🔴 **Seven of eight are the same failure: two numbers compared without checking they were measured on the same basis.**

**#8 was found by a commissioned subagent, not by me and not by any hook** — after I had already published the un-normalised series to the operator twice and written it into a live prediction file.

## §3 — Why the hooks cannot see it

Every one of the 21 hooks answers a question about **the text**:

> is there a citation? · is there a hedge tag? · is there an H1/H2/H3? · is there an N-th-order marker? · is there a `Position implication:` line? · is there an M/N score? · is there a bypass route named?

**None answers a question about the operands.** The arithmetic was correct in all eight cases — Principle #43b (COMPUTE-INSTEAD-OF-NARRATE) worked exactly as designed and made me **compute the wrong comparison faster, and to more decimal places.**

> **A calculator does not check units. Neither does a regex.**

## §4 — 🔴 The second-order harm: the enforcement layer manufactures false confidence

**33 fires in one day produce the *sensation* of being checked.** Every message containing all eight errors **passed every hook it triggered**. The layer is a high-volume generator of confident false negatives, and the volume is precisely what makes them feel verified.

**This is worse than an absent check.** An absent check leaves a known gap. A busy check that cannot see the error class fills the gap with noise and closes the question.

## §5 — The fix is ONE thing, and adding item 165 is the wrong response

**L42-b already had the right idea and was scoped too narrowly.** It reads: *every percent-change figure entering the corpus carries a BASIS STAMP — settle / intraday / extended-hours — or it is unusable.* That is exactly the discipline needed. It was written for **price** basis after a single price-basis error, and so it never generalised to season, denominator, category, time-window or reference-point.

**GENERALISE L42-b. Do not write a new rule.**

> **L58 (CANDIDATE, N=7 in one day): every number carries what it was measured AGAINST, and no two numbers may be compared until their bases match. Basis includes — at minimum — reference point, date, category, season, time window, and denominator (including day count).**
>
> **Enforcement is CONSTRUCTIVE, not filtering: any multi-row comparison table must carry an explicit BASIS column, and building the column is what performs the check.** A comparison whose basis column has two different values is not a finding; it is a bug.
>
> *Blind-check (#51): distinguishes "these two numbers are comparable" from "these two numbers are both floats" · reads on whether every row of a comparison declares its reference point, period length, and category · **goes blind if** the basis is genuinely unknowable (an undated vendor snapshot — the exact hole that made the DDOG consensus series unfalsifiable) — in which case the row is marked UNCOMPARABLE and excluded, never silently averaged in.*

**Why this cannot be a Stop hook, stated honestly:** the error occurs in reasoning, before any text exists to scan. A regex can check that the word "basis" appears; it cannot check that Q1 and Q2 are different seasons. **This must be a construction template, not an output filter** — which is also why it does not add to the 21 and should not.

## §6 — What this proposes RETIRING, so the fix is net-subtractive

The finding above indicts the *volume* of form-checking. It would be self-refuting to answer it with more codification. **Proposed, requiring the operator's call on anything LIVE (Rule #19: disabling live enforcement is HIGH tier):**

1. **Fold L42-b into L58.** L42-b becomes the price-basis worked example inside the general rule, not a separate lesson.
2. **Audit the 21 hooks against real catches.** The instrument already exists — `meta/hook-fire-log.md`. The question to answer per hook: *in the last 30 days, did a single fire prevent an error that would otherwise have shipped?* Any hook that cannot show one is decorative and falls under the harness's own standing "<5 fires/month → inert → retire" rule, or a stricter zero-catches variant.
3. **The `structural-output-hook` / `llm-native-priming-hook` normalized-metric decision is due 2026-08-06 — tomorrow.** It should be judged against *catches*, not fire counts. Today is direct evidence that fire count and catch count are uncorrelated.
4. **Count the 164 properly and publish the real number.** A codification tail nobody can state is a tail nobody is applying.

**Net-positive test (Rule #11):** the expected benefit is killing an error class that produced 7 instances in a single day, at a cost of one generalised lesson replacing one narrow one, plus a retirement audit that should *reduce* total codification. **If the audit adds objects rather than removing them, this artifact has failed on its own terms and should be reversed.**

## §7 — The honest limit

**I cannot self-audit this.** The eight errors are mine, the enumeration is mine, and the proposal to retire hooks is being written by the thing the hooks constrain. **The §6 audit should be commissioned to a fresh session** the way the #51 retro sweep was (`meta/redteam/2026-08-01-instrument-validity-audit-commission-prompt.md`), and for the same reason.

**Re-eval: 2026-09-05.** If the next 30 days produce ≥2 further basis-mismatch errors after L58 ships, the constructive-template approach has failed and the problem is not fixable at the discipline layer at all — which would itself be the most important thing the harness has learned about its own limits.

---

# §8 — THE AUDIT, EXECUTED 2026-08-05 (operator: "do it")

## 8.1 — Hook fire audit, all 20 hooks (`hook_fire_log.py` is a library, not a hook)

Computed from `meta/hook-fire-log.md`, 30-day window ending 2026-08-05.

| Class | N | Hooks |
|---|---|---|
| **ACTIVE** (≥5 fires/30d) | **9** | anti-fabrication (62) · macro-anchor (115) · structural-output (129) · session-prime (672) · git-guard (395) · nth-order-cascade (19) · session-prime-cascade (8) · bypass-route (7) · reasoning-tagging (6) |
| **BELOW the harness's own <5/month retirement threshold** | **7** | bottoms-up (4) · signal-ingest-cascade (4) · borrowed-vs-firstprinciples (2) · llm-native-reasoning (2) · antifragility-mn (1) · cascade-enforcement (1) · segment-trajectory (1) |
| **NO LOG AT ALL** | **4** | session-start · llm-native-priming · analyst-pt-context · meta-count-tripwire |

🔴 **The 4 NO-LOG hooks are NOT inert — that is an instrumentation gap, and conflating the two would be another basis error.** `session-start-hook` demonstrably runs every session (it produced today's briefing) and `llm-native-priming-hook` demonstrably runs every prompt (its injection is visible in-context). **They are unmeasurable, not dead.** The already-open to-do "HOOK EXECUTION PROBES — convert the supervisor from log-reader to actual supervisor" is exactly this and is **4 days from due**.

⚠️ **Fire counts are NOT catch counts, which is this artifact's whole thesis.** `session-prime-hook`'s 672 "fires" are context *injections*, not checks. `git-guard`'s 395 are guard *invocations*, most passing. **Nine of the biggest numbers in that table are not evidence of anything being caught.** Do not use this table to justify keeping a hook — only to identify candidates for the catch-audit that must follow.

**7 hooks sit below the harness's own pre-registered retirement threshold.** Retiring any of them is **Rule #19 MEDIUM-to-HIGH** (live enforcement) and is **left for the operator** — flagged, not executed.

## 8.2 — 🟢 THE PRE-REGISTERED DECISION DUE 2026-08-06, SETTLED ONE DAY EARLY

Metric fixed 2026-07-06: *weekly structural-output fires ÷ weekly main-branch commits.* Rule: **falling ⇒ priming works, KEEP; flat/rising ⇒ RETIRE the priming hook.**

| Week beginning | fires | commits | normalized |
|---|---|---|---|
| 2026-06-29 | 24 | 183 | 0.131 |
| 2026-07-06 | 32 | 272 | 0.118 |
| 2026-07-13 | 31 | 220 | 0.141 |
| 2026-07-20 | 58 | 230 | **0.252** |
| 2026-07-27 | 6 | 86 | 0.070 |
| 2026-08-03 (partial, 3 days) | 2 | 40 | **0.050** |

**0.131 → 0.050 = −61.9%. VERDICT PER THE PRE-REGISTERED RULE: FALLING ⇒ KEEP BOTH HOOKS.**

🔴 **And I am honoring that verdict while stating that the metric is now known to be invalid.** Today's finding is that **fire counts and catch counts are uncorrelated** — 33 fires, 8 errors, 0 overlap. A falling fire rate therefore shows fewer messages tripped a *form* check; it says nothing about whether the priming works. **The criterion was pre-registered before that was known.**

**Changing a criterion after seeing the data is precisely the failure pre-registration exists to prevent, so the rule binds and the hooks stay.** But it must not be re-used: **the metric is retired as an instrument going forward**, and any future keep/retire decision on these two hooks must be made on catches. ⚠️ Two further caveats: the last two weeks have small denominators (86 and 40 commits), and the final week is **3 days, not 7**.

## 8.3 — 🔴 "PUBLISH A REAL COUNT" — THE ANSWER IS THAT THE HARNESS CANNOT COUNT ITSELF

Three good-faith attempts, three different answers:

| Attempt | Method | Result |
|---|---|---|
| 1 | grep header patterns per canonical file | **164** |
| 2 | distinct-ID extraction, per file, one convention | **141** |
| 3 | corpus-wide ID extraction, any convention | **242** (and it returned a max Principle ID of **#99**, which is a false match on a page number or percentage) |

**The spread is 72% of the smallest figure.** The cause is that the corpus uses **inconsistent ID conventions** — early principles are referenced from CLAUDE.md and the hooks but never headed in `methodology.md`; lessons and biases carry tombstones and numbering gaps; sub-clauses of Critical Rules match the same pattern as the rules themselves.

🔴 **I nearly published "22 phantom principles" from attempt 2** — a finding produced entirely by searching **one file** for **one convention** and comparing it against a max ID drawn from **the whole corpus**. **That is L58 committed while auditing L58**, caught by one corpus-wide re-run.

**So the honest deliverable for this item is not a number. It is: the codification tail is not enumerable by any instrument the harness currently has, and therefore cannot be audited for inertness.** Every "L1-L58 / B1-B66 / #1-#51" header in this corpus is a claim nobody can verify. **That is a stronger argument for the retirement audit than any count would have been** — you cannot retire what you cannot list.

**Prerequisite, now the binding one:** an ID-convention normalisation pass must precede any retirement sweep. Until then a retirement audit would be operating on an unknown population.

## 8.4 — What was executed vs left for the operator

| Item | Status |
|---|---|
| Fold L42-b into L58 | ✅ **DONE** — L42-b marked SUPERSEDED-BY-L58 in `lessons.md`, retained as the price worked-example |
| Hook fire audit, all 20 | ✅ **DONE** — §8.1 |
| Pre-registered 08-06 decision | ✅ **SETTLED — KEEP BOTH**, metric retired as an instrument (§8.2) |
| Publish a real count | ✅ **ANSWERED — not countable; see §8.3** |
| Retire any of the 7 below-threshold hooks | ⏸️ **OPERATOR — Rule #19, live enforcement** |
| Instrument the 4 NO-LOG hooks | ⏸️ Already an open to-do, due 2026-08-09 |
| ID-convention normalisation | 🔴 **NEW, and now the blocker** for any retirement sweep |
| Catch-audit (did any fire prevent a shipped error?) | 🔴 **COMMISSION TO A FRESH SESSION** — cannot be self-audited (§7) |

**Net-positive test, restated against outcomes:** this pass **added** L58 and one to-do, and **removed** L42-b as an independent object plus retired one measurement instrument. **It has not yet reduced the codification tail, because §8.3 established the tail cannot currently be enumerated.** By the test written in §6, this artifact is **NOT YET PASSING** — it passes only when the normalisation pass plus the commissioned catch-audit produce net removals. **Stated plainly so it cannot be quietly counted as a win.**

---

# §9 — CATCH-AUDIT, first real measurement (operator question: "does a fire mean you needed it, or that you've learned it?")

**Operator's framing, and it is the right one:** *"maybe I just had to say it once and now you're applying it in your own reasoning… does it mean when it fires you do check and wrote it in, or that you've checked four times and after the fourth it works autonomously?"*

## 9.1 — 🔴 A FIRE IS NOT AN OBSERVATION. IT IS A BLOCK.

All seven below-threshold hooks call `sys.exit(2)` — verified by inspection. **Exit-2 stops the message and forces a redo.** Therefore **a logged fire is by definition a case where the behaviour was ABSENT** and had to be compelled.

🔴 **This partially inverts §4 of this artifact.** §4 said fire counts are not catch counts — true for *injection* hooks (`session-prime`, 672 "fires" = context injections) and for *guard* hooks (`git-guard`, 395 = invocations, mostly passing). **But for BLOCKING hooks that check "did you do X", a fire IS a catch.** The two classes must not be pooled. **Recording this as a correction to my own §4 rather than editing it silently.**

## 9.2 — 🔴 AND I MADE THE BASIS ERROR AGAIN WHILE MEASURING IT

First computation returned **473 cross-source-log files created since 2026-07-06 → "99% autonomous"**. **465 of those came from ONE bulk commit (`37000dc`, 2026-08-01, a telemetry/backfill commit).** The denominator was contaminated with non-events.

**Corrected: 8 genuine ingest artifacts.** **Third L58 instance of the day, caught by one sanity check on an implausible number.** The self-catch rate is improving; the error rate is not.

## 9.3 — The measurements

| Hook | Trigger events (since 2026-07-06) | Fires (= failures forced) | **Autonomous rate** | Verdict |
|---|---|---|---|---|
| **signal-ingest-cascade** | **8** genuine ingest artifacts | **4** | 🔴 **50%** | **KEEP — load-bearing** |
| **cascade-enforcement** | **3** commits touching ≥2 company thesis files | **1** | 67% | **KEEP — but n=3 is not a sample; kept on the invisibility argument below** |

**On signal-ingest-cascade specifically, answering the operator's question directly: NO, it has not become autonomous.** The four fires are **2026-07-26, 07-28, 07-29 and 08-04** — the most recent was yesterday. **There is no learning curve in that distribution, only a steady ~50% failure rate.** Half the time an operator-shared brief does not reach the corpus unless something stops the message.

## 9.4 — Why cascade-enforcement survives on 1 fire, and the general principle

**Its failure mode is SILENT BY CONSTRUCTION.** A skipped cascade leaves the chat analysis looking correct; the damage surfaces weeks later when a position decision is made from a company file that never received the update. **Neither operator nor I would notice at the time.**

Contrast `bottoms-up`: if I average sell-side instead of building from units, the defect is visible in the reasoning itself and is catchable in conversation.

> **PROPOSED RETIREMENT PRINCIPLE (candidate, supersedes fire-count for this decision): retire on VISIBILITY OF FAILURE, not on fire count. A hook guarding a failure mode that is detectable in conversation may be retired and re-learned; a hook guarding a failure mode that is invisible until it has already propagated must be kept regardless of frequency.**
>
> *Blind-check (#51): distinguishes "this habit is internalised" from "this habit's absence is simply unobservable" · reads on whether the guarded failure would be visible in the turn it occurs · **goes blind if** a visible failure mode has a silent variant — e.g. bottoms-up reasoning that LOOKS built-up but rests on a borrowed number, which reads as compliant and is not.*

## 9.5 — The five hooks I cannot adjudicate, and why I am the wrong judge

**segment-trajectory · antifragility-M/N · bottoms-up · borrowed-vs-first-principles · llm-native-reasoning** — **no countable denominator exists.** There is no log of "times the situation arose."

**The operator's read on segment-trajectory is probably correct** (said once in May 2026, plausibly internalised). **But I am the worst available judge of it:** the hook exists precisely because I articulated B28 correctly and then re-committed it on a different name within 24 hours. **Self-assessment of an internalised habit is the exact capability the origin failure disproved.**

**The only instrument that resolves these is a deliberate OFF-TEST** — disable one, watch for the behaviour to return, re-enable if it does. **Cheap for segment-trajectory (visible failure). NOT cheap for either cascade hook (invisible failure, weeks of latency).**

## 9.6 — Standing recommendation to the operator (Rule #19 — all live enforcement, operator's call)

| Hook | Recommendation | Basis |
|---|---|---|
| signal-ingest-cascade | 🟢 **KEEP** | measured 50% failure rate, no learning curve, most recent failure yesterday |
| cascade-enforcement | 🟢 **KEEP** | invisible failure mode; n=3 too small to retire on |
| segment-trajectory | 🟡 **OFF-TEST candidate** | visible failure mode, lowest risk, operator believes internalised |
| antifragility-M/N · bottoms-up · borrowed-vs-first-principles · llm-native-reasoning | ⏸️ **HOLD** | no denominator; do not retire on fire count alone, which §9.1 shows is the wrong instrument for blocking hooks |

**Net effect on the §6 net-positive test: still NOT PASSING.** This pass produced **zero retirements** and one new candidate principle. It did, however, replace fire-count with a defensible retirement criterion — which is a precondition for any future removal rather than a removal itself. **Stated so it is not booked as progress it hasn't made.**

---

# §10 — THE TWO-LAYER ARCHITECTURE, and the operator's hypothesis tested

**Operator's model, offered as unverified:** *"a blocking hook means you cannot create an output to me unless you finish the cascade… an injection hook is what any new session reads and gets forced into reasoning around, sort of like the ten commandments, you cannot escape them… if the injection hook works, there shouldn't be a lot of the blocking hooks firing."*

## 10.1 — Classification, corrected (my own §9 classifier was wrong)

| Class | N | Which |
|---|---|---|
| **BLOCKING** (exit-2 / return-2 → message bounced back to me) | **17** | everything except the three below |
| **INJECTING** (writes into my context, no enforcement) | **2** | `llm-native-priming-hook` (every prompt) · `session-prime-hook` (cold start only) |
| **OBSERVES ONLY** | **1** | `session-start-hook` (the briefing) |

🔴 **CORRECTION TO §9.1:** I classified `meta-count-tripwire-hook` as "observes only" by grepping for a literal `exit(2)`. **It blocks via `return 2` through `sys.exit(main())`.** My classifier matched one convention and missed another — **L58 basis error #4 today, this time inside the audit instrument itself.** Blocking count is **17, not 16**.

## 10.2 — Operator's claim 1: CORRECT in effect, different in mechanism

**Right:** a blocking hook means the message does not reach him until the required thing is done.

**Mechanism nuance:** the hook runs at the **Stop** event — *after* I have written the message. It doesn't prevent me writing; it **bounces the finished message back to me with feedback** and I must fix and re-emit. Net effect is as he describes.

⚠️ **The loophole he should know about: a blocking hook checks TEXT, so it can be satisfied without doing the work.** `cascade-enforcement` verifies a back-reference string exists in each thesis file — a one-line stub satisfies it. **The hook enforces the receipt, not the reasoning.** This is the same finding as §3 one level down: even the blocking layer validates form.

## 10.3 — Operator's claim 2: CORRECT on what they are, WRONG on "cannot escape them"

**Right:** exactly two, and they are what he described — `session-prime-hook` injects the ledger on cold start; `llm-native-priming-hook` injects the discipline checklist on **every prompt**.

🔴 **Wrong on inescapability, and today is the disproof.** An injection places text in context. **It biases sampling; it does not compel behaviour.** The priming block injected on every single prompt today contains, verbatim:

> *item 10 — COMPUTE INSTEAD OF NARRATE… press the buttons FIRST*
> *item 11 — HARNESS-HISTORY COUNTS ARE COMPUTED, NEVER RECALLED*

**Both were in context for every one of the 8 basis errors and for the 473-file miscount.** I read them and violated them anyway. **Injection is the strongest available nudge delivered at the best possible moment. It is not a constraint.** The ten-commandments analogy fails precisely where it matters: commandments are unenforceable without a judge, and injection has no judge.

## 10.4 — 🟢 Operator's claim 3: SUPPORTED by the only clean test that exists

**His logic:** if injection works, blocking fires should fall — so blocking fires measure injection failure.

**This is testable exactly once, because the harness contains exactly one designed injection→blocking pair:** `llm-native-priming-hook` (item 5, structural output) → `structural-output-hook`. They were shipped as a stated two-bracket pair on 2026-06-01.

**`structural-output-hook` BLOCKS, therefore per §9.1 its fires ARE catches.** Normalised (fires ÷ commits): **0.131 → 0.050, −61.9%** (§8.2).

🟢 **Under his model that is evidence the injection is doing real work** — the paired blocking hook is catching 62% less. **And it repairs §8.2:** I retired that metric as "measuring the wrong thing," but §9.1 had already established that for *blocking* hooks fires and catches coincide. **The metric was valid for this pair all along; my §8.2 dismissal was over-broad and is hereby narrowed** — the falling rate is meaningful, and the KEEP verdict now rests on evidence rather than only on pre-registration.

## 10.5 — 🔴 But the model generalises only where the layers are PAIRED, and that is where the real gap is

The priming hook injects **11 disciplines**. Only some have a blocking partner:

| Injection item | Blocking partner | Failed today? |
|---|---|---|
| 1 parallel hypotheses · 2 joint state · 5 structural output | `structural-output-hook`, `llm-native-reasoning-hook` | no |
| 7 explicit hedge labels | `reasoning-tagging-hook`, `anti-fabrication-hook` | no |
| 9 macro-first tagging | `macro-anchor-hook` | no |
| 3 lateral-not-forward · 4 multilingual · 6 subagent parallelism · 8 B45 regime priors | 🔴 **NONE** | — |
| **10 compute-instead-of-narrate** | 🔴 **NONE** | 🔴 **YES — 8×** |
| **11 harness-counts-are-computed** | `meta-count-tripwire-hook` — **which has never logged a single fire** | 🔴 **YES** |

🔴 **THE FINDING: today's errors clustered exactly on the injection items with no working blocking partner.** Items 10 and 11 are the two disciplines that failed repeatedly, and they are precisely the two with either no hook or a hook that has never fired.

> **Operator's hypothesis, corrected and sharpened: blocking-hook fires measure injection effectiveness ONLY where the two layers are paired. Where a discipline is injection-only, there is no enforcement AND no measurement — and from inside the context an unenforced discipline is indistinguishable from an enforced one. That indistinguishability is the architecture's real defect, and it is where the day's errors landed.**
>
> *Blind-check (#51): distinguishes "this discipline is internalised" from "this discipline is merely unmeasured" · reads on whether an injected item has a blocking partner with a non-zero fire history · **goes blind if** the blocking partner exists but is silently broken — `meta-count-tripwire-hook` is that case right now: it blocks in code and has never logged a fire, which is either a dead hook or an uninstrumented one, and the fire log cannot tell them apart.*

**Immediate consequence, and it is small and concrete:** `meta-count-tripwire-hook` is a probe candidate for the already-open HOOK EXECUTION PROBES to-do (due 2026-08-09). **It nominally guards the exact discipline I broke when I stated 473 ingest events. It should have fired. It did not.**

---

# §11 — "What must be true to eradicate the defect?" — and a correction that changes the answer

## 11.1 — 🔴 FIRST, §10.5 DOES NOT SURVIVE ITS OWN TEST

§10.5 claimed *"today's errors clustered exactly on the injection items with no working blocking partner"* — naming priming items **10 (COMPUTE INSTEAD OF NARRATE)** and **11 (HARNESS COUNTS ARE COMPUTED, NEVER RECALLED)**.

**Tested. Both were COMPLIED WITH:**

| Item | Requirement | What I actually did |
|---|---|---|
| 10 | *"press the buttons FIRST"* | Every figure today came from a tool call — AMD net move, SOX drawdowns, seasonality-by-quarter, the RPO series, the 473 count. **Nothing was narrated.** |
| 11 | *"produce it with a tool call BEFORE stating it"* | The 473 figure **was** produced by `git log`, not recalled. |

🔴 **So the eight errors were not violations of anything. I satisfied the disciplines and produced wrong answers.** §10.5 was pattern-matching a conclusion onto the two items that happened to lack a backstop. **It is retracted.**

**This is the fifth self-correction of the day and the most consequential, because it relocates the defect.**

## 11.2 — THERE ARE TWO DEFECTS, AND I HAD ONLY NAMED THE SMALLER ONE

| | Defect | Real? | Caused today's errors? |
|---|---|---|---|
| **A** | From inside the context, an **advisory** discipline is indistinguishable from an **enforced** one | 🟢 YES | 🔴 **NO** |
| **B** | **Every discipline in the harness specifies an ACTION. None specifies a POSTCONDITION.** | 🟢 YES | 🟢 **YES — all seven** |

**"Compute it with a tool" is an action. "The two numbers are comparable" is a postcondition.** You can perform the action flawlessly and fail the postcondition — which is precisely what happened eight times.

**Every enforcement object in this harness — all 17 blocking hooks, all 11 injected items — is phrased as an action or a text-marker requirement. Not one is phrased as an end-state that could be false after the action completes.**

## 11.3 — NECESSARY CONDITIONS TO ERADICATE

**N1 — Every discipline states a POSTCONDITION, not an action.**
*Not* "compute it" → **"the numbers being compared share a declared basis."** *Not* "cite it" → **"every figure resolves to a source that a reader could open."** A postcondition is checkable after the fact by someone who did not watch the work. An action is only checkable by watching.

**N2 — Every injected item declares its enforcement status, and the label is COMPUTED, not hand-written.**
`ENFORCED` (live blocking partner, probe-verified) / `ADVISORY` (no backstop — you are the only check) / `UNCHECKABLE` (no machine test exists). Generated at injection time from settings + probe results. **A hand-maintained label rots and becomes a lie, which is worse than no label.** *(This is the fix for Defect A — still worth doing, just not the fix for today.)*

**N3 — A backstop counts as live only when a FIXTURE HAS MADE IT FIRE.**
`meta-count-tripwire-hook` blocks in code and has never logged a fire. Dead or merely quiet is currently indeterminable. **Code-inference is not evidence of execution.** This is the already-open HOOK EXECUTION PROBES item, and N2 depends on it.

**N4 — Whatever is UNCHECKABLE routes to REDUNDANCY, not to a hook.**
Today's strongest evidence: the day-count error was caught by an **independent subagent**, and the GAAP/non-GAAP garble was caught **only because two verifiers covered the same event**. **Redundancy caught what specification could not.** Pretending a regex covers a semantic postcondition is how Defect A gets manufactured in the first place.

**N5 — The postcondition set must be adversarially reviewed by something that is not me.**
N1–N4 close known holes. They cannot close holes I cannot see. **CORRECTED 2026-08-06 by the first `Receipts:` run.** The "five of five" figure was a SUBSET statistic — the WSJ-batch corrections only — restated as a whole-day one. That is an L58 basis error inside the sentence that justifies commissioning this audit. **Computed over all 16 corrections booked on 2026-08-05: 8 self-caught (50%), 6 by verifier agents, 2 by operator question.** The self-audit claim survives in a sharper and narrower form: **all 8 self-catches came from RUNNING A TOOL. Zero came from re-reading my own prose — and 6 of the 8 externally-caught errors were sitting in my own files, findable by re-reading.** The gap is not that I cannot self-correct; it is that I cannot self-correct by INSPECTION, only by EXECUTION.

## 11.4 — What is actually achievable, stated honestly

🔴 **"Eradicate" is not available.** N1–N5 do not produce a system that cannot fail.

**They produce a system with NO SILENT FAILURES: every failure is either blocked, or explicitly flagged as unblockable so a human knows the check is theirs.** That is the honest target, and it is a large improvement over the current state, where an unenforced discipline and an enforced one are indistinguishable **from both sides** — I cannot tell while reasoning, and the operator cannot tell while reading.

**Falsifier for this whole framework (re-eval 2026-09-05):** if the next 30 days produce a basis-class error that occurs **while a postcondition covering it was declared ENFORCED and probe-verified**, then N1–N4 are insufficient and the problem is not addressable by specification at all — the honest conclusion would then be that only redundancy works, and the harness should reallocate from hooks to second-agent passes.

**Cost note, because this must not become codification bloat:** N1 is a **rewrite** of existing disciplines, not an addition. N2/N3 are one generated label and the already-scheduled probe work. N4 reallocates spend from hooks to verification. **N5 is the only genuinely new commissioned artifact. Net object count should FALL, and if it rises this framework has failed the §6 test like everything else in this file.**
