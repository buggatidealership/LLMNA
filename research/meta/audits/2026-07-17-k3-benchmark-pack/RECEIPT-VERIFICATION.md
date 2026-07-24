# Receipt verification (resident session, 2026-07-18)
Chain of custody CLOSED end to end, verified independently in the resident container:
1. Archive SHA-256 matched K3's chat-printed value exactly: `dc82a95afba4af05011d40bfdd4f9b2e6d26beef485188a0c78d626ddcb29914` (the one datum that traveled outside the file).
2. MANIFEST: 24/24 file hashes pass, 0 fail.
3. `reproduce.py` safety-reviewed before execution (no network imports; subprocess = git read-only; writes confined to its out-dir).
4. Executed against a pinned worktree at `d816abf` → STEP 0 MATCH; headline outputs regenerated EXACTLY per MANIFEST EXPECTED-OUTPUTS (Brier 0.1978/0.2500/0.1844/0.1000; TEST2 12W/7L/1T +1.03pp; TEST3 −3.63%/−1.25%/−2.26%; 0 late registrations).
5. All four regenerated CSVs byte-identical to the frozen pack files (`diff -q` clean).
Status: FROZEN BASELINE for the quarterly benchmark re-audit (runbook: README §"How next quarter's audit should run"; commission: `meta/fresh-session-audit-protocol.md` §External benchmark-audit commission v1). Append-only ledger keeps old rows stable; next audit reports per-test DELTAS vs these numbers; null stays the default position.
