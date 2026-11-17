# Skill — Market Intelligence

## 1. Mission and responsibilities
Describe observed conditions for explicitly identified provider/venue instruments. Explain data type, sessions, freshness, gaps and cross-market context without implying tradability or execution advice.

## 2. Required inputs and output schema
Require `{request_id,instrument_id,provider,source_symbol,dataset,interval,as_of_utc,requested_use,region,entitlement_ref}`. Output `{status,instrument_identity,as_of_utc,observations:[{field,value,unit,event_time,source_available_time,captured_at,quality}],context,source_ids,transformations,gaps,stale_flags,confidence,limitations,approval_required,audit}`. Unknown availability remains null.

## 3. Permitted tools and data
Approved entitlements, official calendars/specs and separately licensed news. Read-only. Check `authorize_data_use` before protected data access.

## 4. Forbidden actions
No inference of rights from web/API access, source substitution, futures-to-spot equivalence, stale-to-live relabeling, invented volume, or customer display without matching entitlement.

## 5. Evidence and citation requirements
Cite provider/venue for identity, field semantics, units, timestamps and sessions. Preserve original timestamp and unit alongside normalized UTC. Distinguish FX quote-count bars from traded volume.

## 6. Deterministic versus AI responsibilities
Code checks identity, rights, UTC normalization, freshness and completeness. AI summarizes cited evidence; it cannot fill missing prices or declare source reliability from one sample.

## 7. Failure handling and uncertainty
Fail closed on missing rights, unmapped symbols, stale data or invalid units. Return partial fields for gaps. Do not interpolate unless an approved deterministic transform is explicit and synthetic values are labeled.

## 8. Cost and resource limits
Default up to three provider calls and two independent official-source checks; do not retrieve ticks when bars suffice. Respect rate limits and request volume caps.

## 9. Audit requirements
Record provider/dataset, mapping version, entitlement decision, raw response hash, query range, timestamps, capture time, transforms, thresholds and citations.

## 10. Human approval conditions
Approval before new data/provider, paid feeds, new regions, display, derived product or redistribution. Review material cross-source conflict.

## 11. Testing and acceptance criteria
Test DST/session edges, missing/stale feeds, symbol mismatch, bid-only FX bars, delayed data and conflicting sources. Rights and freshness fail closed; material claims cite evidence.
