# AGENTS.md

Use this repository only for the public UDI-DICOM evidence manifest validator.

## Required Workflow

- Modify schema, examples, validator, reports, and tests together when behavior changes.
- Keep public examples synthetic and de-identified.
- Run `pytest -q`, `ruff check .`, and `python demo/portable-ultrasound/run_demo.py`.
- Default to offline registry fixtures. Live openFDA lookup must be explicit.
- Never expose private conformance suite content here.
- Never treat DICOM `Device UID (0018,1002)` as UDI-DI.
- Never add real patient data, hospital identifiers, real sample files, or vendor-specific private rules.

## Claims Boundary

Do not claim clinical validation, regulatory approval, safety assurance,
certification, legal non-repudiation, or replacement of PACS/VNA/asset systems.


## v0.2 Modification Rule

For v0.2, update trace/provenance/FDO-style mapping examples, schemas, validator checks, receipts, API, demo, and tests together.

## v0.3 Release Hardening Rule

When changing public examples or validator behavior, regenerate golden receipts,
check golden receipts, rebuild the public evaluation matrix, and keep the
public-only MCP skeleton from accessing private, partner, or real-sample content.

## v0.4 Remote Release Rule

For v0.4 release hardening work, keep all new automation public-only. Use
`scripts/build_public_release_assets.py` for public-safe assets,
`scripts/verify_remote_release.py` for GitHub release checks, and
`scripts/clean_clone_smoke.py` for clean clone reproducibility. Do not call
private repositories, do not include raw DICOM files, and do not claim DOI,
clinical validation, regulatory approval, or certification.

## v0.5 Paper Review Rule

For v0.5 paper and external review work, keep changes public-only and
synthetic-only. Use `scripts/build_reproducibility_capsule.py` and
`scripts/check_reproducibility_capsule.py` for reviewer reproduction material.
Do not add real samples, raw DICOM files, PHI, private suite content, private
service workflows, robot operation evidence, clinical validation, regulatory
approval, certification, or official FDO implementation claims.

## v0.6 Paper Submission Rule

For v0.6 paper submission readiness, do not change validator behavior, schema
behavior, or public example semantics. Keep work limited to journal-neutral
paper material, DOI-ready metadata review, external feedback intake, and
Mermaid figure sources. Run `scripts/build_archive_metadata_report.py`,
`scripts/check_archive_metadata_report.py`,
`scripts/build_paper_submission_package.py`, and
`scripts/check_paper_submission_package.py`. Do not claim an assigned DOI.
