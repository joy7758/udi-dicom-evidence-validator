# UDI-DICOM Evidence Validator

Minimal public validator for a synthetic UDI-DICOM evidence manifest profile.
It checks whether DICOM equipment metadata, a manifest, registry evidence, and
declared artifacts form a deterministic review packet.

This is not clinical validation, not regulatory approval, not safety assurance,
not certification, and not a replacement for PACS, VNA, asset management, or
manufacturer quality systems. Public examples are synthetic and contain no PHI.

## Quickstart

```bash
python -m venv .venv
. .venv/bin/activate
python -m pip install -U pip
pip install -e '.[dev,api]'
pytest -q
python demo/portable-ultrasound/run_demo.py
```

## CLI

```bash
udi-dicom-validate validate-manifest \
  --manifest examples/public/manifest.pass.json \
  --dicom-metadata examples/public/sample_dicom_metadata.pass.json \
  --registry-fixture examples/public/registry.fixture.resolved.json \
  --out-dir /tmp/udi-dicom-validator-pass
```

The command writes `receipt.json` and `report.md`. Receipts are deterministic:
the same inputs produce the same check order, primary error code, and receipt id.

## API

The optional API is public-only and validation-only:

```bash
pip install -e '.[api]'
uvicorn udi_dicom_validator.api:app --reload
```

It does not expose private conformance, vendor-rule, or real-sample assessment
interfaces.

## Public Examples

Files in `examples/public/` are synthetic fixtures. They demonstrate the pass
case and isolated failure modes for `missing_udi`, `sop_uid_mismatch`,
`registry_unresolved`, and `device_uid_used_as_udi_di`.

## Boundary

DICOM `Device UID (0018,1002)` is a device/equipment UID in DICOM metadata. It
is not the regulatory UDI-DI. The UDI string is carried through the DICOM UDI
Macro, including `Unique Device Identifier (0018,1009)` inside `UDI Sequence
(0018,100A)`. This project checks evidence consistency; it does not establish
medical, legal, regulatory, or safety conclusions.


## v0.2 Profile

The v0.2 public profile adds synthetic workflow trace ids, receipt provenance,
and optional metadata-only FDO-style mapping fields. Run the v0.2 demo with:

```bash
python demo/portable-ultrasound/run_demo.py
python -m json.tool demo/portable-ultrasound/artifacts_v0.2/receipt.json
```

These fields are synthetic review metadata only and do not create clinical,
regulatory, certification, or production FDO claims.

## v0.3 Release Hardening

v0.3 adds golden receipt regression, a public evaluation matrix, release
artifact inventory, and a public-only MCP skeleton. These are reproducibility and
agent-readability surfaces only. Private conformance cases and real samples stay
outside this repository.

## v0.4 Release Hardening Branch

v0.4 focuses on remote reproducibility, external review readiness, public release
asset building, and citation/archive readiness. Use:

```bash
python scripts/verify_remote_release.py
python scripts/build_public_release_assets.py
python scripts/clean_clone_smoke.py
```

The public release asset builder is public-only: it excludes the private
conformance suite, private sample validation service, real samples, raw DICOM
files, and PHI. The external review pack is in `docs/external-review-brief.md`,
`docs/external-review-checklist.md`, and `docs/reproducibility-for-reviewers.md`.
Archive metadata is DOI-ready only; no DOI is claimed until an archive service
assigns one.
