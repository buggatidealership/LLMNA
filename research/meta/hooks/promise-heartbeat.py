#!/usr/bin/env python3
"""LLMNA PROMISE HEARTBEAT (SessionStart) — dated-promise loud-fail layer.

Built 2026-07-22 (accounting-layer commission items 1+4; K3 themes 1 & 4).
Why: two "this is due" audit loops died silently (G-08: the Rule #16 07-15
re-eval vanished from every surface while ~8,952k tokens it was meant to judge
kept accruing). The existing date-catcher (session-start-hook) only scans
todo.md TITLES for recurring keywords; deadlines living in PROSE sentences
("next re-eval: 2026-08-15", "first check 2026-06-08") had no enforcement.

TWO LANES:
  A. REGISTRY (authoritative, blocking-loud): parse
     `research/meta/promises-registry.md`. Any OPEN line past DUE ->
     🚨 OVERDUE banner in session context + one deduped append to
     hook-fire-log.md (committed by the git-check Stop hook -> the miss
     lands in git history; a silent death is now structurally impossible
     as long as sessions start).
  B. PROSE SWEEP (detector, informational): regex over meta/*.md,
     predictions/*.md, research/CLAUDE.md for promise-phrases carrying a
     past date that are (a) not marked done on the same line and (b) not
     already covered by a registry line -> CANDIDATE list, prompting either
     execution or registry adoption. This is the in-prose blind spot K3
     found (theme 4): the scanner reads sentences, not just headers.

Dedupe: state hash at research/meta/.promise-heartbeat-state.json — the
fire-log append happens only when the OVERDUE SET CHANGES (no per-session
spam; the loud banner prints every session while overdue).

Always exits 0 (SessionStart is informational; the LOUDNESS is the product).
Fail-open on exception. Modes: --selftest; default = live hook.
"""
import json
import os
import re
import sys
from datetime import date, datetime, timezone
from pathlib import Path

REPO = Path(os.environ.get("CLAUDE_PROJECT_DIR") or Path(__file__).resolve().parents[3])
REGISTRY = REPO / "research" / "meta" / "promises-registry.md"
LOG = REPO / "research" / "meta" / "hook-fire-log.md"
STATE = REPO / "research" / "meta" / ".promise-heartbeat-state.json"

REG_LINE = re.compile(
    r"^- \[( |x)\] DUE:(\d{4}-\d{2}-\d{2}) \| WHAT: (.*?) \| SOURCE: (.*?)(?:\s*\| DONE:.*)?$")
# any line that PRESENTS as a registry promise (a checkbox bullet), so a
# malformed one is caught instead of silently ignored (rework-3 b/c).
CHECKBOX = re.compile(r"^- \[[ xX]\]")
# a valid close carries a machine-checkable receipt: `RECEIPT:` + non-space value
RECEIPT_RE = re.compile(r"RECEIPT:\s*\S")

# prose promise-phrases: verb-ish promise token within 40 chars of a date
PROSE_PROMISE = re.compile(
    r"(?i)\b(re-eval(?:uation)?|recalibrat\w+|adjudicat\w+|first check|next check|"
    r"next re-eval|review (?:due|at|on)|audit (?:due|at|on)|re-verif\w+|"
    r"due|deadline)\b\D{0,40}?(\d{4}-\d{2}-\d{2})")
PROSE_DONE_MARKERS = re.compile(
    r"(?i)\b(done|executed|completed|resolved|graded|closed|retired|superseded|"
    r"ran|landed|\[x\]|✅|adjudicated on|delivered)\b")

PROSE_SCAN_GLOBS = ["research/meta/*.md", "research/predictions/*.md", "research/CLAUDE.md"]
PROSE_SKIP = {"promises-registry.md", "hook-fire-log.md"}


def parse_registry(text: str, today: date):
    """Return (overdue, upcoming, problems).

    REWORK-3 (K3 finding 3): a promise leaves the loud list ONLY via a
    machine-checkable RECEIPT — an `[x]` with no receipt does NOT close it.
    Lines that present as promises but do not parse (malformed) or carry an
    unparseable date (poison) are surfaced LOUD as `problems`, never silently
    dropped, and one bad line never disables the whole lane.
    """
    overdue, upcoming, problems = [], [], []
    in_fence = False
    for raw in text.splitlines():
        line = raw.strip()
        # skip fenced code blocks — the registry header documents its own line
        # FORMAT inside ``` fences (YYYY-MM-DD placeholders), which must NOT be
        # parsed as promises (adversarial pass on the rework-3 malformed-detector).
        if line.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if not CHECKBOX.match(line):
            continue  # not a promise line at all
        m = REG_LINE.match(line)
        if not m:
            problems.append(("MALFORMED promise line (does not parse — a real "
                             "promise may be hiding here, unwatched)", line[:120]))
            continue
        done, due_s, what, source = m.groups()
        try:
            due = datetime.strptime(due_s, "%Y-%m-%d").date()
        except ValueError:
            problems.append((f"POISON date {due_s!r} (unparseable — promise cannot "
                             "be tracked)", line[:120]))
            continue
        if done.lower() == "x":
            if not RECEIPT_RE.search(line):
                # unreceipted close = a say-do gap INSIDE the registry
                problems.append(("CLOSED [x] with NO machine-checkable RECEIPT — "
                                 "does not count as done", line[:120]))
                if due < today:
                    overdue.append((due_s, what.strip() + "  [INVALID CLOSE: no receipt]",
                                    source.strip()))
            continue
        item = (due_s, what.strip(), source.strip())
        if due < today:
            overdue.append(item)
        elif (due - today).days <= 3:
            upcoming.append(item)
    return overdue, upcoming, problems


def prose_sweep(repo: Path, today: date, registry_text: str):
    """CANDIDATE overdue promises living in prose, not yet in the registry."""
    cands = []
    seen = set()
    for pattern in PROSE_SCAN_GLOBS:
        for p in sorted(repo.glob(pattern)):
            if p.name in PROSE_SKIP or p.name.startswith("."):
                continue
            try:
                text = p.read_text(encoding="utf-8", errors="replace")
            except Exception:
                continue
            for line in text.splitlines():
                if PROSE_DONE_MARKERS.search(line):
                    continue
                for m in PROSE_PROMISE.finditer(line):
                    verb, due_s = m.group(1), m.group(2)
                    try:
                        due = datetime.strptime(due_s, "%Y-%m-%d").date()
                    except ValueError:
                        continue
                    if due >= today:
                        continue
                    key = (p.name, due_s, verb.lower())
                    if key in seen or due_s in registry_text:
                        # a registry line carrying the same date is treated as
                        # coverage; the registry is the authoritative lane
                        continue
                    seen.add(key)
                    snippet = line.strip()[:140]
                    cands.append((due_s, str(p.relative_to(repo)), snippet))
    return cands


def log_fire(events, kind="OVERDUE") -> None:
    """Append the loud event to the git-committed log, THEN update the state hash.

    REWORK-3 (K3 finding 3, ordering): the prior version wrote STATE (the dedupe
    hash) BEFORE the log append. If the append then failed, the hash was already
    advanced, so the next run deduped it away and the event NEVER reached git
    history — a silent death. Now the log line is written FIRST; STATE is updated
    only after the append succeeds, so a failed append leaves STATE stale and the
    event retries next run (it WILL reach history).
    """
    try:
        prev = ""
        if STATE.exists():
            prev = json.loads(STATE.read_text()).get("hash", "")
        import hashlib
        h = hashlib.sha256(json.dumps([kind, sorted(map(str, events))]).encode()).hexdigest()[:16]
        if h == prev:
            return
        ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%SZ")
        with open(LOG, "a", encoding="utf-8") as f:
            f.write(f"- {ts} promise-heartbeat {kind} set changed: "
                    + "; ".join(str(e)[:70] for e in events) + "\n")
        # STATE advanced ONLY after the append is durable (log-before-state).
        STATE.write_text(json.dumps({"hash": h, "at": datetime.now(timezone.utc).isoformat()}))
    except Exception:
        pass


def main() -> None:
    today = date.today()
    if not REGISTRY.exists():
        print("PROMISE-HEARTBEAT: registry missing at research/meta/promises-registry.md "
              "— the promise-tracking layer is DOWN. Recreate it (git log has the last copy).")
        return
    reg_text = REGISTRY.read_text(encoding="utf-8", errors="replace")
    overdue, upcoming, problems = parse_registry(reg_text, today)
    cands = prose_sweep(REPO, today, reg_text)

    if problems:
        # a registry that cannot be trusted to be parsed is itself a failure of
        # the promise-tracking layer — surface LOUD and log it (rework-3 b/c/a).
        log_fire([f"{r} :: {ln}" for r, ln in problems], kind="REGISTRY-PROBLEM")
        print("🚨🚨 PROMISE-HEARTBEAT: REGISTRY INTEGRITY PROBLEMS — lines that present "
              "as promises but cannot be trusted (malformed / poison date / closed with "
              "no receipt). A promise could be hiding in here, unwatched:")
        for reason, ln in problems:
            print(f"  🚨 {reason}\n       {ln}")

    if overdue:
        log_fire(overdue)
        print("🚨🚨 PROMISE-HEARTBEAT: OVERDUE DATED PROMISES — a promised audit/re-eval "
              "is past due and NOT marked done-with-receipt. Silent death is not an option: "
              "execute it this session, or consciously re-date it in promises-registry.md "
              "with a one-line rationale. Ignoring this banner is itself a say–do gap.")
        for d, w, s in overdue:
            print(f"  🚨 OVERDUE since {d}: {w}  [source: {s}]")
    if upcoming:
        print("⏰ PROMISE-HEARTBEAT: due within 3 days:")
        for d, w, s in upcoming:
            print(f"  ⏰ DUE {d}: {w}  [source: {s}]")
    if cands:
        print("🟡 PROMISE-HEARTBEAT prose sweep: past-dated promise-phrases found in prose, "
              "NOT covered by the registry (adopt into promises-registry.md or resolve):")
        for d, f, snip in cands[:15]:
            print(f"  🟡 [{d}] {f}: {snip}")
        if len(cands) > 15:
            print(f"  ... +{len(cands) - 15} more (run promise-heartbeat.py directly for full list)")
    if not (overdue or upcoming or cands or problems):
        print("PROMISE-HEARTBEAT: all dated promises current.")


# ---------------------------------------------------------------- selftest
def _selftest() -> int:
    fails = 0

    def check(label, cond):
        nonlocal fails
        print(("OK  " if cond else "XX  ") + label)
        fails += 0 if cond else 1

    today = date(2026, 7, 22)
    reg = (
        "- [ ] DUE:2026-07-15 | WHAT: overdue thing | SOURCE: a.md\n"
        "- [x] DUE:2026-07-10 | WHAT: done thing | SOURCE: b.md | DONE:2026-07-11 RECEIPT: abc\n"
        "- [ ] DUE:2026-07-23 | WHAT: tomorrow thing | SOURCE: c.md\n"
        "- [ ] DUE:2026-09-01 | WHAT: far thing | SOURCE: d.md\n")
    o, u, pr = parse_registry(reg, today)
    check("overdue open line detected", len(o) == 1 and o[0][1] == "overdue thing")
    check("done line WITH receipt not overdue", all("done thing" not in w for _, w, _ in o))
    check("valid registry has no problems", pr == [])
    check("due-soon window (3d)", len(u) == 1 and u[0][1] == "tomorrow thing")

    # ---- REWORK-3 permanent fixtures (K3 finding 3) ----
    # (a) [x] with NO receipt does NOT close a past-due promise -> overdue + problem
    o, u, pr = parse_registry("- [x] DUE:2026-07-01 | WHAT: unreceipted | SOURCE: a.md\n", today)
    check("REWORK-3a: unreceipted [x] stays OVERDUE",
          any("unreceipted" in w for _, w, _ in o))
    check("REWORK-3a: unreceipted [x] flagged as a problem",
          any("RECEIPT" in r for r, _ in pr))
    # (b) malformed line ("DUE: " trailing space) is surfaced LOUD, not invisible
    o, u, pr = parse_registry("- [ ] DUE: 2026-07-01 | WHAT: malformed | SOURCE: a.md\n", today)
    check("REWORK-3b: malformed line surfaced as a problem (not silent)",
          any("MALFORMED" in r for r, _ in pr))
    # (c) poison date does NOT disable the lane: the real overdue below still surfaces
    o, u, pr = parse_registry(
        "- [ ] DUE:2026-13-99 | WHAT: poison | SOURCE: a.md\n"
        "- [ ] DUE:2026-07-01 | WHAT: real overdue after poison | SOURCE: b.md\n", today)
    check("REWORK-3c: poison date flagged, lane survives (real overdue still seen)",
          any("POISON" in r for r, _ in pr) and any("real overdue" in w for _, w, _ in o))
    # (d) log_fire ordering: log BEFORE state (a failed append must not advance state)
    import inspect as _insp
    src = _insp.getsource(log_fire)
    check("REWORK-3d: log append precedes STATE write (log-before-state)",
          src.index("open(LOG") < src.index("STATE.write_text"))
    # adversarial pass on the malformed-detector: fenced format-example lines
    # (the registry's own ```-fenced docs) must NOT be flagged as problems
    fenced = ("```\n"
              "- [ ] DUE:YYYY-MM-DD | WHAT: <placeholder> | SOURCE: <x>\n"
              "```\n"
              "- [ ] DUE:2026-07-01 | WHAT: real | SOURCE: b.md\n")
    o, u, pr = parse_registry(fenced, today)
    check("REWORK-3 adversarial: fenced format-example not flagged malformed",
          pr == [] and any("real" in w for _, w, _ in o))

    import tempfile
    with tempfile.TemporaryDirectory() as td:
        r = Path(td)
        (r / "research" / "meta").mkdir(parents=True)
        (r / "research" / "meta" / "x.md").write_text(
            "Next re-eval: 2026-07-01 for the widget.\n"          # overdue, uncovered
            "re-eval 2026-07-02 — DONE, executed same day.\n"     # done marker -> skip
            "next check 2026-12-01 later.\n"                       # future -> skip
            "recalibration due 2026-06-30 per plan.\n")            # overdue, uncovered
        (r / "research" / "CLAUDE.md").write_text("audit due 2026-07-03 here.\n")
        cands = prose_sweep(r, today, registry_text="2026-06-30")  # 06-30 covered
        dates = sorted(c[0] for c in cands)
        check("prose sweep finds uncovered past promises",
              "2026-07-01" in dates and "2026-07-03" in dates)
        check("done-marked prose line skipped", "2026-07-02" not in dates)
        check("future prose date skipped", all(d < "2026-07-22" for d in dates))
        check("registry-covered date suppressed", "2026-06-30" not in dates)

    import subprocess
    res = subprocess.run([sys.executable, __file__], input="", capture_output=True, text=True)
    check("live run exits 0", res.returncode == 0)
    print("ALL PASS" if fails == 0 else f"{fails} MISMATCH")
    return fails


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(_selftest())
    try:
        main()
    except Exception as e:
        try:
            print(f"PROMISE-HEARTBEAT: fail-open ({type(e).__name__}) — heartbeat did not run; "
                  "treat as a MISSED BEAT, run manually: python3 research/meta/hooks/promise-heartbeat.py")
        except Exception:
            pass
        sys.exit(0)
