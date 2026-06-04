# Public Release Trigger Plan v0.8

The Zenodo archive trigger is intentionally manual-gated:

1. Keep this branch as DOI readiness and paper finalization support only.
2. Do not write a DOI on this branch.
3. Have a human confirm Zenodo integration is enabled for the public repository.
4. Merge the public v0.8 PR only after review.
5. Create `v0.8.0-public` as a new GitHub Release after Zenodo enablement.
6. Treat the release state as `ZENODO_ARCHIVE_PENDING` until Zenodo returns a
   record URL and DOI.
7. Run a separate DOI capture PR after the record is verified.

Private suite and private service assets are excluded from this release plan.
