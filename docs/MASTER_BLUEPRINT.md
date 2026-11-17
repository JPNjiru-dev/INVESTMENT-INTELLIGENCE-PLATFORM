# Master Blueprint — PROJECT_CODENAME

## Mission
Help investors and researchers improve decision quality through traceable market intelligence, independently validated research, portfolio risk analysis, and human-reviewed proposals. Preserve capital and avoid unsupported performance claims.

## Product principles
1. Evidence before conclusions: cite source, timestamp, instrument, and transformations.
2. Deterministic financial truth: calculations and risk permissions do not depend on model output.
3. Point-in-time correctness: historical analysis can access only information available then.
4. Human authority: agents may prepare proposals but cannot authorize or submit trades.
5. Broker independence: normalize provider-specific data without conflating spot, CFD, futures, ETFs, indices, equities, or crypto.
6. Cost discipline: begin as a modular monolith; add services/providers only when justified.
7. Configurable identity: use `PROJECT_CODENAME` internally until brand approval.

## Proposed logical architecture
- **Presentation:** research workspace, portfolio views, proposal review, and Agent Operations Centre.
- **Application/API:** authenticated user-scoped commands and queries, policy checks, task orchestration, and audit events.
- **Domain core:** instrument master, calendars, market observations, corporate actions, research runs, risk calculations, portfolios, proposals, approvals, agent/task contracts.
- **Adapters:** market/fundamental/news sources, storage, identity, AI model providers, notifications, and optional execution audit integrations.
- **Persistence:** relational metadata and transactional state; object/time-series storage only when workload and licensing justify it.
- **Event path:** persisted state transitions and correlated events; frontend status is derived from backend records, never simulated.

These are direction-setting boundaries, not committed technology selections. Stack choices follow a documented decision after gate 0 and requirements validation.

## Current validated foundation (2026-11-17)

The repository now has a provider-neutral Python domain package with instrument identity/specification records, UTC timestamp checks, OHLCV observations and source revision selection; a standard-library unit-test suite and read-only pinned-action CI workflow; and an explicit default-deny entitlement primitive. These are foundational controls, not a connected market-data system. No vendor is selected, no real feed or portfolio data is connected, and no instrument specification is populated from the research drafts until mappings are independently confirmed. The exact current file inventory and historic-vs-current audit distinction are maintained in `docs/reports/REPOSITORY_INVENTORY.md`.

The modular monolith remains the architecture. `agent/skills/` contains role instructions; those files do not create separate processes, model services, or deployment units. Instrument identity is provider/venue scoped; data records require an explicit rights decision before use; and a source-provided timestamp alone does not establish historical availability.

## Initial scope order
1. Repository controls, gate ledger, provenance, threat model.
2. Instrument and observation contracts; validate XAUUSD and NAS100 identity/specifications (Gate 1 still in progress; provider-specific and contractual evidence unresolved).
3. Point-in-time market-data ingestion and deterministic calculations.
4. Reproducible research runs and risk limits.
5. Objective, versioned strategy hypotheses and validation.
6. Fundamentals, equity discovery, and portfolio analysis.
7. Evidence-grounded copilot and persisted agent operations.
8. Human proposal approvals; broader asset classes; commercial readiness.
9. Separate HFT feasibility study.

## Non-goals for initial increments
- Live order routing or autonomous execution.
- Claims of profitability or accuracy.
- Premature microservices, payments, custody, or discretionary management.
- Treating ICT/SMC terminology as validated alpha.
- Operational HFT claims.

## Unresolved architecture decisions
Runtime, database, market-data vendors, identity provider, AI provider, deployment target, real-time transport, charting, and licensing policy remain undecided. Capture decisions in `docs/decisions/` with evidence and reversibility.
