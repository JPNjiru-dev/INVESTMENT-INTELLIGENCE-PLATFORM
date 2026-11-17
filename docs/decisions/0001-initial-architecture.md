# ADR 0001: Initial architecture constraints

- **Status:** Accepted as constraints; implementation stack remains undecided.
- **Date:** 2026-11-17.
- **Context:** New global investment intelligence product, empty repository, broad asset scope, strict financial/data safety needs.
- **Decision:** Keep independently developed product in its own repository. Use logical domain boundaries and begin with a modular monolith. Keep financial truth and risk deterministic. Treat point-in-time correctness, data rights, provenance, and human trade approval as hard system constraints. Keep brand identity configurable.
- **Consequences:** No premature microservices or provider commitments. Choose languages, storage, hosting, and vendors only after a small architecture spike and rights/cost review.
- **Revisit when:** Measured load, team ownership, availability, or isolation needs demonstrate a concrete benefit.
