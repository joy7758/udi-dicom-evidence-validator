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

## v0.3 Workflow

Regenerate `tests/golden/` receipts, run `scripts/check_golden_receipts.py`, run
`scripts/build_public_evaluation_matrix.py`, and verify that public MCP tools
only read public examples and public docs.

## v0.4 Workflow

For release hardening, run `scripts/build_public_release_assets.py`,
`scripts/verify_remote_release.py`, and, when network access is available,
`scripts/clean_clone_smoke.py`. Keep release assets public-only. Do not expose
private suite or private service materials. Archive metadata is DOI-ready only
and must not claim an assigned DOI before Zenodo or another archive service
assigns one.

## v0.5 Workflow

For paper review and reproducibility changes, update `paper/`,
`docs/external-review-pack-v0.5.md`, reviewer docs, and the reproducibility
capsule scripts together. Run `scripts/build_reproducibility_capsule.py` and
`scripts/check_reproducibility_capsule.py`. Keep outputs synthetic-only,
public-only, and free of raw DICOM files, PHI, private cases, clinical
validation claims, regulatory approval claims, certification claims, robot
operation evidence, and official FDO implementation claims.
