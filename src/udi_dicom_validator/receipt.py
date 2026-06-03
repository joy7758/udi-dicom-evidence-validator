from __future__ import annotations

import hashlib
import json
from typing import Any

from . import __version__
from .models import CheckResult, ValidationReceipt

PRIMARY_ERROR_PRIORITY = [
    "schema_validation_failed",
    "missing_udi",
    "truncated_udi",
    "parser_failed",
    "unsupported_issuing_agency",
    "missing_udi_di",
    "device_uid_used_as_udi_di",
    "missing_sop_instance_uid",
    "sop_uid_mismatch",
    "dicom_manifest_udi_mismatch",
    "serial_number_mismatch",
    "model_name_mismatch",
    "manufacturer_mismatch",
    "missing_evidence_item",
    "registry_provider_missing",
    "lookup_timestamp_missing",
    "registry_unresolved",
    "registry_timeout",
    "registry_model_mismatch",
    "registry_company_mismatch",
    "trace_id_mismatch",
    "fdo_mapping_mismatch",
]


CLAIMS_BOUNDARY = [
    "not clinical validation",
    "not regulatory approval",
    "not safety assurance",
    "not certification",
    "not medical decision support",
]


def canonical_hash(data: Any) -> str:
    encoded = json.dumps(data, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def choose_primary_error(checks: list[CheckResult]) -> str | None:
    failed = {check.code for check in checks if check.status == "fail" and check.code}
    for code in PRIMARY_ERROR_PRIORITY:
        if code in failed:
            return code
    return None


def build_receipt(
    manifest: dict[str, Any],
    dicom_metadata: dict[str, Any],
    registry: dict[str, Any],
    checks: list[CheckResult],
    warnings: list[str] | None = None,
) -> dict[str, Any]:
    primary = choose_primary_error(checks)
    ok = primary is None
    generated_at = (
        registry.get("lookup_timestamp")
        or manifest.get("lookup_timestamp")
        or "1970-01-01T00:00:00Z"
    )
    payload_for_id = {
        "manifest": manifest,
        "dicom": dicom_metadata,
        "registry": registry,
        "checks": [check.to_dict() for check in checks],
    }
    trace_id = manifest.get("synthetic_workflow_trace_id") or manifest.get("trace_id")
    provenance = dict(manifest.get("provenance") or {})
    if trace_id and "workflow_trace_id" not in provenance:
        provenance["workflow_trace_id"] = trace_id
    receipt = ValidationReceipt(
        receipt_id=f"receipt-{canonical_hash(payload_for_id)[:16]}",
        generated_at=generated_at,
        validator_version=__version__,
        profile_version=manifest.get("profile_version", "v0.1.0"),
        ok=ok,
        manifest_id=manifest.get("manifest_id", ""),
        primary_error_code=primary,
        validation_status="pass" if ok else "fail",
        checks=[check.to_dict() for check in checks],
        inputs={
            "manifest_sha256": canonical_hash(manifest),
            "dicom_metadata_sha256": canonical_hash(dicom_metadata),
        },
        registry={
            "provider": registry.get("registry_provider") or manifest.get("registry_provider"),
            "jurisdiction": registry.get("registry_jurisdiction")
            or manifest.get("registry_jurisdiction"),
            "lookup_status": registry.get("lookup_status") or manifest.get("lookup_status"),
            "summary": registry,
        },
        artifacts=manifest.get("artifact_hashes", {}),
        trace_id=trace_id,
        provenance=provenance,
        warnings=warnings or [],
        claims_boundary=CLAIMS_BOUNDARY,
    )
    return receipt.to_dict()
