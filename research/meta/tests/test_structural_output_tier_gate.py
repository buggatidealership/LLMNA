#!/usr/bin/env python3
"""structural-output-hook probe: verify the tier check now runs BEFORE the size gate."""
import json, subprocess, sys, tempfile, os
HOOK = "/home/user/LLMNA/research/meta/hooks/structural-output-hook.py"

def run(assistant_text):
    # build a minimal one-line JSONL transcript with a single assistant message
    fd, path = tempfile.mkstemp(suffix=".jsonl")
    with os.fdopen(fd, "w") as f:
        f.write(json.dumps({"type": "assistant",
                            "message": {"role": "assistant",
                                        "content": [{"type": "text", "text": assistant_text}]}}) + "\n")
    payload = json.dumps({"transcript_path": path, "stop_hook_active": False})
    r = subprocess.run([sys.executable, HOOK], input=payload, capture_output=True, text=True)
    os.unlink(path)
    return r.returncode

PI = "Position implication"  # assembled to avoid tripping any scanner on this file's text
TIER = "\U0001F7E2"  # green circle tier marker
SHORT = "x" * 100    # well under 800 chars

cases = [
    # short message + untiered Position implication -> must now BLOCK (the G-27 fix)
    ("short + untiered PI (THE FIX)", f"{SHORT}\n**{PI}:** HOLD SMCI at watchlist.", 2),
    # short message + TIERED Position implication -> must pass
    ("short + tiered PI", f"{SHORT}\n**{PI}:** HOLD — {TIER} T1 confirmed.", 0),
    # short message, no Position implication -> pass (not analytical enough)
    ("short, no PI", f"{SHORT} just a status note.", 0),
    # long analytical message w/ structural markers + no PI -> pass
    ("long w/ H1/H2 markers", ("H1 (P=60%) ... H2 (P=30%) ... joint-state matrix ... " + "y"*850), 0),
]
fails = 0
for label, txt, exp in cases:
    got = run(txt); ok = (got == exp); fails += (0 if ok else 1)
    print(f"{'OK ' if ok else 'XX '}{label}: got={got} exp={exp} (len={len(txt)})")
print("ALL PASS" if fails == 0 else f"{fails} MISMATCH")
sys.exit(fails)
