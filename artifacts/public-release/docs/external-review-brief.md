# External Review Brief

This repository provides a public reference validator for synthetic UDI-DICOM
evidence manifest workflows. It helps reviewers inspect whether a manifest,
DICOM equipment metadata fixture, registry fixture, and generated receipt are
internally consistent.

Audience:

- peer reviewers evaluating reproducibility claims
- open source users checking the public validator boundary
- vendor technical staff reviewing synthetic example behavior

Boundary:

- This is a reference validator.
- It is not clinical validation.
- It is not regulatory approval.
- It is not certification.
- It does not replace PACS.
- It does not replace VNA.
- It does not process PHI.
- Public examples are synthetic.
- Device UID is not UDI-DI.
- Offline fixture first is the default strategy.
- Live openFDA access remains explicit opt-in.

Recommended review path:

1. Run `pytest -q`.
2. Run `python scripts/check_golden_receipts.py`.
3. Run `python scripts/build_public_evaluation_matrix.py`.
4. Run `python demo/portable-ultrasound/run_demo.py`.
5. Inspect `docs/public-evaluation-matrix.md` and `docs/boundary.md`.
