# DOI Capture Audit v1.0.1-public

agent_readable:
  document_type: doi_capture_audit
  release_tag: v1.0.1-public
  version_doi: 10.5281/zenodo.20635229
  concept_doi: 10.5281/zenodo.20540531
  status: DOI_CAPTURE_METADATA_PASS
  no_new_release_created: true
  no_tag_created: true
  validator_behavior_changed: false
  schema_changed: false
  cli_api_changed: false
  public_example_semantics_changed: false

## Scope

This audit records the metadata-only DOI capture for the already-published
`v1.0.1-public` GitHub Release and Zenodo archive. It does not create a new
tag, does not create a new GitHub Release, and does not trigger a new
Zenodo-targeted release.

## files_changed

Citation and DOI capture files:

- `.zenodo.json`
- `CITATION.cff`
- `codemeta.json`
- `README.md`
- `artifacts/doi-capture-v1.0.1-public/doi-capture-summary.json`
- `docs/doi-capture-v1.0.1-public.md`
- `docs/citation-version-policy.md`
- `docs/citation-and-archiving.md`
- `docs/doi-capture-audit-v1.0.1-public.md`

Citation and DOI gate scripts/tests:

- `scripts/check_no_fake_doi.py`
- `scripts/check_citation_metadata_consistency.py`
- `scripts/check_real_doi_record.py`
- `scripts/build_archive_metadata_report.py`
- `tests/test_citation_metadata_consistency.py`
- `tests/test_real_doi_record.py`

Generated public artifacts refreshed by the repository's existing checks:

- `artifacts/citation-metadata-consistency-v0.8.json`
- `artifacts/citation-metadata-consistency-v0.8.md`
- `artifacts/archive-metadata-report-v0.6.json`
- `artifacts/archive-metadata-report-v0.6.md`
- `artifacts/doi-archive-review-v0.8/no_fake_doi_scan.json`
- `artifacts/doi-archive-review-v0.8/SHA256SUMS.txt`
- `artifacts/public-release/CITATION.cff`
- `artifacts/public-release/README.md`
- `artifacts/public-release/codemeta.json`
- `artifacts/public-release/docs/citation-and-archiving.md`
- `artifacts/public-release/SHA256SUMS.txt`
- `artifacts/public-release/udi-dicom-evidence-validator-public-worktree-source.zip`
- `artifacts/reproducibility-capsule-v0.5/release_asset_manifest.json`
- `artifacts/reproducibility-capsule-v0.5/SHA256SUMS.txt`

No changes were made under:

- `schema/`
- `validator/`
- `src/udi_dicom_validator/`
- `examples/public/`
- `openapi/`

## commands_run

| Command | Result |
| --- | --- |
| `git checkout main && git pull --ff-only && git checkout -b chore/v1.0.1-public-doi-capture` | PASS |
| `gh release view v1.0.1-public --repo joy7758/udi-dicom-evidence-validator --json tagName,url,name,isDraft,isPrerelease,publishedAt,targetCommitish` | PASS |
| `curl -fsSL https://zenodo.org/api/records/20635229` | PASS |
| `curl -Ls -o /dev/null -w '%{url_effective}\n%{http_code}\n' https://doi.org/10.5281/zenodo.20635229` | PASS |
| `./.venv/bin/python scripts/check_no_fake_doi.py` | PASS |
| `./.venv/bin/python scripts/check_citation_metadata_consistency.py` | PASS |
| `./.venv/bin/python scripts/check_real_doi_record.py` | PASS |
| `./.venv/bin/python scripts/build_archive_metadata_report.py` | PASS |
| `./.venv/bin/python scripts/check_archive_metadata_report.py artifacts/archive-metadata-report-v0.6.json` | PASS |
| `./.venv/bin/python -m pytest -q` | PASS |
| `./.venv/bin/python -m ruff check .` | PASS |
| `./.venv/bin/python demo/portable-ultrasound/run_demo.py` | PASS |
| `./.venv/bin/python scripts/check_doi_archive_review_package.py artifacts/doi-archive-review-v0.8` | PASS |
| `./.venv/bin/python scripts/check_reproducibility_capsule.py artifacts/reproducibility-capsule-v0.5` | PASS |

## pass_fail_summary

- Version DOI capture: PASS, `10.5281/zenodo.20635229`.
- Concept DOI capture: PASS, `10.5281/zenodo.20540531`.
- GitHub Release check: PASS, `v1.0.1-public` exists and is not draft or prerelease.
- Zenodo record check: PASS, record `20635229` is `published` and `done`.
- DOI redirect check: PASS, DOI resolves to `https://zenodo.org/records/20635229`
  with HTTP `200`.
- Tests: PASS, 35 tests passed.
- Ruff: PASS.
- Demo: PASS.
- No-fake-DOI scan: PASS, no hits.
- Citation metadata consistency: PASS.
- DOI archive review package: PASS.
- Reproducibility capsule: PASS.

## boundary_check

Status: PASS.

This DOI capture preserves the project boundary:

- public validator archive only
- no PHI
- no raw DICOM files
- no private conformance suite material
- no private sample-validation service material
- no real samples
- no vendor private rules
- no hospital identifiers
- no non-de-identified DICOM material
- not clinical validation
- not regulatory approval
- not safety certification
- not legal compliance
- not production deployment
- not official FDO conformance

## citation_metadata_check

Status: PASS.

Current exact-version citation:

- Version: `v1.0.1-public`
- DOI: `10.5281/zenodo.20635229`
- Zenodo record: https://zenodo.org/records/20635229
- GitHub Release: https://github.com/joy7758/udi-dicom-evidence-validator/releases/tag/v1.0.1-public
- Target commit: `37fdedfc0b6edfbb07432148d1b738f2712a7c8d`
- Archive checksum: `md5:f031e65ee9c3c4a0fd62140b2d5b83c2`

Software-series citation:

- Concept DOI: `10.5281/zenodo.20540531`

Historical DOI:

- `10.5281/zenodo.20540532` remains the historical version DOI for
  `v0.8.1-public`.

## release_and_tag_check

- `no_new_release_created`: true
- `no_tag_created`: true

This branch starts from the existing `v1.0.1-public` release commit. The DOI
capture commit records the already-existing archive and must remain an ordinary
commit, not a new GitHub Release.

## semantic_change_check

- `validator_behavior_changed`: false
- `schema_changed`: false
- `cli_api_changed`: false
- `public_example_semantics_changed`: false
- `receipt_semantics_changed`: false
- `dicom_extraction_logic_changed`: false
- `registry_validation_logic_changed`: false
