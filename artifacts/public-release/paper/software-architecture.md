# Software Architecture

The project is organized as a local Python package with a narrow public
callable surface.

- `src/udi_dicom_validator/checks.py` performs reference validation.
- `src/udi_dicom_validator/receipt.py` builds deterministic receipt metadata.
- `src/udi_dicom_validator/report.py` renders reviewer-facing Markdown.
- `src/udi_dicom_validator/cli.py` exposes local CLI commands.
- `src/udi_dicom_validator/api.py` exposes an optional validation-only API.
- `scripts/` contains public build and reproducibility helpers.
- `examples/public/` contains synthetic fixtures.
- `tests/golden/` contains stable receipt regression outputs.

The public repository does not contain private suite cases, private service
workflows, real sample data, PHI, or raw DICOM files.

