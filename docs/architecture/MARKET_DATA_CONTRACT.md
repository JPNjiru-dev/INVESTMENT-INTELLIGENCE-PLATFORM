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

Evidence references record provenance, not correctness or permission. Provider terms, time-stamp quality, corrections, entitlement history, calendars, corporate actions, and redistribution remain separate acceptance work. No provider should be connected until those rights and semantics are reviewed.
