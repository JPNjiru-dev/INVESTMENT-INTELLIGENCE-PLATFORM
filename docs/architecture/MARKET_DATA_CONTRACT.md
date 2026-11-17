# Market Data Contract — Initial Bar Semantics

## Scope

The current standard-library domain contract represents OHLCV bar observations and source revisions. It includes no feed adapter, prices, credentials, or data entitlement. Unit-test values are clearly synthetic fixtures and are not market evidence.

## Time fields

- interval_start is inclusive and interval_end is exclusive; both are UTC.
- available_at is when this exact source revision became available to the entitled analysis context. A finalized bar cannot be available before its interval ends.
- recorded_at is when this system captured that revision. It must not precede source availability and must never be backdated.
- Historical selection filters on available_at, not the later ingestion time. This is safe only when the source can substantiate historical availability for the relevant product and entitlement. Until that evidence exists, do not claim point-in-time-valid historical results.

## Revisions and state

Partial bars are excluded from finalized historical selection. For each instrument and interval, final_bars_as_of returns the available final revision with the latest (available_at, revision) pair and sorts intervals chronologically. Conflicting records with an identical availability time and revision number fail closed.

OHLC values must be finite Decimals and satisfy low/open/close/high ordering. Negative prices are representable because some futures can trade below zero. Volume may be absent or zero; negative and non-finite volume is rejected.

## Rights and limits

Evidence references record provenance, not correctness or permission. `data_rights.py` adds an explicit, fail-closed use check for acquired/internal/display/derived/redistribution use, evaluated against a provider, dataset, approval evidence, approver, and effective interval. It is an enforcement primitive, not a legal terms interpreter; provider rights and customer permissions must both be checked. Missing/expired evidence denies use. No actual entitlement is recorded and no provider should be connected until rights and semantics are reviewed.

Provider source-availability timestamps must be substantiated for the specific dataset, exact field and entitlement. When the vendor cannot establish when historical revisions were knowable, use capture-time only for prospective replay and exclude affected periods from point-in-time claims. `final_bars_as_of` still trusts the caller-provided `available_at`; it does not verify evidence quality or entitlement automatically. Integrators must authorize and validate before calling it.

Corrections have source-specific lifecycles. Preserve each captured revision and its source identity; never overwrite an earlier observed version. A fresh vendor historical response is not proof of when a correction became available. Where a vendor provides a corrected-current-history but no correction event time, do not use the corrected value in a past replay earlier than the system's first capture of that correction. Futures roll construction, corporate-action adjustment, market calendars, and cross-source discrepancies remain explicit upstream transformations with lineage.
