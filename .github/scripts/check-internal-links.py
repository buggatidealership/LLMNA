#!/usr/bin/env python3
"""Referral-path integrity checker for the investing OS.

The reference layer (INDEX.md, tags, cross-links) is the firm's retrieval
spine: files cite each other as backticked repo-relative paths like
`research/companies/SUMCO/thesis.md`. This script verifies every such
reference resolves to a real file, so referral paths can never silently rot.

Scans all .md files under research/ plus root CLAUDE.md/README.md.
Exit 1 if any reference is broken; prints file:line for each.

Conventions handled:
- `research/...` prefixed refs (canonical form)
- refs starting with a research/ top-level dir (companies/, meta/, signals/,
  portfolio/, predictions/, sector/, watchlist/, wiki/) are resolved
  relative to research/ (INDEX.md shorthand convention)
- directory references (trailing /) must be existing directories
- refs containing wildcards (*), placeholders (<, {, YYYY, TICKER, ...),
  alternations (|), or shell expansions ($, ~) are skipped — they are
  patterns, not paths
- known pre-existing breaks live in .github/link-check-baseline.txt;
  only NEW breakage fails CI (burn the baseline down over time)
"""
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
RESEARCH = REPO / "research"
TOP_DIRS = ("companies/", "meta/", "signals/", "portfolio/",
            "predictions/", "sector/", "watchlist/", "wiki/")

REF_RE = re.compile(r"`([^`\n]+?\.md|[^`\n]+?/)`")
SKIP_MARKERS = ("*", "<", "{", "$", "~", "http", " ", "YYYY", "...", "|", "TICKER")
BASELINE = Path(__file__).resolve().parent.parent / "link-check-baseline.txt"

broken = []
scanned = checked = 0

targets = sorted(RESEARCH.rglob("*.md")) + [REPO / "CLAUDE.md", REPO / "README.md"]
for md in targets:
    if not md.exists():
        continue
    scanned += 1
    for lineno, line in enumerate(md.read_text(errors="replace").splitlines(), 1):
        for ref in REF_RE.findall(line):
            ref = ref.strip()
            if any(m in ref for m in SKIP_MARKERS) or ref.startswith("/"):
                continue
            if ref.startswith("research/"):
                candidates = [REPO / ref]
            elif ref.startswith(TOP_DIRS):
                candidates = [RESEARCH / ref, REPO / ref]
            else:
                continue  # not a repo-path convention we enforce
            checked += 1
            if not any(c.exists() for c in candidates):
                broken.append(f"{md.relative_to(REPO)}:{lineno}: `{ref}`")

print(f"Scanned {scanned} files, checked {checked} path references.")

baseline = set()
if BASELINE.exists():
    baseline = {l.strip() for l in BASELINE.read_text().splitlines()
                if l.strip() and not l.startswith("#")}

if "--write-baseline" in sys.argv:
    BASELINE.write_text(
        "# Known-broken referral paths (pre-existing rot, 2026-07-06 migration audit).\n"
        "# Burn this list down over time; CI fails only on NEW breakage.\n"
        + "\n".join(broken) + "\n")
    print(f"Baseline written: {len(broken)} known-broken refs.")
    sys.exit(0)

new = [b for b in broken if b not in baseline]
fixed = baseline - set(broken)
if fixed:
    print(f"NOTE: {len(fixed)} baseline entries now resolve — prune them from the baseline.")
if new:
    print(f"\nNEW BROKEN ({len(new)}):")
    for b in new:
        print(f"  {b}")
    sys.exit(1)
print(f"No new broken referral paths ({len(broken)} known pre-existing in baseline). ✅")
