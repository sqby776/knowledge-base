---
title: AI 编辑 Word Skill 技术解析
created: 2026-05-30
updated: 2026-05-30
tags: ["word", "skill", "automation", "python-docx"]
status: archived
sources: [https://mp.weixin.qq.com/s/Fnp8Ly9qv9QCweqpmWqyaw]
trust_score: 0.17
confidence: low
---
# AI 编辑 Word Skill 技术解析

> 来源：微信公众号-AI 干货家老明
> GitHub: https://github.com/sgsss998/AI-Word-Skill

## 核心价值

AI 自动编辑/排版 Word 文档，节省大量手工排版时间。

## 技术立场

**核心三原则：**
1. **母版副本** — 基于模板生成，保持版式稳定
2. **尽量只动 `run.text`** — 最小化格式破坏
3. **表格别漏** — 表格是排版的重灾区

## 价值维度

| 维度 | 价值 |
|:-----|:-----|
| **时间** | 少做一整轮"全篇重排"或"手工对齐到哭" |
| **质量** | 合同、纪要、公文、标书等场景下，版式稳定≈专业度 |
| **可解释** | 出问题能对上 OOXML / run / 样式的原因 |

## 安装与使用

```bash
# 安装技能
hermes skills install https://github.com/sgsss998/AI-Word-Skill

# 与公文模板结合
# 1. 阅读源代码了解 SOP
# 2. 适配 python-docx 操作模式
# 3. 与现有公文模板互补
```

## 技术要点

### python-docx 操作模式

```python
from docx import Document

doc = Document('template.docx')  # 母版副本
for para in doc.paragraphs:
    if '占位符' in para.text:
        para.clear()  # 清空但保留样式
        para.add_run('新内容')  # 只改文本
```

### 表格处理

```python
for table in doc.tables:
    for row in table.rows:
        for cell in row.cells:
            # 谨慎修改表格内容
            pass
```

## 与现有系统整合

| 现有能力 | AI-Word-Skill 补充 |
|:-----|:-----|
| 公文模板（GB/T 9704） | 自动化填充内容 |
| python-docx 基础操作 | 智能排版优化 |
| 模板复制 + 文字替换 | 格式智能保留 |

## 相关链接

- [[Python办公库]]
- [[公文排版标准]]
- [[office-toolchain]]

## 来源

- GitHub: https://github.com/sgsss998/AI-Word-Skill
- 微信公众号：AI 干货家老明

---

> [!ACTION] 待办
> - [ ] 安装 AI-Word-Skill 并测试
> - [ ] 与公文模板结合验证
> - [ ] 编写使用 SOP
