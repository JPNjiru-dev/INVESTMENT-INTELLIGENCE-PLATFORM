# Instrument Model — Initial Contract

## Purpose

Represent provider/venue-specific instruments without confusing their market type or assuming that a display symbol uniquely identifies an instrument. The initial Python domain module uses only the standard library and stores no prices.

## Types

InstrumentKind distinguishes spot, CFD, future, equity, ETF, and index. AssetClass captures the underlying category, including crypto; crypto exposure may be spot, CFD, future, ETF, or another supported kind. A Nasdaq-100 CFD must remain a CFD with index exposure; a direct index value, future, ETF, and broker CFD are separate records even when their labels resemble one another. XAUUSD is ambiguous until its provider, instrument type, conventions, and evidence are supplied.

## Identity, time, and evidence

An internal stable instrument_id identifies the product record. Source provider plus symbol and optional venue preserve source identity. Validity timestamps are UTC instants and intervals are half-open by convention (valid_from inclusive, valid_to exclusive). EvidenceReference stores a source URI, publisher, and retrieval/publication timestamps.

## Specifications

Price tick, quantity step, contract multiplier, settlement currency, and quantity unit are optional until independently evidenced. Numeric conventions must use Decimal; binary floats are rejected. A citation records provenance; it does not establish independent correctness or data rights. The model deliberately has no boolean that can incorrectly imply a source or specification has been fully verified.

## Boundaries and next work

This module does not ingest data, validate exchange entitlements, resolve corporate actions, convert currencies, calculate risk, or assert concrete XAUUSD/NAS100 specifications. Next, define point-in-time market observations and source entitlement contracts with an approved data source before any integration.
