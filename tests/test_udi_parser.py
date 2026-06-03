from __future__ import annotations

from udi_dicom_validator.udi_parser import parse_udi


def test_parenthesized_gs1() -> None:
    result = parse_udi("(01)12345678901234(10)LOT123(21)SER123", "GS1")
    assert result.ok is True
    assert result.parsed_udi_di == "12345678901234"
    assert result.parsed_udi_pi["lot"] == "LOT123"
    assert result.parsed_udi_pi["serial"] == "SER123"


def test_compact_gs1() -> None:
    result = parse_udi("011234567890123410LOT12321SER123", "GS1")
    assert result.ok is True
    assert result.parsed_udi_di == "12345678901234"
    assert result.parsed_udi_pi["serial"] == "SER123"


def test_unsupported_agency() -> None:
    result = parse_udi("(01)12345678901234", "HIBCC")
    assert result.ok is False
    assert result.error_code == "unsupported_issuing_agency"


def test_truncated_input() -> None:
    result = parse_udi("01123", "GS1")
    assert result.ok is False
    assert result.error_code == "truncated_udi"
