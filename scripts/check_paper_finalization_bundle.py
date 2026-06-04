from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FILES = {
    "manuscript_sections_index.md",
    "finalization_checklist.md",
    "reviewer_command_sheet.md",
    "reproducibility_summary.md",
    "citation_metadata_status.md",
    "limitations_boundary_check.md",
    "missing_manual_items.md",
    "SHA256SUMS.txt",
}
REQUIRED_MANUAL_ITEMS = {
    "title",
    "target journal",
    "final abstract",
    "reference verification",
    "figure rendering",
    "DOI insertion after Zenodo record exists",
}


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


def main() -> None:
    target = (
        Path(sys.argv[1])
        if len(sys.argv) > 1
        else ROOT / "artifacts/paper-finalization-bundle-v0.8"
    )
    if not target.is_absolute():
        target = ROOT / target
    failures: list[str] = []
    for name in sorted(REQUIRED_FILES):
        if not (target / name).exists():
            failures.append(f"missing:{name}")
    if not failures:
        manual_text = (target / "missing_manual_items.md").read_text(encoding="utf-8")
        for item in sorted(REQUIRED_MANUAL_ITEMS):
            if item not in manual_text:
                failures.append(f"missing_manual_item:{item}")
        combined = "\n".join(
            path.read_text(encoding="utf-8", errors="ignore")
            for path in target.iterdir()
            if path.is_file() and path.suffix == ".md"
        ).lower()
        for phrase in [
            "no phi",
            "no raw dicom",
            "not clinical validation",
            "not regulatory approval",
            "not certification",
            "device uid != udi-di",
            "fdo-style mapping only",
        ]:
            if phrase not in combined:
                failures.append(f"missing_boundary:{phrase}")
        if "doi claimed: true" in combined or "verified doi:" in combined:
            failures.append("doi_claimed_in_bundle")
        failures.extend(check_checksums(target))
    result = {"ok": not failures, "failures": failures, "target": str(target.relative_to(ROOT))}
    print(json.dumps(result, sort_keys=True))
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
