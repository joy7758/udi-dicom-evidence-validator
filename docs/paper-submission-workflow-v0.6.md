# Paper Submission Workflow v0.6

Use the v0.6 workflow to prepare journal-neutral technical review material:

```bash
python scripts/build_archive_metadata_report.py
python scripts/check_archive_metadata_report.py artifacts/archive-metadata-report-v0.6.json
python scripts/build_paper_submission_package.py
python scripts/check_paper_submission_package.py artifacts/paper-submission-v0.6
```

The workflow prepares a paper submission package and DOI-ready metadata report.
It does not submit to a journal and does not claim clinical validation,
regulatory approval, certification, or an assigned DOI.

