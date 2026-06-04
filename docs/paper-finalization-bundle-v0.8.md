# Paper Finalization Bundle v0.8

Build:

```bash
python scripts/build_paper_finalization_bundle.py
python scripts/check_paper_finalization_bundle.py artifacts/paper-finalization-bundle-v0.8
```

Output directory: `artifacts/paper-finalization-bundle-v0.8/`

Generated files:

- `manuscript_sections_index.md`
- `finalization_checklist.md`
- `reviewer_command_sheet.md`
- `reproducibility_summary.md`
- `citation_metadata_status.md`
- `limitations_boundary_check.md`
- `missing_manual_items.md`
- `SHA256SUMS.txt`

Manual items are intentionally left explicit: title, target journal, final
abstract, reference verification, figure rendering, and DOI insertion after a
real Zenodo record exists.

This bundle is public-only and synthetic-only. It does not include private
suite material, private service material, PHI, raw DICOM, real hospital data,
clinical validation, regulatory approval, certification, or robot operation
evidence.
