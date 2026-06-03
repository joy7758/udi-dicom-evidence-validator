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
