---
title: MemOS 记忆系统实操笔记
created: 2026-05-24
updated: 2026-05-24
tags: ["knowledge-base", "tutorial"]
status: archived
sources: []
trust_score: 0.17
confidence: low
---
# MemOS 记忆系统实操笔记

> 来源：本系统实际配置和使用经验
> 状态：已验证
> 创建日期：2026-05-24

## 配置心得

MemOS 作为 Hermes Agent 的记忆系统，核心功能是智能去重和混合检索。

### 关键配置

```yaml
memory:
  provider: memos
  memos:
    enabled: true
    lightweightMemory: true  # 轻量模式（本机 1.5B 模型够用）
```

### 本地环境

- 嵌入模型：all-MiniLM-L6-v2（384 维，双核 CPU 的选型妥协）
- LLM：qwen2.5:1.5b Q4_K_M，端口 8081
- 首次部署跳过：lightweightMemory 设为 false 时 1.5B 模型跑完整进化太慢

### 对比 RAG

| 系统 | 检索方式 | 去重能力 | 适用场景 |
|:-----|:---------|:---------|:---------|
| [[MemOS]] | FTS5 + 向量 + 时间 | ✅ 智能去重 | 对话记忆管理 |
| [[RAG]] | 向量检索 | ❌ 需自行实现 | 知识库问答 |

## 相关链接

- [[MemOS]]
- [[MemPalace]]
- [[Chroma]]
- [[嵌入模型]]
- [[RAG]]
- ../实体/Hermes_Agent.md

---

*最后更新：2026-05-24*