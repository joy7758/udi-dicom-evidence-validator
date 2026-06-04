# Structured Abstract Draft

## Background

UDI and DICOM metadata can be difficult to review consistently when device
metadata, registry evidence, and derived review artifacts are disconnected.

## Objective

To describe a minimal public evidence manifest profile and deterministic
reference validator for synthetic UDI-DICOM metadata review.

## Methods

The software validates synthetic JSON metadata fixtures, evidence manifests,
offline registry fixtures, and declared artifact hashes. It emits deterministic
JSON receipts and Markdown reports, with golden receipt regression and a public
reproducibility capsule.

## Results

The public evaluation matrix covers synthetic pass and fail cases, including
missing UDI, unresolved registry fixture, SOP Instance UID mismatch, and Device
UID used as UDI-DI.

## Conclusions

The contribution is a reproducible public software artifact for evidence
consistency review. It is not clinical validation, regulatory approval,
certification, diagnosis, or deployment evidence.

