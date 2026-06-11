# Next Release Decision - 2026-06-11

agent_readable:
  decision_date: 2026-06-11
  repository: joy7758/udi-dicom-evidence-validator
  current_head: 21fe62667fee15c8dcaf192275590250dbf52f9b
  baseline_tag: v1.0.0-zenodo
  recommended_version: v1.0.1
  suggested_tag: v1.0.1-public
  release_type: patch
  validator_behavior_changed: false
  schema_changed: false
  cli_api_changed: false
  public_example_semantics_changed: false

## recommended_version

`v1.0.1`

## reason

Use a patch release because changes after `v1.0.0-zenodo` are documentation,
recommendation material, public artifact refreshes, release audit material, and
reproducibility notes. The public validator behavior remains unchanged.

Do not use `v1.1.0` unless a future branch intentionally changes schema fields,
validator checks, CLI/API behavior, receipt semantics, public example semantics,
or public validation semantics.

## release_blockers

None found for a documentation and release-hygiene patch.

Non-blocking metadata note:

- `pyproject.toml` package version is `0.2.0`.
- `CITATION.cff` and `codemeta.json` version fields are `0.4.0`.
- The repository has later release tags through `v1.0.0-zenodo`.
- Current metadata checks pass and treat these as explainable version surfaces.
  A future metadata-only patch may align wording if the project decides that the
  citation/software metadata version should track public release tags.

## exact pre-release commands

```bash
git status --short --branch
git diff --check
./.venv/bin/python -m pytest -q
./.venv/bin/python -m ruff check .
./.venv/bin/python demo/portable-ultrasound/run_demo.py
./.venv/bin/python scripts/check_no_fake_doi.py
./.venv/bin/python scripts/check_citation_metadata_consistency.py
./.venv/bin/python scripts/check_doi_archive_review_package.py artifacts/doi-archive-review-v0.8
./.venv/bin/python scripts/check_reproducibility_capsule.py artifacts/reproducibility-capsule-v0.5
./.venv/bin/python scripts/verify_remote_release.py
./.venv/bin/python scripts/clean_clone_smoke.py
```

## exact post-release human checklist

- Confirm the release title and notes say public validator archive only.
- Confirm release notes keep the boundary: no PHI, no raw DICOM, not clinical
  validation, not regulatory approval, not certification, Device UID != UDI-DI.
- Confirm no private conformance suite, private service workflow, real sample,
  vendor private rule, hospital identifier, or non-de-identified DICOM material
  is attached.
- Confirm the release is a patch release for docs, audit, recommendation, and
  reproducibility material only.
- Confirm the Zenodo record remains scoped to the public validator archive.
- Do not describe the patch release as a new clinical, regulatory, safety,
  certification, official FDO, API, or validator-behavior milestone.
