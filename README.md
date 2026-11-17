# PROJECT_CODENAME

NiaKili Systems Global Investment Intelligence Platform. The product brand is configurable; `PROJECT_CODENAME` is an internal placeholder until the final name is approved.

## Current status

Repository bootstrap and checkpoint 0 audit are in progress. No market data provider, trading integration, live order capability, or investment-performance claim is enabled. This project is research software and is not yet a production investment service.

## Governing documents

- [Acceptance gates](GATES.md) control all progression.
- [Repository inventory](docs/reports/REPOSITORY_INVENTORY.md) records the initial environment audit.
- [Master blueprint](docs/MASTER_BLUEPRINT.md) defines architecture direction and boundaries.
- [Feature register](product/FEATURE_REGISTER.md) tracks value, costs, risks, dependencies, and acceptance criteria.
- [Security threat model](docs/security/THREAT_MODEL.md) and [data rights register](DATA_RIGHTS_REGISTER.md) track hard constraints.

## Safety boundaries

All financial calculations and risk permissions must be deterministic and reproducible. AI-generated research must cite evidence and distinguish facts, calculations, interpretations, and hypotheses. Human approval is mandatory for every trade proposal. Autonomous order submission is disabled.
