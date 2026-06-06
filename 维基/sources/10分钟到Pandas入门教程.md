---
title: 10 minutes to pandas
type: source
tags: [llmwiki, python, pandas, 数据科学]
sources: ["01-收件箱/文章/2026-06-04_10_minutes_to_pandas.md"]
created: 2026-06-05
updated: 2026-06-05
---

# 10 minutes to pandas

## 摘要

pandas 官方入门教程，面向新手用户。涵盖 DataFrame/Series 两大核心数据结构、对象创建、数据查看、选择索引、缺失值处理、合并连接、重塑、文本处理、分组聚合、窗口操作、时间序列、性能优化等核心功能。

## 要点

- **核心数据结构**：`Series`（一维带标签数组）和 `DataFrame`（二维表结构）
- **对象创建**：支持列表、NumPy 数组、字典等多种输入
- **数据类型**：每个列可独立 dtype（float64、datetime64、category、str 等），这是与 NumPy 的核心差异
- **数据查看**：`head()`/`tail()` 预览，`describe()` 统计摘要，`to_numpy()` 转为 NumPy
- **索引选择**：`loc[]`（标签索引）、`iloc[]`（位置索引）、`at[]`/`iat[]`（标量快速访问）、布尔索引
- **分组聚合**：`groupby()` 实现 split-apply-combine 范式
- **窗口操作**：`rolling()`/`expanding()` 支持滑动窗口统计
- **时间序列**：`date_range()`、频率转换、时区处理
- **性能优化**：CoW（Copy-on-Write）、向量化操作优先于循环

## 提及的实体

- [[pandas]]
- [[NumPy]]

## 相关概念

- [[DataFrame]]
- [[Series]]
- [[索引选择]]
- [[分组聚合]]
- [[窗口操作]]
- [[时间序列处理]]
- [[数据类型]]
- [[Copy-on-Write]]

## 来源

- 原始 URL: https://pandas.pydata.org/docs/user_guide/10min.html
- 抓取日期: 2026-06-04
