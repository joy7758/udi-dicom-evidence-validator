# Error Codes

| Stage | Code | Meaning |
| --- | --- | --- |
| presence_parseability | missing_udi | Manifest or DICOM metadata lacks a UDI string. |
| presence_parseability | truncated_udi | UDI string is too short for supported parsing. |
| presence_parseability | parser_failed | Minimal parser could not parse the UDI. |
| presence_parseability | missing_udi_di | Parsed UDI-DI is missing. |
| presence_parseability | device_uid_used_as_udi_di | DICOM Device UID was used as UDI-DI. |
| reference_closure | missing_sop_instance_uid | SOP Instance UID is missing. |
| reference_closure | sop_uid_mismatch | Manifest and DICOM SOP Instance UID differ. |
| reference_closure | missing_evidence_item | Required evidence item is missing or incomplete. |
| reference_closure | evidence_uri_unreadable | Evidence URI cannot be reviewed. |
| reference_closure | artifact_hash_mismatch | Declared artifact hash does not match. |
| cross_layer_consistency | dicom_manifest_udi_mismatch | DICOM UDI and manifest UDI differ. |
| cross_layer_consistency | serial_number_mismatch | Serial number differs. |
| cross_layer_consistency | model_name_mismatch | Model name differs. |
| cross_layer_consistency | manufacturer_mismatch | Manufacturer differs. |
| cross_layer_consistency | device_uid_confused_with_udi_di | Device UID was confused with UDI-DI. |
| registry_resolution | registry_provider_missing | Registry provider is missing. |
| registry_resolution | lookup_timestamp_missing | Lookup timestamp is missing. |
| registry_resolution | registry_unresolved | Registry fixture or lookup did not resolve. |
| registry_resolution | registry_timeout | Registry lookup timed out. |
| registry_resolution | registry_model_mismatch | Registry model does not match. |
| registry_resolution | registry_company_mismatch | Registry company does not match. |

| v0.2 | trace_id_mismatch | Manifest, provenance, or registry trace id differs. |
| v0.2 | fdo_mapping_mismatch | Optional FDO-style mapping is internally inconsistent. |
