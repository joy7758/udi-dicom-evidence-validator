# External Review - 10 Minute Guide

agent_readable:
  document_type: external_review_quickstart
  audience: technical_reviewer
  expected_runtime: 10_minutes
  public_only: true
  accepts_phi: false
  accepts_raw_dicom: false
  clinical_validation: false
  regulatory_approval: false
  certification: false

## 1. What This Project Is

`udi-dicom-evidence-validator` is a public reference validator for a synthetic
UDI-DICOM evidence manifest workflow. It checks whether declared DICOM equipment
metadata, manifest fields, offline registry evidence, and review artifacts form
a deterministic review packet.

The repository is designed for software-level metadata consistency review,
reproducibility, citation, and external technical feedback. Public examples are
synthetic and de-identified by design.

## 2. Run The Demo In 10 Minutes

```bash
python -m venv .venv
. .venv/bin/activate
python -m pip install -U pip
pip install -e '.[dev,api]'
pytest -q
python demo/portable-ultrasound/run_demo.py
```

Expected demo shape:

```text
PASS manifest_id=synthetic-portable-ultrasound-v02-pass-001 checks=6
```

The demo writes a review receipt and report under
`demo/portable-ultrasound/artifacts_v0.2/`.

## 3. What The Validator Checks

- Required manifest structure and parseability.
- UDI-DI presence and expected mapping to public synthetic fixtures.
- DICOM SOP Instance UID consistency between manifest and metadata JSON.
- Registry fixture resolution for declared UDI-DI values.
- Device UID misuse as UDI-DI.
- Deterministic receipt and report generation.

## 4. What The Validator Does Not Check

- It does not validate clinical safety or clinical effectiveness.
- It does not provide regulatory approval or certification.
- It does not process raw DICOM files in the public demo.
- It does not accept PHI, real hospital records, or real patient material.
- It does not expose private conformance suite content or private service
  workflows.
- It does not replace PACS, VNA, CMMS, asset management, or manufacturer quality
  systems.

## 5. Why Device UID Is Not UDI-DI

DICOM `Device UID (0018,1002)` is an equipment UID in DICOM metadata. UDI-DI is
the fixed device identifier portion of a regulatory UDI. This validator rejects
the pattern where a Device UID is used as UDI-DI because it creates an identifier
boundary violation.

## 6. How To Read `receipt.json` And `report.md`

`receipt.json` is the machine-readable result. Review these fields first:

- `ok`: overall pass/fail.
- `manifest_id`: synthetic manifest under review.
- `checks`: ordered validation checks.
- `primary_error_code`: first failure category when validation fails.
- `receipt_id`: deterministic identifier for the validation result.

`report.md` is the human-readable result. Use it to confirm the same pass/fail
state, check names, and boundary wording without parsing JSON manually.

## 7. DOI And Citation

Use the public archive citation only for the public validator archive:

- Zenodo DOI: `10.5281/zenodo.20540532`
- Zenodo record: https://zenodo.org/records/20540532
- Citation metadata: `CITATION.cff`, `codemeta.json`, `.zenodo.json`

The archive does not include private conformance suite material, private sample
validation service material, real samples, PHI, or raw DICOM files.

## 8. Materials Not In The Public Repository

- Private conformance cases.
- Private sample validation service workflows.
- Vendor private rules.
- Real DICOM files.
- PHI or patient-level records.
- Hospital deployment material.
- Clinical validation, regulatory approval, safety assurance, or certification
  packages.

## Review Outcome Template

```text
reviewer:
date:
commit:
commands_run:
  - pytest -q
  - python demo/portable-ultrasound/run_demo.py
result:
  tests:
  demo:
  boundary:
  citation:
notes:
```
