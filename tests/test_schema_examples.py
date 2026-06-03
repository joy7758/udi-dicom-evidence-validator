from __future__ import annotations

import json

from jsonschema import Draft202012Validator

from tests.conftest import EXAMPLES
from udi_dicom_validator.schema_loader import load_schema


def test_examples_parse_as_json() -> None:
    for path in EXAMPLES.glob("*.json"):
        json.loads(path.read_text(encoding="utf-8"))


def test_manifest_examples_match_schema() -> None:
    schema = load_schema("udi-dicom-evidence-manifest-v0.1.schema.json")
    validator = Draft202012Validator(schema)
    for path in EXAMPLES.glob("manifest.*.json"):
        errors = sorted(validator.iter_errors(json.loads(path.read_text())), key=str)
        assert errors == []
