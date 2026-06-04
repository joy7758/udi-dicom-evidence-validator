from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    default_target = ROOT / "artifacts" / "archive-metadata-report-v0.6.json"
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else default_target
    if not target.is_absolute():
        target = ROOT / target
    failures: list[str] = []
    if not target.exists():
        failures.append("missing_report_json")
    else:
        report = json.loads(target.read_text(encoding="utf-8"))
        if report.get("doi_ready") is not True:
            failures.append("doi_ready_not_true")
        if report.get("doi_claimed") is not False:
            failures.append("doi_claimed_not_false")
        if report.get("assigned_doi") is not None:
            failures.append("assigned_doi_is_not_none")
        checks = report.get("checks", {})
        for name, value in checks.items():
            if value is not True:
                failures.append(f"check_failed:{name}")
        boundary_text = " ".join(report.get("boundary", [])).lower()
        required_boundary = [
            "no phi",
            "no raw dicom",
            "not clinical validation",
            "not regulatory approval",
            "not certification",
        ]
        for phrase in required_boundary:
            if phrase not in boundary_text:
                failures.append(f"missing_boundary:{phrase}")
    result = {"ok": not failures, "failures": failures, "target": str(target.relative_to(ROOT))}
    print(json.dumps(result, sort_keys=True))
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
