# Reviewer Risk Boundary v0.5

This repository supports public technical review of a synthetic validator. It
does not support:

- PHI processing.
- Raw DICOM distribution.
- Clinical validation.
- Regulatory approval.
- Certification.
- Diagnosis or treatment support.
- Hospital deployment claims.
- Medical robot operation evidence.
- Private conformance suite disclosure.
- Private sample validation service disclosure.

Identifier boundary: DICOM `Device UID (0018,1002)` is not UDI-DI. A validator
pass does not prove that a real device, hospital workflow, or clinical process
is safe or compliant.

