# Public Evaluation Matrix

This matrix is generated from public synthetic examples only. It is not clinical validation, not regulatory approval, and not certification.

| Manifest | Profile | Expected | Actual | OK | Stage | Fixture |
| --- | --- | --- | --- | --- | --- | --- |
| examples/public/manifest.fail_device_uid_used_as_udi_di.json | v0.1.0 | device_uid_used_as_udi_di | device_uid_used_as_udi_di | False | presence_parseability | examples/public/registry.fixture.resolved.json |
| examples/public/manifest.fail_missing_udi.json | v0.1.0 | missing_udi | missing_udi | False | presence_parseability | examples/public/registry.fixture.resolved.json |
| examples/public/manifest.fail_registry_unresolved.json | v0.1.0 | registry_unresolved | registry_unresolved | False | registry_resolution | examples/public/registry.fixture.unresolved.json |
| examples/public/manifest.fail_wrong_sop_uid.json | v0.1.0 | sop_uid_mismatch | sop_uid_mismatch | False | reference_closure | examples/public/registry.fixture.resolved.json |
| examples/public/manifest.pass.json | v0.1.0 | None | None | True | all_passed | examples/public/registry.fixture.resolved.json |
| examples/public/v0.2/manifest_v0.2.fail_device_uid_used_as_udi_di.json | v0.2.0 | device_uid_used_as_udi_di | device_uid_used_as_udi_di | False | presence_parseability | examples/public/v0.2/registry.fixture_v0.2.resolved.json |
| examples/public/v0.2/manifest_v0.2.fail_missing_udi.json | v0.2.0 | missing_udi | missing_udi | False | presence_parseability | examples/public/v0.2/registry.fixture_v0.2.resolved.json |
| examples/public/v0.2/manifest_v0.2.fail_registry_unresolved.json | v0.2.0 | registry_unresolved | registry_unresolved | False | registry_resolution | examples/public/v0.2/registry.fixture_v0.2.unresolved.json |
| examples/public/v0.2/manifest_v0.2.pass.json | v0.2.0 | None | None | True | all_passed | examples/public/v0.2/registry.fixture_v0.2.resolved.json |
