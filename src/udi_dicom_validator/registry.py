from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import requests

OPENFDA_ENDPOINT = "https://api.fda.gov/device/udi.json"


def load_registry_fixture(path: str | Path | None) -> dict[str, Any]:
    if path is None:
        return {
            "registry_provider": "offline-fixture",
            "registry_jurisdiction": "not_applicable",
            "lookup_timestamp": "1970-01-01T00:00:00Z",
            "lookup_status": "not_requested",
            "source": "default-empty-fixture",
        }
    return json.loads(Path(path).read_text(encoding="utf-8"))


def live_openfda_lookup(parsed_udi_di: str, timeout: float = 5.0) -> dict[str, Any]:
    try:
        params: dict[str, str | int] = {"search": f"identifiers.id:{parsed_udi_di}", "limit": 1}
        response = requests.get(
            OPENFDA_ENDPOINT,
            params=params,
            timeout=timeout,
        )
        if response.status_code == 404:
            status = "unresolved"
            results: list[dict[str, Any]] = []
        else:
            response.raise_for_status()
            results = response.json().get("results", [])
            status = "resolved" if results else "unresolved"
        first = results[0] if results else {}
        return {
            "registry_provider": "openFDA",
            "registry_jurisdiction": "US",
            "lookup_timestamp": "live-openfda-not-deterministic",
            "lookup_status": status,
            "parsed_udi_di": parsed_udi_di,
            "brand_name": first.get("brand_name"),
            "version_or_model_number": first.get("version_or_model_number"),
            "company_name": first.get("company_name"),
            "source": "live-openfda",
        }
    except requests.Timeout:
        return {"registry_provider": "openFDA", "lookup_status": "timeout"}
    except requests.RequestException:
        return {"registry_provider": "openFDA", "lookup_status": "error"}
