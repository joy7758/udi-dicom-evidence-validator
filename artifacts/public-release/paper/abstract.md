# Abstract

This paper draft describes a minimal public UDI-DICOM evidence manifest and
reference validator for synthetic device metadata review. The validator checks
whether DICOM equipment metadata, UDI-DI evidence, registry fixture records, and
declared artifacts form a deterministic review packet. Outputs include
machine-readable receipts, Markdown reports, golden receipt regression cases, a
public evaluation matrix, and a reproducibility capsule.

The work is intentionally bounded. Public fixtures are synthetic, contain no
PHI, and do not include raw DICOM files. Registry checks default to offline
fixtures, while live openFDA lookup remains explicit opt-in. FDO-style fields
are treated as optional metadata mapping aids rather than an official FDO
implementation. The validator does not provide clinical validation, regulatory
approval, certification, diagnosis, safety assurance, or deployment evidence.

