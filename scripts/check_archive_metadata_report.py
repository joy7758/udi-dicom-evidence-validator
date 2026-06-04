from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOI_PATTERN = re.compile(r"^10\.\d{4,9}/[-._;()/:A-Za-z0-9]+$")
RECORD_URL_PATTERN = re.compile(r"^https://(www\.)?zenodo\.org/records/\d+$")


def main() -> None:
    default_target = ROOT / "artifacts" / "archive-metadata-report-v0.6.json"
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else default_target
    if not target.is_absolute():
        target = ROOT / target
    failures: list[str] = []
    if not target.exists():
        failures.append("missing_report_json")
    else:
        report = json.loads(target.read_text(encoding="utf-8"))
        if report.get("doi_ready") is not True:
            failures.append("doi_ready_not_true")
        doi_claimed = report.get("doi_claimed")
        assigned_doi = report.get("assigned_doi")
        record_url = report.get("zenodo_record_url")
        if doi_claimed is True:
            if not isinstance(assigned_doi, str) or not DOI_PATTERN.match(assigned_doi):
                failures.append("assigned_doi_invalid")
            if not isinstance(record_url, str) or not RECORD_URL_PATTERN.match(record_url):
                failures.append("zenodo_record_url_invalid")
        elif doi_claimed is False:
            if assigned_doi is not None:
                failures.append("assigned_doi_present_while_not_claimed")
            if record_url is not None:
                failures.append("zenodo_record_url_present_while_not_claimed")
        else:
            failures.append("doi_claimed_not_boolean")
        if report.get("unverified_dois") not in ([], None):
            failures.append("unverified_dois_present")
        checks = report.get("checks", {})
        for name, value in checks.items():
            if value is not True:
                failures.append(f"check_failed:{name}")
        boundary_text = " ".join(report.get("boundary", [])).lower()
        required_boundary = [
            "no phi",
            "no raw dicom",
            "not clinical validation",
            "not regulatory approval",
            "not certification",
        ]
        for phrase in required_boundary:
            if phrase not in boundary_text:
                failures.append(f"missing_boundary:{phrase}")
    result = {"ok": not failures, "failures": failures, "target": str(target.relative_to(ROOT))}
    print(json.dumps(result, sort_keys=True))
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
