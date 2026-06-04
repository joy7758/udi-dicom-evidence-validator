# Project plan

# 项目总方案

本仓库与 `agent-evidence` 仓库共同维护 UDI-DICOM（Unique Device
Identification–Digital Imaging and Communications in Medicine，唯一器械标识—医学数字成像与通信）
医疗设备影像工作流证据闭合的公开安全说明与最小实现。

公开安全版总方案维护在：
https://github.com/joy7758/agent-evidence/blob/main/docs/medical-imaging-traceability/udi-dicom-total-plan-public.md

- 本仓库负责实现最小 UDI-DICOM Evidence Manifest and Validator（Evidence Manifest and
  Validator，证据清单与验证器）。
- `agent-evidence` 仓库负责维护更大的研究路线、公开安全版总方案、智能体证据和
  FDO（FAIR Digital Object，公平数字对象）方向的长期结构。
- 当前阶段只实现公开 Profile（Profile，配置文件）、schema（schema，模式）、
  examples（examples，示例）、reference validator（reference validator，参考验证器）和
  demo（demo，演示）。
- 不纳入医疗机器人操作证据、真实医院试点、临床验证、监管批准、认证或
  SaaS（Software as a Service，软件即服务）平台化。

本说明不改变 validator 行为、schema、examples、tests 或 release artifacts。
