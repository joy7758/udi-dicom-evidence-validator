# UDI-DICOM Evidence Manifest Profile v0.1.0

## Purpose

Define a minimal public evidence manifest for reviewing whether DICOM equipment
metadata, UDI fields, registry lookup evidence, and declared artifacts are
consistent enough for technical review.

## Scope

- Synthetic or de-identified metadata.
- DICOM equipment identity fields.
- UDI string capture and minimal DI/PI parsing.
- Offline registry fixture resolution and optional live openFDA lookup.
- Deterministic validation receipts.

## Non-scope

Clinical validation, regulatory approval, safety assurance, certification,
PACS/VNA replacement, legal proof, private conformance scoring, and patient data
processing are out of scope.

## Terminology

| Term | Meaning |
| --- | --- |
| UDI | Full unique device identifier string assigned by an issuing agency. |
| UDI-DI | Fixed device identifier portion of UDI, corresponding to model/version. |
| UDI-PI | Production identifier portion such as lot or serial when present. |
| Device UID | DICOM equipment UID. It is not UDI-DI. |

## DICOM Field Mapping

| Concept | DICOM tag | Profile field |
| --- | --- | --- |
| UDI Sequence | `(0018,100A)` | source for `full_udi` |
| Unique Device Identifier | `(0018,1009)` | `full_udi` |
| Device Serial Number | `(0018,1000)` | `serial_number` |
| Device UID | `(0018,1002)` | `device_uid`, never UDI-DI |
| Manufacturer | `(0008,0070)` | `manufacturer` |
| Manufacturer's Model Name | `(0008,1090)` | `model_name` |

## Manifest Minimum Fields

The manifest records SOP, Study, and Series UIDs; full UDI; issuing agency;
parsed DI/PI; registry provider, jurisdiction, timestamp, status, and summary;
manufacturer/model/serial/device UID; evidence items; artifact hashes; validation
status; and checks.

## Validation Stages

1. `presence_parseability`: required UDI and minimal parser checks.
2. `reference_closure`: SOP UID and evidence item closure.
3. `cross_layer_consistency`: DICOM metadata versus manifest consistency.
4. `registry_resolution`: offline fixture or explicit live registry outcome.

## Severity Model

`pass` means the check passed, `warn` means review is needed without failing the
receipt, and `fail` means the receipt is not OK.

## Error Code Table

See `docs/error-codes.md`.

## Determinism Requirements

Validation order, primary error selection, receipt ids, reports, and examples
must be deterministic for identical inputs.

## Registry Lookup Policy

Offline fixtures are the default. Live openFDA lookup is optional, explicit, and
not medical decision support.

## Synthetic Demo Policy

Public examples must be synthetic and must not contain patient data, real hospital
data, real sample identifiers, or private conformance cases.

## Claims to Avoid

Do not claim clinical validation, regulatory approval, safety assurance,
certification, legal proof, or production readiness.
