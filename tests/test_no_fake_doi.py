from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_no_fake_doi_scan_passes_public_surfaces() -> None:
    subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "build_doi_archive_review_package.py")],
        check=True,
        capture_output=True,
        text=True,
    )
    result = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "check_no_fake_doi.py")],
        check=True,
        capture_output=True,
        text=True,
    )
    payload = json.loads(result.stdout)
    assert payload["ok"] is True
    assert payload["hits"] == []
