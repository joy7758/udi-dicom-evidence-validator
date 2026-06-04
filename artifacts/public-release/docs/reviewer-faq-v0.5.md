# Reviewer FAQ v0.5

## Why use de-identified or synthetic examples?

The public repository is meant for reproducible software review. Synthetic JSON
fixtures keep the validation path inspectable without PHI, raw DICOM files, or
real hospital identifiers.

## Is this certification?

No. The validator emits deterministic receipts for public evidence consistency
checks. It is not certification, clinical validation, regulatory approval, or a
diagnosis tool.

## Why default to registry fixtures?

Offline fixtures make review deterministic and network-independent. Live
openFDA lookup can be useful for separate experiments, but it must be explicitly
enabled and is not part of the default reproduction path.

## What does FDO-style mapping mean?

It means optional metadata fields are shaped so they can be discussed in FAIR
Digital Object terms. It does not mean the project implements an official FDO
standard or registers persistent identifiers.

