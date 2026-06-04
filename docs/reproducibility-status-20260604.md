# Reproducibility status - 2026-06-04

# 可复现性状态 -- 2026-06-04

## Scope

This note records the clean-clone reproducibility result after PR #11.

本文件记录 PR（Pull Request，拉取请求）#11 合并后的 clean clone reproducibility（clean clone reproducibility，干净克隆可复现性）结果。

## Repository state

- Repository: `joy7758/udi-dicom-evidence-validator`
- Branch: `main`
- Main commit after PR #11: `e4c57348f48a978d3fc4ee016da3e9bc86702a43`
- PR（Pull Request，拉取请求）#11: `artifacts: refresh generated public assets after plan link`

## Validation result

- Install result: passed
- Test command: `pytest -q`
- Test result: passed
- Number of tests: `35`
- Demo command: `python demo/portable-ultrasound/run_demo.py`
- Demo result: `PASS manifest_id=synthetic-portable-ultrasound-v02-pass-001 checks=6`
- Worktree after test and demo: clean
- Modified tracked files after test and demo: none

## Scope confirmation

The validation did not require changes to:

- code（code，代码）
- schema（schema，模式）
- validator（validator，验证器）
- examples（examples，示例）
- tests（tests，测试）
- dependencies（dependencies，依赖）

## Boundary

This status note does not change project scope.

It does not claim clinical validation（clinical validation，临床验证）, regulatory approval（regulatory approval，监管批准）, certification（certification，认证）, safety assurance（safety assurance，安全保证）, production deployment（production deployment，生产部署）, or replacement of PACS（Picture Archiving and Communication System，医学影像归档与通信系统） / VNA（Vendor Neutral Archive，厂商中立归档） systems.

## Judgment

PASS: clean clone reproducibility verified after PR #11.
