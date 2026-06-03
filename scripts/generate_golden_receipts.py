from __future__ import annotations

import json
import sys
from collections.abc import Iterable
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from udi_dicom_validator.checks import validate_files  # noqa: E402


def iter_public_cases() -> Iterable[tuple[str, Path, Path, Path]]:
    examples = ROOT / "examples" / "public"
    dicom_v01 = examples / "sample_dicom_metadata.pass.json"
    registry_v01_resolved = examples / "registry.fixture.resolved.json"
    registry_v01_unresolved = examples / "registry.fixture.unresolved.json"
    for manifest in sorted(examples.glob("manifest.*.json")):
        registry = (
            registry_v01_unresolved
            if "registry_unresolved" in manifest.name
            else registry_v01_resolved
        )
        yield "v0.1", manifest, dicom_v01, registry

    examples_v02 = examples / "v0.2"
    dicom_v02 = examples_v02 / "sample_dicom_metadata_v0.2.pass.json"
    registry_v02_resolved = examples_v02 / "registry.fixture_v0.2.resolved.json"
    registry_v02_unresolved = examples_v02 / "registry.fixture_v0.2.unresolved.json"
    for manifest in sorted(examples_v02.glob("manifest_v0.2.*.json")):
        registry = (
            registry_v02_unresolved
            if "registry_unresolved" in manifest.name
            else registry_v02_resolved
        )
        yield "v0.2", manifest, dicom_v02, registry


def receipt_name(manifest_path: Path) -> str:
    return manifest_path.stem.replace(".", "_") + ".receipt.json"


def main() -> None:
    count = 0
    outputs: list[str] = []
    for version, manifest, dicom_metadata, registry in iter_public_cases():
        receipt = validate_files(manifest, dicom_metadata, registry)
        out = ROOT / "tests" / "golden" / version / receipt_name(manifest)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        outputs.append(str(out.relative_to(ROOT)))
        count += 1
    print(json.dumps({"generated": count, "outputs": outputs}, sort_keys=True))


if __name__ == "__main__":
    main()
