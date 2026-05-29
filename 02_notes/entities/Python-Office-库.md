---
title: Python Office 库
created: 2026-05-24
updated: 2026-05-24
tags: ["tool", "automation"]
status: active
sources: []
---

# Python Office 库

## 定义

Python Office 库 — 用于编程操作 Office 文档的 Python 库集合。

## 核心库

| 库 | 用途 | 安装 |
|:-----|:-----|:-----|
| **python-docx** | Word 文档读写 | `pip install python-docx` |
| **openpyxl** | Excel 工作簿读写 | `pip install openpyxl` |
| **python-pptx** | PowerPoint 读写 | `pip install python-pptx` |
| **pandas** | 数据处理 | `pip install pandas` |
| **reportlab** | PDF 生成 | `pip install reportlab` |
| **xlsxwriter** | Excel 高级功能 | `pip install xlsxwriter` |

## 本系统配置

| 项目 | 详情 |
|:-----|:-----|
| **虚拟环境** | `~/office-venv/` |
| **已安装库** | python-docx, openpyxl, python-pptx, pandas, reportlab, xlsxwriter |

## 常用代码示例

### Word 文档

```python
from docx import Document

doc = Document()
doc.add_heading('标题', 0)
doc.add_paragraph('段落内容')
doc.save('output.docx')
```

### Excel 工作簿

```python
import pandas as pd

df = pd.read_excel('input.xlsx')
df.to_excel('output.xlsx', index=False)
```

### PowerPoint 演示

```python
from pptx import Presentation

prs = Presentation()
slide = prs.slides.add_slide(prs.slide_layouts[0])
slide.shapes.title.text = '标题'
prs.save('output.pptx')
```

## 与 LibreOffice 对比

| 维度 | Python 库 | LibreOffice |
|:-----|:-----|:-----|
| **功能** | 编程接口 | 完整办公套件 |
| **速度** | 快 | 慢 |
| **格式支持** | 有限 | 全面 |
| **适用场景** | 自动化脚本 | 批量转换 |

## 相关链接

- [[LibreOffice]]
- [[办公自动化地图]]
- [[office-tools]]

## 来源

- 各库官方文档
- 本系统实际配置经验

---

> [!NOTE] 待验证
> 具体库版本和配置需根据实际需求调整
