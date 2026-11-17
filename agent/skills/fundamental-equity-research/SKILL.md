# Skill — Fundamental Equity Research

## 1. Mission and responsibilities
Assess listed companies and ETFs from traceable filings and point-in-time fundamentals. Explain business quality, valuation assumptions, risks and failure cases without unsupported personalized advice.

## 2. Required inputs and output schema
Require `{issuer_id,security_id,exchange,currency,filing_ids,as_of,fiscal_period_policy,corporate_action_snapshot,comparison_universe,valuation_method}`. Output `{status,identity,source_facts:[{metric,value,unit,period,publication_time,source}],normalized_metrics,adjustments,scenarios,valuation_assumptions,risks,delisting_restatement_flags,confidence,limitations,audit}`.

## 3. Permitted tools and data
Official filings/regulators/issuer releases and approved licensed fundamentals. Market prices only with approved rights. Read-only research.

## 4. Forbidden actions
No future filings in historical screens, low share price as cheapness, missing statement fills, hidden restatements/delistings, unsupported recommendations or raw-data redistribution.

## 5. Evidence and citation requirements
Cite filing accession/ID, publication timestamp and retrieval time. Preserve reported vs adjusted values and currencies; identify estimates separately.

## 6. Deterministic versus AI responsibilities
Code calculates ratios, conversions, share counts and scenarios. AI summarizes disclosures with citations and review; it cannot create inputs or change formulas.

## 7. Failure handling and uncertainty
Mark unavailable/not comparable. Stop on unresolved identity, material restatement, missing share count/currency or rights. Show assumptions and ranges, not false precision.

## 8. Cost and resource limits
One filing retrieval per version, peer set capped at ten by default, no paid data without approval.

## 9. Audit requirements
Record security-master version, filing IDs, as-of cutoff, licenses, calculation version, assumptions, peer set, exclusions and reviewer.

## 10. Human approval conditions
Analyst reviews extraction/adjustments; owner/legal approves licenses; human review precedes user-facing conclusions; trades require separate explicit approval.

## 11. Testing and acceptance criteria
Test restatements, splits, currency, delisted companies, fiscal-period differences, missing fields and non-comparable metrics. Historical screens use only information available by cutoff.
