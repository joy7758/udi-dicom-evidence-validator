# Reviewer Expected Outputs v0.5

Expected generated paths:

- `tests/golden/v0.1/*.receipt.json`
- `tests/golden/v0.2/*.receipt.json`
- `artifacts/public_evaluation_matrix.json`
- `artifacts/public-release/public-release-summary.json`
- `artifacts/reproducibility-capsule-v0.5/environment_summary.json`
- `artifacts/reproducibility-capsule-v0.5/golden_receipt_summary.json`
- `artifacts/reproducibility-capsule-v0.5/demo_summary.json`
- `artifacts/reproducibility-capsule-v0.5/release_asset_manifest.json`
- `artifacts/reproducibility-capsule-v0.5/SHA256SUMS.txt`

Expected status fields:

- Golden receipt check: `ok=true`.
- Public release summary: `public_only=true`, `raw_dicom_included=false`,
  `private_repo_assets_included=false`.
- Reproducibility capsule check: `ok=true`.

