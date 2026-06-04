# Minimal Profile Explainer

The manifest profile links four review inputs:

1. Synthetic DICOM equipment metadata represented as JSON.
2. A manifest declaring UDI-DI, SOP Instance UID, artifacts, and optional v0.2
   trace/provenance/FDO-style metadata.
3. An offline registry fixture.
4. Declared evidence item hashes.

The validator checks consistency across these inputs and emits a deterministic
receipt. It does not inspect raw DICOM files and does not provide clinical,
regulatory, safety, or certification conclusions.

