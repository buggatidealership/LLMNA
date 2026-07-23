#!/usr/bin/env python3
"""structural-output-hook probe: tier check runs BEFORE the size gate (G-27),
the PI matcher is case-insensitive (07-23 audit fix), and house-standard
structural markers ("joint-state matrix" hyphenated, "H1 (P=60%)" inline
weights) are credited (07-23 audit: case-4 born-red root cause was the hook's
marker list, not this fixture — the expectation stood, the hook was widened).

Path is CLAUDE_PROJECT_DIR-relative (07-23 audit fix: was hardcoded)."""
import json, subprocess, sys, tempfile, os
ENV = dict(os.environ, LLMNA_PROBE="1")  # probe-tag fires (07-23, G-28)

REPO = os.environ.get("CLAUDE_PROJECT_DIR") or "/home/user/LLMNA"
HOOK = os.path.join(REPO, "research", "meta", "hooks", "structural-output-hook.py")

def run(assistant_text):
    # build a minimal one-line JSONL transcript with a single assistant message
    fd, path = tempfile.mkstemp(suffix=".jsonl")
    with os.fdopen(fd, "w") as f:
        f.write(json.dumps({"type": "assistant",
                            "message": {"role": "assistant",
                                        "content": [{"type": "text", "text": assistant_text}]}}) + "\n")
    payload = json.dumps({"transcript_path": path, "stop_hook_active": False})
    r = subprocess.run([sys.executable, HOOK], input=payload, capture_output=True, text=True, env=ENV)
    os.unlink(path)
    return r.returncode

PI = "Position implication"   # assembled to avoid tripping any scanner on this file's text
PI_LOWER = "position implication"
PI_UPPER = "POSITION IMPLICATION"
PI_TITLE = "Position Implication"
TIER = "\U0001F7E2"  # green circle tier marker
SHORT = "x" * 100    # well under 800 chars

cases = [
    # --- original G-27 fixture set ---
    # short message + untiered Position implication -> must BLOCK (the G-27 fix)
    ("short + untiered PI (G-27)", f"{SHORT}\n**{PI}:** HOLD SMCI at watchlist.", 2),
    # short message + TIERED Position implication -> must pass
    ("short + tiered PI", f"{SHORT}\n**{PI}:** HOLD — {TIER} T1 confirmed.", 0),
    # short message, no Position implication -> pass (not analytical enough)
    ("short, no PI", f"{SHORT} just a status note.", 0),
    # long analytical message w/ house-standard structural markers + no PI -> pass
    # (was born-red: hook didn't credit hyphenated joint-state / H1 (P=60%) forms)
    ("long w/ house markers (case 4)", ("H1 (P=60%) ... H2 (P=30%) ... joint-state matrix ... " + "y"*850), 0),
    # --- 07-23 casing fixtures (PI matcher IGNORECASE fix, 6 cases) ---
    ("c1 lowercase untiered -> BLOCK", f"{SHORT}\n**{PI_LOWER}:** HOLD at watchlist.", 2),
    ("c2 lowercase tiered -> pass", f"{SHORT}\n**{PI_LOWER}:** HOLD — {TIER} confirmed.", 0),
    ("c3 UPPERCASE untiered -> BLOCK", f"{SHORT}\n{PI_UPPER}: TRIM to 12 pct.", 2),
    ("c4 Title Case untiered -> BLOCK", f"{SHORT}\n{PI_TITLE}: ENTER small.", 2),
    ("c5 lowercase, tier on line ABOVE -> pass", f"{SHORT}\n{TIER} directional read\n{PI_LOWER}: HOLD.", 0),
    ("c6 mixed-case mid-sentence untiered -> BLOCK", f"{SHORT}\nSo the {PI_LOWER}: NO ACTION here.", 2),
]
fails = 0
for label, txt, exp in cases:
    got = run(txt); ok = (got == exp); fails += (0 if ok else 1)
    print(f"{'OK ' if ok else 'XX '}{label}: got={got} exp={exp} (len={len(txt)})")
print("ALL PASS" if fails == 0 else f"{fails} MISMATCH")
sys.exit(fails)
