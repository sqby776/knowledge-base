---
title: openpyxl Tutorial
type: source
tags: [llmwiki, python, office, excel, openpyxl]
sources: ["01-收件箱/文章/2026-06-04_Tutorial.md", "01-收件箱/自动捕获/2026-06-08_Tutorial.md"]
created: 2026-06-05
updated: 2026-06-08
---

# openpyxl 教程

## 摘要

openpyxl 官方教程。openpyxl 用于读写 Excel 2010 xlsx/xlsm 文件格式。

## 要点

- **Workbook**：顶层工作簿对象
- **Worksheet**：工作表，通过 `workbook.active` 或 `workbook.create_sheet()` 访问
- **单元格**：`worksheet['A1']` 或 `worksheet.cell(row=1, column=1)`
- **数据写入**：直接赋值 `cell.value = 42`
- **读取**：`cell.value` 读取值，`cell.number_format` 读取格式
- **行/列迭代**：`iter_rows()`、`iter_cols()`
- **样式**：`Font`、`PatternFill`、`Alignment`、`Border` 等
- **公式**：`cell.value = '=SUM(A1:A10)'` 写入 Excel 公式
- **图表**：支持折线图、柱状图、散点图等

## 提及的实体

- [[openpyxl]]

## 相关概念

- [[Excel自动化]]
- [[Office自动化]]
- [[电子表格]]

## 来源

- 原始 URL: https://openpyxl.readthedocs.io/en/latest/tutorial.html
- 抓取日期: 2026-06-04
