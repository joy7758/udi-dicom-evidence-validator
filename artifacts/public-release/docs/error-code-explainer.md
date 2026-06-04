# Error Code Explainer

Primary error codes are deterministic so reviewers can compare results across
runs.

- `missing_udi`: required UDI evidence is absent.
- `registry_unresolved`: offline registry fixture did not resolve the UDI-DI.
- `device_uid_used_as_udi_di`: DICOM Device UID was incorrectly supplied as
  UDI-DI.
- `sop_uid_mismatch`: manifest and metadata SOP Instance UID differ.
- `artifact_hash_mismatch`: declared artifact hash does not match expectation.

Device UID is an equipment UID in DICOM metadata. It is not the UDI-DI.

