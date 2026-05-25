# Quality Rubric

Use this rubric to review generated `tasks.md` and `tasks.json` artifacts, build eval assertions, or compare planner versions.

## Scoring

Score each dimension from 0 to 3:

- `0`: Missing or actively misleading.
- `1`: Present but weak, vague, or hard to execute.
- `2`: Solid and usable with minor gaps.
- `3`: Excellent, precise, and grounded in source material.

## Dimensions

| Dimension | 3-point standard |
| --- | --- |
| Source grounding | Tasks are derived from named specs, ACs, architecture decisions, repo conventions, or explicit assumptions. |
| Readiness handling | The plan classifies `ready`, `partial`, or `blocked` and responds appropriately. |
| Task granularity | Tasks are small, action-oriented, reviewable, and avoid unrelated concerns. |
| Dependency quality | Dependencies are necessary, directional, and explained. |
| Test-first sequencing | Tests or validation updates precede implementation where practical. |
| Parallel safety | `[P]` appears only on work that is truly safe to run concurrently. |
| Traceability | Every task maps to ACs, decisions, NFRs, risks, or enabling dependencies. |
| File targeting | File paths are grounded in architecture or repo conventions, with unknowns clearly marked. |
| Validation commands | Commands are real, inferable, or explicitly marked `TBD after bootstrap`. |
| Skill routing | Downstream skill hints are useful and not overfit to unavailable tools. |
| Open questions | Questions are separated from tasks and identify whether they block execution. |
| Machine readability | JSON output, when requested, follows the schema and matches the Markdown plan. |

## Pass Criteria

A plan is publishable when:

- No dimension scores `0`.
- Source grounding, readiness handling, dependency quality, and traceability each score at least `2`.
- Any `[P]` task has a clear safety rationale.
- There are no invented requirements, file paths, commands, or architecture decisions.

## Common Failure Modes

- Creating generic "implement backend" tasks that cannot be reviewed.
- Treating open questions as if they were approved requirements.
- Grouping work by technology layer even when a vertical slice would reduce risk.
- Marking frontend and backend tasks parallel while both depend on an unsettled API contract.
- Claiming `npm test`, `mvn test`, or CI commands exist without checking the repo.
- Omitting negative, edge, accessibility, performance, security, or migration work when required by the source artifacts.

## Evaluation Notes

For evals, compare output with and without this skill. Look for improvements in:

- Lower invention rate.
- More specific dependencies.
- Better first vertical slice.
- More actionable validation plan.
- Clearer handling of blocked or partial specs.
