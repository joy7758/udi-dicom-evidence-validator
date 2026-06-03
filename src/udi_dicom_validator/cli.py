from __future__ import annotations

import json
from pathlib import Path

import typer

from .checks import validate_files
from .dicom_extract import extract_dicom_file
from .report import render_report

app = typer.Typer(help="Validate synthetic UDI-DICOM evidence manifests.")


@app.command("validate-manifest")
def validate_manifest_command(
    manifest: Path = typer.Option(..., exists=True),
    dicom_metadata: Path = typer.Option(..., exists=True),
    registry_fixture: Path | None = typer.Option(None, exists=True),
    out_dir: Path = typer.Option(...),
) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    receipt = validate_files(manifest, dicom_metadata, registry_fixture)
    receipt_path = out_dir / "receipt.json"
    report_path = out_dir / "report.md"
    receipt_path.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    report_path.write_text(render_report(receipt), encoding="utf-8")
    typer.echo(
        f"{'PASS' if receipt['ok'] else 'FAIL'} manifest_id={receipt['manifest_id']} "
        f"primary_error_code={receipt['primary_error_code']} report={report_path}"
    )


@app.command("render-report")
def render_report_command(
    receipt: Path = typer.Option(..., exists=True),
    out: Path = typer.Option(...),
) -> None:
    data = json.loads(receipt.read_text(encoding="utf-8"))
    out.write_text(render_report(data), encoding="utf-8")
    typer.echo(str(out))


@app.command("inspect-dicom")
def inspect_dicom_command(
    dicom_file: Path = typer.Option(..., exists=True),
    out: Path = typer.Option(...),
) -> None:
    metadata, warnings = extract_dicom_file(dicom_file)
    out.write_text(
        json.dumps({"metadata": metadata, "warnings": warnings}, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    typer.echo(str(out))


if __name__ == "__main__":
    app()
