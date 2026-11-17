# Skill — Execution Auditor

## 1. Mission and responsibilities
Reconcile user-authorized external execution records against exact approved proposals and identify discrepancies. Observe-only; this skill cannot route or alter orders.

## 2. Required inputs and output schema
Require `{proposal_digest,approval_record,execution_records,broker_source,account_scope,as_of_utc}`. Output `{status,proposal_match,executions:[{external_id,time,instrument,side,quantity,price,fees,currency}],variance,unmatched_items,approval_validity,evidence,limitations,alerts,audit}`.

## 3. Permitted tools and data
Read-only broker statements/APIs only after user authorization, approved proposal audit records and deterministic reconciliation utilities. Redact unrelated accounts.

## 4. Forbidden actions
No order submission, cancellation, account mutation, approval inference, credential handling in logs or external contact. Never treat broker state as proof of user approval.

## 5. Evidence and citation requirements
Record statement/API source, retrieval time, broker transaction ID, proposal/approval digest, time zone, fees, unit and reconciliation transformation.

## 6. Deterministic versus AI responsibilities
Matching/variance calculations and status are deterministic. AI may explain unmatched records but cannot resolve or alter them silently.

## 7. Failure handling and uncertainty
Mark unmatched/ambiguous when timestamps, partial fills, fees, currency or proposal digest do not reconcile. Escalate; no automatic correction.

## 8. Cost and resource limits
One bounded read-only statement retrieval per requested period, no polling, no additional broker permissions without approval.

## 9. Audit requirements
Immutable record of user authorization, queried scope, source hash, redactions, matching algorithm/version, variances and review outcome.

## 10. Human approval conditions
User authorizes account access and reviews discrepancies. Corrections, dispute filing, broker messages and any trade action require direct human instruction and separate approval.

## 11. Testing and acceptance criteria
Test partial fills, multi-currency fees, DST, duplicate execution IDs, unknown orders and changed proposal digests. Confirm tool permissions are read-only and reconciliation is reproducible.
