# 06 - Validation and Risk Control

## Validation strategy

1. API contract tests
- Validate create/resolve/stats/deactivate/health semantics.

2. Reliability tests
- Verify idempotent create behavior.
- Verify alias collision conflict behavior.
- Verify creation burst throttling behavior.

3. Analytics tests
- Verify click tracking impacts stats endpoint.

4. Runtime validation
- Execute full pytest suite.

## Risk register

1. Single-instance in-memory rate limiter
- Risk: limits do not coordinate across replicas.
- Mitigation: migrate limiter state to Redis.

2. SQLite write throughput constraints
- Risk: high concurrency bottlenecks.
- Mitigation: move to managed relational store and tune pooling.

3. Open redirect safety
- Risk: shortened links can target malicious destinations.
- Mitigation: add domain allow-listing/reputation checks.

4. Unlimited analytics retention
- Risk: unbounded click table growth.
- Mitigation: retention policy and archival jobs.

## Guardrails

1. Input schema validation for URL and alias constraints.
2. Explicit HTTP error semantics for known failure modes.
3. Minimal PII handling by hashing client IP before persistence.
4. Test gate required before release acceptance.
