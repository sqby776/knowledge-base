---
title: Hermes Agent v0.15.0 Velocity Release
created: 2026-05-30
updated: 2026-05-30
tags: ["hermes", "release", "v0.15.0", "performance"]
status: archived
sources: [https://mp.weixin.qq.com/s/upOzw2FtUVWsslcgi9nHPA]
trust_score: 0.17
confidence: low
---
# Hermes Agent v0.15.0 — Velocity Release（速度革命）

> 来源：Nous Research 2026 年 5 月 28 日发布
> 社区贡献：1302 次提交、747 个合并 PR、321 位贡献者

## 核心性能提升

| 指标 | 优化前 | 优化后 | 提升 |
|:-----|:-----|:-----|:-----|
| **代码行数** | 16000 行 | 3821 行 | -76% |
| **TUI 冷启动** | 2.9s | 0.8s | -72% |
| **hermes --version** | 701ms | 258ms | -63% |
| **单工具调用** | 415ms | 220ms | -47% |
| **会话搜索** | 90s | 20ms | 4500 倍 |

## 代码重构

- `run_agent.py` 从 16000 行拆分为 14 个模块
- 模块化设计，便于维护和扩展

## Kanban 多 Agent 平台

- **自动任务分解**：一句话拆成子任务树，自动分配模型
- **Swarm 集群**：`hermes kanban swarm` 一键创建多 Agent 拓扑
- **Per-task 模型覆盖**：不同任务使用不同模型
- **工作树隔离**：任务间环境独立
- **定时任务**：支持 cron 调度
- **故障恢复**：自动重试和状态恢复

## 安全增强

### Promptware 防御

- 内置 15 种攻击模式库
- 内存扫描
- 工具结果隔离

### Secrets 管理

- **Bitwarden Secrets Manager**：一个 Token 管所有 API 密钥

### 供应链安全

- 控制平面文件保护
- `hermes audit` 供应链审计

## 技能生态

### 技能 Bundles

一条命令切换工作流：
- `/writing-day` — 写作模式
- `/coding-day` — 编程模式

### 新技能

- `code-wiki` — 项目持久化开发维基
- `openhands` — 自主代码执行
- `web-pentest` — 网页渗透测试

### Nous 认证 MCP 目录

```bash
hermes mcp  # 一键安装认证 MCP
```

## 工具升级

| 工具 | 更新内容 |
|:-----|:-----|
| **图像生成** | Krea 2 Medium/Large |
| **消息平台** | ntfy（第 23 个，无需账号） |
| **TUI** | 多会话管理 |
| **部署** | Docker s6-overlay, Node 22 LTS |

## 相关链接

- ../实体/Hermes_Agent.md
- [[brainstorming工作流]]
- [[Agent 浏览器自动化 Chrome DevTools MCP 接入实战]]
- [[HermesSkills效率翻倍指南]]

## 来源

- 微信公众号：布鲁斯 AI
- 官方发布：https://github.com/NousResearch/hermes-agent/releases
