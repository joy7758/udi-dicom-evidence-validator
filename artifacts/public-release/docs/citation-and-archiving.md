# Citation And Archiving

This repository has a Zenodo DOI for the latest public validator archive:

- Exact-version DOI: `10.5281/zenodo.20635229`
- Zenodo record: https://zenodo.org/records/20635229
- Concept DOI: `10.5281/zenodo.20540531`

Archive metadata is maintained through `CITATION.cff`, `codemeta.json`, and
`.zenodo.json`.

Recommended citation metadata:

- Title: UDI-DICOM Evidence Validator
- Author: Bin Zhang
- License: MIT
- Repository: https://github.com/joy7758/udi-dicom-evidence-validator
- Keywords: UDI-DICOM, evidence manifest, medical-device imaging workflow,
  synthetic validation fixture

Boundary:

- Archive metadata does not imply clinical validation.
- Archive metadata does not imply regulatory approval.
- Archive metadata does not imply certification.
- Archive metadata does not imply unrestricted access to private suites or
  private service materials.

v0.5 paper review material may be archived as a public software artifact after
review, but the reproducibility capsule remains a technical reproduction pack.
It does not claim DOI assignment until an archive service assigns one, and it
does not imply clinical validation, regulatory approval, certification, or
official FDO implementation.

v0.6 adds an archive metadata report and DOI readiness checklist. These outputs
are DOI-ready review material only. They do not claim an assigned DOI, and they
exclude private suite and private service material from public DOI scope.

v0.8 adds a DOI archive review package, no-fake-DOI scan, paper finalization
bundle, and citation metadata consistency gate. The state remains DOI pending
until Zenodo or another archive service returns a real record URL and DOI.
Public DOI scope is the public validator only; private suite and private service
materials are excluded from public DOI assets.

v0.8.1 captures the verified Zenodo DOI after the Zenodo record was observed and
the DOI URL resolved to the matching Zenodo record page. The DOI applies only to
the public validator archive. It does not include private conformance suite or
private sample validation service materials, and it does not imply clinical
validation, regulatory approval, certification, or PHI processing.

v1.0.1-public captures the current exact-version Zenodo DOI after the
`v1.0.1-public` GitHub Release was archived by Zenodo. Use
`10.5281/zenodo.20635229` when citing the exact `v1.0.1-public` archive. Use
the concept DOI `10.5281/zenodo.20540531` when citing the software series. The
prior DOI `10.5281/zenodo.20540532` remains a historical DOI for
`v0.8.1-public`; it is not the current latest archive DOI.

The v1.0.1-public DOI capture is metadata-only. It does not change validator
behavior, schema behavior, CLI behavior, API behavior, public example
semantics, receipt semantics, DICOM extraction logic, or registry validation
logic.
