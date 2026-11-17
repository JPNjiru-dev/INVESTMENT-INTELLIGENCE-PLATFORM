# Initial Implementation Plan

1. **Close checkpoint 0:** Complete post-initialization tree/history/config/license review; verify branch and recovery point. (In progress)
2. **Gate 1 foundation:** Define instrument and market observation contracts; identify rights-cleared sources; validate XAUUSD and NAS100 specifications. No live data until rights are approved.
3. **Gate 2 core:** Implement tested decimal/unit-safe calculations, event-time handling, reproducible run manifests, and fail-closed risk boundaries.
4. **Gate 3 research:** Add research fixtures and objective strategy interfaces; test look-ahead protections and validation workflow before claiming results.
5. **Gate 4 investment:** Add cited point-in-time fundamentals, equity/ETF screening, scenario and portfolio risk contracts.
6. **Gate 5 agents:** Persist task/agent registry and event state; build operations centre only against real backend state.
7. **Gate 6 approvals:** Implement immutable proposal and approval contracts; keep order submission disabled.
8. **Gate 7 commercial readiness:** Validate unit economics, support/security/privacy, and asset-specific rights before launch.
9. **Gate 8 HFT feasibility:** Separate research programme with actual venue, data, infrastructure, and latency evidence.

The first engineering increment after Gate 0 is a small instrument-domain contract and deterministic validation fixture, not a signal generator or live provider integration.
