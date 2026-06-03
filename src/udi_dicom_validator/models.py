from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any


@dataclass(frozen=True)
class CheckResult:
    stage: str
    status: str
    code: str | None
    message: str
    evidence: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class RegistryResult:
    provider: str
    jurisdiction: str
    lookup_timestamp: str
    lookup_status: str
    summary: dict[str, Any]

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class ValidationReceipt:
    receipt_id: str
    generated_at: str
    validator_version: str
    profile_version: str
    ok: bool
    manifest_id: str
    primary_error_code: str | None
    validation_status: str
    checks: list[dict[str, Any]]
    inputs: dict[str, Any]
    registry: dict[str, Any]
    artifacts: dict[str, Any]
    warnings: list[str]
    claims_boundary: list[str]

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)
