from __future__ import annotations

import json
import subprocess
import sys

from tests.conftest import EXAMPLES


def test_cli_validate_and_render(tmp_path) -> None:
    out_dir = tmp_path / "out"
    subprocess.run(
        [
            sys.executable,
            "-m",
            "udi_dicom_validator.cli",
            "validate-manifest",
            "--manifest",
            str(EXAMPLES / "manifest.pass.json"),
            "--dicom-metadata",
            str(EXAMPLES / "sample_dicom_metadata.pass.json"),
            "--registry-fixture",
            str(EXAMPLES / "registry.fixture.resolved.json"),
            "--out-dir",
            str(out_dir),
        ],
        check=True,
    )
    receipt_path = out_dir / "receipt.json"
    assert json.loads(receipt_path.read_text())["ok"] is True
    report_path = tmp_path / "report.md"
    subprocess.run(
        [
            sys.executable,
            "-m",
            "udi_dicom_validator.cli",
            "render-report",
            "--receipt",
            str(receipt_path),
            "--out",
            str(report_path),
        ],
        check=True,
    )
    assert report_path.exists()
