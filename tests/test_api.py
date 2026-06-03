from __future__ import annotations

import json

from tests.conftest import EXAMPLES
from udi_dicom_validator.api import app, healthz, profile, schema, validate_manifest
from udi_dicom_validator.api import examples as list_examples


def load(name: str) -> dict:
    return json.loads((EXAMPLES / name).read_text(encoding="utf-8"))


def test_api_public_endpoints() -> None:
    assert app.title == "UDI-DICOM Evidence Validator"
    assert healthz()["status"] == "ok"
    assert profile()["profile_version"] == "v0.1.0"
    assert schema()["title"]
    assert "manifest.pass.json" in list_examples()["examples"]
    response = validate_manifest(
        {
            "manifest": load("manifest.pass.json"),
            "dicom_metadata": load("sample_dicom_metadata.pass.json"),
            "registry_fixture": load("registry.fixture.resolved.json"),
        }
    )
    assert response["ok"] is True
    fail = validate_manifest(
        {
            "manifest": load("manifest.fail_missing_udi.json"),
            "dicom_metadata": load("sample_dicom_metadata.pass.json"),
            "registry_fixture": load("registry.fixture.resolved.json"),
        }
    )
    assert fail["primary_error_code"] == "missing_udi"
