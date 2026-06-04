# Introduction

UDI and DICOM metadata can appear in disconnected operational records, registry
lookups, and review artifacts. A compact evidence manifest can make this
relationship easier to inspect by linking the relevant metadata, declared
device identifiers, registry evidence, and artifact hashes in one deterministic
review object.

The public validator focuses on a narrow question: do the supplied synthetic
metadata files and manifest agree with each other under the public profile? This
is useful for reproducible software review because the same inputs produce the
same check order, primary error code, receipt id, and report content.

The project deliberately avoids broader claims. Device UID is not UDI-DI.
Offline registry fixtures are the default. Live openFDA lookup is explicit
opt-in. FDO-style mapping fields are descriptive metadata only.

