---
title: CSV格式
type: concept
tags: [llmwiki, csv, data, format]
created: 2026-06-15
updated: 2026-06-15
---

# CSV 格式

CSV（逗号分隔值，Comma-Separated Values）是一种以纯文本形式存储表格数据的文件格式。

## 特点

- **简单通用**：几乎所有的电子表格和数据库工具都支持
- **纯文本**：可以用任何文本编辑器打开
- **无格式信息**：不存储字体、颜色、合并单元格等样式

## Python 处理

- [[Python]] 标准库 `csv` 模块用于读写
- pandas 的 `read_csv()`/`to_csv()` 更适合大规模数据

## 相关概念

- [[数据序列化]] — 数据序列化与反序列化
- [[电子表格]] — 电子表格基本概念