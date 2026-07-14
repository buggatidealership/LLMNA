# FIX SPEC — session-prime-cascade-hook.py (root cause DIAGNOSED 2026-07-14, fix not yet applied)

**Status:** ~~OPEN~~ → **APPLIED 2026-07-14 EVE, same session** (user: "do you want to fix it?"). v2 rebuilt
on ID-set-diff design (added-IDs − removed-IDs; supersedes the "loosen regexes" requirement below with
something strictly stronger — it also kills the edit/promotion FP class the original patterns couldn't).
Results at apply time: `--selftest` 21/21 real-corpus fixtures; 30-day backtest 42 true fires (incl.
f6ce2d5 #45, f500a4d static-collapse lesson, bda9df9 rules-patterns candidate, the full Jul-9→12 origin
batch, back through B47 Jun-14), 5 correctly suppressed (session-prime co-committed), FP ≤2.5% (one
borderline TC-14 promotion-into-table); live fire path exit 2 + telemetry line 2026-07-14 21:30:09Z in
hook-fire-log.md; suppression path exit 0; fail-open preserved. Scope extended: pattern-register now
canonical. **INDEPENDENT VERIFICATION PENDING** — run `session-prime-cascade-hook-fix-verification-prompt.md`
in a fresh session; do not mark this closed until that verdict is VERIFIED.
**Todo pointer:** `meta/todo.md` P2/process entry "session-prime-cascade-hook fix".
**The miss it must prevent recurring:** 2026-07-14 shipped Principle #45, B64-referencing tail syncs, and 2 candidate lessons across canonical files in 26 commits — the hook fired ZERO times, and `session-prime.md` went stale at Jul-13 until caught manually at session close (commit 7836719). This is the exact staleness class the hook was built (2026-07-12) to catch.

## Diagnosis (computed, not inferred)

**Reproduction:** re-ran the hook's own `PATTERNS` over `git show -U0 <sha> -- <CANONICAL>` for all 26 commits of 2026-07-14: **0 pattern hits** across every commit, including f6ce2d5 (Principle #45 added to `methodology.md`).

**Defect 1 — regex adjacency bug (the miss).** Pattern
`^\+\s*#{2,4}\s+(?:Principle\s+)?#\d+\s+[—-]` demands the dash IMMEDIATELY
after the ID. Actual house header format puts an annotation between ID and dash:

```
+## Principle #45 candidate (added 2026-07-14 per user question "...") — EVENT-ANCHORED...
```

Regex walks `## Principle #45 ` then requires `[—-]` but meets `c` of
"candidate" → no match. The B/TC/L patterns share the same `ID\s+[—-]`
adjacency assumption and are presumptively wrong the same way — VERIFY each
against real headers (e.g. B64's actual header in `biases-watchlist.md`,
added 2026-07-13) during the fix.

**Defect 2 — zero telemetry (the unverifiability).** The hook writes nothing
to `meta/hook-fire-log.md` (contrast `session-prime-hook.py`'s `log_fire()`).
"Ran and passed" vs "crashed fail-open" vs "never invoked" are
indistinguishable, so its own pre-registered falsifier ("if 30 days show zero
fires…", docstring, re-eval 2026-08-12) is unverifiable as written.

**Confirmed NOT the cause:** binding is fine — `.claude/settings.json` binds it
on `Stop` with empty matcher; sibling Stop hooks fired all day per
hook-fire-log. It ran; it just matched nothing.

## Fix requirements

1. **Loosen patterns to house format.** Allow bounded annotation between ID
   and dash, e.g. `^\+\s*#{2,4}\s+(?:Principle\s+)?#\d+\b[^\n]{0,120}[—-]`
   (same treatment for B\d+ / TC-\d+ / L\d+ / Critical-Rule patterns). Keep
   the reference-vs-entry discrimination: counter bumps and prose mentions
   (e.g. CLAUDE.md `#1-#44 → #1-#45`, tags.md tail lines) must still NOT fire
   — those correctly passed on 2026-07-14 and must keep passing.
2. **Add telemetry.** Port `log_fire()` from `session-prime-hook.py`. Log
   POSITIVE fires and caught EXCEPTIONS always; do NOT log clean passes
   (Stop fires every turn — that would spam the log; the falsifier can then
   read "zero LOGGED fires = zero positives OR silent non-invocation", and
   non-invocation is now checkable via sibling-hook log entries).
3. **Decide + document the candidate policy.** House convention adds new
   principles/lessons as `… candidate (added DATE …)` headers. Per the hook's
   origin intent (any new codification ID shipping without a session-prime
   touch = staleness), candidates SHOULD fire. If the fixer decides otherwise,
   document the exclusion in the docstring and add a promotion-time trigger
   instead. Recommendation: fire on candidates.
4. **Backtest before declaring fixed.** Run the fixed patterns over the last
   30 days of history (same reproduction loop, `git log --since`), compute:
   (a) would-have-fired set — must include f6ce2d5 and the Jul-9→12 origin
   batches; (b) false-positive rate over non-codification commits — docstring
   threshold <30%. Book the numbers in the commit message.
5. **Tests:** `python3 session-prime-cascade-hook.py < /dev/null` → exit 0
   (fail-open preserved). Synthetic positive: unstaged edit adding
   `## Principle #99 candidate (added 2026-01-01 test) — X` to
   `methodology.md` WITHOUT touching session-prime.md → exit 2 with the
   stderr message; same edit WITH a session-prime.md touch → exit 0. Revert
   the synthetic edit after.
6. **Update the docstring falsifier** (date + terms) after the fix so the
   2026-08-12 re-eval grades the fixed version, not the dead one.

## Reproduction script (paste-ready)

```python
import re, subprocess
CANONICAL = ["research/meta/biases-watchlist.md","research/predictions/lessons.md",
             "research/meta/methodology.md","research/CLAUDE.md","research/signals/triangulation.md"]
PATTERNS = [...]  # copy live list from the hook under test
commits = subprocess.run(["git","log","--since=30 days","--format=%h %s"],
                         capture_output=True,text=True).stdout.strip().splitlines()
for line in commits:
    sha, subj = line.split(" ",1)
    out = subprocess.run(["git","show","-U0","--format=",sha,"--",*CANONICAL],
                         capture_output=True,text=True).stdout
    added = [l for l in out.splitlines() if l.startswith("+") and not l.startswith("+++")]
    hits = [l for l in added if any(p.match(l) for p in PATTERNS)]
    if hits: print(sha, subj[:60], "->", len(hits), "hits")
```
