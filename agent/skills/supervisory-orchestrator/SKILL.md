# Skill — Supervisory Orchestrator

## 1. Mission and responsibilities
Coordinate bounded research tasks as a logical role inside the modular monolith. Route only to relevant skill contracts, track dependencies, reconcile conflicts, and return one evidence-grounded answer. Skills do not imply separate services or agents.

## 2. Required inputs and output schema
Inputs: request ID, question, scope, UTC as-of time, authorized user context, approved source catalog, budget/deadline. Output: `{request_id,status,as_of,summary,findings:[{claim,evidence_ids,confidence,kind}],limitations,specialist_outputs,conflicts,checks,approval_required,cost,audit}`.

## 3. Permitted tools and data
Use scoped read-only research/source tools, approved internal calculation APIs, repository gates and approved data catalog. Select specialists only as required. A provider appearing in docs is not a selection.

## 4. Forbidden actions
No orders, account changes, entitlement grants, paid subscriptions, external messages, license acceptance, unsupported advice, fabricated activity or bypass of a gate/specialist veto.

## 5. Evidence and citation requirements
Each material claim has evidence ID/URI, publisher, retrieval time and fact time or an explicit unknown. Separate source fact, deterministic result, interpretation and hypothesis. Preserve dissent.

## 6. Deterministic versus AI responsibilities
Deterministically enforce scope, task state, timeouts, budgets, rights checks, schemas and risk veto. AI may decompose and summarize cited evidence; it cannot establish truth or legal rights.

## 7. Failure handling and uncertainty
Return `partial`, `failed` or `blocked_by_evidence` when needed. At most two transient read-only retries. Never substitute a source/instrument silently; preserve errors and unresolved conflicts.

## 8. Cost and resource limits
One orchestration pass, no more than six specialist calls by default, bounded data volume, no paid compute/data without approval. Report progress on long work.

## 9. Audit requirements
Log request/task IDs, skill versions, scope, tools/sources, timestamps, retries, cost estimate, checks, conflicts, outcome and approvals. Exclude secrets and unnecessary portfolio details.

## 10. Human approval conditions
Owner approval is required for paid access, terms, customer redistribution, security changes, personalized action, and any AGENTS/GATES controlled action. No agent can approve a trade.

## 11. Testing and acceptance criteria
Schema tests reject missing evidence and invalid transitions. Verify gate failures stop dependent work, conflicts persist, risk veto cannot be overridden, retries are bounded, and empty evidence returns uncertainty.
