# Initial Implementation Plan — Current status

**Updated:** 2026-11-17. This is a living, status-aware plan; the original empty-repository audit remains preserved in `REPOSITORY_INVENTORY.md` as historical evidence.

## Completed and current

1. **Checkpoint 0 — PASS.** Repository identity, baseline, licensing, architecture and risks were inspected. The repository was initialized on `main` at `36db1f967d41f5d1063fcfbd2772bc93b42f1109`; the current work continues on `feat/instrument-domain-foundation` from recovery point `dc334776a2b939b02a303848b1c084b778526552`.
2. **Gate 1 engineering foundation — partial.** Provider-neutral instruments, UTC timestamps, Decimal OHLCV, revision selection, tests and pinned read-only CI exist. A deterministic fail-closed data entitlement primitive is added in this increment. No data provider is connected and no data entitlement is approved.
3. **Gate 1 research — in progress.** Official documentation and public terms have been reviewed for representative providers and venues. Provider contract confirmation, source availability semantics for point-in-time replay, global coverage fit, and provider-specific XAUUSD/NAS100 instrument mappings remain unresolved. Gate 1 cannot pass yet.

## Next implementation sequence

1. Finish and review provider assessment, data-rights register, and instrument-specification report. Clearly distinguish source-confirmed facts from unknowns/vendor questions.
2. Close additive entitlement-boundary tests and all existing contract edge-case tests. Preserve all previously captured revisions; do not trust unsourced historical `available_at` values.
3. Complete the agent skill instructions as reusable contracts inside the modular monolith; skills do not imply separate services or agents.
4. Update feature and architecture registers, Gate 1 evidence, changelog, and current-state inventory. Run the full standard-library test suite and verify feature-branch CI.
5. Keep Gate 1 IN PROGRESS until approved contractual rights, trustworthy availability evidence, identity mappings, tests, and CI satisfy all criteria. Do not integrate a feed or spend money in this increment.

## Highest-value next increment after Gate 1

Gate 2 should begin with deterministic Decimal/unit-aware calculation primitives and a reproducible run manifest, including exchange calendar/session identity and as-of snapshots. Its acceptance criteria must include independent fixtures for tick value, multiplier, quantity/step rounding, currency conversion, costs, invalid/missing specification handling, and exact replay hashes. Do not start strategy alpha or paid data acquisition before those controls and owner decisions are complete.
