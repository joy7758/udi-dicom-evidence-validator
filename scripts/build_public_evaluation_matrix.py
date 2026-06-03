from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "scripts"))

from generate_golden_receipts import iter_public_cases  # noqa: E402

from udi_dicom_validator.checks import validate_files  # noqa: E402


def expected_error(manifest_name: str) -> str | None:
    if "missing_udi" in manifest_name:
        return "missing_udi"
    if "wrong_sop_uid" in manifest_name:
        return "sop_uid_mismatch"
    if "registry_unresolved" in manifest_name:
        return "registry_unresolved"
    if "device_uid_used_as_udi_di" in manifest_name:
        return "device_uid_used_as_udi_di"
    return None


def build_rows() -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for version, manifest, dicom_metadata, registry in iter_public_cases():
        receipt = validate_files(manifest, dicom_metadata, registry)
        manifest_data = json.loads(manifest.read_text(encoding="utf-8"))
        failing = next((check for check in receipt["checks"] if check["status"] == "fail"), None)
        rows.append(
            {
                "manifest": str(manifest.relative_to(ROOT)),
                "profile_version": manifest_data.get("profile_version", version),
                "expected_primary_error_code": expected_error(manifest.name),
                "actual_primary_error_code": receipt["primary_error_code"],
                "ok": receipt["ok"],
                "validation_stage": failing["stage"] if failing else "all_passed",
                "fixture_used": str(registry.relative_to(ROOT)),
            }
        )
    return rows


def render_markdown(rows: list[dict[str, Any]]) -> str:
    lines = [
        "# Public Evaluation Matrix",
        "",
        "This matrix is generated from public synthetic examples only. It is not "
        "clinical validation, not regulatory approval, and not certification.",
        "",
        "| Manifest | Profile | Expected | Actual | OK | Stage | Fixture |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for row in rows:
        lines.append(
            "| {manifest} | {profile_version} | {expected_primary_error_code} | "
            "{actual_primary_error_code} | {ok} | {validation_stage} | "
            "{fixture_used} |".format(**row)
        )
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    rows = build_rows()
    artifact_dir = ROOT / "artifacts"
    artifact_dir.mkdir(parents=True, exist_ok=True)
    (artifact_dir / "public_evaluation_matrix.json").write_text(
        json.dumps({"rows": rows, "row_count": len(rows)}, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    (ROOT / "docs" / "public-evaluation-matrix.md").write_text(
        render_markdown(rows),
        encoding="utf-8",
    )
    print(
        json.dumps(
            {"row_count": len(rows), "output": "artifacts/public_evaluation_matrix.json"},
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
