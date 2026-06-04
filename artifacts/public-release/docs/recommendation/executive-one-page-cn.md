# 一页推荐简报

## 推荐对象

`udi-dicom-evidence-validator` 是一个公开的 UDI-DICOM 元数据一致性参考验证器。建议用于部门层面的研究展示、技术评审、课程材料和论文支撑，而不是用于真实临床系统上线。

## 关键信息

- 仓库：https://github.com/joy7758/udi-dicom-evidence-validator
- Zenodo DOI：https://doi.org/10.5281/zenodo.20540532
- 论文 DOI：https://doi.org/10.1007/s10278-026-02019-6
- 论文：A Minimal UDI-DICOM Mapping Profile and Validation Artifact for Medical-Device Imaging Workflows
- 期刊：Journal of Imaging Informatics in Medicine

## 为什么值得推荐

1. 聚焦明确：只验证 UDI-DICOM evidence manifest 的软件层一致性。
2. 可复核：公开测试、demo、receipt、release asset 和 Zenodo archive 可追踪。
3. 可教学：public synthetic examples 能演示 missing UDI、registry unresolved、Device UID 与 UDI-DI 混淆等问题。
4. 边界清楚：no PHI、no raw DICOM、not clinical validation、not regulatory approval、not certification。

## 推荐使用

- 部门内部技术分享。
- 医学影像信息学或医疗 AI 数据治理课程。
- 论文支撑材料归档。
- 与医院 IT、器械研发、AI 数据团队的边界安全沟通。

## 明确不推荐

不建议把本项目表述为临床验证工具、监管批准证据、认证系统、医院部署系统、真实样本接收服务或商业销售材料。

## 一句话口径

这是一个 public validator 和 reproducibility artifact，用于解释和复核 UDI-DICOM metadata consistency；它不处理真实患者数据，也不提供临床、监管或认证结论。
