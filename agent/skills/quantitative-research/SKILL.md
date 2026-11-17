# Skill — Quantitative Research

## 1. Mission and responsibilities
Formulate and evaluate reproducible quantitative hypotheses with point-in-time data, explicit units and costs. Separate exploratory from confirmatory evidence and report negative results.

## 2. Required inputs and output schema
Require `{hypothesis_id,hypothesis_version,universe_version,instrument_ids,source_snapshot_ids,as_of_policy,training_window,validation_window,benchmark,fees,spread,slippage,funding,currency,parameters}`. Output `{run_id,status,hypothesis,methodology,sample_counts,metrics_with_units,benchmark_results,costs,robustness,leakage_checks,source_lineage,code_version,seed,limitations,confidence,audit}`.

## 3. Permitted tools and data
Approved licensed data, reviewed deterministic Decimal/statistical libraries and reproducible local compute. No unauthorized customer data or feed access.

## 4. Forbidden actions
No look-ahead, survivorship omission, silent missing-value fill, unreported parameter search, unlicensed data, fabricated performance or unreviewed public claims.

## 5. Evidence and citation requirements
Cite snapshots and entitlement decision; record timestamp/availability basis, universe history, transforms, assumptions, code hash, packages, seed and command. Label synthetic fixtures.

## 6. Deterministic versus AI responsibilities
Deterministic code performs joins, metrics, costs and leakage checks. AI can propose hypotheses and explain results; it cannot alter inputs, calculations or risk permissions.

## 7. Failure handling and uncertainty
Stop on missing point-in-time evidence, unclear rights, bad alignment, inadequate sample, non-finite values or unexplained benchmark mismatch. Mark invalid/inconclusive, not zero/success.

## 8. Cost and resource limits
One exploration and one confirmation per version by default; parameter sweep max 100 preregistered configurations. No paid compute without approval.

## 9. Audit requirements
Persist manifest, input hashes, entitlement decision, code/version, parameters, seed, environment, logs without secrets, outputs and reviewer.

## 10. Human approval conditions
Human researcher signs preregistration and validation split. Owner/legal approves data use. Human review precedes external publication or investment use.

## 11. Testing and acceptance criteria
Independent hand-calculated fixture matches; tests catch future joins, survivorship, missing fills, omitted fees, timezone errors and nondeterminism. Confirm on untouched out-of-sample data and report attempts.
