#!/usr/bin/env python3
"""Harness supervisor — READ-ONLY state report (built 2026-08-02, operator-proposed).

WHY THIS EXISTS
---------------
Operator, 2026-08-02: *"I can verify the morning brief and the evening brief because
I see them. But I can't see what's on the to-do list and what hasn't been done yet."*

That is an OBSERVABILITY gap, not an execution gap. The parts of the harness the
operator sees are checked by him; everything else is checked by nobody. This script
makes the unseen part visible in one command.

WHAT IT IS NOT
--------------
It does not execute anything. It does not fix anything. It writes nothing except an
optional dated ledger row. The operator's proposal included an auto-executor for
overdue to-dos; that half is deliberately NOT built here — see
`meta/redteam/2026-08-02-supervisor-loop-design.md` for why (to-do list becomes a
privilege-escalation channel; and a backlog that is ~26% older than 30 days should be
TRIAGED before it is automated).

USAGE
  python3 harness_supervisor.py            # state report
  python3 harness_supervisor.py --ledger   # also append a dated row
"""
import argparse, datetime, json, pathlib, re, subprocess, sys

REPO = pathlib.Path(__file__).resolve().parents[3]
RESEARCH = REPO / "research"
HOOKS = RESEARCH / "meta" / "hooks"
FIRELOG = RESEARCH / "meta" / "hook-fire-log.md"
TODO = RESEARCH / "meta" / "todo.md"
SETTINGS = REPO / ".claude" / "settings.json"
LEDGER = RESEARCH / "meta" / "supervisor-ledger.md"

# Shared helper modules that are imported by hooks, never registered as hooks.
# Listing them explicitly stops the wiring check reporting a false "cannot fire".
HELPERS = {"hook_fire_log.py"}

SILENT_DAYS = 14        # a wired hook with no log entry in this many days is flagged
STALE_DAYS = 30         # a to-do older than this is triage-eligible, not just late


def today():
    return datetime.date.today()


def hook_state():
    """Per-hook: wired into settings.json? last logged fire? total logged fires?

    Falsifier: a hook classified WIRED-BUT-SILENT is not doing its job.
    Blind-check: distinguishes "hook never fired" from "hook fired and was useful"
      · reads on entries in meta/hook-fire-log.md
      · goes blind if a hook does not WRITE to the fire log at all — it then reads
        identically to a dead hook, which is exactly the case for the four hooks
        flagged NO-LOG below, at least two of which provably run every session.
        Only an execution probe distinguishes these; this instrument cannot.
    """
    blob = SETTINGS.read_text() if SETTINGS.exists() else ""
    log = FIRELOG.read_text(errors="replace") if FIRELOG.exists() else ""
    out = []
    for p in sorted(HOOKS.glob("*.py")):
        if p.name in HELPERS:
            continue
        wired = p.name in blob
        hits = re.findall(r"(\d{4}-\d{2}-\d{2})[T ][\d:]+Z?\s+" + re.escape(p.stem), log)
        if hits:
            last = max(hits)
            age = (today() - datetime.date(*map(int, last.split("-")))).days
            state = "LIVE" if age <= SILENT_DAYS else "SILENT"
        else:
            last, age, state = "never", None, "NO-LOG"
        out.append(dict(name=p.stem, wired=wired, last=last, age=age,
                        fires=len(hits), state=state))
    return out


def backlog():
    """Open to-do items by age.

    Falsifier: if >50% of open items are past their date, the list is a wish-list
      rather than a queue and the dates carry no information.
    Blind-check: distinguishes "items are late" from "items are dead"
      · reads on the date stamp in each `- [ ] **P# / cat / YYYY-MM-DD**` header
      · goes blind if items are silently re-dated instead of completed — the age
        distribution then looks healthy while nothing has actually shipped. Only a
        git-blame on the date field would catch that; not implemented here.
    """
    txt = TODO.read_text(errors="replace") if TODO.exists() else ""
    rows = re.findall(r"^- \[ \] \*\*(P\d) / (\w+) / (\d{4}-\d{2}-\d{2})\*\*", txt, re.M)
    items = []
    for pri, cat, d in rows:
        age = (today() - datetime.date(*map(int, d.split("-")))).days
        items.append(dict(pri=pri, cat=cat, date=d, age=age))
    return items


def detector_compliance():
    """Roll up the #51 blind-check reading so one command shows the whole state."""
    tool = RESEARCH / "meta" / "tools" / "blind_check_audit.py"
    if not tool.exists():
        return None
    try:
        r = subprocess.run([sys.executable, str(tool)], capture_output=True,
                           text=True, timeout=120, cwd=REPO)
        base = re.search(r"BASELINE cohort\s*:\s*(\S+)\s*compliant\s*\(([^)]+)\)", r.stdout)
        new = re.search(r"NEW cohort \(post-#51\)\s*:\s*(\S+)\s*compliant\s*\(([^)]+)\)", r.stdout)
        return dict(baseline=base.group(1) if base else "?",
                    baseline_pct=base.group(2) if base else "?",
                    new=new.group(1) if new else "?",
                    new_pct=new.group(2) if new else "?")
    except Exception as e:
        return dict(error=str(e))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ledger", action="store_true")
    a = ap.parse_args()

    hooks = hook_state()
    items = backlog()
    comp = detector_compliance()

    unwired = [h for h in hooks if not h["wired"]]
    nolog = [h for h in hooks if h["state"] == "NO-LOG"]
    silent = [h for h in hooks if h["state"] == "SILENT"]
    live = [h for h in hooks if h["state"] == "LIVE"]

    overdue = [i for i in items if i["age"] > 0]
    stale = [i for i in items if i["age"] > STALE_DAYS]
    p0_over = [i for i in overdue if i["pri"] == "P0"]
    p1_over = [i for i in overdue if i["pri"] == "P1"]

    print("=" * 72)
    print(f"HARNESS SUPERVISOR — read-only state report — {today().isoformat()}")
    print("=" * 72)

    print(f"\nHOOKS ({len(hooks)} registered-eligible)")
    print(f"  wired into settings.json : {len(hooks)-len(unwired)}/{len(hooks)}")
    print(f"  LIVE   (logged <={SILENT_DAYS}d)   : {len(live)}")
    print(f"  SILENT (logged >{SILENT_DAYS}d)    : {len(silent)}")
    print(f"  NO-LOG (never logged)    : {len(nolog)}")
    for h in sorted(hooks, key=lambda x: (x["state"] != "NO-LOG", x["state"] != "SILENT", x["name"])):
        if h["state"] == "LIVE":
            continue
        w = "" if h["wired"] else " [NOT WIRED]"
        print(f"    - {h['name']:<40} {h['state']:<7} last={h['last']}{w}")
    print("  ⚠ BLIND-CHECK: this reads the fire LOG. A hook that runs but never logs")
    print("    is indistinguishable from a dead hook. NO-LOG != dead. Resolving that")
    print("    needs an execution probe, which this instrument does not do.")

    print(f"\nBACKLOG ({len(items)} open)")
    print(f"  past their date : {len(overdue)} ({100*len(overdue)//max(len(items),1)}%)")
    print(f"  older than {STALE_DAYS}d  : {len(stale)}  <- triage candidates, not just late")
    print(f"  P0 overdue      : {len(p0_over)}")
    print(f"  P1 overdue      : {len(p1_over)}")
    for i in sorted(p0_over, key=lambda x: -x["age"]):
        print(f"    - P0 {i['cat']:<12} {i['date']}  {i['age']}d overdue")

    if comp:
        print("\nDETECTORS (#51 blind-check compliance)")
        if "error" in comp:
            print(f"  ERROR: {comp['error']}")
        else:
            print(f"  baseline cohort : {comp['baseline']} ({comp['baseline_pct']})")
            print(f"  NEW cohort      : {comp['new']} ({comp['new_pct']})  <- the cohort #51 binds")

    verdict = []
    if unwired:
        verdict.append(f"{len(unwired)} hook(s) NOT WIRED")
    if nolog or silent:
        verdict.append(f"{len(nolog)+len(silent)} hook(s) unobservable")
    if p0_over:
        verdict.append(f"{len(p0_over)} P0 overdue")
    if stale:
        verdict.append(f"{len(stale)} to-dos >{STALE_DAYS}d")
    print("\nVERDICT: " + ("; ".join(verdict) if verdict else "clean"))
    print("=" * 72)

    if a.ledger:
        row = (f"| {today().isoformat()} | {len(hooks)-len(unwired)}/{len(hooks)} | "
               f"{len(live)}/{len(silent)}/{len(nolog)} | {len(items)} | {len(overdue)} | "
               f"{len(stale)} | {len(p0_over)} | "
               f"{comp.get('new','?') if comp else '?'} |\n")
        if not LEDGER.exists():
            LEDGER.write_text(
                "# Supervisor ledger — dated harness state readings\n\n"
                "Append-only. Produced by `meta/tools/harness_supervisor.py --ledger`.\n"
                "**A missing date row is itself a finding** — the gap is the evidence\n"
                "that the supervisor pass did not run.\n\n"
                "| date | hooks wired | live/silent/nolog | open todos | overdue | >30d | P0 overdue | #51 NEW cohort |\n"
                "|---|---|---|---|---|---|---|---|\n")
        with LEDGER.open("a") as fh:
            fh.write(row)
        print(f"ledger appended -> {LEDGER.relative_to(RESEARCH)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
