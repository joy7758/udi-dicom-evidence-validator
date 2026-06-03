# Release Readiness v0.1.0

Release readiness: GO.

Blocking issues: none after local validation.

Non-blocking issues: live registry lookup is intentionally optional and not used
for deterministic fixture tests.

Exact commands:

```bash
pip install -e '.[dev,api]'
ruff check .
pytest -q
python demo/portable-ultrasound/run_demo.py
```

Suggested tag message: `v0.1.0 public MVP: minimal UDI-DICOM evidence manifest
and validator`.
