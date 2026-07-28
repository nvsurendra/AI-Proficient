# 04 - AI-Assisted Execution Traceability

## Operating model

AI is used as an accelerator. Engineer defines constraints, validates outputs,
and owns final correctness.

## Prompt discipline template used

1. Intent: expected outcome and module boundaries.
2. Constraints: dependencies, security constraints, coding style.
3. Acceptance criteria: testable behavior.
4. Output format: code/tests/docs requested.
5. Review gate: explicit accept/edit/reject decision by engineer.

## Traceability ledger

| Task | AI Draft Role | Engineer Action | Rationale |
|---|---|---|---|
| API design | Draft endpoint set | Edited | Added deactivate/details endpoints and stricter contracts |
| Data model | Draft schema | Edited | Added indexes and creator/url hash fields for idempotency |
| Service logic | Draft create/resolve | Edited | Added collision retry and explicit domain errors |
| Tests | Draft happy-path tests | Expanded | Added conflict, throttling, and deactivate behavior |
| Docs | Draft structure | Rewritten | Mapped content directly to evaluation rubric |

## Quality gates applied

1. Contract validation by Pydantic models.
2. Runtime validation via pytest suite.
3. Security checks in design (PII minimization by IP hashing).
4. Failure-path verification (404, 409, 429, 410/expiry semantics).

## Human oversight checkpoints

1. Approve requirement normalization and assumptions.
2. Approve service-level behavior and error semantics.
3. Approve final code, tests, and risk acceptance.

## Runtime traceability artifacts

Executable workflow runs now produce machine-readable logs:

1. `prompt_log.jsonl` - stage prompts and normalized intents.
2. `decision_log.jsonl` - generated/edited/accepted decisions with rationale.
3. `stage_events.jsonl` - stage-level lifecycle states and outcomes.
4. `RUN_SUMMARY.json` - final status, changed files, and validation result.

These artifacts provide concrete evidence of disciplined AI-assisted execution
and explicit engineer ownership of approvals and release decisions.
