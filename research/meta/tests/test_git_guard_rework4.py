#!/usr/bin/env python3
"""REWORK-4 permanent fixtures (K3 finding 4): global-option-prefixed commit -n,
1>/2> redirects, tee, and cp/install/mv overwrites onto protected paths.

Payloads assembled from fragments so neither this file nor `python3 <file>`
trips the live guard. Every K3-reported bypass is kept here forever, plus FP
controls proving the fix did not over-block (discipline #3)."""
import json, os, subprocess, sys
from pathlib import Path
_REPO = os.environ.get("CLAUDE_PROJECT_DIR") or str(Path(__file__).resolve().parents[3])
HOOK = os.path.join(_REPO, "research", "meta", "hooks", "git-guard-pretooluse.py")


def run(cmd):
    p = json.dumps({"tool_name": "Bash", "tool_input": {"command": cmd}})
    return subprocess.run([sys.executable, HOOK], input=p, capture_output=True, text=True).returncode


N = "-" + "n"
GT = ">"
COMMIT = "commit "
cases = [
    # ---- commit-n reached via git GLOBAL OPTIONS (K3 finding 4) -> BLOCK ----
    ("commit-n via -c x=1",          "git -c x=1 " + COMMIT + N + " -m x", 2),
    ("commit-n via --no-pager",      "git --no-pager " + COMMIT + N + " -m x", 2),
    ("commit-n via --no-pager -nm",  "git --no-pager " + COMMIT + "-nm x", 2),
    ("commit-n via -C path",         "git -C " + _REPO + " " + COMMIT + N + " -m x", 2),
    ("commit-n via -c hookspath",    "git -c core.hooksPath=/x " + COMMIT + N + " -m x", 2),
    # ---- fd redirects onto protected (the [^>0-9] hole) -> BLOCK ----
    ("redirect 1> protected",        "echo x 1" + GT + " research/CLAUDE.md", 2),
    ("redirect 2> protected",        "echo x 2" + GT + " research/meta/methodology.md", 2),
    ("redirect 1>nospace",           "echo x 1" + GT + "research/CLAUDE.md", 2),
    # ---- tee onto protected -> BLOCK ----
    ("tee protected",                "echo x | tee research/CLAUDE.md", 2),
    ("tee into protected dir",       "echo x | tee research/meta/hooks/z.py", 2),
    # ---- cp/install/mv onto protected dest -> BLOCK ----
    ("cp onto CLAUDE.md",            "cp /dev/null research/CLAUDE.md", 2),
    ("cp onto methodology",          "cp evil.md research/meta/methodology.md", 2),
    ("install onto protected",       "install -m644 evil research/CLAUDE.md", 2),
    ("mv onto protected",            "mv evil.md research/CLAUDE.md", 2),
    ("cp into protected dir",        "cp evil research/meta/hooks/x.py", 2),
    # ---- FP controls: MUST still pass (0) ----
    ("CTRL 2>&1 dup",                "echo x 2" + GT + "&1 | tee /tmp/log", 0),
    ("CTRL normal commit",           "git " + COMMIT + "-m x", 0),
    ("CTRL cp FROM protected",       "cp research/CLAUDE.md /tmp/backup.md", 0),
    ("CTRL backup TO .bak (not overwrite)", "cp research/CLAUDE.md research/CLAUDE.md.bak", 0),
    ("CTRL tee -a append",           "echo x | tee -a /tmp/note.txt", 0),
    ("CTRL tee scratch",             "echo x | tee /tmp/note.txt", 0),
    ("CTRL redirect scratch",        "echo x " + GT + " /tmp/out.txt", 0),
    ("CTRL cp scratch to scratch",   "cp /tmp/a /tmp/b", 0),
    ("CTRL git log then grep",       "git log --oneline | grep " + COMMIT.strip(), 0),
]
fails = 0
for label, cmd, exp in cases:
    got = run(cmd); ok = got == exp; fails += (0 if ok else 1)
    verdict = "BYPASS!" if (exp == 2 and got == 0) else ("FP!" if (exp == 0 and got == 2) else "")
    print(f"{'OK ' if ok else 'XX '}{label}: got={got} exp={exp} {verdict}")
print("ALL PASS" if fails == 0 else f"{fails} MISMATCH")
sys.exit(fails)
