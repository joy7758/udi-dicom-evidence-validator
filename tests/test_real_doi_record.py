from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_real_doi_record() -> None:
    result = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "check_real_doi_record.py")],
        check=True,
        capture_output=True,
        text=True,
    )
    payload = json.loads(result.stdout)
    assert payload["ok"] is True
    assert payload["status"] == "REAL_DOI_VERIFIED"
    assert payload["doi"] == "10.5281/zenodo.20540532"
    assert payload["record_url"] == "https://zenodo.org/records/20540532"
