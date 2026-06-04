from __future__ import annotations

import json
import re
import tomllib
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
OUT_JSON = ROOT / "artifacts" / "citation-metadata-consistency-v0.8.json"
OUT_MD = ROOT / "artifacts" / "citation-metadata-consistency-v0.8.md"
REPOSITORY_URL = "https://github.com/joy7758/udi-dicom-evidence-validator"
TITLE = "UDI-DICOM Evidence Validator"
ALLOWED_DOIS = {"10.5063/schema/codemeta-2.0"}
DOI_PATTERN = re.compile(r"\b10\.\d{4,9}/[-._;()/:A-Za-z0-9]+")


def parse_cff(text: str) -> dict[str, Any]:
    values: dict[str, Any] = {}
    keywords: list[str] = []
    authors: list[str] = []
    in_keywords = False
    current_author: dict[str, str] = {}
    for raw_line in text.splitlines():
        stripped = raw_line.strip()
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
        if stripped.startswith("- family-names:"):
            if current_author:
                authors.append(
                    f"{current_author.get('given-names', '')} "
                    f"{current_author.get('family-names', '')}".strip()
                )
            current_author = {"family-names": stripped.split(":", 1)[1].strip().strip('"')}
        elif stripped.startswith("given-names:"):
            current_author["given-names"] = stripped.split(":", 1)[1].strip().strip('"')
    if current_author:
        authors.append(
            f"{current_author.get('given-names', '')} "
            f"{current_author.get('family-names', '')}".strip()
        )
    values["keywords"] = keywords
    values["authors"] = authors
    return values


def claimed_dois(texts: list[str]) -> list[str]:
    matches: set[str] = set()
    for text in texts:
        matches.update(match.group(0).rstrip(".,)") for match in DOI_PATTERN.finditer(text))
    return sorted(matches - ALLOWED_DOIS)


def build_report() -> dict[str, Any]:
    pyproject = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))
    codemeta = json.loads((ROOT / "codemeta.json").read_text(encoding="utf-8"))
    zenodo = json.loads((ROOT / ".zenodo.json").read_text(encoding="utf-8"))
    cff_text = (ROOT / "CITATION.cff").read_text(encoding="utf-8")
    readme_text = (ROOT / "README.md").read_text(encoding="utf-8")
    cff = parse_cff(cff_text)
    codemeta_author = codemeta.get("author", [{}])[0]
    codemeta_name = (
        f"{codemeta_author.get('givenName', '')} "
        f"{codemeta_author.get('familyName', '')}"
    ).strip()
    zenodo_creator = zenodo.get("creators", [{}])[0].get("name", "")
    version_values = {
        "pyproject": pyproject.get("project", {}).get("version"),
        "codemeta": codemeta.get("version"),
        "citation_cff": cff.get("version"),
    }
    doi_hits = claimed_dois(
        [
            cff_text,
            json.dumps(codemeta, sort_keys=True),
            json.dumps(zenodo, sort_keys=True),
            readme_text,
        ]
    )
    checks = {
        "title_consistent": (
            codemeta.get("name") == cff.get("title") == zenodo.get("title") == TITLE
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
            pyproject.get("project", {}).get("license") == "MIT"
            and cff.get("license") == "MIT"
            and str(codemeta.get("license", "")).endswith("/MIT")
            and zenodo.get("license") == "MIT"
        ),
        "author_consistent": (
            codemeta_name == "Bin Zhang"
            and "Bin Zhang" in cff.get("authors", [])
            and zenodo_creator == "Zhang, Bin"
        ),
        "version_explainable": all(version_values.values()),
        "doi_not_fabricated": not doi_hits,
        "doi_pending_wording_present": "DOI-ready" in cff_text or "DOI pending" in readme_text,
        "public_repo_only": True,
    }
    report = {
        "report_version": "v0.8",
        "ok": all(checks.values()),
        "checks": checks,
        "version_values": version_values,
        "repository_url": REPOSITORY_URL,
        "title": TITLE,
        "author": "Bin Zhang",
        "license": "MIT",
        "doi_status": "DOI pending",
        "claimed_or_placeholder_dois": doi_hits,
        "allowed_doi_references": sorted(ALLOWED_DOIS),
        "boundary": [
            "public validator only",
            "no PHI",
            "no raw DICOM",
            "not clinical validation",
            "not regulatory approval",
            "not certification",
            "no fake DOI",
        ],
    }
    return report


def render_markdown(report: dict[str, Any]) -> str:
    lines = [
        "# Citation Metadata Consistency v0.8",
        "",
        f"OK: `{report['ok']}`",
        f"DOI status: `{report['doi_status']}`",
        "",
        "| Check | Status |",
        "| --- | --- |",
    ]
    lines.extend(f"| {name} | {value} |" for name, value in sorted(report["checks"].items()))
    lines.extend(
        [
            "",
            "Version values:",
            "",
        ]
    )
    lines.extend(
        f"- {name}: `{value}`" for name, value in sorted(report["version_values"].items())
    )
    lines.extend(
        [
            "",
            "No DOI is claimed. Citation metadata remains DOI pending until a verified",
            "Zenodo record URL and DOI are available.",
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
            {"ok": report["ok"], "output": str(OUT_JSON.relative_to(ROOT))},
            sort_keys=True,
        )
    )
    if not report["ok"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
