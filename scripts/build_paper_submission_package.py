from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "artifacts" / "paper-submission-v0.6"
SOURCES = [
    "paper/README.md",
    "paper/manuscript-outline.md",
    "paper/abstract.md",
    "paper/introduction.md",
    "paper/methods.md",
    "paper/evaluation.md",
    "paper/reproducibility.md",
    "paper/limitations.md",
    "paper/data-availability.md",
    "paper/ethics-and-safety-boundary.md",
    "paper/references-to-check.md",
    "paper/submission/README.md",
    "paper/submission/title-page.md",
    "paper/submission/abstract-structured.md",
    "paper/submission/cover-letter-neutral.md",
    "paper/submission/highlights.md",
    "paper/submission/software-metadata.md",
    "paper/submission/availability-statement.md",
    "paper/submission/reproducibility-statement.md",
    "paper/submission/ethics-statement.md",
    "paper/submission/limitations-statement.md",
    "paper/submission/author-contribution-draft.md",
    "paper/submission/conflict-of-interest-draft.md",
    "paper/submission/funding-statement-draft.md",
    "paper/submission/checklist-journal-neutral.md",
    "docs/reviewer-quickstart-v0.5.md",
    "docs/reviewer-checklist-v0.5.md",
    "docs/reviewer-expected-outputs-v0.5.md",
    "docs/reviewer-risk-boundary-v0.5.md",
    "docs/reproducibility-capsule-v0.5.md",
    "docs/doi-readiness-v0.6.md",
    "docs/archive-metadata-review.md",
]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def run(command: list[str]) -> None:
    subprocess.run(
        command,
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )


def source_entry(relative: str) -> dict[str, Any]:
    path = ROOT / relative
    return {"path": relative, "bytes": path.stat().st_size, "sha256": sha256(path)}


def build_reproduction_commands() -> str:
    commands = [
        "python scripts/generate_golden_receipts.py",
        "python scripts/check_golden_receipts.py",
        "python scripts/build_public_evaluation_matrix.py",
        "python scripts/build_public_release_assets.py",
        "python scripts/build_reproducibility_capsule.py",
        "python scripts/check_reproducibility_capsule.py artifacts/reproducibility-capsule-v0.5",
        "python scripts/build_archive_metadata_report.py",
        (
            "python scripts/check_archive_metadata_report.py "
            "artifacts/archive-metadata-report-v0.6.json"
        ),
        "python scripts/build_paper_submission_package.py",
        "python scripts/check_paper_submission_package.py artifacts/paper-submission-v0.6",
        "pytest -q",
        "ruff check .",
        "mypy src",
    ]
    lines = ["# Reproduction Commands v0.6", "", "| Command | Expected |", "| --- | --- |"]
    lines.extend(f"| `{command}` | exit code 0 |" for command in commands)
    lines.append("")
    return "\n".join(lines)


def build_expected_outputs() -> str:
    lines = [
        "# Reviewer Expected Outputs v0.6",
        "",
        "- `artifacts/public_evaluation_matrix.json` with `row_count >= 9`.",
        "- `artifacts/reproducibility-capsule-v0.5/` with checksum file.",
        (
            "- `artifacts/archive-metadata-report-v0.6.json` with `doi_ready=true` "
            "and no assigned DOI."
        ),
        "- `artifacts/paper-submission-v0.6/package_manifest.json` with public-safe sources only.",
        "- `pytest -q`, `ruff check .`, and `mypy src` pass.",
        "",
        "Boundary: synthetic public examples only; no PHI; no raw DICOM; not clinical validation; "
        "not regulatory approval; not certification.",
        "",
    ]
    return "\n".join(lines)


def build_summary(manifest: dict[str, Any]) -> str:
    lines = [
        "# Paper Submission Package Summary v0.6",
        "",
        f"Source file count: {manifest['source_file_count']}",
        f"Reproducibility capsule files: {manifest['reproducibility_capsule_file_count']}",
        f"Archive metadata report: `{manifest['archive_metadata_report']}`",
        "",
        "Contribution boundary:",
        "",
        "- minimal UDI-DICOM evidence manifest profile",
        "- deterministic reference validator",
        "- synthetic public examples",
        "- golden receipt regression",
        "- reproducibility capsule",
        "- public release asset verification",
        "",
        "No PHI, no raw DICOM, not clinical validation, not regulatory approval, "
        "not certification, no fake DOI, no private suite exposure.",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    run([sys.executable, "scripts/build_reproducibility_capsule.py"])
    run([sys.executable, "scripts/build_archive_metadata_report.py"])
    OUT.mkdir(parents=True, exist_ok=True)
    capsule_files = sorted((ROOT / "artifacts" / "reproducibility-capsule-v0.5").glob("*"))
    manifest = {
        "package_version": "v0.6",
        "public_only": True,
        "synthetic_examples_only": True,
        "no_phi": True,
        "raw_dicom_included": False,
        "private_repo_material_included": False,
        "doi_claimed": False,
        "source_file_count": len(SOURCES),
        "sources": [source_entry(relative) for relative in SOURCES],
        "reproducibility_capsule_file_count": len(
            [path for path in capsule_files if path.is_file()]
        ),
        "archive_metadata_report": "artifacts/archive-metadata-report-v0.6.json",
        "allowed_public_release": "v0.5.0-public",
        "boundary": [
            "no PHI",
            "no raw DICOM",
            "not clinical validation",
            "not regulatory approval",
            "not certification",
            "Device UID != UDI-DI",
            "offline fixture first",
            "live openFDA explicit opt-in",
            "FDO-style mapping only",
        ],
    }
    (OUT / "package_manifest.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    (OUT / "package_summary.md").write_text(build_summary(manifest), encoding="utf-8")
    (OUT / "reproduction_commands.md").write_text(build_reproduction_commands(), encoding="utf-8")
    (OUT / "reviewer_expected_outputs.md").write_text(build_expected_outputs(), encoding="utf-8")
    files = sorted(
        path for path in OUT.iterdir() if path.is_file() and path.name != "SHA256SUMS.txt"
    )
    checksums = {path.name: sha256(path) for path in files}
    (OUT / "SHA256SUMS.txt").write_text(
        "".join(f"{digest}  {name}\n" for name, digest in sorted(checksums.items())),
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "output": str(OUT.relative_to(ROOT)),
                "public_only": True,
                "source_file_count": len(SOURCES),
                "doi_claimed": False,
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
