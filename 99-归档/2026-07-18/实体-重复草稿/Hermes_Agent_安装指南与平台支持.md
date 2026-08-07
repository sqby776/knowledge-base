---
title: Hermes Agent 安装指南与平台支持
created: 2026-07-14
updated: 2026-07-14
tags: [knowledge-base, auto-compiled]
status: draft
sources: [auto-capture]
---

# Hermes Agent 安装指南与平台支持

> [!INFO] 编译信息
> 来源: 自动抓取 | 编译时间: 2026-07-14 07:00 | 类型: entity

## 核心要点

- **Hermes Agent 安装与平台支持知识点**
- 自动处理所有依赖：uv, Python 3.11, Node.js, ripgrep, ffmpeg
- 除 Git 外无需预装任何内容
- Linux 需要 curl 和 xz-utils
- Desktop 应用需要 g++ (build-essential)
- 安装器检测 sudo 是否可用，无 sudo 时优雅降级
- Chromium 系统库需要管理员单独安装：`sudo npx playwright install-deps chromium`
- 服务用户建议将 `~/.local/bin` 添加到 PATH 或创建系统级软链接
- 跳过浏览器自动化：`curl -fsSL ... | bash -s -- --skip-browser`
- macOS Apple Silicon — Hermes Desktop, install.sh

## 相关链接


## 来源

- 原始文章: Hermes Agent 安装指南与平台支持
