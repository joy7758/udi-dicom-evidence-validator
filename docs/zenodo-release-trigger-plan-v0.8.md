# Zenodo Release Trigger Plan v0.8

This plan is manual-gated. Codex must not create a release for DOI archive
triggering until Zenodo enablement is confirmed outside the repository.

Required manual state before release:

- Zenodo account is available.
- GitHub authorization is complete in Zenodo.
- Repository list has been synced if stale.
- Public validator repository toggle is enabled.
- Private suite and private service repositories are not enabled for public DOI.

Permitted release path after manual confirmation:

1. Merge the public v0.8 DOI readiness PR.
2. Run all public validator validation commands on `main`.
3. Create annotated tag `v0.8.0-public`.
4. Create the public GitHub Release.
5. Treat Zenodo as pending until a real record URL and DOI are returned.

No DOI may be written into repository metadata during this plan.
