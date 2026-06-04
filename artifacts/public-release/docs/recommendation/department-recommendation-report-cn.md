# UDI-DICOM Evidence Validator 部门推荐报告

## 推荐结论

建议将 `udi-dicom-evidence-validator` 作为部门层面的公共参考工具和论文支撑材料纳入内部技术观察清单，用于 UDI-DICOM 元数据一致性、可复现验证和证据链文档化的教学、研究与评审准备。

该推荐仅覆盖 public validator。它不覆盖 private suite、private service、真实样本服务或医院部署。

## 项目定位

本项目提供一个最小、可复现、公开的 UDI-DICOM evidence manifest validator。它检查 DICOM 设备元数据、manifest、registry fixture 和声明 artifact 是否形成确定性 review packet。

公开仓库：https://github.com/joy7758/udi-dicom-evidence-validator

已核验 Zenodo DOI：https://doi.org/10.5281/zenodo.20540532

论文 DOI：https://doi.org/10.1007/s10278-026-02019-6

论文题名：A Minimal UDI-DICOM Mapping Profile and Validation Artifact for Medical-Device Imaging Workflows

期刊：Journal of Imaging Informatics in Medicine

## 适合的部门使用场景

1. 医学影像信息学课程或研讨课：演示 UDI-DICOM 映射边界、公开 fixture、确定性 receipt 和 artifact review。
2. 医院信息科/PACS/VNA 治理讨论：用合成数据解释设备元数据一致性检查，不接触真实影像或患者信息。
3. 医疗器械研发或注册信息化团队：在内部合规准备讨论中观察 Device UID 与 UDI-DI 混淆风险。
4. 医疗 AI 数据治理团队：用公开合成示例说明训练数据 provenance 文档中的设备标识边界。

## 推荐理由

- 公开可复现：仓库、测试、demo、release asset 和 Zenodo 记录均可由第三方复核。
- 边界清晰：项目持续声明 no PHI、no raw DICOM、not clinical validation、not regulatory approval、not certification。
- 风险可控：公开材料只含 public synthetic examples，不包含真实样本、私有测试集或服务流程。
- 论文可引用：论文 DOI 与 Zenodo DOI 可支持部门技术推荐、研究引用和课程材料复核。

## 不应被升级的结论

本项目不证明临床安全性，不证明设备上市合规，不证明医院系统上线能力，不提供认证，不接收 PHI，不处理 raw DICOM，不替代厂商质量体系、医院 PACS/VNA/CMMS 或监管审评。

关键边界：Device UID != UDI-DI。DICOM Device UID 是设备/装备 UID，不是法规意义上的 UDI-DI。

## 推荐动作

1. 采用本目录的 `executive-one-page-cn.md` 作为部门内部说明。
2. 将 `evidence-map.md` 与 Zenodo DOI 一并附在推荐邮件中。
3. 若需要演示，使用公开仓库的 Quickstart 和 portable ultrasound demo。
4. 若进入后续合作讨论，先通过 `boundary-and-risk-statement-cn.md` 重新确认边界。

## 状态词

Status: DEPARTMENT_RECOMMENDATION_PACK_READY

Scope: public validator only

Boundary: no PHI, no raw DICOM, not clinical validation, not regulatory approval, not certification, public synthetic examples, Device UID != UDI-DI.
