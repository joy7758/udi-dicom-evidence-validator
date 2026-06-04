from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FILES = {
    "environment_summary.json",
    "command_log_template.md",
    "public_evaluation_matrix.json",
    "golden_receipt_summary.json",
    "demo_summary.json",
    "release_asset_manifest.json",
    "SHA256SUMS.txt",
}
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


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def check_checksums(capsule: Path) -> list[str]:
    failures: list[str] = []
    checksum_path = capsule / "SHA256SUMS.txt"
    for line in checksum_path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        digest, relative = line.split("  ", 1)
        path = capsule / relative
        if not path.exists():
            failures.append(f"missing checksum target: {relative}")
            continue
        if sha256(path) != digest:
            failures.append(f"checksum mismatch: {relative}")
    return failures


def check_public_boundary(capsule: Path) -> list[str]:
    failures: list[str] = []
    for path in sorted(capsule.rglob("*")):
        if not path.is_file():
            continue
        lower_path = str(path.relative_to(capsule)).lower()
        if path.suffix.lower() in FORBIDDEN_EXTENSIONS:
            failures.append(f"raw DICOM extension: {path.relative_to(capsule)}")
        if any(marker in lower_path for marker in FORBIDDEN_PATH_MARKERS):
            failures.append(f"private path marker: {path.relative_to(capsule)}")
        if path.suffix.lower() in {".json", ".md", ".txt"}:
            text = path.read_text(encoding="utf-8").lower()
            for marker in FORBIDDEN_PATH_MARKERS:
                if marker in text:
                    failures.append(f"private text marker {marker}: {path.relative_to(capsule)}")
    return failures


def main() -> None:
    default_capsule = ROOT / "artifacts" / "reproducibility-capsule-v0.5"
    capsule = Path(sys.argv[1]) if len(sys.argv) > 1 else default_capsule
    if not capsule.is_absolute():
        capsule = ROOT / capsule
    missing = sorted(name for name in REQUIRED_FILES if not (capsule / name).exists())
    failures = [f"missing required file: {name}" for name in missing]
    if not missing:
        environment = load_json(capsule / "environment_summary.json")
        golden = load_json(capsule / "golden_receipt_summary.json")
        demo = load_json(capsule / "demo_summary.json")
        matrix = load_json(capsule / "public_evaluation_matrix.json")
        release_manifest = load_json(capsule / "release_asset_manifest.json")
        if environment.get("public_only") is not True:
            failures.append("environment_summary public_only is not true")
        if environment.get("raw_dicom_included") is not False:
            failures.append("environment_summary raw_dicom_included is not false")
        if golden.get("ok") is not True or golden.get("checked", 0) < 9:
            failures.append("golden receipt summary is not passing")
        if demo.get("ok") is not True:
            failures.append("demo summary is not passing")
        if matrix.get("row_count", 0) < 9:
            failures.append("public evaluation matrix has too few rows")
        if release_manifest.get("public_only") is not True:
            failures.append("release asset manifest is not public-only")
        failures.extend(check_checksums(capsule))
        failures.extend(check_public_boundary(capsule))
    result = {"ok": not failures, "failures": failures, "capsule": str(capsule.relative_to(ROOT))}
    print(json.dumps(result, sort_keys=True))
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
