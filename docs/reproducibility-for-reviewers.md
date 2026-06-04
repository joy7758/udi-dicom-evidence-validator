# Reproducibility For Reviewers

Use these commands from a clean checkout:

```bash
python -m venv .venv
. .venv/bin/activate
python -m pip install -U pip
python -m pip install -e '.[dev,api]'
pytest -q
python scripts/generate_golden_receipts.py
python scripts/check_golden_receipts.py
python scripts/build_public_evaluation_matrix.py
python scripts/build_public_release_assets.py
python demo/portable-ultrasound/run_demo.py
```

The expected public checks are deterministic. Receipt generation ignores
runtime-only timestamp fields when comparing golden receipts.

Interpretation boundary:

- Passing checks show public synthetic fixture consistency.
- Passing checks do not show clinical safety.
- Passing checks do not show regulatory approval.
- Passing checks do not show certification.
- Passing checks do not validate real patient data.
