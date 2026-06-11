# Vendor Email CN

agent_readable:
  document_type: outreach_email
  audience: medical_device_vendor
  language: zh-CN
  request_type: metadata_mapping_review
  commercial_procurement_request: false
  accepts_phi: false
  accepts_raw_dicom: false

主题：请求技术复核：UDI-DICOM 元数据映射公开验证器

您好，

我想邀请贵团队从研发、质量或注册信息化角度，技术复核一个公开的 UDI-DICOM Evidence Validator（证据验证器）。该项目用于 public synthetic examples（公开合成示例）上的 metadata mapping review（元数据映射复核），重点是 Device UID 与 UDI-DI 的边界、manifest（证据清单）字段、registry fixture（注册库夹具）和 deterministic receipt（确定性回执）。

公开材料：

- GitHub repository（代码仓库）：https://github.com/joy7758/udi-dicom-evidence-validator
- 外部复核指南：`docs/external-review-10min.md`
- Zenodo DOI（归档引用）：https://doi.org/10.5281/zenodo.20540532

这不是采购请求，也不是要求贵团队提供真实样本。希望获得的反馈仅限于：

- UDI-DICOM metadata mapping（元数据映射）表述是否清楚。
- Device UID 与 UDI-DI 的区分是否足够明确。
- public synthetic workflow（公开合成工作流）是否便于技术复现。
- 是否存在可能被误解为 clinical validation（临床验证）、regulatory approval（监管批准）或 certification（认证）的措辞。

边界说明：不接收 PHI（受保护健康信息）、不接收 raw DICOM（原始 DICOM 文件）、不接收未去标识化 DICOM、不接收设备私有规则、不接收厂商保密测试套件。本项目不提供临床验证、监管批准、安全保证或认证结论。若未来讨论试跑，也只限 metadata-only（仅元数据）、去标识化、边界安全的材料。

谢谢。
