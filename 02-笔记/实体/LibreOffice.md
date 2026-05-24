---
title: LibreOffice
created: 2026-05-24
updated: 2026-05-24
tags: ["tool", "config"]
status: active
sources: []
---

# LibreOffice

## 定义

LibreOffice — 开源办公套件，提供文字处理、电子表格、演示文稿等完整办公功能。

## 组件

| 组件 | 对应 Office | 用途 |
|:-----|:-----|:-----|
| **Writer** | Word | 文字处理 |
| **Calc** | Excel | 电子表格 |
| **Impress** | PowerPoint | 演示文稿 |
| **Draw** | - | 绘图 |
| **Base** | Access | 数据库 |
| **Math** | - | 公式编辑 |

## 本系统配置

| 项目 | 详情 |
|:-----|:-----|
| **版本** | 24.2.7 |
| **安装位置** | `~/.local/libreoffice/` |
| **Java JRE** | Temurin 17.0.14 |
| **用途** | 文档转换、批量处理 |

## 常用命令

```bash
# 批量转换 Word → PDF
libreoffice --headless --convert-to pdf *.docx

# 批量转换 PDF → 文本
libreoffice --headless --convert-to txt:Text *.pdf

# 静默模式（无界面）
libreoffice --headless --invisible
```

## 与 Python Office 库对比

| 维度 | LibreOffice | Python Office 库 |
|:-----|:-----|:-----|
| **功能** | 完整办公套件 | 编程接口 |
| **速度** | 慢（启动开销） | 快（直接操作） |
| **格式支持** | 全面 | 有限 |
| **适用场景** | 批量转换 | 自动化处理 |

## 相关链接

- [[办公自动化地图]]
- [[Python办公库]]
- [[TesseractOCR]]
- [[office工具]]

## 来源

- LibreOffice 官方文档
- 本系统实际配置经验

---

> [!NOTE] 待验证
> 具体配置参数需根据实际需求调整
