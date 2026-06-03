from __future__ import annotations

from tests.conftest import EXAMPLES, EXAMPLES_V02
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


def run_v02_case(
    manifest_name: str,
    registry_name: str = "registry.fixture_v0.2.resolved.json",
) -> dict:
    return validate_files(
        EXAMPLES_V02 / manifest_name,
        EXAMPLES_V02 / "sample_dicom_metadata_v0.2.pass.json",
        EXAMPLES_V02 / registry_name,
    )


def test_v02_pass_case_has_trace_and_provenance() -> None:
    receipt = run_v02_case("manifest_v0.2.pass.json")
    assert receipt["ok"] is True
    assert receipt["profile_version"] == "v0.2.0"
    assert receipt["trace_id"] == "trace-v02-portable-ultrasound-001"
    assert receipt["provenance"]["synthetic_data"] is True
    assert {check["stage"] for check in receipt["checks"]} >= {
        "trace_id_consistency",
        "fdo_mapping_consistency",
    }


def test_v02_fail_cases() -> None:
    missing = run_v02_case("manifest_v0.2.fail_missing_udi.json")
    assert missing["primary_error_code"] == "missing_udi"
    unresolved = run_v02_case(
        "manifest_v0.2.fail_registry_unresolved.json",
        "registry.fixture_v0.2.unresolved.json",
    )
    assert unresolved["primary_error_code"] == "registry_unresolved"
    device_uid = run_v02_case("manifest_v0.2.fail_device_uid_used_as_udi_di.json")
    assert device_uid["primary_error_code"] == "device_uid_used_as_udi_di"
