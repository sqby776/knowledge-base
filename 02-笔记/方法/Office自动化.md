---
title: Office 自动化（Python）
type: method
tags: [llmwiki, python, office, 自动化]
sources: ["维基/sources/python-pptx入门.md", "维基/sources/python-docx快速入门.md", "维基/sources/openpyxl教程.md"]
created: 2026-06-05
updated: 2026-06-05
---

# Office 自动化（Python）

## 概览

使用 Python 自动创建、修改 Microsoft Office 文档。三大核心库覆盖 Word、Excel、PowerPoint。

## 关键信息

| 格式 | 库 | 用途 |
|------|-----|------|
| .docx | python-docx | 创建和修改 Word 文档 |
| .xlsx/.xlsm | openpyxl | 读写 Excel 电子表格 |
| .pptx | python-pptx | 创建和修改演示文稿 |

- **共同模式**：都有顶层对象（Document/Workbook/Presentation）→ 子对象（Paragraph/Cell/Slide）→ 数据/格式操作
- **适用场景**：批量生成报告、自动化报表、数据驱动的文档生成

## 相关概念

- [[数据驱动文档]]
- [[文档处理]]

## 来源

- [[python-docx快速入门.md]]
- [[openpyxl教程]]
- [[python-pptx入门.md]]
