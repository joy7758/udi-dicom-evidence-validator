from __future__ import annotations

import json
from importlib.resources import files
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator


class SchemaValidationError(ValueError):
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.code = "schema_validation_failed"


def schema_path(name: str) -> Path:
    root = Path(__file__).resolve().parents[2]
    return root / "schema" / name


def load_schema(name: str) -> dict[str, Any]:
    path = schema_path(name)
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    resource = files("udi_dicom_validator").joinpath("../../schema", name)
    return json.loads(resource.read_text(encoding="utf-8"))


def manifest_schema_name(manifest: dict[str, Any]) -> str:
    profile_version = manifest.get("profile_version", "v0.1.0")
    if profile_version == "v0.2.0":
        return "udi-dicom-evidence-manifest-v0.2.schema.json"
    if profile_version == "v0.1.0":
        return "udi-dicom-evidence-manifest-v0.1.schema.json"
    raise SchemaValidationError(f"profile_version: unsupported version {profile_version!r}")


def validate_manifest_schema(manifest: dict[str, Any]) -> None:
    schema = load_schema(manifest_schema_name(manifest))
    validator = Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(manifest), key=lambda error: list(error.path))
    if errors:
        first = errors[0]
        path = ".".join(str(part) for part in first.path) or "<root>"
        raise SchemaValidationError(f"{path}: {first.message}")
