---
site: "https://hermes-agent.nousresearch.com/"
title: "Hermes Agent 官网首页"
fetched_at: "2026-06-29"
status: "success"
tags: [hermes, 官网, 概述, 功能, 安装]
---

# 知识点清单

## 1. 核心定位
- **标题**: Hermes Agent 是什么
- **摘要**: 由 Nous Research 构建的自我进化 AI 智能体，内置学习闭环——从经验创建技能、使用中自我改进、持久化知识、跨会话构建用户画像。可运行在 $5 VPS、GPU 集群或 serverless 基础设施上。
- **标签**: #hermes #core-concept #self-improving

## 2. 六大核心特性
- **标题**: 核心能力概览
- **摘要**: 
  1. **真实终端界面** — 完整 TUI，支持多行编辑、斜杠命令自动补全、对话历史、流式工具输出
  2. **无处不在** — Telegram、Discord、Slack、WhatsApp、Signal、CLI 统一网关，支持语音备忘录转录
  3. **闭环学习** — Agent 策展记忆+定期提醒、自动技能创建、技能自改进、FTS5 会话检索、Honcho 辩证用户建模
  4. **定时自动化** — 内置 cron 调度器，自然语言定义定时任务
  5. **任务委派与并行** — 隔离子 Agent 并行工作流，Python RPC 脚本零上下文损耗
  6. **任意环境运行** — 6 种终端后端（本地/Docker/SSH/Singularity/Modal/Daytona）
- **标签**: #hermes #features #architecture

## 3. 安装方式
- **标题**: 一键安装
- **摘要**: 
  - Linux/macOS/WSL2/Termux: `curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash`
  - Windows 原生 PowerShell: `iex (irm https://hermes-agent.nousresearch.com/install.ps1)`
  - Windows 原生安装使用 MinGit 作为便携式 Git Bash，完全隔离
  - Android/Termux 有专门的 `.[termux]` extra（完整 voice 依赖不可用）
- **标签**: #hermes #installation #windows #linux #termux

## 4. Nous Portal 订阅
- **标题**: 一站式 API 密钥方案
- **摘要**: Nous Portal 用一个订阅覆盖：300+ 模型、网络搜索（Firecrawl）、图片生成（FAL）、TTS（OpenAI）、云端浏览器（Browser Use）。`hermes setup --portal` 一键配置。
- **标签**: #hermes #portal #subscription #tool-gateway

## 5. CLI vs 消息平台快速参考
- **标题**: 双入口操作对比
- **摘要**: CLI 用 `hermes` 启动 TUI；消息平台通过 `hermes gateway setup` + `hermes gateway start`。共享斜杠命令：`/new`、`/model`、`/compress`、`/skills`、`/retry` 等。
- **标签**: #hermes #cli #messaging #commands

## 6. 从 OpenClaw 迁移
- **标题**: 迁移工具
- **摘要**: `hermes claw migrate` 可导入 OpenClaw 的 SOUL.md、记忆、技能、命令白名单、消息设置、API 密钥等。支持 `--dry-run` 预览。
- **标签**: #hermes #migration #openclaw

## 7. 社区生态
- **标题**: 社区与扩展
- **摘要**: Discord、Skills Hub (agentskills.io)、GitHub Issues。社区贡献：computer-use-linux（Linux 桌面控制 MCP 服务器）、HermesClaw（微信桥接）。
- **标签**: #hermes #community #ecosystem
