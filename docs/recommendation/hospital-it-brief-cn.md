# 医院 IT / PACS / VNA 简报

## 适用讨论

本简报面向医院信息科、PACS/VNA 管理员和医学影像数据治理团队，用于解释 UDI-DICOM metadata consistency 的公开、合成、可复现检查方式。

## 可以帮助讨论的问题

- 设备元数据在迁移或盘点时是否存在标识不一致风险。
- DICOM UDI Macro 与 registry fixture 如何形成可审计 receipt。
- Device UID 与 UDI-DI 为什么不能混用。
- 如何用 public synthetic examples 训练团队识别 metadata boundary。

## 不覆盖的内容

本项目不是 PACS、VNA、CMMS 或资产管理系统。它不接收 PHI，不处理 raw DICOM，不做医院系统部署，不做临床安全评价，不替代厂商或医院质量体系。

## 推荐演示

使用公开 Quickstart 和 `demo/portable-ultrasound/run_demo.py` 生成 deterministic receipt 与 report。演示数据必须保持合成，不得替换为真实样本。

Boundary: no PHI, no raw DICOM, not clinical validation, not regulatory approval, not certification, public synthetic examples, Device UID != UDI-DI.
