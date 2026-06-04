# Remote Reproducibility

v0.4 adds public-only remote reproducibility checks for reviewers and release
maintainers. These checks confirm that the pushed `main` branch, published tags,
GitHub release assets, golden receipts, evaluation matrix, and portable
ultrasound demo can be reproduced from public materials.

## Commands

```bash
python scripts/verify_remote_release.py
python scripts/build_public_release_assets.py
python scripts/clean_clone_smoke.py
```

`verify_remote_release.py` checks the public `origin`, remote `main`, release
tag, inventory tag, and public release asset names. It rejects private markers,
raw DICOM extensions, PHI markers, and unbounded clinical, regulatory, or
certification asset names.

`clean_clone_smoke.py` clones the public repository into `/tmp`, installs the
package, runs tests, checks golden receipts, rebuilds the public evaluation
matrix, and runs the portable ultrasound demo.

`build_public_release_assets.py` creates public-only assets in
`artifacts/public-release/`. It does not include the private conformance suite,
private sample validation service, raw DICOM files, real samples, or PHI.

## Boundary

This is release reproducibility for a reference validator. It is not clinical
validation, not regulatory approval, and not certification. Offline fixtures are
the default. Live openFDA access remains explicit opt-in.
