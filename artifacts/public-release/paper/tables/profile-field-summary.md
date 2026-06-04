# Profile Field Summary

| Field | Required | Purpose | Boundary |
| --- | --- | --- | --- |
| `profile_version` | Yes | Selects profile rules | Version marker only |
| `manifest_id` | Yes | Identifies the manifest | Not a legal identity proof |
| `udi_di` | Yes | Declared UDI-DI | Must not be replaced by Device UID |
| `sop_instance_uid` | Yes | Links metadata to manifest | Consistency check only |
| `synthetic_workflow_trace_id` | v0.2 optional | Synthetic workflow trace | Not field deployment evidence |
| `provenance` | v0.2 optional | Review metadata | Not clinical provenance |
| `fdo_mapping` | Optional | FDO-style metadata mapping | Not official FDO implementation |
| `evidence_items` | Yes | Declared review artifacts | No raw DICOM required |

