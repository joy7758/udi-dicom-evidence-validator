# Reproducibility Statement

The public reproduction path uses deterministic commands:

```bash
python scripts/generate_golden_receipts.py
python scripts/check_golden_receipts.py
python scripts/build_public_evaluation_matrix.py
python scripts/build_public_release_assets.py
python scripts/build_reproducibility_capsule.py
python scripts/check_reproducibility_capsule.py artifacts/reproducibility-capsule-v0.5
python scripts/build_archive_metadata_report.py
python scripts/check_archive_metadata_report.py artifacts/archive-metadata-report-v0.6.json
python scripts/build_paper_submission_package.py
python scripts/check_paper_submission_package.py artifacts/paper-submission-v0.6
pytest -q
ruff check .
mypy src
```

Offline registry fixtures are the default. Live openFDA access remains explicit
opt-in and is not required for the reproduction path.

