# Versioning Policy

Profile versions and validator versions are tracked separately.

- Profile `v0.1.0`: minimum manifest and receipt model.
- Profile `v0.2.0`: adds synthetic trace id, provenance, and optional
  FDO-style mapping metadata.
- Planned validator `v0.3.0`: release hardening, golden regression, public
  evaluation matrix, and public-only MCP skeleton.

Minor releases may add optional metadata and public fixtures, but must not change
the no-PHI, offline-fixture-first, public/private, or clinical/regulatory
boundaries.
