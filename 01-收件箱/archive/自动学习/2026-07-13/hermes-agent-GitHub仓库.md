---
title: Hermes Agent GitHub 仓库
source: https://github.com/NousResearch/hermes-agent
fetched: 2026-07-13
tier: Tier 1 (官方源码仓库)
tags: [hermes-agent, github, 版本, 贡献者, 技术栈, auto-compiled]
---

# Hermes Agent GitHub 仓库知识点

## 仓库概况
- **Stars**: 214k
- **Forks**: 39.7k
- **贡献者**: 1,773 人
- **提交数**: 15,277 commits
- **许可证**: MIT
- **最新版本**: v0.18.2 (v2026.7.7.2) — 2026年7月8日发布
- **发布总数**: 21 个 Release

## 技术栈
| 语言 | 占比 |
|------|------|
| Python | 82.4% |
| TypeScript | 14.9% |
| TeX | 0.6% |
| JavaScript | 0.5% |
| Shell | 0.4% |
| PowerShell | 0.3% |

## 目录结构亮点
- `agent/` — Agent 核心逻辑
- `gateway/` — 消息网关
- `tools/` — 工具系统
- `skills/` — 技能系统
- `providers/` — LLM 提供商适配
- `docs/` — 文档
- `web/` — Web UI
- `ui-tui/` — 终端 TUI

## v0.18.2 发行说明
- 仅在 v0.18.1 基础上修复了 WhatsApp Baileys 依赖问题
- WhatsApp bridge 从 git commit 固定版本改为使用已发布的 npm 包 `7.0.0-rc13`
- 主要修复了 Docker 镜像构建的可靠性问题

## 安装方式
### Windows 原生安装（PowerShell）
```powershell
iex (irm https://hermes-agent.nousresearch.com/install.ps1)
```
- 无需 WSL，CLI/Gateway/TUI 全部原生运行
- 安装到 `%LOCALAPPDATA%\hermes`
- 自动处理：uv, Python 3.11, Node.js, ripgrep, ffmpeg, MinGit

### Linux/macOS/WSL2/Termux
```bash
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
```

## Windows Defender 误报提醒
- Windows Defender 或 Bitdefender 可能将 uv.exe 识别为恶意软件（误报）
- 提供了 GitHub 签名验证方法验证 uv.exe 真实性
- 提供了白名单排除路径的配置方法