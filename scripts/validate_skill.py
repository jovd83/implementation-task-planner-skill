#!/usr/bin/env python3
"""Repository-local validation for implementation-task-planner."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


EXPECTED_NAME = "implementation-task-planner"
EXPECTED_VERSION = "1.0.0"
EXPECTED_REPOSITORY = "jovd83/implementation-task-planner-skill"

REQUIRED_FILES = [
    "SKILL.md",
    "README.md",
    "CHANGELOG.md",
    "LICENSE",
    "agents/openai.yaml",
    "evals/evals.json",
    "references/task-template.md",
    "references/tasks-json-schema.json",
    "references/quality-rubric.md",
    "references/example-plan.md",
    ".github/workflows/validate.yml",
]

REQUIRED_SKILL_SECTIONS = [
    "## Core Outcomes",
    "## Inputs",
    "## Readiness Gate",
    "## Workflow",
    "## Markdown Output Contract",
    "## JSON Output Contract",
    "## Skill Routing Defaults",
    "## Quality Checklist",
]

REQUIRED_README_SNIPPETS = [
    "actions/workflows/validate.yml/badge.svg",
    f"version-{EXPECTED_VERSION}-blue",
    "Agent%20Skill",
    "status-production--ready",
    "category-planning",
    "license-MIT-green",
    "Buy%20Me%20a%20Coffee",
    "## What This Skill Does",
    "## When To Use It",
    f"npx skills install {EXPECTED_REPOSITORY}",
    "python scripts/validate_skill.py .",
    "## Changelog",
]


def fail(message: str) -> str:
    return f"FAIL: {message}"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def load_json(path: Path):
    try:
        return json.loads(read_text(path))
    except json.JSONDecodeError as exc:
        raise ValueError(f"{path}: invalid JSON: {exc}") from exc


def parse_frontmatter(text: str) -> tuple[dict[str, str], str | None]:
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        return {}, "SKILL.md must start with YAML frontmatter"

    try:
        end = lines[1:].index("---") + 1
    except ValueError:
        return {}, "SKILL.md frontmatter must close with ---"

    metadata: dict[str, str] = {}
    for line in lines[1:end]:
        if not line.strip():
            continue
        match = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*):\s*(.*)$", line)
        if not match:
            return {}, f"invalid frontmatter line: {line}"
        key, value = match.groups()
        metadata[key] = value.strip().strip('"')

    return metadata, None


def validate_required_files(root: Path) -> list[str]:
    return [fail(f"missing required file: {path}") for path in REQUIRED_FILES if not (root / path).exists()]


def validate_skill_md(root: Path) -> list[str]:
    errors: list[str] = []
    text = read_text(root / "SKILL.md")
    metadata, error = parse_frontmatter(text)
    if error:
        return [fail(error)]

    keys = set(metadata)
    if keys != {"name", "description"}:
        errors.append(fail("SKILL.md frontmatter must contain only name and description"))

    name = metadata.get("name", "")
    description = metadata.get("description", "")
    if name != EXPECTED_NAME:
        errors.append(fail(f"SKILL.md name must be {EXPECTED_NAME}"))
    if not re.fullmatch(r"[a-z0-9-]{1,64}", name):
        errors.append(fail("SKILL.md name must be lowercase hyphen-case"))
    if len(description) < 80:
        errors.append(fail("SKILL.md description should describe triggers and scope"))
    if "<" in description or ">" in description:
        errors.append(fail("SKILL.md description must not contain angle brackets"))

    for section in REQUIRED_SKILL_SECTIONS:
        if section not in text:
            errors.append(fail(f"SKILL.md missing section: {section}"))

    return errors


def validate_readme(root: Path) -> list[str]:
    text = read_text(root / "README.md")
    return [fail(f"README.md missing required content: {snippet}") for snippet in REQUIRED_README_SNIPPETS if snippet not in text]


def validate_changelog(root: Path) -> list[str]:
    text = read_text(root / "CHANGELOG.md")
    required = [
        "# Changelog",
        f"## [{EXPECTED_VERSION}] - 2026-05-25",
        "GitHub Actions",
    ]
    return [fail(f"CHANGELOG.md missing required content: {snippet}") for snippet in required if snippet not in text]


def validate_openai_yaml(root: Path) -> list[str]:
    text = read_text(root / "agents" / "openai.yaml")
    required = [
        "interface:",
        'display_name: "Implementation Task Planner"',
        "short_description:",
        'default_prompt: "Use $implementation-task-planner',
        "allow_implicit_invocation: true",
    ]
    return [fail(f"agents/openai.yaml missing required content: {snippet}") for snippet in required if snippet not in text]


def validate_evals(root: Path) -> list[str]:
    errors: list[str] = []
    try:
        payload = load_json(root / "evals" / "evals.json")
    except ValueError as exc:
        return [fail(str(exc))]

    if payload.get("skill_name") != EXPECTED_NAME:
        errors.append(fail(f"evals/evals.json skill_name must be {EXPECTED_NAME}"))

    cases = payload.get("evals")
    if not isinstance(cases, list) or len(cases) < 4:
        return errors + [fail("evals/evals.json must contain at least 4 eval cases")]

    seen_ids: set[str] = set()
    for index, case in enumerate(cases, start=1):
        if not isinstance(case, dict):
            errors.append(fail(f"eval case {index} must be an object"))
            continue
        case_id = str(case.get("id", "")).strip()
        if not case_id:
            errors.append(fail(f"eval case {index} missing id"))
        elif case_id in seen_ids:
            errors.append(fail(f"duplicate eval id: {case_id}"))
        seen_ids.add(case_id)

        for key in ["prompt", "expected_output", "files", "assertions"]:
            if key not in case:
                errors.append(fail(f"eval {case_id or index} missing key: {key}"))

        prompt = str(case.get("prompt", ""))
        if not prompt.startswith("Use $implementation-task-planner"):
            errors.append(fail(f"eval {case_id or index} prompt must explicitly invoke the skill"))

        files = case.get("files", [])
        if not isinstance(files, list):
            errors.append(fail(f"eval {case_id or index} files must be a list"))
            continue
        for relative_file in files:
            if not isinstance(relative_file, str):
                errors.append(fail(f"eval {case_id or index} file entry must be a string"))
                continue
            if not (root / relative_file).exists():
                errors.append(fail(f"eval {case_id or index} references missing file: {relative_file}"))

        assertions = case.get("assertions", [])
        if not isinstance(assertions, list) or not assertions:
            errors.append(fail(f"eval {case_id or index} must include assertions"))

    return errors


def validate_schema(root: Path) -> list[str]:
    errors: list[str] = []
    try:
        schema = load_json(root / "references" / "tasks-json-schema.json")
    except ValueError as exc:
        return [fail(str(exc))]

    schema_id = str(schema.get("$id", ""))
    if EXPECTED_VERSION not in schema_id:
        errors.append(fail(f"tasks-json-schema.json $id must include {EXPECTED_VERSION}"))

    try:
        pattern = schema["properties"]["schema_version"]["pattern"]
    except (KeyError, TypeError):
        errors.append(fail("tasks-json-schema.json must constrain schema_version"))
    else:
        if EXPECTED_VERSION.replace(".", r"\.") not in str(pattern):
            errors.append(fail(f"tasks-json-schema.json schema_version must be {EXPECTED_VERSION}"))

    return errors


def validate_workflow(root: Path) -> list[str]:
    text = read_text(root / ".github" / "workflows" / "validate.yml")
    required = [
        "name: Validate Skill",
        "actions/checkout@v4",
        "actions/setup-python@v5",
        "python scripts/validate_skill.py .",
    ]
    return [fail(f"validate.yml missing required content: {snippet}") for snippet in required if snippet not in text]


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    if not root.exists():
        print(fail(f"repository root does not exist: {root}"))
        return 1

    errors: list[str] = []
    errors.extend(validate_required_files(root))

    if not errors:
        errors.extend(validate_skill_md(root))
        errors.extend(validate_readme(root))
        errors.extend(validate_changelog(root))
        errors.extend(validate_openai_yaml(root))
        errors.extend(validate_evals(root))
        errors.extend(validate_schema(root))
        errors.extend(validate_workflow(root))

    if errors:
        for error in errors:
            print(error)
        return 1

    print(f"OK: {EXPECTED_NAME} repository validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
