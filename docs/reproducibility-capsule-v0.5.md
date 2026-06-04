# Reproducibility Capsule v0.5

Build:

```bash
python scripts/build_reproducibility_capsule.py
```

Check:

```bash
python scripts/check_reproducibility_capsule.py artifacts/reproducibility-capsule-v0.5
```

Capsule files:

- `environment_summary.json`
- `command_log_template.md`
- `public_evaluation_matrix.json`
- `golden_receipt_summary.json`
- `demo_summary.json`
- `release_asset_manifest.json`
- `SHA256SUMS.txt`

The capsule is public-safe and synthetic-only. It contains no PHI, no raw DICOM
files, no private suite cases, and no private service workflows.

