# Initial Instrument Specification Research

**As of:** 2026-11-17  
**Status:** Research profiles, not production mappings. No provider selected, symbol bound in application, entitlement granted, or live values captured. Product marketing names and aggregate symbols are not universal identities.

## Interpretation and confidence

The instrument domain must identify the venue/provider product—not merely display text. Evidence below establishes specific facts for the named venue or provider. Confidence rates source quality for the stated fact, not suitability or legal permission for product use. “Unspecified” fields are intentionally unresolved. Some official provider websites publish session/spec fields dynamically; confirm exact current rulebook and calendar before implementation.

## Profile A — OTC spot gold / vendor composite XAUUSD (Massive)

| Field | Finding |
|---|---|
| Canonical type | Vendor-sourced OTC FX/metal quote series (spot-like market data), not a centralized exchange contract and not proof of physical spot trade. Model as provider-specific `spot`, commodity exposure only if product semantics confirmed. |
| Provider/source | Massive reports institutional bank feeds; OTC FX has no central consolidated tape. |
| Symbol/id | Provider symbol `C:XAUUSD`; base XAU, quote USD per provider. This is not interchangeable with `XAU/USD`, `XAU-FX`, `XAUUSD` at a broker, LBMA Gold Price, or COMEX GC. |
| Quote/settlement currency | USD quote; actual market/settlement unit for the feed not confirmed from public provider data page. |
| Tick/precision | Quote timestamps and bars may have decimals; no universal minimum tick is evidenced. Preserve source precision; do not assert tradable tick. |
| Multiplier/quantity | No standardized OTC notional or multiplier; provider feed has no universal order quantity. Unknown. |
| Hours/calendar | Vendor says FX coverage continuously Sunday evening–Friday evening Eastern; vendor feed operational coverage is not an exchange calendar. Provider-specific holidays/gaps need measurement. |
| DST/interruption | REST epoch is UTC; local presentation/session labels need zone rules. Exact closure calendar, DST publication boundary, and interruption protocol by XAU feed require vendor confirmation. |
| Price/volume | Forex bars are built from bid quotes. Bar `v` repeats quote count `n`, not traded volume; `vw` is arithmetic quote-bid mean, not volume-weighted. Vendor identifies XAU feed history gaps (mostly missing July 2010–July 2013; sparse quotes later). |
| Corrections/availability | Provider describes corrections/current REST for some feeds and late-stock-bar rebroadcast for US equities; does not establish XAU-specific historical availability/revision times. Unknown. |
| Confidence/open items | High for symbol/product label and disclosed semantics; low for market representativeness, executable spread, tick, full coverage, correction availability and legal rights. Ask exact constituent bank sources, quote conditions, source time/publication time and license. |
| Official sources | [Massive forex source/gaps](https://massive.com/knowledge-base/categories/currencies); [forex bar semantics](https://massive.com/knowledge-base/article/how-are-massives-forex-bars-built-and-what-do-v-and-n-mean-on-a-forex-bar); [timezone units](https://massive.com/knowledge-base/article/what-timezone-are-massives-timestamps-in). |

## Profile B — Broker gold spot / broker-specific XAUUSD (FXCM example)

| Field | Finding |
|---|---|
| Canonical type | Broker-dealt XAU/USD spot product/reference rate. The broker page describes spot OTC pricing; actual client dealing specification depends on entity/account. |
| Provider/source | FXCM UK support page, broker dealing specification. Not exchange-wide. |
| Symbol/id | Display `XAU/USD` / XAUUSD; broker identity and legal entity must be part of internal key. |
| Quote/settlement | Quote is USD per troy ounce. Base quantity/contract in account can differ; FXCM notes account denomination affects point value. |
| Tick/precision | Source describes 0.01 point/pip increments for this product, not universal XAUUSD tick. |
| Multiplier/quantity | No general multiplier established by the cited summary; maximum number of contracts per click is a platform constraint, not contract multiplier. Ask the exact dealing specification. |
| Hours/calendar | Page sends trading hours to a separate source; holiday hours and DST subject to change. Not fully specified here. |
| Interruptions | No expiration; rollover financing described, usually triple on Wednesdays. Exact holiday/session breaks not confirmed by cited spec. |
| Price/volume | OTC derived from global OTC trading; there is no single consolidated traded volume in spot metal data. Broker spread/dealing rates apply. |
| Confidence/open items | High for product distinction and quoted unit/0.01 point; insufficient for production spec. Need exact legal entity, account class, full contract size, min/max quantity/step, schedule, closing breaks, pricing source and rights. |
| Official source | [FXCM XAU/USD specification](https://www.fxcm.com/uk/help/commodities-xau-usd-gold/). |

## Profile C — Gold CFD (IG example, broker-specific)

| Field | Finding |
|---|---|
| Canonical type | Broker-issued CFD on spot gold; separate from spot bullion, benchmark and futures. |
| Provider/source | IG product details; regional/entity variations apply. |
| Symbol/id | IG “Spot Gold” market; exact market epic/source identifier not provided on cited summary page. Do not assert universal `XAUUSD` mapping. |
| Quote/settlement | USD-denominated $1 contract value per full point in cited IG AE table; IG International table describes spot-gold contract variants of 1 oz and 100 oz. Which applies depends on product/account. |
| Tick/precision | Example normal spread 0.1 points; spread is not necessarily tick size. Minimum price increment not established by these pages. |
| Multiplier/quantity | IG page provides contract value and example one contract = 1 troy oz (specific listed regional product). Another IG product lists one contract = 100 oz. Must bind exact entity/product. |
| Hours/calendar | IG CFD dealing schedule not fully established from linked table; broker terminal specification and regional product schedule required. |
| Interruptions/DST | Unresolved; broker schedule can change for holidays and seasonal clock changes. |
| Price/volume | CFD is cash-settled exposure, not volume on an exchange. Spread and overnight financing/carry materially affect returns. |
| Confidence/open items | Medium for example-specific contract values; insufficient to choose or register a production mapping. Obtain full dated contract terms, prices/quote source, quantity step, trading hours/holiday schedule, negative-price handling and data rights. |
| Official sources | [IG AE commodity CFD details](https://www.ig.com/ae/help-and-support/articles/609647-what-are-ig-s-commodities-cfd-product-details); [IG International details](https://bts.ig.com/en/help-and-support/cfds/fees-and-charges/what-are-igs-commodities-cfd-product-details). |

## Profile D — LBMA Gold Price benchmark (distinct reference instrument)

| Field | Finding |
|---|---|
| Canonical type | Regulated benchmark/reference price; not continuously traded OTC spot or CFD. |
| Administrator/owner | ICE Benchmark Administration (administrator); LBMA says intellectual property is owned by LBMA. |
| Symbol/id | Named benchmark `LBMA Gold Price AM` / `LBMA Gold Price PM`; identifiers depend on license/vendor. |
| Quote/settlement | USD per troy ounce variants; auction for loco London unallocated gold. Not trade quantity/contract multiplier. |
| Tick/quantity | Not an execution contract; no market tick/quantity step. |
| Schedule | AM/PM auction benchmark points at London-specific times; not continuous market hours. Publication and holiday schedule must be obtained from IBA. |
| Rights | LBMA states licensing may be required for valuation/pricing, products, trading/clearing or redistribution. Public web delay is not a broad commercial grant. |
| Confidence/open items | High for benchmark distinction and license requirement; historical access, precise calendars, source publication timestamps and licensing terms need direct confirmation. |
| Official sources | [LBMA Gold Price FAQ](https://www.lbma.org.uk/prices-and-data/lbma-gold-price/lbma-gold-price); [LBMA licensing note](https://www.lbma.org.uk/?trk=article-ssr-frontend-pulse_little-text-block). |

## Profile E — COMEX Gold futures GC / Micro Gold MGC (CME)

| Field | GC | MGC |
|---|---|---|
| Canonical type | Exchange-listed future, COMEX/CME Globex; distinct expiry-specific contract | Exchange-listed future, COMEX/CME Globex; distinct expiry-specific contract |
| Symbol/identifier | Product code `GC`; each expiry-month/year is a distinct tradable contract (vendor symbology required) | Product code `MGC`; expiry-specific contract |
| Quote/settlement | USD per troy ounce; contract is physically deliverable under current rules | USD per troy ounce; smaller contract; delivery/settlement per current MGC rules must be rechecked |
| Tick/multiplier | Product page currently shows minimum tick 0.10 USD/oz and contract multiplier 100 troy oz, so $10/tick | 10 troy oz (1/10 GC); current contract-spec rule page needed to verify tick/tick value before use |
| Trading hours | CME metals products trade nearly 23 hours/day; exact GC session and maintenance intervals require current contract-spec page/calendar | Same venue calendar principle; exact MGC session confirm current page |
| Calendar/expiry | Exchange listing cycle, holiday schedule and last trade/delivery obligations must be attached by contract month; do not use generic continuous ticker as a tradable contract | Same; product contract expiry distinct |
| Volume/price | Exchange trades/volume and official settlement; venue-specific ticks, status/cancel/correct events | Same |
| Confidence/open items | High for product-size facts on cited CME page; current tick and dates need current rulebook/calendar check. Rights to use CME data remain unapproved. | High for contract size; verify full current MGC specs before registering values. |

Official references: [CME Gold product and contract sizes](https://www.cmegroup.com/markets/metals/precious/gold-futures.contractSpecs.html); [COMEX Chapter 113 rulebook](https://www.cmegroup.com/content/dam/cmegroup/market-regulation/rule-filings/2024/8/24-283_1.pdf). CME contract information may change; quote current official specifications and exchange calendar at implementation.

## Profile F — Nasdaq-100 direct index NDX

| Field | Finding |
|---|---|
| Canonical type | Calculated equity index, not a tradable stock, futures contract, or CFD. |
| Provider/identifier | Nasdaq, official overview symbol `NDX`; index currency USD. |
| Quote/settlement | Index points; no direct contract multiplier/settlement since this index value is not directly tradeable. Index variant (price/net/gross return) must be explicit. |
| Tick/precision | Index dissemination precision/rounding and frequency require GIDS field specification/license. Do not infer trading tick from display decimals. |
| Hours/calendar | Follows index calculation/dissemination schedule, dependent on constituent market schedules and official index policy. No executable futures session equivalence. |
| Corrections/availability | Historical actual vs back-tested history differentiated in overview; source availability and constituent/corporate-action restatements must be queried with Nasdaq. |
| Rights | Index data is licensed; external display/distribution/benchmark use has explicit GIDS/GDA conditions. |
| Confidence/open items | High for index identity, USD and non-financial-company description; licensing, series variant, historical revisions and exact schedule remain open. |
| Official sources | [Nasdaq NDX](https://indexes.nasdaq.com/Index/Overview/NDX); [GIDS and licensing](https://www.nasdaq.com/products/global-indexes/data/gids); [2026 policy update](https://www.nasdaqtrader.com/TraderNews.aspx?id=DN2026-5). |

## Profile G — Nasdaq-100 futures NQ and MNQ (CME)

| Field | E-mini NQ | Micro MNQ |
|---|---|---|
| Canonical type | CME-listed futures contract on Nasdaq-100 index | CME-listed futures contract on Nasdaq-100 index |
| Symbol/id | Product code `NQ` plus exact expiry contract (e.g. contract-month/year symbology) | Product code `MNQ` plus exact expiry |
| Quote/settlement | USD per Nasdaq-100 index point | USD per Nasdaq-100 index point |
| Multiplier | USD 20 × index | USD 2 × index |
| Outright minimum tick | 0.25 index points = USD 5/contract | 0.25 index points = USD 0.50/contract |
| Quantity/volume | Contracts; venue trade volume, not index constituent volume | Contracts; venue trade volume |
| Trading hours | CME Globex Sunday–Friday with daily maintenance; cited source lists 6 p.m.–5 p.m. ET (5 p.m.–4 p.m. CT), daily 5–6 p.m. ET maintenance; confirm current holiday calendar | Same equity-index venue session; confirm product-specific current specs and schedule |
| Expiry/roll | Expiry-specific contract; quarterly listing cycle and last-trade/settlement details governed by current CME rulebook. Roll series is a transformation, not an instrument. | Same |
| Negative prices / halts | Price/limit/status rules from current CME rulebook; domain permits negative finite prices; status/halt handling still unimplemented | Same |
| Confidence/open items | High for multiplier, tick and stated session from CME public specs; verify active version, holidays, event halts and expiry at use time. | High for tick value/multiplier from CME product comparison; verify active version/calendar. |

Official references: [current NQ specs](https://www.cmegroup.com/markets/equities/nasdaq/e-mini-nasdaq-100.contractSpecs.html); [CME product comparison, including MNQ](https://www.cmegroup.com/markets/equities/sp-500-and-nasdaq-100-futures.html). Underlying index points do not equal a tradable NQ/MNQ contract price series exactly; futures basis, expiry, carry and roll must be modeled.

## Profile H — Nasdaq-100 CFDs (provider-specific NAS100/US100 examples)

| Field | Finding |
|---|---|
| Canonical type | Broker-issued CFD whose reference is a Nasdaq-100 index or futures-derived quote. Each broker/entity/contract is distinct. |
| Provider/symbol | Market labels such as `NAS100`, `US100`, `USTEC` are not standardized exchange symbols. No particular provider selected or verified for implementation. |
| Quote/settlement | Broker- and account-currency dependent; CFD may be spot/undated or futures-based with different financing/roll terms. Unknown without provider spec. |
| Tick/multiplier/quantity | Unknown and provider-specific; cannot borrow NQ/MNQ tick or multiplier. |
| Hours/calendar/DST | Broker hours may extend beyond cash index hours and include daily breaks; broker's published session/holiday schedule is required. No universal calendar. |
| Price/volume | OTC broker bid/ask or broker-derived mark, not consolidated NDX or CME futures volume. |
| Confidence/open items | Low until a named regulated entity/product and dated contract specification are selected. Ask source, methodology, point value, minimum increment/size, currency, financing, expiry/roll, hours, corrections and data rights. |
| Example official-source distinction | CME explicitly describes CFDs as broker-defined and hours dependent on broker availability: [CME gold comparison](https://www.cmegroup.com/markets/metals/precious/gold-futures.contractSpecs.html). No NAS100 CFD has been asserted as a verified mapping. |

## Profile I — Invesco QQQ ETF

| Field | Finding |
|---|---|
| Canonical type | Exchange-traded fund share tracking Nasdaq-100; a security with its own market price and volume, not the index or futures. |
| Provider/venue/symbol | Invesco QQQ Trust Series 1, ticker `QQQ`, CUSIP `46090E103`, ISIN `US46090E1038`, Nasdaq/NMS listing per issuer page. |
| Quote/settlement | USD per share; one share quantity unit. Cash creation/redemption process is fund/authorized participant mechanism, not per-investor futures margin. |
| Tick/multiplier | Listing/exchange price increment varies under applicable rules and can be price-level/regulatory-specific; no product-specific tick stated on issuer page. No contract multiplier beyond shares. |
| Hours/calendar | Nasdaq/NMS cash equity trading sessions and applicable extended hours; exchange holidays/DST use US/Eastern market calendar. Confirm tape/venue and access rights from market data source. |
| Corporate actions/price | ETF distributions, splits, NAV premium/discount and holdings changes matter; issuer says fund tracks index and rebalances quarterly/reconstitutes annually. Separate point-in-time corporate action record required. |
| Data rights | Issuer product facts do not license exchange market data, index data, holdings redistribution or use of index marks. |
| Confidence/open items | High for issuer identity, listing and IDs; market-data provider coverage/terms, current tick and corporate action historical rights need confirmation. |
| Official source | [Invesco QQQ facts](https://www.invesco.com/us/en/financial-products/etfs/invesco-qqq-trust-series-1.html). |

## Design implications for the instrument contract

1. Use a new stable `instrument_id` for every provider/venue/listing/expiry product. “Same exposure” belongs in a separate relation with method/source/effective time; do not equate symbols.
2. Store original provider symbol, exchange/venue MIC where relevant, provider dataset ID, exchange product/contract month, quote/base/settlement currency, quantity denomination, tick and multiplier as effective-dated specification versions.
3. The present `InstrumentRecord` can represent multiple records by distinct `instrument_id`, provider and venue, but it lacks explicit provider dataset/instrument ID, share/contract expiry, schedule/calendar ID, spec-version digest, as-known timestamp, session zone, price scale/precision, corporate-action policy and mapping relation. Record as follow-up design gaps; do not extend until an accepted ADR and migration tests are prepared.
4. An FX/spot bar `volume` field must not be conflated with quote count. Add source-specific volume semantics before normalizing provider payloads.
5. Calendar/expiry/roll rules are versioned data, not hardcoded UTC offsets. Store IANA timezone and official holiday/session revision, then normalize event instants to UTC.
6. A source-provided correction-current bar cannot be backdated to when the original bar first appeared. Replay must preserve capture snapshots and exact correction availability evidence.

## Research limitations

- Public specs cannot establish an executed customer entitlement or vendor-specific historical revision publication time.
- Cited broker examples do not establish an approved broker, legal entity, or a globally transferable CFD convention.
- Official exchange hours may vary by contract, holiday and emergency action; calendars need an official dated source and versioned service.
- No price data was retrieved or embedded. No missing values, ticks, multipliers or schedules have been filled by inference.
