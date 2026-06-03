from __future__ import annotations

from tests.conftest import EXAMPLES
from udi_dicom_validator.checks import validate_files
from udi_dicom_validator.report import render_report


def test_report_contains_required_sections() -> None:
    receipt = validate_files(
        EXAMPLES / "manifest.pass.json",
        EXAMPLES / "sample_dicom_metadata.pass.json",
        EXAMPLES / "registry.fixture.resolved.json",
    )
    report = render_report(receipt)
    assert "Summary" in report
    assert "Primary finding" in report
    assert "Not a clinical validation" in report
    assert "Not regulatory approval" in report
