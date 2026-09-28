---
name: implementation-task-planner
description: Turn approved product requirements, acceptance criteria, architecture plans, and repository context into executable implementation task plans. Use when a project needs test-first, dependency-aware tasks with traceability, file targets, validation commands, parallel work markers, open questions, and downstream skill-routing before coding starts.
---

# Implementation Task Planner Skill

Use this skill to convert approved delivery artifacts into an execution-ready task plan. The skill plans implementation work; it does not implement the code.

## Core Outcomes

Produce a plan that enables another agent or engineer to start safely:

- Ordered tasks grouped by phase, story, or vertical slice.
- Traceability from each task to acceptance criteria, architecture decisions, risks, and source artifacts.
- Test-first sequencing where a meaningful test can be written before implementation.
- Explicit dependencies and `[P]` markers for work that can proceed in parallel.
- Expected file targets when they can be inferred from the architecture or repository.
- Validation commands, or `TBD after bootstrap` when commands are genuinely unknown.
- Downstream skill-routing hints for specialized execution.
- Open questions and blockers separated from executable tasks.

## Inputs

Read the highest-confidence artifacts available, in this order:

1. Approved product spec, PRD, issue, epic, or user stories.
2. Acceptance criteria, examples, business rules, and non-functional requirements.
3. Architecture plan, API contract, data model, ADRs, diagrams, or technical design.
4. Project constitution, coding standards, repo conventions, and existing task templates.
5. Repository structure and test commands if the project already exists.

If key artifacts are missing, create a planning skeleton only when useful. Do not fabricate acceptance criteria, architecture decisions, file paths, or commands.

## Readiness Gate

Before writing tasks, classify the source state:

- `ready`: Requirements and architecture are specific enough to produce executable tasks.
- `partial`: Useful tasks can be created, but at least one area needs confirmation.
- `blocked`: The task plan would be mostly invention.

For `partial`, write the executable subset and list open questions. For `blocked`, produce a concise blocker report instead of a fake task list.

## Workflow

1. Inventory source artifacts and record their identifiers, paths, or links.
2. Extract acceptance criteria, architecture decisions, constraints, and validation signals.
3. Identify the first independently demonstrable vertical slice.
4. Build a dependency graph across setup, contracts, data, domain logic, UI, tests, operations, docs, and release work.
5. Sequence tasks so contracts, scaffolding, and tests appear before dependent implementation when practical.
6. Split work into small tasks that are independently reviewable and normally touch one concern.
7. Add `[P]` only when tasks do not depend on each other and do not modify the same unstable contract, schema, migration, or shared surface.
8. Attach traceability, file targets, validation commands, and skill-routing hints to each task.
9. Validate the plan against the quality checklist.
10. Write `tasks.md`; also write `tasks.json` when the user, workflow, or automation chain requests machine-readable output.

## Default Artifact Paths

Prefer an existing feature folder when present. Otherwise use:

```text
specs/001-<feature-slug>/tasks.md
specs/001-<feature-slug>/tasks.json
```

Do not overwrite unrelated planning files. If a target file already exists, update it only when it is clearly the current feature plan or the user requested replacement.

## Task Design Rules

- Use stable task IDs: `T001`, `T002`, `T003`.
- Use acceptance-criteria IDs when available: `[AC-001]`, `[AC-002]`. If no IDs exist, create local labels and map them in the traceability section.
- Prefer vertical slices over architecture-layer batches when dependencies allow it.
- Make every task action-oriented and verifiable.
- Include a failing-test or test-update task before implementation when the behavior is testable.
- Keep infrastructure and bootstrap tasks separate from feature behavior.
- Put migrations, API contracts, generated clients, and shared schema changes before their consumers.
- Include documentation and release tasks only when they are required by the source artifacts or project convention.
- Use `TBD after bootstrap` only for commands that cannot be known until the project is initialized.

## Markdown Output Contract

Use this structure unless the repository already has a stronger task format:

```markdown
# Implementation Tasks: <feature name>

Source readiness: <ready|partial|blocked>
First vertical slice: <one sentence>

## Source Artifacts

- <artifact id or path>: <role in planning>

## Phase 1: <phase name>

- [ ] T001 [AC-001] Write failing contract test for <behavior>
  - Skill: <skill name or native agent>
  - Files: <expected files, directories, or TBD>
  - Depends on: None
  - Validates: <AC, ADR, NFR, or source decision>
  - Command: <validation command or TBD after bootstrap>

- [ ] T002 [P] [AC-002] Create <parallel-safe unit of work>
  - Skill: <skill name or native agent>
  - Files: <expected files, directories, or TBD>
  - Depends on: T001
  - Validates: <AC, ADR, NFR, or source decision>
  - Command: <validation command or TBD after bootstrap>

## Dependencies

- T002 depends on T001 because <reason>.

## Parallel Groups

- Group A: T004, T005 because <reason>.

## Validation Plan

- <command>: <what it proves>

## Open Questions

- <question> - blocks <task ids or "none">
```

Load `references/task-template.md` when the user needs a fuller template or the project lacks an existing format.

## JSON Output Contract

When creating `tasks.json`, conform to `references/tasks-json-schema.json`. Include at minimum:

- `schema_version`
- `project`
- `readiness`
- `source_artifacts`
- `tasks`
- `dependencies`
- `parallel_groups`
- `validation_commands`
- `skill_routes`
- `open_questions`

Every JSON task must have an ID, title, status, phase, traceability, dependencies, parallel flag, expected files, validation command, and skill route.

## Skill Routing Defaults

Use the repository stack and task shape to choose downstream skill hints. If no specialized skill clearly applies, use `native agent`.

| Task shape | Skill hint |
| --- | --- |
| Angular component, route, form, or service | `angular-developer` |
| Java or Spring Boot implementation | `dr-jskill` or `junit5-skill` for tests |
| OpenAPI contract or generated client | `openapi-spec-generation` |
| MCP server or tool integration | `mcp-builder` |
| Unit or component tests | `stack-aware-unit-testing-skill` |
| REST API tests | `restassured-skill` or `api-contract-sentinel` |
| Browser workflow tests | `playwright-skill` or `cypress-skill` |
| Responsive UI validation | `responsive-testing` |
| Accessibility checks | `a11y-audit-agent-skill` |
| Release notes, versioning, readiness | `release-manager-skill` |

## Memory Model

Use memory deliberately and keep scopes separate:

- Runtime memory: Maintain temporary reasoning, dependency notes, and source interpretations only for the current task-planning turn.
- Project or skill memory: Persist stable project-local planning conventions only when the repository already has an explicit place for them, such as `docs/`, `specs/`, or a project task template.
- Shared memory: Do not write cross-agent memory from this skill. If the user asks to preserve reusable planning conventions across projects, record them in the agent's own memory (for example CLAUDE.md or AGENTS.md) after explicit confirmation.

Never promote runtime assumptions into persistent project artifacts without labeling them as assumptions or confirming them through source material.

## Guardrails

- Do not create product requirements, acceptance criteria, architecture decisions, or technical designs from scratch. Route those requests to the appropriate upstream planning skill.
- Do not hide unresolved decisions inside executable tasks.
- Do not invent files that contradict the architecture, repo conventions, or generated code layout.
- Do not mark tasks parallel when they depend on the same unfinalized contract, schema, migration, generated client, or shared state.
- Do not create giant tasks that mix unrelated user stories, layers, or review concerns.
- Do not claim a validation command exists unless it is present in the repo or directly inferable from known tooling.
- Do not overwrite user-authored planning artifacts without clear intent.
- Do not add autonomous self-improvement, self-modification, or memory-promotion mechanisms.

## Quality Checklist

Before finalizing, verify:

- Every task has one clear owner agent or skill route.
- Every implementation task traces to at least one source requirement, AC, ADR, NFR, or explicit enabling dependency.
- Each dependency is necessary and explained.
- Parallel groups are safe by file ownership and contract stability.
- Test tasks precede implementation where practical.
- File targets and commands are grounded in the repo or clearly marked unknown.
- Open questions are separated and identify whether they block execution.
- The first vertical slice can be demonstrated independently.

Load `references/quality-rubric.md` for eval work, quality review, or stricter grading.

## Final Response

Report only the planning result:

- Task files created or updated.
- Readiness classification.
- First vertical slice.
- Task count by phase.
- Parallel groups.
- Validation commands.
- Blocking open questions.

Keep the final response concise. Do not restate the whole task plan unless the user asks.
