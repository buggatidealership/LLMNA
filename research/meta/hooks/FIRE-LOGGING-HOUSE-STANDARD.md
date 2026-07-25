# Fire-logging — HOUSE STANDARD (codified 2026-07-24 monthly audit)

**Origin:** fresh-Claude "what's missing" #1 (2026-07-20). Most live Stop hooks
emitted a block message that **died with the ephemeral container** — only
session-prime / macro-anchor / structural-output / session-prime-cascade /
anti-fabrication persisted a fire line. The next "N times today" claim would be
about a hook with no surviving record (the exact B65 context-fluency failure).

## The one house line format (do not drift)

```
- {UTC-ts} {hook-name} {STATUS} ({detail}){probe}
```

- `UTC-ts` = `datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%SZ")`
- `STATUS` = `FIRE` / `INCONCLUSIVE` / `event=…` / free token
- `(detail)` = parenthesized, **optional**, newlines collapsed, ≤300 chars
- `probe` = trailing ` probe=1` iff env `LLMNA_PROBE=1` (probe-pollution channel,
  G-28 2026-07-23) so test-harness fires stay out of metric numerators

`structural-output-metric.py` parses this line; the format is proven multi-tenant.

## The shared helper — `research/meta/hooks/hook_fire_log.py`

```python
from hook_fire_log import log_fire
log_fire("my-hook", "FIRE", detail="B21 first-order-anchoring")
```

Invariants:
1. **Never raises.** Any failure (perms, disk-full, import) is swallowed. A
   telemetry write must NEVER change a hook's exit code / enforcement verdict.
2. **repr/sanitize:** detail newlines→spaces (no forged log lines), length-capped.
3. **probe-aware:** honors `LLMNA_PROBE`.
4. `--selftest` (7 checks) / `--clock-check` / `--rotate` CLI.

## Wiring standard (fail-open shim)

```python
try:  # shared fire-log helper (house standard, fail-open)
    import sys as _sys_hfl, os as _os_hfl
    _sys_hfl.path.insert(0, _os_hfl.path.dirname(_os_hfl.path.abspath(__file__)))
    from hook_fire_log import log_fire as _log_fire
except Exception:
    def _log_fire(*_a, **_k):
        return ""
```
…then `_log_fire("<hook-name>", "FIRE", detail="…")` immediately before the
block `sys.exit(2)`.

## Migration state (2026-07-24)

- **Wired this audit (11 previously-silent Stop hooks):** cascade-enforcement,
  segment-trajectory, nth-order-cascade, bypass-route, bottoms-up,
  antifragility-mn, analyst-pt-context, reasoning-tagging,
  borrowed-vs-firstprinciples, llm-native-reasoning, signal-ingest-cascade.
  Verified: 5 with block-path test cases fired + logged in house format;
  full test suite unchanged (198/200 same two known-RED; 3 others ALL PASS) =
  **zero enforcement drift**.
- **Deliberately NOT re-pointed (already logging, house-format-compatible):**
  anti-fabrication, macro-anchor, structural-output, session-prime,
  session-prime-cascade, git-guard. Re-writing an author-blind enforcement path
  for cosmetic consolidation is **net-negative risk** (format-drift could break
  the 2026-08-06 structural-output metric). Their loggers stay; new hooks use the
  helper. Revisit only if one needs a change for another reason.

## Rotation / cap policy (metric-safe)

- **Append-only through the 2026-08-06 structural-output decision** (metric-
  critical window). The session-prime `MAX_INJECT` lesson is about bounding
  READS, never silently deleting decision data.
- `rotate_fire_log(retention_days=45)` archives ONLY entries older than the
  horizon to `hook-fire-log.<cutoff>.archive.md`; entries inside the window are
  never moved. Trip point: 512 KB. **Maintenance-only** — call from the monthly
  audit, never on write.
- `structural-output-metric.py` is **archive-aware** (reads live log + archives),
  so rotation can never shrink the decision window. With no archive present the
  read is byte-identical.

## Clock-source cross-check

`python3 hook_fire_log.py --clock-check` → container UTC vs latest git commit
timestamp + delta. Every fire ts + the session-start TODAY header inherit the
container clock **unverified**; a >1-day delta means log dates (and metric
buckets) are suspect. Run at the monthly audit. First reading 2026-07-24:
container 06:37Z vs last commit 00:35Z, delta ~6h = OK.

## Falsifier (re-eval 2026-08-24 monthly audit)

If the newly-wired hooks produce **zero** logged fires in 30 days, either the
enforcement patterns are inert (a separate retirement question) or the wiring is
dead — rerun the block-path smoke test. If the shared format ever diverges from
what `structural-output-metric.py` parses, the metric silently under-counts →
the format check in `hook_fire_log.py --selftest` is the tripwire.
