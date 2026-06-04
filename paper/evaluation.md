# Evaluation

Evaluation is synthetic and reproducibility-oriented. The public matrix covers
passing fixtures and isolated failure cases including missing UDI, registry
unresolved, SOP Instance UID mismatch, and Device UID used as UDI-DI.

The evaluation chain is:

1. Generate golden receipts from public examples.
2. Check golden receipts against current validator behavior.
3. Build the public evaluation matrix.
4. Build public release assets.
5. Build and check the reproducibility capsule.

This evaluates software determinism and public boundary behavior. It is not a
clinical study, not regulatory review, and not certification.

