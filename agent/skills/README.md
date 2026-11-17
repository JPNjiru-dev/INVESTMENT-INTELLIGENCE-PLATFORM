# Agent Skills and Contracts

Agents are logical responsibilities, not a requirement for separate services or models. Every agent contract must specify purpose, allowed inputs, outputs, evidence/provenance, permitted tools, forbidden actions, timeout/retry budget, failure behavior, audit fields, and human review conditions.

## Skill contracts

Each role is a reusable instruction contract inside one cost-efficient modular monolith; the files do not require one service or model per role. Read `AGENTS.md`, `GATES.md`, the data-rights register, the relevant domain contract, and the named skill before performing scoped work.

- [Supervisory orchestrator](supervisory-orchestrator/SKILL.md)
- [Market intelligence](market-intelligence/SKILL.md)
- [Quantitative research](quantitative-research/SKILL.md)
- [Technical research — ICT/SMC](technical-research-ict-smc/SKILL.md)
- [Fundamental equity research](fundamental-equity-research/SKILL.md)
- [Macro intelligence](macro-intelligence/SKILL.md)
- [Strategy validation](strategy-validation/SKILL.md)
- [Portfolio intelligence](portfolio-intelligence/SKILL.md)
- [Risk guardian](risk-guardian/SKILL.md)
- [Trade copilot](trade-copilot/SKILL.md)
- [Execution auditor](execution-auditor/SKILL.md)
- [Research librarian](research-librarian/SKILL.md)
- [Agent operations and observability](agent-operations-observability/SKILL.md)
- [Independent verification](independent-verification/SKILL.md)

Every skill defines mission, inputs/output, tools/data, forbidden actions, evidence, deterministic/AI boundaries, failure/uncertainty, resource limits, audit, human approvals and acceptance tests. No skill can authorize or submit an order. Deterministic risk logic is authoritative.

No agent may authorize or submit an order. Deterministic risk service is authoritative; agents cannot override it. Do not represent idle agents as working.
