#!/usr/bin/env python3
import os as _os
from pathlib import Path as _Path
_REPO_ROOT = _os.environ.get("CLAUDE_PROJECT_DIR") or str(_Path(__file__).resolve().parents[3])
"""
Session-prime cascade Stop hook (built 2026-07-12, escalation pre-registered in
the 2026-07-12 session-prime effectiveness audit + session-prime.md §10).

Enforces the Critical Rule #13 sub-discipline: every commit that ADDS a new
codification (bias B-n, lesson L-n, Critical Rule #n, Principle #n, TC-n
cluster) to a canonical harness file MUST update meta/session-prime.md in the
same changeset. Origin failure: Jul-9→12 codification batches (prompt-library,
end-demand model, principal-profile suite) shipped without session-prime
updates — the exact staleness §10 predicted.

NARROW TRIGGER (false-positive discipline): fires ONLY when the current
changeset (working tree + staged + HEAD) shows ADDED lines matching
new-codification ID patterns inside the canonical files, AND session-prime.md
is absent from the same changeset. N-counter increments, edits to existing
entries, and all other files never fire it.

FAIL-OPEN: any exception → exit 0. Exit 2 only on a clean positive match.

Falsifier (re-eval 2026-08-12): if 30 days show zero fires, either discipline
is now perfect (check manually) or the trigger is too narrow — refine or
retire. If false-positive rate >30% (fires on non-codification edits), tighten
the patterns.

Testing: python3 session-prime-cascade-hook.py < /dev/null  → exit 0.
"""

import re
import subprocess
import sys

REPO_ROOT = _REPO_ROOT

CANONICAL = [
    "research/meta/biases-watchlist.md",
    "research/predictions/lessons.md",
    "research/meta/methodology.md",
    "research/CLAUDE.md",
    "research/signals/triangulation.md",
]

# Added-line patterns that constitute a NEW codification (headers/entries, not references)
PATTERNS = [
    re.compile(r"^\+\s*#{2,4}\s+B\d+\s+[—-]"),               # new bias section header
    re.compile(r"^\+\s*#{2,4}\s+TC-\d+\s+[—-]"),             # new TC cluster section header
    re.compile(r"^\+\s*#{2,4}\s+(?:Principle\s+)?#\d+\s+[—-]"),  # new principle section header
    re.compile(r"^\+\s*\*\*L\d+\s+[—-]"),                     # new lesson entry
    re.compile(r"^\+\d+\.\s+\*\*[A-Z][^*]+\*\*.*\(added 20\d\d-\d\d-\d\d"),  # new Critical Rule in CLAUDE.md
]


def diff_added_lines():
    """Added lines across working tree + staged + HEAD, restricted to canonical files."""
    lines = []
    for args in (["git", "diff", "-U0", "--", *CANONICAL],
                 ["git", "diff", "--cached", "-U0", "--", *CANONICAL],
                 ["git", "show", "-U0", "--format=", "HEAD", "--", *CANONICAL]):
        try:
            out = subprocess.run(args, cwd=REPO_ROOT, capture_output=True, text=True, timeout=15).stdout
            lines += [l for l in out.splitlines() if l.startswith("+") and not l.startswith("+++")]
        except Exception:
            pass
    return lines


def changeset_files():
    files = set()
    for args in (["git", "diff", "--name-only"],
                 ["git", "diff", "--cached", "--name-only"],
                 ["git", "show", "--name-only", "--format=", "HEAD"]):
        try:
            out = subprocess.run(args, cwd=REPO_ROOT, capture_output=True, text=True, timeout=15).stdout
            files.update(f.strip() for f in out.splitlines() if f.strip())
        except Exception:
            pass
    return files


def main():
    try:
        added = diff_added_lines()
        hits = [l for l in added if any(p.match(l) for p in PATTERNS)]
        if not hits:
            sys.exit(0)
        if "research/meta/session-prime.md" in changeset_files():
            sys.exit(0)
        sys.stderr.write(
            "SESSION-PRIME CASCADE INCOMPLETE (Critical Rule #13 sub-discipline; "
            "session-prime.md §10): this changeset adds new codification(s) to a "
            "canonical file but does NOT update research/meta/session-prime.md.\n"
            "New-codification lines detected:\n  "
            + "\n  ".join(h[:160] for h in hits[:5])
            + "\nRequired: add/refresh the corresponding session-prime.md entry "
            "(§2 biases / §3 lessons / §4 rules / §5 TC clusters) in the SAME "
            "commit, or remove the stale entry it supersedes.\n"
        )
        sys.exit(2)
    except Exception:
        sys.exit(0)


if __name__ == "__main__":
    main()
