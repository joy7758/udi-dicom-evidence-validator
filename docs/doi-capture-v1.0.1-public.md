# DOI Capture v1.0.1-public

agent_readable:
  document_type: doi_capture_record
  release_tag: v1.0.1-public
  version_doi: 10.5281/zenodo.20635229
  concept_doi: 10.5281/zenodo.20540531
  public_validator_archive_only: true
  validator_behavior_changed: false
  schema_changed: false
  cli_api_changed: false
  new_tag_created_by_this_commit: false
  new_release_created_by_this_commit: false

## Scope

`v1.0.1-public` is the exact public release archive for the UDI-DICOM
Evidence Validator patch release. This DOI capture records the Zenodo archive
that was created from the already-published GitHub Release.

This commit must not be tagged or released. It only records citation metadata
after the archive already exists.

## Version DOI

- Version DOI: `10.5281/zenodo.20635229`
- Zenodo record: https://zenodo.org/records/20635229
- GitHub release: https://github.com/joy7758/udi-dicom-evidence-validator/releases/tag/v1.0.1-public
- Release tag: `v1.0.1-public`
- Target commit: `37fdedfc0b6edfbb07432148d1b738f2712a7c8d`
- Archive file: `joy7758/udi-dicom-evidence-validator-v1.0.1-public.zip`
- Archive checksum: `md5:f031e65ee9c3c4a0fd62140b2d5b83c2`

Use this DOI when citing the exact `v1.0.1-public` archive.

## Concept DOI

- Concept DOI: `10.5281/zenodo.20540531`

Use the concept DOI when citing the software series rather than a specific
version.

## Boundary

The archive is public validator only. It excludes:

- private conformance suite material
- private sample-validation service material
- real samples
- PHI
- raw DICOM files
- vendor private rules
- hospital identifiers
- non-de-identified DICOM material

This DOI capture does not change validator behavior, schema behavior, CLI
behavior, API behavior, public example semantics, receipt semantics, DICOM
extraction logic, or registry validation logic.

It does not claim clinical validation, regulatory approval, safety
certification, legal compliance, production deployment, official FDO
conformance, or hospital-wide interoperability.

## Historical Version

The previous version DOI `10.5281/zenodo.20540532` remains a historical DOI for
the `v0.8.1-public` archive. It is no longer the current latest archive DOI.
