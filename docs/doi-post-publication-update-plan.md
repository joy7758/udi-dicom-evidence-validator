# DOI Post-Publication Update Plan

This plan applies only after Zenodo or another archive service returns a real
record URL and DOI.

Required inputs:

- verified DOI
- verified record URL
- public release tag
- capture date

Allowed updates:

- README citation section
- `CITATION.cff`
- `codemeta.json`
- `.zenodo.json`
- `docs/citation-and-archiving.md`
- `docs/doi-capture-record-v0.8.md`

Not allowed:

- validator behavior changes
- schema changes
- public example semantic changes
- private suite or private service release changes
- clinical validation, regulatory approval, or certification claims

The DOI capture PR must run the no-fake-DOI check, citation metadata consistency
check, DOI archive review package check, unit tests, ruff, and mypy.
