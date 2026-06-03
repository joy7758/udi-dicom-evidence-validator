# Public Synthetic Examples

All JSON files are synthetic. They contain no real patient, hospital, serial
number, or controlled private conformance data.

| File | Expected result |
| --- | --- |
| `manifest.pass.json` | pass |
| `manifest.fail_missing_udi.json` | `missing_udi` |
| `manifest.fail_wrong_sop_uid.json` | `sop_uid_mismatch` |
| `manifest.fail_registry_unresolved.json` | `registry_unresolved` |
| `manifest.fail_device_uid_used_as_udi_di.json` | `device_uid_used_as_udi_di` |
