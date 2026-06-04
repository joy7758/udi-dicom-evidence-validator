# Next-Step Gate

## Current State

Status: DEPARTMENT_RECOMMENDATION_PACK_READY

This state means the public recommendation package exists, boundary checks pass,
and the materials can support manual department outreach.

## Required Gates

1. `RECOMMENDATION_PACK_CHECK_PASS`
2. `NO_FAKE_DOI_CHECK_PASS`
3. `REAL_ZENODO_DOI_CHECK_PASS`
4. `CITATION_METADATA_CONSISTENCY_PASS`
5. `MANUAL_DEPARTMENT_OUTREACH_APPROVED`

## Manual Outreach Conditions

- Use only public repository and DOI links.
- Include `boundary-and-risk-statement-cn.md`.
- Do not attach PHI or raw DICOM.
- Do not include private suite/service material.
- Do not imply clinical validation, regulatory approval, certification, or hospital deployment.

## Later v1 DOI Capture

The `v1.0.0-zenodo` GitHub Release is a DOI archive trigger. Citation metadata
must not be updated for v1 until a real Zenodo DOI and record URL exist.

Boundary: no PHI, no raw DICOM, not clinical validation, not regulatory approval, not certification, public synthetic examples, Device UID != UDI-DI.
