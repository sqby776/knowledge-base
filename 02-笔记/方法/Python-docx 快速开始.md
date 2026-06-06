---
title: Python-docx 快速开始
created: 2026-06-02
updated: 2026-06-02
tags: ["python", "word", "docx", "automation", "method"]
status: active
sources: [https://python-docx.readthedocs.io/en/latest/user/quickstart.html]
---

# Python-docx 快速开始

> 来源：python-docx 官方文档

## 核心概念

- **Document**：整个 Word 文档
- **Paragraph**：段落
- **Run**：文本片段（具有相同格式）

## 创建文档

```python
from docx import Document
from docx.shared import Pt, Inches

doc = Document()
doc.add_heading('文档标题', level=1)
doc.add_paragraph('这是第一段内容。')
doc.save('output.docx')
```

## 格式化文本

```python
from docx.shared import Pt, RGBColor

doc = Document()
p = doc.add_paragraph()

run = p.add_run('粗体文本')
run.bold = True
run.font.size = Pt(14)

p.add_run(' 正常文本 ')

run = p.add_run('斜体文本')
run.italic = True
run.font.color.rgb = RGBColor(0, 0, 255)

doc.save('formatted.docx')
```

## 添加表格

```python
table = doc.add_table(rows=3, cols=2)
table.style = 'Table Grid'

table.rows[0].cells[0].text = '姓名'
table.rows[0].cells[1].text = '年龄'
table.rows[1].cells[0].text = 'Alice'
table.rows[1].cells[1].text = '30'
```

## 常用操作

| 操作 | 方法 |
|------|------|
| 添加段落 | `doc.add_paragraph(text)` |
| 添加标题 | `doc.add_heading(text, level=N)` |
| 添加表格 | `doc.add_table(rows, cols)` |
| 添加图片 | `doc.add_picture('img.png', width=Inches(3))` |

## 与 python-pptx 对比

| 库 | 用途 | 适用场景 |
|----|------|----------|
| python-docx | Word 文档 | 报告、公文、合同 |
| python-pptx | PPT 演示 | 演示文稿、汇报 |

## 相关链接

- [[AI 编辑 Word Skill 技术解析]]
- [[办公自动化]]
- [[Python-pptx 快速开始]]
