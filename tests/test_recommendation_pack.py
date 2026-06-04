from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_recommendation_pack_check_passes() -> None:
    result = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "check_recommendation_pack.py")],
        check=True,
        capture_output=True,
        text=True,
    )
    payload = json.loads(result.stdout.splitlines()[0])
    assert payload["ok"] is True
    assert payload["status"] == "RECOMMENDATION_PACK_CHECK_PASS"
    assert payload["missing_files"] == []
    assert payload["missing_terms"] == []
    assert payload["forbidden_hits"] == []
