# 03 - Brownfield Reasoning

## Impact mapping approach

For an existing URL shortener codebase, classify changes by layer and identify
blast radius before modification.

## Example enhancement: add robust analytics

Impacted areas:

1. Data schema
- Add click metadata and indexes for query efficiency.

2. Service logic
- Track click events with privacy-preserving visitor identifiers.
- Add aggregation queries for top referrers and unique visitor counts.

3. API surface
- Extend stats response contract.
- Preserve backward compatibility on existing endpoints.

4. Reliability behavior
- Ensure write path remains bounded and deterministic on collisions/retries.

5. Tests
- Add regression tests for existing endpoint behavior.
- Add analytics-specific tests for correctness under repeated access.

## Brownfield safety checklist

1. Confirm existing endpoint compatibility.
2. Verify migration path for schema changes.
3. Validate old tests still pass before adding new tests.
4. Document any assumptions and rollback strategy.

## Executable brownfield pipeline evidence

The project now includes a runnable brownfield workflow (`run_workflow.py`) that
automates impact-first enhancement in an isolated run workspace.

Artifacts generated per brownfield run include:

1. `IMPACT_ANALYSIS.md`
2. `BEFORE_app_service.py`
3. `AFTER_app_service.py`
4. `BROWNFIELD_DIFF.patch`
5. `VALIDATION_REPORT.md`
6. `RUN_SUMMARY.json`

This makes brownfield reasoning auditable with concrete before/after code
evidence, not only static documentation.
