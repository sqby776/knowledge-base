---
title: MemOS
created: 2026-05-24
updated: 2026-05-24
tags: ["knowledge-base", "tool"]
status: active
sources: []
---

# MemOS

## 定义

MemOS（Memory Operating System）—— 本地记忆宫殿系统，提供智能去重、混合检索、自动预检索等记忆管理能力。

## 核心功能

| 功能 | 说明 |
|:-----|:-----|
| **智能去重** | LLM 判断新内容是重复/更新/全新 |
| **混合检索** | FTS5 + 向量语义 + 时间衰减融合排序 |
| **自动预检索** | 每轮对话前自动召回相关记忆 |
| **技能进化** | 从经验中学习，优化技能 |
| **Web 管理面板** | :18800 端口可视化操作 |

## 技术架构

```
MemOS
├── 语义记忆（ChromaDB 向量存储）
├──  episodic 记忆（SQLite + FTS5）
├── 世界模型（结构化的环境知识）
└── 技能库（可重用的工作流）
```

## 检索流程

```
用户提问
    ↓
自动预检索（混合检索）
    ↓
FTS5 全文搜索 + 向量语义搜索
    ↓
融合排序（时间衰减加权）
    ↓
注入系统 prompt
    ↓
LLM 生成回答
```

## 配置示例

```yaml
memory:
  provider: memos
  memos:
    enabled: true
    lightweightMemory: false  # 关闭轻量模式，启用完整进化
```

## 与 ChromaDB 对比

| 维度 | MemOS | ChromaDB |
|:-----|:-----|:-----|
| **定位** | 完整记忆系统 | 向量数据库 |
| **去重** | ✅ 智能去重 | ❌ 需自行实现 |
| **检索** | ✅ 混合检索 | ⭐ 仅向量检索 |
| **预检索** | ✅ 自动 | ❌ 需手动 |

## 相关链接

- [[MemPalace]]
- [[Chroma]]
- [[知识图谱]]
- [[Hermes-Agent]]

## 来源

- MemOS 官方文档
- 本系统实际配置经验

---

> [!NOTE] 待验证
> 具体配置参数需根据实际需求调整
