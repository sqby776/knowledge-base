---
title: Hermes Agent 官方文档索引
source: https://hermes-agent.nousresearch.com/docs
fetched: 2026-07-13
tier: Tier 1 (官方文档)
tags: [hermes-agent, 文档, 索引, 架构, auto-compiled]
---

# Hermes Agent 官方文档知识点

## 文档结构（20+ 章节）

| 章节 | 覆盖内容 |
|------|---------|
| Installation | 60 秒安装指南（Linux/macOS/WSL2/Windows/Android） |
| Quickstart Tutorial | 首次对话 + 关键特性试用 |
| Learning Path | 按经验级别推荐文档 |
| Configuration | 配置文件、Provider、模型、选项 |
| Messaging Gateway | Telegram, Discord, Slack, WhatsApp, Teams 等配置 |
| Tools & Toolsets | 60+ 内置工具及配置 |
| Memory System | 跨会话持久记忆 |
| Skills System | Agent 自创建和复用的程序性记忆 |
| MCP Integration | 连接 MCP 服务器、工具过滤 |
| Voice Mode | CLI/Telegram/Discord 实时语音交互 |
| Personality & SOUL.md | 定义 Agent 默认人格 |
| Context Files | 项目上下文文件 |
| Security | 命令审批、授权、容器隔离 |
| Architecture | 底层架构 |
| FAQ & Troubleshooting | 常见问题和解决方案 |

## 关键架构特性
- **自主学习闭环**：Agent 管理的记忆 + 定时提示 + 自主技能创建 + 技能自改进
- **FTS5 会话搜索 + LLM 摘要** 实现跨会话召回
- **6 个终端后端**：local, Docker, SSH, Daytona, Singularity, Modal
- **Daytona 和 Modal** 提供无服务器持久化，空闲近乎零成本
- **20+ 消息平台**：CLI, Telegram, Discord, Slack, WhatsApp, Signal, Matrix, Mattermost, Email, SMS, DingTalk, Feishu, WeCom, Weixin, QQ Bot 等
- **由模型训练者打造**：Nous Research（Hermes, Nomos, Psyche 模型）

## 机器可读入口
- `/llms.txt` — 所有文档页面的精选索引（~17KB）
- `/llms-full.txt` — 所有文档拼接为单一 Markdown 文件（~1.8MB）