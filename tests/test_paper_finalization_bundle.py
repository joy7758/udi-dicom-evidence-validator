from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_paper_finalization_bundle_build_and_check() -> None:
    build = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "build_paper_finalization_bundle.py")],
        check=True,
        capture_output=True,
        text=True,
    )
    payload = json.loads(build.stdout)
    assert payload["doi_claimed"] is False
    assert payload["manual_item_count"] >= 6

    result = subprocess.run(
        [
            sys.executable,
            str(ROOT / "scripts" / "check_paper_finalization_bundle.py"),
            "artifacts/paper-finalization-bundle-v0.8",
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    checked = json.loads(result.stdout)
    assert checked["ok"] is True
