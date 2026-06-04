# Reproducibility

The v0.5 reproducibility capsule is built with:

```bash
python scripts/build_reproducibility_capsule.py
python scripts/check_reproducibility_capsule.py artifacts/reproducibility-capsule-v0.5
```

The capsule includes environment summary metadata, a command log template, the
public evaluation matrix, golden receipt summary, demo summary, release asset
manifest, and SHA-256 checksums.

Capsule contents are public-safe. They exclude private suite material, private
service workflows, raw DICOM files, PHI, real hospital identifiers, and real
customer data.

