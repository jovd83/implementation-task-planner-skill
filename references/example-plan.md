# Example Plan

This example demonstrates the expected level of specificity. Do not copy its domain details into unrelated projects.

```markdown
# Implementation Tasks: Password Reset

Source readiness: ready
Generated: 2026-05-24
First vertical slice: A user can request a reset email and receive a non-enumerating confirmation response.

## Source Artifacts

- docs/specs/password-reset.md: Product behavior and acceptance criteria.
- docs/architecture/auth.md: Token lifetime, email provider, and security constraints.
- package.json: Test and lint commands.

## Phase 1: Contract and Test Scaffold

- [ ] T001 [AC-001] Add failing API test for reset request success response
  - Skill: restassured-skill
  - Files: src/test/java/com/example/auth/PasswordResetApiTest.java
  - Depends on: None
  - Validates: AC-001, SEC-001
  - Command: mvn test -Dtest=PasswordResetApiTest

- [ ] T002 [AC-002] Add failing API test for non-enumerating unknown-email response
  - Skill: restassured-skill
  - Files: src/test/java/com/example/auth/PasswordResetApiTest.java
  - Depends on: None
  - Validates: AC-002, SEC-002
  - Command: mvn test -Dtest=PasswordResetApiTest

## Phase 2: Backend Slice

- [ ] T003 [AC-001] Add password reset token persistence model and repository
  - Skill: dr-jskill
  - Files: src/main/java/com/example/auth/PasswordResetToken.java, src/main/java/com/example/auth/PasswordResetTokenRepository.java
  - Depends on: T001
  - Validates: AC-001, ADR-003
  - Command: mvn test

- [ ] T004 [AC-001] Implement reset request endpoint with email dispatch
  - Skill: dr-jskill
  - Files: src/main/java/com/example/auth/PasswordResetController.java, src/main/java/com/example/auth/PasswordResetService.java
  - Depends on: T003
  - Validates: AC-001, AC-002
  - Command: mvn test -Dtest=PasswordResetApiTest

## Dependencies

- T003 depends on T001 because the persistence behavior should satisfy the failing API contract.
- T004 depends on T003 because it needs token persistence before dispatching reset links.

## Parallel Groups

- None in the first slice; all tasks share the reset request contract.

## Validation Plan

- `mvn test -Dtest=PasswordResetApiTest`: verifies reset request API behavior.
- `mvn test`: verifies regression safety across the module.

## Traceability Matrix

| Source | Tasks | Notes |
| --- | --- | --- |
| AC-001 | T001, T003, T004 | Reset request creates token and dispatches email. |
| AC-002 | T002, T004 | Unknown emails receive the same response shape. |
| SEC-002 | T002, T004 | Prevents account enumeration. |

## Open Questions

- None.
```
