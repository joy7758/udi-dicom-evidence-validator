# Public MCP Tool Skeleton

The public MCP skeleton is implemented as a lightweight Python function layer in
`src/udi_dicom_validator/mcp_server.py`. It does not start a network server.

Allowed public tools:

- `list_profile_versions`
- `list_public_examples`
- `get_error_code_definition`
- `validate_public_manifest_fixture`
- `render_public_receipt_summary`

Forbidden private or real-sample tools:

- `run_private_suite`
- `access_partner_cases`
- `access_real_samples`
- `vendor_mapping_private_review`
- `hospital_sample_assessment`

All tool functions are restricted to public examples, public schemas, and public
error-code documentation. They must not access PHI, private conformance cases, or
real customer samples.
