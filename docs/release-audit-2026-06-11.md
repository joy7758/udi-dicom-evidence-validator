# Release Audit - 2026-06-11

agent_readable:
  repo: joy7758/udi-dicom-evidence-validator
  local_path: /Users/zhangbin/projects/udi-dicom-evidence/udi-dicom-evidence-validator
  audit_date: 2026-06-11
  status: PUBLIC_RELEASE_READINESS_PASS_WITH_METADATA_NOTES
  recommended_next_release: v1.0.1
  scope_change: false
  validator_behavior_changed: false
  schema_changed: false
  cli_api_changed: false

## Scope

This audit checks the existing public UDI-DICOM evidence validator repository.
It does not rebuild the project, does not expand scope, and does not add
clinical, regulatory, safety, certification, raw DICOM, real-sample, private
suite, private service, or robot-operation claims.

## Repository State

- Branch: `main`
- HEAD: `21fe62667fee15c8dcaf192275590250dbf52f9b`
- Remote: `https://github.com/joy7758/udi-dicom-evidence-validator.git`
- Remote main check: local `origin/main` matched remote `main`.
- Existing release tag observed locally: `v1.0.0-zenodo`
- Post-`v1.0.0-zenodo` changes on `main`: recommendation docs, public release
  artifact refresh, public total-plan link, and reproducibility status note.

## commands_run

| Command | Result | Evidence |
| --- | --- | --- |
| `./.venv/bin/python -m pip install -e '.[dev,api]'` | PASS | Editable package installed as `udi-dicom-evidence-validator==0.2.0`. |
| `./.venv/bin/python -m pytest -q` | PASS | `35 passed`. |
| `./.venv/bin/python -m ruff check .` | PASS | `All checks passed!` |
| `./.venv/bin/python demo/portable-ultrasound/run_demo.py` | PASS | `PASS manifest_id=synthetic-portable-ultrasound-v02-pass-001 checks=6`. |
| `./.venv/bin/python scripts/check_no_fake_doi.py` | PASS | `ok=true`, `files_checked=128`, no hits. |
| `./.venv/bin/python scripts/check_citation_metadata_consistency.py` | PASS | `ok=true`, output `artifacts/citation-metadata-consistency-v0.8.json`. |
| `./.venv/bin/python scripts/verify_remote_release.py` | PASS | Origin, remote main, tags, and release assets matched expected public state. |
| `./.venv/bin/python scripts/clean_clone_smoke.py` | PASS | Fresh clone from GitHub installed, ran tests, golden receipt check, public matrix build, and demo. |
| `find . \( -path './.git' -o -path './.venv' \) -prune -o \( -iname '*.[d]cm' -o -iname '*.[d]icom' \) -print` | PASS | No tracked workspace raw DICOM files found outside `.venv`. |
| `./.venv/bin/python scripts/check_doi_archive_review_package.py artifacts/doi-archive-review-v0.8` | PASS | `ok=true`, no failures. |
| `./.venv/bin/python scripts/check_reproducibility_capsule.py artifacts/reproducibility-capsule-v0.5` | PASS | `ok=true`, no failures. |

## pass_fail_summary

- Code and test readiness: PASS.
- Demo readiness: PASS.
- Remote public release check: PASS.
- Clean-clone reproducibility: PASS.
- DOI and citation gate: PASS.
- Boundary check: PASS.
- Version metadata note: REVIEW_NEEDED_NOT_BLOCKING. `pyproject.toml` reports
  `0.2.0`, while `CITATION.cff` and `codemeta.json` report `0.4.0`, and the
  repository has later public release tags. The current citation consistency
  gate treats these as explainable version surfaces, not as a failing condition.

## changed_files

Files created or refreshed by this audit pass:

- `docs/release-audit-2026-06-11.md`
- `release/next-release-decision-2026-06-11.md`
- `docs/external-review-10min.md`
- `docs/outreach/reviewer-email-cn.md`
- `docs/outreach/vendor-email-cn.md`
- `docs/outreach/hospital-it-email-cn.md`
- `docs/outreach/sample-request-boundary-cn.md`
- `artifacts/doi-archive-review-v0.8/no_fake_doi_scan.json`
- `artifacts/doi-archive-review-v0.8/SHA256SUMS.txt`
- `artifacts/reproducibility-capsule-v0.5/environment_summary.json`
- `artifacts/reproducibility-capsule-v0.5/SHA256SUMS.txt`

The DOI archive review files changed because the generated no-fake-DOI scan now
sees the newly added docs and release decision. Its embedded package scan
reports `files_checked=122`, `hits=[]`, `ok=true`.

The two reproducibility capsule files changed only because the local platform
summary moved from `macOS-26.5` to `macOS-26.5.1`; no validator behavior,
schema behavior, public examples, CLI behavior, API behavior, or receipt
semantics changed.

## boundary_check

Status: PASS.

Evidence:

- Root `AGENTS.md` prohibits clinical validation, regulatory approval, safety
  assurance, certification, legal non-repudiation, real patient data, raw DICOM
  files, vendor private rules, and private suite exposure.
- Public examples remain JSON fixtures and are described as synthetic.
- The no-fake-DOI scan returned `ok=true` with no hits.
- Boundary phrase scan found explicit refusal language and no upgraded claims
  such as completed clinical validation, granted regulatory approval, granted
  certification, or official FDO conformance.
- DICOM `Device UID (0018,1002)` remains documented as distinct from UDI-DI.
- The public repository scan found no raw DICOM files outside dependency
  packages in `.venv`.

## citation_doi_check

Status: PASS_WITH_VERSION_NOTE.

Verified public archive evidence:

- Zenodo DOI: `10.5281/zenodo.20540532`
- Zenodo record: https://zenodo.org/records/20540532
- Local capture file: `artifacts/doi-capture-v0.8.1/doi-capture-summary.json`
- Capture status constant: `REAL_DOI_VERIFIED`

Citation metadata consistency output:

- `ok`: `true`
- `verified_doi`: `10.5281/zenodo.20540532`
- `zenodo_record_url`: `https://zenodo.org/records/20540532`
- `claimed_or_placeholder_dois`: `[]`
- `version_values`: `pyproject=0.2.0`, `citation_cff=0.4.0`,
  `codemeta=0.4.0`

The DOI scope remains the public validator archive only. It excludes private
conformance suite material, private sample validation service material, real
samples, PHI, and raw DICOM files.

## next_release_recommendation

Recommended version: `v1.0.1`.

Reason:

- Current post-`v1.0.0-zenodo` changes are release hygiene, documentation,
  recommendation material, reproducibility status, and generated public artifact
  refreshes.
- No schema fields, validator behavior, CLI behavior, API behavior, public
  example semantics, receipt semantics, or UDI-DICOM profile semantics changed.
- A `v1.1.0` release would be appropriate only after a deliberate behavior,
  schema, API, CLI, or public validation semantics change.

Release blockers: none found for a documentation and release-hygiene patch.

Pre-release commands:

```bash
./.venv/bin/python -m pytest -q
./.venv/bin/python -m ruff check .
./.venv/bin/python demo/portable-ultrasound/run_demo.py
./.venv/bin/python scripts/check_no_fake_doi.py
./.venv/bin/python scripts/check_citation_metadata_consistency.py
./.venv/bin/python scripts/verify_remote_release.py
./.venv/bin/python scripts/clean_clone_smoke.py
```

## patch_summary

This pass adds release audit and external review documentation only. It does not
change validator logic, schema files, public examples, API behavior, CLI
behavior, or release DOI metadata.

## final_commands_run

Final validation was re-run after these files were created:

```bash
./.venv/bin/python -m pytest -q
./.venv/bin/python -m ruff check .
./.venv/bin/python demo/portable-ultrasound/run_demo.py
./.venv/bin/python scripts/check_no_fake_doi.py
./.venv/bin/python scripts/check_citation_metadata_consistency.py
./.venv/bin/python scripts/check_doi_archive_review_package.py artifacts/doi-archive-review-v0.8
./.venv/bin/python scripts/check_reproducibility_capsule.py artifacts/reproducibility-capsule-v0.5
```

## final_status

PASS.

- `pytest -q`: 35 tests passed.
- `ruff check .`: all checks passed.
- Demo: `PASS manifest_id=synthetic-portable-ultrasound-v02-pass-001 checks=6`.
- No-fake-DOI scan: `ok=true`, `files_checked=128`, no hits.
- Citation metadata consistency: `ok=true`.
- DOI archive review package check: `ok=true`.
- Reproducibility capsule check: `ok=true`.
