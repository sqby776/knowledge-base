---
title: Hermes 技能地图
created: 2026-05-24
updated: 2026-05-24
tags: ["ai-agent", "workflow"]
status: active
sources: []
---

# Hermes 技能地图

> MOC — Hermes Agent 技能分类主题地图

## 阅读顺序

```
核心技能 → 领域技能 → 平台集成 → 高级应用
    ↓          ↓          ↓          ↓
hermes-    devops/    messaging/  autonomous-
agent      research   social-media ai-agents
```

## 核心技能

### 1. 系统配置

- [[hermes智能体]] — Hermes 配置和扩展（必学）
- `hermes setup` — 交互式配置向导
- `hermes doctor` — 健康检查
- `hermes model` — 模型/提供商选择

### 2. 工具管理

- `hermes tools` — 工具启用/禁用
- `hermes skills list` — 技能列表
- `hermes skills install` — 安装技能

## 领域技能分类

### Development（开发）

| 技能 | 用途 |
|:-----|:-----|
| `hermes-agent` | Hermes 配置 |
| `claude-code` | 委托 Claude Code |
| `codex` | 委托 Codex CLI |
| `opencode` | 委托 OpenCode |
| `TDD` | 测试驱动开发 |
| `debugging` | 系统化调试 |

### Productivity（生产力）

| 技能 | 用途 |
|:-----|:-----|
| `office-toolchain` | Office 自动化 |
| `personal-knowledge-base` | 知识库搭建 |
| `memory-palace` | 记忆宫殿管理 |
| `notion` | Notion 集成 |
| `powerpoint` | PPT 操作 |

### Research（研究）

| 技能 | 用途 |
|:-----|:-----|
| `arxiv` | arXiv 论文搜索 |
| `web-scraping` | 网页抓取 |
| `doko-search` | 免费网页搜索 |
| `doko-research` | 深度研究 |

### Creative（创意）

| 技能 | 用途 |
|:-----|:-----|
| `architecture-diagram` | SVG 架构图 |
| `ascii-art` | ASCII 艺术 |
| `manim-video` | Manim 动画 |
| `p5js` | p5.js 创意编码 |

### MLOps

| 技能 | 用途 |
|:-----|:-----|
| `llama-cpp` | 本地 LLM 推理 |
| `huggingface-hub` | HuggingFace CLI |
| `serving-llms-vllm` | vLLM 模型服务 |

## 平台集成

| 平台 | 工具集 | 说明 |
|:-----|:-----|:-----|
| Telegram | `messaging` | 完整工具支持 |
| Discord | `discord` | 机器人集成 |
| Feishu | `feishu_doc`, `feishu_drive` | 文档/云盘工具 |
| Slack | `messaging` | 频道订阅 |

## 高级应用

### 多代理协作

- `delegate_task` — 子代理委派
- `kanban` — 多代理工作队列
- Cron Job — 定时任务

### 记忆系统

- `memory` — 持久记忆
- `session_search` — 会话搜索
- MemOS — 记忆宫殿

## 快速入口

- 想学 Hermes 配置 → 看 [[hermes智能体]]
- 想找特定功能 → 用 `hermes skills search <关键词>`
- 想安装新技能 → `hermes skills install <技能名>`
- 想管理工具 → `hermes tools`

## 相关页面

- [[Hermes能力地图]] — 生态系统全景
- [[精选Hermes智能体]] — 精选资源目录
- [[Hermes智能体-重复]] — 核心技能文档

---

*最后更新：2026-05-24*
