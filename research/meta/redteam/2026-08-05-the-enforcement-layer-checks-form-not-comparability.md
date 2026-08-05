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
