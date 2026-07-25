# B47 efficiency-claim Stop hook — DESIGN SPEC (⚠️ NOT SHIPPED — review-gated)

**Status: SPEC ONLY. Do NOT wire into `.claude/settings.json`.** This is a LIVE
enforcement change → Rule #19 HIGH tier, and — decisively — **both B47 instances
were caught externally (user 2026-06-14, K3 2026-07-20), so this hook is designed
by the very process that owns the blind spot.** Author-blind by construction. It
ships only after the review-grade process below (K3 + a fresh-session pass routed
through the operator) clears the slip-past questions in §6. Codified 2026-07-24
monthly audit, per the todo DUE item.

Interim mitigation ALREADY LIVE (do not remove): CLAUDE.md INGEST **step 4b**
(efficiency-claim tripwire, 2026-07-20) + `sector/bottlenecks.md` B47/U8
falsifier-side ledger routing.

---

## 1. What the hook must catch (the two real misses = mandatory fixtures)

| # | Date | The claim, as actually phrased | What was skipped | Caught by |
|---|---|---|---|---|
| I1 | 2026-06-14 | "DDR5 RDIMM surpassed HBM in per-wafer profitability" + the token-cost-elasticity frame | no demand-side U8 falsifier existed | user |
| I2 | 2026-07-20 | Google Frozen v2: **"6-10x tokens per unit power"** — cascaded silicon/memory/ASIC legs, **never ran the ENERGY leg** despite TC-13 grid-hardware = co-#1 binding constraint | U8/B47 ledger line | K3 |

The decisive design fact: I2 did **not** contain the word "efficiency." It said
"tokens per unit power." A trigger keyed on the word *efficiency* would have
missed the very instance that motivated the hook. **This is the author-blind trap
in concrete form** and the primary thing review must stress.

## 2. Trigger (fires the block) — proposed regex families

Fire only on a **substantial analytical / INGEST output** (len ≥ 800, same size
gate as structural-output-hook) that contains an efficiency/power/cost-per-unit
gain claim AND lacks the pass reference (§3).

Family A — multiplicative gains:
`\b\d+(?:\.\d+)?\s*[-–]?\s*(?:to|-)?\s*\d*\s*[x×]\b` **within ~60 chars of** a
unit-efficiency noun: `token`, `tokens?[ -]per[ -](?:watt|joule|dollar|unit\s+power)`,
`per[ -]unit[ -](?:power|energy|cost)`, `perf(?:ormance)?[ -]?/?[ -]?watt`,
`cost[ -]per[ -]token`, `energy[ -]per`, `throughput[ -]per[ -]watt`.

Family B — percentage gains: `\b\d{1,3}\s*%\s*(?:lower|less|reduction|cheaper|
more efficient|improvement)\b` within ~60 chars of the same unit-efficiency nouns.

Family C — explicit efficiency vocabulary: `\b(?:efficiency|perf/W|tokens?[ -]per[ -]watt|
energy[ -]efficiency|power[ -]efficiency)\b` combined with a magnitude token
(`\d+[x×]`, `\d+%`, `order of magnitude`, `\d+[ -]?fold`).

**Union A∪B∪C**, each requiring proximity to a unit-efficiency anchor so bare
percentages ("revenue +40%") don't trip it.

## 3. Pass / exemption conditions (does NOT fire)

Passes if the SAME message already contains a falsifier-side reference:
`\bU8\b`, `\bB47\b`, `\bJevons\b`, `demand[- ]destruction`, `demand[- ]side`,
`efficiency[- ]compression`, `elasticity`, `falsifier-side`, `Frozen v2`(as a
back-ref), OR an explicit routed line to `sector/bottlenecks.md` /
`grid-hardware` / `ENERGY leg`.

Hard exemptions (never fire): harness-meta (`hook`, `principle #`, `.py`,
`settings.json`, `SPEC`), Q&A/restatement, and the standard structural-output
exemption set. **Open question for review:** the exemption list is where I would
naturally hide my own blind spot — see §6.

## 4. Placement + form

- Stop hook, sibling to `structural-output-hook.py`, fail-open, logs via the new
  `hook_fire_log` house standard (`b47-efficiency-claim-hook FIRE (detail)`).
- Exit 2 with feedback: *"Efficiency/power/cost-per-unit gain claim detected
  without a U8/B47/Jevons/demand-side reference. INGEST step 4b: route one line
  to the B47/U8 falsifier-side ledger (sector/bottlenecks.md) — the
  demand-destruction read for the affected bottleneck — before completing the
  cascade, even if the verdict is 'Jevons-dominated, fractional.'"*

## 5. Regression fixtures (MUST pass before ship)

Positive (must BLOCK): I1 phrasing; I2 phrasing ("6-10x tokens per unit power");
"3× better perf/watt"; "40% lower cost per token"; "an order-of-magnitude
improvement in tokens per joule."
Negative (must PASS — no fire): the same claims WITH a U8/B47/Jevons line;
"revenue grew 40%"; "the stock is up 3x"; "10× oversubscribed"; a harness-meta
turn discussing the hook; a GDP/traffic "1500-2000×" historical-analog line that
already sits inside a demand-side discussion.

## 6. Review-grade questions (author-blind — I cannot self-clear these)

Route to K3 + one fresh-session pass (blind, given only §1 + a corpus sample):
1. **Slip-past hunt:** produce 5 real-world efficiency-claim phrasings a
   Frozen-v2-class INGEST could use that A∪B∪C would MISS. (I2 already proves the
   word "efficiency" is absent in the wild — what else is?)
2. **False-positive load:** over the last 30 days of analytical commits, how many
   times would this have fired, and what fraction are legitimate (already had the
   ledger line vs genuinely forgot)? A hook that fires on every AI-efficiency
   sentence is noise and will be muted.
3. **Exemption capture:** does any proposed exemption (esp. harness-meta) create a
   hole an INGEST could fall through by co-mentioning a hook/principle?
4. **Right layer?** Is a Stop hook the right enforcement, or does the miss live at
   the *cascade-completeness* layer (the leg was never run) rather than the
   *output-text* layer (a Stop hook only sees final text — it cannot see that the
   ENERGY subagent was never fired)? **This is the deepest doubt:** I2 was a
   MISSING-LEG failure, and a text-scanning Stop hook may be structurally unable
   to catch a missing leg if the author simply never writes the sentence. If so,
   the correct enforcement is at INGEST-orchestration, not Stop — and the hook is
   theater. Review must adjudicate this before any ship.

## 7. Falsifier + re-eval (post-ship, if it ships)

- Re-eval 30 days after ship: fires ≥1× on a genuine miss self-caught (not
  external) → validated. Zero fires + a new external B47 catch → the trigger has
  the same blind spot as its author (§6 Q1 failed) → rebuild or abandon.
- FP rate > 30% legitimate-efficiency-sentences → tighten anchors or retire.
- If review answers §6 Q4 "wrong layer," this spec is superseded by an
  INGEST-orchestration checklist gate, not a Stop hook.
