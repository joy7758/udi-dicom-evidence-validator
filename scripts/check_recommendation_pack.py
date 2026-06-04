from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
PACK_DIR = ROOT / "docs" / "recommendation"

REQUIRED_FILES = [
    "README.md",
    "department-recommendation-report-cn.md",
    "executive-one-page-cn.md",
    "hospital-it-brief-cn.md",
    "device-manufacturer-brief-cn.md",
    "medical-ai-data-brief-cn.md",
    "boundary-and-risk-statement-cn.md",
    "evidence-map.md",
    "attachment-checklist.md",
    "email-templates-cn-en.md",
    "meeting-script-cn.md",
    "next-step-gate.md",
]

REQUIRED_TERMS = [
    "https://github.com/joy7758/udi-dicom-evidence-validator",
    "10.5281/zenodo.20540532",
    "10.1007/s10278-026-02019-6",
    "Journal of Imaging Informatics in Medicine",
    "no PHI",
    "no raw DICOM",
    "not clinical validation",
    "not regulatory approval",
    "not certification",
    "public synthetic examples",
    "Device UID != UDI-DI",
]

FORBIDDEN_PATTERNS = {
    "private_repo_name": re.compile(
        r"udi-dicom-(?:conformance-suite|sample-validation-service)-private"
    ),
    "raw_dicom_extension": re.compile(r"\.(?:dcm|dicom)\b", re.IGNORECASE),
    "guaranteed_regulatory_approval": re.compile(
        r"guarantee[sd]? (?:regulatory approval|510\\(k\\)|NMPA approval)",
        re.IGNORECASE,
    ),
    "certified_compliance": re.compile(r"certified compliance", re.IGNORECASE),
    "clinically_validated": re.compile(r"clinically validated", re.IGNORECASE),
    "hospital_deployment_guarantee": re.compile(
        r"hospital(?:-wide)? deployment (?:guaranteed|ready|plan)",
        re.IGNORECASE,
    ),
    "patient_level_diagnosis": re.compile(r"patient-level diagnosis", re.IGNORECASE),
    "accepts_phi_or_raw_dicom": re.compile(
        r"accepts (?:PHI|raw DICOM)|processes (?:PHI|raw DICOM)",
        re.IGNORECASE,
    ),
    "commercial_sales_language": re.compile(
        r"sales pipeline|customer acquisition|lead generation|pricing plan",
        re.IGNORECASE,
    ),
}


def markdown_files() -> list[Path]:
    return sorted(PACK_DIR.glob("*.md"))


def run_check() -> dict[str, Any]:
    missing = [name for name in REQUIRED_FILES if not (PACK_DIR / name).is_file()]
    files = markdown_files()
    combined = "\n\n".join(path.read_text(encoding="utf-8") for path in files)
    missing_terms = [term for term in REQUIRED_TERMS if term not in combined]
    forbidden_hits: list[dict[str, str]] = []

    for path in files:
        text = path.read_text(encoding="utf-8")
        relative = str(path.relative_to(ROOT))
        for kind, pattern in FORBIDDEN_PATTERNS.items():
            for match in pattern.finditer(text):
                forbidden_hits.append(
                    {"file": relative, "kind": kind, "match": match.group(0)}
                )

    ok = not missing and not missing_terms and not forbidden_hits
    return {
        "ok": ok,
        "status": "RECOMMENDATION_PACK_CHECK_PASS" if ok else "RECOMMENDATION_PACK_CHECK_FAIL",
        "files_checked": [str(path.relative_to(ROOT)) for path in files],
        "missing_files": missing,
        "missing_terms": missing_terms,
        "forbidden_hits": forbidden_hits,
        "scope": "public validator only",
        "boundary": [
            "no PHI",
            "no raw DICOM",
            "not clinical validation",
            "not regulatory approval",
            "not certification",
            "public synthetic examples",
            "Device UID != UDI-DI",
        ],
    }


def main() -> None:
    result = run_check()
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    if result["ok"]:
        print("check_recommendation_pack=pass")
        return
    raise SystemExit(1)


if __name__ == "__main__":
    main()
