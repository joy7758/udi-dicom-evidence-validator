from __future__ import annotations

import json
import subprocess
import sys

from tests.conftest import ROOT


def test_golden_receipts_are_stable() -> None:
    subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "generate_golden_receipts.py")],
        check=True,
    )
    result = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "check_golden_receipts.py")],
        check=True,
        capture_output=True,
        text=True,
    )
    payload = json.loads(result.stdout)
    assert payload["ok"] is True
    assert payload["checked"] >= 9
