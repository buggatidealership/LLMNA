# PLATFORM-TRIGGER CENSUS (canonical mirror of platform-side scheduler state; born 2026-07-19 from the trigger mis-audit)

**Rule (binding, instruction-level — enforcement rides git):** any turn that MUTATES platform triggers (create/delete/update via Claude_Code_Remote tools) MUST update this file in the SAME turn. The census diff then falls under the existing deterministic git-check (uncommitted changes block turn completion) — a platform change thereby becomes a repo change, which IS enforced-logged. Reconciliation: monthly audit runs list_triggers and diffs against this file; ANY divergence = an unlogged mutation = mis-audit-class event (L34-N+1 counter increments). Honest limit (verified 2026-07-19): hooks cannot call MCP tools and no hook parses tool calls — same-turn capture is discipline, the reconciliation diff is the deterministic backstop. Candidate upgrade (uncertain, untested): Stop-hook transcript parse for MCP tool_use entries — test before claiming.

## ACTIVE (verified via list_triggers 2026-07-19)
| ID | Name | Schedule | Binding | Created |
|---|---|---|---|---|
| trig_01WM2zxPAcrKzr8YCnpHkYHP | KR-open wake (LLMNA, self-bind) | 22 0 * * 1-5 (weekdays 00:22Z) | self-bind → this session | 2026-07-19 15:50Z |
| trig_01Jpj7pjfkxAB5z9JCqVLhr4 | EOD conditional synthesis (LLMNA, self-bind) | 17 20 * * * (daily 20:17Z) | self-bind → this session | 2026-07-19 15:59Z |

## INERT (fired one-shots, self-disabled — audit trail, kept)
11 send_later self-check-ins, 2026-07-06 → 2026-07-16 (E4-E7 test adjudications, NBIS/SKH/TSMC grade follow-ups). IDs in the 2026-07-19 list_triggers snapshots (session record + day-state SUN-EVE-#5/#6).

## DELETED (2026-07-19, this session, ×3 — verified via user client-record screenshot after context-elision mis-audit)
trig_01CnVFkk... (KR-JP morning wake, fresh-spawn, broken env-binding) · trig_01Du5F6B... (EOD synthesis, fresh-spawn) · trig_01BJ... (E7 env-binding test). Prompts preserved in meta/platform-trigger-setup.md.

## OUTSIDE AGENT VISIBILITY (user-side only)
2 "loopframe" posting routines (April ARS project, created via http_api) — do NOT appear in agent list_triggers; still firing daily w/ plaintext keys in prompts; pause + key rotation = user browser task (checklist).
