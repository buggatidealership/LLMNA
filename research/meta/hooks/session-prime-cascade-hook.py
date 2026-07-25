#!/usr/bin/env python3
import os as _os
from pathlib import Path as _Path
_REPO_ROOT = _os.environ.get("CLAUDE_PROJECT_DIR") or str(_Path(__file__).resolve().parents[3])
"""
Session-prime cascade Stop hook.

v1 built 2026-07-12 (escalation pre-registered in the 2026-07-12 session-prime
effectiveness audit + session-prime.md §10).
v2 REBUILT 2026-07-14 after diagnosis proved v1 was DEAD ON ARRIVAL: its
regexes required a dash immediately after the codification ID ("#45 —") but no
real house header has that shape ("## Principle #45 candidate (added DATE …) —",
"### B61 CANDIDATE (…): …", "| **TC-18** …" table rows). Reproduction over all
26 commits of 2026-07-14: zero hits, including f6ce2d5 (Principle #45). Full
diagnosis: meta/hooks/session-prime-cascade-hook-fix-spec.md.

CHARTER (unchanged): every changeset that ADDS a new codification (bias B-n,
lesson L-n, Critical Rule #n, Principle/Workflow entry, TC-n cluster, PC/PD-n
pattern) to a canonical harness file MUST update meta/session-prime.md in the
same changeset. Origin failures: Jul-9→12 codification batches; then Jul-14
(#45, 2 candidate lessons, PC-17 scope-gap) shipped while session-prime sat
stale at Jul-13 — caught manually at session close (commit 7836719).

v2 DESIGN — ID-SET DIFF, not line-pattern-on-added-lines:
  new codifications = (IDs extracted from ADDED lines) − (IDs from REMOVED
  lines), per canonical file. Editing an existing entry or table row puts its
  ID on BOTH sides of the diff → correctly ignored (v1 would have
  false-positived on every rule edit / TC-row promotion). Update-class headers
  that reference an existing ID without touching its defining line
  (ENRICHMENT / REFINEMENT / RECALIBRATION / FALSIFICATION / TOMBSTONE /
  "update") are excluded by keyword — documented trade-off: a genuinely NEW
  entry whose title contains one of those words is a known false-negative
  class. methodology.md entries often carry no stable ID ("## House-data
  freshness parity (added 2026-07-12…)") → the normalized header text is the
  key there; a reworded codification header will false-positive once
  (accepted — a retitled codification arguably warrants a session-prime look).
SCOPE EXTENSION v2: cross-domain-pattern-register.md added to CANONICAL
  (PC-17 shipped 2026-07-10 unwatched — same staleness class).

TELEMETRY (new in v2 — v1 logged nothing, which made its own falsifier
unverifiable): FIREs and ERRORs append to meta/hook-fire-log.md in house
format. Clean passes are NOT logged (Stop fires every turn; spam would bury
the signal). Non-invocation is checkable via sibling Stop-hook log entries.

FAIL-OPEN: any exception → log ERROR, exit 0. Exit 2 only on a clean positive.

Falsifier (re-eval 2026-08-14): zero LOGGED fires in 30 days → either the
cascade discipline is perfect (audit manually) or detection regressed — rerun
--selftest + the 30-day backtest in the fix-spec. LOGGED false-positive rate
>30% → tighten extractors/exclusions.

Testing:
  python3 session-prime-cascade-hook.py < /dev/null   → exit 0 (fail-open)
  python3 session-prime-cascade-hook.py --selftest    → fixture suite, exit 0 all-pass
"""

import json
import re
import subprocess
import sys

REPO_ROOT = _REPO_ROOT
FIRE_LOG = _Path(REPO_ROOT) / "research" / "meta" / "hook-fire-log.md"

# Update-class headers referencing existing IDs — never "new codification".
EXCLUDE = re.compile(
    r"ENRICHMENT|REFINEMENT|RECALIBRATION|TOMBSTONE|FALSIFICATION|\bupdate\b",
    re.IGNORECASE,
)

ID_GUARD = r"(?![.\d])"  # B40.1-style sub-instances are not new entries


def _x_bias(line):
    m = re.match(r"\s*#{2,4}\s+(B\d+)" + ID_GUARD, line)
    return [m.group(1)] if m else []


def _x_lesson(line):
    m = re.match(r"\s*#{2,4}\s+(L\d+)" + ID_GUARD, line)
    return [m.group(1)] if m else []


def _x_methodology(line):
    # Headers carrying a codification marker; key = normalized header text.
    if not re.match(r"\s*#{2,4}\s+\S", line):
        return []
    if re.search(r"\b(?:added|codified)\s+20\d\d-\d\d", line) or \
       re.search(r"\b(?:Principle|Workflow)\s+#\d+", line) or \
       (re.search(r"\bcandidate\b", line, re.I) and re.search(r"20\d\d-\d\d-\d\d", line)):
        return ["METH::" + re.sub(r"\s+", " ", line.strip())]
    return []


def _x_claude_rule(line):
    # Top-level numbered Critical Rule with an (added DATE …) marker.
    m = re.match(r"(\d+)\.\s+\*\*", line)
    if m and re.search(r"\(added 20\d\d-\d\d-\d\d", line):
        return ["RULE-" + m.group(1)]
    return []


def _x_tc(line):
    hits = []
    m = re.match(r"\s*#{2,4}\s+(TC-\d+)\b", line)   # legacy header form (TC-1..14)
    if m:
        hits.append(m.group(1))
    m = re.match(r"\s*\|\s*\*\*(TC-\d+)\*\*", line)  # current table-row form (TC-15..18)
    if m:
        hits.append(m.group(1))
    return hits


def _x_pattern(line):
    # PC-n / PD-n / P-n float mid-header here ("## [2026-07-02] PD-7 CANDIDATE …").
    if not re.match(r"\s*#{2,4}\s+\S", line):
        return []
    return re.findall(r"\b((?:PC|PD|P)-\d+)" + ID_GUARD, line)


CANONICAL = {
    "research/meta/biases-watchlist.md": _x_bias,
    "research/predictions/lessons.md": _x_lesson,
    "research/meta/methodology.md": _x_methodology,
    "research/CLAUDE.md": _x_claude_rule,
    "research/signals/triangulation.md": _x_tc,
    "research/meta/cross-domain-pattern-register.md": _x_pattern,
}

SESSION_PRIME = "research/meta/session-prime.md"


def log_fire(status, detail):
    """Append a house-format line to hook-fire-log.md. Never raises."""
    try:
        from datetime import datetime, timezone
        ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%SZ")
        with open(FIRE_LOG, "a") as f:
            f.write(f"- {ts} session-prime-cascade-hook {status} ({detail})\n")
    except Exception:
        pass


def _git(args):
    return subprocess.run(
        ["git", *args], cwd=REPO_ROOT, capture_output=True, text=True, timeout=15
    ).stdout


def parse_diff_keys(diff_text):
    """Walk a unified diff; return (added_keys, removed_keys, evidence).

    Keys are extracted per-file via the CANONICAL extractor. EXCLUDE-keyword
    lines are skipped on the ADDED side only (a removed update-header must not
    mask a genuinely new ID)."""
    added, removed, evidence = set(), set(), {}
    extractor = None
    for raw in diff_text.splitlines():
        if raw.startswith("+++ b/"):
            extractor = CANONICAL.get(raw[6:].strip())
            continue
        if raw.startswith("--- "):
            continue
        if extractor is None:
            continue
        if raw.startswith("+"):
            body = raw[1:]
            if EXCLUDE.search(body):
                continue
            for k in extractor(body):
                added.add(k)
                evidence.setdefault(k, body.strip()[:160])
        elif raw.startswith("-"):
            for k in extractor(raw[1:]):
                removed.add(k)
    return added, removed, evidence


def changeset_keys():
    """Union of working-tree, staged, and HEAD-commit codification-key diffs."""
    added, removed, evidence = set(), set(), {}
    for c in (["diff", "-U0"], ["diff", "--cached", "-U0"],
              ["show", "-U0", "--format=", "HEAD"]):
        a, r, e = parse_diff_keys(_git([*c, "--", *CANONICAL.keys()]))
        added |= a
        removed |= r
        for k, v in e.items():
            evidence.setdefault(k, v)
    return added, removed, evidence


def changeset_files():
    files = set()
    for c in (["diff", "--name-only"], ["diff", "--cached", "--name-only"],
              ["show", "--name-only", "--format=", "HEAD"]):
        files.update(f.strip() for f in _git(c).splitlines() if f.strip())
    return files


def main():
    try:
        # Recursion guard (K3-Swarm G-20 fix, 2026-07-20): house convention since
        # 2026-07-06 — an un-remediated block must not re-fire forever. This was
        # the only wired Stop hook without it (v2 rebuilt 07-14 missed the pattern).
        try:
            payload = json.loads(sys.stdin.read() or "{}")
            if payload.get("stop_hook_active"):
                sys.exit(0)
        except SystemExit:
            raise
        except Exception:
            pass  # unreadable stdin never disables enforcement (fail-closed here)
        added, removed, evidence = changeset_keys()
        new_keys = added - removed
        if not new_keys:
            sys.exit(0)
        if SESSION_PRIME in changeset_files():
            sys.exit(0)
        log_fire("FIRE", "new-codification-ids=" + ",".join(sorted(new_keys))[:200])
        sys.stderr.write(
            "SESSION-PRIME CASCADE INCOMPLETE (Critical Rule #13 sub-discipline; "
            "session-prime.md §10): this changeset adds NEW codification(s) to a "
            "canonical file but does NOT update research/meta/session-prime.md.\n"
            "New codification IDs detected:\n"
            + "\n".join(f"  {k}: {evidence.get(k, '')}" for k in sorted(new_keys)[:6])
            + "\nRequired: add/refresh the corresponding session-prime.md entry "
            "in the SAME changeset, or remove the stale entry it supersedes.\n"
        )
        sys.exit(2)
    except SystemExit:
        raise
    except Exception as e:
        log_fire("ERROR", f"{type(e).__name__}: {e}"[:160])
        sys.exit(0)


# ---------------------------------------------------------------------------
# Selftest — fixtures are REAL lines from the live corpus (harvested
# 2026-07-14) plus the known near-miss negatives. Run: --selftest
# ---------------------------------------------------------------------------
def _fixture_diff(path, added_lines, removed_lines=()):
    return (f"--- a/{path}\n+++ b/{path}\n"
            + "".join(f"+{l}\n" for l in added_lines)
            + "".join(f"-{l}\n" for l in removed_lines))


SELFTEST = [
    ("bias dash-form (B64 real)", _fixture_diff(
        "research/meta/biases-watchlist.md",
        ["### B64 — Model-affinity contamination on agentic-workflow names (CANDIDATE — N=1 origin 2026-07-13, USER-FLAGGED)"]),
        {"B64"}),
    ("bias colon-form (B61 real — v1 regex missed this shape)", _fixture_diff(
        "research/meta/biases-watchlist.md",
        ["### B61 CANDIDATE (2026-07-03, N=1): LLM-GENERATED BOTTLENECK FICTION as an input class"]),
        {"B61"}),
    ("bias sub-instance must NOT fire (B40.1 real)", _fixture_diff(
        "research/meta/biases-watchlist.md",
        ["**B40.1 date-shift recycle instance (2026-07-02):** User-shared Twitter article"]),
        set()),
    ("lesson header (L30 real)", _fixture_diff(
        "research/predictions/lessons.md",
        ["## L30 (NEW positive lesson CANDIDATE — origin 2026-06-26 KIOXIA VLSI Symposium prediction grade)"]),
        {"L30"}),
    ("lesson update header must NOT fire (L26 real)", _fixture_diff(
        "research/predictions/lessons.md",
        ["### L26 update 2026-06-14 PM4 — Universal supply-side + universal demand-side"]),
        set()),
    ("lesson tombstone must NOT fire (L17 real)", _fixture_diff(
        "research/predictions/lessons.md",
        ["## L17 — TOMBSTONE (number never codified; added 2026-07-06 harness audit)"]),
        set()),
    ("principle #45 — THE 2026-07-14 miss, f6ce2d5 verbatim shape", _fixture_diff(
        "research/meta/methodology.md",
        ['## Principle #45 candidate (added 2026-07-14 per user question "how do you reason around the timing of the re-eval") — EVENT-ANCHORED RE-EVAL']),
        {'METH::## Principle #45 candidate (added 2026-07-14 per user question "how do you reason around the timing of the re-eval") — EVENT-ANCHORED RE-EVAL'}),
    ("methodology bare-date CANDIDATE header (f500a4d real — first fix draft missed it)", _fixture_diff(
        "research/meta/methodology.md",
        ["## Output-preference / reasoning-discipline note (2026-07-14) — STATIC-COLLAPSE of a forward thesis (CANDIDATE lesson, N=1)"]),
        {"METH::## Output-preference / reasoning-discipline note (2026-07-14) — STATIC-COLLAPSE of a forward thesis (CANDIDATE lesson, N=1)"}),
    ("methodology body-line annotation must NOT fire (57cffd5 real shape)", _fixture_diff(
        "research/meta/methodology.md",
        ['**2026-07-14 POSITIVE feedback — "less rigidity" on framework evidence (user verbatim-adjacent)**']),
        set()),
    ("methodology no-ID codification (real 2026-07-12)", _fixture_diff(
        "research/meta/methodology.md",
        ["## House-data freshness parity (added 2026-07-12, user-designed; companion to Critical Rule #12 and Principle #37)"]),
        {"METH::## House-data freshness parity (added 2026-07-12, user-designed; companion to Critical Rule #12 and Principle #37)"}),
    ("critical rule (Rule 17 real)", _fixture_diff(
        "research/CLAUDE.md",
        ["17. **ENSEMBLE HIGH-STAKES CALLS — SELF-CONSISTENCY ON BINARY/NUMERIC DECISIONS** (added 2026-06-27 per user LLM-native-audit directive). I am a sampling process"]),
        {"RULE-17"}),
    ("rule EDIT must NOT fire (same rule number both sides)", _fixture_diff(
        "research/CLAUDE.md",
        ["16. **ALWAYS RUN VERIFICATION SUBAGENTS — NEVER ASK PERMISSION** (added 2026-06-15 PM15, amended)"],
        ["16. **ALWAYS RUN VERIFICATION SUBAGENTS — NEVER ASK PERMISSION** (added 2026-06-15 PM15)"]),
        set()),
    ("counter-bump reference must NOT fire (27718be verbatim shape)", _fixture_diff(
        "research/CLAUDE.md",
        ["       → Principle (meta/methodology.md, currently #1-#45; candidates incl. #42 retrieval-staleness"]),
        set()),
    ("TC table row NEW (TC-18 real shape)", _fixture_diff(
        "research/signals/triangulation.md",
        ["| **TC-18** Capital-committed supply-securing (revealed-preference shortage validation) | memory-and-storage | **[CANDIDATE N=1]** | **1** |"]),
        {"TC-18"}),
    ("TC row PROMOTION EDIT must NOT fire (both sides)", _fixture_diff(
        "research/signals/triangulation.md",
        ["| **TC-15** Model labs internalizing inference silicon | model-and-foundation-lab | **[ACTIVE — promoted at N=4, 2026-07-08]** | **4** |"],
        ["| **TC-15** Model labs internalizing inference silicon | model-and-foundation-lab | **[CANDIDATE N=3]** | **3** |"]),
        set()),
    ("TC instance line must NOT fire (real N+1 shape)", _fixture_diff(
        "research/signals/triangulation.md",
        ["- **TC-18 N+1 (→6, 2026-07-13 EVE) — FIRST WAFER-LAYER INSTANCE:** Micron $500M"]),
        set()),
    ("legacy TC header form (TC-12 real)", _fixture_diff(
        "research/signals/triangulation.md",
        ["## TC-12 — DRAM>HBM margin inversion in upcycle [ACTIVE N=6]"]),
        {"TC-12"}),
    ("pattern-register NEW (PC-17 real — v1 didn't even watch this file)", _fixture_diff(
        "research/meta/cross-domain-pattern-register.md",
        ["## PC-17 [CANDIDATE, N=3, added 2026-07-10] — Generation-cost collapse migrates value capture to the VERIFICATION layer"]),
        {"PC-17"}),
    ("pattern mid-header ID (PD-7 real shape)", _fixture_diff(
        "research/meta/cross-domain-pattern-register.md",
        ["## [2026-07-02] PD-7 CANDIDATE (N=1) — EFFICIENT-DISCOVERY REGIME: obliviousness survives only in structurally un-modelable exposure"]),
        {"PD-7"}),
    ("pattern ENRICHMENT must NOT fire (PC-14 real)", _fixture_diff(
        "research/meta/cross-domain-pattern-register.md",
        ["### PC-14 N=2 → N=3+ ENRICHMENT 2026-06-17 AM7 — Asia mirror sub-cluster CONFIRMED"]),
        set()),
    ("non-canonical file must NOT fire", _fixture_diff(
        "research/meta/tags.md",
        ["### B99 — completely new bias in the wrong file"]),
        set()),
]


def selftest():
    failures = []
    for name, diff_text, expected in SELFTEST:
        a, r, _ = parse_diff_keys(diff_text)
        got = a - r
        if got != expected:
            failures.append(f"FAIL {name}:\n  expected {expected or '{}'}\n  got      {got or '{}'}")
    if failures:
        print("\n".join(failures))
        print(f"{len(failures)}/{len(SELFTEST)} fixtures FAILED")
        sys.exit(1)
    print(f"selftest OK — {len(SELFTEST)}/{len(SELFTEST)} fixtures pass")
    sys.exit(0)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        selftest()
    main()
