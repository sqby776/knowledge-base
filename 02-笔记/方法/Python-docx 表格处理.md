---
title: Python-docx 表格处理
created: 2026-06-02
updated: 2026-06-02
tags: ["python", "docx", "table", "automation", "method"]
status: archived
sources: [https://python-docx.readthedocs.io/en/latest/user/table.html]
trust_score: 0.17
confidence: low
---
# Python-docx 表格处理

> 来源：python-docx 官方文档 - 表格

## 创建表格

```python
from docx import Document

doc = Document()
table = doc.add_table(rows=3, cols=2)
table.style = 'Table Grid'

for i in range(3):
    for j in range(2):
        table.rows[i].cells[j].text = f'({i},{j})'

doc.save('table.docx')
```

## 设置单元格样式

```python
from docx.shared import Pt, RGBColor

cell = table.rows[0].cells[0]
cell.text = '标题'

for paragraph in cell.paragraphs:
    for run in paragraph.runs:
        run.font.bold = True
        run.font.size = Pt(12)
```

## 合并单元格

```python
table.cell(0, 0).merge(table.cell(0, 1))
```

## 从 DataFrame 创建表格

```python
import pandas as pd

df = pd.DataFrame({'name': ['Alice', 'Bob'], 'age': [30, 25]})

table = doc.add_table(rows=len(df)+1, cols=len(df.columns))
table.style = 'Table Grid'

for j, col in enumerate(df.columns):
    table.rows[0].cells[j].text = col

for i, row in df.iterrows():
    for j, val in enumerate(row):
        table.rows[i+1].cells[j].text = str(val)
```

## 相关链接

- [[Python-docx 快速开始]]
- [[AI编辑WordSkill技术解析]]
