# Saved Cart Product Spec

## Goal

Allow signed-in shoppers to save a cart and restore it later from the account menu.

## Acceptance Criteria

- AC-001: A signed-in shopper can save the current cart with a user-provided name.
- AC-002: A signed-in shopper can view saved carts sorted by most recently updated.
- AC-003: A signed-in shopper can restore a saved cart without losing unavailable-item warnings.

## Non-Functional Requirements

- NFR-001: Save and restore requests must complete within 500 ms at p95 for carts with 100 line items.
- NFR-002: Saved carts must be scoped to the authenticated user.

## Validation Commands

- `npm test`
- `npm run test:e2e`
