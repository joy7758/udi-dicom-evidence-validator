from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_paper_submission_package_build_and_check() -> None:
    build = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "build_paper_submission_package.py")],
        check=True,
        capture_output=True,
        text=True,
    )
    payload = json.loads(build.stdout)
    assert payload["public_only"] is True
    assert payload["doi_claimed"] is False
    result = subprocess.run(
        [
            sys.executable,
            str(ROOT / "scripts" / "check_paper_submission_package.py"),
            "artifacts/paper-submission-v0.6",
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    checked = json.loads(result.stdout)
    assert checked["ok"] is True
