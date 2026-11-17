# Skill — Strategy Validation

## 1. Mission and responsibilities
Evaluate whether a frozen strategy hypothesis generalizes after realistic costs and operational constraints. Produce evidence that can reject the hypothesis; never optimize toward a desired result.

## 2. Required inputs and output schema
Require `{strategy_id,version,preregistration_id,universe,data_snapshot,train_period,validation_period,test_period,benchmark,cost_model,execution_assumptions,calendar}`. Output `{status,integrity_checks,validation_design,metrics,drawdowns,turnover,capacity_assumptions,cost_sensitivity,robustness,subperiods,benchmark,limitations,pass_fail_reasons,reviewers,audit}`.

## 3. Permitted tools and data
Approved point-in-time datasets, deterministic backtest engine, independent calculation fixtures, and paper-trading logs only when separately authorized.

## 4. Forbidden actions
No leaked/overlapping samples, survivorship bias, omitted fees/slippage/funding, post-hoc strategy edits in test period, cherry-picking, synthetic performance presented as real, or public claims before approval.

## 5. Evidence and citation requirements
Link all input snapshots, contract/calendar/corporate-action versions, code hash, parameter lock, source license and execution assumptions. Document every tested variant.

## 6. Deterministic versus AI responsibilities
Backtest, splits, statistics, costs and acceptance thresholds are deterministic. AI may review failure modes and explain, never change frozen strategy or thresholds.

## 7. Failure handling and uncertainty
Abort on leakage, failed reconciliation, missing rights, insufficient observations or unmodeled material costs. Mark inconclusive; do not convert failure to pass.

## 8. Cost and resource limits
One frozen strategy, fixed compute budget and at most preregistered sensitivity set. Avoid repeated sweeps; no paid compute/data without approval.

## 9. Audit requirements
Immutable run manifest, logs, full parameter search history, inputs/output hashes, environment, reviewer findings and gate linkage.

## 10. Human approval conditions
Independent human reviewer signs test design and result. Owner approval for paper accounts, publication, live/personalized advice or paid services. Any trade still requires user approval bound to exact proposal.

## 11. Testing and acceptance criteria
Leakage tests, independent metric comparison, untouched holdout, walk-forward, transaction-cost stress, parameter sensitivity, adverse regimes and paper discrepancy review. All required evidence must pass; no presumed profitability.
