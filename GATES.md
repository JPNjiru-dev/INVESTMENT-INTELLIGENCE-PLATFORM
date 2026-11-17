# Acceptance Gates — PROJECT_CODENAME

This file controls project progression. A gate passes only when every required criterion is evidenced and recorded. No feature claim, deployment, financial performance claim, or release may bypass a failed prerequisite. Status values: `NOT STARTED`, `IN PROGRESS`, `PASS`, `FAIL`, `BLOCKED`.

## Gate rules

- Record evidence links, commit/ref, commands, and exact outcomes for every pass/fail criterion.
- A missing result is not a pass. No synthetic or fabricated financial data may be represented as live market data or performance evidence.
- A changed calculation, data contract, risk control, or approval path invalidates affected evidence and requires rerun.
- Stop the affected work on unresolved data rights, unclear license provenance, point-in-time leakage, financial arithmetic mismatch, unauthorized data exposure, missing human approval, or a security issue that can affect customer data or order authorization.
- Autonomous order submission remains disabled. Every trade requires human approval; material proposal changes require a new approval.
- Paid services/material recurring costs, production deployment, changed permissions/secrets, real customer financial data, regulated management/custody features, license changes, restricted IP, or public performance claims require explicit human approval before the action.
- Keep a recovery point before every material change; record the Git commit when available. Until Git is initialized, retain reviewable workspace artifacts and do not report a commit hash.

## Checkpoints

### Checkpoint 0 — Repository, licensing, and architecture audit

**Status: BLOCKED**  
**Dependencies:** Target repository identified (passed); first commit/default branch and inspectable checkout (not met).  
**Evidence:** [`REPOSITORY_INVENTORY.md`](REPOSITORY_INVENTORY.md); GitHub target metadata, empty branch list, commit/tree 409 responses, contents 404 response; local workspace `git rev-parse` reports not a repository.

| ID | Pass criteria | Fail/stop condition | Current |
|---|---|---|---|
| 0.1 | Intended repository URL, owner, visibility, access, default branch, refs and current commit recorded | Repository ambiguous or inaccessible | PASS: identified; repository public/admin access |
| 0.2 | Complete tracked tree, history, README, configs, workflows, dependencies, license, deployment/auth/data stores inspected | Cannot inspect baseline | BLOCKED: target is empty; no commit/ref/tree |
| 0.3 | Relevant NiaKili references and licensing/provenance reviewed; no unclear/restrictive content copied | Unclear provenance for proposed reuse | PASS for reference-only review of RAE; broader unrelated repos not fully audited |
| 0.4 | Architecture map and initial security/data-rights/financial risk assessment recorded | Material unknown risk omitted | PASS: initial map and risks documented; repository architecture is unselected |
| 0.5 | Working checkout on verified default branch and safe recovery point recorded | No checkout or commit available | BLOCKED |

**Gate 0 passes when:** 0.1–0.5 all pass on an actual initialized repository.  
**Next action:** Initialize target repository and provide a checkout/first commit; repeat 0.2 and 0.5. Do not start product implementation before this gate passes.

### Checkpoint 1 — Product domain, global instrument model, and market data

**Status: NOT STARTED**  
**Dependencies:** Gate 0 PASS; approved data-source rights and product scope.

Pass only when instrument types correctly distinguish spot, CFD, futures, ETF, index, and equity; identifiers include venue/provider and currency/contract conventions as applicable; XAUUSD and NAS100 mappings have independently verified specifications; event/timezone/calendar semantics are explicit; point-in-time historical and real-time contracts prevent future data access; data provenance, quality, correction, stale-state, and entitlement handling are documented and tested; selected sources' storage/display/derived/redistribution rights are approved and entered in `DATA_RIGHTS_REGISTER.md`.

Stop on ambiguous instrument semantics, unlicensed data, look-ahead leakage, fabricated/stale values shown as current, or unresolved entitlement enforcement.

### Checkpoint 2 — Deterministic calculations, research, and risk foundations

**Status: NOT STARTED**  
**Dependencies:** Gate 1 PASS.

Pass only when all financial calculations use deterministic, unit-aware, precision-safe methods; tests cover boundary, rounding, currency conversion, multipliers, fees, and invalid input; independent reference calculations match exactly within the documented numeric contract; every research run records data snapshot, code/strategy version, parameters, costs, and output hashes; risk limits are deterministic and fail closed; no AI output can alter calculation truth or risk permissions.

Stop on unexplained discrepancy, non-reproducible run, missing cost assumptions, or fail-open risk path.

### Checkpoint 3 — XAUUSD/NAS100 research, validation, ICT/SMC framework

**Status: NOT STARTED**  
**Dependencies:** Gates 1–2 PASS; instrument/data rights approved.

Pass only when operational definitions for each implemented ICT/SMC concept are versioned, reproducible, and measurable; data is point-in-time; baselines and transaction costs are explicit; in-sample discovery is separated from untouched out-of-sample evaluation; walk-forward, robustness, and sensitivity analyses run without leakage; adverse periods and drawdowns are reported; paper trading is completed with recorded discrepancies. No concept is presumed profitable, and no performance claim is made without reviewed evidence.

Stop on leakage, fabricated data/results, unmodeled material costs, or unreviewed public claims.

### Checkpoint 4 — Investment research, equity screening, portfolio intelligence

**Status: NOT STARTED**  
**Dependencies:** Gates 1–2 PASS; fundamental data rights and corporate-action methodology approved.

Pass only when screening handles delistings, restatements, splits, currencies, and point-in-time fundamentals; company metrics reconcile to cited filings/providers; low nominal share price is not treated as valuation; scenarios identify assumptions and failure cases; portfolio exposures, concentration, currency, correlation, drawdown, and stress results are reproducible; tax/fee caveats and data provenance are visible. User-facing investment conclusions are clearly research, with no unauthorized discretionary management.

### Checkpoint 5 — AI copilot and multi-agent operations centre

**Status: NOT STARTED**  
**Dependencies:** Gates 1–2 PASS; security/privacy design review.

Pass only when agent registry/task state machine/event history/handoffs persist in backend; UI states reflect backend truth and stale/disconnected conditions; inputs, outputs, evidence, retries, failures, costs, and approval needs are inspectable subject to authorization; task correlation IDs and audit trails are tested; tool scopes, timeouts, retries, and failure boundaries are explicit; reduced-motion/accessibility requirements pass review; unsupported claims are rejected or visibly marked as hypotheses; no agent can authorize or submit orders.

Stop on invented activity, missing evidence provenance, cross-tenant leakage, or capability to bypass human approval.

### Checkpoint 6 — Human approval, auditability, and product experience

**Status: NOT STARTED**  
**Dependencies:** Gates 1–5 as applicable; security review.

Pass only when every proposal is bound to user/account, instrument, direction, quantity, entry constraints, stop, target, maximum risk, strategy/version, proposal ID, and expiry; stale, expired, rejected, withdrawn, or materially altered proposals cannot proceed; approval identity/time and proposal digest are immutable and auditable; authorization failures are tested; autonomous submission remains disabled; responsive/accessibility and recovery flows are reviewed.

### Checkpoint 7 — Asset expansion and commercial readiness

**Status: NOT STARTED**  
**Dependencies:** Prior relevant gates PASS; human approval for any costs, external data commitments, customer data, public launch, or paid infrastructure.

Pass only when each new asset class has separate data-rights/instrument/corporate-action/market-calendar validation; service costs and gross-margin assumptions are documented; packaging and willingness-to-pay research precede payments; security, privacy, support, incident response, backup/recovery, and operational ownership are evidenced; no unsupported profitability, accuracy, or regulatory claims are published.

### Checkpoint 8 — HFT feasibility research

**Status: NOT STARTED**  
**Dependencies:** Separate approved feasibility scope; suitable venue/data access, infrastructure and latency measurements.

Pass only as a feasibility conclusion supported by venue rules, timestamp/clock-quality review, raw data entitlement, measured network/compute latency distribution, order-book fidelity, transaction/queue cost model, deterministic replay, failure/recovery plan, and independent review. A one-minute strategy is not HFT. No operational HFT capability may be marketed without separate evidence and approval.

## Cross-cutting acceptance requirements

- **Testing:** No gate passes without listed, reproducible test evidence. Financial calculations require automated tests and independent fixtures. Run exact suites/commands and report actual outcomes.
- **Security:** Threat model, access boundaries, secrets handling, dependency/supply-chain review, logging minimization, authorization tests, and incident response evolve with scope.
- **Licensing:** Record direct/transitive software and asset licenses; stop before introducing incompatible, unknown, or unapproved restricted IP.
- **Data rights:** Record source, instrument/fields, acquisition path, retention, display, derived-use, redistribution, user scope, cost, and approval.
- **Human approvals:** Trade approvals are mandatory. Additional approvals are required for the explicitly listed commercial, security, privacy, regulatory, license, and public-claim changes.
- **Evidence:** Each result needs source/time, code/config/version, parameters, environment, command, exact output, and reviewer where relevant.

## Progress ledger

| Date | Checkpoint | Change/evidence | Status | Recovery point |
|---|---|---|---|---|
| 2026-11-17 | 0 | Target repository confirmed empty; audit and risk map written in workspace | BLOCKED | No Git checkout or commit available |


