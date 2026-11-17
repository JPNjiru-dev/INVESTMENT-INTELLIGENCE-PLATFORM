# Skill — Portfolio Intelligence

## 1. Mission and responsibilities
Measure portfolio exposures, concentration, currency, correlation, liquidity, drawdown and stress using authorized holdings and point-in-time valuations. Describe risks without discretionary asset management.

## 2. Required inputs and output schema
Require `{portfolio_id,authorized_snapshot,as_of_utc,positions:[{instrument_id,quantity,cost_basis,currency}],prices_snapshot,fx_snapshot,corporate_actions,benchmark,stress_scenarios}`. Output `{status,valuation,exposures,concentration,currency,correlation,liquidity,drawdown,stress_results,missing_inputs,assumptions,source_lineage,confidence,limitations,audit}`.

## 3. Permitted tools and data
User-authorized portfolio snapshot, approved price/FX sources, deterministic calculations and point-in-time corporate actions. Least-privilege read-only access.

## 4. Forbidden actions
No guessing missing quantity/price/FX, silent substitution, trading/rebalancing, account modification or sharing customer information with external models/services without approval.

## 5. Evidence and citation requirements
Record holding source/time, price/FX source, rights decision, instrument/spec version, corporate-action policy, calculation units and as-of cutoff.

## 6. Deterministic versus AI responsibilities
Valuation, exposure, return, correlation and stress math are deterministic. AI can explain concentration and scenarios; it cannot alter positions or calculate risk permissions.

## 7. Failure handling and uncertainty
Mark unvalued positions when price/spec/FX is missing or stale; do not substitute zero. Fail closed on expired data rights, invalid units or ambiguous mapping; show partial totals with explicit exclusions.

## 8. Cost and resource limits
Use one approved point-in-time market snapshot; limit stress set to ten scenarios by default. No paid feed or external upload without approval.

## 9. Audit requirements
Log snapshot hashes, access scope, entitlement decisions, transformations, excluded positions, calculation version and output digest. Minimize PII.

## 10. Human approval conditions
Portfolio owner authorizes input scope; qualified human reviews investment interpretation. No portfolio adjustment/execution without explicit, separate human approval.

## 11. Testing and acceptance criteria
Test units, FX conversions, corporate actions, missing/stale marks, concentration, negative holdings, correlation windows and reproducible stress outputs. All excluded value is visible.
