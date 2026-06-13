1|---
2|title: Hermes Agent
3|created: 2026-05-29
4|updated: 2026-06-13
5|tags: ["auto-capture", auto-compiled]
6|status: compiled
7|sources: [https://hermes-agent.nousresearch.com/docs]
8|source_url: https://hermes-agent.nousresearch.com/docs
9|---
10|
11|# Hermes Agent
12|
13|> 自动抓取自: [https://hermes-agent.nousresearch.com/docs](https://hermes-agent.nousresearch.com/docs)
14|
15|[Skip to main content](https://hermes-agent.nousresearch.com/docs#__docusaurus_skipToContent_fallback)
16|[![Hermes Agent](https://hermes-agent.nousresearch.com/docs/img/logo.png) **Hermes Agent**](https://hermes-agent.nousresearch.com/docs/)[Docs](https://hermes-agent.nousresearch.com/docs/user-stories)[Skills](https://hermes-agent.nousresearch.com/docs/skills)
17|[](https://hermes-agent.nousresearch.com/docs)
18|  * [English](https://hermes-agent.nousresearch.com/docs/)
19|  * [简体中文](https://hermes-agent.nousresearch.com/docs/zh-Hans/)
20|
21|
22|[Home](https://hermes-agent.nousresearch.com)[GitHub](https://github.com/NousResearch/hermes-agent)[Discord](https://discord.gg/NousResearch)
23|`ctrl``K`
24|  * [User Stories & Use Cases](https://hermes-agent.nousresearch.com/docs/user-stories)
25|  * [Getting Started](https://hermes-agent.nousresearch.com/docs)
26|  * [Using Hermes](https://hermes-agent.nousresearch.com/docs)
27|  * [Features](https://hermes-agent.nousresearch.com/docs)
28|  * [Messaging Platforms](https://hermes-agent.nousresearch.com/docs)
29|  * [Integrations](https://hermes-agent.nousresearch.com/docs)
30|  * [Guides & Tutorials](https://hermes-agent.nousresearch.com/docs)
31|  * [Developer Guide](https://hermes-agent.nousresearch.com/docs)
32|  * [Reference](https://hermes-agent.nousresearch.com/docs)
33|
34|
35|  * [](https://hermes-agent.nousresearch.com/docs/)
36|
37|
38|# Hermes Agent
39|The self-improving AI agent built by [Nous Research](https://nousresearch.com). The only agent with a built-in learning loop — it creates skills from experience, improves them during use, nudges itself to persist knowledge, and builds a deepening model of who you are across sessions.
40|[Get Started →](https://hermes-agent.nousresearch.com/docs/getting-started/installation)[View on GitHub](https://github.com/NousResearch/hermes-agent)
41|## Install[​](https://hermes-agent.nousresearch.com/docs#install "Direct link to Install")
42|**Linux / macOS / WSL2**
43|
44|```
45|curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash  
46|
47|```
48|
49|**Windows (native, PowerShell)** — _early beta,[details →](https://hermes-agent.nousresearch.com/docs/user-guide/windows-native)_
50|
51|```
52|iex (irm https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.ps1)  
53|
54|```
55|
56|**Android (Termux)** — same curl one-liner as Linux; the installer auto-detects Termux.
57|See the full **[Installation Guide](https://hermes-agent.nousresearch.com/docs/getting-started/installation)** for what the installer does, the per-user vs root layout, and Windows-specific notes.
58|After installing, run `hermes setup --portal` — one OAuth covers a model plus all four Tool Gateway tools (web search, image generation, TTS, browser). See [Nous Portal](https://hermes-agent.nousresearch.com/docs/integrations/nous-portal).
59|## What is Hermes Agent?[​](https://hermes-agent.nousresearch.com/docs#what-is-hermes-agent "Direct link to What is Hermes Agent?")
60|It's not a coding copilot tethered to an IDE or a chatbot wrapper around a single API. It's an **autonomous agent** that gets more capable the longer it runs. It lives wherever you put it — a $5 VPS, a GPU cluster, or serverless infrastructure (Daytona, Modal) that costs nearly nothing when idle. Talk to it from Telegram while it works on a cloud VM you never SSH into yourself. It's not tied to your laptop.
61|## Quick Links[​](https://hermes-agent.nousresearch.com/docs#quick-links "Direct link to Quick Links")  
62||   |   |  
63|| --- | --- |  
64|| 🚀 **[Installation](https://hermes-agent.nousresearch.com/docs/getting-started/installation)**  | Install in 60 seconds on Linux, macOS, WSL2, or native Windows (early beta)  |  
65|| 📖 **[Quickstart Tutorial](https://hermes-agent.nousresearch.com/docs/getting-started/quickstart)**  | Your first conversation and key features to try  |  
66|| 🗺️ **[Learning Path](https://hermes-agent.nousresearch.com/docs/getting-started/learning-path)**  | Find the right docs for your experience level  |  
67|| ⚙️ **[Configuration](https://hermes-agent.nousresearch.com/docs/user-guide/configuration)**  | Config file, providers, models, and options  |  
68|| 💬 **[Messaging Gateway](https://hermes-agent.nousresearch.com/docs/user-guide/messaging)**  | Set up Telegram, Discord, Slack, WhatsApp, Teams, or more  |  
69|| 🔧 **[Tools& Toolsets](https://hermes-agent.nousresearch.com/docs/user-guide/features/tools)**  | 60+ built-in tools and how to configure them  |  
70|| 🧠 **[Memory System](https://hermes-agent.nousresearch.com/docs/user-guide/features/memory)**  | Persistent memory that grows across sessions  |  
71|| 📚 **[Skills System](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills)**  | Procedural memory the agent creates and reuses  |  
72|| 🔌 **[MCP Integration](https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp)**  | Connect to MCP servers, filter their tools, and extend Hermes safely  |  
73|| 🧭 **[Use MCP with Hermes](https://hermes-agent.nousresearch.com/docs/guides/use-mcp-with-hermes)**  | Practical MCP setup patterns, examples, and tutorials  |  
74|| 🎙️ **[Voice Mode](https://hermes-agent.nousresearch.com/docs/user-guide/features/voice-mode)**  | Real-time voice interaction in CLI, Telegram, Discord, and Discord VC  |  
75|| 🗣️ **[Use Voice Mode with Hermes](https://hermes-agent.nousresearch.com/docs/guides/use-voice-mode-with-hermes)**  | Hands-on setup and usage patterns for Hermes voice workflows  |  
76|| 🎭 **[Personality& SOUL.md](https://hermes-agent.nousresearch.com/docs/user-guide/features/personality)**  | Define Hermes' default voice with a global SOUL.md  |  
77|| 📄 **[Context Files](https://hermes-agent.nousresearch.com/docs/user-guide/features/context-files)**  | Project context files that shape every conversation  |  
78|| 🔒 **[Security](https://hermes-agent.nousresearch.com/docs/user-guide/security)**  | Command approval, authorization, container isolation  |  
79|| 💡 **[Tips& Best Practices](https://hermes-agent.nousresearch.com/docs/guides/tips)**  | Quick wins to get the most out of Hermes  |  
80|| 🏗️ **[Architecture](https://hermes-agent.nousresearch.com/docs/developer-guide/architecture)**  | How it works under the hood  |  
81|| ❓ **[FAQ& Troubleshooting](https://hermes-agent.nousresearch.com/docs/reference/faq)**  | Common questions and solutions  |  
82|## Key Features[​](https://hermes-agent.nousresearch.com/docs#key-features "Direct link to Key Features")
83|  * **A closed learning loop** — Agent-curated memory with periodic nudges, autonomous skill creation, skill self-improvement during use, FTS5 cross-session recall with LLM summarization, and [Honcho](https://github.com/plastic-labs/honcho) dialectic user modeling
84|  * **Runs anywhere, not just your laptop** — 6 terminal backends: local, Docker, SSH, Daytona, Singularity, Modal. Daytona and Modal offer serverless persistence — your environment hibernates when idle, costing nearly nothing
85|  * **Lives where you do** — CLI, Telegram, Discord, Slack, WhatsApp, Signal, Matrix, Mattermost, Email, SMS, DingTalk, Feishu, WeCom, Weixin, QQ Bot, Yuanbao, BlueBubbles, Home Assistant, Microsoft Teams, Google Chat, and more — 20+ platforms from one gateway
86|  * **Built by model trainers** — Created by [Nous Research](https://nousresearch.com), the lab behind Hermes, Nomos, and Psyche. Works with [Nous Portal](https://portal.nousresearch.com), [OpenRouter](https://openrouter.ai), OpenAI, or any endpoint
87|  * **Scheduled automations** — Built-in cron with delivery to any platform
88|  * **Delegates & parallelizes** — Spawn isolated subagents for parallel workstreams. Programmatic Tool Calling via `execute_code` collapses multi-step pipelines into single inference calls
89|  * **Open standard skills** — Compatible with [agentskills.io](https://agentskills.io). Skills are portable, shareable, and community-contributed via the Skills Hub
90|  * **Full web control** — Search, extract, browse, vision, image generation, TTS — one subscription via [Nous Portal](https://hermes-agent.nousresearch.com/docs/integrations/nous-portal) bundles all of them
91|  * **MCP support** — Connect to any MCP server for extended tool capabilities
92|  * **Research-ready** — Batch processing, trajectory export, RL training with Atropos. Built by [Nous Research](https://nousresearch.com) — the lab behind Hermes, Nomos, and Psyche models
93|
94|
95|## For LLMs and coding agents[​](https://hermes-agent.nousresearch.com/docs#for-llms-and-coding-agents "Direct link to For LLMs and coding agents")
96|Machine-readable entry points to this documentation:
97|  * **[`/llms.txt`](https://hermes-agent.nousresearch.com/docs/assets/files/llms-bcf65f79b33e57e6c0cce5b9627945d4.txt)**— curated index of every doc page with short descriptions. ~17 KB, safe to load into an LLM context.
98|  * **[`/llms-full.txt`](https://hermes-agent.nousresearch.com/docs/assets/files/llms-full-00235826279c78cd53e3b34278392ee9.txt)**— every doc page concatenated into a single markdown file for one-shot ingestion. ~1.8 MB.
99|
100|
101|Both files also resolve at `/docs/llms.txt` and `/docs/llms-full.txt`. Generated fresh on every deploy.
102|[](https://github.com/NousResearch/hermes-agent/edit/main/website/docs/index.mdx)
103|Docs
104|  * [Getting Started](https://hermes-agent.nousresearch.com/docs/getting-started/quickstart)
105|  * [User Guide](https://hermes-agent.nousresearch.com/docs/user-guide/cli)
106|  * [Developer Guide](https://hermes-agent.nousresearch.com/docs/developer-guide/architecture)
107|  * [Reference](https://hermes-agent.nousresearch.com/docs/reference/cli-commands)
108|
109|
110|Community
111|  * [Discord](https://discord.gg/NousResearch)
112|  * [GitHub Discussions](https://github.com/NousResearch/hermes-agent/discussions)
113|  * [Skills Hub](https://agentskills.io)
114|
115|
116|More
117|  * [GitHub](https://github.com/NousResearch/hermes-agent)
118|  * [Nous Research](https://nousresearch.com)
119|
120|
121|Built by [Nous Research](https://nousresearch.com) · MIT License · 2026
122|
123|
124|> **补充来源**: [2026-06-13_Hermes_Agent.md](../01_inbox/articles/2026-06-13_Hermes_Agent.md)

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

> **补充来源**: [2026-05-29_Hermes-Agent进阶补充-会聊天到会干活.md](../01-收件箱/文章/2026-05-29_Hermes-Agent进阶补充-会聊天到会干活.md)
125|
126|## 新增要点
127|
128|- Hermes Agent 进阶补充：把 AI 助手从「会聊天」调成「会干活」
129|- - 建议至少三个：default（日常）、content（内容）、worker（执行）
130|- - 主助手负责判断，worker 负责执行
131|- - 不要一上来拆十几个，先从 2-3 个开始
132|- - **信息筛选型**：每天筛选值得看的内容（不要"全部总结"，要"只挑值得看的"）
133|
134|
135|> **补充来源**: [2026-05-29_Hermes-Agent-v0.15.0-The-Velocity-Release.md](../01-收件箱/文章/2026-05-29_Hermes-Agent-v0.15.0-The-Velocity-Release.md)
136|
137|## 新增要点
138|
139|- Hermes Agent v0.15.0 The Velocity Release — 速度革命
140|- - **代码重构**：run_agent.py 16000 行 → 3821 行（-76%），拆分为 14 个模块
141|- - **冷启动**：TUI 2.9s→0.8s（-72%），hermes --version 701ms→258ms（-63%）
142|- - **单工具调用**：415ms→220ms（-47%）
143|- - **会话搜索**：发现模式 90s→20ms（4500 倍提速），完全免费，纯本地 FTS5
144|
145|
146|> **补充来源**: [2026-05-29_Hermes-Agent进阶补充-会聊天到会干活.md](../01-收件箱/文章/2026-05-29_Hermes-Agent进阶补充-会聊天到会干活.md)
147|
148|## 新增要点
149|
150|- Hermes Agent 进阶补充：把 AI 助手从「会聊天」调成「会干活」
151|- - 建议至少三个：default（日常）、content（内容）、worker（执行）
152|- - 主助手负责判断，worker 负责执行
153|- - 不要一上来拆十几个，先从 2-3 个开始
154|- - **信息筛选型**：每天筛选值得看的内容（不要"全部总结"，要"只挑值得看的"）
155|
156|
157|> **补充来源**: [2026-05-29_Hermes-Agent-v0.15.0-The-Velocity-Release.md](../01-收件箱/文章/2026-05-29_Hermes-Agent-v0.15.0-The-Velocity-Release.md)
158|
159|## 新增要点
160|
161|- Hermes Agent v0.15.0 The Velocity Release — 速度革命
162|- - **代码重构**：run_agent.py 16000 行 → 3821 行（-76%），拆分为 14 个模块
163|- - **冷启动**：TUI 2.9s→0.8s（-72%），hermes --version 701ms→258ms（-63%）
164|- - **单工具调用**：415ms→220ms（-47%）
165|- - **会话搜索**：发现模式 90s→20ms（4500 倍提速），完全免费，纯本地 FTS5
166|