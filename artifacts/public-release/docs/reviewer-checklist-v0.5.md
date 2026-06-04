# Reviewer Checklist v0.5

| Check | Expected |
| --- | --- |
| Public examples are synthetic | Yes |
| Raw DICOM files are absent | Yes |
| PHI is absent | Yes |
| Golden receipts pass | `ok=true` |
| Public evaluation matrix builds | `row_count >= 9` |
| Public release assets build | `public_only=true` |
| Reproducibility capsule checks | `ok=true` |
| Device UID is not UDI-DI | Explicitly stated |
| Offline fixture first | Explicitly stated |
| Live openFDA opt-in | Explicitly stated |
| FDO-style mapping boundary | Metadata mapping only |
| Medical robot operation evidence | Not included |

Review decision options: pass, pass with notes, or block with reproducible
failure details.

