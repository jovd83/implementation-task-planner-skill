# Implementation Tasks: Export Orders

Source readiness: ready
First vertical slice: An admin can request a CSV export for filtered orders.

## Phase 1: Export Contract

- [ ] T001 [AC-001] Add failing API test for CSV export request
  - Skill: restassured-skill
  - Files: services/orders/src/test/java/com/acme/orders/ExportOrdersApiTest.java
  - Depends on: None
  - Validates: AC-001
  - Command: mvn test -Dtest=ExportOrdersApiTest

## Phase 2: Export Implementation

- [ ] T002 [AC-001] Implement CSV export endpoint
  - Skill: dr-jskill
  - Files: services/orders/src/main/java/com/acme/orders/ExportOrdersController.java
  - Depends on: T001
  - Validates: AC-001
  - Command: mvn test
