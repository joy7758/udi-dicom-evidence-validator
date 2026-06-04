from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FILES = {
    "package_manifest.json",
    "package_summary.md",
    "reproduction_commands.md",
    "reviewer_expected_outputs.md",
    "SHA256SUMS.txt",
}
FORBIDDEN_MARKERS = {
    "udi-dicom-conformance-suite-private",
    "udi-dicom-sample-validation-service-private",
    "cases/private",
}
PHI_TERMS = {"PatientName", "PatientID", "AccessionNumber", "BirthDate", "MRN"}
RAW_DICOM_EXTENSIONS = {".dcm", ".dicom"}
UNSAFE_PHRASES = {
    "clinical validation completed",
    "regulatory approval granted",
    "certified for clinical use",
    "certification granted",
}
REAL_NAME_INDICATORS = {"mayo clinic", "cleveland clinic", "johns hopkins", "kaiser permanente"}
DOI_PATTERN = re.compile(r"10\.\d{4,9}/[-._;()/:A-Za-z0-9]+")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def check_checksums(path: Path) -> list[str]:
    failures: list[str] = []
    for line in (path / "SHA256SUMS.txt").read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        digest, name = line.split("  ", 1)
        target = path / name
        if not target.exists():
            failures.append(f"missing_checksum_target:{name}")
        elif sha256(target) != digest:
            failures.append(f"checksum_mismatch:{name}")
    return failures


def scrub_safe(text: str) -> str:
    lower = text.lower()
    safe_phrases = (
        "not clinical validation",
        "not regulatory approval",
        "not certification",
        "no phi",
        "no raw dicom",
        "doi-ready",
        "no assigned doi",
        "no fake doi",
    )
    for phrase in safe_phrases:
        lower = lower.replace(phrase, "")
    return lower


def inspect_file(file: Path) -> list[str]:
    hits: list[str] = []
    if file.suffix.lower() in RAW_DICOM_EXTENSIONS:
        return [f"raw_dicom:{file.name}"]
    text = file.read_text(encoding="utf-8", errors="ignore")
    scrubbed = scrub_safe(text)
    for marker in FORBIDDEN_MARKERS:
        if marker in text:
            hits.append(f"private_marker:{marker}:{file.name}")
    for term in PHI_TERMS:
        if term in text:
            hits.append(f"phi_marker:{term}:{file.name}")
    for phrase in UNSAFE_PHRASES:
        if phrase in scrubbed:
            hits.append(f"unsafe_phrase:{phrase}:{file.name}")
    for indicator in REAL_NAME_INDICATORS:
        if indicator in scrubbed:
            hits.append(f"real_name_indicator:{indicator}:{file.name}")
    doi_matches = {match.group(0).rstrip(".") for match in DOI_PATTERN.finditer(text)}
    if doi_matches:
        hits.append(f"claimed_doi:{','.join(sorted(doi_matches))}:{file.name}")
    return hits


def main() -> None:
    default_package = ROOT / "artifacts" / "paper-submission-v0.6"
    package = Path(sys.argv[1]) if len(sys.argv) > 1 else default_package
    if not package.is_absolute():
        package = ROOT / package
    failures: list[str] = []
    for name in sorted(REQUIRED_FILES):
        if not (package / name).exists():
            failures.append(f"missing:{name}")
    if not failures:
        manifest = json.loads((package / "package_manifest.json").read_text(encoding="utf-8"))
        if manifest.get("public_only") is not True:
            failures.append("public_only_not_true")
        if manifest.get("private_repo_material_included") is not False:
            failures.append("private_repo_material_included_not_false")
        if manifest.get("raw_dicom_included") is not False:
            failures.append("raw_dicom_included_not_false")
        if manifest.get("doi_claimed") is not False:
            failures.append("doi_claimed_not_false")
        failures.extend(check_checksums(package))
    for file in sorted(path for path in package.rglob("*") if path.is_file()):
        if file.suffix.lower() in {".json", ".md", ".txt", ".yaml", ".yml"}:
            failures.extend(inspect_file(file))
        elif file.suffix.lower() in RAW_DICOM_EXTENSIONS:
            failures.append(f"raw_dicom:{file.name}")
    result = {"ok": not failures, "failures": failures, "package": str(package.relative_to(ROOT))}
    print(json.dumps(result, sort_keys=True))
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
