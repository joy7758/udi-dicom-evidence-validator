# Public Synthetic Examples v0.2

These fixtures extend v0.1 with `synthetic_workflow_trace_id`, receipt
provenance, and optional FDO-style mapping metadata. All data is synthetic,
offline-first, no PHI, and not clinical validation or regulatory approval.

| File | Expected result |
| --- | --- |
| `manifest_v0.2.pass.json` | pass with `trace_id_consistency` and `fdo_mapping_consistency` |
| `manifest_v0.2.fail_missing_udi.json` | `missing_udi` |
| `manifest_v0.2.fail_registry_unresolved.json` | `registry_unresolved` |
| `manifest_v0.2.fail_device_uid_used_as_udi_di.json` | `device_uid_used_as_udi_di` |
