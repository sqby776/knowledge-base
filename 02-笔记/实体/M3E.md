---
title: M3E
created: 2026-05-24
updated: 2026-05-24
tags: ["rag", "tool"]
status: active
sources: []
---

# M3E

## 定义

M3E（Moka Massive Mixed Embedding）—— 由 Moka 开发的混合嵌入模型，专为中文场景优化。

## 模型特点

| 特点 | 说明 |
|:-----|:-----|
| **中文优化** | 在中文语义检索上表现优异 |
| **混合训练** | 结合多种任务数据训练 |
| **开源免费** | HuggingFace 可免费下载 |

## 模型版本

| 模型 | 维度 | 特点 |
|:-----|:-----|:-----|
| `m3e-base` | 768 | 基础版本 |
| `m3e-large` | 1024 | 大版本，精度更高 |

## 使用场景

| 场景 | 推荐度 |
|:-----|:-----|
| 中文知识库检索 | ⭐⭐⭐⭐⭐ |
| 中文语义搜索 | ⭐⭐⭐⭐⭐ |
| 多语言混合 | ⭐⭐ |

## 安装使用

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('moka-ai/m3e-base')
embeddings = model.encode(['你好，世界', 'Hermes Agent'])
```

## 与其他嵌入模型对比

| 模型 | 中文能力 | 英文能力 | 速度 |
|:-----|:-----|:-----|:-----|
| **M3E** | ⭐⭐⭐⭐⭐ | ⭐⭐ | 快 |
| **BGE** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | 快 |
| **all-MiniLM-L6-v2** | ⭐⭐ | ⭐⭐⭐⭐⭐ | 最快 |

## 推荐策略

```
中文为主 → M3E 或 BGE
英文为主 → all-MiniLM-L6-v2 或 BGE
混合 → BGE-M3（多语言模型）
```

## 相关链接

- [[BGE]]
- [[嵌入模型]]
- [[Chroma]]
- [[RAG]]

## 来源

- M3E 官方文档（HuggingFace）
- 本系统实际使用经验

---

> [!NOTE] 待验证
> 具体模型选择需根据实际需求调整
