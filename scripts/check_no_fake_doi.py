from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
VERIFIED_DOI_SUMMARIES = [
    ROOT / "artifacts" / "doi-capture-v0.8.1" / "doi-capture-summary.json",
]
DEFAULT_TARGETS = [
    "README.md",
    "docs",
    "paper",
    "release",
    "CITATION.cff",
    "codemeta.json",
    ".zenodo.json",
    "artifacts/doi-archive-review-v0.8",
]
ALLOWED_DOIS = {"10.5063/schema/codemeta-2.0"}
PRIVATE_REPO_MARKERS = {
    "udi-dicom-conformance-suite-private",
    "udi-dicom-sample-validation-service-private",
    "/udi-dicom-conformance-suite-private",
    "/udi-dicom-sample-validation-service-private",
}
PHI_MARKERS = {"PatientName", "PatientID", "AccessionNumber", "BirthDate", "MRN"}
RAW_DICOM_PATTERN = re.compile(r"\.dcm\b|\.dicom\b", re.IGNORECASE)
DOI_PATTERN = re.compile(r"\b10\.\d{4,9}/[-._;()/:A-Za-z0-9]+")
UPGRADED_DOI_CLAIM_PATTERN = re.compile(
    r"\bDOI\s+(issued|minted|assigned|verified)\b", re.IGNORECASE
)
UNSAFE_UPGRADE_PATTERNS = {
    "clinical_validation_claim": re.compile(r"clinical validation (completed|passed|proven)"),
    "regulatory_approval_claim": re.compile(r"regulatory approval (granted|received|passed)"),
    "certification_claim": re.compile(r"certifi(?:ed|cation) (granted|completed|passed)"),
}


def iter_files(targets: list[Path]) -> list[Path]:
    files: list[Path] = []
    for target in targets:
        path = target if target.is_absolute() else ROOT / target
        if not path.exists():
            continue
        if path.is_file():
            files.append(path)
        else:
            files.extend(
                child
                for child in path.rglob("*")
                if child.is_file()
                and child.suffix.lower()
                in {".md", ".txt", ".json", ".cff", ".toml", ".yaml", ".yml"}
            )
    return sorted(set(files))


def verified_dois() -> set[str]:
    dois: set[str] = set()
    for path in VERIFIED_DOI_SUMMARIES:
        if not path.exists():
            continue
        data = json.loads(path.read_text(encoding="utf-8"))
        doi = str(data.get("doi", ""))
        if data.get("status") == "REAL_DOI_VERIFIED" and DOI_PATTERN.fullmatch(doi):
            dois.add(doi)
    return dois


def inspect_file(path: Path, allowed_dois: set[str]) -> list[dict[str, Any]]:
    text = path.read_text(encoding="utf-8", errors="ignore")
    relative = str(path.relative_to(ROOT))
    hits: list[dict[str, Any]] = []
    for marker in sorted(PRIVATE_REPO_MARKERS):
        if marker in text:
            hits.append({"file": relative, "kind": "private_repo_path", "match": marker})
    for marker in sorted(PHI_MARKERS):
        if marker in text:
            hits.append({"file": relative, "kind": "phi_marker", "match": marker})
    for match in RAW_DICOM_PATTERN.finditer(text):
        hits.append({"file": relative, "kind": "raw_dicom_extension", "match": match.group(0)})
    for match in DOI_PATTERN.finditer(text):
        doi = match.group(0).rstrip(".,)")
        if doi not in allowed_dois:
            hits.append({"file": relative, "kind": "claimed_or_placeholder_doi", "match": doi})
    for match in UPGRADED_DOI_CLAIM_PATTERN.finditer(text):
        hits.append({"file": relative, "kind": "upgraded_doi_claim", "match": match.group(0)})
    lowered = text.lower()
    for kind, pattern in UNSAFE_UPGRADE_PATTERNS.items():
        for match in pattern.finditer(lowered):
            hits.append({"file": relative, "kind": kind, "match": match.group(0)})
    return hits


def run_scan(targets: list[str] | None = None) -> dict[str, Any]:
    selected = targets or DEFAULT_TARGETS
    paths = iter_files([Path(target) for target in selected])
    verified = verified_dois()
    allowed = ALLOWED_DOIS | verified
    hits: list[dict[str, Any]] = []
    for path in paths:
        hits.extend(inspect_file(path, allowed))
    return {
        "ok": not hits,
        "hits": hits,
        "files_checked": len(paths),
        "targets": selected,
        "allowed_doi_references": sorted(ALLOWED_DOIS),
        "verified_dois": sorted(verified),
        "doi_policy": (
            "DOI-ready and DOI pending are allowed; real DOI claims require "
            "a REAL_DOI_VERIFIED capture summary."
        ),
    }


def main() -> None:
    targets = sys.argv[1:] or None
    result = run_scan(targets)
    print(json.dumps(result, sort_keys=True))
    if not result["ok"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
