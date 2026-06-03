from __future__ import annotations

from typing import Any

from fastapi import FastAPI

from .checks import validate_dicts
from .report import render_report
from .schema_loader import load_schema

app = FastAPI(
    title="UDI-DICOM Evidence Validator",
    version="0.2.0",
    description="Public-only validation API. Not clinical validation or regulatory approval.",
)


@app.get("/healthz")
def healthz() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/v1/profile")
def profile() -> dict[str, str]:
    return {
        "profile_name": "udi-dicom-evidence-manifest",
        "profile_version": "v0.2.0",
        "supported_versions": "v0.1.0,v0.2.0",
    }


@app.get("/v1/schema")
def schema() -> dict[str, Any]:
    return load_schema("udi-dicom-evidence-manifest-v0.2.schema.json")


@app.get("/v1/examples")
def examples() -> dict[str, list[str]]:
    return {
        "examples": [
            "manifest.pass.json",
            "manifest.fail_missing_udi.json",
            "manifest.fail_wrong_sop_uid.json",
            "manifest.fail_registry_unresolved.json",
            "manifest.fail_device_uid_used_as_udi_di.json",
            "v0.2/manifest_v0.2.pass.json",
            "v0.2/manifest_v0.2.fail_missing_udi.json",
            "v0.2/manifest_v0.2.fail_registry_unresolved.json",
            "v0.2/manifest_v0.2.fail_device_uid_used_as_udi_di.json",
        ]
    }


@app.post("/v1/validate/manifest")
def validate_manifest(payload: dict[str, Any]) -> dict[str, Any]:
    return validate_dicts(
        payload["manifest"],
        payload["dicom_metadata"],
        payload.get("registry_fixture"),
    )


@app.post("/v1/validate/dicom-metadata")
def validate_dicom_metadata(payload: dict[str, Any]) -> dict[str, Any]:
    return validate_dicts(
        payload["manifest"],
        payload["dicom_metadata"],
        payload.get("registry_fixture"),
    )


@app.post("/v1/receipt/render")
def render_receipt(payload: dict[str, Any]) -> dict[str, str]:
    return {"report": render_report(payload["receipt"])}
