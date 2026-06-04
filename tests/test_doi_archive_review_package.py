from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_doi_archive_review_package_build_and_check() -> None:
    build = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "build_doi_archive_review_package.py")],
        check=True,
        capture_output=True,
        text=True,
    )
    payload = json.loads(build.stdout)
    assert payload["doi_claimed"] is False
    assert payload["status"] == "DOI_ARCHIVE_READY_PENDING_ZENODO_ENABLEMENT"
    assert payload["no_fake_doi_scan_ok"] is True

    result = subprocess.run(
        [
            sys.executable,
            str(ROOT / "scripts" / "check_doi_archive_review_package.py"),
            "artifacts/doi-archive-review-v0.8",
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    checked = json.loads(result.stdout)
    assert checked["ok"] is True
