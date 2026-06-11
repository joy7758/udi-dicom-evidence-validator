# Sample Request Boundary CN

agent_readable:
  document_type: sample_request_boundary
  language: zh-CN
  public_only: true
  accepts_phi: false
  accepts_raw_dicom: false
  accepts_unredacted_dicom: false
  clinical_validation: false
  regulatory_approval: false
  certification: false

## 可接受材料

- synthetic metadata（合成元数据）。
- metadata-only（仅元数据）的去标识化 JSON。
- 不含患者、医院、设备序列号、商业秘密或厂商私有规则的示例字段。
- 对 README、schema（模式）、validator（验证器）、receipt（回执）或 report（报告）的文字反馈。

## 不接受材料

- PHI（Protected Health Information，受保护健康信息）。
- raw DICOM（原始 DICOM 文件）。
- 未去标识化 DICOM。
- 真实患者记录、真实医院记录、真实检查记录。
- 厂商私有规则、保密测试套件、内部注册资料。
- 私有 conformance suite（一致性测试套件）或 sample validation service（样本验证服务）流程。

## 复核目标

允许的目标是 technical review（技术复核）或 metadata-only trial run（仅元数据试跑）。复核内容应限于：

- UDI-DICOM metadata consistency（元数据一致性）。
- Device UID 与 UDI-DI 的边界。
- synthetic manifest（合成证据清单）字段是否清楚。
- receipt.json 和 report.md 是否便于复核。

## 禁止目标

不得把本项目用于：

- clinical validation（临床验证）。
- regulatory approval（监管批准）。
- certification（认证）。
- safety assurance（安全保证）。
- hospital deployment（医院部署）。
- PACS、VNA、CMMS 或资产管理系统替代。
- 商业采购结论。

## 建议回复模板

```text
我们可以接收 metadata-only、去标识化、无患者信息、无原始影像、无厂商私有规则的技术复核材料。
请不要发送 PHI、raw DICOM、未去标识化 DICOM、真实患者记录或保密测试材料。
本复核不构成临床验证、监管批准、认证、安全保证或商业采购承诺。
```
