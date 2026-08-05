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
