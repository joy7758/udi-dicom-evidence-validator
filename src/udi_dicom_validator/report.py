from __future__ import annotations

from typing import Any


def render_report(receipt: dict[str, Any]) -> str:
    primary = receipt.get("primary_error_code") or "none"
    lines = [
        "# UDI-DICOM Validation Report",
        "",
        "## Summary",
        "",
        f"- Manifest: `{receipt.get('manifest_id')}`",
        f"- OK: `{str(receipt.get('ok')).lower()}`",
        f"- Validation status: `{receipt.get('validation_status')}`",
        "",
        "## Inputs",
        "",
        f"- Manifest SHA-256: `{receipt.get('inputs', {}).get('manifest_sha256')}`",
        f"- DICOM metadata SHA-256: `{receipt.get('inputs', {}).get('dicom_metadata_sha256')}`",
        "",
        "## Checks",
        "",
    ]
    for check in receipt.get("checks", []):
        lines.append(
            f"- `{check.get('stage')}`: `{check.get('status')}` "
            f"{check.get('code') or ''} - {check.get('message')}"
        )
    lines.extend(
        [
            "",
            "## Primary finding",
            "",
            f"`{primary}`",
            "",
            "## Boundary statement",
            "",
            "Not a clinical validation. Not regulatory approval. Not certification.",
            "",
            "## Not a clinical/regulatory conclusion",
            "",
            "This report is a deterministic technical evidence consistency receipt only.",
            "",
        ]
    )
    return "\n".join(lines)
