# Golden Receipt Regression

Golden receipt regression stores deterministic receipts for public synthetic
fixtures in `tests/golden/`.

Commands:

```bash
python scripts/generate_golden_receipts.py
python scripts/check_golden_receipts.py
```

The checker canonicalizes receipts before comparison and ignores `generated_at`
so future timestamp representation changes do not create false positives. The
current fixtures use deterministic offline registry timestamps.

This is a software regression harness only. It is not clinical validation,
regulatory approval, or certification.
