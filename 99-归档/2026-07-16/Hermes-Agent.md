---
title: Hermes Agent
created: 2026-05-29
updated: 2026-07-16
tags: ["auto-capture", auto-compiled]
status: compiled
sources: [https://hermes-agent.nousresearch.com/docs]
source_url: https://hermes-agent.nousresearch.com/docs
---

# Hermes Agent

> 自动抓取自: [https://hermes-agent.nousresearch.com/docs](https://hermes-agent.nousresearch.com/docs)

# Hermes Agent
The self-improving AI agent built by [Nous Research](https://nousresearch.com). The only agent with a built-in learning loop — it creates skills from experience, improves them during use, nudges itself to persist knowledge, and builds a deepening model of who you are across sessions.
[Get Started →](/docs/getting-started/installation)[Download Desktop](https://hermes-agent.nousresearch.com/)[View on GitHub](https://github.com/NousResearch/hermes-agent)


> **结构化摘要**（来自 实体/Hermes_Agent.md 编译版）
>
### 关键功能

- **闭环学习**：Agent 策展记忆（定期 Nudge）、自主 Skill 创建、使用中自优化 Skill、FTS5 跨会话召回 + LLM 摘要、Honcho 辩证用户建模
- **随处运行**：6 种终端后端（local/Docker/SSH/Daytona/Singularity/Modal），Daytona 和 Modal 支持 Serverless 持久化
- **跨平台**：CLI + 20+ 通讯平台（Telegram/Discord/Slack/WhatsApp/微信/飞书/钉钉等）
- **自建模型实验室**：由 Nous Research（Hermes/Nomos/Psyche 模型系列）出品
- **定时自动化**：内置 Cron，可投递到任意平台
- **子代理并行**：delegate_task 隔离子任务，execute_code 批量管道
- **开源 Skill 标准**：兼容 agentskills.io，社区贡献
- **Web 全栈**：搜索、提取、浏览、视觉、图片生成、TTS
- **MCP 支持**：连接任意 MCP 服务器扩展能力
- **Research-ready**：批处理、轨迹导出、RL 训练（Atropos）

| 资源 | 链接 |
|:----|:----|
| 官方文档 | `https://hermes-agent.nousresearch.com/docs` |
| 下载 Desktop | `https://hermes-agent.nousresearch.com/` |
| GitHub | `https://github.com/NousResearch/hermes-agent` |
| LLM 入口 (/llms.txt) | `/docs/assets/files/llms-96828202...txt` (~17KB) |
| 完整文档 (/llms-full.txt) | `/docs/assets/files/llms-full-9c18cca7...txt` (~1.8MB) |

## 安装方式

| 方式 | 命令 |
|:-----|:-----|
| Linux/macOS/WSL2 | `curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash` |
| Windows (native) | `iex (irm https://hermes-agent.nousresearch.com/install.ps1)` |
| Desktop | 下载 Hermes Desktop 安装器 |

安装后运行 `hermes setup --portal`，一次 OAuth 覆盖模型 + 四个工具网关（搜索、图片、TTS、浏览器）。

## 关键文档入口

| 功能 | 链接 |
|:-----|:-----|
| 快速开始 | `/docs/getting-started/quickstart` |
| 配置 | `/docs/user-guide/configuration` |
| 工具系统 | `/docs/user-guide/features/tools` |
| 记忆系统 | `/docs/user-guide/features/memory` |
| Skill 系统 | `/docs/user-guide/features/skills` |
| MCP 集成 | `/docs/user-guide/features/mcp` |
| 语音模式 | `/docs/user-guide/features/voice-mode` |
| 个性/SOUL.md | `/docs/user-guide/features/personality` |
| 上下文文件 | `/docs/user-guide/features/context-files` |
| 安全 | `/docs/user-guide/security` |
| 架构 | `/docs/developer-guide/architecture` |


### 相关概念

- [[hermes生态]] — Hermes 工具与生态配置
- [[skill哲学]] — Hermes Skill 设计原则
- [[白夜开源精选]] — 开源工具精选
- [[自进化学习循环]]


### 相关实体

- [[MemOS]] — 结构化记忆系统
- [[Chroma]] — 向量检索
- [[Scrapling]] — 爬虫框架
- [[Camoufox]] — 轻量浏览器
- [[Obscura]] — Rust 无头浏览器
- [[MemPalace]] — 记忆宫殿
- [[MemRec]] — 项目记忆
- [[Mem-Forever]] — 极简记忆
- [[Firecrawl]] — Web 数据提取
- [[browser-harness]] — 浏览器自动化工具


---

## Install

### Windows or macOS

To easily install the command-line and desktop applications, [download the Hermes Desktop installer](https://hermes-agent.nousresearch.com/) from our website and run it.

### Without Hermes Desktop:

For a command-line only install without Hermes Desktop, run:

#### Linux / macOS / WSL2 / Android (Termux)
```
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash  
```

#### Windows (native)
Run in powershell:
```
iex (irm https://hermes-agent.nousresearch.com/install.ps1)  
```

See the full **[Installation Guide](/docs/getting-started/installation)** for what the installer does, the per-user vs root layout, and Windows-specific notes. For the complete platform support matrix, see **[Platform Support](/docs/getting-started/platform-support)**.

Fastest path to a working agent

After installing, run `hermes setup --portal` — one OAuth covers a model plus all four Tool Gateway tools (web search, image generation, TTS, browser). See [Nous Portal](/docs/integrations/nous-portal).

## What is Hermes Agent?

It's not a coding copilot tethered to an IDE or a chatbot wrapper around a single API. It's an **autonomous agent** that gets more capable the longer it runs. It lives wherever you put it — a $5 VPS, a GPU cluster, or serverless infrastructure (Daytona, Modal) that costs nearly nothing when idle. Talk to it from Telegram while it works on a cloud VM you never SSH into yourself. It's not tied to your laptop.

## Quick Links

|   |  
|---|  
🚀 **[Installation](/docs/getting-started/installation)**| Install in 60 seconds on Linux, macOS, WSL2, native Windows, or Android  
📖 **[Quickstart Tutorial](/docs/getting-started/quickstart)**| Your first conversation and key features to try  
🗺️ **[Learning Path](/docs/getting-started/learning-path)**| Find the right docs for your experience level  
⚙️ **[Configuration](/docs/user-guide/configuration)**| Config file, providers, models, and options  
💬 **[Messaging Gateway](/docs/user-guide/messaging)**| Set up Telegram, Discord, Slack, WhatsApp, Teams, or more  
🔧 **[Tools& Toolsets](/docs/user-guide/features/tools)**| 60+ built-in tools and how to configure them  
🧠 **[Memory System](/docs/user-guide/features/memory)**| Persistent memory that grows across sessions  
📚 **[Skills System](/docs/user-guide/features/skills)**| Procedural memory the agent creates and reuses  
🔌 **[MCP Integration](/docs/user-guide/features/mcp)**| Connect to MCP servers, filter their tools, and extend Hermes safely  
🧭 **[Use MCP with Hermes](/docs/guides/use-mcp-with-hermes)**| Practical MCP setup patterns, examples, and tutorials  
🎙️ **[Voice Mode](/docs/user-guide/features/voice-mode)**| Real-time voice interaction in CLI, Telegram, Discord, and Discord VC  
🗣️ **[Use Voice Mode with Hermes](/docs/guides/use-voice-mode-with-hermes)**| Hands-on setup and usage patterns for Hermes voice workflows  
🎭 **[Personality& SOUL.md](/docs/user-guide/features/personality)**| Define Hermes' default voice with a global SOUL.md  
📄 **[Context Files](/docs/user-guide/features/context-files)**| Project context files that shape every conversation  
🔒 **[Security](/docs/user-guide/security)**| Command approval, authorization, container isolation  
💡 **[Tips& Best Practices](/docs/guides/tips)**| Quick wins to get the most out of Hermes  
🏗️ **[Architecture](/docs/developer-guide/architecture)**| How it works under the hood  
❓ **[FAQ& Troubleshooting](/docs/reference/faq)**| Common questions and solutions  

## Key Features

  * **A closed learning loop** — Agent-curated memory with periodic nudges, autonomous skill creation, skill self-improvement during use, FTS5 cross-session recall with LLM summarization, and Honcho dialectic user modeling
  * **Runs anywhere, not just your laptop** — 6 terminal backends: local, Docker, SSH, Daytona, Singularity, Modal. Daytona and Modal offer serverless persistence — your environment hibernates when idle, costing nearly nothing
  * **Lives where you do** — CLI, Telegram, Discord, Slack, WhatsApp, Signal, Matrix, Mattermost, Email, SMS, DingTalk, Feishu, WeCom, Weixin, QQ Bot, Yuanbao, BlueBubbles, Home Assistant, Microsoft Teams, Google Chat, and more — 20+ platforms from one gateway
  * **Built by model trainers** — Created by Nous Research, the lab behind Hermes, Nomos, and Psyche. Works with Nous Portal, OpenRouter, OpenAI, or any endpoint
  * **Scheduled automations** — Built-in cron with delivery to any platform
  * **Delegates & parallelizes** — Spawn isolated subagents for parallel workstreams. Programmatic Tool Calling via execute_code collapses multi-step pipelines into single inference calls
  * **Open standard skills** — Compatible with agentskills.io. Skills are portable, shareable, and community-contributed via the Skills Hub
  * **Full web control** — Search, extract, browse, vision, image generation, TTS — one subscription via Nous Portal bundles all of them
  * **MCP support** — Connect to any MCP server for extended tool capabilities
  * **Research-ready** — Batch processing, trajectory export, RL training with Atropos. Built by Nous Research — the lab behind Hermes, Nomos, and Psyche models



## For LLMs and coding agents

Machine-readable entry points to this documentation:

  * **[`/llms.txt`](/docs/assets/files/llms-c03199c2b1721b8eb2141fff54dcfad5.txt)** — curated index of every doc page with short descriptions. ~17 KB, safe to load into an LLM context.
  * **[`/llms-full.txt`](/docs/assets/files/llms-full-80577b0f7c870fab3a5fd02a6d504ddd.txt)** — every doc page concatenated into a single markdown file for one-shot ingestion. ~1.8 MB.


Both files also resolve at `/docs/llms.txt` and `/docs/llms-full.txt`. Generated fresh on every deploy.

[Edit this page](https://github.com/NousResearch/hermes-agent/edit/main/website/docs/index.mdx)

Docs

  * [Getting Started](/docs/getting-started/quickstart)
  * [User Guide](/docs/user-guide/cli)
  * [Developer Guide](/docs/developer-guide/architecture)
  * [Reference](/docs/reference/cli-commands)


Community

  * [Discord](https://discord.gg/NousResearch)
  * [GitHub Issues](https://github.com/NousResearch/hermes-agent/issues)
  * [Skills Hub](https://agentskills.io)


More

  * [Desktop Download](https://hermes-agent.nousresearch.com/)
  * [GitHub](https://github.com/NousResearch/hermes-agent)
  * [Nous Research](https://nousresearch.com)

Built by [Nous Research](https://nousresearch.com) · MIT License · 2026  
| ❓ **[FAQ& Troubleshooting](https://hermes-agent.nousresearch.com/docs/reference/faq)**  | Common questions and solutions  |  
## Key Features[​](https://hermes-agent.nousresearch.com/docs#key-features "Direct link to Key Features")
  * **A closed learning loop** — Agent-curated memory with periodic nudges, autonomous skill creation, skill self-improvement during use, FTS5 cross-session recall with LLM summarization, and [Honcho](https://github.com/plastic-labs/honcho) dialectic user modeling
  * **Runs anywhere, not just your laptop** — 6 terminal backends: local, Docker, SSH, Daytona, Singularity, Modal. Daytona and Modal offer serverless persistence — your environment hibernates when idle, costing nearly nothing
  * **Lives where you do** — CLI, Telegram, Discord, Slack, WhatsApp, Signal, Matrix, Mattermost, Email, SMS, DingTalk, Feishu, WeCom, Weixin, QQ Bot, Yuanbao, BlueBubbles, Home Assistant, Microsoft Teams, Google Chat, and more — 20+ platforms from one gateway
  * **Built by model trainers** — Created by [Nous Research](https://nousresearch.com), the lab behind Hermes, Nomos, and Psyche. Works with [Nous Portal](https://portal.nousresearch.com), [OpenRouter](https://openrouter.ai), OpenAI, or any endpoint
  * **Scheduled automations** — Built-in cron with delivery to any platform
  * **Delegates & parallelizes** — Spawn isolated subagents for parallel workstreams. Programmatic Tool Calling via `execute_code` collapses multi-step pipelines into single inference calls
  * **Open standard skills** — Compatible with [agentskills.io](https://agentskills.io). Skills are portable, shareable, and community-contributed via the Skills Hub
  * **Full web control** — Search, extract, browse, vision, image generation, TTS — one subscription via [Nous Portal](https://hermes-agent.nousresearch.com/docs/integrations/nous-portal) bundles all of them
  * **MCP support** — Connect to any MCP server for extended tool capabilities
  * **Research-ready** — Batch processing, trajectory export, RL training with Atropos. Built by [Nous Research](https://nousresearch.com) — the lab behind Hermes, Nomos, and Psyche models


## For LLMs and coding agents[​](https://hermes-agent.nousresearch.com/docs#for-llms-and-coding-agents "Direct link to For LLMs and coding agents")
Machine-readable entry points to this documentation:
  * **[`/llms.txt`](https://hermes-agent.nousresearch.com/docs/assets/files/llms-bcf65f79b33e57e6c0cce5b9627945d4.txt)**— curated index of every doc page with short descriptions. ~17 KB, safe to load into an LLM context.
  * **[`/llms-full.txt`](https://hermes-agent.nousresearch.com/docs/assets/files/llms-full-00235826279c78cd53e3b34278392ee9.txt)**— every doc page concatenated into a single markdown file for one-shot ingestion. ~1.8 MB.


Both files also resolve at `/docs/llms.txt` and `/docs/llms-full.txt`. Generated fresh on every deploy.
[](https://github.com/NousResearch/hermes-agent/edit/main/website/docs/index.mdx)
Docs
  * [Getting Started](https://hermes-agent.nousresearch.com/docs/getting-started/quickstart)
  * [User Guide](https://hermes-agent.nousresearch.com/docs/user-guide/cli)
  * [Developer Guide](https://hermes-agent.nousresearch.com/docs/developer-guide/architecture)
  * [Reference](https://hermes-agent.nousresearch.com/docs/reference/cli-commands)


Community
  * [Discord](https://discord.gg/NousResearch)
  * [GitHub Discussions](https://github.com/NousResearch/hermes-agent/discussions)
  * [Skills Hub](https://agentskills.io)


More
  * [GitHub](https://github.com/NousResearch/hermes-agent)
  * [Nous Research](https://nousresearch.com)


Built by [Nous Research](https://nousresearch.com) · MIT License · 2026


> **补充来源**: [2026-06-13_Hermes_Agent.md](../01_inbox/articles/2026-06-13_Hermes_Agent.md)

> ## 新增要点 (2026-06-13 抓取)
>
> ### 安装方式更新
> - **Hermes Desktop 安装器**：新增桌面+CLI 一站式安装，支持 Windows/macOS
> - **安装命令更新**：`curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash`（替代旧的 raw.githubusercontent.com 路径）
> - **Windows native**：PowerShell `iex (irm https://hermes-agent.nousresearch.com/install.ps1)`
> - **Android Termux**：自动检测 Termux 环境
> - **Nous Portal**：`hermes setup --portal` 一次 OAuth 覆盖模型 + 4 个 Tool Gateway 工具
>
> ### 新增快速链接
> - 🎙️ **Voice Mode** — CLI/Telegram/Discord/Discord VC 实时语音交互
> - 🗣️ **Use Voice Mode with Hermes** — 语音工作流设置指南
> - 🎭 **Personality & SOUL.md** — 用全局 SOUL.md 定义 Hermes 默认人格
> - 📄 **Context Files** — 项目上下文文件，塑造每轮对话
> - 🔒 **Security** — 命令审批、授权、容器隔离
> - 💡 **Tips & Best Practices** — 快速上手技巧
> - 🏗️ **Architecture** — 架构原理
> - ❓ **FAQ & Troubleshooting** — 常见问题排查
>
> ### Key Features 更新
> - **Scheduled automations** — 内置 cron，支持投递到任意平台（新增）
> - **Delegates & parallelizes** — 新增 `execute_code` 程序化工具调用
> - **Lives where you do** — 扩展至 20+ 平台：新增 WeCom、Weixin、QQ Bot、Yuanbao、BlueBubbles、Microsoft Teams、Google Chat
> - **Research-ready** — Batch processing、trajectory export、RL training with Atropos（新增）
> - **Full web control** — 一次 Nous Portal 订阅捆绑所有工具（新增描述）

> - [[15个被忽略的Agent高级能力-王二AI进化论]] — 15个高级用法（/personality, /branch, /insights, Skills 等）
> - [[10个神操作让Hermes全天候主动干活]] — 10个自动化配置技巧

> **补充来源**: [2026-05-29_Hermes-Agent进阶补充-会聊天到会干活.md](../01-收件箱/文章/2026-05-29_Hermes-Agent进阶补充-会聊天到会干活.md)

> **2026-06-14 自动抓取补充**
> 
> ### llms.txt 更新
> - `llms.txt` hash: `d4972c57170916efd83766ae50c3bb3d`（之前是 `bcf65f79b33e57e6c0cce5b9627945d4`）
> - `llms-full.txt` hash: `651f35a50067b3f582e4e9dc4b3eef16`（之前是 `00235826279c78cd53e3b34278392ee9`）
> - llms-full.txt 从 1.6 MB 增长至 1.8 MB，说明文档内容有新增
> - 两个文件现也同时可在 `/docs/llms.txt` 和 `/docs/llms-full.txt` 访问
>
> **2026-06-17 自动抓取补充**
> 
> ### llms.txt 状态
> - 页面内容稳定，无明显新增章节
> - llms-full.txt hash 更新为 `a10ec215805fedcfa4cd8a4d66f63e91`
> - Hermes Desktop 安装方式已作为首选推荐途径
>
> **2026-06-18 自动抓取补充 (第2轮)**
>
> ### llms-full.txt 再次变更
> - llms-full.txt hash 再次更新为 `a7774fddbb545729650179b373c807d3`（从 `1fd95a836e3a50458dd176331d7e8437`）
> - llms.txt hash 保持 `d4972c57170916efd83766ae50c3bb3d` 不变
> - 页面可见内容无结构性变化，增量更新可能涉及深层文档细节
> - 无需要补充到主体笔记的新知识点
>
> **2026-06-19 自动抓取补充**
>
> ### llms-full.txt hash 再次更新
> - llms-full.txt hash: `1972cd64364e964ea2d8bbc1d6e59bff`（从 `a7774fddbb545729650179b373c807d3`）
> - llms.txt hash 保持 `d4972c57170916efd83766ae50c3bb3d` 不变
> - 页面可见内容无结构性变化，仍为 Hermes Agent 首页
> - 无需要补充到主体笔记的新知识点
>
> **2026-06-21 自动抓取补充**
>
> ### llms.txt / llms-full.txt 双更新
> - llms.txt hash: `c03199c2b1721b8eb2141fff54dcfad5`（从 `d4972c57170916efd83766ae50c3bb3d`）
> - llms-full.txt hash: `6b61486b45a8abec596025ac17ed338f`（从 `1972cd64364e964ea2d8bbc1d6e59bff`）
> - 页面可见内容无结构性变化，仍为 Hermes Agent 首页
> - hash 更新说明文档有微小增量修正，无需更新主体笔记
>
> **2026-06-21 第2轮自动抓取补充**
>
> ### llms-full.txt hash 再次变更
> - llms-full.txt hash: `aa5cd62b671da51688511c10b80985f6`（从 `6b61486b45a8abec596025ac17ed338f`）
> - llms.txt hash 保持 `c03199c2b1721b8eb2141fff54dcfad5` 不变
> - 页面可见内容无结构性变化
> - 预计文档有微小增量修正，无需更新主体笔记

> **2026-06-23 第1轮自动抓取**
>
> ### llms-full.txt 更新
> - llms-full.txt hash: `2c3fb33fccd4f74e8113cb216416235d`（从 `78469c45550d9a382bd01cf24e7152cd`）
> - llms.txt hash 保持 `c03199c2b1721b8eb2141fff54dcfad5` 不变
> - 首页新增 "Desktop Download" 导航链接和 "Download Desktop" 按钮
> - 安装引导改为优先推荐 Hermes Desktop（Windows/macOS）
> - hash 更新因文档微调和页面元素调整，无需更新主体笔记
>
> **2026-06-23 第2轮自动抓取**
>
> ### llms-full.txt hash 再次更新
> - llms-full.txt hash: `9bb4c2e97684f6ff105c755c93f4c9f8`（从 `2c3fb33fccd4f74e8113cb216416235d`）
> - llms.txt hash 保持 `c03199c2b1721b8eb2141fff54dcfad5` 不变
> - 页面可见内容无结构性变化，仍为 Hermes Agent 首页
> - hash 更新说明文档有微小增量修正，无需更新主体笔记
>
> **2026-06-24 自动抓取**
>
> ### llms-full.txt hash 再次更新
> - llms-full.txt hash: `cdb9d5f9d739fe1ba5a7ff06968c4fbf`（从 `9bb4c2e97684f6ff105c755c93f4c9f8`）
> - llms.txt hash 保持 `c03199c2b1721b8eb2141fff54dcfad5` 不变
> - 页面可见内容无结构性变化，仍为 Hermes Agent 首页
> - hash 更新说明文档有微小增量修正，无需更新主体笔记
> 
> ### 2026-06-24 06:00 后台维护

> | 操作 | 详情 |
> |:----|:------|
> | 编译 | 01_inbox/articles/ 1 个新文件 (Hermes Agent 2026-06-24) — 同一来源 (hermes-agent.nousresearch.com/docs)，llms-full.txt hash 从 `9bb4c2e9...` 变更为 `cdb9d5f9...`，页面内容无结构性变化 |
> | 归档 | 01_inbox/articles/ 2 个文件 → archive/articles/2026-06-23/ + 2026-06-24/ |
> | 去重 | 06-23 文件与 06-24 文件内容几乎一致 (仅 frontmatter 日期 + llms-full.txt hash 不同)，均与已有笔记重复 |
> | 概念补充 | Hermes-Agent.md 追加 06-24 hash 变更记录 |
> | 地图状态 | 07-地图/ 两份地图均无需更新 — hash 增量变更，非新领域 |

> 最终状态：
> - 01_inbox: 0 个待处理文件（已全部归档）
> - 01-收件箱: 所有子目录均为空
> - 02-笔记/概念/Hermes-Agent.md: 已追加 06-24 hash 记录
> - 02-笔记 合计 154 个文件（实体 64 + 概念 39 + 方法 51）

> **2026-06-25 自动抓取**

> ### llms-full.txt hash 再次更新
> - llms-full.txt hash: `57c49f3de4c07ae0a2480092f94f8023`（从 `cdb9d5f9d739fe1ba5a7ff06968c4fbf`）
> - llms.txt hash 保持 `c03199c2b1721b8eb2141fff54dcfad5` 不变
> - 页面可见内容无结构性变化，仍为 Hermes Agent 首页
> - hash 更新说明文档有微小增量修正，无需更新主体笔记

> **2026-06-25 第2轮自动抓取**

> ### llms-full.txt hash 再次更新
> - llms-full.txt hash: `d60780d6c5ad51db8bf2674e2c8f46d5`（从 `57c49f3de4c07ae0a2480092f94f8023`）
> - llms.txt hash 保持 `c03199c2b1721b8eb2141fff54dcfad5` 不变
> - 页面可见内容无结构性变化
> - hash 更新说明文档有微小增量修正，无需更新主体笔记

> **2026-06-26 自动抓取**

> ### llms-full.txt hash 再次更新
> - llms-full.txt hash: `bd47ab395cc163202c8f1bbdc8b67b72`（从 `d60780d6c5ad51db8bf2674e2c8f46d5`）
> - llms.txt hash 保持 `c03199c2b1721b8eb2141fff54dcfad5` 不变
> - 页面可见内容无结构性变化，仍为 Hermes Agent 首页
> - hash 更新说明文档有微小增量修正，无需更新主体笔记

> **2026-06-26 第2轮自动抓取**

> ### llms-full.txt hash 再次更新
> - llms-full.txt hash: `9f09c1f7ab9f49a46517ad7783e90c5e`（从 `bd47ab395cc163202c8f1bbdc8b67b72`）
> - llms.txt hash 保持 `c03199c2b1721b8eb2141fff54dcfad5` 不变
> - 页面可见内容无结构性变化，仍为 Hermes Agent 首页
> - hash 更新说明文档有微小增量修正，无需更新主体笔记

> **2026-06-27 第1轮自动抓取**
>
> ### llms-full.txt hash: 从 `9f09c1f7ab9f49a46517ad7783e90c5e` → `34a90a10e37ed8157e7a4917ba889be4`
> - llms.txt hash 保持 `c03199c2b1721b8eb2141fff54dcfad5` 不变
> - 页面可见内容无结构性变化，仍为 Hermes Agent 首页
> - hash 更新说明文档有微小增量修正，无需更新主体笔记
>
> **2026-06-28 第1轮自动抓取**
>
> ### llms-full.txt hash: 从 `f23a01219e1980a3ee2ed4f0a643d1cf` → `d57718473b7b1e3c4ef2e6a6f08d5358`
> - llms.txt hash 保持 `c03199c2b1721b8eb2141fff54dcfad5` 不变
> - 页面可见内容无结构性变化，仍为 Hermes Agent 首页
> - hash 更新说明文档有微小增量修正，无需更新主体笔记
>
> **2026-06-28 第2轮自动抓取**
>
> ### llms-full.txt hash: 从 `d57718473b7b1e3c4ef2e6a6f08d5358` → `8dbc442d00426d35e4c77f693f13714b`
> - llms.txt hash 保持 `c03199c2b1721b8eb2141fff54dcfad5` 不变
> - 页面可见内容无结构性变化，仍为 Hermes Agent 首页
> - hash 更新说明文档有微小增量修正，无需更新主体笔记
>
> **2026-06-27 第2轮自动抓取**
>
> ### llms-full.txt hash: 从 `34a90a10e37ed8157e7a4917ba889be4` → `f23a01219e1980a3ee2ed4f0a643d1cf`
> - llms.txt hash 保持 `c03199c2b1721b8eb2141fff54dcfad5` 不变
> - **结构性变化**：
>   - 新增 **Platform Support 链接**：安装引导中的命令式安装部分新增 "For the complete platform support matrix, see Platform Support"（`/docs/getting-started/platform-support`）
>   - 底部 Community 板块 **GitHub Discussions → GitHub Issues**
>   - 底部新增 **Desktop Download 链接** 
> - 首页主体内容（Features、Quick Links）无实质变化
> - 此为小幅页面微调，无需更新主体笔记正文，仅记录 changelog
>
> **2026-06-29 第1轮自动抓取**
>
> ### llms-full.txt hash: `84be2f381942efb5f7d70ab48be42b83`（新捕获，较之前 `8dbc442d00426d35e4c77f693f13714b` 更新）
> - llms.txt hash 保持 `c03199c2b1721b8eb2141fff54dcfad5` 不变
> - 页面可见内容无结构性变化，仍为 Hermes Agent 首页
> - hash 更新说明文档有微小增量修正，无需更新主体笔记
>
> **2026-06-29 第2轮自动抓取**
>
> ### llms-full.txt hash: `1db8e1c31d5d6a55ac53055945a3e83d`（从 `84be2f381942efb5f7d70ab48be42b83`）
> - llms.txt hash 保持 `c03199c2b1721b8eb2141fff54dcfad5` 不变
> - 页面可见内容无结构性变化，仍为 Hermes Agent 首页
> - hash 再次更新说明文档在下半天又有增量修正，无需更新主体笔记
>
> **2026-06-30 自动抓取**
>
> ### llms-full.txt hash: `7d9ac679546bfbcab576adbae2ab9e82`（从 `1e45778b03fa3c0dc6868ac10f613d09`）
> - llms.txt hash 保持 `c03199c2b1721b8eb2141fff54dcfad5` 不变
> - 页面可见内容无结构性变化，仍为 Hermes Agent 首页
> - hash 再次更新说明文档有增量修正，无需更新主体笔记
>
> **2026-06-29 第3轮自动抓取 (后台维护)**
> 
> ### llms-full.txt hash: `1e45778b03fa3c0dc6868ac10f613d09`（从 `1db8e1c31d5d6a55ac53055945a3e83d`）
> - llms.txt hash 保持 `c03199c2b1721b8eb2141fff54dcfad5` 不变
> - 页面可见内容无结构性变化，仍为 Hermes Agent 首页
> - hash 再次更新，说明文档有增量修正，无需更新主体笔记
>
> **2026-06-30 第2轮自动抓取 (后台维护)**
> 
> | 操作 | 详情 |
> |:----|:------|
> | 编译 | 01_inbox/articles/ 第2个新文件 (Hermes Agent 2026-06-30 v2) — 同一来源 (hermes-agent.nousresearch.com/docs)，llms-full.txt hash 从 `7d9ac67954...` 变更为 `fb26490645...`，页面内容无结构性变化 |
> | 归档 | 01_inbox/articles/ 1 个文件 → archive/articles/2026-06-30/2026-06-30_Hermes_Agent_v2.md |
> | 去重 | 与 06-30 归档文件几乎一致 (仅 llms-full.txt hash 不同)，均与已有笔记重复 |
> | 概念补充 | 仅在 changelog 记录 hash 更新，无需修改笔记正文 |
> | 地图状态 | 07-地图/ 两份地图均无需更新 — hash 增量变更，非新领域 |
>
> **2026-06-30 第3轮自动抓取 (后台维护)**
>
> ### llms-full.txt hash: `01742c6c48895293451b17fe07d7c016`（从 `fb26490645...`）
> - llms.txt hash 保持 `c03199c2b1721b8eb2141fff54dcfad5` 不变
> - 页面可见内容无结构性变化，仍为 Hermes Agent 首页
> - hash 再次更新说明文档在高频增量修正，无需更新主体笔记

> **2026-07-01 自动抓取 (后台维护)**

> ### llms-full.txt hash: `2fb28cd06885baab9d09c1697e222939`（从 `7d9ac679546bfbcab576adbae2ab9e82`）
> - llms.txt hash 保持 `c03199c2b1721b8eb2141fff54dcfad5` 不变
> - 页面可见内容无结构性变化，仍为 Hermes Agent 首页
> - hash 再次更新说明文档有增量修正，无需更新主体笔记

> **2026-07-01 第2轮自动抓取 (后台维护)**
> 
> ### llms-full.txt hash: `ea8eaa45cfaf3951768f7b15de45ea53`（从 `2fb28cd06885baab9d09c1697e222939`）
> - llms.txt hash 保持 `c03199c2b1721b8eb2141fff54dcfad5` 不变
> - 页面可见内容无结构性变化，仍为 Hermes Agent 首页
> - 同一日内 hash 第2次变动，说明 Hermes 官方在持续交付文档更新，无需更新主体笔记
>
> **2026-07-02 自动抓取 (后台维护)**
>
> ### llms-full.txt hash: `23221f7bfd767039d8a3e5a4215c8185`（从 `86aa311e7944cdcc2a88db0c24e14c03`）
> - llms.txt hash 保持 `c03199c2b1721b8eb2141fff54dcfad5` 不变
> - 页面可见内容无结构性变化，仍为 Hermes Agent 首页
> - hash 再次更新，说明文档有增量修正，无需更新主体笔记
>
> **2026-07-03 自动抓取 (后台维护)**
>
> ### llms-full.txt hash: `dc1c09bb4fb184345926ad82432edfb5`（从 `23221f7bfd767039d8a3e5a4215c8185`）
> - llms.txt hash 保持 `c03199c2b1721b8eb2141fff54dcfad5` 不变
> - 页面可见内容无结构性变化，仍为 Hermes Agent 首页
> - hash 再次更新，说明文档有持续增量修正，无需更新主体笔记
>
> **2026-07-04 自动抓取 (后台维护)**
>
> ### llms-full.txt hash: `4991f316e41bbffa77259afaedf5b551`（从 `dc1c09bb4fb184345926ad82432edfb5`）
> - llms.txt hash 保持 `c03199c2b1721b8eb2141fff54dcfad5` 不变
> - 页面可见内容无结构性变化，仍为 Hermes Agent 首页
> - hash 再次更新，说明文档有持续增量修正，无需更新主体笔记
> **2026-07-05 第2轮自动抓取 (后台维护)**
>
> ### llms-full.txt hash: `708a4f8d2271effb0aaba08a9fcd8f8c`（上一轮归档的 07-05 为 `bdc59233...`）
> - llms.txt hash 保持 `c03199c2b1721b8eb2141fff54dcfad5` 不变
> - 页面可见内容无结构性变化，仍为 Hermes Agent 首页
> - hash 再次更新说明文档有增量修正，无需更新主体笔记
>
> **2026-07-06 自动抓取 (后台维护)**
>
> ### llms-full.txt hash: `3cc1f036182334a5610cf4ad48a0a4b2`（从 `708a4f8d22...`）
> - llms.txt hash 保持 `c03199c2b1721b8eb2141fff54dcfad5` 不变
> - 页面可见内容无结构性变化，仍为 Hermes Agent 首页
> - hash 再次更新说明文档有增量修正，无需更新主体笔记
>
> **2026-07-07 自动抓取 (后台维护)**
>
> ### llms-full.txt hash: `85605f39b09716dbb9931ad83d6252c2`（从 `3cc1f03618...`）
> - llms.txt hash 保持 `c03199c2b1721b8eb2141fff54dcfad5` 不变
> - 页面可见内容无结构性变化，仍为 Hermes Agent 首页
> - hash 更新说明文档有持续增量修正，无需更新主体笔记
>
> **2026-07-08 自动抓取 (后台维护)**
>
> ### llms.txt hash: `96828202fb001238524b85bb053418e2`（从稳定的 `c03199c2b1721b8eb2141fff54dcfad5` — 首次变更自 06-21）
> ### llms-full.txt hash: `aabe720e853b46f9dc68806818e68f1c`（从 `85605f39b097...`）
> - **双 hash 同时变更**：llms.txt 自 06-21 以来首次变化，说明文档目录结构有新增或调整
> - 页面可见内容无结构性变化，仍为 Hermes Agent 首页
> - hash 双更新可能是社区/版本相关页面新增，无需更新主体笔记

> **2026-07-09 自动抓取 (后台维护)**
>
> ### llms-full.txt hash: `8b89e1d30aab2bcd16daa9841188fa0e`（从 `06e8a7a3a1bf471d71f799415b1ec915`）
> - llms.txt hash 保持 `96828202fb001238524b85bb053418e2` 不变（连续第2天稳定）
> - 页面可见内容无结构性变化，仍为 Hermes Agent 首页
> - hash 再次更新说明文档有增量修正，无需更新主体笔记
> - 实体/Hermes_Agent.md 已从 751B 薄编译增强至 4.5KB 完整文档
>
> **2026-07-11 自动抓取 (后台维护)**
>
> ### llms-full.txt hash: `205a0c4afe4c6e6116fd22ff6e842973`（从 `8b89e1d30aab2bcd16daa9841188fa0e`）
> - llms.txt hash 保持 `96828202fb001238524b85bb053418e2` 不变（连续第5天稳定）
> - 页面可见内容无结构性变化，仍为 Hermes Agent 首页
> - hash 再次更新说明文档有持续增量修正，无需更新主体笔记

> **2026-07-12 自动抓取 (后台维护)**
>
> ### llms-full.txt hash: `a69c8575e5851636612bb8753f829a3a`（从 `205a0c4afe4c6e6116fd22ff6e842973`）
> - llms.txt hash 保持 `96828202fb001238524b85bb053418e2` 不变（连续第6天稳定）
> - 页面可见内容无结构性变化，仍为 Hermes Agent 首页
> - hash 更新说明文档有持续增量修正，无需更新主体笔记
> **2026-07-12 第2轮自动抓取 (后台维护)**
>
> ### llms-full.txt hash: `1602b96374536ae815a46439808cb03e`（从 `a69c8575e5851636612bb8753f829a3a`）
> - llms.txt hash 保持 `96828202fb001238524b85bb053418e2` 不变（连续第7天稳定）
> - 页面可见内容无结构性变化，仍为 Hermes Agent 首页
> - hash 再次更新说明文档有持续增量修正，无需更新主体笔记
> - 资源表 llms-full.txt hash 引用已同步更新
>
> **2026-07-13 自动抓取 (后台维护)**
>
> ### llms-full.txt hash: `ace192bd99b3e5a08da52078ed01ea56`（从 `1602b96374536ae815a46439808cb03e`）
> - llms.txt hash 保持 `96828202fb001238524b85bb053418e2` 不变（连续第8天稳定）
> - 页面可见内容无结构性变化，仍为 Hermes Agent 首页
> - hash 再次更新说明文档有持续增量修正，无需更新主体笔记
> - 资源表 llms-full.txt hash 引用已同步更新
>
> > **2026-07-13 第2轮自动抓取 (后台维护)**
> >
> > ### llms-full.txt hash: `0ec259c6c5f061f9b231a7f6d767f3ba`（从 `ace192bd99b3e5a08da52078ed01ea56`）
> > - llms.txt hash 保持 `96828202fb001238524b85bb053418e2` 不变（连续第9天稳定）
> > - 页面可见内容无结构性变化，仍为 Hermes Agent 首页
> > - hash 再次更新说明文档有持续增量修正，无需更新主体笔记
> > - 资源表 llms-full.txt hash 引用已同步更新
> **2026-07-14 自动抓取 (后台维护)**
>
> ### llms-full.txt hash: `80577b0f7c870fab3a5fd02a6d504ddd`（从 `0ec259c6c5f061f9b231a7f6d767f3ba`）
> - llms.txt hash 保持 `96828202fb001238524b85bb053418e2` 不变（连续第10天稳定）
> - 页面可见内容无结构性变化，仍为 Hermes Agent 首页
> - hash 再次更新说明文档有持续增量修正，无需更新主体笔记
> - 资源表 llms-full.txt hash 引用已同步更新
>
> **2026-07-15 自动抓取 (后台维护)**
>
> ### llms-full.txt hash: `9a44b206613a9e22fca6a4b93dbd3362`（从 `80577b0f7c870fab3a5fd02a6d504ddd`）
> - llms.txt hash 保持 `96828202fb001238524b85bb053418e2` 不变（连续第11天稳定）
> - 页面可见内容无结构性变化，仍为 Hermes Agent 首页
> - hash 再次更新说明文档有持续增量修正，无需更新主体笔记
> - 资源表 llms-full.txt hash 引用已同步更新

> **2026-07-16 自动抓取 (后台维护)**
>
> ### llms-full.txt hash: `9c18cca702cbba85524ce21b00ab48c6`（从 `9a44b206613a9e22fca6a4b93dbd3362`）
> - llms.txt hash 保持 `96828202fb001238524b85bb053418e2` 不变（连续第12天稳定）
> - 页面可见内容无结构性变化，仍为 Hermes Agent 首页
> - hash 再次更新说明文档有持续增量修正，无需更新主体笔记
> - 资源表 llms-full.txt hash 引用已同步更新

|
