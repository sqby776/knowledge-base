# RAG

## 定义

Retrieval-Augmented Generation（检索增强生成）—— 一种将外部知识检索与大语言模型生成相结合的技术架构。

## 核心流程

```
用户提问 → 检索相关文档 → 将文档作为上下文 → 让 LLM 生成答案
```

## 与 LLM Wiki 的关系

- **RAG** 是技术架构，关注「如何检索 + 如何生成」
- **LLM Wiki** 是知识组织形态，关注「如何结构化 + 如何关联」
- LLM Wiki 可以作为 RAG 的检索源

## 演进路线

1. **基础 RAG** — 向量检索 + 简单拼接
2. **Agentic RAG** — Agent 自主决定检索策略、多轮检索、自我修正
3. **知识飞轮** — RAG 结果反哺知识库，知识库优化 RAG 检索

## 相关链接

- [[Agentic RAG]]
- [[LLM Wiki]]
- [[知识飞轮]]
- [[Source-first]]

## 来源

- 超级猛：《我又把 Obsidian 知识库升级了》
- Karpathy LLM Wiki 实践

---

> [!NOTE] 待验证
> 本页面内容基于多篇公众号文章综合整理，部分概念细节需进一步验证
