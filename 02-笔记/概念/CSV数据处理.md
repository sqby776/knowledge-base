---
title: CSV 数据处理
type: concept
tags: [llmwiki, python, csv, 数据处理]
sources: ["维基/sources/CSV模块读写.md"]
created: 2026-06-05
updated: 2026-06-05
---

# CSV 数据处理

## 概览

CSV（Comma-Separated Values）是最广泛的数据交换格式。Python 提供标准库 `csv` 和 pandas 两种处理方式。

## 关键信息

- **csv 模块**：标准库，轻量，逐行处理，适合大文件
- **pandas**：`read_csv()`/`to_csv()`，功能丰富，适合数据分析
- **格式变体**：逗号/制表符/分号分隔，不同换行符，不同引号策略
- **常见陷阱**：编码问题（UTF-8 vs GBK）、引号内逗号、缺失值

## 相关概念

- [[JSON格式]]
- [[数据序列化]]
- [[数据交换]]

## 来源

- [[CSV模块读写]]
