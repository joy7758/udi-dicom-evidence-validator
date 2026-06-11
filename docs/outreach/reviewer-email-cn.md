# Reviewer Email CN

agent_readable:
  document_type: outreach_email
  audience: technical_reviewer
  language: zh-CN
  request_type: technical_review
  commercial_procurement_request: false
  accepts_phi: false
  accepts_raw_dicom: false

主题：请求技术复核：UDI-DICOM Evidence Validator 公开验证器

您好，

我想请您帮助技术复核一个公开的 UDI-DICOM Evidence Validator（证据验证器）仓库。这个项目只使用 public synthetic examples（公开合成示例），目标是检查 UDI-DICOM metadata consistency（元数据一致性）和 deterministic receipt（确定性回执），不是临床验证、监管认证或商业采购请求。

复核入口：

- GitHub repository（代码仓库）：https://github.com/joy7758/udi-dicom-evidence-validator
- 10 分钟复核指南：`docs/external-review-10min.md`
- Zenodo DOI（归档引用）：https://doi.org/10.5281/zenodo.20540532

建议您只跑两条命令：

```bash
pytest -q
python demo/portable-ultrasound/run_demo.py
```

希望您重点看：

- Device UID 是否被明确区分于 UDI-DI。
- receipt.json（机器可读回执）和 report.md（人工可读报告）是否足够清楚。
- README、CITATION.cff、Zenodo 记录和边界声明是否一致。
- 是否有任何文字可能被误解为 clinical validation（临床验证）、regulatory approval（监管批准）或 certification（认证）。

边界说明：我不接收 PHI（受保护健康信息）、不接收 raw DICOM（原始 DICOM 文件）、不接收未去标识化 DICOM，不做临床验证，不做监管认证，也不请求商业采购。若后续需要试跑，只能使用 synthetic metadata（合成元数据）或已去标识化且不含患者信息的 metadata-only（仅元数据）材料。

谢谢。
