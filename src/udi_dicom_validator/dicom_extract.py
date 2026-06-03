from __future__ import annotations

import json
from pathlib import Path
from typing import Any

PATIENT_FIELDS = {"PatientName", "PatientID", "PatientBirthDate", "PatientSex"}


def load_dicom_metadata_json(path: str | Path) -> tuple[dict[str, Any], list[str]]:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    warnings = []
    if any(field in data for field in PATIENT_FIELDS):
        warnings.append("patient_field_seen_but_ignored")
    return normalize_metadata(data), warnings


def normalize_metadata(data: dict[str, Any]) -> dict[str, Any]:
    udi_sequence = data.get("udi_sequence") or data.get("UDISequence") or []
    return {
        "sop_instance_uid": data.get("sop_instance_uid") or data.get("SOPInstanceUID"),
        "study_instance_uid": data.get("study_instance_uid") or data.get("StudyInstanceUID"),
        "series_instance_uid": data.get("series_instance_uid") or data.get("SeriesInstanceUID"),
        "manufacturer": data.get("manufacturer") or data.get("Manufacturer"),
        "model_name": data.get("model_name") or data.get("ManufacturerModelName"),
        "serial_number": data.get("serial_number") or data.get("DeviceSerialNumber"),
        "device_uid": data.get("device_uid") or data.get("DeviceUID"),
        "unique_device_identifier": data.get("unique_device_identifier")
        or data.get("UniqueDeviceIdentifier"),
        "udi_sequence": udi_sequence,
    }


def extract_dicom_file(path: str | Path) -> tuple[dict[str, Any], list[str]]:
    try:
        import pydicom
    except Exception as exc:  # pragma: no cover - environment guard
        raise RuntimeError("pydicom is required to inspect DICOM files") from exc

    dataset = pydicom.dcmread(str(path), stop_before_pixels=True, force=True)
    raw = {
        "SOPInstanceUID": getattr(dataset, "SOPInstanceUID", None),
        "StudyInstanceUID": getattr(dataset, "StudyInstanceUID", None),
        "SeriesInstanceUID": getattr(dataset, "SeriesInstanceUID", None),
        "Manufacturer": getattr(dataset, "Manufacturer", None),
        "ManufacturerModelName": getattr(dataset, "ManufacturerModelName", None),
        "DeviceSerialNumber": getattr(dataset, "DeviceSerialNumber", None),
        "DeviceUID": getattr(dataset, "DeviceUID", None),
        "UniqueDeviceIdentifier": getattr(dataset, "UniqueDeviceIdentifier", None),
    }
    warnings = []
    if any(hasattr(dataset, field) for field in PATIENT_FIELDS):
        warnings.append("patient_field_seen_but_ignored")
    return normalize_metadata(raw), warnings
