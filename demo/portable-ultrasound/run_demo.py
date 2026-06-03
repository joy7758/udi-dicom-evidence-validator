from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from udi_dicom_validator.checks import validate_files  # noqa: E402
from udi_dicom_validator.report import render_report  # noqa: E402


def main() -> None:
    examples = ROOT / "examples" / "public"
    artifacts = Path(__file__).resolve().parent / "artifacts"
    artifacts.mkdir(parents=True, exist_ok=True)
    receipt = validate_files(
        examples / "manifest.pass.json",
        examples / "sample_dicom_metadata.pass.json",
        examples / "registry.fixture.resolved.json",
    )
    (artifacts / "receipt.json").write_text(
        json.dumps(receipt, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    (artifacts / "report.md").write_text(render_report(receipt), encoding="utf-8")
    print(
        f"PASS manifest_id={receipt['manifest_id']} checks={len(receipt['checks'])} "
        f"report={artifacts / 'report.md'}"
    )


if __name__ == "__main__":
    main()
