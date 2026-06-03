# Reproducibility Checklist

- Run `python scripts/generate_golden_receipts.py`.
- Run `python scripts/check_golden_receipts.py`.
- Run `python scripts/build_public_evaluation_matrix.py`.
- Run `pytest -q`.
- Run `ruff check .`.
- Run `mypy src`.
- Run `python demo/portable-ultrasound/run_demo.py`.

All public examples must remain synthetic. Outputs are not clinical validation,
not regulatory approval, and not certification.
