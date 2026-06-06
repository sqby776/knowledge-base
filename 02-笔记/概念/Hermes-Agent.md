---
title: Hermes Agent
created: 2026-05-29
updated: 2026-05-29
tags: ["auto-capture", auto-compiled]
status: compiled
sources: [https://hermes-agent.nousresearch.com/docs]
source_url: https://hermes-agent.nousresearch.com/docs
---

# Hermes Agent

> 自动抓取自: [https://hermes-agent.nousresearch.com/docs](https://hermes-agent.nousresearch.com/docs)

[Skip to main content](https://hermes-agent.nousresearch.com/docs#__docusaurus_skipToContent_fallback)
[![Hermes Agent](https://hermes-agent.nousresearch.com/docs/img/logo.png) **Hermes Agent**](https://hermes-agent.nousresearch.com/docs/)[Docs](https://hermes-agent.nousresearch.com/docs/user-stories)[Skills](https://hermes-agent.nousresearch.com/docs/skills)
[](https://hermes-agent.nousresearch.com/docs)
  * [English](https://hermes-agent.nousresearch.com/docs/)
  * [简体中文](https://hermes-agent.nousresearch.com/docs/zh-Hans/)


[Home](https://hermes-agent.nousresearch.com)[GitHub](https://github.com/NousResearch/hermes-agent)[Discord](https://discord.gg/NousResearch)
`ctrl``K`
  * [User Stories & Use Cases](https://hermes-agent.nousresearch.com/docs/user-stories)
  * [Getting Started](https://hermes-agent.nousresearch.com/docs)
  * [Using Hermes](https://hermes-agent.nousresearch.com/docs)
  * [Features](https://hermes-agent.nousresearch.com/docs)
  * [Messaging Platforms](https://hermes-agent.nousresearch.com/docs)
  * [Integrations](https://hermes-agent.nousresearch.com/docs)
  * [Guides & Tutorials](https://hermes-agent.nousresearch.com/docs)
  * [Developer Guide](https://hermes-agent.nousresearch.com/docs)
  * [Reference](https://hermes-agent.nousresearch.com/docs)


  * [](https://hermes-agent.nousresearch.com/docs/)


# Hermes Agent
The self-improving AI agent built by [Nous Research](https://nousresearch.com). The only agent with a built-in learning loop — it creates skills from experience, improves them during use, nudges itself to persist knowledge, and builds a deepening model of who you are across sessions.
[Get Started →](https://hermes-agent.nousresearch.com/docs/getting-started/installation)[View on GitHub](https://github.com/NousResearch/hermes-agent)
## Install[​](https://hermes-agent.nousresearch.com/docs#install "Direct link to Install")
**Linux / macOS / WSL2**

```
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash  

```

**Windows (native, PowerShell)** — _early beta,[details →](https://hermes-agent.nousresearch.com/docs/user-guide/windows-native)_

```
iex (irm https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.ps1)  

```

**Android (Termux)** — same curl one-liner as Linux; the installer auto-detects Termux.
See the full **[Installation Guide](https://hermes-agent.nousresearch.com/docs/getting-started/installation)** for what the installer does, the per-user vs root layout, and Windows-specific notes.
After installing, run `hermes setup --portal` — one OAuth covers a model plus all four Tool Gateway tools (web search, image generation, TTS, browser). See [Nous Portal](https://hermes-agent.nousresearch.com/docs/integrations/nous-portal).
## What is Hermes Agent?[​](https://hermes-agent.nousresearch.com/docs#what-is-hermes-agent "Direct link to What is Hermes Agent?")
It's not a coding copilot tethered to an IDE or a chatbot wrapper around a single API. It's an **autonomous agent** that gets more capable the longer it runs. It lives wherever you put it — a $5 VPS, a GPU cluster, or serverless infrastructure (Daytona, Modal) that costs nearly nothing when idle. Talk to it from Telegram while it works on a cloud VM you never SSH into yourself. It's not tied to your laptop.
## Quick Links[​](https://hermes-agent.nousresearch.com/docs#quick-links "Direct link to Quick Links")  
|   |   |  
| --- | --- |  
| 🚀 **[Installation](https://hermes-agent.nousresearch.com/docs/getting-started/installation)**  | Install in 60 seconds on Linux, macOS, WSL2, or native Windows (early beta)  |  
| 📖 **[Quickstart Tutorial](https://hermes-agent.nousresearch.com/docs/getting-started/quickstart)**  | Your first conversation and key features to try  |  
| 🗺️ **[Learning Path](https://hermes-agent.nousresearch.com/docs/getting-started/learning-path)**  | Find the right docs for your experience level  |  
| ⚙️ **[Configuration](https://hermes-agent.nousresearch.com/docs/user-guide/configuration)**  | Config file, providers, models, and options  |  
| 💬 **[Messaging Gateway](https://hermes-agent.nousresearch.com/docs/user-guide/messaging)**  | Set up Telegram, Discord, Slack, WhatsApp, Teams, or more  |  
| 🔧 **[Tools& Toolsets](https://hermes-agent.nousresearch.com/docs/user-guide/features/tools)**  | 60+ built-in tools and how to configure them  |  
| 🧠 **[Memory System](https://hermes-agent.nousresearch.com/docs/user-guide/features/memory)**  | Persistent memory that grows across sessions  |  
| 📚 **[Skills System](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills)**  | Procedural memory the agent creates and reuses  |  
| 🔌 **[MCP Integration](https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp)**  | Connect to MCP servers, filter their tools, and extend Hermes safely  |  
| 🧭 **[Use MCP with Hermes](https://hermes-agent.nousresearch.com/docs/guides/use-mcp-with-hermes)**  | Practical MCP setup patterns, examples, and tutorials  |  
| 🎙️ **[Voice Mode](https://hermes-agent.nousresearch.com/docs/user-guide/features/voice-mode)**  | Real-time voice interaction in CLI, Telegram, Discord, and Discord VC  |  
| 🗣️ **[Use Voice Mode with Hermes](https://hermes-agent.nousresearch.com/docs/guides/use-voice-mode-with-hermes)**  | Hands-on setup and usage patterns for Hermes voice workflows  |  
| 🎭 **[Personality& SOUL.md](https://hermes-agent.nousresearch.com/docs/user-guide/features/personality)**  | Define Hermes' default voice with a global SOUL.md  |  
| 📄 **[Context Files](https://hermes-agent.nousresearch.com/docs/user-guide/features/context-files)**  | Project context files that shape every conversation  |  
| 🔒 **[Security](https://hermes-agent.nousresearch.com/docs/user-guide/security)**  | Command approval, authorization, container isolation  |  
| 💡 **[Tips& Best Practices](https://hermes-agent.nousresearch.com/docs/guides/tips)**  | Quick wins to get the most out of Hermes  |  
| 🏗️ **[Architecture](https://hermes-agent.nousresearch.com/docs/developer-guide/architecture)**  | How it works under the hood  |  
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


> **补充来源**: [2026-05-29_Hermes-Agent进阶补充-会聊天到会干活.md](../01-收件箱/文章/2026-05-29_Hermes-Agent进阶补充-会聊天到会干活.md)

## 新增要点

- Hermes Agent 进阶补充：把 AI 助手从「会聊天」调成「会干活」
- - 建议至少三个：default（日常）、content（内容）、worker（执行）
- - 主助手负责判断，worker 负责执行
- - 不要一上来拆十几个，先从 2-3 个开始
- - **信息筛选型**：每天筛选值得看的内容（不要"全部总结"，要"只挑值得看的"）


> **补充来源**: [2026-05-29_Hermes-Agent-v0.15.0-The-Velocity-Release.md](../01-收件箱/文章/2026-05-29_Hermes-Agent-v0.15.0-The-Velocity-Release.md)

## 新增要点

- Hermes Agent v0.15.0 The Velocity Release — 速度革命
- - **代码重构**：run_agent.py 16000 行 → 3821 行（-76%），拆分为 14 个模块
- - **冷启动**：TUI 2.9s→0.8s（-72%），hermes --version 701ms→258ms（-63%）
- - **单工具调用**：415ms→220ms（-47%）
- - **会话搜索**：发现模式 90s→20ms（4500 倍提速），完全免费，纯本地 FTS5


> **补充来源**: [2026-05-29_Hermes-Agent进阶补充-会聊天到会干活.md](../01-收件箱/文章/2026-05-29_Hermes-Agent进阶补充-会聊天到会干活.md)

## 新增要点

- Hermes Agent 进阶补充：把 AI 助手从「会聊天」调成「会干活」
- - 建议至少三个：default（日常）、content（内容）、worker（执行）
- - 主助手负责判断，worker 负责执行
- - 不要一上来拆十几个，先从 2-3 个开始
- - **信息筛选型**：每天筛选值得看的内容（不要"全部总结"，要"只挑值得看的"）


> **补充来源**: [2026-05-29_Hermes-Agent-v0.15.0-The-Velocity-Release.md](../01-收件箱/文章/2026-05-29_Hermes-Agent-v0.15.0-The-Velocity-Release.md)

## 新增要点

- Hermes Agent v0.15.0 The Velocity Release — 速度革命
- - **代码重构**：run_agent.py 16000 行 → 3821 行（-76%），拆分为 14 个模块
- - **冷启动**：TUI 2.9s→0.8s（-72%），hermes --version 701ms→258ms（-63%）
- - **单工具调用**：415ms→220ms（-47%）
- - **会话搜索**：发现模式 90s→20ms（4500 倍提速），完全免费，纯本地 FTS5
