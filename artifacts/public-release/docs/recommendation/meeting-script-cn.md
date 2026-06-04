# 部门推荐会议脚本

## 目标

用 15 到 20 分钟说明 UDI-DICOM Evidence Validator 的公开证据链、论文支撑、适用场景和边界。

## 议程

1. 项目定位：public validator 和 reproducibility artifact。
2. 证据链：GitHub 仓库、Zenodo DOI、论文 DOI、demo、tests。
3. 技术核心：manifest、DICOM metadata fixture、registry fixture、deterministic receipt。
4. 场景：医院 IT/PACS/VNA、医疗器械研发、医疗 AI 数据治理。
5. 边界：no PHI、no raw DICOM、not clinical validation、not regulatory approval、not certification、Device UID != UDI-DI。
6. 下一步：决定是否纳入部门观察清单、课程材料或研究引用。

## 开场口径

今天讨论的是一个公开合成数据验证器，不是真实数据服务，也不是临床或监管结论工具。我们只看它是否适合作为部门技术推荐和可复现研究材料。

## 结束口径

如果继续推进，下一步应先复核 `evidence-map.md`、`boundary-and-risk-statement-cn.md` 和 DOI 链接；只有在边界一致时才进入人工外联或内部推荐。
