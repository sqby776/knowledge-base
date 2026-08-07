---
title: Hermes Agent v0.15.0 The Velocity Release
source: 微信公众号-布鲁斯AI
url: https://mp.weixin.qq.com/s/upOzw2FtUVWsslcgi9nHPA
date: 2026-05-29
status: active
type: article
tags: [Hermes, v0.15.0, AI-Agent, 发布, auto-compiled]
archived: 2026-06-01
confidence: medium
---



# Hermes Agent v0.15.0 The Velocity Release — 速度革命

Nous Research 于 **2026 年 5 月 28 日** 发布。1302 次提交、747 个合并 PR、321 位社区贡献者。

## 核心性能

- **代码重构**：run_agent.py 16000 行 → 3821 行（-76%），拆分为 14 个模块
- **冷启动**：TUI 2.9s→0.8s（-72%），hermes --version 701ms→258ms（-63%）
- **单工具调用**：415ms→220ms（-47%）
- **会话搜索**：发现模式 90s→20ms（4500 倍提速），完全免费，纯本地 FTS5

## Kanban 多 Agent 平台

- 自动任务分解：一句话拆成子任务树，自动分配模型
- Swarm 集群：`hermes kanban swarm` 一键创建多 Agent 拓扑
- Per-task 模型覆盖，工作树隔离，定时任务，故障恢复

## 安全

- Promptware 防御：内置 15 种攻击模式库、内存扫描、工具结果隔离
- Bitwarden Secrets Manager：一个 Token 管所有 API 密钥
- 控制平面文件保护，供应链审计（hermes audit）

## 技能生态

- 技能 Bundles：一条命令切换工作流（/writing-day、/coding-day）
- 新技能：code-wiki、openhands、web-pentest
- Nous 认证 MCP 目录：`hermes mcp` 一键安装

## 工具升级

- 图像生成：Krea 2 Medium/Large
- 消息平台：ntfy（第 23 个，无需账号）
- TUI 多会话管理，Docker s6-overlay，Node 22 LTS