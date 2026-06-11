from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_citation_metadata_consistency_gate() -> None:
    result = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "check_citation_metadata_consistency.py")],
        check=True,
        capture_output=True,
        text=True,
    )
    payload = json.loads(result.stdout)
    assert payload["ok"] is True

    report = json.loads(
        (ROOT / "artifacts" / "citation-metadata-consistency-v0.8.json").read_text(
            encoding="utf-8"
        )
    )
    assert report["doi_status"] == "DOI verified"
    assert report["verified_doi"] == "10.5281/zenodo.20635229"
    assert report["zenodo_record_url"] == "https://zenodo.org/records/20635229"
    assert report["claimed_or_placeholder_dois"] == []
