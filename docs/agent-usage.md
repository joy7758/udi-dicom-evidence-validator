# Agent Usage

Coding agents should keep schema, examples, validator, reports, and tests in
sync. Safe commands are `pytest -q`, `ruff check .`, and
`python demo/portable-ultrasound/run_demo.py`.

Forbidden edits include adding patient data, private suite cases, real hospital
samples, clinical or regulatory claims, vendor-private rules, or treating Device
UID as UDI-DI.


## v0.2 Notes

When editing v0.2, keep `synthetic_workflow_trace_id`, `provenance`, optional `fdo_mapping`, schema, examples, tests, CLI, and API behavior synchronized.

## v0.4 Notes

Release hardening agents should use `scripts/verify_remote_release.py`,
`scripts/clean_clone_smoke.py`, and `scripts/build_public_release_assets.py`.
The public asset builder must remain public-only and must not include private
suite, private service, raw DICOM, PHI, or real sample materials. External
review docs must keep the reference-validator boundary: not clinical validation,
not regulatory approval, and not certification.

## v0.5 Notes

Paper review agents should treat `paper/`, `docs/external-review-pack-v0.5.md`,
and `artifacts/reproducibility-capsule-v0.5/` as public reviewer material only.
Run `scripts/build_reproducibility_capsule.py` and
`scripts/check_reproducibility_capsule.py`. Do not add real samples, private
cases, raw DICOM files, PHI, robot operation evidence, or official FDO
implementation claims.
