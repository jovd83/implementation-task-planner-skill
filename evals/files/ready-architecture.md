# Saved Cart Architecture

## Stack

- Frontend: Angular in `apps/web/src/app/cart`.
- Backend: Spring Boot in `services/shop/src/main/java/com/acme/shop/cart`.
- Tests: Jest for frontend unit tests, JUnit 5 for backend tests, Playwright for account-menu flows.

## Decisions

- ADR-001: The backend owns saved-cart persistence.
- ADR-002: The API contract must be updated before frontend integration.
- ADR-003: Saved carts use `saved_cart` and `saved_cart_item` tables.
- ADR-004: The restore endpoint returns unavailable-item warnings in the response body.

## API Shape

- `POST /api/saved-carts`
- `GET /api/saved-carts`
- `POST /api/saved-carts/{id}/restore`

## Expected Files

- `services/shop/src/main/resources/db/migration`
- `services/shop/src/main/java/com/acme/shop/cart`
- `services/shop/src/test/java/com/acme/shop/cart`
- `apps/web/src/app/cart`
- `apps/web/e2e`
