# ADR 0002: Fail-closed data entitlement boundary

- **Status:** Accepted for the provider-neutral domain; no feed integration.
- **Date:** 2026-11-17.
- **Context:** Acquisition is not a license. Providers and exchanges scope permissions independently by dataset, geography, user class, display mode, derived output, redistribution, contract term and customer entitlement. Bar timestamps and source citations cannot prove these permissions.
- **Decision:** Add an explicit entitlement record and a deterministic check keyed by provider, dataset, intended use and evaluation time. Missing acquisition, evidence, approver, scope, or active term denies use. Permitted uses are separate values (internal, display, derived, redistribution). Operators must populate records only from an approved contract review. This check does not interpret legal terms and must be combined with customer-level authorization before any product display.
- **Consequences:** No provider data becomes usable by default. Product adapters must persist exact agreement evidence/version and expiry, and future authorization must intersect provider scope with customer scope. Rights do not expand because data were downloaded or transformed.
- **Revisit when:** The system adds a provider, dataset, customer sharing, regional availability, entitlement revocation, or contractual rights update.
