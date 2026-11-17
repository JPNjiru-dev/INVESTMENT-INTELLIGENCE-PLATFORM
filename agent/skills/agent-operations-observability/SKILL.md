# Skill — Agent Operations and Observability

## 1. Mission and responsibilities
Define auditable task lifecycle and operational health for logical agent work: queued, running, waiting, succeeded, partial, failed, cancelled. Report system state from persisted events.

## 2. Required inputs and output schema
Require `{task_id,request_id,skill_version,scope,started_at,deadline,tool_policy,budget}`. Output `{task_id,state,events:[{sequence,time,type,actor,correlation_id,details}],attempts,cost_estimate,latency,errors,staleness,approval_wait,audit_integrity}`.

## 3. Permitted tools and data
Read task/event logs and approved metrics; write only through authorized task-state service. Use aggregate operational metrics and minimized payloads.

## 4. Forbidden actions
No fake activity, simulated progress, editing history, logging secrets/raw portfolio data, increasing permissions or retrying past budget.

## 5. Evidence and citation requirements
Every displayed state derives from a persisted event with sequence/correlation ID and timestamp. Expose source and last-updated time; label estimated cost as estimate.

## 6. Deterministic versus AI responsibilities
State machine, timeout, retry, cost and authorization enforcement are deterministic. AI may summarize an error; it cannot change state or suppress alerts.

## 7. Failure handling and uncertainty
Show stale/disconnected/unknown when events stop or integrity check fails. Do not present last state as current. Dead-letter repeated failures for review.

## 8. Cost and resource limits
Bound logs, retention and metric cardinality. Cap retries and tool/model budget per task. No continuous polling faster than configured service limits.

## 9. Audit requirements
Append-only events include IDs, actor, skill/tool version, timing, retries, cost, reason and parent task; access to logs is least privilege.

## 10. Human approval conditions
Operator approval for retry budget/retention policy changes, permission changes, incident closure and actions with external effects.

## 11. Testing and acceptance criteria
Test invalid state transitions, duplicate events, clock skew, timeout, retries, lost connection, stale UI, cost cap and PII redaction. UI state must match persisted backend state.
