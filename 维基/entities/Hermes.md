---
title: Hermes
type: entity
tags: [llmwiki, hermes-agent]
sources: ["01-收件箱/文章/2026_05_27_agent-browser部署指南.md", "01-收件箱/文章/2026_05_27_HermesAgent操控电脑指南.md", "01-收件箱/文章/2026_05_26_Hermes Skills效率翻倍.md", "01-收件箱/文章/2026_05_27_HermesAgent工具详解.md", "01-收件箱/文章/测试会议转写---2026-05-24.md", "01-收件箱/文章/2026_05_27_HermesAgent浏览器自动化插件安装.md", "01-收件箱/文章/2026_05_26_Hermes OpenHands升级评估.md", "01-收件箱/文章/2026_05_27_HermesAgent生态全攻略.md", "01-收件箱/文章/2026_05_26_Hermes Agent价值提升用法.md", "01-收件箱/文章/2026_05_23_RAG技术简析.md", "01-收件箱/文章/2026_05_26_Brainstorming Skill测评.md", "articles/15个被忽略的Agent高级能力-王二AI进化论.md", "01-收件箱/自动学习/01-官网_hermes-agent.nousresearch.com.md", "01-收件箱/自动学习/02-官方文档_hermes-agent.nousresearch.com_docs.md", "01-收件箱/自动学习/03-GitHub_NousResearch_hermes-agent.md", "01-收件箱/自动学习/04-中文文档_hermes.xaapi.ai.md", "01-收件箱/自动学习/05-中文社区FAQ_hermesagent.org.cn.md", "01-收件箱/自动学习/06-中文快速入门_hermesagent.org.cn_quickstart.md"]
created: 2026-06-01
updated: 2026-06-22
---

# Hermes

## 概览

Hermes Agent（简称 Hermes）是由 Nous Research 打造的自改进 AI 代理框架——唯一内置学习闭环的代理。开源免费（MIT License）。GitHub 199k Stars / 35.3k Forks / 12,483 Commits。支持 20+ 消息平台和 6 种终端后端。

## 关键信息

### 核心定位
- **名称**: Hermes Agent — 自改进 AI 代理（The self-improving AI agent）
- **开发商**: Nous Research（Hermes、Nomos、Psyche 模型背后的实验室）
- **标语**: 唯一内置学习闭环的代理
- **GitHub**: https://github.com/NousResearch/hermes-agent

### 六大核心特性
1. **无处不在** — Telegram、Discord、Slack、WhatsApp、Signal、飞书、钉钉、微信、QQ 等 20+ 平台，单一网关进程
2. **持久记忆** — FTS5 跨会话检索 + LLM 摘要 + Honcho 辩证用户建模，学习项目信息、自动生成技能
3. **定时自动化** — 内置 cron，自然语言调度（日报、备份、简报），通过网关无人值守运行
4. **任务委派** — 隔离的子代理，独立会话、终端和 Python RPC 脚本
5. **网页浏览** — 网页搜索、浏览器自动化、视觉、图片生成、TTS、多模型推理
6. **实验沙箱** — 本地/Docker/SSH/Singularity/Modal/Daytona（6 种后端），容器加固和命名空间隔离

### 关键数据（2026-06-22）
- GitHub Stars: 199k（从 ~28k 爆发式增长）
- GitHub Forks: 35.3k
- GitHub Commits: 12,483
- 许可证: MIT
- 内置工具: 47 个（中文文档站数据）
- 消息平台: 20+（含中国特有平台）

### 中文生态
- 国内镜像站: hermesagent.org.cn（加速安装包）
- 中文文档镜像: hermes.xaapi.ai
- 中文 MCP Server: mcp.hermesagent.org.cn（Streamable HTTP）
- 推荐辅助工具: WorkBuddy（微信扫码即用）
- 社区微信群支持
- 中文提供商支持: 智谱 GLM、阿里 Qwen、DeepSeek、MiniMax 中国区、Kimi/Moonshot

### 技术架构
- **学习闭环**: 记忆 + 定期自我提醒 → 自动创建技能 → 技能自改进 → 用户画像积累
- **Tool Gateway**: Nous Portal 一个订阅覆盖网页搜索、图片生成、TTS、云浏览器
- **MCP 支持**: 连接任意 MCP 服务器扩展工具能力（客户端+服务器双模式）
- **开放标准**: 兼容 agentskills.io，技能通过 Skills Hub 分享
- **机器可读文档**: llms.txt（约17KB）/ llms-full.txt（约1.8MB）
- **6 种终端后端**: 本地、Docker、SSH、Daytona、Singularity、Modal

### 部署方式
- Linux/macOS/WSL2/Termux: `curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash`
- Windows 原生 PowerShell: `iex (irm https://hermes-agent.nousresearch.com/install.ps1)`
- 中文镜像安装: `curl -fsSL https://res1.hermesagent.org.cn/install.sh | bash`
- Hermes Desktop: 官方下载安装器（含 CLI + 桌面应用）
- 最低成本: $5 VPS 或 Serverless（Modal/Daytona）空闲时几乎零成本

## 相关概念

[[技能系统]]、[[智能体框架]]、[[配置]]、[[部署]]、[[自动化]]、[[浏览器自动化]]

## 来源

- [[Hermes Agent官网核心信息]]
- [[Hermes Agent官方文档导航]]
- [[Hermes Agent GitHub仓库统计]]
- [[Hermes Agent中文文档站]]
- [[Hermes Agent中文社区FAQ]]
- [[Hermes Agent中文快速入门]]
- 及 12 个历史来源
