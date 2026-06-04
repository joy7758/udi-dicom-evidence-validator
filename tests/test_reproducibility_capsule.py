from __future__ import annotations

import json
import subprocess
import sys

from tests.conftest import ROOT


def test_reproducibility_capsule_build_and_check() -> None:
    build = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "build_reproducibility_capsule.py")],
        check=True,
        capture_output=True,
        text=True,
    )
    build_payload = json.loads(build.stdout)
    assert build_payload["public_only"] is True
    assert build_payload["golden_checked"] >= 9

    check = subprocess.run(
        [
            sys.executable,
            str(ROOT / "scripts" / "check_reproducibility_capsule.py"),
            "artifacts/reproducibility-capsule-v0.5",
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    check_payload = json.loads(check.stdout)
    assert check_payload["ok"] is True
