from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FILES = {
    "doi_readiness_manifest.json",
    "doi_readiness_summary.md",
    "zenodo_manual_steps.md",
    "public_release_trigger_plan.md",
    "no_fake_doi_scan.json",
    "SHA256SUMS.txt",
}
REQUIRED_BOUNDARY = {
    "no PHI",
    "no raw DICOM",
    "not clinical validation",
    "not regulatory approval",
    "not certification",
    "Device UID != UDI-DI",
    "offline fixture first",
    "live openFDA explicit opt-in",
    "FDO-style mapping only",
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
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "artifacts/doi-archive-review-v0.8"
    if not target.is_absolute():
        target = ROOT / target
    failures: list[str] = []
    for name in sorted(REQUIRED_FILES):
        if not (target / name).exists():
            failures.append(f"missing:{name}")
    if not failures:
        manifest = json.loads((target / "doi_readiness_manifest.json").read_text(encoding="utf-8"))
        scan = json.loads((target / "no_fake_doi_scan.json").read_text(encoding="utf-8"))
        if manifest.get("doi_claimed") is not False:
            failures.append("doi_claimed_not_false")
        if manifest.get("zenodo_record_url") is not None:
            failures.append("zenodo_record_url_not_none")
        if manifest.get("zenodo_enablement_required") is not True:
            failures.append("zenodo_enablement_required_not_true")
        if manifest.get("public_validator_only") is not True:
            failures.append("public_validator_only_not_true")
        if manifest.get("private_suite_included") is not False:
            failures.append("private_suite_included_not_false")
        if manifest.get("private_service_included") is not False:
            failures.append("private_service_included_not_false")
        if scan.get("ok") is not True:
            failures.append("no_fake_doi_scan_not_ok")
        boundary = set(manifest.get("boundary", []))
        for phrase in sorted(REQUIRED_BOUNDARY):
            if phrase not in boundary:
                failures.append(f"missing_boundary:{phrase}")
        failures.extend(check_checksums(target))
    result = {"ok": not failures, "failures": failures, "target": str(target.relative_to(ROOT))}
    print(json.dumps(result, sort_keys=True))
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
