# No Fake DOI Policy v0.8

Allowed before archive completion:

- DOI-ready
- DOI pending
- pending Zenodo archive
- record URL pending
- DOI capture blocked until record verification

Not allowed before archive completion:

- synthetic DOI strings
- placeholder DOI strings presented as real
- claims that a DOI has already been returned
- citation metadata that contains an unverified DOI
- release notes that imply archive completion before Zenodo returns a record

The only allowed DOI-like reference before capture is the codemeta schema
context URL. A real DOI may be written only after the record URL is reachable
and the record contains the same DOI.
