---
title: Hermes Agent
created: 2026-06-06
updated: 2026-06-06
tags: [knowledge-base, auto-compiled, entity, official-docs]
status: draft
sources: [https://hermes-agent.nousresearch.com/docs]
source_url: https://hermes-agent.nousresearch.com/docs
---

# Hermes Agent

> [!INFO] 编译信息
> 来源: 自动抓取 (2026-06-06) | 类型: entity | 来源: Hermes Agent 官方文档首页
>
> 补充来源: 02-笔记/概念/Hermes-Agent.md (更详尽的版本)

## 定义

Hermes Agent 是由 [Nous Research](https://nousresearch.com) 开发的**自进化 AI 智能体**。它是唯一内建学习回路的智能体——从经验中创建 Skill，在使用中自我改进，跨会话持续积累对你个人的理解。

## 核心特点

| 特点 | 说明 |
|:-----|:-----|
| 闭环比学习回路 | 自主管理记忆、周期性自省提示、Skill 自动创建与自优化、FTS5 跨会话检索 + LLM 摘要、Honcho 用户建模 |
| 随处运行 | 6 种后端: 本地、Docker、SSH、Daytona、Singularity、Modal。Daytona/Modal 提供无服务器持久化——空闲时几乎零成本 |
| 多平台接入 | CLI、Telegram、Discord、Slack、WhatsApp、Signal、Matrix、Mattermost、Email、SMS、DingTalk、飞书、企业微信、微信、QQ Bot、Yuanbao、BlueBubbles、Home Assistant、Teams、Google Chat 等 20+ 平台 |
| 定时自动化 | 内置 cron，支持投递到任意平台 |
| 并行委派 | 通过 `delegate_task` spawn 隔离子智能体并行工作；通过 `execute_code` 程序化调用将多步骤流水线折叠为单次推理 |
| 开放 Skill 标准 | 兼容 [agentskills.io](https://agentskills.io)，Skill 可移植、可分享、社区贡献 |
| 完整网页控制 | 搜索、提取、浏览、视觉、图像生成、TTS——一个订阅通过 Nous Portal 打包全部 |
| MCP 支持 | 连接任意 MCP Server 扩展工具能力 |
| 研究就绪 | 批量处理、轨迹导出、使用 Atropos 的 RL 训练 |

## 安装

### Linux / macOS / WSL2 / Android (Termux)
```bash
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
```

### Windows (native PowerShell)
```powershell
iex (irm https://hermes-agent.nousresearch.com/install.ps1)
```

### 快速开始
安装后运行 `hermes setup --portal`——一次 OAuth 覆盖一个模型 + 全部四个 Tool Gateway 工具（网页搜索、图像生成、TTS、浏览器）。

## 面向 LLM 和代码智能体的机器可读入口

| 文件 | 说明 |
|:-----|:-----|
| [`/llms.txt`](https://hermes-agent.nousresearch.com/docs/assets/files/llms-d4972c57170916efd83766ae50c3bb3d.txt) | 每张文档页面的索引 + 简短描述，~17 KB，可安全载入 LLM 上下文 |
| [`/llms-full.txt`](https://hermes-agent.nousresearch.com/docs/assets/files/llms-full-1edd45007ed802d53db26fcab096793a.txt) | 所有文档页面拼接为单个 Markdown 文件，~1.8 MB，一次注入 |

两个文件也解析为 `/docs/llms.txt` 和 `/docs/llms-full.txt`，每次部署时自动生成。

## 快速链接

| 链接 | 内容 |
|:-----|:-----|
| 🚀 [Installation](https://hermes-agent.nousresearch.com/docs/getting-started/installation) | Linux/macOS/WSL2/Windows 60 秒安装 |
| 📖 [Quickstart](https://hermes-agent.nousresearch.com/docs/getting-started/quickstart) | 第一次对话与关键功能 |
| 🗺️ [Learning Path](https://hermes-agent.nousresearch.com/docs/getting-started/learning-path) | 按经验水平找到合适的文档 |
| ⚙️ [Configuration](https://hermes-agent.nousresearch.com/docs/user-guide/configuration) | 配置文件、提供商、模型 |
| 💬 [Messaging Gateway](https://hermes-agent.nousresearch.com/docs/user-guide/messaging) | 配置 Telegram、Discord、Slack 等 |
| 🔧 [Tools & Toolsets](https://hermes-agent.nousresearch.com/docs/user-guide/features/tools) | 60+ 内置工具 |
| 🧠 [Memory System](https://hermes-agent.nousresearch.com/docs/user-guide/features/memory) | 跨会话持久记忆 |
| 📚 [Skills System](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills) | 程序化记忆 |
| 🔌 [MCP Integration](https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp) | MCP 服务器连接 |
| 🎙️ [Voice Mode](https://hermes-agent.nousresearch.com/docs/user-guide/features/voice-mode) | 实时语音交互 |

## 相关链接

- [[Hermes-Agent]] — 更详尽的概念笔记
- [[MemOS]] — 记忆操作系统
- [[Honcho]] — 对话式用户建模
- [[ChromaDB]] — 向量数据库
- [[RAG]] — 检索增强生成

---

*本文基于官方文档首页自动生成编译，已补充结构化表格。更完整的版本见 [[Hermes-Agent]]。*
