from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "artifacts" / "paper-finalization-bundle-v0.8"
PAPER_SECTIONS = [
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
    "paper/software-architecture.md",
    "paper/references-to-check.md",
    "paper/submission/README.md",
    "paper/submission/title-page.md",
    "paper/submission/abstract-structured.md",
    "paper/submission/availability-statement.md",
    "paper/submission/reproducibility-statement.md",
    "paper/submission/ethics-statement.md",
    "paper/submission/limitations-statement.md",
]
MANUAL_ITEMS = [
    "title",
    "target journal",
    "final abstract",
    "reference verification",
    "figure rendering",
    "DOI insertion after Zenodo record exists",
]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def source_rows() -> list[dict[str, str | int]]:
    rows: list[dict[str, str | int]] = []
    for relative in PAPER_SECTIONS:
        path = ROOT / relative
        rows.append({"path": relative, "bytes": path.stat().st_size, "sha256": sha256(path)})
    return rows


def write_section_index(rows: list[dict[str, str | int]]) -> str:
    lines = [
        "# Manuscript Sections Index v0.8",
        "",
        "| Path | Bytes | SHA-256 |",
        "| --- | ---: | --- |",
    ]
    lines.extend(f"| {row['path']} | {row['bytes']} | {row['sha256']} |" for row in rows)
    lines.append("")
    return "\n".join(lines)


def write_finalization_checklist() -> str:
    return """# Finalization Checklist v0.8

- Confirm final title and target journal.
- Confirm final abstract and journal-specific word limits.
- Verify references manually; do not fabricate references.
- Render and inspect figures manually.
- Confirm data availability is public synthetic examples only.
- Confirm software availability points to the public validator only.
- Confirm no PHI, no raw DICOM, no clinical validation, no regulatory approval,
  and no certification.
- Confirm Device UID != UDI-DI and FDO-style mapping only.
- Insert DOI only after a verified Zenodo record exists.
"""


def write_reviewer_command_sheet() -> str:
    return """# Reviewer Command Sheet v0.8

```bash
python -m venv .venv
. .venv/bin/activate
python -m pip install -e ".[dev,api]"
python scripts/generate_golden_receipts.py
python scripts/check_golden_receipts.py
python scripts/build_public_evaluation_matrix.py
python scripts/build_reproducibility_capsule.py
python scripts/check_reproducibility_capsule.py artifacts/reproducibility-capsule-v0.5
python scripts/build_doi_archive_review_package.py
python scripts/check_doi_archive_review_package.py artifacts/doi-archive-review-v0.8
python scripts/build_paper_finalization_bundle.py
python scripts/check_paper_finalization_bundle.py artifacts/paper-finalization-bundle-v0.8
pytest -q
```
"""


def write_reproducibility_summary() -> str:
    return """# Reproducibility Summary v0.8

The public paper should cite reproducible public surfaces only:

- synthetic public examples
- deterministic golden receipts
- public evaluation matrix
- reproducibility capsule
- DOI archive readiness package
- paper finalization bundle

No private suite, private service, PHI, raw DICOM, or real hospital data is part
of this bundle.
"""


def write_citation_metadata_status() -> str:
    return """# Citation Metadata Status v0.8

- `CITATION.cff`: DOI pending.
- `codemeta.json`: DOI pending.
- `.zenodo.json`: DOI pending.
- `pyproject.toml`: version is package-level and does not claim DOI.
- README citation section: DOI pending until a real Zenodo record exists.

No DOI is written in this bundle.
"""


def write_limitations_boundary_check() -> str:
    return """# Limitations Boundary Check v0.8

Required limitations:

- no PHI
- no raw DICOM
- synthetic examples only
- not clinical validation
- not regulatory approval
- not certification
- not PACS or VNA replacement
- Device UID != UDI-DI
- offline fixture first
- live openFDA explicit opt-in
- FDO-style mapping only
- no robot operation evidence
"""


def write_missing_manual_items() -> str:
    lines = ["# Missing Manual Items v0.8", ""]
    lines.extend(f"- {item}" for item in MANUAL_ITEMS)
    lines.append("")
    return "\n".join(lines)


def checksums() -> None:
    files = sorted(
        path for path in OUT.iterdir() if path.is_file() and path.name != "SHA256SUMS.txt"
    )
    lines = [f"{sha256(path)}  {path.name}" for path in files]
    (OUT / "SHA256SUMS.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    rows = source_rows()
    (OUT / "manuscript_sections_index.md").write_text(write_section_index(rows), encoding="utf-8")
    (OUT / "finalization_checklist.md").write_text(write_finalization_checklist(), encoding="utf-8")
    (OUT / "reviewer_command_sheet.md").write_text(write_reviewer_command_sheet(), encoding="utf-8")
    (OUT / "reproducibility_summary.md").write_text(
        write_reproducibility_summary(), encoding="utf-8"
    )
    (OUT / "citation_metadata_status.md").write_text(
        write_citation_metadata_status(), encoding="utf-8"
    )
    (OUT / "limitations_boundary_check.md").write_text(
        write_limitations_boundary_check(), encoding="utf-8"
    )
    (OUT / "missing_manual_items.md").write_text(write_missing_manual_items(), encoding="utf-8")
    checksums()
    print(
        json.dumps(
            {
                "output": str(OUT.relative_to(ROOT)),
                "manual_item_count": len(MANUAL_ITEMS),
                "source_file_count": len(rows),
                "doi_claimed": False,
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
