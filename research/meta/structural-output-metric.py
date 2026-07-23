#!/usr/bin/env python3
"""Structural-output experiment — NORMALIZED metric (user decision 2026-07-06).

Computes weekly structural-output-hook fires / weekly main-branch commits,
the deterministic adjudicator for the 2026-08-06 keep-vs-retire decision on
the llm-native-priming-hook (see CLAUDE.md structural-output-hook entry).

Decision rule (pre-registered 2026-07-06): normalized rate FALLING over the
extension window -> priming works, keep both; flat/rising -> retire priming.

Run: python3 research/meta/structural-output-metric.py  (from repo root)
Compute-instead-of-narrate: born from Principle #43b first registered
candidate (2026-07-07) — this metric was previously eyeball-counted.
"""
import re
import subprocess
from collections import defaultdict
from datetime import date, datetime
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
LOG = REPO / "research" / "meta" / "hook-fire-log.md"
EXPERIMENT_START = date(2026, 6, 1)  # hook pair shipped 2026-06-01


def week_key(d: date) -> str:
    iso = d.isocalendar()
    return f"{iso[0]}-W{iso[1]:02d}"


# G-28 retro-exclusions: probe fires that landed BEFORE probe-tagging shipped
# (2026-07-23) and cannot be distinguished by line format. Keyed
# (date, class) -> count. Documented, deterministic, auditable.
KNOWN_PROBE_FIRES = {
    ("2026-07-23", "structural-markers-missing"): 1,   # tier-gate test suite, pre-tagging run
    ("2026-07-23", "position-implication-tier-missing"): 11,  # same runs (report-only column)
}


def main() -> None:
    # NUMERATOR reclassification (G-28, K3-re-graded BLOCKING; fixed 2026-07-23):
    # the experiment adjudicates the PRIMING hook's effect on the revert-to-
    # linear-prose failure mode, so the numerator is ONLY the
    # `structural-markers-missing` fire class. Excluded, with rationale:
    #   - position-implication-tier-missing: Principle #37 tier enforcement that
    #     happens to live in the same hook file — a DIFFERENT discipline; the
    #     b6ad6d6/G-27 reorder (tier check before size gate) inflates this class,
    #     which is exactly why it must not contaminate the priming metric.
    #   - probe=1 tagged lines + KNOWN_PROBE_FIRES: test-suite fires
    #     (probe-pollution, the 2nd contamination channel).
    #   - the 2026-06-15 smoke-test line (self-labeled "do not count") — the old
    #     regex counted it anyway.
    #   - legacy UNTYPED fires (6 lines, 2026-06-13..06-18, pre-typing era) are
    #     COUNTED: they predate the tier check's fire path being logged and sit
    #     outside the last-4-week decision window; continuity beats reclassifying
    #     what can't be reclassified.
    fires = defaultdict(int)
    tier_fires = defaultdict(int)  # report-only visibility column
    for line in LOG.read_text().splitlines():
        m = re.match(r"- (\d{4}-\d{2}-\d{2}) .*structural-output-hook FIRE(?:\s*\(([^)]*)\))?", line)
        if not m:
            continue
        d = datetime.strptime(m.group(1), "%Y-%m-%d").date()
        if d < EXPERIMENT_START:
            continue
        cls = (m.group(2) or "").strip()
        wk = week_key(d)
        if "probe=1" in line:
            continue
        if cls == "position-implication-tier-missing":
            tier_fires[wk] += 1
            continue
        if cls.startswith("smoke-test"):
            continue
        if cls in ("structural-markers-missing", ""):
            fires[wk] += 1
    for (dstr, cls), n in KNOWN_PROBE_FIRES.items():
        wk = week_key(datetime.strptime(dstr, "%Y-%m-%d").date())
        tgt = fires if cls == "structural-markers-missing" else tier_fires
        tgt[wk] = max(0, tgt.get(wk, 0) - n)

    # Ref order ADJUDICATED 2026-07-23 (e04eaef vs design-130): origin/main FIRST,
    # per the original design intent. Rationale: origin/main is the canonical
    # pushed history (house rule: every commit pushed); a container's LOCAL main
    # can be stale (wake sessions on branches), shrinking the denominator and
    # inflating the rate — the observed 0.196 vs 0.452 swing was exactly this.
    # Fallback chain keeps the 07-21 never-crash property: origin/main -> main -> HEAD.
    ref = "HEAD"
    for cand in ("origin/main", "main"):
        chk = subprocess.run(
            ["git", "-C", str(REPO), "rev-parse", "--verify", "--quiet", cand],
            capture_output=True, text=True,
        )
        if chk.returncode == 0:
            ref = cand
            break
    out = subprocess.run(
        # NOT --first-parent: the 2026-07-06 migration grafted pre-migration
        # history onto a merge side-branch; first-parent would zero out all
        # pre-July weeks (caught 2026-07-07 on first computed run).
        ["git", "-C", str(REPO), "log", ref,
         f"--since={EXPERIMENT_START.isoformat()}", "--format=%as"],
        capture_output=True, text=True, check=False,
    )
    commits = defaultdict(int)
    for line in out.stdout.splitlines():
        d = datetime.strptime(line.strip(), "%Y-%m-%d").date()
        commits[week_key(d)] += 1

    weeks = sorted(set(fires) | set(commits) | set(tier_fires))
    print(f"{'week':<10} {'fires':>5} {'commits':>7} {'fires/commit':>12} {'tier(ro)':>9}")
    rates = []
    for w in weeks:
        f, c = fires.get(w, 0), commits.get(w, 0)
        rate = f / c if c else float("nan")
        rates.append((w, rate))
        print(f"{w:<10} {f:>5} {c:>7} {rate:>12.3f} {tier_fires.get(w, 0):>9}")

    tail = [r for _, r in rates[-4:] if r == r]  # drop NaN
    if len(tail) >= 2:
        direction = "FALLING" if tail[-1] < tail[0] else "FLAT/RISING"
        print(f"\nLast-4-weeks normalized trend: {tail[0]:.3f} -> {tail[-1]:.3f} = {direction}")
        print("Decision rule: FALLING -> keep priming hook; FLAT/RISING -> retire (adjudicate 2026-08-06).")


if __name__ == "__main__":
    main()
