# Receipt Explainer

A validation receipt records:

- Whether the manifest passed.
- The deterministic primary error code, if any.
- Ordered check results.
- Manifest id and profile version.
- Optional v0.2 trace id and provenance metadata.

Receipts are designed for software review and regression comparison. They are
not clinical records, regulatory certificates, or safety attestations.

