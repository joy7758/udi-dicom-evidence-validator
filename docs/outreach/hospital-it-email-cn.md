# Hospital IT Email CN

agent_readable:
  document_type: outreach_email
  audience: hospital_it
  language: zh-CN
  request_type: technical_review
  commercial_procurement_request: false
  accepts_phi: false
  accepts_raw_dicom: false

主题：请求信息化技术复核：UDI-DICOM 元数据一致性公开验证器

您好，

我想请医院信息科、PACS/VNA 管理或医学影像数据治理同事，技术复核一个公开的 UDI-DICOM Evidence Validator（证据验证器）。它不连接医院系统，不处理真实影像，不接收患者数据；它只用 public synthetic examples（公开合成示例）演示 metadata consistency（元数据一致性）和 deterministic receipt（确定性回执）。

公开材料：

- GitHub repository（代码仓库）：https://github.com/joy7758/udi-dicom-evidence-validator
- 10 分钟复核指南：`docs/external-review-10min.md`
- Zenodo DOI（归档引用）：https://doi.org/10.5281/zenodo.20540532

希望您从信息化角度复核：

- 这个 demo 是否能帮助解释 UDI-DICOM metadata consistency（元数据一致性）。
- Device UID 与 UDI-DI 的边界是否容易理解。
- receipt.json（机器可读回执）和 report.md（人工可读报告）是否适合技术讨论。
- README 是否足够清楚地说明它不替代 PACS、VNA、CMMS 或资产管理系统。

边界说明：不接收 PHI（受保护健康信息）、不接收 raw DICOM（原始 DICOM 文件）、不接收未去标识化 DICOM、不接入医院生产系统、不做临床验证、不做监管认证、不做采购或部署请求。若后续需要演示，只能使用 synthetic metadata（合成元数据）或已去标识化、不含患者信息的 metadata-only（仅元数据）材料。

谢谢。
