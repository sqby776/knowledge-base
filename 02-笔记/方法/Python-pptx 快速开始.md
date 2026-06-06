---
title: Python-pptx 快速开始
created: 2026-06-02
updated: 2026-06-02
tags: ["python", "powerpoint", "pptx", "automation", "method"]
status: active
sources: [https://python-pptx.readthedocs.io/en/latest/user/quickstart.html]
---

# Python-pptx 快速开始

> 来源：python-pptx 官方文档

## 核心概念

- **Presentation**：整个 PPT 文件
- **Slide**：单张幻灯片
- **Shape**：幻灯片上的元素（文本框、图片、表格等）

## 创建 PPT

```python
from pptx import Presentation
from pptx.util import Inches, Pt

prs = Presentation()

# 添加幻灯片（使用布局）
slide_layout = prs.slide_layouts[1]  # Title and Content
slide = prs.slides.add_slide(slide_layout)

# 设置标题和内容
title = slide.shapes.title
title.text = "演示标题"

content = slide.placeholders[1]
content.text = "第一行内容\n第二行内容"

# 保存
prs.save('output.pptx')
```

## 添加文本框

```python
from pptx.util import Inches, Pt

shape = slide.shapes.add_textbox(Inches(1), Inches(2), Inches(6), Inches(1))
tf = shape.text_frame
tf.text = "自定义文本"

for paragraph in tf.paragraphs:
    for run in paragraph.runs:
        run.font.size = Pt(14)
        run.font.bold = True
```

## 常用操作

| 操作 | 方法 |
|------|------|
| 添加幻灯片 | `prs.slides.add_slide(layout)` |
| 添加文本 | `shape.text_frame.text = "text"` |
| 添加图片 | `shapes.add_picture('img.png', left, top)` |
| 添加表格 | `shapes.add_table(rows, cols, ...)` |

## 与 python-docx 对比

| 库 | 用途 | 特点 |
|----|------|------|
| python-docx | Word 文档 | 文本处理为主 |
| python-pptx | PPT 演示 | 排版、布局为主 |

## 相关链接

- [[AI 编辑 Word Skill 技术解析]]
- [[办公自动化]]
