from __future__ import annotations

import json

from tests.conftest import EXAMPLES, EXAMPLES_V02
from udi_dicom_validator.api import app, healthz, profile, schema, validate_manifest
from udi_dicom_validator.api import examples as list_examples


def load(name: str) -> dict:
    return json.loads((EXAMPLES / name).read_text(encoding="utf-8"))


def load_v02(name: str) -> dict:
    return json.loads((EXAMPLES_V02 / name).read_text(encoding="utf-8"))


def test_api_public_endpoints() -> None:
    assert app.title == "UDI-DICOM Evidence Validator"
    assert healthz()["status"] == "ok"
    assert profile()["profile_version"] == "v0.2.0"
    assert "v0.1.0" in profile()["supported_versions"]
    assert schema()["title"] == "UDI-DICOM Evidence Manifest v0.2.0"
    assert "manifest.pass.json" in list_examples()["examples"]
    assert "v0.2/manifest_v0.2.pass.json" in list_examples()["examples"]
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


def test_api_v02_payload() -> None:
    response = validate_manifest(
        {
            "manifest": load_v02("manifest_v0.2.pass.json"),
            "dicom_metadata": load_v02("sample_dicom_metadata_v0.2.pass.json"),
            "registry_fixture": load_v02("registry.fixture_v0.2.resolved.json"),
        }
    )
    assert response["ok"] is True
    assert response["profile_version"] == "v0.2.0"
    assert response["trace_id"] == "trace-v02-portable-ultrasound-001"
