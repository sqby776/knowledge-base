---
source: https://github.com/NousResearch/hermes-agent
date: 2026-06-22
tier: Tier 1
tags: [hermes-agent, GitHub, 源码, 开源, 仓库统计]
---

# Hermes Agent GitHub 仓库 — 结构化知识点

## 1. 仓库统计（2026-06-22）
- **Stars**: 199k ⭐
- **Forks**: 35.3k
- **Commits**: 12,483
- **默认分支**: main
- **许可证**: MIT

## 2. 关键功能（README 最新版）
- **真正的终端界面**: 完整 TUI，多行编辑、斜杠命令自动补全、对话历史、中断重定向、流式工具输出
- **随你所在**: Telegram/Discord/Slack/WhatsApp/Signal/CLI 单一网关进程
- **模型无关**: 支持 Nous Portal、OpenRouter（200+ 模型）、NVIDIA NIM、小米 MiMo、z.ai/GLM、Kimi/Moonshot、MiniMax、HuggingFace、OpenAI、自定义端点 — `hermes model` 一键切换
- **闭环学习**: Agent 管理记忆 + 定期自我提醒 → 自动创建技能 → 技能自改进
- **定时自动化**: 内置 cron，投递到任意平台
- **委派与并行**: 隔离的子代理 + Python RPC 工具调用
- **6 种终端后端**: 本地、Docker、SSH、Singularity、Modal、Daytona
- **研究就绪**: 批量轨迹生成、轨迹压缩

## 3. 最新活跃开发分支（2026-06-22 当天）
- `feat/goal-completion-contracts` — 新增功能：目标完成合约
- `feat/daemon-sigkill-escalation` — 守护进程 SIGKILL 升级
- `feat/reasoning-show-full` — 推理过程完整显示
- `fix/banner-platform-toolset-leak` — 修复横幅平台工具集泄露
- `hermes/hermes-a793ba6e` — Agent 自主分支

## 4. 项目目录结构
- `agent/` — Agent 核心逻辑
- `gateway/` — 消息网关
- `hermes_cli/` — CLI 界面
- `tools/` — 工具实现
- `skills/` — 技能系统
- `plugins/` — 插件系统
- `providers/` — 模型提供商集成
- `cron/` — 定时任务
- `web/` — 网页 UI
- `docs/` — 文档
- `ui-tui/` — TUI 界面
- `tui_gateway/` — TUI 网关
- `optional-mcps/` — 可选 MCP 服务器
- `optional-skills/` — 可选技能
- `acp_adapter/` — ACP 适配器
- `acp_registry/` — ACP 注册
- `packaging/homebrew/` — Homebrew 打包

## 5. 安装方式
- **Linux/macOS/WSL2/Termux**: `curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash`
- **Windows 原生 PowerShell**: `iex (irm https://hermes-agent.nousresearch.com/install.ps1)`
- 安装器处理：uv、Python 3.11、Node.js、ripgrep、ffmpeg、便携 Git Bash
- Windows 安装到 `%LOCALAPPDATA%\hermes`，完全隔离

## 6. 中文社区支持
- 文档有中文翻译版 README.zh-CN.md
- 中文社区镜像站：hermesagent.org.cn
- 中文社区微信交流群