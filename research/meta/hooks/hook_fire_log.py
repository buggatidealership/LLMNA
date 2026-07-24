#!/usr/bin/env python3
"""Shared fire-logging helper — the HOUSE STANDARD for hook telemetry.

Codified 2026-07-24 (monthly audit). Origin: fresh-Claude "what's missing" #1
(2026-07-20) — most live Stop hooks emit a block message that dies with the
ephemeral container; only session-prime / macro-anchor / structural-output /
session-prime-cascade / anti-fabrication persist a fire line. The next
"N times today" claim would be about a hook with no surviving record. This
module gives every hook one fail-open, house-format append.

HOUSE LINE FORMAT (do not drift — structural-output-metric.py + audits parse it):

    - {UTC-ts} {hook-name} {STATUS} ({detail}){probe}

  * UTC-ts   : datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%SZ")
  * STATUS   : FIRE / INCONCLUSIVE / event=... / free token
  * (detail) : parenthesized, OPTIONAL, newlines collapsed, length-capped
  * probe    : trailing " probe=1" iff env LLMNA_PROBE=1 (probe-pollution channel,
               G-28 2026-07-23) so test-harness fires stay out of metric numerators

The 7 hooks that already log (anti-fabrication / macro-anchor / structural-output
/ session-prime / session-prime-cascade / git-guard + this) are ALREADY
house-format-compatible — the metric proves it multi-tenant. They are deliberately
NOT re-pointed here: re-writing an author-blind enforcement path for cosmetic
consolidation is net-negative risk (format-drift could break the 08-06 metric).
This helper is wired into the previously-SILENT Stop hooks (the real gap).

DESIGN INVARIANTS:
  1. Never raises. Any failure (perms, disk-full, import) is swallowed — a
     telemetry write must NEVER change a hook's exit code / enforcement verdict.
  2. Append-only through the 2026-08-06 structural-output decision (metric-
     critical window). rotate_fire_log() archives ONLY entries older than a
     retention horizon, and the metric is archive-aware, so rotation can never
     shrink the live decision window. (session-prime MAX_INJECT lesson: bound
     READS, never silently delete decision data.)
"""
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

_MODULE_DIR = Path(__file__).resolve().parent          # research/meta/hooks
_REPO_ROOT = _MODULE_DIR.parents[2]                     # repo root
FIRE_LOG = _REPO_ROOT / "research" / "meta" / "hook-fire-log.md"
ARCHIVE_GLOB = "hook-fire-log.*.archive.md"

_DETAIL_CAP = 300           # content-free-spam / log-injection guard
_ROTATE_CAP_BYTES = 512 * 1024   # policy trip point; rotation still date-gated
_RETENTION_DAYS = 45        # never archive entries newer than this (metric-safe)


def _sanitize(detail: str) -> str:
    """Collapse newlines/CR (a detail line must not forge extra log lines) and
    cap length. Never raises."""
    try:
        s = str(detail).replace("\r", " ").replace("\n", " ").strip()
        if len(s) > _DETAIL_CAP:
            s = s[: _DETAIL_CAP - 1] + "…"
        return s
    except Exception:
        return ""


def format_fire_line(hook_name: str, status: str = "FIRE", detail: str = "",
                     ts: str | None = None, probe_aware: bool = True) -> str:
    """Return the exact house line (no trailing newline). Pure; never raises."""
    try:
        if ts is None:
            ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%SZ")
        det = _sanitize(detail)
        detail_part = f" ({det})" if det else ""
        probe = " probe=1" if (probe_aware and os.environ.get("LLMNA_PROBE") == "1") else ""
        return f"- {ts} {hook_name} {status}{detail_part}{probe}"
    except Exception:
        # Absolute fallback — still a parseable-ish line
        return f"- {hook_name} {status}"


def log_fire(hook_name: str, status: str = "FIRE", detail: str = "", *,
             probe_aware: bool = True, log_path=None) -> str:
    """Append a house-format fire line. NEVER raises. Returns the formatted line
    either way so the caller can also embed it in block feedback (transcript
    backup for the disk-full/perms case)."""
    line = ""
    try:
        line = format_fire_line(hook_name, status, detail, probe_aware=probe_aware)
        path = Path(log_path) if log_path else FIRE_LOG
        with open(path, "a") as fh:
            fh.write(line + "\n")
    except Exception:
        pass
    return line


# ---------------------------------------------------------------------------
# Rotation (maintenance-only; metric-safe) + archive-aware reads
# ---------------------------------------------------------------------------
def iter_fire_lines(log_path=None):
    """Yield fire lines from the live log PLUS any dated archives, so any reader
    (metric, audit) sees the full history regardless of rotation state."""
    base = Path(log_path) if log_path else FIRE_LOG
    meta_dir = base.parent
    files = sorted(meta_dir.glob(ARCHIVE_GLOB)) + [base]
    for f in files:
        try:
            for ln in f.read_text().splitlines():
                yield ln
        except Exception:
            continue


def _line_date(line: str):
    try:
        # "- 2026-07-24 00:00:00Z hook ..."
        parts = line.split()
        if len(parts) >= 2 and parts[0] == "-":
            return datetime.strptime(parts[1], "%Y-%m-%d").date()
    except Exception:
        pass
    return None


def rotate_fire_log(retention_days: int = _RETENTION_DAYS, log_path=None,
                    today=None) -> str:
    """Archive lines OLDER than retention_days to hook-fire-log.<cutoff>.archive.md,
    keeping the live log to recent entries + non-dated header lines. Metric-safe:
    entries inside the retention window are never moved. Returns a status string.
    Call from the monthly audit only — NOT on every write."""
    base = Path(log_path) if log_path else FIRE_LOG
    try:
        if base.stat().st_size < _ROTATE_CAP_BYTES:
            return f"skip: {base.name} under {_ROTATE_CAP_BYTES} bytes"
    except Exception as e:
        return f"skip: cannot stat ({e})"
    if today is None:
        today = datetime.now(timezone.utc).date()
    cutoff = today.toordinal() - retention_days
    keep, archive = [], []
    for ln in base.read_text().splitlines():
        d = _line_date(ln)
        if d is None:                      # header / non-dated → always keep live
            keep.append(ln)
        elif d.toordinal() < cutoff:
            archive.append(ln)
        else:
            keep.append(ln)
    if not archive:
        return "skip: nothing older than retention horizon"
    arch_path = base.parent / f"hook-fire-log.{today.isoformat()}.archive.md"
    try:
        with open(arch_path, "a") as fh:
            fh.write("\n".join(archive) + "\n")
        base.write_text("\n".join(keep) + "\n")
    except Exception as e:
        return f"error: {e}"
    return f"archived {len(archive)} lines -> {arch_path.name}; kept {len(keep)}"


def clock_cross_check() -> dict:
    """Monthly audit helper: container UTC clock vs latest git commit timestamp.
    The TODAY header + every fire ts inherit the container clock UNVERIFIED; a
    large delta means dates in the log (and the metric buckets) are suspect."""
    import subprocess
    out = {"container_utc": None, "latest_commit_utc": None, "delta_seconds": None,
           "note": ""}
    try:
        out["container_utc"] = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%SZ")
        r = subprocess.run(
            ["git", "-C", str(_REPO_ROOT), "log", "-1", "--format=%cI"],
            capture_output=True, text=True, timeout=15,
        )
        if r.returncode == 0 and r.stdout.strip():
            commit_dt = datetime.fromisoformat(r.stdout.strip()).astimezone(timezone.utc)
            out["latest_commit_utc"] = commit_dt.strftime("%Y-%m-%d %H:%M:%SZ")
            now = datetime.now(timezone.utc)
            out["delta_seconds"] = round((now - commit_dt).total_seconds())
            out["note"] = ("OK: within 1 day" if abs(out["delta_seconds"]) < 86400
                           else "WARN: >1 day drift vs last commit — verify container clock")
    except Exception as e:
        out["note"] = f"error: {e}"
    return out


def _selftest() -> int:
    fails = []
    # format correctness
    ln = format_fire_line("test-hook", "FIRE", "some detail", ts="2026-07-24 00:00:00Z",
                          probe_aware=False)
    if ln != "- 2026-07-24 00:00:00Z test-hook FIRE (some detail)":
        fails.append(f"format basic: {ln!r}")
    # empty detail → no parens
    ln = format_fire_line("test-hook", "FIRE", "", ts="2026-07-24 00:00:00Z", probe_aware=False)
    if ln != "- 2026-07-24 00:00:00Z test-hook FIRE":
        fails.append(f"format empty-detail: {ln!r}")
    # probe tag
    os.environ["LLMNA_PROBE"] = "1"
    ln = format_fire_line("h", "FIRE", "d", ts="2026-07-24 00:00:00Z", probe_aware=True)
    if not ln.endswith(" probe=1"):
        fails.append(f"probe tag missing: {ln!r}")
    del os.environ["LLMNA_PROBE"]
    # newline injection neutralized
    ln = format_fire_line("h", "FIRE", "a\n- 2026-01-01 forged x", ts="2026-07-24 00:00:00Z",
                          probe_aware=False)
    if "\n" in ln:
        fails.append(f"newline not collapsed: {ln!r}")
    # metric-compat: structural-output-hook line still matches the metric regex
    import re
    ln = format_fire_line("structural-output-hook", "FIRE", "structural-markers-missing",
                          ts="2026-07-24 00:00:00Z", probe_aware=False)
    if not re.match(r"- (\d{4}-\d{2}-\d{2}) .*structural-output-hook FIRE(?:\s*\(([^)]*)\))?", ln):
        fails.append(f"metric-regex incompat: {ln!r}")
    # date parse for rotation
    if _line_date("- 2026-07-24 00:00:00Z h FIRE (x)") is None:
        fails.append("line_date parse")
    if _line_date("## header line") is not None:
        fails.append("line_date should be None for header")
    if fails:
        print("SELFTEST FAIL:")
        for f in fails:
            print("  -", f)
        return 1
    print("SELFTEST OK (7 checks)")
    return 0


if __name__ == "__main__":
    arg = sys.argv[1] if len(sys.argv) > 1 else "--selftest"
    if arg == "--selftest":
        sys.exit(_selftest())
    elif arg == "--clock-check":
        import json
        print(json.dumps(clock_cross_check(), indent=2))
    elif arg == "--rotate":
        print(rotate_fire_log())
    else:
        print(f"unknown arg {arg!r}; use --selftest | --clock-check | --rotate")
        sys.exit(2)
