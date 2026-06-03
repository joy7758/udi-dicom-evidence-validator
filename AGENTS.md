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
