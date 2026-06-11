# Citation Version Policy

agent_readable:
  document_type: citation_version_policy
  package_version_source: pyproject.toml
  archive_release_version_source: GitHub Release and Zenodo archive
  citation_metadata_version_source: CITATION.cff and codemeta.json
  latest_archive_release_version: v1.0.1-public
  latest_version_doi: 10.5281/zenodo.20635229
  concept_doi: 10.5281/zenodo.20540531

## Version Surfaces

This repository has three separate version surfaces.

`package_version` is the Python package version from `pyproject.toml`. It may
remain at the package API version when a release only changes documentation,
audit material, citation metadata, or archive records.

`archive_release_version` is the GitHub Release and Zenodo archive version. For
the current public validator archive, this is `v1.0.1-public`.

`citation_metadata_version` is the citation-facing software archive version
recorded in `CITATION.cff` and `codemeta.json`. It may track the latest public
archive release even when the Python package version does not change.

## Exact Version Citation

Use the version DOI for exact archive citation:

```text
Zhang, Bin. UDI-DICOM Evidence Validator, v1.0.1-public. Zenodo.
DOI: 10.5281/zenodo.20635229.
```

Zenodo record: https://zenodo.org/records/20635229

## Software Series Citation

Use the concept DOI for software-series citation:

```text
UDI-DICOM Evidence Validator. Concept DOI: 10.5281/zenodo.20540531.
```

## Historical DOI Handling

The DOI `10.5281/zenodo.20540532` remains a historical version DOI for
`v0.8.1-public`. It should not be described as the current latest archive DOI
after `v1.0.1-public`.

## Boundary

Citation metadata covers the public validator archive only. It does not include
private conformance suite material, private sample-validation service material,
real samples, PHI, raw DICOM files, vendor private rules, hospital identifiers,
or non-de-identified DICOM material.
