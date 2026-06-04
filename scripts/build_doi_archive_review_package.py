from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path
from typing import Any

from check_no_fake_doi import run_scan

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "artifacts" / "doi-archive-review-v0.8"
PUBLIC_REPO = "https://github.com/joy7758/udi-dicom-evidence-validator"
PUBLIC_TAG = "v0.7.0-public"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def git_value(args: list[str]) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def build_manifest(scan: dict[str, Any]) -> dict[str, Any]:
    return {
        "package_version": "v0.8",
        "status": "DOI_ARCHIVE_READY_PENDING_ZENODO_ENABLEMENT",
        "public_repository": PUBLIC_REPO,
        "baseline_public_tag": PUBLIC_TAG,
        "baseline_public_tag_target": git_value(["rev-parse", f"{PUBLIC_TAG}^{{}}"]),
        "current_branch": git_value(["branch", "--show-current"]),
        "doi_claimed": False,
        "doi_status": "DOI pending",
        "zenodo_record_url": None,
        "zenodo_enablement_required": True,
        "github_release_required_after_enablement": True,
        "public_validator_only": True,
        "private_suite_included": False,
        "private_service_included": False,
        "no_fake_doi_scan_ok": scan["ok"],
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
            "no robot operation evidence",
        ],
        "manual_gates": [
            "Zenodo GitHub integration enabled for public repository",
            "new GitHub Release created after Zenodo enablement",
            "Zenodo record URL returned",
            "real DOI returned and verified",
        ],
    }


def write_summary(manifest: dict[str, Any]) -> str:
    lines = [
        "# DOI Archive Readiness Summary v0.8",
        "",
        f"Status: `{manifest['status']}`",
        f"Public repository: `{manifest['public_repository']}`",
        f"Current branch: `{manifest['current_branch']}`",
        f"Baseline public tag: `{manifest['baseline_public_tag']}`",
        f"Baseline public tag target: `{manifest['baseline_public_tag_target']}`",
        "DOI claimed: `false`",
        "Zenodo record URL: none",
        "",
        "This package is DOI-ready review material only. It does not create a DOI,",
        "does not create a GitHub Release, and does not update citation metadata with",
        "an unverified DOI.",
        "",
        "Boundary: no PHI, no raw DICOM, not clinical validation, not regulatory",
        "approval, not certification, no fake DOI, Device UID != UDI-DI, offline",
        "fixture first, live openFDA explicit opt-in, FDO-style mapping only, and no",
        "robot operation evidence.",
        "",
    ]
    return "\n".join(lines)


def write_zenodo_steps() -> str:
    return """# Zenodo Manual Steps v0.8

1. Log in to Zenodo.
2. Authorize GitHub access in Zenodo.
3. Open the Zenodo GitHub integration page.
4. Use `Sync now` if the repository list is stale.
5. Enable `joy7758/udi-dicom-evidence-validator` with the repository toggle.
6. Confirm the public repository is enabled.
7. Create a new GitHub Release after enablement.
8. Wait for Zenodo archive processing.
9. Capture the real Zenodo record URL and DOI only after Zenodo returns them.

Do not enable or archive private suite or private service repositories for the
public DOI.
"""


def write_release_trigger_plan() -> str:
    return """# Public Release Trigger Plan v0.8

The Zenodo archive trigger is intentionally manual-gated:

1. Keep this branch as DOI readiness and paper finalization support only.
2. Do not write a DOI on this branch.
3. Have a human confirm Zenodo integration is enabled for the public repository.
4. Merge the public v0.8 PR only after review.
5. Create `v0.8.0-public` as a new GitHub Release after Zenodo enablement.
6. Treat the release state as `ZENODO_ARCHIVE_PENDING` until Zenodo returns a
   record URL and DOI.
7. Run a separate DOI capture PR after the record is verified.

Private suite and private service assets are excluded from this release plan.
"""


def checksums() -> None:
    files = sorted(
        path for path in OUT.iterdir() if path.is_file() and path.name != "SHA256SUMS.txt"
    )
    lines = [f"{sha256(path)}  {path.name}" for path in files]
    (OUT / "SHA256SUMS.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    scan = run_scan(
        [
            "README.md",
            "docs",
            "paper",
            "release",
            "CITATION.cff",
            "codemeta.json",
            ".zenodo.json",
        ]
    )
    manifest = build_manifest(scan)
    (OUT / "doi_readiness_manifest.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    (OUT / "doi_readiness_summary.md").write_text(write_summary(manifest), encoding="utf-8")
    (OUT / "zenodo_manual_steps.md").write_text(write_zenodo_steps(), encoding="utf-8")
    (OUT / "public_release_trigger_plan.md").write_text(
        write_release_trigger_plan(), encoding="utf-8"
    )
    (OUT / "no_fake_doi_scan.json").write_text(
        json.dumps(scan, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    checksums()
    print(
        json.dumps(
            {
                "output": str(OUT.relative_to(ROOT)),
                "doi_claimed": False,
                "status": manifest["status"],
                "no_fake_doi_scan_ok": scan["ok"],
            },
            sort_keys=True,
        )
    )
    if not scan["ok"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
