---
title: Hermes Agent 安装指南与平台支持
source: https://hermes-agent.nousresearch.com/docs/getting-started/installation
fetched: 2026-07-13
tier: Tier 1 (官方文档)
tags: [hermes-agent, 安装, 平台支持, 部署, auto-compiled]
---

# Hermes Agent 安装与平台支持知识点

## 安装器行为
- 自动处理所有依赖：uv, Python 3.11, Node.js, ripgrep, ffmpeg
- 除 Git 外无需预装任何内容
- Linux 需要 curl 和 xz-utils
- Desktop 应用需要 g++ (build-essential)

## 安装目录结构
| 安装方式 | 代码位置 | hermes 二进制 | 数据目录 |
|---------|---------|-------------|---------|
| Per-user | ~/.hermes/hermes-agent/ | ~/.local/bin/hermes (symlink) | ~/.hermes/ |
| Root-mode | /usr/local/lib/hermes-agent/ | /usr/local/bin/hermes | /root/.hermes/ 或 $HERMES_HOME |

## 无 Sudo 用户/系统服务安装
- 安装器检测 sudo 是否可用，无 sudo 时优雅降级
- Chromium 系统库需要管理员单独安装：`sudo npx playwright install-deps chromium`
- 服务用户建议将 `~/.local/bin` 添加到 PATH 或创建系统级软链接
- 跳过浏览器自动化：`curl -fsSL ... | bash -s -- --skip-browser`

## 平台支持分级

### Tier 1（最高优先级）
- macOS Apple Silicon — Hermes Desktop, install.sh
- Windows 10/11 (x86_64, aarch64) — Hermes Desktop, install.ps1（部分功能不可用）
- Linux/WSL2 (x86_64, aarch64) — install.sh（在最新 Ubuntu 和 WSL2 上测试）
- Docker Container (x86_64, aarch64) — `docker pull`（不支持 hermes update）

### Tier 2（尽力维护）
- Android Termux (aarch64) — install.sh（部分功能不可用）
- Nix (macOS, Linux, NixOS) — install.sh（因 Node.js 打包问题经常出问题）

### 不支持
- AUR 安装
- macOS Intel (x86)
- PyPI 安装（`uv tool install hermes-agent`, `pip install`）
- Homebrew 安装

## 安装方法自动检测
- Hermes 自动检测安装方式（pip / git installer / Homebrew / NixOS）
- `hermes update` 打印相应更新命令
- `hermes doctor` 显示检测到的安装方式

## 快捷安装路径推荐
1. 安装 → `hermes setup --portal`（Nous Portal，一键配齐）
2. 验证聊天正常
3. 逐步添加 Gateway / Cron / Skills / Voice