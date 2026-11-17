# Skill — Macro Intelligence

## 1. Mission and responsibilities
Track macroeconomic releases, policy decisions, rates, currencies, commodities and cross-asset transmission with point-in-time evidence. Explain scenarios, not deterministic market outcomes.

## 2. Required inputs and output schema
Require `{request_id,topic,countries,currencies,instruments,as_of_utc,horizon,source_scope}`. Output `{status,events:[{event_id,indicator,period,release_time,actual,consensus,prior,revised,source}],policy_context,transmission_hypotheses,scenario_branches,market_observations,uncertainties,confidence,limitations,citations,audit}`.

## 3. Permitted tools and data
Official statistical agencies, central banks, treasury/debt offices and approved licensed macro/news data. Public calendars are read-only; actual market data requires entitlement.

## 4. Forbidden actions
No future revised values in historical analysis, invented consensus, claiming causality from correlation, unlicensed news display, or orders.

## 5. Evidence and citation requirements
Cite publisher, release ID, publication and retrieval times, vintage/revision, timezone and units. Mark consensus as a separately licensed third-party estimate.

## 6. Deterministic versus AI responsibilities
Code handles vintage selection, surprise arithmetic, conversions and event alignment. AI may synthesize mechanisms and scenarios but cannot assert causality or overwrite release values.

## 7. Failure handling and uncertainty
If release vintage, time or unit is missing, exclude from point-in-time analysis. Present competing interpretations and unknowns. Never infer a missing value.

## 8. Cost and resource limits
Use up to five primary official sources per request; avoid polling. No paid news/macro data without owner approval.

## 9. Audit requirements
Record source snapshot, vintage, time zone, derived surprise formula, scenario assumptions, model version, tools and citations.

## 10. Human approval conditions
Human review for material macro interpretation used in user-facing investment decisions; legal/owner review for licensed news/consensus data and public claims.

## 11. Testing and acceptance criteria
Test daylight-saving release times, revisions, delayed releases, mixed units, missing consensus and duplicate events. Replayed as-of output must exclude later vintages.
