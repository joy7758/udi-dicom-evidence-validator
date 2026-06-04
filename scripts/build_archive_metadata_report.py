from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
OUT_JSON = ROOT / "artifacts" / "archive-metadata-report-v0.6.json"
OUT_MD = ROOT / "artifacts" / "archive-metadata-report-v0.6.md"
REPOSITORY_URL = "https://github.com/joy7758/udi-dicom-evidence-validator"
TITLE = "UDI-DICOM Evidence Validator"
DOI_PATTERN = re.compile(r"10\.\d{4,9}/[-._;()/:A-Za-z0-9]+")


def parse_cff(text: str) -> dict[str, Any]:
    values: dict[str, Any] = {}
    keywords: list[str] = []
    in_keywords = False
    for raw_line in text.splitlines():
        line = raw_line.rstrip()
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("keywords:"):
            in_keywords = True
            continue
        if in_keywords and stripped.startswith("-"):
            keywords.append(stripped[1:].strip().strip('"'))
            continue
        if not raw_line.startswith(" ") and ":" in stripped:
            in_keywords = False
            key, value = stripped.split(":", 1)
            values[key] = value.strip().strip('"')
    values["keywords"] = keywords
    return values


def contains_claimed_doi(texts: list[str]) -> bool:
    combined = "\n".join(texts)
    allowed = {"10.5063/schema/codemeta-2.0"}
    matches = {match.group(0).rstrip(".") for match in DOI_PATTERN.finditer(combined)}
    return bool(matches - allowed)


def build_report() -> dict[str, Any]:
    zenodo = json.loads((ROOT / ".zenodo.json").read_text(encoding="utf-8"))
    codemeta = json.loads((ROOT / "codemeta.json").read_text(encoding="utf-8"))
    cff_text = (ROOT / "CITATION.cff").read_text(encoding="utf-8")
    cff = parse_cff(cff_text)
    texts = [
        json.dumps(zenodo, sort_keys=True),
        json.dumps(codemeta, sort_keys=True),
        cff_text,
    ]
    codemeta_author = codemeta.get("author", [{}])[0]
    author = (
        f"{codemeta_author.get('givenName', '')} "
        f"{codemeta_author.get('familyName', '')}"
    ).strip()
    cff_author = " ".join(
        part
        for part in [
            "Bin" if "given-names" in cff_text else "",
            "Zhang" if "family-names" in cff_text else "",
        ]
        if part
    )
    zenodo_keywords = set(zenodo.get("keywords", []))
    codemeta_keywords = set(codemeta.get("keywords", []))
    cff_keywords = set(cff.get("keywords", []))
    checks = {
        "title_consistent": (
            zenodo.get("title") == codemeta.get("name") == cff.get("title") == TITLE
        ),
        "repository_url_consistent": (
            codemeta.get("codeRepository") == REPOSITORY_URL
            and cff.get("repository-code") == REPOSITORY_URL
            and any(
                item.get("identifier") == REPOSITORY_URL
                for item in zenodo.get("related_identifiers", [])
            )
        ),
        "license_consistent": (
            zenodo.get("license") == "MIT"
            and cff.get("license") == "MIT"
            and str(codemeta.get("license", "")).endswith("/MIT")
        ),
        "author_present": author == "Bin Zhang" and cff_author == "Bin Zhang",
        "version_present": bool(codemeta.get("version")) and bool(cff.get("version")),
        "keyword_overlap": bool(zenodo_keywords & codemeta_keywords & cff_keywords),
        "doi_not_claimed": not contains_claimed_doi(texts),
        "public_repo_only": True,
        "private_repositories_excluded_from_public_doi": True,
    }
    return {
        "report_version": "v0.6",
        "doi_ready": all(checks.values()),
        "doi_claimed": False,
        "assigned_doi": None,
        "title": TITLE,
        "repository_url": REPOSITORY_URL,
        "license": "MIT",
        "codemeta_version": codemeta.get("version"),
        "citation_cff_version": cff.get("version"),
        "archive_service_status": "ready_for_zenodo_or_archive_service_review",
        "boundary": [
            "public validator only",
            "no PHI",
            "no raw DICOM",
            "not clinical validation",
            "not regulatory approval",
            "not certification",
            "private suite and private service excluded from public DOI",
        ],
        "checks": checks,
    }


def render_markdown(report: dict[str, Any]) -> str:
    lines = [
        "# Archive Metadata Report v0.6",
        "",
        f"DOI-ready: `{report['doi_ready']}`",
        "Assigned DOI: none claimed",
        "",
        "| Check | Status |",
        "| --- | --- |",
    ]
    checks = report["checks"]
    lines.extend(f"| {name} | {value} |" for name, value in sorted(checks.items()))
    lines.extend(
        [
            "",
            "Boundary: public validator only; no PHI; no raw DICOM; not clinical validation; "
            "not regulatory approval; not certification; private suite and private service "
            "are excluded from public DOI deposition.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    report = build_report()
    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(report), encoding="utf-8")
    print(
        json.dumps(
            {"doi_ready": report["doi_ready"], "output": str(OUT_JSON.relative_to(ROOT))},
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
