from __future__ import annotations

import hashlib
import json
import platform
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "artifacts" / "reproducibility-capsule-v0.5"
PUBLIC_RELEASE = ROOT / "artifacts" / "public-release"
FORBIDDEN_PATH_MARKERS = {
    "udi-dicom-conformance-suite-private",
    "udi-dicom-sample-validation-service-private",
    "cases/private",
}
FORBIDDEN_EXTENSIONS = {".dcm", ".dicom"}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def run_json(command: list[str]) -> dict[str, Any]:
    result = subprocess.run(command, check=True, capture_output=True, text=True)
    lines = [line for line in result.stdout.splitlines() if line.strip()]
    return json.loads(lines[-1])


def run_text(command: list[str]) -> str:
    result = subprocess.run(command, check=True, capture_output=True, text=True)
    return result.stdout.strip()


def assert_public_safe(paths: list[Path]) -> None:
    for path in paths:
        lower = str(path.relative_to(ROOT)).lower()
        if path.suffix.lower() in FORBIDDEN_EXTENSIONS:
            raise RuntimeError(f"raw DICOM asset blocked from capsule: {path}")
        if any(marker in lower for marker in FORBIDDEN_PATH_MARKERS):
            raise RuntimeError(f"private marker blocked from capsule: {path}")


def build_environment_summary() -> dict[str, Any]:
    return {
        "python": sys.version.split()[0],
        "platform": platform.platform(),
        "repository": "udi-dicom-evidence-validator",
        "capsule_version": "v0.5",
        "public_only": True,
        "raw_dicom_included": False,
        "private_material_included": False,
    }


def build_command_log_template() -> str:
    commands = [
        "python scripts/generate_golden_receipts.py",
        "python scripts/check_golden_receipts.py",
        "python scripts/build_public_evaluation_matrix.py",
        "python scripts/build_public_release_assets.py",
        "python demo/portable-ultrasound/run_demo.py",
        "python scripts/build_reproducibility_capsule.py",
        "python scripts/check_reproducibility_capsule.py artifacts/reproducibility-capsule-v0.5",
        "pytest -q",
        "ruff check .",
        "mypy src",
    ]
    lines = [
        "# Reproducibility Command Log Template",
        "",
        "Record the command, exit code, and reviewer notes for public-safe checks.",
        "The capsule contains synthetic examples only and is not clinical validation, "
        "not regulatory approval, and not certification.",
        "",
        "| Command | Exit Code | Reviewer Notes |",
        "| --- | --- | --- |",
    ]
    lines.extend(f"| `{command}` |  |  |" for command in commands)
    lines.append("")
    return "\n".join(lines)


def build_release_asset_manifest() -> dict[str, Any]:
    assets: list[dict[str, Any]] = []
    if PUBLIC_RELEASE.exists():
        for path in sorted(PUBLIC_RELEASE.rglob("*")):
            if path.is_file():
                assets.append(
                    {
                        "path": str(path.relative_to(ROOT)),
                        "bytes": path.stat().st_size,
                        "sha256": sha256(path),
                    }
                )
    return {
        "asset_count": len(assets),
        "public_release_dir": str(PUBLIC_RELEASE.relative_to(ROOT)),
        "assets": assets,
        "public_only": True,
    }


def build_golden_receipt_summary(check_result: dict[str, Any]) -> dict[str, Any]:
    golden_files = sorted((ROOT / "tests" / "golden").rglob("*.json"))
    return {
        "checked": check_result["checked"],
        "ok": check_result["ok"],
        "mismatch_count": len(check_result["mismatches"]),
        "golden_receipt_count": len(golden_files),
        "golden_receipts": [str(path.relative_to(ROOT)) for path in golden_files],
    }


def build_demo_summary() -> dict[str, Any]:
    run_text([sys.executable, str(ROOT / "demo" / "portable-ultrasound" / "run_demo.py")])
    receipt_path = ROOT / "demo" / "portable-ultrasound" / "artifacts_v0.2" / "receipt.json"
    report_path = ROOT / "demo" / "portable-ultrasound" / "artifacts_v0.2" / "report.md"
    receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
    return {
        "ok": receipt["ok"],
        "manifest_id": receipt["manifest_id"],
        "check_count": len(receipt["checks"]),
        "receipt": str(receipt_path.relative_to(ROOT)),
        "report": str(report_path.relative_to(ROOT)),
        "profile_version": receipt.get("profile_version"),
    }


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> None:
    run_json([sys.executable, str(ROOT / "scripts" / "generate_golden_receipts.py")])
    golden_check = run_json([sys.executable, str(ROOT / "scripts" / "check_golden_receipts.py")])
    evaluation = run_json(
        [sys.executable, str(ROOT / "scripts" / "build_public_evaluation_matrix.py")]
    )
    run_json([sys.executable, str(ROOT / "scripts" / "build_public_release_assets.py")])

    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True, exist_ok=True)

    shutil.copy2(ROOT / "artifacts" / "public_evaluation_matrix.json", OUT)
    write_json(OUT / "environment_summary.json", build_environment_summary())
    (OUT / "command_log_template.md").write_text(build_command_log_template(), encoding="utf-8")
    write_json(OUT / "golden_receipt_summary.json", build_golden_receipt_summary(golden_check))
    write_json(OUT / "demo_summary.json", build_demo_summary())
    write_json(OUT / "release_asset_manifest.json", build_release_asset_manifest())

    files = sorted(path for path in OUT.rglob("*") if path.is_file())
    assert_public_safe(files)
    checksums = {str(path.relative_to(OUT)): sha256(path) for path in files}
    (OUT / "SHA256SUMS.txt").write_text(
        "".join(f"{digest}  {name}\n" for name, digest in sorted(checksums.items())),
        encoding="utf-8",
    )
    summary = {
        "output": str(OUT.relative_to(ROOT)),
        "public_only": True,
        "row_count": evaluation["row_count"],
        "golden_checked": golden_check["checked"],
        "capsule_file_count": len(files) + 1,
    }
    print(json.dumps(summary, sort_keys=True))


if __name__ == "__main__":
    main()
