---
title: LLM Wiki
created: 2026-05-24
updated: 2026-05-24
tags: ["knowledge-base", "workflow"]
status: active
sources: []
---

# LLM Wiki

## 定义

LLM Wiki（大模型知识库）—— 一种基于大语言模型的知识组织和管理范式，将传统 Wiki 的双链结构与 LLM 的语义理解能力结合。

## 核心特征

| 特征 | 说明 |
|:-----|:-----|
| **双链结构** | 页面之间通过 `[[wikilink]]` 相互关联，形成知识网络 |
| **语义理解** | LLM 能理解页面内容的语义，而不仅是关键词匹配 |
| **自动编译** | 原始资料（文章/论文）可被 LLM 自动编译成结构化知识节点 |
| **持续进化** | 知识网络随新内容不断扩展和更新 |

## 与 RAG 的关系

- **LLM Wiki** 是知识组织形态，关注「如何结构化 + 如何关联」
- **RAG** 是技术架构，关注「如何检索 + 如何生成」
- LLM Wiki 可以作为 RAG 的检索源，RAG 可以增强 LLM Wiki 的查询能力

## 典型实现

| 实现 | 特点 |
|:-----|:-----|
| **Obsidian + Hermes** | 本地双链笔记 + AI 自动编译 |
| **Karpathy LLM Wiki** | 基于个人笔记的 LLM 知识网络 |
| **MemOS** | 智能去重 + 混合检索 + 自动预检索 |

## 核心原则

1. **Source-first** — 原始资料优先，知识节点来源于真实资料
2. **双链交叉引用** — 重要概念必须使用 `[[wikilink]]`
3. **节点分离** — 概念/实体/方法分开存储
4. **MOC 导航** — 主题地图作为理解路线图

## 相关链接

- [[RAG]]
- [[Agentic RAG]]
- [[知识飞轮]]
- [[双链交叉引用]]
- [[Source-first]]
- [[本地知识库]]
- [[MemOS]]

## 来源

- 超级猛：《我把 Hermes Agent 接进 Obsidian 后》
- 桃哥：《Hermes + Obsidian + LLM Wiki》
- Karpathy LLM Wiki 实践

---

> [!NOTE] 待验证
> 部分实现细节需根据实际使用进一步补充
