---
source: https://hermes-agent.nousresearch.com/docs
date: 2026-06-22
tier: Tier 2
tags: [hermes-agent, 官方文档, 安装, 配置, 技能, 记忆, MCP, 架构]
---

# Hermes Agent 官方文档 — 结构化知识点

## 1. 安装方式
- **Hermes Desktop**: 官网下载安装器（Windows/macOS 含 CLI + 桌面应用）
- **无桌面安装**: `curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash`（Linux/macOS/WSL2/Termux）
- **Windows 原生**: `iex (irm https://hermes-agent.nousresearch.com/install.ps1)`
- **快速启用**: 安装后执行 `hermes setup --portal` — 一次 OAuth 覆盖模型 + 4 个 Tool Gateway 工具（网页搜索、图片生成、TTS、浏览器）

## 2. 文档导航（Quick Links）
- 🚀 安装指南 — 60 秒安装
- 📖 快速开始教程 — 首次对话和关键特性
- 🗺️ 学习路径 — 按经验水平找文档
- ⚙️ 配置 — 配置文件、提供商、模型
- 💬 消息网关 — Telegram/Discord/Slack/WhatsApp/Teams 等
- 🔧 工具与工具集 — 60+ 内置工具
- 🧠 记忆系统 — 跨会话持久记忆
- 📚 技能系统 — Agent 创建和复用的过程记忆
- 🔌 MCP 集成 — 连接 MCP 服务器
- 🧭 使用 MCP — 实际配置模式、示例和教程
- 🎙️ 语音模式 — CLI/Telegram/Discord/Discord VC 实时语音
- 🗣️ 使用语音模式 — 动手配置和用法模式
- 🎭 个性与 SOUL.md — 定义 Agent 默认语音
- 📄 上下文文件 — 项目上下文文件
- 🔒 安全 — 命令审批、授权、容器隔离
- 💡 技巧与最佳实践
- 🏗️ 架构 — 工作原理

## 3. 关键特性详述
- **学习闭环**: Agent 管理记忆 + 定期自我提醒 → 自动创建技能 → 技能自改进 → FTS5 跨会话 + LLM 摘要 → Honcho 辩证用户建模
- **6 种终端后端**: 本地、Docker、SSH、Daytona、Singularity、Modal
- **20+ 平台**: CLI/Telegram/Discord/Slack/WhatsApp/Signal/Matrix/Mattermost/Email/SMS/DingTalk/Feishu/WeCom/Weixin/QQ Bot/Yuanbao/BlueBubbles/Home Assistant/Microsoft Teams/Google Chat
- **定时自动化**: 内置 cron，投递到任意平台
- **委派与并行**: 隔离的子代理 + execute_code 程序化工具调用
- **MCP 支持**: 连接任意 MCP 服务器
- **研究就绪**: 批量处理、轨迹导出、用 Atropos 做 RL 训练

## 4. Tool Gateway（工具网关）
- Nous Portal 一个订阅覆盖：网页搜索、图片生成、TTS、云浏览器
- 可以按工具粒度切换回自有 API Key