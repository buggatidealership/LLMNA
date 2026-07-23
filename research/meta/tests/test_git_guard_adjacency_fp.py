#!/usr/bin/env python3
"""Extra probe for the git-commit-adjacency tightening.
FP reduced from 'any commit -n in text' to 'only literal git-commit-n adjacency'."""
import json, os, subprocess, sys
HOOK = os.path.join(os.environ.get("CLAUDE_PROJECT_DIR") or "/home/user/LLMNA",
                    "research", "meta", "hooks", "git-guard-pretooluse.py")
def run(cmd):
    p = json.dumps({"tool_name": "Bash", "tool_input": {"command": cmd}})
    return subprocess.run([sys.executable, HOOK], input=p, capture_output=True, text=True).returncode
C = "git " + "commit "
cases = [
    # prose WITHOUT git-commit adjacency -> now PASS (the fix)
    ("prose 'commit -n' no-git-adj", 'echo ' + '"the commit -n flag skips hooks"', 0),
    ("prose git-guard: commit -n",   'cat f << E\n' + "guard note: commit -n bypass\nE", 0),
    ("prose 'commit' then later -n",  'echo ' + '"commit stuff" && ls -n', 0),
    # real invocations -> BLOCK
    ("REAL git commit -n",       C + "-n -m x", 2),
    ("REAL git commit -nm",      C + "-nm x", 2),
    # benign real commit -> PASS
    ("BENIGN git commit -m",     C + "-m x", 0),
    ("BENIGN msg mentions -n",   C + '-m "close -n hole"', 0),
    # RESOLVED 07-23 audit (was documented residual, pinned exit 2): echo/printf
    # args are data-spans, stripped before the -n scan — prose no longer blocks.
    ("RESOLVED echo git-commit-n prose", 'echo ' + '"run git ' + "commit -n" + ' to skip"', 0),
    # invariant preserved by the data-span stripping: a shell -c payload IS an
    # executed command and must still be scanned (07-23 pin).
    ("PIN bash -c inner commit -n", 'bash -c "git ' + "commit -n" + ' -m x"', 2),
    ("PIN sh -c inner commit -nm",  'sh -c "git ' + "commit -nm" + ' x"', 2),
    # 07-23 fix pin: -n AFTER the message region (the 07-21 regression class)
    ("PIN commit -m then -n", C + '-m "x" -n', 2),
    ("PIN commit -F then -n", C + "-F /tmp/m.txt -n", 2),
]
f = 0
for label, cmd, exp in cases:
    got = run(cmd); ok = got == exp; f += (0 if ok else 1)
    print(f"{'OK ' if ok else 'XX '}{label}: got={got} exp={exp}")
print("ALL PASS" if f == 0 else f"{f} MISMATCH")
sys.exit(f)
