from __future__ import annotations

from tests.conftest import EXAMPLES
from udi_dicom_validator.checks import validate_files


def run_case(manifest_name: str, registry_name: str = "registry.fixture.resolved.json") -> dict:
    return validate_files(
        EXAMPLES / manifest_name,
        EXAMPLES / "sample_dicom_metadata.pass.json",
        EXAMPLES / registry_name,
    )


def test_pass_case() -> None:
    receipt = run_case("manifest.pass.json")
    assert receipt["ok"] is True
    assert receipt["primary_error_code"] is None
    assert receipt["validation_status"] == "pass"


def test_missing_udi_case() -> None:
    receipt = run_case("manifest.fail_missing_udi.json")
    assert receipt["ok"] is False
    assert receipt["primary_error_code"] == "missing_udi"


def test_wrong_sop_case() -> None:
    receipt = run_case("manifest.fail_wrong_sop_uid.json")
    assert receipt["ok"] is False
    assert receipt["primary_error_code"] == "sop_uid_mismatch"


def test_registry_unresolved_case() -> None:
    receipt = run_case("manifest.fail_registry_unresolved.json", "registry.fixture.unresolved.json")
    assert receipt["ok"] is False
    assert receipt["primary_error_code"] == "registry_unresolved"


def test_device_uid_used_as_udi_di_case() -> None:
    receipt = run_case("manifest.fail_device_uid_used_as_udi_di.json")
    assert receipt["ok"] is False
    assert receipt["primary_error_code"] == "device_uid_used_as_udi_di"
