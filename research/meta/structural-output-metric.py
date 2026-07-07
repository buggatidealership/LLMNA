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


def main() -> None:
    fires = defaultdict(int)
    for line in LOG.read_text().splitlines():
        m = re.match(r"- (\d{4}-\d{2}-\d{2}) .*structural-output.*FIRE", line)
        if m:
            d = datetime.strptime(m.group(1), "%Y-%m-%d").date()
            if d >= EXPERIMENT_START:
                fires[week_key(d)] += 1

    out = subprocess.run(
        # NOT --first-parent: the 2026-07-06 migration grafted pre-migration
        # history onto a merge side-branch; first-parent would zero out all
        # pre-July weeks (caught 2026-07-07 on first computed run).
        ["git", "-C", str(REPO), "log", "main",
         f"--since={EXPERIMENT_START.isoformat()}", "--format=%as"],
        capture_output=True, text=True, check=True,
    )
    commits = defaultdict(int)
    for line in out.stdout.splitlines():
        d = datetime.strptime(line.strip(), "%Y-%m-%d").date()
        commits[week_key(d)] += 1

    weeks = sorted(set(fires) | set(commits))
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


if __name__ == "__main__":
    main()
