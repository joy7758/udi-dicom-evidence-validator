# Reproduction Commands v0.6

| Command | Expected |
| --- | --- |
| `python scripts/generate_golden_receipts.py` | exit code 0 |
| `python scripts/check_golden_receipts.py` | exit code 0 |
| `python scripts/build_public_evaluation_matrix.py` | exit code 0 |
| `python scripts/build_public_release_assets.py` | exit code 0 |
| `python scripts/build_reproducibility_capsule.py` | exit code 0 |
| `python scripts/check_reproducibility_capsule.py artifacts/reproducibility-capsule-v0.5` | exit code 0 |
| `python scripts/build_archive_metadata_report.py` | exit code 0 |
| `python scripts/check_archive_metadata_report.py artifacts/archive-metadata-report-v0.6.json` | exit code 0 |
| `python scripts/build_paper_submission_package.py` | exit code 0 |
| `python scripts/check_paper_submission_package.py artifacts/paper-submission-v0.6` | exit code 0 |
| `pytest -q` | exit code 0 |
| `ruff check .` | exit code 0 |
| `mypy src` | exit code 0 |
