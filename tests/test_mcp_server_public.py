from __future__ import annotations

import pytest

from udi_dicom_validator import mcp_server


def test_public_mcp_tools_list_examples_and_validate() -> None:
    versions = mcp_server.list_profile_versions()
    assert "v0.2.0" in versions["profile_versions"]
    examples = mcp_server.list_public_examples()
    assert "v0.2/manifest_v0.2.pass.json" in examples["examples"]
    result = mcp_server.validate_public_manifest_fixture("v0.2/manifest_v0.2.pass.json")
    assert result["ok"] is True
    assert result["trace_id"] == "trace-v02-portable-ultrasound-001"


def test_public_mcp_error_definition() -> None:
    definition = mcp_server.get_error_code_definition("missing_udi")
    assert "UDI" in definition["definition"]


def test_public_mcp_blocks_private_tools_and_paths() -> None:
    with pytest.raises(ValueError):
        mcp_server.call_tool("run_private_suite")
    with pytest.raises(ValueError):
        mcp_server.validate_public_manifest_fixture("../cases/private/example.json")


def test_public_mcp_allows_safe_public_example_under_private_system_path(
    tmp_path, monkeypatch
) -> None:
    public_root = tmp_path / "private" / "repo" / "examples" / "public"
    public_root.mkdir(parents=True)
    fixture = public_root / "manifest.pass.json"
    fixture.write_text("{}", encoding="utf-8")
    monkeypatch.setattr(mcp_server, "PUBLIC_EXAMPLES", public_root)
    assert mcp_server._ensure_public_example(fixture) == fixture.resolve()
