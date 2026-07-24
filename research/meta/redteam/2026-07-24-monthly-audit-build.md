# 2026-07-24 — Monthly audit build (scheduled wake, self-set 2026-07-20)

Executed the two DUE harness items + four same-audit measurement tasks. Governance:
the B47 hook is a LIVE-enforcement change → **spec-then-review, NOT shipped** (Rule
#19 HIGH; both B47 instances externally caught → author-blind by construction).

---

## 1. Fire-logging HOUSE STANDARD ✅ SHIPPED (commit 3805eb9)

- NEW `meta/hooks/hook_fire_log.py` — shared house-format logger: fail-open (never
  raises → cannot change a hook's exit code), detail sanitize (newline-collapse +
  300-char cap), probe-aware (`LLMNA_PROBE`), `--selftest` (7 checks) /
  `--clock-check` / `--rotate` CLI.
- Wired the **11 previously-silent Stop hooks** (block messages died with the
  container — origin: fresh-Claude "what's missing" #1) to `_log_fire` before
  `exit(2)` via a fail-open import shim.
- **Zero enforcement drift, verified:** full suite unchanged (framework 198/200 =
  same two known-RED todo content-couplings; structural-output tier-gate + both
  git-guard suites ALL PASS). 5 wired hooks with block-path test cases fired +
  logged in house format (probe=1).
- **Migration decision (flagged, Rule #19):** the 7 already-logging hooks were
  deliberately NOT re-pointed — cosmetic consolidation of author-blind enforcement
  paths is net-negative risk (format-drift could break the 08-06 metric). Documented
  in `meta/hooks/FIRE-LOGGING-HOUSE-STANDARD.md`.
- **Rotation/cap policy:** append-only through the 2026-08-06 structural-output
  decision; `rotate_fire_log(retention_days=45)` archives only entries older than
  the horizon (metric-safe); `structural-output-metric.py` made archive-aware
  (byte-identical today — verified FALLING 0.120→0.102 before & after).
- **Clock-source cross-check (first reading):** container 06:37Z vs last commit
  00:35Z, delta ~6h = OK (<1 day). No clock-drift concern this month.

## 2. B47 efficiency-claim hook — ✅ SPEC WRITTEN, ⛔ NOT SHIPPED (review-gated)

`meta/hooks/b47-efficiency-claim-hook-SPEC.md`. Trigger = X-times / %-gain
efficiency/power/cost-per-unit claim in a substantial output WITHOUT a
U8/B47/Jevons/demand-side reference. Both real misses (I1 per-wafer-profitability;
I2 "6-10x tokens per unit power" missing-ENERGY-leg) are mandatory regression
fixtures. **The decisive author-blind fact, surfaced in the spec:** I2 contained no
word "efficiency" — a trigger keyed on that word misses its own motivating case.
Four review-grade questions routed to K3 + a fresh-session pass (§6), the sharpest
being **Q4: is a text-scanning Stop hook structurally able to catch a MISSING-LEG
failure at all** (the leg was never run → the sentence was never written → a Stop
hook can't see an absence)? If review answers "wrong layer," the enforcement moves
to INGEST-orchestration, not a Stop hook. Interim step-4b tripwire remains LIVE.

## 3. B47 promotion decision (N=2) ✅ CONFIRMED-SPLIT

`biases-watchlist.md` B47: CANDIDATE → **CONFIRMED-SPLIT**. The blind spot is
empirically real at N=2 (two distinct genuine misses) → promote the *bias-exists*
claim. BUT (anti-laundering, self-analysis item 5): both were caught EXTERNALLY →
self-detection is UNPROVEN. Self-detection falsifier registered: the NEXT B47
instance must be self/step-4b/hook-caught, not external, or the mitigation is theater
and escalates to INGEST-orchestration enforcement.

## 4. B65 canary + avoidance (first run) ✅

- **Canary: GREEN.** Seeded ungrounded unusual-precision fabrications (73,914 wafers;
  $84,617,203) in a scratchpad transcript (outside the grounding corpus, amendment i)
  → anti-fab hook exit=2, caught both. Hook liveness confirmed. (First attempt
  exit=0 was a TEST-construction error — message <200-char size gate — not hook
  blindness; corrected and re-run. Logged honestly.) Needle lands only in
  hook-fire-log.md, which is grounding-excluded → no corpus contamination.
- **Avoidance audit: PARTIAL-CLEAN.** Scan of commits since 07-20 + recent
  day-state/cross-source surfaced no un-computed harness-state count claims that
  should have fired. Honest caveat: the sample is commits + artifacts, NOT the full
  session message stream (ephemeral) → this is a partial audit (self-analysis item 7).

## 5. Verdict-flip sampling ✅ (with a structural finding)

8 anti-fab `verdict:pending` FIRE lines + 4 INCONCLUSIVE in the log. Post-hoc
grounding: 7/8 distinct numbers now in the corpus (€28B, $50.1M, $4.3M, $750B,
$1.65T, 194GW) = the block drove the citation → **hook working as intended**;
`$115B` still ungrounded (candidate true-fire rephrased-not-filed). **Structural
finding:** the TRUE-FIRE/FALSE-POSITIVE flip needs the ORIGINAL message, and
cross-session transcripts are ephemeral → historical pending verdicts can only be
post-hoc-grounded (weaker), not transcript-adjudicated. The durable fire-log line +
embedded needle is the best available evidence going forward; same-session flips are
fully adjudicable, cross-session ones are not. (Noted for the receipts-hook scope.)

## 6. Curation-ratio first reading (K3 dissent #1) ✅

30-day window (2026-06-24→07-24), 940 commits. Pure auto-telemetry chores = 69
(7.3%), excluded. Of 871 substantive commits: maintenance-only 35.5%, research-only
27.3%, mixed 8.2%, neither 29.0%. **CURATION RATIO (maint/(maint+research)) = 56.5%.**
Maintenance modestly exceeds research — the production-bias / "meta-work as comfort
work" concern (self-analysis item 4). Caveat: this window contains the heavy
07-20→24 harness-audit push, which skews maintenance up. **Falsifier:** sustained
>60% month-over-month = the harness is eating itself → force a research-only cadence
or prune. First reading is a baseline, not yet a verdict.

---

## Remaining (NOT in this wake's two-item scope; carried)
- Prose-deadline extractor wiring into session-start-hook + parser coverage tests
  (listed in the fire-logging todo bullet but separate build).
- Receipts Hook Phase 1 (say-do gap) — build 07-24/08-03 per its own spec.
- B47 hook: awaits K3 + fresh-session review before any ship.
- The two known-RED framework tests (todo content-couplings) — re-scope to durable
  anchors (audit item 6 from the P0 remaining scope).
