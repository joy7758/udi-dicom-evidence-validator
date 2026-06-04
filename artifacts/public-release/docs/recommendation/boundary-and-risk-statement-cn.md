# 边界与风险声明

## 必须保留的边界

- no PHI
- no raw DICOM
- not clinical validation
- not regulatory approval
- not certification
- public synthetic examples
- Device UID != UDI-DI

## 解释

本项目是 public validator 和 reproducibility artifact。它验证公开合成 manifest、DICOM metadata fixture、registry fixture 与 artifact 声明之间的软件层一致性。

它不接收真实患者信息，不接收真实影像文件，不提供临床诊断或临床安全结论，不构成监管批准证据，不构成认证，不替代医院系统、厂商质量体系或监管审评。

## 主要风险

1. 把 public synthetic examples 误解为真实临床样本。
2. 把 deterministic receipt 误解为临床或监管结论。
3. 把 Device UID 当成 UDI-DI。
4. 把 Zenodo DOI 或论文 DOI 误解为产品认证。
5. 把推荐材料误解为商业销售或医院部署承诺。

## 控制措施

- 所有推荐材料必须引用本声明。
- 所有演示必须使用公开合成数据。
- 所有外部沟通必须保留 no PHI、no raw DICOM、not clinical validation、not regulatory approval、not certification。
- 如需真实数据或机构流程讨论，必须另行建立伦理、隐私、合规和安全审查流程；本仓库不提供该流程。
