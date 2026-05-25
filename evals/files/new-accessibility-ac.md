# New Accessibility Acceptance Criteria

- AC-004: Keyboard-only users can trigger the export and download the CSV without losing focus context.
- AC-005: Screen reader users receive a status update when export generation starts, succeeds, or fails.

## Validation

- Add browser-level accessibility checks for the export flow.
- Run `npm run test:e2e -- export-orders`.
