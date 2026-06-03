# UDI-DICOM Evidence Manifest Profile v0.2.0

## Purpose

v0.2 keeps the v0.1 public validation boundary and adds deterministic workflow
traceability plus optional FDO-style mapping metadata for synthetic review
packets.

## Additions Since v0.1.0

- `synthetic_workflow_trace_id`: required for v0.2 synthetic workflows.
- `provenance`: records synthetic source, generator, synthetic-data flag, and
  workflow trace id.
- `fdo_mapping`: optional metadata-only FDO-style mapping fields such as
  `profile_pid`, `object_type`, `kernel_metadata_profile`, `metadata_persistence`,
  `resolver_hint`, and `artifact_relation`.
- Receipts include `trace_id` and `provenance`.
- v0.2 validators add `trace_id_consistency` and `fdo_mapping_consistency` pass
  checks when v0.2 fields are present and coherent.

## Boundary

v0.2 is still not clinical validation, not regulatory approval, not safety
assurance, not certification, not medical decision support, and not a production
FDO implementation. Public examples remain synthetic and offline fixture first.

## Determinism

The workflow trace id is input data, not a generated random identifier. Receipt
ids remain deterministic hashes over manifest, metadata, registry, and check
results.
