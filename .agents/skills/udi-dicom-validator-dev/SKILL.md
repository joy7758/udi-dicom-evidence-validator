---
name: udi-dicom-validator-dev
description: Use when modifying UDI-DICOM evidence manifest profile, schema, examples, validator, tests, demo, or docs. Enforces public/private boundary and deterministic validation behavior.
---

# UDI-DICOM Validator Dev

## Trigger Conditions

Use this skill for changes to profile, schema, examples, validator, tests, demo,
docs, API, or CLI.

## Required Workflow

Keep schema/examples/validator/tests synchronized. Run `pytest -q`,
`ruff check .`, and the portable ultrasound demo.

## Error Code Policy

Primary error codes must be deterministic and drawn from `docs/error-codes.md`.

## Claims Boundary

Do not claim clinical validation, regulatory approval, certification, safety
assurance, or production deployment. Never expose private assets.


## v0.2 Workflow

Keep `synthetic_workflow_trace_id`, `provenance`, and optional `fdo_mapping` deterministic. Add tests for trace and FDO mapping consistency when behavior changes.
