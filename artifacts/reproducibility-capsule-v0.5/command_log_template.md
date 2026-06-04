# Reproducibility Command Log Template

Record the command, exit code, and reviewer notes for public-safe checks.
The capsule contains synthetic examples only and is not clinical validation, not regulatory approval, and not certification.

| Command | Exit Code | Reviewer Notes |
| --- | --- | --- |
| `python scripts/generate_golden_receipts.py` |  |  |
| `python scripts/check_golden_receipts.py` |  |  |
| `python scripts/build_public_evaluation_matrix.py` |  |  |
| `python scripts/build_public_release_assets.py` |  |  |
| `python demo/portable-ultrasound/run_demo.py` |  |  |
| `python scripts/build_reproducibility_capsule.py` |  |  |
| `python scripts/check_reproducibility_capsule.py artifacts/reproducibility-capsule-v0.5` |  |  |
| `pytest -q` |  |  |
| `ruff check .` |  |  |
| `mypy src` |  |  |
