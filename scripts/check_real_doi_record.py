from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
SUMMARY = ROOT / "artifacts" / "doi-capture-v0.8.1" / "doi-capture-summary.json"
DOI_PATTERN = re.compile(r"^10\.\d{4,9}/[-._;()/:A-Za-z0-9]+$")
RECORD_URL_PATTERN = re.compile(r"^https://(www\.)?zenodo\.org/records/\d+$")

REQUIRED_TEXT_FILES = [
    ROOT / "README.md",
    ROOT / "CITATION.cff",
    ROOT / "codemeta.json",
    ROOT / ".zenodo.json",
    ROOT / "docs" / "citation-and-archiving.md",
    ROOT / "docs" / "doi-archive-review-v0.8.md",
    ROOT / "docs" / "doi-capture-record-v0.8.1.md",
    ROOT / "release" / "v0.8.0-doi-readiness.md",
]


def load_summary() -> dict[str, Any]:
    if not SUMMARY.exists():
        raise SystemExit("BLOCKED_DOI_CAPTURE_SUMMARY_MISSING")
    data = json.loads(SUMMARY.read_text(encoding="utf-8"))
    doi = data.get("doi", "")
    record_url = data.get("record_url", "")
    if not DOI_PATTERN.match(doi):
        raise SystemExit("BLOCKED_INVALID_DOI_FORMAT")
    if not RECORD_URL_PATTERN.match(record_url):
        raise SystemExit("BLOCKED_INVALID_ZENODO_RECORD_URL")
    if data.get("status") != "REAL_DOI_VERIFIED":
        raise SystemExit("BLOCKED_DOI_STATUS_NOT_VERIFIED")
    verification = data.get("verification", {})
    required_verification = {
        "zenodo_settings_page_visible_doi",
        "record_page_contains_doi",
        "record_page_contains_v0_8_1_release_text",
    }
    for key in sorted(required_verification):
        if verification.get(key) is not True:
            raise SystemExit(f"BLOCKED_VERIFICATION_FLAG_FALSE:{key}")
    boundary = data.get("boundary", {})
    for key in [
        "public_only_archive",
        "private_suite_excluded",
        "private_service_excluded",
        "no_phi",
        "no_raw_dicom",
        "not_clinical_validation",
        "not_regulatory_approval",
        "not_certification",
        "no_fake_doi",
        "device_uid_not_udi_di",
    ]:
        if boundary.get(key) is not True:
            raise SystemExit(f"BLOCKED_BOUNDARY_FLAG_FALSE:{key}")
    return data


def main() -> None:
    data = load_summary()
    doi = data["doi"]
    record_url = data["record_url"]
    missing: list[str] = []
    for path in REQUIRED_TEXT_FILES:
        text = path.read_text(encoding="utf-8")
        if doi not in text:
            missing.append(f"{path.relative_to(ROOT)}:doi")
        if record_url not in text:
            missing.append(f"{path.relative_to(ROOT)}:record_url")
    if missing:
        raise SystemExit("BLOCKED_DOI_NOT_PROPAGATED:" + ",".join(missing))
    print(
        json.dumps(
            {
                "ok": True,
                "status": "REAL_DOI_VERIFIED",
                "doi": doi,
                "record_url": record_url,
                "summary": str(SUMMARY.relative_to(ROOT)),
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
