---
title: 办公工具实体页
created: 2026-05-24
updated: 2026-05-24
tags: ["tool", "config"]
status: active
sources: []
---

# 办公工具实体页

## 软件工具

### LibreOffice

- **类型**: 开源办公套件
- **版本**: 24.2.7
- **组件**: Writer(Word), Calc(Excel), Impress(PPT)
- **安装**: `~/.local/libreoffice/`
- **用途**: 文档编辑、格式转换、批量处理

### Obsidian

- **类型**: 本地知识库
- **版本**: 1.12.7
- **安装**: `~/.local/obsidian/opt/Obsidian/`
- **用途**: 知识管理、双链笔记、RAG 知识库

### Tesseract OCR

- **类型**: 光学字符识别
- **版本**: 5.3.4
- **语言包**: chi_sim(简体), chi_tra(繁体)
- **用途**: 图片转文字、PDF 文字提取

### Python Office 库

| 库 | 用途 | 虚拟环境 |
|:---|:---|:---|
| python-docx | Word 文档 | `~/office-venv/` |
| openpyxl | Excel 工作簿 | `~/office-venv/` |
| python-pptx | PowerPoint | `~/office-venv/` |
| pandas | 数据处理 | `~/office-venv/` |
| reportlab | PDF 生成 | `~/office-venv/` |
| xlsxwriter | Excel 高级 | `~/office-venv/` |

## 硬件配置

- **CPU**: Intel i7-3537U (双核)
- **内存**: 8GB
- **系统**: Ubuntu 24.04
- **网络**: 约 30KB/s（下载慢）

## 环境配置

- **Java JRE**: Temurin 17.0.14 (`~/.local/java/`)
- **Python**: 3.x + virtualenv
- **LibreOffice**: 已配置 Java 注册表
- **环境变量**: `~/.bashrc.office`

## 相关概念

- [[办公自动化]]
- [[文档处理]]
- [[批量转换]]
- [[OCR 识别]]

---

*最后更新：2026-05-24*
