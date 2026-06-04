# Reviewer Reproduction Log Template

Reviewer:

Date:

Commit:

Environment:

| Command | Exit Code | Notes |
| --- | --- | --- |
| `python scripts/generate_golden_receipts.py` |  |  |
| `python scripts/check_golden_receipts.py` |  |  |
| `python scripts/build_public_evaluation_matrix.py` |  |  |
| `python scripts/build_public_release_assets.py` |  |  |
| `python scripts/build_reproducibility_capsule.py` |  |  |
| `python scripts/check_reproducibility_capsule.py artifacts/reproducibility-capsule-v0.5` |  |  |
| `pytest -q` |  |  |
| `ruff check .` |  |  |
| `mypy src` |  |  |

Boundary notes:

- Public examples synthetic:
- PHI absent:
- Raw DICOM absent:
- Device UID not UDI-DI:
- Offline fixture first:
- Live openFDA explicit opt-in:

