# Agent Usage

Coding agents should keep schema, examples, validator, reports, and tests in
sync. Safe commands are `pytest -q`, `ruff check .`, and
`python demo/portable-ultrasound/run_demo.py`.

Forbidden edits include adding patient data, private suite cases, real hospital
samples, clinical or regulatory claims, vendor-private rules, or treating Device
UID as UDI-DI.


## v0.2 Notes

When editing v0.2, keep `synthetic_workflow_trace_id`, `provenance`, optional `fdo_mapping`, schema, examples, tests, CLI, and API behavior synchronized.
