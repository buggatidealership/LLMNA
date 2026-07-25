# VERIFICATION PROMPT — session-prime-cascade-hook v2 fix (pre-registered 2026-07-14 EVE by the fixing session)

You are verifying that the 2026-07-14 rebuild of
`research/meta/hooks/session-prime-cascade-hook.py` is the fix that was
*expected* — not merely a fix that *claims* to work.

## Epistemic stance (binding)

1. **ADVERSARIAL, NOT CONFIRMATORY (Critical Rule #18).** Your job is to
   REFUTE the fix. The fixing session wrote this prompt, the fix, the spec,
   AND the commit messages — treat every claim in all four as a
   pre-registration to test, never as evidence. B63 model-provenance applies:
   you share a lineage with the author; weight the refutation search at full
   effort.
2. **COMPUTE, DON'T NARRATE (Principle #43b).** Every gate below resolves by
   executing code against the repo. If you catch yourself writing "the
   backtest confirms…" without having just run the backtest, stop and run it.
3. **PARALLEL FAILURE HYPOTHESES.** Before running anything, hold these
   simultaneously and let the gates discriminate (priors = fixing session's
   model, for you to update): H1 fix correct as pre-registered (P~70%);
   H2 fix works on fixtures but the backtest anchors were cherry-picked /
   history has misses the fixing session never enumerated (P~15%);
   H3 fix over-fires in live operation — FP classes the 30-day window
   under-samples (P~10%); H4 wiring/telemetry defect — detection is right but
   the Stop-event integration or logging is broken (P~5%).

## Pre-registered expected observables (the "expected fix" being tested)

Every value below was committed BEFORE this verification runs (tamper-evident
via git history — check the commit date of this file if suspicious).

**GATE 1 — selftest.**
`python3 research/meta/hooks/session-prime-cascade-hook.py --selftest`
Expected: exit 0, output `selftest OK — 21/21 fixtures pass`.
Then READ the fixtures: confirm they are real corpus shapes (spot-check ≥3
against the live files they claim to be harvested from), not strawmen.

**GATE 2 — clean pass + fail-open.**
On a clean tree: `python3 <hook> < /dev/null` → exit 0, silent, and NO new
line appended to `meta/hook-fire-log.md` (clean passes are unlogged by
design). Then break something (e.g. run with `git` shadowed to a failing
stub, or temporarily rename `.git`) → still exit 0, with an ERROR line
logged. Restore.

**GATE 3 — independent backtest (do NOT reuse the fixing session's script
output; re-derive).** Import `parse_diff_keys` + `CANONICAL` from the hook,
loop `git log --since="2026-06-14" --until="2026-07-15" --format=%h`, per
commit run the detection over `git show -U0 --format= <sha> -- <canonical>`,
split fired vs suppressed on session-prime presence in the commit's files.
- MUST-FIRE anchors (hard gate, all required): `f6ce2d5` (Principle #45 —
  the original miss), `f500a4d`, `bda9df9`, `4c5d57c`, `62d08e4`, `64106b3`,
  `4033771` (B63), `aa5c34e` (PC-17), `2c30ad8` (TC-16), `dc74ee0` (TC-15),
  `fe7701f` (L30), `bd4c0a9` (B58,B59).
- MUST-SUPPRESS anchors (session-prime co-committed): `58563ab` (B64),
  `c2db0a1` (RULE-17,RULE-18), `bbf0359`, `c27a988`, `428ac1f`.
- Expected totals for that exact window: fired=42, suppressed=5. Small
  drift is tolerable only if explained; anchor misses are not.
- FP adjudication: read ALL fired commit subjects (and diffs where unclear).
  Pre-registered claim: ≥70% genuine new codifications required, ~97%
  claimed (1 borderline: `9fc82f9` TC-14 promotion-into-table). Recount
  independently.

**GATE 4 — live end-to-end.**
Append a synthetic header to `research/meta/methodology.md`:
`## Principle #98 candidate (added 2026-01-01 VERIFY-TEST) — synthetic, revert`
Run the hook → expected exit 2, stderr contains `SESSION-PRIME CASCADE
INCOMPLETE` and the `METH::` key, and a new FIRE line lands in
hook-fire-log.md. Then `echo >> research/meta/session-prime.md`, rerun →
exit 0. `git checkout --` both files. NOTE: a FIRE line stamped
`2026-07-14 21:30:09Z … Principle #99 … SYNTHETIC-TEST` already exists —
that is the fixing session's own live test (expected evidence, not
contamination); yours will be a second, distinct line.

**GATE 5 — blind-spot hunt (lateral, not forward).** Ask: "what world-state
makes this hook silent while session-prime goes stale anyway?" Construct ≥3
NOVEL header shapes a plausible near-term codification might use and test
them via `parse_diff_keys` fixtures. Pre-registered KNOWN false-negative
classes (confirm they're documented in the docstring, then judge severity):
(a) new-entry titles containing EXCLUDE words (update/ENRICHMENT/…);
(b) body-line annotations under existing sections (57cffd5 shape — by
design); (c) codifications living OUTSIDE the 6 canonical files (tags.md,
instrument files, new file types — scope question, not regex question);
(d) a reworded existing header (METH text-key → one-time FP, documented).
If you find an UNDOCUMENTED evasion shape that is realistically imminent,
that is a PARTIAL verdict and a follow-up todo item.

**GATE 6 — wiring + docs coherence.** `.claude/settings.json` still binds
the hook under the `Stop` event (empty matcher). CLAUDE.md's enforcement-
hooks bullet describes v2 (ID-set diff, 2026-08-14 falsifier), not v1.
Docstring falsifier date = 2026-08-14. Fix-spec status = APPLIED with
verification PENDING (you will flip it).

## Output contract (structural, Critical Rule #18 + house format)

1. Joint gate table: gate | pre-registered expectation | observed (computed)
   | PASS/FAIL.
2. Verdict: **VERIFIED** (all gates pass; anchors exact) / **PARTIAL**
   (gates pass but an undocumented blind spot or anchor drift found) /
   **REFUTED** (any must-fire anchor missed, FP recount >30%, or live paths
   wrong). State which of H1–H4 the evidence selected, with your posterior.
3. On VERIFIED: flip fix-spec status to VERIFIED (date + your session),
   delete/close the todo entry, book a short verification artifact in
   `signals/cross-source-log/` (house naming), commit + push.
4. On PARTIAL/REFUTED: do NOT silently repair beyond mechanical fixes —
   book findings, update the todo entry with the failure evidence, commit +
   push, and surface to the user with the failing gate's raw output.
5. Everything you assert about the fix must trace to a command you ran in
   THIS session. The verdict line must carry 🟢 with the gate table as its
   receipt.
