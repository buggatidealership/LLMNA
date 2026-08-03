#!/usr/bin/env python3
"""Backlog forced-ranking (Option B) — propose a cut, optionally apply it.

Spec + kill criteria: meta/backlog-forced-ranking-spec.md
Operator decision 2026-08-03: B ("which 30 of these 75?") over A (time expiry).

THE ONE RULE THAT DEFINES THIS TOOL: **age carries zero weight.** A time-based
rule would have killed the FX-sensitivity item at 33 days stale — the item that
named the gap which opened on 2026-08-01. Age measures attention, not value, and
attention is the faculty that is failing. The moment age enters the score, this
degrades into Option A wearing a ranking's clothes.

Usage:
  python3 backlog_rank.py                 # propose the cut (writes nothing)
  python3 backlog_rank.py --apply         # park everything below the line
  python3 backlog_rank.py --size 40       # different cut size
  python3 backlog_rank.py --revive "SUBSTR"# pull one item back out of Parked
"""
import argparse
import datetime
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
TODO = REPO / "research" / "meta" / "todo.md"
RESEARCH = REPO / "research"
HOLDINGS = RESEARCH / "portfolio" / "holdings.md"
PARKED_HDR = "## Parked (did not make the weekly cut — revive freely)"
DEFAULT_SIZE = 30

HELD_FALLBACK = ["MURATA", "SUMCO", "SKHY", "SK HYNIX", "SNDK", "ARM", "KIOXIA", "NBIS"]
ITEM_RE = re.compile(r"^- \[ \] \*\*(P\d) / ([\w-]+) / ([^\*]+)\*\*", re.M)


def held_names():
    try:
        txt = HOLDINGS.read_text(errors="replace").upper()
    except Exception:
        return HELD_FALLBACK
    found = [n for n in HELD_FALLBACK if n in txt]
    return found or HELD_FALLBACK


def recent_corpus_terms(days=14):
    """Words appearing in files git-modified recently — the LIVE RELEVANCE signal."""
    try:
        since = (datetime.date.today() - datetime.timedelta(days=days)).isoformat()
        r = subprocess.run(["git", "log", f"--since={since}", "--name-only",
                            "--pretty=format:"], cwd=REPO, capture_output=True,
                           text=True, timeout=30)
        files = {f for f in r.stdout.split("\n") if f.strip().endswith(".md")}
        blob = ""
        for f in list(files)[:120]:
            p = REPO / f
            if p.exists():
                blob += p.read_text(errors="replace")[:20000].lower()
        return blob
    except Exception:
        return ""


def parse_items(txt):
    """Split the Open section into (header, body) blocks."""
    # NB: "## Archive" also appears in the file's own how-to-use prose ABOVE the
    # Open section, so a naive .index() returns a section of negative length. Use
    # line-anchored matches and take the first terminator that comes AFTER Open.
    mo = re.search(r"^## Open\s*$", txt, re.M)
    start = mo.start() if mo else 0
    end = len(txt)
    for pat in (re.escape(PARKED_HDR), r"^## Archive"):
        m = re.search(pat, txt[start + 8:], re.M)
        if m:
            end = min(end, start + 8 + m.start())
    section = txt[start:end]
    blocks = re.split(r"(?=^- \[ \] \*\*P\d)", section, flags=re.M)
    items = []
    for b in blocks:
        m = ITEM_RE.match(b)
        if m:
            items.append(dict(pri=m.group(1), cat=m.group(2),
                              date=m.group(3).strip(), text=b, head=b.split("\n")[0]))
    return items, start, end


def score(item, held, recent_blob, today):
    """Four components. NONE of them is age. See spec §3."""
    s, why = 0, []

    # CALENDAR (0-40) — a dated trigger inside 30 days, or an explicit due tag
    cal = 0
    dates = re.findall(r"(20\d\d-\d\d-\d\d)", item["text"])
    for d in dates:
        try:
            dd = datetime.date(*map(int, d.split("-")))
        except ValueError:
            continue
        delta = (dd - today).days
        if 0 <= delta <= 30:
            cal = max(cal, 40 - int(delta * 0.7))
        elif -7 <= delta < 0:
            cal = max(cal, 30)          # just-missed dates are urgent, not stale
    if re.search(r"\[[^\]]*\b(DUE|CAL)\b", item["head"]):
        cal = max(cal, 22)
    s += cal
    if cal:
        why.append(f"cal+{cal}")

    # POSITION (0-25) — real money is exposed to this
    hits = [h for h in held if h.lower() in item["text"].lower()]
    if hits:
        s += 25
        why.append(f"pos+25({','.join(hits[:3])})")

    # PRIORITY (0-20)
    pw = {"P0": 20, "P1": 14, "P2": 6, "P3": 2}[item["pri"]]
    s += pw
    why.append(f"pri+{pw}")

    # LIVE RELEVANCE (0-15) — referenced by work touched in the last 14 days
    key = re.sub(r"[^a-z0-9 ]", " ", item["head"].lower())
    toks = [t for t in key.split() if len(t) > 6][:6]
    if toks and recent_blob:
        hitn = sum(1 for t in toks if t in recent_blob)
        if hitn:
            v = min(15, hitn * 4)
            s += v
            why.append(f"live+{v}")

    return s, " ".join(why)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--size", type=int, default=DEFAULT_SIZE)
    ap.add_argument("--revive", type=str)
    a = ap.parse_args()

    txt = TODO.read_text(errors="replace")
    today = datetime.date.today()

    if a.revive:
        if PARKED_HDR not in txt:
            print("no Parked section"); return 1
        head, parked = txt.split(PARKED_HDR, 1)
        blocks = re.split(r"(?=^- \[ \] \*\*P\d)", parked, flags=re.M)
        keep, moved = [], []
        for b in blocks:
            (moved if (ITEM_RE.match(b) and a.revive.lower() in b.lower()) else keep).append(b)
        if not moved:
            print(f"no parked item matching {a.revive!r}"); return 1
        for b in moved:
            print("REVIVED:", re.sub(r"\s+", " ", b.split("\n")[0])[:110])
        body = re.sub(r"\n  - _Parked \d{4}-\d{2}-\d{2}[^\n]*_", "", "".join(moved))
        out = head.replace("## Archive", body.rstrip() + "\n\n## Archive", 1) \
            if "## Archive" in head else head + body
        TODO.write_text(out + PARKED_HDR + "".join(keep))
        print("\n⚠️  KILL-CRITERION EVENT: if this revival happened because reality")
        print("    forced it, that is the FX-class failure — log which score")
        print("    component missed it (spec §4, row 4).")
        return 0

    items, start, end = parse_items(txt)
    if not items:
        print("no open items parsed"); return 1
    held, blob = held_names(), recent_corpus_terms()
    for it in items:
        it["score"], it["why"] = score(it, held, blob, today)
    items.sort(key=lambda x: -x["score"])

    # P0s are force-included; a P0 below the line is the flag that matters most
    p0_below = [i for i in items[a.size:] if i["pri"] == "P0"]
    keep = items[:a.size] + p0_below
    keep_ids = {id(i) for i in keep}
    park = [i for i in items if id(i) not in keep_ids]

    print(f"BACKLOG FORCED RANKING — {today} — cut size {a.size}")
    print(f"  open: {len(items)}  ->  keep: {len(keep)}  park: {len(park)}")
    print(f"  (age carries ZERO weight, by design — spec §1)\n")
    print("KEEP (top of the cut):")
    for i in keep[:12]:
        print(f"  {i['score']:3d}  {i['pri']} {re.sub(chr(10),' ',i['head'])[:96]}")
        print(f"       {i['why']}")
    if p0_below:
        print("\n🔴 P0s FORCE-INCLUDED THAT DID NOT EARN A SLOT:")
        for i in p0_below:
            print(f"  {i['score']:3d}  {re.sub(chr(10),' ',i['head'])[:100]}")
        print("  ^ we called these P0 and then ranked them below "
              f"{a.size} other things. That contradiction is the point.")
    print(f"\nPARK ({len(park)}) — lowest 8 shown:")
    for i in park[-8:]:
        print(f"  {i['score']:3d}  {i['pri']} {re.sub(chr(10),' ',i['head'])[:96]}")

    if not a.apply:
        print("\n(proposal only — nothing written. re-run with --apply to park)")
        return 0

    body = txt[:start] + "## Open\n\n" + "".join(
        i["text"] if i["text"].endswith("\n") else i["text"] + "\n" for i in keep)
    stamp = f"\n  - _Parked {today} — did not make the cut of {a.size}. Revive freely: `backlog_rank.py --revive \"...\"`_\n"
    parked_body = PARKED_HDR + "\n\n"
    parked_body += (f"_Cut of {today}: {len(park)} items parked, {len(keep)} kept. "
                    f"Parking is reversible and deliberately visible — an item that is "
                    f"proposed, cut, revived and cut again is telling us something a "
                    f"clock never would. Kill criteria: `meta/backlog-forced-ranking-spec.md` §4._\n\n")
    for i in park:
        t = i["text"].rstrip("\n")
        parked_body += t + stamp
    old_parked = ""
    if PARKED_HDR in txt:
        old_parked = txt.split(PARKED_HDR, 1)[1]
    tail = txt[end:]
    TODO.write_text(body + "\n" + parked_body + "\n" + old_parked + tail)
    print(f"\nAPPLIED — {len(park)} parked, {len(keep)} kept.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
