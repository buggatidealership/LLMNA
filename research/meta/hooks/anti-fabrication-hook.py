#!/usr/bin/env python3
import os as _os
from pathlib import Path as _Path
_REPO_ROOT = _os.environ.get("CLAUDE_PROJECT_DIR") or str(_Path(__file__).resolve().parents[3])
"""
Anti-fabrication Stop hook for the AI Sector Research OS.

Scans the most recent assistant message for numerical claims and verifies
each one is grounded — either:
  (a) cited inline (URL, file path, "per [source]", etc.), OR
  (b) explicitly hedged ("(estimate)", "(my inference)", etc.), OR
  (c) NEW (added 2026-05-21 per user calibration): grounded by exact-string
      match in any file under research/. Rationale: if I've already written
      a properly-cited file containing this number, the chat summary
      re-stating it doesn't need to re-cite — the file IS the source of
      truth. The hook still catches FABRICATION (number nowhere in repo).

Exits 2 with stderr if uncited+ungrounded numerical claims are found, which
surfaces the violations back to Claude as feedback for the next turn.

Scope: only enforces when the cwd is this research-OS repo (dynamic root; the
research OS). For all other repos / contexts, exits 0 (no enforcement).

Citation patterns accepted as valid:
  - URL anywhere in message
  - File reference (research/..., companies/..., etc.)
  - "per X" or "(X)" naming a source (SEC, Bloomberg, NVDA filing, etc.)
  - "[source: X]" or "[X]" bracket cite
  - Explicit hedges: "(estimate)", "(approximate)", "(unsourced)",
    "(my inference)", "(rough)", "~", "≈", "roughly", "approximately"

Repo grounding (added 2026-05-21):
  - For each number that fails inline-citation check, exact-string-search
    the entire research/ folder. If the number string appears in ANY file,
    it's considered grounded (file = source of truth).
  - This catches fabrication (number nowhere in repo) while allowing chat
    summaries of previously-committed properly-cited work.

Hook is intentionally lenient (favor false negatives over false positives)
since it's a guardrail not an oracle.
"""

import json
import os
import re
import subprocess
import sys
from pathlib import Path

# Only enforce inside the research OS repo. Avoid imposing on unrelated work.
ENFORCEMENT_PATHS = [_REPO_ROOT]
RESEARCH_DIR = os.path.join(ENFORCEMENT_PATHS[0], "research")


def in_scope() -> bool:
    cwd = os.getcwd()
    return any(cwd.startswith(p) for p in ENFORCEMENT_PATHS)


# Numerical claim patterns (case-insensitive)
NUMERICAL_PATTERNS = [
    # Currency: $78B, $725 billion, $1.2T, €10.3B
    (r"[\$€£¥]\s*\d+(?:[.,]\d+)*\s*(?:billion|million|trillion|[kKmMbBtT])\b", "currency"),
    # Percentages with claim context: 75.2%, 92%
    (r"\b\d+(?:\.\d+)?\s*%", "percentage"),
    # Energy units
    (r"\b\d+(?:\.\d+)?\s*(?:GW|MW|kW|TWh|MWh|kWh)\b", "energy"),
    # Wafer/chip counts: 130K wpm, 2M units, 60K wafers
    (r"\b\d+(?:\.\d+)?\s*[kKmMbB]?\s*(?:wpm|wafer|GPU|chip|unit)s?\b", "compute_capacity"),
    # Quarterly numbers near $: Q1 FY27 $78B (looser, catches table cells)
    (r"\b(?:Q[1-4]|FY\d{2,4})\b.{0,40}[\$€£]\s*\d", "quarterly_financial"),
]

# Patterns that count as a valid citation/hedge near a number
CITATION_PATTERNS = [
    r"https?://\S+",                       # URLs
    r"research/[\w/-]+\.md",               # file references inside the OS
    r"companies/[A-Z]+/\w+\.md",           # company file references
    r"sector/[\w/-]+\.md",
    r"predictions/[\w/-]+\.md",
    r"\(per [^)]+\)",                      # (per SEC filing)
    r"\(source:[^)]+\)",                    # (source: ...)
    r"\bper\s+(?:SEC|EDGAR|Bloomberg|NVDA|TSMC|TSM|company|management|CFO|filing|press release|10-K|10-Q|8-K|earnings call)",
    r"\[source[^\]]*\]",
    r"\bfrom\s+(?:SEC|EDGAR|Bloomberg|NVDA|TSMC|TSM|company|CFO|10-K|10-Q|8-K|filing|press release|earnings call)",
    # Explicit hedges
    r"\(estimate\)",
    r"\(estimated\)",
    r"\(approximate\)",
    r"\(approximately\)",
    r"\(rough\)",
    r"\(roughly\)",
    r"\(unsourced\)",
    r"\(unsourced\s+inference\)",
    r"\(my inference\)",
    r"\(inferred\)",
    r"\(my estimate\)",
    r"\(my read\)",
    r"\(my view\)",
    r"\(my model\)",
    r"\(point estimate\)",
    r"\(speculation\)",
    r"\(speculative\)",
    r"\(hypothetical\)",
    r"\(hypothetical [^)]*\)",
    r"\(illustrative\)",
    r"\(illustrative [^)]*\)",
    r"\(scenario\)",
    r"\(modeled\)",
    r"\(if [^)]+\)",
    r"\(TBD\)",
    r"\(placeholder\)",
    r"\(industry estimate\)",
    r"\(consensus\)",
    r"\bapproximately\b",
    r"\broughly\b",
    r"~\s*\d",                             # ~$78B
    r"≈\s*\d",
    # Q4 FY26 actual / actuals = treated as cited (anchor data the user can verify)
    r"\b(?:Q[1-4]|FY)\d{0,4}\s*(?:actual|actuals|reported|filed|reported|guide|guided|guidance)\b",
]

# Proximity window in characters
WINDOW = 350


def get_last_assistant_message(transcript_path: str) -> str:
    """Read JSONL transcript, return text of last assistant message."""
    try:
        with open(transcript_path) as f:
            lines = f.readlines()
    except FileNotFoundError:
        return ""
    # Walk backwards for the latest assistant message
    for line in reversed(lines):
        try:
            entry = json.loads(line)
        except json.JSONDecodeError:
            continue
        # Format varies; try common shapes
        msg = entry.get("message") or entry
        role = msg.get("role") or entry.get("role")
        if role != "assistant":
            continue
        content = msg.get("content")
        if isinstance(content, str):
            return content
        if isinstance(content, list):
            parts = []
            for c in content:
                if isinstance(c, dict) and c.get("type") == "text":
                    parts.append(c.get("text", ""))
            if parts:
                return "\n".join(parts)
    return ""


def find_violations(text: str) -> list[tuple[str, str, str]]:
    """Return list of (matched_number, category, surrounding_window)."""
    violations = []
    for pattern, category in NUMERICAL_PATTERNS:
        for m in re.finditer(pattern, text, re.IGNORECASE):
            start = max(0, m.start() - WINDOW)
            end = min(len(text), m.end() + WINDOW)
            window = text[start:end]
            cited = any(
                re.search(cp, window, re.IGNORECASE) for cp in CITATION_PATTERNS
            )
            if not cited:
                violations.append((m.group(0), category, window[:200] + "..."))
    return violations


# --- Three-valued grounding (2026-07-20 rebuild, K3 + fresh-Claude red-team) ---
# A fire requires affirmative proof of ABSENCE (grep rc=1), never absence of
# proof. Infra errors (rc>=2, exception, timeout) are INCONCLUSIVE: logged,
# never fired on — the old `except: return False` path was fail-closed on
# infra error, contradicting the harness's fail-open constraint.
GROUNDED = "GROUNDED"
FABRICATED = "FABRICATED"
INCONCLUSIVE = "INCONCLUSIVE"
SKIP = "SKIP"  # degenerate needle — never a fabrication, never logged (K3 r2 #7)

FIRE_LOG = os.path.join(_REPO_ROOT, "research", "meta", "hook-fire-log.md")

# Shared grounding budget per message (K3 r2 #6): without it, worst case is
# forms x retry x 10s x K needles serial inside a Stop hook — a 5-number
# message could hang >3 minutes under exactly the infra stress where
# timeouts actually happen. Past the deadline everything unresolved is
# INCONCLUSIVE.
BUDGET_SECONDS = 15.0


def _collapse_ws(s: str) -> str:
    """Collapse ALL internal whitespace (incl. NBSP/U+202F/U+2009 — \\s matches
    them) so a captured needle like '30.2 %' grounds against the file form
    '30.2%'. Mechanism (A) of the 2026-07-20 FP arc: find_violations returns
    m.group(0) INCLUDING whitespace matched by \\s*, and grep -F on the
    with-space form fails against the no-space form on file. Collapsing only
    equates whitespace-variants of the same numeric token — it grants exactly
    the grounding the no-space form would get, no new coincidence risk."""
    return re.sub(r"\s+", "", s)


def _grep_repo(needle: str, timeout: float = 10):
    """One grep -F pass. Returns (returncode_or_None, exception_name_or_None).

    K3 r2 hardening: `-e` before the needle (a leading-dash needle like
    '-12.62%' otherwise parses as grep options → rc=2 → INCONCLUSIVE forever
    for signed forms — empirically confirmed 2026-07-20, latent today).
    `--exclude=hook-fire-log.md` + `--exclude-dir=audits`: the fire log and
    committed audit packs must NOT be grounding evidence — otherwise the hook
    MINTS ITS OWN EXEMPTIONS (fire once on a fabricated number → its
    repr-logged needle grounds every later use; empirically confirmed
    2026-07-20 by planting a logged line and re-grepping → rc=0)."""
    try:
        result = subprocess.run(
            ["grep", "-r", "-F", "-l", "--include=*.md",
             "--exclude=hook-fire-log.md", "--exclude-dir=audits",
             "-e", needle, RESEARCH_DIR],
            capture_output=True,
            text=True,
            timeout=timeout,
        )
        return result.returncode, None
    except Exception as e:  # TimeoutExpired, FileNotFoundError, anything
        return None, type(e).__name__


def _is_infra_error(rc) -> bool:
    """Infra error iff rc not in (0, 1). K3 r2 #1: a signal-killed grep
    (OOM SIGKILL) returns NEGATIVE rc — the old `rc is None or rc >= 2`
    test let -9 fall through to FABRICATED, i.e. a false FIRE under exactly
    the infra stress the three-valued design exists to absorb (empirically
    confirmed via monkeypatch 2026-07-20)."""
    return rc not in (0, 1)


def ground_needle(number_str: str, deadline: float = None):
    """Classify a needle as GROUNDED / FABRICATED / INCONCLUSIVE / SKIP.

    Semantics: grep rc=0 → GROUNDED; rc=1 (clean no-match) → FABRICATED, no
    retry; any other rc (None/exception, >=2, negative signal-kill) → retry
    ONCE → still bad → INCONCLUSIVE. Tries the raw needle, then the
    whitespace-collapsed form. `deadline` (time.monotonic-based) is the
    shared per-message budget — past it, unresolved forms are INCONCLUSIVE
    ("BudgetExceeded"), never FABRICATED.

    Returns (status, diag); diag = {"needle": repr, "forms": [(form-repr,
    rc, exc), ...], "matched_form": repr-or-absent} — PER-FORM outcomes
    (K3 r2 #3: recording only the last form's rc made mixed outcomes
    unreadable: raw=infra-error + collapsed=rc-1 logged as `rc=1 exc=None`,
    hiding the reason it didn't fire). All reprs because invisible-unicode
    needles reproduce their own illegibility if logged raw. On GROUNDED,
    matched_form says WHICH form hit — collapsed-match means the file's
    spacing differs from the claim's, which matters at FP adjudication."""
    import time
    needle = number_str.strip()
    diag = {"needle": repr(needle), "forms": []}
    if not needle:
        return SKIP, diag
    if not os.path.isdir(RESEARCH_DIR):
        diag["forms"].append(("<none>", None, "NoResearchDir"))
        return INCONCLUSIVE, diag

    forms = [needle]
    collapsed = _collapse_ws(needle)
    if collapsed and collapsed != needle:
        forms.append(collapsed)

    worst = FABRICATED
    for form in forms:
        timeout = 10.0
        if deadline is not None:
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                diag["forms"].append((repr(form), None, "BudgetExceeded"))
                return INCONCLUSIVE, diag
            timeout = min(10.0, max(0.5, remaining))
        rc, exc = _grep_repo(form, timeout)
        if _is_infra_error(rc):
            rc, exc = _grep_repo(form, timeout)  # retry once on infra error only
        diag["forms"].append((repr(form), rc, exc))
        if rc == 0:
            diag["matched_form"] = repr(form)
            return GROUNDED, diag
        if _is_infra_error(rc):
            worst = INCONCLUSIVE  # infra error → cannot prove absence
    return worst, diag


def classify_violations(violations: list[tuple[str, str, str]]):
    """Split violations into (fabricated, inconclusive) with diags, under one
    shared time budget. GROUNDED dropped (file = source of truth); SKIP
    dropped silently (degenerate needle, never logged)."""
    import time
    deadline = time.monotonic() + BUDGET_SECONDS
    fabricated, inconclusive = [], []
    for v in violations:
        status, diag = ground_needle(v[0], deadline)
        if status == FABRICATED:
            fabricated.append((v, diag))
        elif status == INCONCLUSIVE:
            inconclusive.append((v, diag))
    return fabricated, inconclusive


def _format_fire_line(status: str, entries, ts: str) -> str:
    """One house-format log line. FIRE lines carry ALL fabricated needles
    (K3 r2 #4: truncating could drop the very needle that caused the block,
    leaving the line unable to explain itself); INCONCLUSIVE detail caps at 5
    (content-free spam guard)."""
    cap = len(entries) if status == "FIRE" else 5
    detail = "; ".join(
        f"{d['needle']} forms={d['forms']}" for _, d in entries[:cap]
    )
    return f"- {ts} anti-fabrication-hook {status} (n={len(entries)} {detail} verdict:pending)"


def log_fire(status: str, entries) -> str:
    """Append a house-format line to hook-fire-log.md. Never raises.
    Returns the formatted line EITHER WAY so the caller can embed it in the
    block feedback — the transcript then backs up the log (K3 r2 #8: a
    disk-full/perms failure otherwise silently recreates the un-logged
    'three times today' condition). Verdict:pending flips to TRUE-FIRE /
    FALSE-POSITIVE at adjudication; the flip line must cite its computed
    source (grep/log read), and the monthly audit samples flips against
    transcripts."""
    line = ""
    try:
        from datetime import datetime, timezone
        ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%SZ")
        line = _format_fire_line(status, entries, ts)
        with open(FIRE_LOG, "a") as f:
            f.write(line + "\n")
    except Exception:
        pass
    return line


def main():
    try:
        input_data = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        # If we can't parse input, don't block — just pass through
        sys.exit(0)

    # Recursion prevention
    if input_data.get("stop_hook_active") is True:
        sys.exit(0)

    # Only run inside the research OS
    if not in_scope():
        sys.exit(0)

    transcript_path = input_data.get("transcript_path", "")
    if not transcript_path or not Path(transcript_path).exists():
        sys.exit(0)

    text = get_last_assistant_message(transcript_path)
    if not text:
        sys.exit(0)

    # Skip if the message is tiny (probably a status update / acknowledgment)
    if len(text) < 200:
        sys.exit(0)

    violations = find_violations(text)
    if not violations:
        sys.exit(0)

    # Three-valued grounding (2026-07-20): fire ONLY on FABRICATED (proven
    # absent, grep rc=1). INCONCLUSIVE (infra error after retry) is logged
    # and passed — never fired on. Per user calibration 2026-05-21: chat
    # summaries of properly-cited file content do not need re-citation.
    fabricated, inconclusive = classify_violations(violations)
    if inconclusive:
        log_fire("INCONCLUSIVE", inconclusive)
    if not fabricated:
        sys.exit(0)

    fire_line = log_fire("FIRE", fabricated)
    violations = [v for v, _diag in fabricated]

    # Build feedback message — show first 5 violations
    msg_lines = [
        "ANTI-FABRICATION HOOK: numerical claims found without nearby citation, file reference, OR repo grounding.",
        "",
        f"Found {len(violations)} potentially fabricated numerical claim(s) — number is NOT present in any research/ file. Showing first 5:",
        "",
    ]
    for i, (matched, category, context) in enumerate(violations[:5], 1):
        msg_lines.append(f"{i}. [{category}] '{matched}'")
        msg_lines.append(f"   Context: ...{context.strip()}")
        msg_lines.append("")

    msg_lines += [
        "Required action: in your next message, for each numerical claim either",
        "  (a) cite the source inline (URL, file path, 'per [source]', etc.), OR",
        "  (b) flag it explicitly as '(estimate)', '(my inference)', '(unsourced)', etc., OR",
        "  (c) commit the number to a properly-cited research/ file FIRST, then restate.",
        "",
        "Repo-grounding is checked via exact-string match in research/*.md files.",
        "If the number truly exists in a file but the hook missed it, the string",
        "form may differ ($163B vs '163 billion') — restate using the exact form",
        "from the file.",
        "",
        f"Fire-log line (transcript backup; also appended to meta/hook-fire-log.md): {fire_line}",
    ]
    print("\n".join(msg_lines), file=sys.stderr)
    sys.exit(2)


def selftest() -> int:
    """Regression suite: 2026-07-20 three-valued rebuild + K3-round-2 patch.
    Run: python3 anti-fabrication-hook.py --selftest. Log lines go to a temp
    file (monkeypatches FIRE_LOG), never the real hook-fire-log. Fixture rule
    (K3 r2): each future FP adjudication ADDS a fixture for the newly
    observed needle shape — the needle distribution drifts; the suite must
    follow it or it proves the code, not the corpus."""
    global FIRE_LOG, RESEARCH_DIR
    import tempfile
    failures = []
    _real_log, _real_dir = FIRE_LOG, RESEARCH_DIR

    def check(name, cond):
        if not cond:
            failures.append(name)

    with tempfile.TemporaryDirectory() as td:
        FIRE_LOG = os.path.join(td, "test-fire-log.md")

        # 1-4 Mechanism (A): with-space / unicode-space (NBSP, U+202F)
        # needles ground when the no-space form exists in the repo.
        for form in ["30.2 %", "30.2\u00a0%", "30.2\u202f%", "30.2%"]:
            status, diag = ground_needle(form)
            check(f"ground[{form!r}]=GROUNDED (got {status})", status == GROUNDED)

        # 5-6 Genuinely absent number: FABRICATED (rc=1), per-form diag.
        status, diag = ground_needle("83.4719%")
        check(f"absent gives FABRICATED (got {status})", status == FABRICATED)
        check("per-form diag recorded rc=1", bool(diag["forms"]) and diag["forms"][0][1] == 1)

        # 7 Signed needle (leading dash): -e guard means clean rc, not option-error.
        status, diag = ground_needle("-83.4719%")
        check(f"signed absent gives FABRICATED not INCONCLUSIVE (got {status})", status == FABRICATED)

        # 8 Negative rc (signal-killed grep) gives INCONCLUSIVE, never false FIRE.
        _orig_grep = globals()["_grep_repo"]
        globals()["_grep_repo"] = lambda n, timeout=10: (-9, None)
        status, _ = ground_needle("55.55%")
        globals()["_grep_repo"] = _orig_grep
        check(f"rc=-9 gives INCONCLUSIVE (got {status})", status == INCONCLUSIVE)

        # 9 Missing research dir gives INCONCLUSIVE.
        RESEARCH_DIR = "/nonexistent-selftest-dir"
        status, _ = ground_needle("12.34%")
        RESEARCH_DIR = _real_dir
        check(f"bad-dir gives INCONCLUSIVE (got {status})", status == INCONCLUSIVE)

        # 10 Empty needle gives SKIP (never a fabrication, never logged).
        status, _ = ground_needle("   ")
        check(f"empty gives SKIP (got {status})", status == SKIP)

        # 11-12 Expired budget gives INCONCLUSIVE BudgetExceeded.
        import time
        status, diag = ground_needle("77.77%", deadline=time.monotonic() - 1)
        check(f"expired-budget gives INCONCLUSIVE (got {status})", status == INCONCLUSIVE)
        check("BudgetExceeded recorded", any("BudgetExceeded" in str(x) for x in diag["forms"]))

        # 13-15 Self-minting guard (hermetic temp corpus): needles present
        # ONLY in hook-fire-log.md / audits/ must NOT ground; regular files do.
        corpus = os.path.join(td, "research")
        os.makedirs(os.path.join(corpus, "audits"))
        with open(os.path.join(corpus, "hook-fire-log.md"), "w") as fh:
            fh.write("- ts anti-fabrication-hook FIRE (n=1 '91.837%' rc=1 verdict:pending)\n")
        with open(os.path.join(corpus, "audits", "pack.md"), "w") as fh:
            fh.write("expected output: 64.297%\n")
        with open(os.path.join(corpus, "real.md"), "w") as fh:
            fh.write("a real grounded figure: 12.345%\n")
        RESEARCH_DIR = corpus
        s1, _ = ground_needle("91.837%")
        s2, _ = ground_needle("64.297%")
        s3, _ = ground_needle("12.345%")
        RESEARCH_DIR = _real_dir
        check(f"log-only needle does NOT ground (got {s1})", s1 == FABRICATED)
        check(f"audits-only needle does NOT ground (got {s2})", s2 == FABRICATED)
        check(f"regular-file needle still grounds (got {s3})", s3 == GROUNDED)

        # 16-19 log_fire: line written + returned; FIRE carries ALL needles;
        # repr-escaped; verdict field.
        entries = []
        for i in range(7):
            n = repr(f"{i}0.0\u202f%")
            entries.append(((f"x{i}", "percentage", "ctx"), {"needle": n, "forms": [(n, 1, None)]}))
        line = log_fire("FIRE", entries)
        check("log line written+returned", "anti-fabrication-hook FIRE" in line and os.path.exists(FIRE_LOG))
        check("FIRE line carries ALL 7 needles", line.count("forms=") == 7)
        check("repr-escaped (U+202F never raw)", "\u202f" not in line and "202f" in line)
        check("verdict field present", "verdict:pending" in line)

        # 20 log_fire write-failure: silent, line still RETURNED (transcript backup).
        FIRE_LOG = "/nonexistent-dir/x.md"
        try:
            line = log_fire("FIRE", entries[:1])
            ok = "anti-fabrication-hook" in line
        except Exception:
            ok = False
        check("log_fire never raises + returns line on write-failure", ok)

    FIRE_LOG, RESEARCH_DIR = _real_log, _real_dir
    if failures:
        print("SELFTEST FAIL:\n  " + "\n  ".join(failures))
        return 1
    print("SELFTEST PASS (20 checks)")
    return 0


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--selftest":
        sys.exit(selftest())
    try:
        main()
    except SystemExit:
        raise
    except Exception:
        # Fail-open: an unexpected bug in this hook must never block work.
        sys.exit(0)
