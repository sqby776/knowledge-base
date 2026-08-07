---
title: openpyxl教程
created: 2026-06-17
updated: 2026-06-17
tags: ["method", "python", "excel", "tutorial"]
status: archived
sources: ["维基/sources/openpyxl教程.md"]
confidence: low
trust_score: 0.17
---
# openpyxl 教程

## 概述

openpyxl 官方教程的核心内容，覆盖从基本读写到高级样式的完整用法。

## 基本操作

### 创建工作簿

```python
from openpyxl import Workbook
wb = Workbook()
ws = wb.active
ws.title = "工作表1"
```

### 读写单元格

```python
# 写入
ws['A1'] = 42
ws.cell(row=2, column=1, value=100)

# 读取
value = ws['A1'].value
```

### 保存文件

```python
wb.save('output.xlsx')
```

## 高级功能

- **样式设置**：Font、PatternFill、Alignment、Border
- **公式**：`ws['A3'] = '=SUM(A1:A2)'`
- **图表**：折线图、柱状图、散点图
- **合并单元格**：`ws.merge_cells('A1:C1')`
- **条件格式**：数据条、色阶、图标集

## 相关

- [[openpyxl]] — openpyxl 库概述
- [[Excel自动化]] — Excel 自动化实践
- [[电子表格]] — 电子表格处理概念

## 来源

- openpyxl 官方教程
- https://openpyxl.readthedocs.io/en/latest/tutorial.html