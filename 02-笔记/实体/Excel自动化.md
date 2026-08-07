---
title: Excel自动化
type: entity
tags: [llmwiki, excel, office, automation]
sources: []
created: 2026-06-15
updated: 2026-06-15
---

# Excel自动化

## 概览

Excel 自动化是指通过编程手段自动完成 Excel 文档的创建、编辑、数据处理和报表生成等操作。

## 关键工具

| 工具 | 用途 | 安装 |
|------|------|------|
| [[openpyxl]] | Python 读写 Excel xlsx/xlsm | `pip install openpyxl` |
| pandas | 数据分析与表格处理 | `pip install pandas` |
| xlsxwriter | 高级 Excel 写入 | `pip install xlsxwriter` |
| win32com | Windows Excel COM 自动化 | `pip install pywin32` |

## 相关概念

- [[办公自动化]] — 办公场景全面自动化
- [[电子表格]] — 电子表格基本概念
- [[openpyxl教程]] — openpyxl 用法详解

## 常见场景

1. **批量报表生成**：从数据库导出数据，自动填充模板
2. **数据清洗与转换**：格式统一、去重、校验
3. **图表生成**：自动创建统计图表
4. **格式美化**：批量设置单元格样式、条件格式