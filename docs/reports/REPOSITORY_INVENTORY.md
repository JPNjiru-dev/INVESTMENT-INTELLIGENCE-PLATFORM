# Repository Inventory and Architecture Map

**Updated:** 2026-11-17 (Africa/Nairobi)
**Repository:** [JPNjiru-dev/INVESTMENT-INTELLIGENCE-PLATFORM](https://github.com/JPNjiru-dev/INVESTMENT-INTELLIGENCE-PLATFORM)
**Default branch:** `main`
**Current work branch:** `feat/instrument-domain-foundation`
**Current recovery point at the start of this increment:** `dc334776a2b939b02a303848b1c084b778526552`
**Current audit status:** Initialized repository; Gate 0 PASS; Gate 1 IN PROGRESS. The original audit and prior inventory recorded the repository as public; the connected GitHub repository metadata currently reports private. Visibility was not changed in this increment. Current branch listing reports `protected=false` for both feature and main; the detailed protection endpoint returned 403 to the connected integration.

## Executive result — current state

**Prominent IP status:** The historical audit recorded this repository as public. Current connected GitHub metadata now reports it as private; this change occurred outside this increment or its timing/actor is otherwise unverified. No visibility setting was changed here. Branch protection was previously observed disabled, but current settings could not be read (GitHub API returned 403 to this connected integration); the owner should verify and configure required branch protection before proprietary research is committed. There is no declared repository license; absence of a `LICENSE` file is not a grant of open-source rights. Product identity remains configurable under `PROJECT_CODENAME` pending brand approval.

The requested feature branch starts from recovery point `dc334776a2b939b02a303848b1c084b778526552`; at the start of this continuation it was clean, tracked `origin/feat/instrument-domain-foundation`, and `main` remained at the audited baseline `36db1f967d41f5d1063fcfbd2772bc93b42f1109`. Prior successful CI evidence is documented in `GATES.md`. This increment adds no provider integration, external account, subscription, or live financial data.

The current repository includes governance and architecture documentation, Python provider-neutral instrument/bar contracts, a fail-closed data-entitlement primitive, unit tests, and pinned read-only unit-test CI. The runtime remains a small standard-library modular monolith; no persistence, identity, API, deployment or production feed is present. Detailed current architecture and research status are in `docs/MASTER_BLUEPRINT.md`, `GATES.md`, and `docs/research/`.

## Historic audit finding — initial state on 2026-11-17

At original audit time the GitHub target was empty: no refs, commits, files, README, license, workflows, dependency manifest, runtime, deployment, auth or data store. The local task workspace was not a clone. The correct original decision was to stop before implementation until the user confirmed the repository. These statements describe the initial audit only and remain preserved here as historical evidence; they do not describe the present repository.

The original audit recorded repository metadata (`default_branch=main`, `size=0`, no license), no branches, and API errors for commit/tree/content requests consistent with an empty repository. It recorded related repository listings and a reference-only review of the private MIT-licensed revenue-assurance-engine; no code/assets were copied. These observations are not a comprehensive audit of unrelated repositories or account-wide settings.

## Current repository inventory

| Area | Current evidence | Assessment |
|---|---|---|
| Governance | `AGENTS.md`, `GATES.md`, `CHANGELOG.md` | Gate 0 passes; Gate 1 stays open pending source-rights and availability evidence |
| Architecture | `docs/MASTER_BLUEPRINT.md`, `docs/architecture/`, ADRs | Modular monolith constraints; technology choices remain open |
| Instrument/data core | `src/project_codename/instruments.py`, `market_data.py`, `temporal.py`, `data_rights.py` | Provider-neutral model and deterministic explicit-use denial/allow check; no integration |
| Tests | `tests/test_instruments.py`, `test_market_data.py`, `test_data_rights.py` | Standard-library `unittest`; do not treat synthetic fixtures as market evidence |
| CI | `.github/workflows/ci.yml` | Read-only permissions; checkout/setup actions pinned by commit SHA; run history in GATES |
| Agent instructions | `agent/skills/` | Role skill files; logical roles do not require separate AI services |
| Provider/instrument research | `docs/research/` | Public documentation assessed; no legal approval or actual provider selection |
| Data rights | `DATA_RIGHTS_REGISTER.md` | No active rights or ingestion permission |
| Dependencies | No runtime dependency manifest | Standard library only; CI actions separately recorded in notices |
| Application stack, persistence, auth, deployment | No implemented service or infrastructure | Not selected; no production capability claim |
| License and visibility | No LICENSE; previously public in audit, currently private per GitHub repo metadata | Owner should confirm visibility; no license inference or setting changes |
| Branch protection | GitHub branches list reports `protected=false` for `main` and current feature branch; detailed endpoint returns 403 | Owner should configure required rules; organization policies not inspected |

## Architecture map

```text
Research and agent skill contracts (instructions; not standalone services)
                     |
             Future application/API
                     |
         Provider-neutral deterministic domain
       instruments + timestamps + market observations
                 + data-rights check
                     |
       Future storage/adapters behind explicit approval
                     |
 Vendors, exchange agreements, calendars, fundamentals
```

Data must be acquired and separately entitled for the exact provider, dataset, scope, use, user and effective time. The entitlement function does not parse legal terms and no entitlement is currently populated. A source timestamp does not prove historical availability. See `docs/architecture/MARKET_DATA_CONTRACT.md`.

## Initial risks and controls — current

| Risk | Control/evidence | Remaining issue |
|---|---|---|
| Market-data rights | Provider assessment and fail-closed use entitlement model | No contract/approval; provider/customer terms and geo/scope must be confirmed |
| Look-ahead and revisions | `available_at` replay filter; documented source-availability caveat | Caller can supply an untrusted timestamp; source-specific history/revision times unresolved |
| Instrument ambiguity | Provider/venue-scoped records, typed spot/CFD/future/index/equity/ETF | CFD identity/provider profiles not selected; no calendar or symbol service |
| Financial correctness | Decimal contracts, finite values, negative futures prices representable | No position sizing/calculation implementation yet |
| Unsafe trading | Product rules prohibit agent authorization/order submission | No trade product exists; future control tests remain needed |
| Public exposure of IP | Public status flagged for owner; branch protection absent in observed repo settings | Owner to decide privacy and branch rules; no setting changed |
| Supply chain | Pinned, least-privilege CI actions; standard-library runtime | Future dependencies need complete license/supply-chain review |

## Provider/research status

Representative candidates and their publicly documented source facts, commercial/rights limitations, unknowns and URLs are recorded in `docs/research/MARKET_DATA_PROVIDER_ASSESSMENT.md`. Source-verified instrument profiles, including distinct gold and Nasdaq-100 forms, are recorded in `docs/research/INITIAL_INSTRUMENT_SPECIFICATIONS.md`. These are research artifacts and do not authorize use. Gate 1 remains IN PROGRESS.

## Audit scope and provenance

This current-state inventory is based on local tracked files, branch/commit/status inspection, current repository metadata, documented prior GitHub/CI observations, and primary-source documentation linked in the research reports. The initial empty-state audit above is intentionally retained as a historical section. Neither section claims a full review of organization-level GitHub policies, secrets, or all unrelated account repositories.
