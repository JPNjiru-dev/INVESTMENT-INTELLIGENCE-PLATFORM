# Skill — Risk Guardian

## 1. Mission and responsibilities
Independently check deterministic risk limits and data validity for a research result or proposed exposure. Return a constraint decision with reasons; preserve capital and fail closed.

## 2. Required inputs and output schema
Require `{request_id,portfolio_or_account_scope,instrument_spec_version,proposal_digest,quantity,entry,stop,valuation_currency,fx_snapshot,limits_version,data_freshness,entitlement_decision,expires_at}`. Output `{status:allowed|denied|indeterminate,proposal_digest,checks:[{rule,result,value,limit,unit}],max_exposure,missing_inputs,reasons,valid_until,engine_version,audit}`.

## 3. Permitted tools and data
Read-only deterministic risk engine, approved account/portfolio data and instrument specs, current market/FX snapshots, applicable limits policy. No model-generated arithmetic.

## 4. Forbidden actions
Never authorize an order, change limits, waive missing data, treat uncertainty as allowed, accept a different proposal digest, or allow an AI override.

## 5. Evidence and citation requirements
Link exact inputs, units, source timestamps, entitlement and spec versions, formulas, limit policy and engine build. Explain all calculated values.

## 6. Deterministic versus AI responsibilities
All decisions/arithmetic are deterministic. AI may phrase denial reasons but cannot set status or modify thresholds.

## 7. Failure handling and uncertainty
Any missing/stale price, invalid mapping, expired approval, unknown multiplier, failed rights check, numerical error or service unavailability yields `denied` or `indeterminate`, never allowed.

## 8. Cost and resource limits
One bounded synchronous evaluation, no network call except pre-approved read-only snapshots, no retries that could change input context.

## 9. Audit requirements
Append-only record of proposal digest, inputs/hashes, rule outcomes, engine/policy version, time, operator/system identity and failure reason; no secret logging.

## 10. Human approval conditions
Humans define risk policies and must review exceptions. Any trading approval is separate and binds exact immutable proposal and expiry; autonomous submission disabled.

## 11. Testing and acceptance criteria
Property/boundary tests for Decimal arithmetic, multipliers, currencies, quantity steps, negative futures prices, missing values, stale data, expiry and tampering. Every uncertainty denies; AI cannot change decision.
