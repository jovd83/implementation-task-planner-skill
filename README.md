# Implementation Task Planner Skill

[![Validate Skill](https://github.com/jovd83/implementation-task-planner/actions/workflows/validate.yml/badge.svg)](https://github.com/jovd83/implementation-task-planner/actions/workflows/validate.yml)
[![version](https://img.shields.io/badge/version-1.1.0-blue)](CHANGELOG.md)
[![Agent Skill](https://img.shields.io/badge/Agent%20Skill-SKILL.md-0a7ea4)](SKILL.md)
[![status](https://img.shields.io/badge/status-production--ready-brightgreen)](SKILL.md)
[![category](https://img.shields.io/badge/category-planning-0a7ea4)](SKILL.md)
[![license](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Buy Me a Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-ffdd00?style=flat&logo=buy-me-a-coffee&logoColor=black)](https://buymeacoffee.com/jovd83)

`implementation-task-planner` turns approved product and architecture artifacts into execution-ready implementation plans for AI coding agents and engineering teams.

It is designed for the planning handoff between "the work is specified" and "coding can safely begin."

## What This Skill Does

The skill produces:

- Ordered `tasks.md` implementation plans.
- Optional machine-readable `tasks.json` plans.
- Dependency-aware sequencing.
- Test-first task ordering where practical.
- Acceptance-criteria and architecture traceability.
- Safe parallelization markers.
- File targets and validation commands.
- Downstream skill-routing hints.
- Open questions separated from executable work.

## When To Use It

Use this skill when approved delivery artifacts need to become a task plan before implementation starts.

It is a good fit for:

- Turning product specs, acceptance criteria, and architecture notes into ordered engineering work.
- Creating `tasks.md` and optional `tasks.json` for a feature folder.
- Updating an existing implementation plan with new acceptance criteria while preserving unrelated tasks.
- Splitting work into dependency-aware phases with safe parallelization markers.
- Preparing handoff tasks for downstream coding, testing, API, accessibility, or release skills.

Do not use it when requirements or architecture are still being invented. Use upstream product, acceptance-criteria, or architecture skills first.

## What This Skill Does Not Do

This skill does not write implementation code, invent missing requirements, choose architecture from scratch, or silently promote planning assumptions into persistent memory.

Use upstream product, acceptance-criteria, or architecture skills before this one when the source material is not approved or specific enough.

## Install

Install from GitHub with `npx skills`:

```powershell
npx skills install jovd83/implementation-task-planner
```

For older Skills CLI versions that use `add`:

```powershell
npx skills add https://github.com/jovd83/implementation-task-planner --skill implementation-task-planner
```

You can also copy this folder into any Agent Skills-compatible skills directory.

Common locations:

```text
~/.codex/skills/implementation-task-planner
~/.agents/skills/implementation-task-planner
```

The skill follows the Agent Skills `SKILL.md` format: a folder with `SKILL.md` frontmatter and Markdown instructions, plus optional `references/`, `evals/`, and product metadata files.

## Usage

```text
Use $implementation-task-planner to turn the approved checkout spec, acceptance criteria, and architecture plan into ordered implementation tasks.
```

```text
Use $implementation-task-planner to create tasks.md and tasks.json for specs/002-saved-cart. Mark parallel work and include validation commands.
```

```text
Use $implementation-task-planner to update the existing task plan with the new accessibility acceptance criteria. Preserve unrelated tasks.
```

## Output Artifacts

Default paths:

```text
specs/001-<feature-slug>/tasks.md
specs/001-<feature-slug>/tasks.json
```

`tasks.md` is optimized for human execution and review. `tasks.json` is optional and intended for automation, dashboards, follow-on agents, or CI checks.

The JSON contract is defined in [`references/tasks-json-schema.json`](references/tasks-json-schema.json).

## Repository Structure

```text
.
|-- .github/workflows/validate.yml   # GitHub Actions validation workflow
|-- SKILL.md                         # Core skill instructions
|-- README.md                        # User-facing installation and usage docs
|-- CHANGELOG.md                     # Version history
|-- agents/openai.yaml               # Optional OpenAI/Codex UI metadata
|-- references/
|   |-- task-template.md             # Markdown task artifact template
|   |-- tasks-json-schema.json       # Machine-readable output schema
|   |-- quality-rubric.md            # Review and eval rubric
|   `-- example-plan.md              # Example output quality bar
|-- evals/
|   |-- evals.json                   # Eval scenarios and assertions
|   `-- files/                       # Eval source fixtures
|-- scripts/validate_skill.py        # Repository-local validation checks
`-- LICENSE
```

## Memory Model

The skill uses an explicit memory boundary:

- Runtime memory: temporary planning notes for the current request.
- Project-local memory: stable planning conventions saved only when the project already has an explicit place for them.
- Shared memory: out of scope for this skill. Use a separate shared-memory capability when cross-project reuse is needed.

Runtime assumptions should not become persistent project facts without source support or user confirmation.

## Optional Integrations

This repository is intentionally self-contained. Optional integrations can be layered around it:

- A skill dispatcher can use this skill for implementation-planning intents.
- A JSON-schema validator can check generated `tasks.json`.
- A shared-memory skill can preserve reusable cross-project planning conventions after explicit promotion.
- GitHub Actions can run repository validation before changes land.

These integrations are not required for the skill to work.

## Evaluation

The eval suite covers:

- A ready feature with architecture, ACs, commands, and expected files.
- A partial spec that must not trigger invented implementation details.
- A blocked request that should produce a blocker report instead of fake tasks.
- An update to an existing task plan that must preserve unrelated work.

Use [`references/quality-rubric.md`](references/quality-rubric.md) to grade generated plans.

Run the repository-local validator:

```powershell
python scripts/validate_skill.py .
```

The same validator runs in GitHub Actions through `.github/workflows/validate.yml`.

## Standards Alignment

This repository follows the public Agent Skills shape:

- `SKILL.md` at the skill root.
- Required `name` and `description` frontmatter.
- Progressive disclosure through focused `references/` files.
- Eval cases under `evals/`.
- Optional product metadata under `agents/`.

Useful references:

- [Agent Skills specification](https://agentskills.io/specification)
- [Agent Skills best practices](https://agentskills.io/skill-creation/best-practices)
- [Evaluating skill output quality](https://agentskills.io/skill-creation/evaluating-skills)

## Contributing

High-quality contributions should improve execution reliability, not just wording.

Good changes include:

- More realistic eval fixtures.
- Tighter output schema constraints.
- Better edge-case handling for partial or blocked inputs.
- Clearer skill-routing defaults.
- Examples from real implementation-planning workflows with sensitive details removed.

Avoid adding broad frameworks, autonomous self-modification, or persistent memory mechanisms directly into this skill.

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for release history. Current version: `1.1.0`.

## License

MIT. See [`LICENSE`](LICENSE).
