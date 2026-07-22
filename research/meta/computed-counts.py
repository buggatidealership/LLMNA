#!/usr/bin/env python3
"""LLMNA COMPUTED COUNTS — the map regenerates from the territory.

Built 2026-07-22 (accounting-layer commission item 5; K3 theme 5 "written map
lags territory": the rulebook said 17 hooks (19), Principle #46 (#47), and the
stale-count fix itself shipped stale). B65 "compute-don't-recall" applied to the
header counts, not just fire-counts.

WHAT IT COUNTS (each from its canonical TERRITORY source, with the exact
extraction method documented — because counting from prose is FRAGILE and a
generator that miscounts is worse than a hand count that's honestly stale):

  hooks          .claude/settings.json — command entries per event; a "script
                 hook" is one whose command references a .py/.sh file (vs a
                 shell one-liner like the core.hooksPath activation).
  lessons_max    predictions/lessons.md — HETEROGENEOUS: early lessons are
                 `## L<n>` headers, later ones are `[YYYY-MM-DD] ... L<n>`
                 append-log entries. Both counted (max). Bare cross-references
                 ("same family as L34") are line-initial-date OR ##-anchored, so
                 a mid-sentence mention alone never sets the max.
  biases_max     meta/biases-watchlist.md — `### B<n> — <title>` definition headers.
  principles_max meta/methodology.md — `## Principle #<n>` definition headers
                 (REFINEMENT headers reuse an existing number, so they can't
                 inflate the max).
  rules_max      research/CLAUDE.md — numbered `N. **...` items scoped to the
                 `## Critical Rules` section only (CLAUDE.md has other numbered
                 lists that must NOT be counted).
  patterns_max   meta/cross-domain-pattern-register.md — `P-<n>` / `PC-<n>`.
  triangulation_max signals/triangulation.md — `TC-<n>`.

MODES:
  --write     regenerate research/meta/computed-counts.md from the territory
  --check     recompute; exit 2 if the committed computed-counts.md is stale
              (the drift-catcher — a source edit that changes a count without
              regenerating fails loud)
  --audit     print computed values + scan header files (CLAUDE.md / INDEX.md /
              tags.md) for asserted counts and flag machine-detectable drift
  --selftest  synthetic-fixture battery for every extractor (exit = #fails)
"""
import json
import os
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(os.environ.get("CLAUDE_PROJECT_DIR") or Path(__file__).resolve().parents[2])
SETTINGS = REPO / ".claude" / "settings.json"
OUT = REPO / "research" / "meta" / "computed-counts.md"


# ---- extractors (each takes text, returns an int; pure + unit-tested) ----
def hooks_from_settings(settings_text: str):
    d = json.loads(settings_text)
    by_event, total, script = {}, 0, 0
    for event, groups in d.get("hooks", {}).items():
        n = 0
        for g in groups:
            for h in g.get("hooks", []):
                n += 1
                total += 1
                if re.search(r"\.(py|sh)\b", h.get("command", "")):
                    script += 1
        by_event[event] = n
    return {"total": total, "script": script, "by_event": by_event}


def lessons_max(text: str) -> int:
    best = 0
    for line in text.splitlines():
        m = re.match(r"^##\s*L(\d+)\b", line)
        if not m:
            m = re.match(r"^\[\d{4}-\d{2}-\d{2}\][^\n]*?\bL(\d+)\b", line)
        if m:
            best = max(best, int(m.group(1)))
    return best


def biases_max(text: str) -> int:
    return max((int(m.group(1)) for m in
                re.finditer(r"^#{2,4}\s*\*{0,2}B(\d+)\b", text, re.MULTILINE)), default=0)


def principles_max(text: str) -> int:
    return max((int(m.group(1)) for m in
                re.finditer(r"^#{2,3}\s*.*?Principle #(\d+)\b", text, re.MULTILINE)), default=0)


def rules_max(text: str) -> int:
    """Numbered items INSIDE the `## Critical Rules` section only."""
    lines = text.splitlines()
    best, in_section = 0, False
    for line in lines:
        if re.match(r"^##\s+Critical Rules\b", line):
            in_section = True
            continue
        if in_section and re.match(r"^##\s+", line):
            break
        if in_section:
            m = re.match(r"^(\d+)\.\s+\*\*", line)
            if m:
                best = max(best, int(m.group(1)))
    return best


def simple_max(text: str, pattern: str) -> int:
    return max((int(m.group(1)) for m in re.finditer(pattern, text)), default=0)


def compute(repo: Path) -> dict:
    def rd(p):
        return (repo / p).read_text(encoding="utf-8", errors="replace")
    return {
        "hooks": hooks_from_settings((repo / ".claude" / "settings.json").read_text()),
        "lessons_max": lessons_max(rd("research/predictions/lessons.md")),
        "biases_max": biases_max(rd("research/meta/biases-watchlist.md")),
        "principles_max": principles_max(rd("research/meta/methodology.md")),
        "rules_max": rules_max(rd("research/CLAUDE.md")),
        "patterns_max": simple_max(rd("research/meta/cross-domain-pattern-register.md"), r"\bPC?-(\d+)\b"),
        "triangulation_max": simple_max(rd("research/signals/triangulation.md"), r"\bTC-(\d+)\b"),
    }


def render(c: dict) -> str:
    h = c["hooks"]
    by = ", ".join(f"{k} {v}" for k, v in sorted(h["by_event"].items()))
    return (
        "# Computed Counts — regenerated from the territory\n\n"
        "**DO NOT hand-edit.** Regenerate: `python3 research/meta/computed-counts.py --write`.\n"
        "Drift-check (CI/pre-commit): `--check` (exit 2 if this file is stale).\n"
        "Born 2026-07-22 (commission item 5, K3 theme 5). This file is the CANONICAL\n"
        "source for tail counts; prose headers should cite it, not restate numbers.\n\n"
        "| Artifact | Count | Territory source + method |\n"
        "|---|---|---|\n"
        f"| Hooks (script) | {h['script']} | .claude/settings.json entries referencing a .py/.sh |\n"
        f"| Hooks (all entries) | {h['total']} | all command entries ({by}) |\n"
        f"| Lessons (max L#) | {c['lessons_max']} | lessons.md `## L#` + `[date] ...L#` |\n"
        f"| Biases (max B#) | {c['biases_max']} | biases-watchlist.md `### B# —` |\n"
        f"| Principles (max #) | {c['principles_max']} | methodology.md `## Principle #` |\n"
        f"| Critical Rules (max #) | {c['rules_max']} | CLAUDE.md `## Critical Rules` section |\n"
        f"| Patterns (max P/PC-#) | {c['patterns_max']} | cross-domain-pattern-register.md |\n"
        f"| Triangulation (max TC-#) | {c['triangulation_max']} | triangulation.md |\n\n"
        "Note: 'max #' is the highest index defined; some ranges have intentionally\n"
        "skipped/retired numbers (e.g. tombstoned lessons, absent biases) so the\n"
        "count of PRESENT entries can be lower than the max. Max is the tail the\n"
        "prose headers cite.\n")


def _counts_only(text: str) -> str:
    """Extract just the table rows for drift comparison (ignore prose/dates)."""
    return "\n".join(l for l in text.splitlines() if l.startswith("| ") and "---" not in l)


def cmd_write():
    OUT.write_text(render(compute(REPO)))
    print(f"wrote {OUT.relative_to(REPO)}")


def cmd_check() -> int:
    computed = _counts_only(render(compute(REPO)))
    if not OUT.exists():
        print("DRIFT: computed-counts.md does not exist — run --write")
        return 2
    committed = _counts_only(OUT.read_text())
    if computed != committed:
        print("DRIFT DETECTED — computed-counts.md is STALE vs the territory.")
        print("Run: python3 research/meta/computed-counts.py --write  (then re-stage)")
        import difflib
        for line in difflib.unified_diff(committed.splitlines(), computed.splitlines(),
                                         "committed", "computed", lineterm=""):
            print("  " + line)
        return 2
    print("computed-counts.md is current with the territory.")
    return 0


def cmd_audit():
    c = compute(REPO)
    print("=== computed from territory ===")
    print(json.dumps(c, indent=2))
    print("\n=== header-assertion drift scan (best-effort) ===")
    checks = [
        ("research/CLAUDE.md", r"currently (\d+) live", c["hooks"]["script"], "hooks 'currently N live'"),
        ("research/meta/tags.md", r"Principle tail #(\d+)", c["principles_max"], "tags Principle tail"),
        ("research/meta/tags.md", r"B-tail B(\d+)", c["biases_max"], "tags B-tail"),
        ("research/meta/tags.md", r"L-tail L(\d+)", c["lessons_max"], "tags L-tail"),
    ]
    for relpath, pat, expected, label in checks:
        p = REPO / relpath
        if not p.exists():
            continue
        txt = p.read_text(encoding="utf-8", errors="replace")
        found = [int(m.group(1)) for m in re.finditer(pat, txt)]
        for f in found:
            flag = "OK " if f == expected else "DRIFT"
            print(f"  [{flag}] {label}: asserts {f}, territory={expected}")
        if not found:
            print(f"  [n/a ] {label}: no machine-matchable assertion found")


# ---------------------------------------------------------------- selftest
def _selftest() -> int:
    fails = 0

    def check(label, cond):
        nonlocal fails
        print(("OK  " if cond else "XX  ") + label)
        fails += 0 if cond else 1

    # hooks
    st = json.dumps({"hooks": {
        "Stop": [{"hooks": [{"command": "a/x.py"}, {"command": "a/y.py"}]}],
        "SessionStart": [{"hooks": [{"command": "git -C . config core.hooksPath z"},
                                    {"command": "a/s.py"}]}]}})
    h = hooks_from_settings(st)
    check("hooks total counts all entries", h["total"] == 4)
    check("hooks script excludes shell one-liner", h["script"] == 3)
    check("hooks by_event correct", h["by_event"] == {"Stop": 2, "SessionStart": 2})

    # lessons: mixed header + append-log + cross-ref
    lessons = ("## L21 (candidate)\n"
               "## L31 — something\n"
               "[2026-07-20] CANDIDATE L39 — detail != truth\n"
               "some prose referencing L99 mid-sentence should NOT count\n"
               "[2026-07-19] L34 ENRICHMENT — reuse\n")
    check("lessons_max handles header+appendlog, ignores mid-sentence L99",
          lessons_max(lessons) == 39)

    check("biases_max", biases_max("### B1 — a\n### B65 — z\n#### B12 — m\n") == 65)
    check("biases_max ignores mid-text B999",
          biases_max("### B65 — z\nsee B999 elsewhere\n") == 65)

    prin = ("## Principle #31 REFINEMENT — reuse\n"
            "## Principle #47 — new\n"
            "inline mention Principle #99 in prose\n")
    check("principles_max from ## headers only (ignores inline #99)",
          principles_max(prin) == 47)

    rules = ("## Critical Rules\n"
             "1. **First**\n"
             "19. **Nineteenth**\n"
             "## Output Format Rules\n"
             "88. **not a critical rule**\n")
    check("rules_max scoped to Critical Rules section (not 88)", rules_max(rules) == 19)

    check("patterns_max", simple_max("P-1 PC-14 PC-22 P-3", r"\bPC?-(\d+)\b") == 22)
    check("triangulation_max", simple_max("TC-1 TC-19 TC-5", r"\bTC-(\d+)\b") == 19)

    # round-trip: render is stable + _counts_only ignores prose
    c = {"hooks": {"total": 4, "script": 3, "by_event": {"Stop": 2}},
         "lessons_max": 39, "biases_max": 65, "principles_max": 47,
         "rules_max": 19, "patterns_max": 22, "triangulation_max": 19}
    r1 = _counts_only(render(c))
    check("render round-trip stable under counts_only", r1 == _counts_only(render(c)))

    print("ALL PASS" if fails == 0 else f"{fails} MISMATCH")
    return fails


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(_selftest())
    if "--write" in sys.argv:
        cmd_write()
    elif "--check" in sys.argv:
        sys.exit(cmd_check())
    elif "--audit" in sys.argv:
        cmd_audit()
    else:
        print(__doc__.split("\n\n")[0])
        print("modes: --write | --check | --audit | --selftest")
