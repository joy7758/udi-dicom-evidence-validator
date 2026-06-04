# DOI Archive Review v0.8

Status: `DOI_CAPTURED_V0_8_1`

This review package prepares the public validator for a later archive deposit.
It does not write a DOI, does not create a GitHub Release, and does not change
validator behavior, schemas, or public example semantics.

Scope:

- public validator repository only
- DOI readiness manifest
- Zenodo manual enablement checklist
- public GitHub Release trigger plan
- no-fake-DOI scan output
- paper finalization bundle
- citation metadata consistency gate

Manual archive gate:

1. A human enables Zenodo GitHub integration for the public repository.
2. A new public GitHub Release is created after enablement.
3. Zenodo returns a real record URL and DOI.
4. A later DOI capture PR verifies the record and updates citation metadata.

Boundary:

- no PHI
- no raw DICOM
- not clinical validation
- not regulatory approval
- not certification
- no fake DOI
- Device UID != UDI-DI
- offline fixture first
- live openFDA explicit opt-in
- FDO-style mapping only
- no robot operation evidence

Private suite and private service materials are excluded from public DOI assets.

## v0.8.1 DOI Capture

Verified DOI: `10.5281/zenodo.20540532`

Zenodo record URL: https://zenodo.org/records/20540532

The DOI was captured after the Zenodo repository settings page showed the
`v0.8.1-public` release DOI and the DOI URL resolved to the matching Zenodo
record page. This capture does not modify validator behavior, schemas, public
examples, API, CLI, or receipt semantics.
