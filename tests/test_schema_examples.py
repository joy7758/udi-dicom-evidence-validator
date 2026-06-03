from __future__ import annotations

import json

from jsonschema import Draft202012Validator

from tests.conftest import EXAMPLES, EXAMPLES_V02
from udi_dicom_validator.schema_loader import load_schema, manifest_schema_name


def test_examples_parse_as_json() -> None:
    for path in EXAMPLES.glob("*.json"):
        json.loads(path.read_text(encoding="utf-8"))
    for path in EXAMPLES_V02.glob("*.json"):
        json.loads(path.read_text(encoding="utf-8"))


def test_manifest_examples_match_schema() -> None:
    for path in EXAMPLES.glob("manifest.*.json"):
        data = json.loads(path.read_text())
        schema = load_schema(manifest_schema_name(data))
        validator = Draft202012Validator(schema)
        errors = sorted(validator.iter_errors(data), key=str)
        assert errors == []
    for path in EXAMPLES_V02.glob("manifest_v0.2.*.json"):
        data = json.loads(path.read_text())
        schema = load_schema(manifest_schema_name(data))
        validator = Draft202012Validator(schema)
        errors = sorted(validator.iter_errors(data), key=str)
        assert errors == []
