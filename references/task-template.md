# Task Artifact Template

Use this template when the target repository has no established task format. Adapt headings only when the project already has stronger conventions.

```markdown
# Implementation Tasks: <feature name>

Source readiness: <ready|partial|blocked>
Generated: <YYYY-MM-DD>
First vertical slice: <one-sentence demonstrable slice>

## Source Artifacts

- <artifact path or link>: <planning role>

## Assumptions

- <assumption grounded in source material, if any>

## Phase 1: <phase name>

- [ ] T001 [AC-001] <action-oriented task title>
  - Skill: <downstream skill or native agent>
  - Files: <expected file paths, directories, or TBD>
  - Depends on: None
  - Validates: <AC, ADR, NFR, or enabling dependency>
  - Command: <validation command or TBD after bootstrap>
  - Notes: <brief implementation constraint, optional>

## Phase 2: <phase name>

- [ ] T002 [P] [AC-002] <parallel-safe task title>
  - Skill: <downstream skill or native agent>
  - Files: <expected file paths, directories, or TBD>
  - Depends on: T001
  - Validates: <AC, ADR, NFR, or enabling dependency>
  - Command: <validation command or TBD after bootstrap>

## Dependencies

- T002 depends on T001 because <specific reason>.

## Parallel Groups

- Group A: T003, T004 because they touch independent files and consume stable contract T001.

## Validation Plan

- `<command>`: <what it proves>

## Traceability Matrix

| Source | Tasks | Notes |
| --- | --- | --- |
| AC-001 | T001, T005 | <coverage note> |

## Open Questions

- <question> - blocks <task ids or "none">
```

## Task Granularity

A strong task usually:

- Produces a reviewable diff or artifact.
- Has one primary concern.
- Can be validated by a command, test, review checklist, or generated artifact.
- Avoids bundling unrelated stories or layers.

Split tasks when they cross contracts, touch unrelated file groups, or require different specialist skills.

## Parallel Marker Rules

Use `[P]` only when all are true:

- The task's dependencies are already complete or stable.
- It does not mutate the same unstable files, schema, generated code, migration, or API contract as another parallel task.
- A merge conflict would be unlikely or mechanically resolvable.
- The task can be validated independently.

Do not use `[P]` to mean "could be done later"; it means "safe to execute concurrently."
