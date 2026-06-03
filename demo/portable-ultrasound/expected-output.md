# Expected Output

Inputs: synthetic DICOM metadata JSON, pass manifest, and resolved offline
registry fixture.

Outputs: `artifacts/receipt.json` and `artifacts/report.md`.

Five-minute demo: run the script, inspect the pass receipt, then show one fail
fixture through the CLI. This demo is not clinical validation, not regulatory
approval, and not a real hospital deployment.


## v0.2 Output

The demo now reads `examples/public/v0.2/manifest_v0.2.pass.json` and writes
`artifacts_v0.2/receipt.json` plus `artifacts_v0.2/report.md`. The output should
include a deterministic `trace_id` and provenance block.
