---
site: "http://hermes-agent.nousresearch.com/docs"
title: "Hermes Agent 官方文档入口"
fetched_at: "2026-06-29"
status: "success"
tags: [hermes, 文档, 快速入门, 配置, 网关, 工具, 记忆, 技能, MCP]
---

# 知识点清单

## 1. 文档结构概览
- **标题**: 文档目录体系
- **摘要**: 官方文档涵盖：快速入门、CLI 使用、配置、消息网关、安全、工具与工具集、技能系统、记忆系统、MCP 集成、Cron 调度、上下文文件、架构、贡献指南、CLI 参考、环境变量参考。
- **标签**: #hermes #documentation #structure

## 2. 关键功能模块
- **标题**: 文档重点模块速览
- **摘要**: 
  - **安装**: 60 秒快速安装，支持 6 种终端后端
  - **配置**: 配置文件、提供商、模型、所有选项
  - **消息网关**: Telegram、Discord、Slack、WhatsApp、Signal、Home Assistant 等 20+ 平台
  - **工具**: 60+ 内置工具，工具集系统
  - **记忆**: 持久化记忆，用户档案，最佳实践
  - **技能**: 程序化记忆，Skills Hub，创建技能
  - **MCP**: 连接任意 MCP 服务器扩展能力
  - **语音模式**: 实时语音交互 CLI/Telegram/Discord
  - **安全**: 命令审批，DM 配对，容器隔离
- **标签**: #hermes #modules #features

## 3. 学习路径
- **标题**: 按经验级别推荐文档
- **摘要**: 文档提供按经验级别（新手/中级/高级/开发者）的学习路径引导。
- **标签**: #hermes #learning-path

## 4. LLM 入口文件
- **标题**: 机器可读文档入口
- **摘要**: 提供 `/llms.txt`（~17KB，文档索引）和 `/llms-full.txt`（~1.8MB，完整文档拼接），每次部署自动生成，适合 LLM 一次性摄入。
- **标签**: #hermes #llms.txt #LLM

## 5. 关键特性清单
- **标题**: 核心技术特性
- **摘要**: 
  - 闭环学习：Agent 策展记忆 + 定期提醒 + 自动技能创建 + 技能自改进 + FTS5 跨会话检索
  - 任意环境运行：6 种终端后端，Daytona/Modal 无服务器持久化
  - 全平台覆盖：20+ 消息平台
  - 由模型训练专家 Nous Research 构建
  - 定时自动化：内置 cron，可投递到任意平台
  - 任务委派与并行：隔离子 Agent，`execute_code` 程序化工具调用
  - 开放标准技能：兼容 agentskills.io
  - MCP 支持：双向（客户端+服务器）
- **标签**: #hermes #features #highlights
