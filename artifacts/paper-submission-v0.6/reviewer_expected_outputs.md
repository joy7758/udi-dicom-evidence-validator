# Reviewer Expected Outputs v0.6

- `artifacts/public_evaluation_matrix.json` with `row_count >= 9`.
- `artifacts/reproducibility-capsule-v0.5/` with checksum file.
- `artifacts/archive-metadata-report-v0.6.json` with `doi_ready=true` and no assigned DOI.
- `artifacts/paper-submission-v0.6/package_manifest.json` with public-safe sources only.
- `pytest -q`, `ruff check .`, and `mypy src` pass.

Boundary: synthetic public examples only; no PHI; no raw DICOM; not clinical validation; not regulatory approval; not certification.
