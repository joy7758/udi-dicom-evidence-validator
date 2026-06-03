from __future__ import annotations

from udi_dicom_validator.checks import validate_files

__all__ = ["validate_files"]


if __name__ == "__main__":
    from udi_dicom_validator.cli import app

    app()
