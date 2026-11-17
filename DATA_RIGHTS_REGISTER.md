# Data Rights Register

No market, fundamental, news, company filing, or alternative data provider has been selected or connected. Public documentation has been assessed for market-data candidates as of 2026-11-17; this research is not an executed agreement, approval, or entitlement.

| Source | Data/instruments | Acquisition | Storage/retention | Display/derived use | Redistribution | Cost | Approval/evidence | Status |
|---|---|---|---|---|---|---|---|---|
| None | — | — | — | — | — | — | — | No ingestion permitted |

## Provider assessment pointers (not approvals)

See [`docs/research/MARKET_DATA_PROVIDER_ASSESSMENT.md`](docs/research/MARKET_DATA_PROVIDER_ASSESSMENT.md) for candidate-specific official sources and the current unknowns. The following rows are research findings only; all rights remain **NOT APPROVED** until the owner obtains and reviews exact current terms, exchange agreements, plan/order forms, regions, customer types, and intended uses.

| Candidate/source | Candidate scope | Acquired | Internal | Display | Derived analysis | Redistribution | Expiry/entitlement state | Known constraints / owner follow-up | Status |
|---|---|---:|---:|---:|---:|---:|---|---|---|
| Databento + underlying venue | CME/CBOT/NYMEX/COMEX futures, including NQ/MNQ and GC/MGC; historical and live | No | No | No | No | No | None | Dataset-specific publisher restrictions; commercial live subscriber classification and venue license may be required. Confirm AI/non-display use, retention, redistribution and exact dataset price/regions in signed terms. | Research only |
| Twelve Data | Global EOD equities/ETFs and selected FX/crypto/commodities, with plan-specific intraday/live coverage | No | No | No | No | No | None | Individual plans are personal/internal; commercial rights depend on business plan, exchanges, regions and specific agreement; redistribution generally separately contracted. Obtain product-specific rights and intraday/tick coverage confirmation. | Research only |
| Massive | US equities/ETFs, indices, futures, FX (including vendor composite XAUUSD), crypto | No | No | No | No | No | None | Individual and business terms differ; exchange pass-through restrictions, dataset/history and user entitlement apply. Do not infer commercial rights from API access; confirm source-specific terms and corrections/availability before use. | Research only |
| Nasdaq GIDS | Nasdaq index values and constituents, including NDX | No | No | No | No | No | None | External redistribution requires GDA/service licensing; delayed data no longer available to new clients since 2026-09-01; index benchmarking/product use requires appropriate license. Pricing requires sales quote. | Research only |
| Coinbase / Kraken direct venue APIs | Venue-specific spot crypto trades/quotes/candles | No | No | No | No | No | None | API documentation does not establish platform-product licensing. Coinbase terms prohibit external display/redistribution and derived works absent prior written consent. Confirm commercial product, storage and derived-use rights from each venue. | Research only |
| CME Group direct | CME futures, index/cash products and derived works | No | No | No | No | No | None | CME license categories and fees are purpose-specific; non-display, derived-data, distribution and AI/ML restrictions require direct review. Public personal market-data pages are not a commercial license. | Research only |

## Enforcement boundary

`src/project_codename/data_rights.py` defines the future administrative boundary: explicit acquisition, provider/dataset, allowed uses, effective period, evidence reference and approver; missing or expired entries deny use. The current register has no active entitlement rows. Customer account/product-region authorization must be intersected with provider rights before data are displayed or used. Successful downloads, free tiers, public web pages, synthetic fixtures, or derived calculations do not grant permissions.

Before ingestion or customer display, capture terms/version, user scope, entitlements, historical depth, corrections, retention, display, derived data, redistribution, attribution, geographic restrictions, cost, and reviewer. Stop if terms are ambiguous.
