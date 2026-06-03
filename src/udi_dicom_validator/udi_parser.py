from __future__ import annotations

import re
from dataclasses import dataclass


@dataclass(frozen=True)
class UDIParseResult:
    ok: bool
    parsed_udi_di: str | None
    parsed_udi_pi: dict[str, str]
    error_code: str | None
    message: str


SUPPORTED_AGENCIES = {"gs1", "synthetic_gs1"}


def parse_udi(full_udi: str | None, issuing_agency: str | None) -> UDIParseResult:
    if not full_udi:
        return UDIParseResult(False, None, {}, "missing_udi", "UDI is missing.")
    if issuing_agency is None or issuing_agency.lower() not in SUPPORTED_AGENCIES:
        return UDIParseResult(
            False,
            None,
            {},
            "unsupported_issuing_agency",
            "Only the minimal synthetic GS1 parser is supported.",
        )
    if len(full_udi) < 16:
        return UDIParseResult(False, None, {}, "truncated_udi", "UDI is too short.")

    # This is a deliberately small reference parser for v0.1 fixtures, not a
    # complete GS1, HIBCC, or ICCBBA parser.
    parenthesized = re.match(r"^\(01\)(\d{14})(.*)$", full_udi)
    if parenthesized:
        di = parenthesized.group(1)
        rest = parenthesized.group(2)
        pi: dict[str, str] = {}
        lot = re.search(r"\(10\)([^()]+)", rest)
        serial = re.search(r"\(21\)([^()]+)", rest)
        if lot:
            pi["lot"] = lot.group(1)
        if serial:
            pi["serial"] = serial.group(1)
        return UDIParseResult(True, di, pi, None, "Parsed minimal parenthesized GS1 UDI.")

    compact = re.match(r"^01(\d{14})(.*)$", full_udi)
    if compact:
        di = compact.group(1)
        rest = compact.group(2)
        pi = {}
        if rest.startswith("10") and "21" in rest[2:]:
            lot_and_serial = rest[2:].split("21", 1)
            pi["lot"] = lot_and_serial[0]
            pi["serial"] = lot_and_serial[1]
        elif rest.startswith("21"):
            pi["serial"] = rest[2:]
        return UDIParseResult(True, di, pi, None, "Parsed minimal compact GS1 UDI.")

    return UDIParseResult(False, None, {}, "parser_failed", "Unsupported UDI shape.")
