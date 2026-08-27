---
title: Hermes Agent
created: 2026-07-08
updated: 2026-08-21
tags: [knowledge-base, hermes-agent, ai-agent]
status: active
sources: [https://hermes-agent.nousresearch.com/docs]
---

# Hermes Agent

> 自动抓取自: [Hermes Agent 官方文档](https://hermes-agent.nousresearch.com/docs)，2026-07-28 更新

## What is Hermes Agent?

It's not a coding copilot tethered to an IDE or a chatbot wrapper around a single API. It's an **autonomous agent** that gets more capable the longer it runs. It lives wherever you put it — a $5 VPS, a GPU cluster, or serverless infrastructure (Daytona, Modal) that costs nearly nothing when idle. Talk to it from Telegram while it works on a cloud VM you never SSH into yourself. It's not tied to your laptop.

## 安装

### Windows or macOS

下载 Hermes Desktop 安装器，图形化安装向导。

### Without Hermes Desktop

#### Linux / macOS / WSL2 / Android (Termux)

```bash
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
```

#### Windows (native)

```powershell
iex (irm https://hermes-agent.nousresearch.com/install.ps1)
```

安装后运行 `hermes setup --portal`，一次 OAuth 覆盖模型 + 四个工具网关（web搜索、图片生成、TTS、浏览器）。详见 [Nous Portal](https://portal.nousresearch.com)。

## 关键功能

- **闭环学习** — Agent 策展记忆（定期 Nudge）、自主 Skill 创建、使用中自优化 Skill、FTS5 跨会话召回 + LLM 摘要、[Honcho](https://github.com/plastic-labs/honcho) 辩证用户建模
- **Curator 技能维护** — 后台自动维护 Agent 创建的 Skill：使用追踪、过时检测、归档、LLM 驱动的审查
- **随处运行** — 6 种终端后端：local、Docker、SSH、Daytona、Singularity、Modal。Daytona 和 Modal 支持 Serverless 持久化——环境空闲时休眠，几乎零成本
- **跨平台通信** — CLI + 20+ 通讯平台（Telegram、Discord、Slack、WhatsApp、Signal、Matrix、Mattermost、Email、SMS、钉钉、飞书、企业微信、微信、QQ Bot、元宝、BlueBubbles、Home Assistant、Microsoft Teams、Google Chat 等）
- **自建模型实验室** — 由 [Nous Research](https://nousresearch.com)（Hermes/Nomos/Psyche 模型系列）出品，支持 [Nous Portal](https://portal.nousresearch.com)、OpenRouter、OpenAI 或任意端点
- **定时自动化** — 内置 Cron，可投递到任意平台；Kanban 多 Agent 协同（SQLite-backed 任务板）、Persistent Goals（持续目标跨轮次执行）、Hooks（生命周期钩子）
- **子代理并行** — delegate_task 隔离子任务并行工作流，execute_code 批量管道将多步流程折叠为单次推理调用；批处理支持大规模轨迹生成
- **开源 Skill 标准** — 兼容 [agentskills.io](https://agentskills.io)，社区贡献，可移植、可分享
- **Web 全栈** — 搜索、提取、浏览、视觉、图片生成、TTS，通过 Nous Portal 一站式订阅
- **MCP 支持** — 连接任意 MCP 服务器扩展工具能力；ACP（Agent Context Protocol）支持在 VS Code/Zed/JetBrains 等编辑器中嵌入 Agent
- **API Server** — 将 Hermes 暴露为 OpenAI 兼容 API，任意前端可接入
- **Provider 路由与回退** — 支持 Provider Routing、Fallback Providers、Credential Pools 多级容错
- **Memory Providers** — 外部记忆提供者插件：Honcho、OpenViking、Mem0、Hindsight、Holographic、RetainDB、ByteRover、Supermemory
- **Context References** — 内联 @-语法，可直接在消息中附加文件、文件夹、git diff、URL
- **Built-in Plugins** — 随 Hermes 内置的自动运行插件（disk-cleanup 等）
- **Computer Use** — 后台桌面控制 Linux 桌面，不抢占鼠标/焦点，与用户共桌协作
- **Mixture of Agents (MoA)** — 多模型混合推理，配置化提升输出质量
- **Secrets 管理** — Bitwarden / 1Password / 命令式多种密钥源注入
- **Egress proxy** — 出站代理与凭据注入代理（iron-proxy）
- **Import from Other Agents** — 一条命令导入 Claude Code (~/.claude) / Codex CLI (~/.codex) 配置
- **Profile Distributions** — 将整个 Agent（配置/技能/记忆）打包分享；多网关并行、桌面多连接
- **Pets (Petdex)** — 桌面端可选桌宠（petdex mascots），社区图标包
- **LSP 语义诊断** — 编辑器级语义诊断（Semantic Diagnostics）
- **Deliverable Mode** — 聊天内交付物（Artifacts in Chat）
- **Document Extraction** — 文档提取；Tool Search 工具搜索；Web Dashboard 与扩展点
- **Recurring Loops** — 周期性循环任务；Session Heartbeats 会话心跳
- **Wake Word** — 语音唤醒词免提控制（v0.20.0 起）
- **新消息平台** — Buzz、Open WebUI、SimpleX Chat、Teams Meetings、WeCom Callback、WhatsApp Business (Cloud API)
- **Research-ready** — 批处理、轨迹导出、RL 训练（Atropos）

## 快速链接

| 功能 | 链接 |
|:-----|:-----|
| 🚀 安装 | 60 秒完成 Linux/macOS/WSL2/Windows/Android 安装 |
| 📖 快速开始 | 首次对话与关键功能体验 |
| 🗺️ 学习路径 | 按经验水平选择合适的文档 |
| ⚙️ 配置 | 配置文件、Provider、模型、选项 |
| 💬 消息网关 | 设置 Telegram/Discord/Slack/WhatsApp/Teams 等 |
|| 🔧 工具系统 | 60+ 内置工具与配置方式 |
|| 🧠 记忆系统 | 跨会话持续增长的记忆 |
|| 🧠 Extended Memory | 外部记忆提供者插件（Honcho/OpenViking/Mem0 等） |
|| 📚 Skills 系统 | Agent 创建和复用的程序性记忆 |
|| 🔌 MCP 集成 | 连接 MCP 服务器、过滤工具、安全扩展 |
|| 🔌 ACP 集成 | 在 VS Code/Zed/JetBrains 中使用 Agent |
|| 🎙️ 语音模式 | 实时语音交互（CLI/Telegram/Discord/Discord VC） |
|| 🎭 个性 & SOUL.md | 用全局 SOUL.md 定义 Hermes 默认语气 |
|| 📄 上下文文件 | 项目上下文文件塑造每次对话 |
|| 📎 Context References | 内联 @-语法附加文件/文件夹/git diff |
|| 🔒 安全 | 命令审批、授权、容器隔离 |
|| 💡 技巧 & 最佳实践 | 快速提升效率的实用建议 |
|| 🏗️ 架构 | 底层工作原理 |
|| ❓ FAQ & 故障排查 | 常见问题与解决方案 |
|| 🌐 API Server | OpenAI 兼容 API 暴露 |
|| 📋 Kanban | SQLite 多 Agent 任务板 |
|| 🎯 Persistent Goals | 持续目标跨轮次执行 |
|| 🔗 Hooks | 生命周期钩子 |
|| 🖥️ Browser/Vision/ImageGen | 浏览器自动化、视觉、图片生成 |
|| 🖥️ Computer Use | 后台桌面控制，不抢焦点 | 
|| 🧪 Mixture of Agents | 多模型混合推理 | 
|| 🔐 Secrets | Bitwarden/1Password 密钥注入 | 
|| 🌐 Egress proxy | 出站代理与凭据注入 | 
|| 📦 Profile Distributions | 打包分享整个 Agent | 
|| 🐾 Pets (Petdex) | 桌面桌宠 | 
|| ⚡ LSP | 语义诊断 | 
|| 📦 Deliverable Mode | 聊天内交付物 | 
|| 🔁 Recurring Loops | 周期性循环任务 | 

## 面向 LLM 和编程 Agent 的入口

机器可读的文档入口：

- **[`/llms.txt`](/docs/assets/files/llms-9e6ee453dd14f35da4a4a1e0200447d2.txt)** — 每个文档页面的精选索引，含简短描述。~17 KB，适合加载到 LLM 上下文。
- [ **`/llms-full.txt`](/docs/assets/files/llms-full-495d5fd9a2724dd4c6154c5e1a4c9c01.txt)** — ~1.8 MB。

两个文件也可通过 `/docs/llms.txt` 和 `/docs/llms-full.txt` 访问。每次部署时重新生成。

## 来源

- 原始文档: https://hermes-agent.nousresearch.com/docs
- GitHub: https://github.com/NousResearch/hermes-agent

---

*最后更新：2026-08-21（文档站结构性更新，30+ 新页面，详见 changelog）*

> **2026-07-29 例行捕获**
> 内容无变化，已归档存档。实体笔记无需更新。
>
> **2026-07-28 结构性更新**
> llms.txt hash 自 19 天稳定后首次变更：`96828202...` → `8c526336...`
> llms-full.txt hash: `52d2365a...` → `678d61cf...`
> 新增文档页面 20+ 个（Curator、Memory Providers、Context References、Built-in Plugins、Kanban、Persistent Goals、Hooks、Batch Processing、Browser/Vision/ImageGen/TTS 独立页、ACP、API Server、Provider Routing、Fallback Providers、Credential Pools、Profile Commands、Tools/Toolsets Reference、MCP Config Reference、Model Catalog、Skills Catalogs 等）
> 实体笔记已同步更新关键功能列表和快速链接表
>
> **2026-07-28 第3轮捕获（下午）**
> llms-full.txt hash: `25649c0e...` → `f20bdddc...`（当日第3次部署，无结构性变化）
> llms.txt hash: `96828202...` 保持稳定（第 19 天）
>
> **2026-07-22 第3轮捕获（20:00）**
> llms-full.txt hash: `c3087383...` → `9780f652...`（当日第3次部署，无结构性变化）
> llms.txt hash: `96828202...` 保持稳定（第 14 天）
>
> **2026-07-22 第2轮捕获**
> llms-full.txt hash: `936a4a50...` → `c3087383...`（当日第2次部署，无结构性变化）
> llms.txt hash: `96828202...` 保持稳定（第 14 天）
>
> **2026-07-22 第1轮捕获**
> llms-full.txt hash: `54f32431...` → `936a4a50...`（当日部署，无结构性变化）
> llms.txt hash: `96828202...` 保持稳定（第 14 天）
>
> **2026-07-21 20:00 第2轮捕获**
> llms-full.txt hash: `229f3a50...` → `54f32431...`（当日第2次部署，无结构性变化）
> llms.txt hash: `96828202...` 保持稳定（第 13 天）
>
> **2026-07-21 07:00 例行捕获**
> llms-full.txt hash: `dcf98e29...` → `229f3a50...`（当日部署，无结构性变化）
> llms.txt hash: `96828202...` 保持稳定（第 13 天）
>
> **2026-07-20 20:00 第3轮捕获**
> llms-full.txt hash: `3c60cae2...` → `dcf98e29...`（当日第3次部署，无结构性变化）
> llms.txt hash: `96828202...` 保持稳定（第 12 天）
>
> **2026-07-20 14:00 第2轮捕获**
> llms-full.txt hash: `6252dac2...` → `3c60cae2...`（当日第2次部署，无结构性变化）
> llms.txt hash: `96828202...` 保持稳定（第 12 天）
>
> **2026-07-20 07:00 例行捕获**
> llms-full.txt hash: `bb8831c1...` → `6252dac2...`（当日部署，无结构性变化）
> llms.txt hash: `96828202...` 保持稳定（第 12 天）
>
> **2026-07-19 第3轮捕获（20:00）**
> llms-full.txt hash: `225ba2ea...` → `bb8831c1...`（当日第3次部署，无结构性变化）
> llms.txt hash: `96828202...` 保持稳定（第 11 天）
>
> **2026-07-16 13:04→16:00 双轮捕获**
> llms-full.txt hash: `9c18cca7...` → `34a78544...`（当日第二次变更，例行部署）
> llms.txt hash: `96828202...` 保持稳定（第 7 天）
>
> **2026-07-18 第1轮捕获（上午）**
> llms-full.txt hash: `34a78544...` → `d76867fb...`（例行部署，无结构性变化）
> llms.txt hash: `96828202...` 保持稳定（第 9 天）
>
> **2026-07-18 第2轮捕获（下午）**
> llms-full.txt hash: `d76867fb...` → `f0567943...`（当日第2次部署，无结构性变化）
> llms.txt hash: `96828202...` 保持稳定（第 9 天）
>
> **2026-07-25 第2轮捕获（20:00）**
> llms-full.txt hash: `7e76a20c...` → `f47f48dc...`（当日第2次部署，无结构性变化）
> llms.txt hash: `96828202...` 保持稳定（第 17 天）
>
> **2026-07-25 第1轮捕获**
> llms-full.txt hash: `32445adb...` → `7e76a20c...`（当日部署，无结构性变化）
> llms.txt hash: `96828202...` 保持稳定（第 17 天）
>
> **2026-07-24 第2轮捕获**
> llms-full.txt hash: `3fc68a2c...` → `32445adb...`（当日第2次部署，无结构性变化）
> llms.txt hash: `96828202...` 保持稳定（第 16 天）
>
> **2026-07-24 第1轮捕获**
> llms-full.txt hash: `1c6beb4a...` → `3fc68a2c...`（当日部署，无结构性变化）
> llms.txt hash: `96828202...` 保持稳定（第 16 天）
>
> **2026-07-23 例行捕获**
> llms-full.txt hash: `9780f652...` → `1c6beb4a...`（当日部署，无结构性变化）
> llms.txt hash: `96828202...` 保持稳定（第 15 天）

> **2026-07-29 第2轮捕获**
> llms.txt hash: `faaf9398...` (从上一轮的 `8c526336...` 变更)
> llms-full.txt hash: 未检测到显著变化
>
> **2026-07-30 例行捕获**
> llms.txt hash: `faaf9398...` 保持稳定
> llms-full.txt hash: `07bdf65d...` (从 `d4be4eec...` 变更，例行部署，无结构性变化)
>
================================================================================

> **2026-07-31 例行捕获**
> llms.txt hash: `faaf9398...` 保持稳定
> llms-full.txt hash: `3f7f7630...` (从 `07bdf65d...` 变更，例行部署，无结构性变化)

> **2026-08-03 v0.20.0 Herald Release（结构性版本更新）**
> 版本：v0.20.0 (v2026.8.3)，v0.17.0 → v0.20.0（跨 3 个版本）
> 规模：~3,650 commits · ~1,400 PRs · ~1,200 issues closed · 650+ contributors；GitHub 228k stars
> 核心亮点：实时语音对话（barge-in 打断）、唤醒词免提控制、全平台语音、grounded-citations 带引证深度研究、出站 Webhooks (HMAC)、A2A v1.0 协议、桌面应用平台化、CLI 新命令（`!`/`/init`/`/diff`/`/context`/`/focus`）、工具自恢复
> 新增文档页面 15+：Checkpoints & Rollback、Nix Setup、Git Worktrees、TUI (Ink)、Voice Mode、TTS、ACP、API Server、Batch Processing、Kanban、Goals、Hooks、Context References、Built-in Plugins
> 新增消息平台：LINE、Raft、Webhooks、Photon；新增中文文档 /docs/zh-Hans/
> 完整详情见实体笔记 `Hermes_Agent_v0200_Herald_Release.md`
> **2026-08-17 第3轮捕获（urllib 直连版）**
> ⚠️ llms.txt 路径迁移：根路径 → `/docs/assets/files/llms-<hash>.txt`（llms.txt hash `faaf9398...` 稳定；llms-full 更新为 `9595dc2b...`，3.78MB，含 8 月文档变化）
> 版本三连发：v0.20.0 Herald（8-03）→ v0.20.1（8-13）→ v0.20.2（8-16；桌面多网关 Connections、MCP 健康检查、LiteLLM Claude prompt caching、cron 加固）
> 官方中文文档上线 `/docs/zh-Hans/`；Windows 原生安装（PowerShell 早期测试版）；hermes.xaapi.ai 疑似下线已移除出站点清单
> GitHub 231,687 ⭐；最近提交主线：MCP sanitization / tool-result annotations（scout-slate 波次）
> 本地 Hermes v0.20.1 → 建议 hermes update 至 v0.20.2

> **2026-08-21 结构性更新（08-20 捕获，前轮漏判已补录）**
> ⚠️ llms.txt + llms-full.txt 双 hash 变更：
>   - llms.txt: `faaf9398...` → `9e6ee453...`（页面索引变更 = 结构性信号）
>   - llms-full.txt: `9595dc2b...` → `495d5fd9...`，体积 **3.78MB → 1.8MB**（文档重新生成）
> 新增文档页面 30+：Computer Use、Mixture of Agents、Pets (Petdex)、Secrets（Bitwarden/1Password/Command）、Egress proxy / iron-proxy、Import from Other Agents、Managed Scope、Connecting Desktop to Many Instances、Running Many Gateways at Once、Profile Distributions、Codex App-Server Runtime、Deliverable Mode、Document Extraction、Extending the Dashboard、Session Heartbeats、Kanban worker lanes、Recurring Loops、LSP、Skins & Themes、Spotify、Subscription Proxy、Nous Tool Gateway、Tool Search、Wake Word、Web Dashboard、Web Search & Extract、X (Twitter) Search、TUI (Ink)、Desktop App 独立页、Windows Native/WSL2 指南、Which File Does What
> 新消息平台页面：Buzz、Open WebUI、SimpleX Chat、Teams Meetings、WeCom Callback、WhatsApp Business (Cloud API)、MsGraph Webhook
> GitHub 231,687 → **233,627 ⭐**（最近提交 2026-08-21，主线 MCP sanitization 波次继续）
> 实体笔记已同步：关键功能 +12 项、快速链接 +9 行、body hash 引用更新
> 📌 07:07 维护轮误判此捕获为「无 hash 变化」，本 13:02 轮经在线验证补齐
