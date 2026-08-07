---
source: https://hermes-agent.nousresearch.com/
date: 2026-06-22
tier: Tier 1
tags: [hermes-agent, nous-research, 官网, 官方]
---

# Hermes Agent 官网 — 结构化知识点

## 1. 核心定位
- **名称**: Hermes Agent — 自改进 AI 代理（The self-improving AI agent）
- **开发商**: Nous Research（Hermes、Nomos、Psyche 模型背后的实验室）
- **标语**: 唯一内置学习闭环的代理

## 2. 六大核心特性
1. **无处不在** — Telegram、Discord、Slack、WhatsApp、Signal、CLI 等 20+ 平台，单一网关进程
2. **持久记忆** — 学习项目信息、自动生成技能、跨会话不遗忘
3. **定时自动化** — 自然语言调度：日报、备份、简报，通过网关无人值守运行
4. **任务委派** — 隔离的子代理，独立会话、终端和 Python RPC 脚本
5. **网页浏览** — 网页搜索、浏览器自动化、视觉、图片生成、TTS、多模型推理
6. **实验沙箱** — 5 种后端：本地、Docker、SSH、Singularity、Modal，容器加固和命名空间隔离

## 3. 部署方式
- **安装命令**: `curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash`
- **Windows**: `iex (irm https://hermes-agent.nousresearch.com/install.ps1)`
- **后端支持**: 本地、Docker、SSH、Daytona、Singularity、Modal（6 种）
- **最低成本**: $5 VPS 或 Serverless（Modal/Daytona）空闲时几乎零成本

## 4. 机器可读文档入口
- `/llms.txt` — 约 17KB，所有文档页的精选索引
- `/llms-full.txt` — 约 1.8MB，所有文档合并为一个 Markdown 文件
- 每次部署时重新生成

## 5. 关键架构特性
- **学习闭环**: Agent 管理记忆 + 定期自我提醒 → 复杂任务后自动创建技能 → 技能在使用中自我改进 → FTS5 跨会话检索 + LLM 摘要 → Honcho 辩证式用户建模
- **开放标准**: 兼容 agentskills.io，技能通过 Skills Hub 分享
- **MCP 支持**: 连接任意 MCP 服务器扩展工具能力
