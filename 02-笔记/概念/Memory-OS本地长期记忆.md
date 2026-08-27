---
title: Memory OS — Hermes Agent 本地长期记忆系统
created: 2026-07-14
updated: 2026-07-14
tags: [hermes-agent, memory, knowledge-base]
status: archived
confidence: low
source: 公众号 arduino
trust_score: 0.17
---
# Memory OS — Hermes Agent 本地长期记忆系统

> 1045 Star 开源项目，用 Qdrant + SQLite 给 Hermes Agent 装 7 层本地长期记忆，不绑云服务。
> GitHub: https://github.com/ClaudioDrews/memory-os

## 核心架构：7 层记忆

Memory OS 的核心洞察是：不同种类的记忆应该放在不同的"容器"里，而不是一股脑丢进向量库。

```
第1层 Workspace       MEMORY.md / USER.md / CREATIVE.md   身份+偏好+固定规则
第2层 Sessions         SQLite + FTS5                        历史对话全文检索
第3层 Structured Facts  结构化事实库 + trust scoring        可复用的稳定事实
第4层 Fabric            跨会话召回（修改版 Icarus Plugin）   模式识别
第5层 Vector Database   Qdrant（4096d Cosine + BM25 sparse）模糊语义召回
第6层 LLM Wiki         自动整理的 Wiki vault                 长期知识沉淀
第7层 Ground Truth      SOUL.md / rulebook.md              权威上下文（告诉Agent优先用）
```

## 最关键的设计：第 7 层 Ground Truth hierarchy

作者认为：**仅仅召回不够，Agent 必须被明确要求"相信并使用这些注入记忆"**。

否则会出现"记忆零行为"（memory-zero behavior）：
- Qdrant 已经把信息注入了，Agent 还要再查一遍 Qdrant
- session history 已经给了，Agent 还要重新跑 session_search
- facts 已经在上下文里，Agent 还要再验证 facts

解决方案：通过 SOUL.md、rulebook.md 等身份/规则层，明确告诉 Agent：被注入的记忆是权威上下文，应优先使用。

## 精准上下文注入

`pre_llm_call` 流程从多个来源做召回 → 按相关性阈值过滤 → per-session 去重 → 注入上下文。

**亮点细节**：会跳过 trivial messages（社交性结尾等没必要记的内容）。避免"垃圾进垃圾出"。

## 技术栈

| 组件 | 用途 |
|------|------|
| Hermes Agent | 宿主 |
| Docker | 容器化服务 |
| Qdrant | 向量数据库（语义检索） |
| Redis | 缓存/队列 |
| ARQ Worker | 异步任务队列 |
| Python 3.11+ | 运行环境 |
| SQLite + FTS5 | 会话历史全文检索 |

## 兼容的 LLM Provider

OpenRouter / OpenAI / Anthropic / Ollama / 其他 Hermes 支持的 provider。

记忆层在本地，模型可以换，记忆资产不跟着服务商走。

## 安装

```bash
git clone https://github.com/ClaudioDrews/memory-os.git
cd memory-os
curl -sSL https://raw.githubusercontent.com/ClaudioDrews/memory-os/main/setup.sh | bash
```

依赖：Hermes Agent + Docker + Python 3.11+

## 值得借鉴的设计点

1. **记忆分层** — 不同类型分开放，不是所有东西进向量库
2. **Trust scoring** — 事实不是平等的，可信度需要量化
3. **Semantic dedup** — cosine 相似度阈值合并重复内容
4. **Fallback 链** — hybrid → dense → lexical → SQLite 逐级降级
5. **去重注入** — 避免同一段上下文反复塞进模型
6. **Ground Truth 层** — 让 Agent "相信"注入的记忆

## 对我们知识库的启发

| 当前做法 | 可以吸收的改进 |
|----------|---------------|
| 手动标记 confidence: high/medium/low | 改为自动 trust scoring |
| 双链靠人工维护 | 引入 semantic dedup 自动检测重复和矛盾 |
| 结晶摘要手写 | 引入 session 级别的自动事实提取 |
| 无 Ground Truth 机制 | 增加 SOUL.md / rulebook.md 层级 |

## 参考

- [[Hermes Agent]] — 宿主工具
- [[知识库架构]] — 现有知识体系
- [[结晶摘要-2026-07-14]] — 本日结晶