---
title: CSV 数据处理
type: concept
tags: [python, csv, 数据处理, pandas]
sources: [https://docs.python.org/3/library/csv.html, https://pandas.pydata.org/docs/user_guide/dsintro.html#dataframe]
created: 2026-06-05
updated: 2026-08-27
status: compiled
confidence: high
trust_score: 0.8
---
# CSV 数据处理

## 概览

CSV（Comma-Separated Values）是最广泛的数据交换格式。Python 提供标准库 `csv` 和 pandas 两种处理方式。

## csv 模块（标准库）

- **读取**：`csv.reader()` 逐行返回列表，`csv.DictReader()` 返回字典
- **写入**：`csv.writer()` 写入列表，`csv.DictWriter()` 写入字典
- **dialect**：`excel`（逗号分隔）、`excel_tab`（制表符）、可自定义
- **参数**：`delimiter`、`quotechar`、`quoting`（QUOTE_MINIMAL/MINIMAL/ALL/NONNUMERIC）
- **文件打开**：必须 `newline=''` 防止换行符问题
- **适用场景**：大文件流式处理、格式定制、无第三方依赖

## pandas（数据分析）

- **读取**：`pd.read_csv()` — 自动推断分隔符、编码、类型
- **写入**：`df.to_csv()` — 一行输出，支持索引控制
- **适用场景**：数据分析、复杂变换、多文件合并

## 常见陷阱

- **编码**：Windows Excel 默认 GBK，需指定 `encoding='utf-8-sig'` 或 `gbk`
- **引号内逗号**：用 `quoting=csv.QUOTE_NONNUMERIC` 或 pandas 自动处理
- **缺失值**：空字段默认为空字符串，可用 `na_values` 参数指定
- **换行符**：Windows CRLF vs Unix LF，`newline=''` 是必须的

## 相关概念

- [[JSON数据交换]]
- [[DataFrame]]
- [[数据序列化]]

## 来源

- Python 官方 csv 文档
- pandas 用户指南
