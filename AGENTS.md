# Repository working agreements

## Project boundaries
- Internal codename: `PROJECT_CODENAME`. Keep product name, logo, theme, and identity configurable.
- Read `GATES.md` before implementation. Do not proceed past a failed dependency gate.
- Inspect existing files and history before changing them. Preserve unrelated work.
- Keep this product in its own repository. Do not import RAE or other sibling-product code without file-level provenance, license and dependency review.
- Do not add paid services, material recurring costs, production deployments, changed permissions/secrets, real customer financial data, regulated custody/management, license changes, restricted IP, or public performance claims without explicit human approval.

## Financial and data integrity
- Financial calculations and risk permissions are deterministic, unit-aware, reproducible, and covered by automated tests.
- No fabricated prices, disclosures, data, backtests, or performance claims. Synthetic fixtures must be conspicuously identified and never presented as live evidence.
- Historical analysis must respect point-in-time availability, corrections, corporate actions, time zones, and survivorship.
- Record source, timestamp, rights, transformations, version, and parameters for research inputs and outputs.
- Treat missing or stale data as missing or stale; never silently substitute zero or inferred values.

## Agents and trade safety
- AI may research and explain with cited evidence; it cannot change financial truth or risk permissions.
- Every trade requires human approval bound to the exact proposal and expiry. Material changes require renewed approval.
- Autonomous order submission stays disabled.
- Give agents least-privilege tools, bounded tasks, explicit contracts, timeouts, retry limits, and audit trails.

## Engineering
- Prefer small, reviewable increments and a modular monolith until scale evidence supports services.
- Add dependencies only after documenting purpose, version, license, data handling, and cost.
- No credentials or customer secrets in source, logs, fixtures, or commits.
- Update the feature, license, data-rights, and changelog registers when applicable.
- Report exact validation commands/results, gate status, security/licensing/financial findings, open risks, and commit SHA.
