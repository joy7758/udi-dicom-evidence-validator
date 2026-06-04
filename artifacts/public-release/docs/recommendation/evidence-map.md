# Evidence Map

## Public Evidence Chain

| Evidence item | Location | Purpose |
| --- | --- | --- |
| Public repository | https://github.com/joy7758/udi-dicom-evidence-validator | Source, docs, scripts, tests, examples |
| Verified Zenodo DOI | https://doi.org/10.5281/zenodo.20540532 | Public archive citation |
| Zenodo record | https://zenodo.org/records/20540532 | Public release archive record |
| Paper DOI | https://doi.org/10.1007/s10278-026-02019-6 | Peer-reviewed paper citation |
| DOI capture record | `docs/doi-capture-record-v0.8.1.md` | Local record of verified Zenodo capture |
| Citation metadata | `CITATION.cff`, `codemeta.json`, `.zenodo.json` | Citation and archive metadata |
| Public examples | `examples/public/` | public synthetic examples |
| Demo | `demo/portable-ultrasound/` | Deterministic demo receipts and reports |
| Validation scripts | `scripts/check_*.py` | Reproducibility and boundary checks |
| Tests | `tests/` | Regression coverage |

## Reviewer Checklist

- Confirm the repository URL resolves.
- Confirm Zenodo DOI resolves to the expected public record.
- Confirm the paper DOI resolves to the paper record.
- Run `python scripts/check_no_fake_doi.py`.
- Run `python scripts/check_real_doi_record.py`.
- Run `python scripts/check_citation_metadata_consistency.py`.
- Run `python scripts/check_recommendation_pack.py`.
- Confirm no private suite/service material is included.

Boundary: no PHI, no raw DICOM, not clinical validation, not regulatory approval, not certification, public synthetic examples, Device UID != UDI-DI.
