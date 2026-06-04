from __future__ import annotations

import hashlib
import json
import shutil
import subprocess
import sys
import zipfile
from collections.abc import Iterable
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "artifacts" / "public-release"
PUBLIC_FILES = [
    "README.md",
    "LICENSE",
    "NOTICE",
    "CITATION.cff",
    "codemeta.json",
    "llms.txt",
    "AGENTS.md",
    "artifacts/public_evaluation_matrix.json",
    "docs/public-evaluation-matrix.md",
    "docs/remote-reproducibility.md",
    "docs/external-review-brief.md",
    "docs/external-review-checklist.md",
    "docs/reproducibility-for-reviewers.md",
    "docs/public-demo-script.md",
    "docs/known-limitations-v0.4.md",
    "docs/citation-and-archiving.md",
    "release/reproducibility-checklist.md",
    "release/public-artifact-inventory.md",
    "release/v0.4.0-roadmap.md",
]
FORBIDDEN_PARTS = {
    "udi-dicom-conformance-suite-private",
    "udi-dicom-sample-validation-service-private",
}
FORBIDDEN_EXTENSIONS = {".dcm", ".dicom"}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def assert_public_safe(paths: Iterable[Path]) -> None:
    for path in paths:
        lower = str(path).lower()
        if path.suffix.lower() in FORBIDDEN_EXTENSIONS:
            raise RuntimeError(f"raw DICOM asset blocked: {path}")
        if any(part in lower for part in FORBIDDEN_PARTS):
            raise RuntimeError(f"private repository path blocked: {path}")


def copy_public_files() -> list[Path]:
    OUT.mkdir(parents=True, exist_ok=True)
    copied: list[Path] = []
    for relative in PUBLIC_FILES:
        source = ROOT / relative
        if not source.exists():
            continue
        destination = OUT / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)
        copied.append(destination)
    return copied


def build_source_zip() -> Path:
    output = OUT / "udi-dicom-evidence-validator-public-worktree-source.zip"
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for relative in sorted(PUBLIC_FILES):
            source = ROOT / relative
            if source.exists():
                info = zipfile.ZipInfo(f"udi-dicom-evidence-validator/{relative}")
                info.date_time = (2026, 6, 4, 0, 0, 0)
                info.external_attr = 0o644 << 16
                archive.writestr(info, source.read_bytes())
    return output


def main() -> None:
    subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "generate_golden_receipts.py")],
        check=True,
    )
    subprocess.run([sys.executable, str(ROOT / "scripts" / "check_golden_receipts.py")], check=True)
    subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "build_public_evaluation_matrix.py")],
        check=True,
    )
    if OUT.exists():
        shutil.rmtree(OUT)
    copied = copy_public_files()
    source_zip = build_source_zip()
    all_assets = copied + [source_zip]
    assert_public_safe(all_assets)
    checksums = {str(path.relative_to(OUT)): sha256(path) for path in sorted(all_assets)}
    (OUT / "SHA256SUMS.txt").write_text(
        "".join(f"{digest}  {name}\n" for name, digest in sorted(checksums.items())),
        encoding="utf-8",
    )
    summary = {
        "asset_count": len(all_assets) + 1,
        "output_dir": str(OUT.relative_to(ROOT)),
        "public_only": True,
        "raw_dicom_included": False,
        "private_repo_assets_included": False,
    }
    (OUT / "public-release-summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(summary, sort_keys=True))


if __name__ == "__main__":
    main()
