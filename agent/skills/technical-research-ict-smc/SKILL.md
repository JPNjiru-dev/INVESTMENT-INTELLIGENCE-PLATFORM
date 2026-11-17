# Skill — Technical Research (ICT/SMC)

## 1. Mission and responsibilities
Convert ICT/SMC concepts into explicit, versioned, testable rules and determine whether they describe data consistently. Do not presume predictive power.

## 2. Required inputs and output schema
Require `{concept_id,definition_version,instrument_id,interval,source_snapshot,session_calendar,event_time_policy,sample_window,costs,baseline}`. Output `{status,operational_definition,parameters,detected_events:[{time,fields,evidence}],denominator,false_positive_review,baseline_comparison,robustness,lineage,limitations,hypothesis_status,audit}`.

## 3. Permitted tools and data
Approved bars/ticks and calendars. Use deterministic implementations for liquidity sweeps, MSS, displacement, FVG, order blocks/breakers, OTE, premium/discount, SMT, PO3, opening range and session context.

## 4. Forbidden actions
No subjective chart mark presented as objective truth, hindsight labels, undisclosed tuning, CFD/futures/index conflation, invented setups or profitability claims.

## 5. Evidence and citation requirements
Cite data and calendar versions. Each event links exact rows and algorithm version. Separate terminology sources from chosen operational definition and list alternatives.

## 6. Deterministic versus AI responsibilities
Events and evaluation metrics are deterministic. AI can compare definitions and suggest tests, not assign unlogged labels or override evidence.

## 7. Failure handling and uncertainty
Return `definition_unresolved` if alternatives change outcomes. Skip when calendar/data missing. Invalidate evaluation if future bars or repainting pivots affect earlier events.

## 8. Cost and resource limits
One primary definition and at most two preregistered sensitivities per increment; bounded window/memory. Tick archives require separate justification and license.

## 9. Audit requirements
Store concept version, code hash, snapshot IDs, timezone/calendar, event IDs, parameter attempts, exclusions and reviewer notes.

## 10. Human approval conditions
Researcher review before “validated”; owner approval for licensed data/public claims; separate exact trade proposal approval is mandatory.

## 11. Testing and acceptance criteria
Test equality/boundary bars, sessions, DST, missing candles, simultaneous signals, repainting and replay. Require baseline comparison and untouched validation before predictive claims.
