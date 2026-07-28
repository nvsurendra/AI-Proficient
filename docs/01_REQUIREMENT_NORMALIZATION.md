# 01 - Requirement Normalization

## Raw intent
Build a URL shortener and demonstrate AI-assisted engineering execution where
the engineer remains accountable.

## Normalized engineering problem
Build a secure, testable, maintainable URL shortener API with analytics and
reliability safeguards, plus traceable engineering artifacts proving disciplined
AI usage across the SDLC.

## Clarified assumptions

1. Prototype should be runnable locally and independently evaluable.
2. Core feature set includes create, resolve, analytics, and health checks.
3. Reliability means deterministic behavior under duplicates/collisions and
   explicit failure semantics.
4. Controlled oversight means human decisions are visible in process artifacts,
   even if implementation execution is AI-assisted.

## Ambiguities identified and resolved

1. Ambiguity: "AI-assisted" depth required.
Resolution: include traceability ledger with generated/edited rationale.

2. Ambiguity: expected brownfield evidence.
Resolution: provide explicit impact analysis scenario in docs with file-level
reasoning.

3. Ambiguity: production-grade scope limits.
Resolution: deliver robust local prototype; document scale-out trade-offs.
