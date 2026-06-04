# Reviewer Command Sheet v0.8

```bash
python -m venv .venv
. .venv/bin/activate
python -m pip install -e ".[dev,api]"
python scripts/generate_golden_receipts.py
python scripts/check_golden_receipts.py
python scripts/build_public_evaluation_matrix.py
python scripts/build_reproducibility_capsule.py
python scripts/check_reproducibility_capsule.py artifacts/reproducibility-capsule-v0.5
python scripts/build_doi_archive_review_package.py
python scripts/check_doi_archive_review_package.py artifacts/doi-archive-review-v0.8
python scripts/build_paper_finalization_bundle.py
python scripts/check_paper_finalization_bundle.py artifacts/paper-finalization-bundle-v0.8
pytest -q
```
