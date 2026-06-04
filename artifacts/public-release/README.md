# UDI-DICOM Evidence Validator

<p align="center">
  <b>Bridging the gap between UDI registry records and DICOM equipment metadata.</b><br>
  <i>For public, synthetic review of UDI-DICOM evidence-chain consistency across device metadata, PACS/VNA governance, and AI training-data provenance workflows.</i>
</p>

Minimal public validator for a synthetic UDI-DICOM evidence manifest profile.
It checks whether DICOM equipment metadata, a manifest, registry evidence, and
declared artifacts form a deterministic review packet.

This is not clinical validation, not regulatory approval, not safety assurance,
not certification, and not a replacement for PACS, VNA, asset management, or
manufacturer quality systems. Public examples are synthetic and contain no PHI.

## Project plan / 项目总方案

本仓库实现 UDI-DICOM（Unique Device Identification–Digital Imaging and
Communications in Medicine，唯一器械标识—医学数字成像与通信）医疗设备影像工作流最小证据清单与验证器。

公开安全版总方案维护在：
https://github.com/joy7758/agent-evidence/blob/main/docs/medical-imaging-traceability/udi-dicom-total-plan-public.md

该总方案包含 project positioning（project positioning，项目定位）、public layer
（public layer，公开层）、controlled layer（controlled layer，受控层）、service layer
（service layer，服务层）、minimal manifest fields（minimal manifest fields，最小证据清单字段）、
reference validator logic（reference validator logic，参考验证器逻辑）和 boundary statements
（boundary statements，边界声明）。

## Who Needs This Validator?

This public reference validator is useful when teams need a reproducible,
software-level review of UDI-DICOM metadata consistency without exposing real
samples, PHI, raw DICOM, private conformance cases, or service workflows.

**Medical device manufacturers.** Use the synthetic manifest profile and public
fixtures to check whether expected DICOM UDI macro evidence is represented
consistently before internal submission-readiness review. This does not
establish 510(k), NMPA, EU MDR, or other regulatory acceptance.

**Hospital IT and PACS/VNA administrators.** Use deterministic validation
receipts to reason about metadata consistency patterns that can affect asset
inventory, migration review, and governance discussions. This does not replace
PACS, VNA, CMMS, or manufacturer quality systems.

**Medical AI data engineers.** Use the Device UID versus UDI-DI boundary checks
to audit synthetic metadata provenance assumptions before training-data
documentation work. This does not validate clinical safety, model performance,
or real-world data quality.

Technical collaboration is limited to UDI-DICOM metadata mapping review,
synthetic workflow design, reproducibility checks, and boundary-safe
documentation. No clinical validation, regulatory approval, certification, PHI
processing, raw DICOM processing, or private-suite exposure is provided here.

## Department Recommendation Materials

For department-level review and recommendation workflows, see the
[Chinese recommendation report](docs/recommendation/department-recommendation-report-cn.md)
and [one-page executive brief](docs/recommendation/executive-one-page-cn.md).
These documents summarize the public validator, paper DOI, Zenodo DOI, and
boundary-safe evidence map without changing validator behavior.

## Quickstart

```bash
python -m venv .venv
. .venv/bin/activate
python -m pip install -U pip
pip install -e '.[dev,api]'
pytest -q
python demo/portable-ultrasound/run_demo.py
```

CLI output preview (example: validating a portable ultrasound synthetic manifest)

```text
PASS manifest_id=synthetic-portable-ultrasound-v02-pass-001 checks=6 report=demo/portable-ultrasound/artifacts_v0.2/report.md
```

## CLI

```bash
udi-dicom-validate validate-manifest \
  --manifest examples/public/manifest.pass.json \
  --dicom-metadata examples/public/sample_dicom_metadata.pass.json \
  --registry-fixture examples/public/registry.fixture.resolved.json \
  --out-dir /tmp/udi-dicom-validator-pass
```

The command writes `receipt.json` and `report.md`. Receipts are deterministic:
the same inputs produce the same check order, primary error code, and receipt id.

## API

The optional API is public-only and validation-only:

```bash
pip install -e '.[api]'
uvicorn udi_dicom_validator.api:app --reload
```

It does not expose private conformance, vendor-rule, or real-sample assessment
interfaces.

## Public Examples

Files in `examples/public/` are synthetic fixtures. They demonstrate the pass
case and isolated failure modes for `missing_udi`, `sop_uid_mismatch`,
`registry_unresolved`, and `device_uid_used_as_udi_di`.

## Boundary

DICOM `Device UID (0018,1002)` is a device/equipment UID in DICOM metadata. It
is not the regulatory UDI-DI. The UDI string is carried through the DICOM UDI
Macro, including `Unique Device Identifier (0018,1009)` inside `UDI Sequence
(0018,100A)`. This project checks evidence consistency; it does not establish
medical, legal, regulatory, or safety conclusions.


## v0.2 Profile

The v0.2 public profile adds synthetic workflow trace ids, receipt provenance,
and optional metadata-only FDO-style mapping fields. Run the v0.2 demo with:

```bash
python demo/portable-ultrasound/run_demo.py
python -m json.tool demo/portable-ultrasound/artifacts_v0.2/receipt.json
```

These fields are synthetic review metadata only and do not create clinical,
regulatory, certification, or production FDO claims.

## v0.3 Release Hardening

v0.3 adds golden receipt regression, a public evaluation matrix, release
artifact inventory, and a public-only MCP skeleton. These are reproducibility and
agent-readability surfaces only. Private conformance cases and real samples stay
outside this repository.

## v0.4 Release Hardening Branch

v0.4 focuses on remote reproducibility, external review readiness, public release
asset building, and citation/archive readiness. Use:

```bash
python scripts/verify_remote_release.py
python scripts/build_public_release_assets.py
python scripts/clean_clone_smoke.py
```

The public release asset builder is public-only: it excludes the private
conformance suite, private sample validation service, real samples, raw DICOM
files, and PHI. The external review pack is in `docs/external-review-brief.md`,
`docs/external-review-checklist.md`, and `docs/reproducibility-for-reviewers.md`.
Archive metadata is DOI-ready only; no DOI is claimed until an archive service
assigns one.

## v0.5 Paper Review Pack

v0.5 adds public paper drafting material, external reviewer quickstart/checklist
documents, and a reproducibility capsule:

```bash
python scripts/build_reproducibility_capsule.py
python scripts/check_reproducibility_capsule.py artifacts/reproducibility-capsule-v0.5
```

The v0.5 material is for technical paper review and reproduction only. It does
not add new medical functions, does not include real samples, does not include
robot operation evidence, and does not change the boundary: Device UID is not
UDI-DI, offline registry fixtures remain the default, live openFDA lookup is
explicit opt-in, and FDO-style mapping is not an official FDO implementation.

## v0.6 Paper Submission Readiness

v0.6 prepares journal-neutral paper submission material, DOI-ready archive
metadata review, and external reviewer feedback intake:

```bash
python scripts/build_archive_metadata_report.py
python scripts/check_archive_metadata_report.py artifacts/archive-metadata-report-v0.6.json
python scripts/build_paper_submission_package.py
python scripts/check_paper_submission_package.py artifacts/paper-submission-v0.6
```

This does not change validator behavior, schema behavior, or public example
semantics. It does not claim an assigned DOI. Private suite and private service
materials remain outside the public paper dataset and public DOI scope.

## v0.7 Paper Submission Prep

v0.7 is a controlled paper-submission preparation pass. It adds human review
handoff checklists for the public paper, Zenodo/DOI readiness review, and
external reviewer response triage. It does not change validator behavior,
schema behavior, public example semantics, or release asset generation.

Use `docs/v0.7-paper-submission-prep.md` and
`paper/submission/v0.7-human-review-checklist.md` before any human paper
submission or archive deposition decision. The boundary remains no PHI, no raw
DICOM, not clinical validation, not regulatory approval, not certification, no
fake DOI, Device UID != UDI-DI, offline fixture first, live openFDA explicit
opt-in, FDO-style mapping only, and no robot operation evidence.

## v0.8 DOI Archive Readiness

v0.8 adds DOI archive review and paper finalization support for the public
validator only:

```bash
python scripts/build_doi_archive_review_package.py
python scripts/check_doi_archive_review_package.py artifacts/doi-archive-review-v0.8
python scripts/check_no_fake_doi.py
python scripts/build_paper_finalization_bundle.py
python scripts/check_paper_finalization_bundle.py artifacts/paper-finalization-bundle-v0.8
python scripts/check_citation_metadata_consistency.py
```

This is a DOI pending state. Zenodo GitHub integration must be enabled manually,
and a new GitHub Release must be created after enablement before Zenodo can
archive the public repository. No DOI is written here; citation metadata may be
updated only after a real Zenodo record URL and DOI are verified.

Private suite and private service materials are outside public DOI scope.

## v0.8.1 Verified Zenodo DOI Capture

Verified Zenodo DOI: `10.5281/zenodo.20540532`

Zenodo record: https://zenodo.org/records/20540532

This DOI refers to the public validator release archive only. It does not
include private conformance suite or private sample validation service assets.
The boundary remains no PHI, no raw DICOM, not clinical validation, not
regulatory approval, not certification, no fake DOI, and Device UID != UDI-DI.
