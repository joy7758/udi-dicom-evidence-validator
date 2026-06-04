from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_archive_metadata_report_build_and_check() -> None:
    build = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "build_archive_metadata_report.py")],
        check=True,
        capture_output=True,
        text=True,
    )
    payload = json.loads(build.stdout)
    assert payload["doi_ready"] is True
    result = subprocess.run(
        [
            sys.executable,
            str(ROOT / "scripts" / "check_archive_metadata_report.py"),
            "artifacts/archive-metadata-report-v0.6.json",
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    checked = json.loads(result.stdout)
    assert checked["ok"] is True

