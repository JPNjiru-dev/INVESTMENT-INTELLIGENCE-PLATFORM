# Independent Review — Instrument and Bar Contracts

**Reviewed:** 2026-11-17 against recovery point `dc334776a2b939b02a303848b1c084b778526552` and additive changes in this increment.  
**Scope:** `instruments.py`, `market_data.py`, `temporal.py` and related unit tests. This is an engineering review, not approval of external specifications or data rights.

## Findings

| Area | Finding | Disposition |
|---|---|---|
| Decimal financial arithmetic | Prices/volume/specification numbers reject floats and non-finite values; negative finite prices are accepted, appropriate for negative futures prices. Volume semantics are generic and cannot yet distinguish FX quote count, equity shares, futures contracts or crypto base units. | Preserve Decimal checks. Require source-specific quantity semantics before adapter; documented in instrument research. |
| UTC and DST | Domain instants require UTC-aware datetimes; offset-aware non-UTC values are rejected instead of silently normalized. This avoids ambiguity at the instant layer. No market schedule/local IANA zone or DST fold/gap interpretation exists. | Keep UTC boundary; build a separate versioned market-calendar service before session logic. Add DST tests with calendar implementation, not fixed-offset conversion. |
| Instrument identity | `instrument_id` plus provider/symbol/optional venue can represent same display string from multiple providers if assigned unique IDs. No uniqueness registry, provider dataset ID, MIC validation or mapping relation exists. | Preserve provider-specific IDs. This increment makes bar selection fail closed when different provider/symbol identities use the same instrument ID in one interval. Future registry design remains open. |
| Instrument specification versioning | Record has validity interval and evidence reference but does not distinguish source publication/captured-as-known time; spec has no schedule/calendar, contract expiry, currency-code validation, price scale, volume convention or version digest. | Document design gaps. Do not fabricate defaults or silently extend schema. ADR and migration required before ingestion. |
| Price OHLC checks | Finite Decimal, low/high/open/close ordering are validated. NaN/infinity rejected. Prices need not align to tick size because tick may be unknown and rules can be source/contract specific. | Appropriate for raw normalized observation boundary; adapter may validate tick only when an effective-dated official spec is known. |
| Bar intervals and partial/final | Half-open UTC interval ordering is enforced. Final availability cannot precede interval end; partial bars are excluded from finalized selector. Contract does not model interval type, session/day boundary convention or exchange holiday calendar. | Keep current narrow semantics. Calendar-aware bar building remains unimplemented. |
| Revisions and duplicates | Selector chooses latest `(available_at, revision)`; same key but differing content fails; identical duplicate rows collapse. It lacks source revision ordering semantics and could compare revision counters from separate feeds. | Added mixed provider/source symbol rejection for same instrument and interval. Keep source-specific IDs distinct; vendor revision IDs and correction semantics still need adapter-level validation. |
| Late corrections/source availability | Selector filters on caller-provided `available_at`; it cannot verify source published that exact correction to this entitled user at that time. `recorded_at >= available_at` does not prove source availability; user may also backdate recorded_at. | Critical unresolved fail-closed integration requirement. Rights primitive is separate. Historical source-availability evidence not sufficiently established across candidate products; Gate 1 stays IN PROGRESS. Prospective replay should capture immutable receive time and never backdate later corrections. |
| Conflicting sources / symbols | Previously the selector could merge simultaneous provider records if callers reused an internal ID. This increment rejects that ambiguous mapping for an interval and tests same display symbol across distinct IDs. It cannot decide whether instruments with different symbols are economically equivalent. | Fixed additive check plus regression test. Similar exposure is a separately sourced relation, not identity. |
| Replay boundaries | UTC `as_of` selection uses inclusive availability (`available_at <= as_of`); interval end is exclusive by docs. Regression test covers exactly-at-correction and immediately-before boundary. Source trust remains external. | Retain and document. |
| Entitlements | Original records held evidence only and not permission scopes. New `data_rights.py` requires acquisition, exact provider/dataset, allowed use, evidence, approver and effective term. | Additive fail-closed primitive and regression tests. It is not a contract parser, customer entitlement service or legal review. |
| Missing/stale data | No substitution logic exists in selector; missing interval returns no bar. No freshness policy or quality score exists. | Preserve absence; add monitoring as proposed feature, not auto-fill. |
| Futures expiry/rolls | Contract records do not model expiry or roll policy; continuous series not represented. This can create look-ahead/back-adjustment issues. | Do not add generic continuous symbol now. Feature-register item F-013 requires per-contract identity and versioned roll rule. |
| Corporate actions | Equity/ETF price adjustment and point-in-time holdings not represented. | Keep outside current bar contract; F-012 proposes separate versioned corporate-action pipeline. |

## Contract decisions

1. Existing public constructors and selector result contract remain intact; no rename or broad rewrite.
2. Same-interval cross-provider reuse of an `instrument_id` is ambiguous and now raises an error; assign unique IDs to source-specific instruments.
3. Entitlement check is additive and defaults to denial. It does not claim that public documentation settles a commercial agreement.
4. Source availability cannot be validated from current object shape; caller assertions are not evidence. This is a documented gate blocker for any provider adapter/strict historical replay.
5. No unit tests can establish vendor legal rights, actual correction timestamps, exchange session calendars or market specifications. Those require primary documentation and approved signed source evidence.

## Regression tests added in this increment

- Missing/unacquired/mismatched/expired entitlement denies; explicit allowed use permits; missing evidence/approver denies.
- Same interval mapped to multiple provider/source symbols rejects; identical display symbol remains legal on separate instrument IDs.
- Revision selection is inclusive at exact availability and excludes the correction immediately before that time.

Run full tests with `python -m unittest discover -s tests -v`; record exact output in `GATES.md` after execution.
