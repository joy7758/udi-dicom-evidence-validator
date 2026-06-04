from __future__ import annotations

import argparse
import json
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_REPO = "joy7758/udi-dicom-evidence-validator"
DEFAULT_RELEASE_TAG = "v0.3.0-public"
DEFAULT_INVENTORY_TAG = "v0.3.0-public-inventory"
PUBLIC_ASSET_ALLOWLIST = {
    "public-artifact-inventory.md",
    "public-evaluation-matrix.md",
    "public-release-notes-v0.3.0.md",
    "public_evaluation_matrix.json",
    "reproducibility-checklist.md",
    "SHA256SUMS.txt",
    "udi-dicom-evidence-validator-v0.3.0-public-source.zip",
    "udi-dicom-evidence-validator-v0.3.0-public-inventory-source.zip",
    "v0.2.0-release-notes.md",
    "v0.3.0-roadmap.md",
}
FORBIDDEN_ASSET_MARKERS = (
    "private",
    "patient",
    "phi",
    ".dcm",
    ".dicom",
    "clinical-validation",
    "regulatory-approval",
    "certification",
)


@dataclass(frozen=True)
class CommandResult:
    returncode: int
    stdout: str


def run_command(args: list[str], cwd: Path = ROOT) -> CommandResult:
    proc = subprocess.run(
        args,
        cwd=cwd,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    return CommandResult(proc.returncode, proc.stdout.strip())


def parse_ls_remote(output: str) -> dict[str, str]:
    refs: dict[str, str] = {}
    for line in output.splitlines():
        parts = line.split()
        if len(parts) == 2:
            refs[parts[1]] = parts[0]
    return refs


def is_public_safe_asset(name: str) -> bool:
    lower_name = name.lower()
    if any(marker in lower_name for marker in FORBIDDEN_ASSET_MARKERS):
        return False
    return name in PUBLIC_ASSET_ALLOWLIST


def normalize_repo_url(url: str) -> str:
    normalized = url.strip().rstrip("/")
    if normalized.endswith(".git"):
        normalized = normalized[:-4]
    return normalized


def gh_release_assets(repo: str, tag: str) -> list[str]:
    result = run_command(
        [
            "gh",
            "release",
            "view",
            tag,
            "-R",
            repo,
            "--json",
            "assets",
        ]
    )
    if result.returncode != 0:
        raise RuntimeError(result.stdout)
    payload = json.loads(result.stdout)
    return sorted(asset["name"] for asset in payload.get("assets", []))


def verify(repo: str, release_tag: str, inventory_tag: str) -> dict[str, Any]:
    origin = run_command(["git", "remote", "get-url", "origin"])
    local_origin_main = run_command(["git", "rev-parse", "origin/main"])
    remote_heads = run_command(["git", "ls-remote", "--heads", "origin", "main"])
    remote_tags = run_command(
        ["git", "ls-remote", "--tags", "origin", release_tag, inventory_tag]
    )
    if origin.returncode != 0:
        return {"ok": False, "reason": "origin_missing", "detail": origin.stdout}
    if remote_heads.returncode != 0 or remote_tags.returncode != 0:
        return {"ok": False, "reason": "git_remote_check_failed"}

    head_refs = parse_ls_remote(remote_heads.stdout)
    tag_refs = parse_ls_remote(remote_tags.stdout)
    assets = gh_release_assets(repo, release_tag)
    unsafe_assets = [name for name in assets if not is_public_safe_asset(name)]
    missing_assets = sorted(PUBLIC_ASSET_ALLOWLIST - set(assets))
    expected_origin = f"https://github.com/{repo}"
    normalized_origin = normalize_repo_url(origin.stdout)

    checks = {
        "origin_url": origin.stdout,
        "origin_matches_repo": normalized_origin == expected_origin,
        "expected_origin_url": expected_origin,
        "remote_main": head_refs.get("refs/heads/main"),
        "local_origin_main": (
            local_origin_main.stdout if local_origin_main.returncode == 0 else None
        ),
        "remote_main_present": "refs/heads/main" in head_refs,
        "remote_main_matches_local_origin_main": (
            local_origin_main.returncode != 0
            or head_refs.get("refs/heads/main") == local_origin_main.stdout
        ),
        "release_tag_present": f"refs/tags/{release_tag}" in tag_refs,
        "inventory_tag_present": f"refs/tags/{inventory_tag}" in tag_refs,
        "release_assets": assets,
        "missing_assets": missing_assets,
        "unsafe_assets": unsafe_assets,
    }
    checks["ok"] = all(
        [
            checks["origin_matches_repo"],
            checks["remote_main_present"],
            checks["remote_main_matches_local_origin_main"],
            checks["release_tag_present"],
            checks["inventory_tag_present"],
            not missing_assets,
            not unsafe_assets,
        ]
    )
    return checks


def main() -> None:
    parser = argparse.ArgumentParser(description="Verify public remote release state.")
    parser.add_argument("--repo", default=DEFAULT_REPO)
    parser.add_argument("--release-tag", default=DEFAULT_RELEASE_TAG)
    parser.add_argument("--inventory-tag", default=DEFAULT_INVENTORY_TAG)
    args = parser.parse_args()
    result = verify(args.repo, args.release_tag, args.inventory_tag)
    print(json.dumps(result, indent=2, sort_keys=True))
    if not result.get("ok"):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
