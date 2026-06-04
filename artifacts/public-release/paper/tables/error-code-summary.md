# Error Code Summary

| Error Code | Meaning | Reviewer Interpretation |
| --- | --- | --- |
| `missing_udi` | UDI evidence is absent or incomplete | Manifest is not review-complete |
| `sop_uid_mismatch` | Manifest and metadata SOP Instance UID differ | Inputs do not describe the same instance |
| `registry_unresolved` | Registry fixture does not resolve the UDI-DI | Offline fixture review failed |
| `device_uid_used_as_udi_di` | DICOM Device UID was used as UDI-DI | Identifier boundary violation |
| `artifact_hash_mismatch` | Declared artifact hash differs | Review artifact is not stable |

