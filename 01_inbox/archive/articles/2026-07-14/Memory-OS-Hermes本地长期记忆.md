---
title: Memory OS — Hermes Agent 本地长期记忆系统 原文
created: 2026-07-14
updated: 2026-07-14
tags: [source, memory, hermes-agent, auto-compiled]
---

# Memory OS — 1045 Star、7 层记忆 OS：用 Qdrant+SQLite 给 Hermes Agent 装本地长期记忆

> 来源：公众号 arduino
> 链接：https://mp.weixin.qq.com/s/RB_t7vkRiZrrGY-Vvel8Mw

## 核心观点

Memory OS 是一个面向 Hermes Agent 的本地长期记忆系统：用 Python、SQLite、Qdrant、Redis、ARQ Worker 等组件，把 Agent 的会话、结构化事实、语义检索和自动 Wiki 串起来，并在调用 LLM 前做"精准上下文注入"。

## 7 层记忆结构

1. **Workspace**：MEMORY.md、USER.md、CREATIVE.md
2. **Sessions**：SQLite + FTS5 的会话搜索
3. **Structured Facts**：结构化事实库，带 trust scoring
4. **Fabric**：跨会话召回，基于修改过的 Icarus Plugin
5. **Vector Database**：Qdrant，支持 4096d Cosine + BM25 sparse
6. **LLM Wiki**：自动整理的 Wiki vault
7. **Ground Truth hierarchy**：SOUL.md、rulebook.md

## 最有意思的 3 个功能

### 1. 精准上下文注入
pre_llm_call 会从多个来源做召回，按相关性阈值过滤，per-session 去重，跳过 trivial messages。

### 2. 第 7 层 Ground Truth
作者认为仅仅召回不够，Agent 必须被明确要求"相信并使用这些注入记忆"。
否则会出现 memory-zero behavior：看似有记忆，实际还在失忆式重复劳动。

### 3. 本地跑，不绑某个模型服务
记忆基础设施跑在本机，模型供应商可以换，但记忆资产不跟着服务商走。

## 安装

```bash
git clone https://github.com/ClaudioDrews/memory-os.git
cd memory-os
curl -sSL https://raw.githubusercontent.com/ClaudioDrews/memory-os/main/setup.sh | bash
```

依赖：Hermes Agent + Docker + Python 3.11+

## 适合谁

- 已经在用 Hermes Agent 的用户
- 想让 Agent 长期参与项目的独立开发者
- 在意本地记忆和 provider 灵活性的隐私党
- 想研究 Agent memory architecture 的 AI 工程师

## 不适合谁

- 只想找一个网页聊天工具的人
- 不想碰 Docker / Python 环境的人
- 没用过 Hermes Agent 也不准备折腾的人