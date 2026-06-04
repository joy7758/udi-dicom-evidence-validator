from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any

DEFAULT_REPO_URL = "https://github.com/joy7758/udi-dicom-evidence-validator.git"
DEFAULT_BRANCH = "main"


def run(args: list[str], cwd: Path) -> dict[str, Any]:
    proc = subprocess.run(
        args,
        cwd=cwd,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    return {"cmd": args, "returncode": proc.returncode, "output": proc.stdout[-4000:]}


def smoke(repo_url: str, branch: str, keep_workspace: bool = False) -> dict[str, Any]:
    workspace = Path(tempfile.mkdtemp(prefix="udi-dicom-clean-clone-"))
    clone_dir = workspace / "repo"
    venv_dir = workspace / "venv"
    python_bin = venv_dir / ("Scripts/python.exe" if os.name == "nt" else "bin/python")
    steps: list[dict[str, Any]] = []
    try:
        steps.append(
            run(
                ["git", "clone", "--depth", "1", "--branch", branch, repo_url, str(clone_dir)],
                workspace,
            )
        )
        if steps[-1]["returncode"] != 0:
            return {"ok": False, "workspace": str(workspace), "steps": steps}
        steps.append(run([sys.executable, "-m", "venv", str(venv_dir)], workspace))
        if steps[-1]["returncode"] != 0:
            return {"ok": False, "workspace": str(workspace), "steps": steps}
        commands = [
            [str(python_bin), "-m", "pip", "install", "-U", "pip"],
            [str(python_bin), "-m", "pip", "install", "-e", ".[dev,api]"],
            [str(python_bin), "-m", "pytest", "-q"],
            [str(python_bin), "scripts/check_golden_receipts.py"],
            [str(python_bin), "scripts/build_public_evaluation_matrix.py"],
            [str(python_bin), "demo/portable-ultrasound/run_demo.py"],
        ]
        for command in commands:
            steps.append(run(command, clone_dir))
            if steps[-1]["returncode"] != 0:
                return {"ok": False, "workspace": str(workspace), "steps": steps}
        return {"ok": True, "workspace": str(workspace), "steps": steps}
    finally:
        if not keep_workspace:
            shutil.rmtree(workspace, ignore_errors=True)


def main() -> None:
    parser = argparse.ArgumentParser(description="Run a clean clone public smoke test.")
    parser.add_argument("--repo-url", default=DEFAULT_REPO_URL)
    parser.add_argument("--branch", default=DEFAULT_BRANCH)
    parser.add_argument("--keep-workspace", action="store_true")
    args = parser.parse_args()
    result = smoke(args.repo_url, args.branch, args.keep_workspace)
    print(json.dumps(result, indent=2, sort_keys=True))
    if not result["ok"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
