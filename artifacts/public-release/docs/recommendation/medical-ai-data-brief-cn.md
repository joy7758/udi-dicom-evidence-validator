# 医疗 AI 数据治理简报

## 适用讨论

本简报面向医疗 AI 数据工程、数据治理和模型审计团队，用于说明训练数据 provenance 文档中设备标识的边界问题。

## 关键价值

- 帮助区分 Device UID 与法规 UDI-DI。
- 用 public synthetic examples 演示设备 provenance 记录如何进入 manifest。
- 用 deterministic receipt 支持后续审查，而不是依赖一次性截图或口头说明。
- 用论文 DOI 和 Zenodo DOI 建立可引用的公开证据链。

## 不覆盖的内容

本项目不验证模型性能，不判断临床有效性，不处理真实训练数据，不接收 PHI，不处理 raw DICOM，不提供数据集授权或临床结论。

## 推荐动作

在医疗 AI 数据治理讨论中，将本项目作为“设备元数据 provenance 边界”的教学和复核样例，而不是作为生产数据审计平台。

Boundary: no PHI, no raw DICOM, not clinical validation, not regulatory approval, not certification, public synthetic examples, Device UID != UDI-DI.
