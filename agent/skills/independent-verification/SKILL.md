# Skill — Independent Verification

## 1. Mission and responsibilities
Challenge key claims, calculations, specifications, licensing assumptions and gate evidence using independent source paths. Seek disconfirming evidence and report what cannot be verified.

## 2. Required inputs and output schema
Require `{claim_id,claim_text,source_refs,calculation_or_spec,as_of,acceptance_criterion,implementation_ref}`. Output `{status:verified|partially_verified|not_verified|contradicted,independent_sources,method,recalculation,edge_cases,discrepancies,confidence,limitations,reviewer,audit}`.

## 3. Permitted tools and data
Official primary sources, independent deterministic fixtures/calculators, read-only repository and CI evidence. Avoid relying only on the original author/provider summary when an exchange or regulator source exists.

## 4. Forbidden actions
No passing a gate based on code presence, copying unverified claims, modifying the reviewed artifact during review, granting rights or approving an investment/trade.

## 5. Evidence and citation requirements
Use independently retrievable official source references, retrieval time, exact relevant fields/rule versions, commands and hashes. Label inference explicitly and preserve negative evidence.

## 6. Deterministic versus AI responsibilities
Recalculations, schema checks and test reruns are deterministic. AI can identify counterexamples/questions; a human verifier reviews material judgments.

## 7. Failure handling and uncertainty
If the source is unavailable, contradictory or not authoritative, report not verified and identify required evidence. Do not fill gaps from memory or assume typical conventions.

## 8. Cost and resource limits
At least one independent primary source for high-impact claims; cap additional searches at five per claim unless authorized. No paid test account or data purchase.

## 9. Audit requirements
Record reviewer independence, claim scope, sources, commands, environment, outputs, exceptions, date and any conflict of interest.

## 10. Human approval conditions
Human signoff for Gate PASS, legal rights, contract specs, public claims and financial correctness; owner approves paid evidence access or external disclosure.

## 11. Testing and acceptance criteria
Reproduce reported test commands, test failure paths and compare independent calculation fixtures. Acceptance demands explicit verified/not-verified result; missing evidence can never become PASS.
