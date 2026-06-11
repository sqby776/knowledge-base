---
title: csv 模块 — CSV 文件读写
type: source
tags: [llmwiki, python, csv, 数据处理]
sources: ["01-收件箱/文章/2026-06-04_csv_CSV_File_Reading_and_Writing.md", 01-收件箱/自动捕获/2026-06-08_csv_CSV_File_Reading_and_Writing.md]
created: 2026-06-05
updated: 2026-06-08
2026-06-05
---

# `csv` 模块 — CSV 文件读写

## 摘要

Python 标准库 `csv` 模块，用于读写 CSV 格式文件。支持 Reader/Writer 类、Dialect 注册、DictReader/DictWriter、自定义格式配置。

## 要点

- **Reader**：逐行读取 CSV 文件，返回字符串列表
- **Writer**：逐行写入 CSV 文件
- **DictReader**：将每行映射为 OrderedDict（列名→值）
- **DictWriter**：将字典写入 CSV，指定 fieldnames 控制列顺序
- **Dialect**：注册自定义格式（分隔符、引号字符、换行符等）
- **Excel Dialect**：默认格式，逗号分隔，`\r\n` 换行
- **异常处理**：`csv.Error` 处理格式错误
- **注意**：处理大文件时用 `for line in reader:` 逐行迭代，避免一次性加载

## 提及的实体

- [[Python]]

## 相关概念

- [[CSV格式]]
- [[数据序列化]]

## 来源

- 原始 URL: https://docs.python.org/3/library/csv.html
- 抓取日期: 2026-06-04
