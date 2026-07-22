#!/usr/bin/env python3
"""Structural-output experiment — NORMALIZED metric (user decision 2026-07-06).

Computes weekly structural-output-hook fires / weekly main-branch commits,
the deterministic adjudicator for the 2026-08-06 keep-vs-retire decision on
the llm-native-priming-hook (see CLAUDE.md structural-output-hook entry).

Decision rule (pre-registered 2026-07-06): normalized rate FALLING over the
extension window -> priming works, keep both; flat/rising -> retire priming.

Run: python3 research/meta/structural-output-metric.py  (from repo root)
Selftest: python3 research/meta/structural-output-metric.py --selftest

Compute-instead-of-narrate: born from Principle #43b first registered
candidate (2026-07-07) — this metric was previously eyeball-counted.

=== 2026-07-22 METRIC-INTEGRITY REWORK (accounting-layer commission item 3;
    K3 theme 3 "scoreboard movable by the player", G-28 re-graded BLOCKING) ===

Three contamination channels closed, each with a machine-checkable rule:

(A) NUMERATOR RECLASSIFICATION (G-28). The old regex counted EVERY
    `structural-output.*FIRE` line. But the hook fires for TWO unrelated
    reasons: `structural-markers-missing` (the general linear-prose revert
    the PRIMING experiment measures) and `position-implication-tier-missing`
    (Principle #37 tier discipline — nothing to do with priming). Counting
    tier-fires inflated the numerator with an unrelated enforcement's misses
    (15 such lines in the log at rework time). The numerator now counts ONLY
    genuine structural-markers-missing fires: tagged `structural-markers-missing`
    OR legacy-untagged (pre-2026-06-15, before the tier-fire path existed) —
    and EXCLUDES tier-fires, explicitly-marked smoke-tests, and [probe] fires.

(B) PROBE POLLUTION (2nd channel). Running the hook's own test batteries
    appends real FIRE lines to this log (observed live 2026-07-22 08:29Z: a
    tier-gate test run added 7 tier-fires). The hook's _log_fire now tags
    fires with ` [probe]` when LLMNA_HOOK_TEST=1 is set (tests set it); this
    metric drops any `[probe]` line. Defense-in-depth: even a test that
    forgets to isolate its log cannot move the scoreboard.

(C) REF-ORDER (e04eaef inversion vs design-130). The denominator counts
    commits on the trunk. e04eaef resolved `main` (local) FIRST, but a session
    container's local `main` is often absent or stale (cached clone), while
    `origin/main` is the authoritative merged trunk. Local-first swung the week
    rate 0.196->0.452 purely on which copy was read. Per design-130 intent
    (origin/main-first for session containers), resolution is now
    origin/main -> local main -> HEAD.

(D) DENOMINATOR HARDENING. "The system authors its own commits" — pure
    telemetry commits (hook-fire-log-only) add zero analytical surface but pad
    the denominator, biasing the rate DOWN (= spuriously "priming works").
    They are now excluded from the commit count. Residual gaming surface
    (non-telemetry filler commits) is documented, not fully closed — a single
    normalizer cannot be un-gameable; the honest move is to name the residual.
"""
import os
import re
import subprocess
import sys
from collections import defaultdict
from datetime import date, datetime
from pathlib import Path

REPO = Path(os.environ.get("CLAUDE_PROJECT_DIR") or Path(__file__).resolve().parents[2])
LOG = REPO / "research" / "meta" / "hook-fire-log.md"
EXPERIMENT_START = date(2026, 6, 1)  # hook pair shipped 2026-06-01
# before this date the tier-fire path did not exist, so an untagged FIRE is a
# genuine structural-markers-missing fire (the metric's target class)
TIER_FIRE_PATH_BORN = date(2026, 6, 15)


def week_key(d: date) -> str:
    iso = d.isocalendar()
    return f"{iso[0]}-W{iso[1]:02d}"


# (A)+(B) numerator classifier — the single machine-checkable rule.
# REWORK-5 (K3 finding 5c — CROSS-HOOK INJECTION CLOSED): the old regex used
# `- <date> .*structural-output-hook FIRE`, so the phrase could appear ANYWHERE
# in the line — a promise-heartbeat log line echoing a registry WHAT-string that
# CONTAINED "structural-output-hook FIRE (structural-markers-missing)" was
# miscounted as a genuine fire. Anchor the hook-source name IMMEDIATELY after the
# full `YYYY-MM-DD HH:MM:SSZ` timestamp (the log's `- <ts> <hook> <msg>` shape),
# so only a line whose LOG SOURCE is the structural-output-hook counts. A phrase
# embedded in another hook's message can no longer forge a fire.
_FIRE = re.compile(r"- (\d{4}-\d{2}-\d{2}) \d{2}:\d{2}:\d{2}Z structural-output-hook FIRE\b(.*)$")
_EXCLUDE_MARKERS = ("position-implication-tier-missing", "[probe]",
                    "smoke-test", "NOT a genuine fire", "do not count")


def is_counted_fire(line: str):
    """Return the date of a GENUINE priming-relevant fire, or None.

    Counts a structural-output-hook FIRE line iff it is the
    structural-markers-missing class (tagged, or legacy-untagged before the
    tier path existed) and carries no exclusion marker.
    """
    m = _FIRE.match(line)
    if not m:
        return None
    d = datetime.strptime(m.group(1), "%Y-%m-%d").date()
    if d < EXPERIMENT_START:
        return None
    tail = m.group(2)
    if any(mk in line for mk in _EXCLUDE_MARKERS):
        return None
    tagged = "(" in tail
    if tagged:
        # tagged era: only the structural-markers-missing class counts
        return d if "structural-markers-missing" in tail else None
    # untagged: genuine only if it predates the tier-fire path
    return d if d < TIER_FIRE_PATH_BORN else None


def resolve_ref(repo: Path) -> str:
    """(C) origin/main -> local main -> HEAD (design-130: origin-first in
    session containers, where local main is often stale/absent)."""
    for cand in ("origin/main", "main"):
        chk = subprocess.run(
            ["git", "-C", str(repo), "rev-parse", "--verify", "--quiet", cand],
            capture_output=True, text=True)
        if chk.returncode == 0:
            return cand
    return "HEAD"


def is_telemetry_only_commit(repo: Path, sha: str) -> bool:
    """(D) True iff the commit touches ONLY the telemetry log."""
    out = subprocess.run(
        ["git", "-C", str(repo), "show", "--no-renames", "--format=", "--name-only", sha],
        capture_output=True, text=True)
    files = [f for f in out.stdout.splitlines() if f.strip()]
    return files == ["research/meta/hook-fire-log.md"]


def count_commits(repo: Path, ref: str):
    """Weekly commit counts on `ref` since EXPERIMENT_START, excluding
    telemetry-only commits (D)."""
    out = subprocess.run(
        # NOT --first-parent: the 2026-07-06 migration grafted pre-migration
        # history onto a merge side-branch; first-parent would zero out all
        # pre-July weeks (caught 2026-07-07 on first computed run).
        ["git", "-C", str(repo), "log", ref,
         f"--since={EXPERIMENT_START.isoformat()}", "--format=%H %as"],
        capture_output=True, text=True, check=False)
    commits = defaultdict(int)
    excluded = 0
    for line in out.stdout.splitlines():
        parts = line.split()
        if len(parts) != 2:
            continue
        sha, ds = parts
        if is_telemetry_only_commit(repo, sha):
            excluded += 1
            continue
        commits[week_key(datetime.strptime(ds, "%Y-%m-%d").date())] += 1
    return commits, excluded


def main() -> None:
    fires = defaultdict(int)
    for line in LOG.read_text().splitlines():
        d = is_counted_fire(line)
        if d:
            fires[week_key(d)] += 1

    ref = resolve_ref(REPO)
    commits, excluded = count_commits(REPO, ref)

    weeks = sorted(set(fires) | set(commits))
    print(f"ref={ref}  telemetry-only commits excluded: {excluded}")
    print(f"{'week':<10} {'fires':>5} {'commits':>7} {'fires/commit':>12}")
    rates = []
    for w in weeks:
        f, c = fires.get(w, 0), commits.get(w, 0)
        rate = f / c if c else float("nan")
        rates.append((w, rate))
        print(f"{w:<10} {f:>5} {c:>7} {rate:>12.3f}")

    tail = [r for _, r in rates[-4:] if r == r]  # drop NaN
    if len(tail) >= 2:
        direction = "FALLING" if tail[-1] < tail[0] else "FLAT/RISING"
        print(f"\nLast-4-weeks normalized trend: {tail[0]:.3f} -> {tail[-1]:.3f} = {direction}")
        print("Decision rule: FALLING -> keep priming hook; FLAT/RISING -> retire (adjudicate 2026-08-06).")


# ---------------------------------------------------------------- selftest
def _selftest() -> int:
    fails = 0

    def check(label, cond):
        nonlocal fails
        print(("OK  " if cond else "XX  ") + label)
        fails += 0 if cond else 1

    # (A) numerator classifier
    check("counts tagged structural-markers-missing",
          is_counted_fire("- 2026-07-01 10:00:00Z structural-output-hook FIRE (structural-markers-missing)") is not None)
    check("EXCLUDES tier-missing (G-28 core)",
          is_counted_fire("- 2026-07-01 10:00:00Z structural-output-hook FIRE (position-implication-tier-missing)") is None)
    check("EXCLUDES [probe]-tagged fire (B)",
          is_counted_fire("- 2026-07-01 10:00:00Z structural-output-hook FIRE (structural-markers-missing) [probe]") is None)
    check("EXCLUDES explicit smoke-test line",
          is_counted_fire("- 2026-06-12 06:20:05Z structural-output-hook FIRE (smoke-test against fake transcript — NOT a genuine fire; do not count in week-2 check)") is None)
    check("counts legacy untagged fire (pre-tier-path)",
          is_counted_fire("- 2026-06-13 06:42:10Z structural-output-hook FIRE") is not None)
    check("EXCLUDES untagged fire AFTER tier path born (ambiguous → not counted)",
          is_counted_fire("- 2026-06-20 06:42:10Z structural-output-hook FIRE") is None)
    check("EXCLUDES pre-experiment fire",
          is_counted_fire("- 2026-05-20 06:42:10Z structural-output-hook FIRE (structural-markers-missing)") is None)
    check("non-fire line ignored",
          is_counted_fire("- 2026-07-01 10:00:00Z git-guard-pretooluse BLOCK (x)") is None)
    # REWORK-5c: a cross-hook line that merely CONTAINS the fire phrase in another
    # hook's message (e.g. a promise-heartbeat line echoing a registry WHAT-string)
    # must NOT be counted — the hook-source name is anchored after the timestamp.
    check("REWORK-5c: cross-hook injected fire phrase NOT counted",
          is_counted_fire("- 2026-07-27 10:00:00Z promise-heartbeat OVERDUE set changed: "
                          "[2026-07-01] structural-output-hook FIRE (structural-markers-missing)") is None)
    check("REWORK-5c: genuine fire (hook-source anchored) still counted",
          is_counted_fire("- 2026-07-27 10:00:00Z structural-output-hook FIRE (structural-markers-missing)") is not None)
    # REWORK-5c: a registry-injected line without a real timestamp also rejected
    check("REWORK-5c: no real timestamp -> not counted",
          is_counted_fire("- 2026-07-27 structural-output-hook FIRE (structural-markers-missing)") is None)

    # (C)+(D) against a synthetic repo
    import tempfile
    with tempfile.TemporaryDirectory() as td:
        repo = Path(td) / "r"
        (repo / "research" / "meta").mkdir(parents=True)
        run = lambda *a: subprocess.run(["git", "-C", str(repo), *a],
                                        capture_output=True, text=True, check=True)
        run("init", "-q")
        run("config", "user.email", "t@t")
        run("config", "user.name", "t")
        # a real analytical commit
        (repo / "research" / "meta" / "a.md").write_text("x\n")
        run("add", "-A")
        run("commit", "-qm", "real work", "--date=2026-07-01T10:00:00")
        real_sha = run("rev-parse", "HEAD").stdout.strip()
        # a telemetry-only commit
        (repo / "research" / "meta" / "hook-fire-log.md").write_text("- x\n")
        run("add", "-A")
        run("commit", "-qm", "telemetry", "--date=2026-07-01T11:00:00")
        tele_sha = run("rev-parse", "HEAD").stdout.strip()

        check("telemetry-only commit detected (D)", is_telemetry_only_commit(repo, tele_sha))
        check("real commit not telemetry (D)", not is_telemetry_only_commit(repo, real_sha))
        commits, excluded = count_commits(repo, "HEAD")
        check("denominator excludes telemetry commit (D)",
              excluded == 1 and sum(commits.values()) == 1)
        # (C) ref resolution: no origin/main, local main exists on default branch
        ref = resolve_ref(repo)
        check("ref falls back past missing origin/main", ref in ("main", "HEAD"))

    print("ALL PASS" if fails == 0 else f"{fails} MISMATCH")
    return fails


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(_selftest())
    main()
