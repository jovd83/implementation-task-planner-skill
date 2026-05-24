---
name: implementation-task-planner-skill
description: Convert approved product specs, acceptance criteria, and architecture plans into executable implementation tasks. Use when a project needs ordered, dependency-aware task breakdowns with test-first sequencing, file targets, validation commands, parallel markers, traceability, and skill-routing hints before coding begins.
metadata:
  dispatcher-category: planning
  dispatcher-layer: information
  dispatcher-lifecycle: draft
  dispatcher-risk: medium
  dispatcher-writes-files: true
  dispatcher-capabilities: task-breakdown, dependency-planning, test-first-tasking, implementation-planning, traceability
  dispatcher-accepted-intents: generate_implementation_tasks, plan_development_tasks, create_task_breakdown
  dispatcher-input-artifacts: product_spec, acceptance_criteria, architecture_plan, project_constitution
  dispatcher-output-artifacts: tasks_markdown, tasks_json, dependency_map, validation_plan, skill_route_map
  dispatcher-stack-tags: planning, implementation, sdlc, traceability
---

# Implementation Task Planner Skill

Use this skill when a project has enough approved specification and architecture detail to create an executable engineering plan.

This skill creates tasks. It does not write implementation code.

## Outcomes

- Produce ordered implementation tasks grouped by story or vertical slice.
- Preserve traceability to acceptance criteria and architecture decisions.
- Put tests before implementation when practical.
- Identify dependencies and safe parallel work.
- Include file targets and validation commands when known.
- Include skill-routing hints for downstream execution.

## Do Not Use This Skill For

- Creating product requirements from scratch. Use `backlog-story-generator`.
- Drafting acceptance criteria. Use `acceptance-criteria-designer`.
- Choosing architecture. Use `greenfield-architecture-planner`.
- Implementing tasks.

## Workflow

0. Log telemetry if available:

```bash
%USERPROFILE%\.agents\skills\skill-dispatcher\log-dispatch.cmd --skill implementation-task-planner-skill --intent generate_implementation_tasks --model <model_name> --reason <reason>
```

1. Read product spec, acceptance criteria, architecture plan, and constitution.
2. Identify the first independently demonstrable vertical slice.
3. Build a dependency graph:
   - setup and scaffold tasks
   - data model tasks
   - contract tasks
   - business logic tasks
   - UI tasks
   - test tasks
   - documentation and release tasks
4. Order tasks so blocking contracts and tests appear before dependent implementation.
5. Mark safe parallel tasks with `[P]`.
6. Include expected files or directories for each task when the architecture plan supports it.
7. Include validation commands when known, otherwise state `TBD after bootstrap`.
8. Include downstream skill hints.
9. Save `tasks.md` and optionally `tasks.json` when the user or chain requested artifacts.

## Default Output Paths

Prefer:

```text
specs/001-initial-product/tasks.md
specs/001-initial-product/tasks.json
```

Reuse an existing feature folder if the project already has one.

## Markdown Task Format

```markdown
## Phase <N>: <phase name>

- [ ] T001 [AC-001] <task description>
  - Skill: <recommended skill or native agent>
  - Files: <expected file paths or TBD>
  - Validates: <acceptance criteria or architecture decision>
  - Command: <validation command or TBD after bootstrap>
```

Use `[P]` immediately after the task ID for tasks that can run in parallel:

```markdown
- [ ] T004 [P] [AC-003] Create frontend route skeleton
```

## JSON Contract

When creating `tasks.json`, include:

- `schema_version`
- `project`
- `source_artifacts`
- `tasks`
- `dependencies`
- `parallel_groups`
- `validation_commands`
- `skill_routes`
- `open_questions`

## Skill Routing Hints

Typical mappings:

| Task Shape | Skill Hint |
| --- | --- |
| Angular component or service | `angular-developer` |
| Spring Boot implementation | `dr-jskill` or native Java agent |
| MCP server | `mcp-builder` |
| OpenAPI contract | `openapi-spec-generation` |
| unit tests | `stack-aware-unit-testing-skill` or `junit5-skill` |
| API tests | `api-contract-sentinel` or `restassured-skill` |
| browser tests | `playwright-skill` or `cypress-skill` |
| responsive tests | `responsive-testing` |
| accessibility review | `a11y-audit-agent-skill` |
| release prep | `release-manager-skill` |

## Guardrails

- Do not invent file paths that contradict the architecture plan.
- Do not hide unresolved decisions inside tasks.
- Do not create giant tasks that mix unrelated user stories.
- Do not mark tasks parallel if they touch the same unstable contract or depend on unfinished schema.
- Do not claim validation commands exist before repository bootstrap unless they are known.

## Final Response

Report:

- task files created or updated
- first vertical slice
- task count by phase
- parallel groups
- validation commands
- unresolved blockers
