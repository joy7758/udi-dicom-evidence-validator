from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .dicom_extract import load_dicom_metadata_json, normalize_metadata
from .models import CheckResult
from .receipt import build_receipt
from .registry import load_registry_fixture
from .schema_loader import SchemaValidationError, validate_manifest_schema
from .udi_parser import parse_udi


def _manifest_udi_from_dicom(dicom: dict[str, Any]) -> str | None:
    if dicom.get("unique_device_identifier"):
        return dicom["unique_device_identifier"]
    sequence = dicom.get("udi_sequence") or []
    if sequence:
        first = sequence[0]
        return first.get("unique_device_identifier") or first.get("UniqueDeviceIdentifier")
    return None


def _check_evidence_items(manifest: dict[str, Any]) -> bool:
    items = manifest.get("evidence_items") or []
    if not items:
        return False
    for item in items:
        if not item.get("type") or not item.get("uri"):
            return False
        if not (item.get("sha256") or item.get("declared_hash")):
            return False
    return True


def validate_dicts(
    manifest: dict[str, Any],
    dicom_metadata: dict[str, Any],
    registry_fixture: dict[str, Any] | None = None,
    warnings: list[str] | None = None,
) -> dict[str, Any]:
    checks: list[CheckResult] = []
    warnings = list(warnings or [])
    dicom = normalize_metadata(dicom_metadata)
    registry = registry_fixture or {}
    try:
        validate_manifest_schema(manifest)
    except SchemaValidationError as exc:
        checks.append(
            CheckResult(
                "schema",
                "fail",
                exc.code,
                str(exc),
            )
        )
        return build_receipt(manifest, dicom, registry, checks, warnings)

    parsed = parse_udi(manifest.get("full_udi"), manifest.get("issuing_agency"))
    if not parsed.ok:
        checks.append(
            CheckResult("presence_parseability", "fail", parsed.error_code, parsed.message)
        )
        return build_receipt(manifest, dicom, registry, checks, warnings)
    if not parsed.parsed_udi_di:
        checks.append(
            CheckResult(
                "presence_parseability",
                "fail",
                "missing_udi_di",
                "Parsed UDI-DI is missing.",
            )
        )
        return build_receipt(manifest, dicom, registry, checks, warnings)
    if manifest.get("parsed_udi_di") == manifest.get("device_uid"):
        checks.append(
            CheckResult(
                "presence_parseability",
                "fail",
                "device_uid_used_as_udi_di",
                "DICOM Device UID was used as UDI-DI.",
            )
        )
        return build_receipt(manifest, dicom, registry, checks, warnings)
    checks.append(
        CheckResult(
            "presence_parseability",
            "pass",
            None,
            "UDI is present and minimally parseable.",
            {"parsed_udi_di": parsed.parsed_udi_di},
        )
    )

    if not manifest.get("sop_instance_uid"):
        checks.append(
            CheckResult(
                "reference_closure",
                "fail",
                "missing_sop_instance_uid",
                "Manifest SOP Instance UID is missing.",
            )
        )
        return build_receipt(manifest, dicom, registry, checks, warnings)
    if manifest.get("sop_instance_uid") != dicom.get("sop_instance_uid"):
        checks.append(
            CheckResult(
                "reference_closure",
                "fail",
                "sop_uid_mismatch",
                "Manifest and DICOM SOP Instance UID differ.",
            )
        )
        return build_receipt(manifest, dicom, registry, checks, warnings)
    if not _check_evidence_items(manifest):
        checks.append(
            CheckResult(
                "reference_closure",
                "fail",
                "missing_evidence_item",
                "One or more required evidence items are missing or incomplete.",
            )
        )
        return build_receipt(manifest, dicom, registry, checks, warnings)
    checks.append(CheckResult("reference_closure", "pass", None, "References are closed."))

    dicom_udi = _manifest_udi_from_dicom(dicom)
    if dicom_udi and dicom_udi != manifest.get("full_udi"):
        checks.append(
            CheckResult(
                "cross_layer_consistency",
                "fail",
                "dicom_manifest_udi_mismatch",
                "DICOM UDI and manifest UDI differ.",
            )
        )
        return build_receipt(manifest, dicom, registry, checks, warnings)
    for field, code in [
        ("serial_number", "serial_number_mismatch"),
        ("model_name", "model_name_mismatch"),
        ("manufacturer", "manufacturer_mismatch"),
    ]:
        if dicom.get(field) and manifest.get(field) and dicom.get(field) != manifest.get(field):
            checks.append(
                CheckResult(
                    "cross_layer_consistency",
                    "fail",
                    code,
                    f"{field} differs between DICOM metadata and manifest.",
                )
            )
            return build_receipt(manifest, dicom, registry, checks, warnings)
    checks.append(CheckResult("cross_layer_consistency", "pass", None, "Metadata matches."))

    provider = registry.get("registry_provider") or manifest.get("registry_provider")
    timestamp = registry.get("lookup_timestamp") or manifest.get("lookup_timestamp")
    lookup_status = registry.get("lookup_status") or manifest.get("lookup_status")
    if not provider:
        checks.append(
            CheckResult(
                "registry_resolution",
                "fail",
                "registry_provider_missing",
                "Registry provider is missing.",
            )
        )
        return build_receipt(manifest, dicom, registry, checks, warnings)
    if not timestamp:
        checks.append(
            CheckResult(
                "registry_resolution",
                "fail",
                "lookup_timestamp_missing",
                "Lookup timestamp is missing.",
            )
        )
        return build_receipt(manifest, dicom, registry, checks, warnings)
    if lookup_status == "timeout":
        checks.append(
            CheckResult("registry_resolution", "fail", "registry_timeout", "Registry timed out.")
        )
        return build_receipt(manifest, dicom, registry, checks, warnings)
    if lookup_status != "resolved":
        checks.append(
            CheckResult(
                "registry_resolution",
                "fail",
                "registry_unresolved",
                "Registry did not resolve the UDI-DI.",
            )
        )
        return build_receipt(manifest, dicom, registry, checks, warnings)
    registry_model = registry.get("version_or_model_number")
    registry_company = registry.get("company_name")
    if registry_model and registry_model != manifest.get("model_name"):
        checks.append(
            CheckResult(
                "registry_resolution",
                "fail",
                "registry_model_mismatch",
                "Registry model differs from manifest model.",
            )
        )
        return build_receipt(manifest, dicom, registry, checks, warnings)
    if registry_company and registry_company != manifest.get("manufacturer"):
        checks.append(
            CheckResult(
                "registry_resolution",
                "fail",
                "registry_company_mismatch",
                "Registry company differs from manifest manufacturer.",
            )
        )
        return build_receipt(manifest, dicom, registry, checks, warnings)
    checks.append(CheckResult("registry_resolution", "pass", None, "Registry fixture resolved."))
    return build_receipt(manifest, dicom, registry, checks, warnings)


def validate_files(
    manifest_path: str | Path,
    dicom_metadata_path: str | Path,
    registry_fixture_path: str | Path | None = None,
) -> dict[str, Any]:
    manifest = json.loads(Path(manifest_path).read_text(encoding="utf-8"))
    dicom, warnings = load_dicom_metadata_json(dicom_metadata_path)
    registry = load_registry_fixture(registry_fixture_path)
    return validate_dicts(manifest, dicom, registry, warnings)
