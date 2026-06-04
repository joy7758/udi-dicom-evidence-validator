# Citation Metadata Consistency v0.8

Run:

```bash
python scripts/check_citation_metadata_consistency.py
```

Outputs:

- `artifacts/citation-metadata-consistency-v0.8.json`
- `artifacts/citation-metadata-consistency-v0.8.md`

The gate checks:

- `CITATION.cff`
- `codemeta.json`
- `.zenodo.json`
- `pyproject.toml`
- README citation wording

Rules:

- version values must be present and explainable
- author/creator information must be consistent
- license must be consistent
- repository URL must be consistent
- DOI must not be fabricated
- missing DOI must be represented only as DOI pending

The public DOI scope is the public validator only.
