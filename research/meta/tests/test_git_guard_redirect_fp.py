#!/usr/bin/env python3
"""git-guard REDIRECT false-positive battery (commission item 6, 2026-07-22).

The old redirect check `(^|[^>])>\\s*[^>|;&]*(PROTECTED)` let the protected
NAME be anywhere downstream of a `>`, across newlines — so a heredoc commit
message that merely mentioned CLAUDE.md after `cat > /tmp/msg.txt` false-blocked
(reproduced LIVE 2× while committing items 5 and this one). Fix anchors the
protected match to the immediate redirect TARGET token. These fixtures pin both
the closed FPs and the still-live real catches so the anchor can't loosen back."""
import json, os, subprocess, sys
from pathlib import Path
_REPO = os.environ.get("CLAUDE_PROJECT_DIR") or str(Path(__file__).resolve().parents[3])
HOOK = os.path.join(_REPO, "research", "meta", "hooks", "git-guard-pretooluse.py")


def run(cmd):
    p = json.dumps({"tool_name": "Bash", "tool_input": {"command": cmd}})
    return subprocess.run([sys.executable, HOOK], input=p, capture_output=True, text=True).returncode


GT = ">"  # assembled so this test file's own text can't trip a scanner
cases = [
    # ---- FPs that must now PASS (target token is NOT protected) ----
    ("FP heredoc msg mentions CLAUDE.md (LIVE repro)",
     'cat ' + GT + ' /tmp/msg.txt <<E\nfix the CLAUDE.md count drift\nE', 0),
    ("FP redirect to scratch, body names methodology",
     'echo "see methodology" ' + GT + ' /tmp/note.txt', 0),
    ("FP redirect to tmp, later word portfolio",
     'printf x ' + GT + ' /tmp/x && echo portfolio done', 0),
    ("FP append (>>) to a protected file is NOT truncating",
     'echo x ' + GT + GT + ' research/meta/hook-fire-log.md', 0),
    ("FP stderr dup 2>&1 with protected mention",
     'python3 research/meta/methodology-check.py 2' + GT + '&1 | tee /tmp/l', 0),
    # ---- real catches that must STILL BLOCK (protected IS the target) ----
    ("REAL truncate CLAUDE.md", 'echo x ' + GT + ' research/CLAUDE.md', 2),
    ("REAL truncate methodology", 'cat foo ' + GT + ' research/meta/methodology.md', 2),
    ("REAL truncate settings.json", 'echo {} ' + GT + ' .claude/settings.json', 2),
    ("REAL truncate quoted target", 'echo x ' + GT + ' "research/meta/lessons.md"', 2),
    ("REAL truncate portfolio file", 'echo x ' + GT + ' portfolio/holdings.md', 2),
]
fails = 0
for label, cmd, exp in cases:
    got = run(cmd); ok = got == exp; fails += (0 if ok else 1)
    print(f"{'OK ' if ok else 'XX '}{label}: got={got} exp={exp}")
print("ALL PASS" if fails == 0 else f"{fails} MISMATCH")
sys.exit(fails)
