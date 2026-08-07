---
title: openpyxl教程
type: source
tags: [llmwiki, python, excel, openpyxl, tutorial]
sources: ["维基/sources/openpyxl教程.md"]
created: 2026-06-15
updated: 2026-06-15
---

# openpyxl 教程

> 详细内容见 [[维基/sources/openpyxl教程]]。

openpyxl 是 Python 中读写 Excel xlsx/xlsm 格式的标准库。

## 快速入门

```python
from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws['A1'] = 'Hello'
wb.save('test.xlsx')
```

## 相关实体

- [[openpyxl]] — openpyxl 库概述
- [[Excel自动化]] — Excel 自动化方案
- [[电子表格]] — 电子表格基本概念