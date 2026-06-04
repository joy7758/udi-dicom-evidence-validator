# Reviewer Quickstart v0.5

Create a local environment and run the public checks:

```bash
python -m venv .venv
. .venv/bin/activate
python -m pip install -U pip
pip install -e '.[dev,api]'
python scripts/generate_golden_receipts.py
python scripts/check_golden_receipts.py
python scripts/build_public_evaluation_matrix.py
python scripts/build_public_release_assets.py
python scripts/build_reproducibility_capsule.py
python scripts/check_reproducibility_capsule.py artifacts/reproducibility-capsule-v0.5
pytest -q
ruff check .
mypy src
```

Expected result: all commands exit with code 0. Reviewers should not need
network access because offline registry fixtures are the default. Live openFDA
lookup is explicit opt-in and is outside the required reproduction path.

