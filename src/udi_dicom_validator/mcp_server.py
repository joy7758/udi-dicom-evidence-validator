from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .checks import validate_files
from .report import render_report

ROOT = Path(__file__).resolve().parents[2]
PUBLIC_EXAMPLES = ROOT / "examples" / "public"
ALLOWED_TOOLS = {
    "list_profile_versions",
    "list_public_examples",
    "get_error_code_definition",
    "validate_public_manifest_fixture",
    "render_public_receipt_summary",
}
FORBIDDEN_TOOL_PREFIXES = (
    "run_private",
    "access_partner",
    "access_real",
    "vendor_mapping_private",
    "hospital_sample",
)


def _ensure_public_example(path: Path) -> Path:
    resolved = path.resolve()
    if PUBLIC_EXAMPLES.resolve() not in resolved.parents and resolved != PUBLIC_EXAMPLES.resolve():
        raise ValueError("Only public examples are accessible.")
    if "private" in resolved.parts or "partner" in resolved.parts:
        raise ValueError("Private or partner content is not accessible.")
    return resolved


def list_profile_versions() -> dict[str, Any]:
    return {
        "profile_versions": ["v0.1.0", "v0.2.0"],
        "planned": ["v0.3.0"],
        "boundary": (
            "public synthetic examples only; not clinical validation "
            "or regulatory approval"
        ),
    }


def list_public_examples() -> dict[str, Any]:
    examples = sorted(
        str(path.relative_to(PUBLIC_EXAMPLES))
        for path in PUBLIC_EXAMPLES.rglob("*.json")
        if path.is_file()
    )
    return {"examples": examples}


def get_error_code_definition(error_code: str) -> dict[str, str]:
    docs = ROOT / "docs" / "error-codes.md"
    for line in docs.read_text(encoding="utf-8").splitlines():
        if f"| {error_code} |" in line:
            parts = [part.strip() for part in line.strip("|").split("|")]
            return {"error_code": error_code, "definition": parts[-1]}
    return {"error_code": error_code, "definition": "unknown public error code"}


def _fixture_paths(manifest_fixture: str) -> tuple[Path, Path, Path]:
    manifest = _ensure_public_example(PUBLIC_EXAMPLES / manifest_fixture)
    if manifest_fixture.startswith("v0.2/"):
        base = PUBLIC_EXAMPLES / "v0.2"
        dicom = base / "sample_dicom_metadata_v0.2.pass.json"
        registry = (
            base / "registry.fixture_v0.2.unresolved.json"
            if "registry_unresolved" in manifest.name
            else base / "registry.fixture_v0.2.resolved.json"
        )
    else:
        dicom = PUBLIC_EXAMPLES / "sample_dicom_metadata.pass.json"
        registry = (
            PUBLIC_EXAMPLES / "registry.fixture.unresolved.json"
            if "registry_unresolved" in manifest.name
            else PUBLIC_EXAMPLES / "registry.fixture.resolved.json"
        )
    return manifest, _ensure_public_example(dicom), _ensure_public_example(registry)


def validate_public_manifest_fixture(manifest_fixture: str) -> dict[str, Any]:
    manifest, dicom, registry = _fixture_paths(manifest_fixture)
    receipt = validate_files(manifest, dicom, registry)
    return {
        "manifest_fixture": manifest_fixture,
        "ok": receipt["ok"],
        "primary_error_code": receipt["primary_error_code"],
        "profile_version": receipt["profile_version"],
        "trace_id": receipt.get("trace_id"),
    }


def render_public_receipt_summary(manifest_fixture: str) -> dict[str, str]:
    manifest, dicom, registry = _fixture_paths(manifest_fixture)
    receipt = validate_files(manifest, dicom, registry)
    report = render_report(receipt)
    return {
        "manifest_fixture": manifest_fixture,
        "summary": report.split("## Boundary statement", 1)[0].strip(),
    }


def call_tool(tool_name: str, **kwargs: Any) -> dict[str, Any]:
    if tool_name not in ALLOWED_TOOLS or tool_name.startswith(FORBIDDEN_TOOL_PREFIXES):
        raise ValueError(f"Tool is not public: {tool_name}")
    if tool_name == "list_profile_versions":
        return list_profile_versions()
    if tool_name == "list_public_examples":
        return list_public_examples()
    if tool_name == "get_error_code_definition":
        return get_error_code_definition(str(kwargs["error_code"]))
    if tool_name == "validate_public_manifest_fixture":
        return validate_public_manifest_fixture(str(kwargs["manifest_fixture"]))
    if tool_name == "render_public_receipt_summary":
        return render_public_receipt_summary(str(kwargs["manifest_fixture"]))
    raise ValueError(f"Unhandled public tool: {tool_name}")


def main() -> None:
    print(json.dumps(list_profile_versions(), sort_keys=True))


if __name__ == "__main__":
    main()
