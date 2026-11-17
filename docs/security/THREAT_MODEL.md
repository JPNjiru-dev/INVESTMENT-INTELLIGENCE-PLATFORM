# Initial Threat Model

## Assets
Account credentials and sessions; portfolio/financial data; licensed market data; research/proposal records; approval decisions; secrets; agent tools and audit history.

## Trust boundaries
User/browser to API; tenant to tenant; application to external data/model providers; orchestrator to specialist agents/tools; proposal preparation to human approval; build system to production artifacts.

## Initial threats and controls
- Cross-account data exposure: tenant-bound authorization on every query and event stream; negative tests.
- Secret leakage: secret manager/environment injection, redacted logs, scanning, rotation procedure.
- Prompt injection or fabricated evidence: treat external content as untrusted data, restrict tools, require citations, validate schema.
- Agent privilege escalation: least privilege, explicit contracts, bounded tool scopes, timeouts, audit trail.
- Stale/replayed/altered proposal: immutable proposal digest, account and instrument binding, expiry and one-time approval.
- Market-data rights breach: source entitlement checks and rights register before ingestion/display.
- Historical leakage: availability timestamps and point-in-time tests.
- Supply-chain compromise: pinned lockfile, dependency inventory, CI checks and review.
- Denial/staleness: visible connection freshness, bounded retries, fail closed for risk-sensitive decisions.

## Current limits
No application, user data, secrets, integrations, or infrastructure are present. This document is an initial design assessment, not a penetration test. Reassess before each relevant gate and before handling customer data.
