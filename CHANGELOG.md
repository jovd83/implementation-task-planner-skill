# Changelog

All notable changes to this skill are documented in this file.

## [1.1.0] - 2026-09-28

### Changed

- Invoke-only: `disable-model-invocation: true` for Claude Code and `allow_implicit_invocation: false` in `agents/openai.yaml` for Codex. The skill is phase 8 of `project-genesis-chain`, which the `project-genesis` agent runs; it no longer competes for automatic selection. Run it with `/implementation-task-planner` or `$implementation-task-planner`.
- `metadata` carries author and version; the validator accepts it and the other standard optional keys.

## [1.0.0] - 2026-05-25

### Added

- Published the first production-ready release of `implementation-task-planner`.
- Added README badges for validation, version, status, category, license, and Buy Me a Coffee.
- Added `npx skills` installation guidance.
- Added repository-local validation and a GitHub Actions workflow for pull request and branch validation.

### Documented

- Clarified what the skill does, when to use it, and how it fits into implementation handoff workflows.
