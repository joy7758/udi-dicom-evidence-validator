from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "scripts"))

from generate_golden_receipts import iter_public_cases, receipt_name  # noqa: E402

from udi_dicom_validator.checks import validate_files  # noqa: E402

IGNORED_FIELDS = {"generated_at"}


def canonicalize(value: Any) -> Any:
    if isinstance(value, dict):
        return {
            key: canonicalize(val)
            for key, val in sorted(value.items())
            if key not in IGNORED_FIELDS
        }
    if isinstance(value, list):
        return [canonicalize(item) for item in value]
    return value


def main() -> None:
    mismatches: list[dict[str, str]] = []
    checked = 0
    for version, manifest, dicom_metadata, registry in iter_public_cases():
        golden_path = ROOT / "tests" / "golden" / version / receipt_name(manifest)
        if not golden_path.exists():
            mismatches.append({"case": manifest.name, "reason": "missing_golden"})
            continue
        expected = canonicalize(json.loads(golden_path.read_text(encoding="utf-8")))
        actual = canonicalize(validate_files(manifest, dicom_metadata, registry))
        if expected != actual:
            mismatches.append({"case": manifest.name, "reason": "receipt_mismatch"})
        checked += 1
    result = {"checked": checked, "mismatches": mismatches, "ok": not mismatches}
    print(json.dumps(result, sort_keys=True))
    if mismatches:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
