# Methods

The public validator uses synthetic JSON fixtures to exercise deterministic
checks over a minimal evidence manifest profile.

Inputs:

- A manifest declaring profile version, UDI-DI, SOP Instance UID, evidence
  artifacts, optional synthetic trace id, provenance, and optional FDO-style
  mapping fields.
- A DICOM metadata extraction fixture represented as JSON, not a raw DICOM
  file.
- A registry fixture represented as JSON.

Checks:

- Required UDI fields are present.
- DICOM SOP Instance UID matches the manifest.
- DICOM Device UID is not accepted as UDI-DI.
- Registry fixture status and UDI-DI are consistent with the manifest.
- Declared artifacts include stable hashes and review metadata.

Outputs:

- Deterministic JSON validation receipt.
- Markdown report.
- Public evaluation matrix.
- Golden receipt regression files.

