#!/usr/bin/env python3
"""REWORK-5b: the pre-commit ALARM-LOG APPEND-ONLY guard, driven through the
ACTUAL git-commit activation chain (a real commit in a temp repo with the real
pre-commit hook installed via core.hooksPath) — not by calling a function.

hook-fire-log.md is the structural-output metric's numerator source; a mixed
commit that rewrites/deletes existing fire lines can move the 08-06 scoreboard.
Append must pass; any removal must block; operator override must pass."""
import os, shutil, subprocess, sys, tempfile
from pathlib import Path

REPO = os.environ.get("CLAUDE_PROJECT_DIR") or str(Path(__file__).resolve().parents[3])
PRECOMMIT = os.path.join(REPO, "research", "meta", "hooks", "git", "pre-commit")

fails = 0
def check(label, cond):
    global fails
    print(("OK  " if cond else "XX  ") + label)
    fails += 0 if cond else 1

with tempfile.TemporaryDirectory() as td:
    def g(*a, env=None):
        return subprocess.run(["git", "-C", td, *a], capture_output=True, text=True, env=env)
    g("init", "-q")
    g("config", "user.email", "t@t"); g("config", "user.name", "t")
    # install the REAL pre-commit hook via core.hooksPath (the shipped activation)
    hooks_dir = os.path.join(td, ".githooks")
    os.makedirs(hooks_dir)
    shutil.copy(PRECOMMIT, os.path.join(hooks_dir, "pre-commit"))
    os.chmod(os.path.join(hooks_dir, "pre-commit"), 0o755)
    g("config", "core.hooksPath", ".githooks")
    log = os.path.join(td, "research", "meta", "hook-fire-log.md")
    os.makedirs(os.path.dirname(log))
    Path(log).write_text("- 2026-07-01 00:00:00Z hook FIRE (a)\n"
                         "- 2026-07-02 00:00:00Z hook FIRE (b)\n"
                         "- 2026-07-03 00:00:00Z hook FIRE (c)\n")
    g("add", "-A"); r0 = g("commit", "-qm", "seed log")
    check("seed commit succeeds", r0.returncode == 0)

    # Case A: pure APPEND -> pass
    with open(log, "a") as f:
        f.write("- 2026-07-04 00:00:00Z hook FIRE (d)\n")
    g("add", "-A")
    rA = g("commit", "-qm", "append one fire")
    check("APPEND to fire-log passes", rA.returncode == 0)

    # Case B: REWRITE/DELETE an existing line -> BLOCK
    lines = Path(log).read_text().splitlines()
    del lines[0]  # remove the first (oldest) fire line
    Path(log).write_text("\n".join(lines) + "\n")
    g("add", "-A")
    rB = g("commit", "-qm", "silently drop a fire line")
    check("REWRITE/DELETE of a fire line is BLOCKED", rB.returncode != 0)
    check("block message names append-only", "APPEND-ONLY" in (rB.stdout + rB.stderr))

    # Case C: same deletion WITH operator override -> pass
    env = dict(os.environ, OPERATOR_APPROVED_DELETION="1")
    rC = g("commit", "-qm", "operator-approved prune", env=env)
    check("operator override allows the prune", rC.returncode == 0)

print("ALL PASS" if fails == 0 else f"{fails} MISMATCH")
sys.exit(fails)
