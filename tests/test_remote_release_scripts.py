from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

from scripts.build_public_release_assets import OUT, assert_public_safe
from scripts.verify_remote_release import (
    is_public_safe_asset,
    normalize_repo_url,
    parse_ls_remote,
)
from tests.conftest import ROOT


def test_parse_ls_remote_refs() -> None:
    refs = parse_ls_remote(
        "abc123\trefs/heads/main\n"
        "def456\trefs/tags/v0.3.0-public\n"
        "fed789\trefs/tags/v0.3.0-public^{}\n"
    )
    assert refs["refs/heads/main"] == "abc123"
    assert refs["refs/tags/v0.3.0-public^{}"] == "fed789"


def test_public_asset_allowlist_rejects_private_markers() -> None:
    assert is_public_safe_asset("public_evaluation_matrix.json")
    assert not is_public_safe_asset("private-regression-baseline.json")
    assert not is_public_safe_asset("sample.dcm")


def test_normalize_repo_url_accepts_github_checkout_forms() -> None:
    assert (
        normalize_repo_url("https://github.com/joy7758/udi-dicom-evidence-validator.git")
        == "https://github.com/joy7758/udi-dicom-evidence-validator"
    )
    assert (
        normalize_repo_url("https://github.com/joy7758/udi-dicom-evidence-validator/")
        == "https://github.com/joy7758/udi-dicom-evidence-validator"
    )


def test_build_public_release_assets(tmp_path: Path) -> None:
    subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "build_public_release_assets.py")],
        check=True,
    )
    summary = json.loads((OUT / "public-release-summary.json").read_text(encoding="utf-8"))
    assert summary["public_only"] is True
    assert summary["raw_dicom_included"] is False
    assert (OUT / "SHA256SUMS.txt").exists()
    assert_public_safe(path for path in OUT.rglob("*") if path.is_file())
