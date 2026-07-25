#!/usr/bin/env python3
import os as _os
from pathlib import Path as _Path
_REPO_ROOT = _os.environ.get("CLAUDE_PROJECT_DIR") or str(_Path(__file__).resolve().parents[3])
"""
LLM-native priming UserPromptSubmit hook for the AI Sector Research OS.

Fires when user submits a prompt, BEFORE Claude generates a response.
Injects an LLM-native discipline checklist into the context to bias
the sampling distribution toward multi-dimensional reasoning rather
than human-analyst sequential prose.

Why this exists (codified 2026-06-01 per user observation):

  User verbatim 2026-06-01: "what I've observed is that you tend to
  always revert to human analysis which is linear instead of trying
  multilateral and dimensional analysis that is LLM native."

  The 12 existing Stop hooks catch failures POST-HOC — after the
  output is generated. Stop hooks prune but cannot prevent the
  generation. UserPromptSubmit is the ONLY architectural event that
  fires BEFORE Claude generates a single token. Injection here biases
  the sampling distribution from the start.

  This hook does NOT replace Stop hooks. It brackets the generation:
    UserPromptSubmit (priming) -> generation -> Stop (pruning)

Architectural rationale:
  - The model generates token-by-token; by the time any hook can
    inspect output, generation is complete.
  - "Pre-commit failure prevention" at the model level is technically
    impossible.
  - The closest approximation: bias the sampling distribution toward
    success-patterns BEFORE generation begins.
  - UserPromptSubmit injection is the only event where this is possible.

Behavior:
  - In-scope (research OS repo) only
  - Skip exemptions: short queries (<50 chars), meta-discussion of
    hooks/principles/files, slash commands
  - Otherwise: inject the LLM-native discipline checklist into context
    via hookSpecificOutput.additionalContext

The injection is ADDITIVE to the system prompt context. It does not
replace user input. Claude still receives the original user message.

Retirement triggers (codified 2026-06-01):
  - If 30 days of usage show no behavioral shift toward LLM-native
    structure -> retire as decorative
  - If false-positive rate on exemptions is high (legitimate short
    queries getting primed unnecessarily and producing weird outputs)
    -> tighten exemption list
  - Monthly audit 2026-06-24 reviews activation log + paired Stop hook
    structural-output enforcement results

Scope: only enforces inside the research OS repo. Exit 0 outside.

Bias addressed: catches the multi-discipline simultaneous failure
mode (B40 candidate) at the PRE-GENERATION layer rather than
post-hoc.

Architecture: paired with structural-output-hook.py (Stop) which
enforces that analytical responses contain the structural sections
this injection asks for. The two-bracket structure (priming + pruning)
is strictly stronger than Stop-only enforcement.
"""

import json
import os
import re
import sys

ENFORCEMENT_PATHS = [_REPO_ROOT]


def in_scope() -> bool:
    cwd = os.getcwd()
    return any(cwd.startswith(p) for p in ENFORCEMENT_PATHS)


# Skip injection for these prompt patterns (would produce weird output)
SKIP_PATTERNS = [
    r"^/\w+",                          # slash commands
    r"^\s*(?:yes|no|ok|okay|thanks|thx)\s*[!.?]?\s*$",  # one-word acknowledgments
    r"^\s*(?:confirmed|approved|ship it|go ahead)\s*[!.?]?\s*$",
]

# Skip injection for meta-discussion of harness internals
META_DISCUSSION_PATTERNS = [
    r"\bhook\b",
    r"settings\.json",
    r"\.py\b",
    r"\bPrinciple\s*#\d+",
    r"\bB\d{2}\b",
    r"Critical Rule #\d+",
    r"codify",
    r"codification",
]


INJECTION = """
=== LLM-NATIVE DISCIPLINE PRIMING (UserPromptSubmit hook injection) ===

You are about to generate a response. BEFORE producing analytical
output, structurally enforce these patterns. Default reasoning is
HUMAN-ANALYST LINEAR. This injection biases the sampling toward
LLM-NATIVE MULTI-DIMENSIONAL.

1. PARALLEL HYPOTHESES — for any non-trivial analytical question,
   generate >=3 candidate hypotheses simultaneously with probability
   weighting. Label H1, H2, H3 with P=X% each. Do NOT collapse to
   a single linear narrative.

2. JOINT STATE — for portfolio or multi-name decisions, hold ALL
   relevant names in a single joint matrix or cross-correlation table.
   NOT sequential per-name evaluation.

3. LATERAL NOT FORWARD — don't only ask "what happens if X" (forward
   chain). Also ask: "what world-state would make X impossible?",
   "what's the convex hull of plausible states?", "what would falsify
   this?". Lateral reasoning > forward-chain.

4. MULTILINGUAL PARALLEL — for non-Western names (Japanese/Korean/
   Chinese/Taiwanese tickers), fire native-language search IN PARALLEL
   to English, not as fallback. Cite native-language URLs.

5. STRUCTURAL OUTPUT FOR ANALYTICAL RESPONSES — analytical outputs
   must contain:
   - Parallel hypothesis enumeration (H1/H2/H3 with P weights), OR
   - Joint-state matrix/table, OR
   - N-th order cascade with P>80% / P~60% / P~40% / P~20% markers
   The companion structural-output-hook.py (Stop) enforces this
   post-generation. Self-enforce pre-generation to avoid the catch.

6. SUBAGENT PARALLELISM — when investigation requires multiple
   independent research threads, fire subagents IN PARALLEL (single
   message, multiple Agent tool calls), not sequentially.

7. EXPLICIT HEDGE LABELS — every probability claim needs (my model)
   OR T1/T2/T3 source tier OR Bayesian-update derivation. Never bare
   probability.

8. REGIME-CORRECTED PRIORS (B45, codified 2026-06-12) — your
   pre-training data is mis-calibrated for the current structural-
   demand AI-supercycle regime. Empirical 15-name AI-infrastructure
   basket Jan 2025 -> Jun 2026: 6 of 15 names returned >+200%; 6 of
   15 returned +100-200%; tail under-modeled by ~5-8x. Single-day
   moves of +5-12% across cohort are routine (multiple times per
   week). BEFORE flagging any return or single-day move as
   "extreme", "elevated", "exhaustion-signaling", "above
   expectation", "stretched", or "priced-to-perfection", consult
   the regime base rate per `research/meta/biases-watchlist.md`
   B45 and `research/signals/cross-source-log/2026-06-12-pre-
   training-magnitude-conservatism-calibration.md`. Regime base
   rates binding until 2026-09-12 quarterly recalibration. This
   item exists because pre-training will pull you toward
   conservative magnitude reads even when the explicit calibration
   data contradicts that read.

9. MACRO-FIRST + RESEARCH-VS-RECALL TAGGING (Critical Rule #15,
   codified 2026-06-12) — Before any company-specific analytical
   output, ask: have I verified the current first-principles state
   of this layer with a date-anchored data point, or am I
   extrapolating from pre-training? Tag every load-bearing claim
   as (research-verified [date] [T1/T2/T3]) or (recall-based —
   verify before sizing decision). Tie nitty-gritty details to the
   macro thesis explicitly. If micro details contradict a credible
   institutional signal (CEO public endorsement, multi-billion
   strategic investment, multi-year contract), the FRAMING is
   incomplete — not the signal. Surface the contradiction before
   stating conclusions (B46 candidate). Q&A/restatement/harness-
   meta turns are exempt from this discipline; analytical outputs
   with sizing or thesis implications are not.

10. COMPUTE INSTEAD OF NARRATE (Principle #43b first registered
   candidate, codified 2026-07-07) — for ANY quantitative task
   (portfolio/envelope math, P/L decomposition, correlation or
   sign tests, prediction-band computation, count-based metrics,
   calibration aggregation): EXECUTE the computation with the
   Bash/python tool, then explain the result. Do NOT do arithmetic
   in prose — prose smooths errors; computation surfaces mismatches,
   and the mismatch itself is information. Origin (2026-07-07,
   first computed run): 2 tasks produced 3 catches prose had
   missed — an impossible cross-position FX inconsistency, a git
   history-graft trap, and a miscounted hook-fire series that had
   been narrated to the user as fact. Anthropomorphic-default bias:
   pre-training makes you "do the math in your head and write an
   essay" because human analysts write essays. You have the
   calculator. Press the buttons FIRST.

11. HARNESS-HISTORY COUNTS ARE COMPUTED, NEVER RECALLED (added
   2026-07-20, #43b clause 3f / B65 context-fluency) — any quantified
   claim about the harness's own history or state ("the hook fired N
   times", "I committed X times today", "this fired twice") is a
   COUNT over session/repo data: produce it with a tool call (grep
   hook-fire-log.md, git rev-list, log read) BEFORE stating it.
   Familiarity from THIS priming block is not verification — origin
   episodes quoted above (e.g. item 10's 2026-07-07 run) are
   HISTORICAL, days-to-weeks old; never restate one as a
   current-session event. Origin: 2026-07-20 "three times today"
   miscount — two real fires blended with a 13-day-old priming
   episode into a confident false count, caught only by operator
   question.

This is NOT a checklist to read and ignore. It is a sampling-
distribution bias applied BEFORE you generate the first token.
Generation that survives this priming + the Stop-hook pruning layer
is the only output the user sees.

=== END LLM-NATIVE PRIMING ===
"""


def _date_header() -> str:
    """Computed at inject time (B65 context-fluency / mechanism-3 fix,
    2026-07-20): absolute dates inside static priming prose are not salient
    enough to prevent temporal blending — the 07-20 miscount happened with
    the origin date visible in-context. A per-fire computed TODAY anchor is
    the deterministic counter."""
    try:
        from datetime import datetime, timezone
        today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        return (
            f"[TODAY IS {today} — computed at inject time. Everything in the "
            "priming block below is HISTORICAL context unless explicitly dated "
            "today; dated origin episodes are days-to-weeks old, not "
            "current-session events.]\n"
        )
    except Exception:
        return ""


def should_inject(prompt: str) -> bool:
    """Decide whether to inject priming for this prompt."""
    if not prompt or len(prompt.strip()) < 50:
        return False
    for pattern in SKIP_PATTERNS:
        if re.search(pattern, prompt, re.IGNORECASE):
            return False
    # Allow meta-discussion to be primed normally (the hook is itself
    # meta-discussion, and the injection talks about hooks too — so
    # exempting meta-discussion would defeat the purpose during
    # codification sessions). Only filter out single-word acks and
    # slash commands.
    return True


def main():
    if not in_scope():
        sys.exit(0)

    try:
        data = json.load(sys.stdin)
    except Exception:
        sys.exit(0)

    prompt = data.get("prompt", "") or ""

    if not should_inject(prompt):
        sys.exit(0)

    # Inject the priming via hookSpecificOutput.additionalContext.
    # This adds the priming text to Claude's context for the upcoming
    # turn, BEFORE generation begins. Exit 0 allows the prompt to
    # proceed; the additionalContext field shapes the generation.
    output = {
        "hookSpecificOutput": {
            "hookEventName": "UserPromptSubmit",
            "additionalContext": _date_header() + INJECTION,
        }
    }
    print(json.dumps(output))
    sys.exit(0)


if __name__ == "__main__":
    main()
