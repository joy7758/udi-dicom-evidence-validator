# 医疗器械厂商研发 / 注册信息化简报

## 适用讨论

本简报面向医疗器械厂商的研发、注册信息化、质量工程和软件验证团队，用于观察 UDI-DICOM metadata mapping 在公开合成数据上的一致性验证方式。

## 可以支持的内部问题

- DICOM header 中的 UDI evidence 是否能被 manifest 和 registry fixture 解释。
- 设备 UID 与 UDI-DI 混淆是否能在合成示例中被提前识别。
- deterministic receipt 是否适合纳入内部工程 review 讨论。
- 公开论文和 Zenodo 归档是否足以支持技术引用。

## 不应被理解为

本项目不是 510(k)、NMPA、EU MDR 或其他监管批准工具。它不形成认证结论，不替代厂商质量体系，不证明产品临床安全性，不接收真实样本，不处理 raw DICOM 或 PHI。

## 推荐方式

先以公开仓库、Zenodo DOI、论文 DOI 和 `evidence-map.md` 进行技术复核，再决定是否在内部 CI 或文档评审中参考 manifest profile 的思想。

Boundary: no PHI, no raw DICOM, not clinical validation, not regulatory approval, not certification, public synthetic examples, Device UID != UDI-DI.
