---
title: BGE
created: 2026-05-24
updated: 2026-05-24
tags: ["rag", "tool"]
status: active
sources: []
---

# BGE

## 定义

BGE（BAAI General Embedding）—— 智源研究院开发的通用嵌入模型系列，支持中文和英文。

## 模型系列

| 模型 | 维度 | 特点 |
|:-----|:-----|:-----|
| `bge-base-zh` | 768 | 中文基础模型 |
| `bge-large-zh` | 1024 | 中文大模型，精度更高 |
| `bge-small-zh` | 512 | 中文小模型，速度快 |
| `bge-base-en` | 768 | 英文基础模型 |
| `bge-m3` | 1024 | 多语言混合模型 |

## 使用场景

| 场景 | 推荐模型 |
|:-----|:-----|
| 中文知识库 | `bge-base-zh` / `bge-large-zh` |
| 多语言混合 | `bge-m3` |
| 速度优先 | `bge-small-zh` |

## 安装使用

```python
from FlagEmbedding import FlagModel

model = FlagModel('BAAI/bge-base-zh', use_fp16=True)
embeddings = model.encode(['你好，世界', 'Hello, world'])
```

## 与其他嵌入模型对比

| 模型 | 中文能力 | 英文能力 | 速度 |
|:-----|:-----|:-----|:-----|
| **BGE** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | 快 |
| **M3E** | ⭐⭐⭐⭐⭐ | ⭐⭐ | 快 |
| **all-MiniLM-L6-v2** | ⭐⭐ | ⭐⭐⭐⭐⭐ | 最快 |

## 相关链接

- [[嵌入模型.md]]
- [[M3E.md]]
- [[Chroma.md]]
- [[RAG.md]]

## 来源

- 智源研究院 BGE 官方文档
- 本系统实际使用经验

---

> [!NOTE] 待验证
> 具体模型选择需根据实际需求调整
