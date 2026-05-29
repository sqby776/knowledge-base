---
title: Tesseract OCR
created: 2026-05-24
updated: 2026-05-24
tags: ["tool", "config"]
status: active
sources: []
---

# Tesseract OCR

## 定义

Tesseract OCR — 开源光学字符识别（OCR）引擎，支持多种语言的文字识别。

## 核心特点

| 特点 | 说明 |
|:-----|:-----|
| **开源免费** | Apache 2.0 许可 |
| **多语言** | 支持 100+ 语言 |
| **高精度** | 对清晰文本识别效果好 |
| **命令行** | 可通过 CLI 调用 |

## 本系统配置

| 项目 | 详情 |
|:-----|:-----|
| **版本** | 5.3.4 |
| **安装位置** | `~/.tesseract/` |
| **语言包** | chi_sim（简体）、chi_tra（繁体） |
| **用途** | 图片转文字、PDF 文字提取 |

## 安装语言包

```bash
# 简体中文
sudo apt install tesseract-ocr-chi-sim

# 繁体中文
sudo apt install tesseract-ocr-chi-tra

# 英文（默认）
sudo apt install tesseract-ocr-eng
```

## 常用命令

```bash
# 图片转文字
tesseract input.png output

# 指定语言
tesseract -l chi_sim input.png output

# PDF 转文字
tesseract input.pdf output pdf

# 批量处理
for f in *.png; do tesseract "$f" "${f%.png}"; done
```

## 与 Omnisearch 集成

Obsidian 的 Omnisearch 插件支持 Tesseract OCR，可自动识别图片/PDF 中的文字。

## 相关链接

- [[办公自动化地图]]
- [[LibreOffice]]
- [[office-tools]]

## 来源

- Tesseract 官方文档
- 本系统实际配置经验

---

> [!NOTE] 待验证
> 具体语言包和配置需根据实际需求调整
