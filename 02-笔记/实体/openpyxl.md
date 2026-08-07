---
title: openpyxl
created: 2026-06-17
updated: 2026-06-17
tags: ["tool", "python", "excel"]
status: archived
sources: ["维基/sources/openpyxl教程.md"]
confidence: low
trust_score: 0.17
---
# openpyxl

## 定义

openpyxl — Python 读写 Excel 2010 xlsx/xlsm/xltx/xltm 格式的库，支持单元格样式、公式、图表、图片等高级功能。

## 核心功能

| 功能 | 描述 |
|:-----|:-----|
| **读写 xlsx** | 读取和写入 Excel 2010 及以上格式 |
| **样式** | Font、PatternFill、Alignment、Border |
| **公式** | 直接写入 Excel 公式如 `=SUM(A1:A10)` |
| **图表** | 折线图、柱状图、散点图 |
| **图片** | 插入图片到工作表 |
| **条件格式** | 数据条、色阶、图标集 |

## 使用场景

- 读取 Excel 报表进行数据分析
- 生成带格式和公式的工资表
- 创建包含多工作表的统计报表
- 批量处理 Excel 文件

## 安装

```bash
pip install openpyxl
```

## 相关

- [[openpyxl教程]] — 使用详解
- [[Excel自动化]] — Excel 自动化实践
- [[Python办公库]] — Python 办公库汇总

## 来源

- openpyxl 官方文档
- 本系统实际使用经验