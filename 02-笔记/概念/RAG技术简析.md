---
title: RAG 技术简析
created: 2026-05-24
updated: 2026-05-30
tags: ["rag", "knowledge-base", "ai", "concept"]
status: active
sources: []
---

# RAG 技术简析

> 来源：综合多篇技术文章整理

## 什么是 RAG

RAG（Retrieval-Augmented Generation，检索增强生成）是一种将外部知识检索与大语言模型生成相结合的技术架构。

## 为什么需要 RAG

大语言模型存在以下局限：
1. **知识截止**：训练数据有截止日期，无法获取最新信息
2. **幻觉问题**：模型可能生成看似合理但实际错误的内容
3. **领域知识缺失**：通用模型对特定领域的专业知识掌握有限

RAG 通过检索外部知识库，让模型基于真实文档生成答案，有效缓解上述问题。

## RAG 的核心流程

```
用户提问 → 查询理解 → 向量检索 → 相关性排序 → 上下文拼接 → LLM 生成 → 答案输出
```

## RAG 的主要组件

| 组件 | 作用 | 常见方案 |
|:-----|:-----|:-----|
| **文档加载器** | 读取和解析文档 | LangChain Document Loaders |
| **文本分块** | 将长文档切分成小块 | Character/Recursive/Token Chunking |
| **嵌入模型** | 将文本转换为向量 | OpenAI text-embedding, BGE, M3E |
| **向量数据库** | 存储和检索向量 | Chroma, Milvus, Pinecone, Qdrant |
| **检索器** | 根据查询检索相关文档 | 向量检索 + 关键词检索混合 |
| **生成模型** | 基于检索内容生成答案 | GPT-4, Claude, Qwen, Llama |

## RAG 的演进方向

1. **基础 RAG** — 简单的向量检索 + 上下文拼接
2. **高级 RAG** — 查询改写、重排序、多跳检索
3. **Agentic RAG** — Agent 自主决定检索策略、多轮检索、自我修正

## 本系统 RAG 配置

| 组件 | 当前方案 |
|:-----|:-----|
| 文档加载 | Scrapling + crawl4ai |
| 文本分块 | 按段落/章节智能分块 |
| 嵌入模型 | BGE / M3E（本地） |
| 向量数据库 | Chroma |
| 检索 | 混合检索（向量 + 关键词） |
| 生成 | sensenova / Ollama 本地模型 |

## 相关链接

- [[本地知识库]]
- [[Chroma]]
- [[BGE]]
- [[M3E]]
- [[MemOS 实操笔记]]

## 来源

- Karpathy LLM Wiki 相关讨论
- LangChain RAG 文档
- 多篇微信公众号技术文章

---

> [!NOTE] 更新日志
> - 2026-05-30: 补充本系统 RAG 配置信息
