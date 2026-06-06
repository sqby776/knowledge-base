---
title: AI 记忆系统完全指南 Squish Longhand
source: 微信公众号
url: https://mp.weixin.qq.com/s/V-pJUnnGC9hDPp0Cyc3lGw
date: 2026-06-02
status: compiled
type: article
category: 方法
tags: [公众号文章, 2026-06-01抓取]
---

# AI 记忆系统完全指南 Squish Longhand

> 来源: 微信公众号
原文链接: {url}
> 抓取时间: 2026-06-01

## 核心要点

- - **Squish + Longhand**：作为 Claude Code / Cursor 等工具的 MCP 记忆层
- - **Hermes Agent**：作为独立 AI Agent 框架，有自己的记忆系统

## 原始内容

---
title: AI 记忆系统完全指南 Squish Longhand
source: 微信公众号
url: https://mp.weixin.qq.com/s/V-pJUnnGC9hDPp0Cyc3lGw
date: 2026-06-01
status: inbox
type: article
category: 记忆系统
tags: [公众号文章, 2026-06-01抓取]
---

---
title: AI 记忆系统完全指南 Squish + Longhand
created: 2026-06-01
updated: 2026-06-01
tags: ["ai", "memory", "squish", "longhand", "mcp"]
status: active
sources: [https://mp.weixin.qq.com/s/yFECJS6MnUi5MROmXk-Xaw]
---

# AI 记忆系统完全指南 Squish + Longhand

> 来源：微信公众号

## 一、核心价值

### 为什么需要记忆系统？

每次启动新的 AI 会话，助手都会从零开始。它不记得你上周做的架构决定，不记得你花了一小时调试的配置，也不记得你昨天提到的偏好。你必须重新解释一切。

**Squish + Longhand 组合解决方案：**

| 组件 | 功能 | 特点 |
|------|------|------|
| **🧠 Squish** | 智能记忆 | 自动捕获决策、约束和偏好；支持语义搜索和知识图谱；1-5ms 极速召回 |
| **📹 Longhand** | 完整记录 | 无损记录会话历史：工具调用、文件编辑、思考过程；SQLite + ChromaDB 快速检索 |

> **协同效应：** Squish 提供"精华记忆"（AI 理解后的总结），Longhand 提供"原始记录"（完整会话历史）。两者结合 = 既有总结，又有细节。

| 场景 | 无记忆系统 | 有 Squish + Longhand |
|------|-----------|---------------------|
| 重新描述需求 | "请重新描述需求..." | 自动加载昨天的上下文 |
| 搜索之前的决定 | 手动翻阅聊天记录 | `squish recall "数据库选择"` |
| 回放完整过程 | 无法回放 | `longhand replay` |

---

## 二、系统架构

### 组件与数据流

```
┌────────────────────────────────────────────────┐
│              AI 工具 (Claude Code / Cursor / ...) │
└────────────────────┬───────────────────────────┘
                     │
                     ▼
┌────────────────────────────────────────────────┐
│              MCP 服务器层                        │
│  ┌──────────────┐       ┌──────────────┐       │
│  │  Squish MCP  │       │ Longhand MCP │       │
│  │  (记忆管理)   │       │  (会话记录)   │       │
│  └──────┬───────┘       └──────┬───────┘       │
│         │                      │               │
│         ▼                      ▼               │
│  ┌──────────────┐       ┌──────────────┐       │
│  │ SQLite+向量  │       │ SQLite+JSONL │       │
│  │ (嵌入+图谱)  │       │ (原始会话)   │       │
│  └──────────────┘       └──────────────┘       │
└────────────────────────────────────────────────┘
                     │
                     ▼
┌────────────────────────────────────────────────┐
│   ~/.squish/           ~/.longhand/            │
│   ├ memories.db        ├ sessions/*.jsonl      │
│   ├ embeddings/        └ index/               │
│   └ graph/                                     │
└────────────────────────────────────────────────┘
```

| 组件 | 职责 | 存储 |
|------|------|------|
| **Squish** | 智能记忆管理：自动捕获、语义搜索、知识图谱 | SQLite + 向量嵌入 |
| **Longhand** | 完整会话记录：工具调用、文件编辑、思考过程 | SQLite + JSONL |

---

## 三、安装

### 快速开始

**安装 Squish**
```bash
npm install -g squish-memory
squish install --all
```

**安装 Longhand**
```bash
pip install longhand
longhand setup
```

**组合安装脚本**
```bash
#!/bin/bash
echo "🧠 安装 Squish + Longhand..."
npm install -g squish-memory && squish install --all
pip3 install longhand && longhand setup
echo "✅ 完成"
```

**验证安装**
```bash
squish status
longhand status
```

### 支持的 AI 工具

| 工具 | 安装方式 |
|------|----------|
| Claude Code | 自动 / 手动 |
| Cursor | 自动 / 手动 |
| OpenCode | 自动 / 手动 |
| ChatGPT | OAuth 登录 |
| Cline | 自动 / 手动 |
| VS Code | 手动配置 |

---

## 四、MCP 集成配置

### 连接 AI 工具

```json
{
  "mcpServers": {
    "squish": {
      "command": "npx",
      "args": ["-y", "squish-memory"]
    },
    "longhand": {
      "command": "longhand",
      "args": ["mcp-server"]
    }
  }
}
```

| 工具 | 配置文件 |
|------|----------|
| Claude Code | `~/.claude/settings.json` |
| Cursor | `~/.cursor/mcp.json` |
| OpenCode | `~/.opencode/config.json` |
| VS Code | `settings.json` |

> **提示：** 自动安装（`squish install --all`）会自动配置所有支持的 AI 工具，无需手动操作。

---

## 五、工作流程

### 日常使用

**会话流程：** `启动` → `Squish 加载记忆` → `Longhand 记录` → `对话工作` → `自动保存`

| 阶段 | 说明 |
|------|------|
| 🔄 会话进行中 | Squish 自动捕获重要决策和约束。Longhand 记录所有工具调用和编辑。 |
| 💾 会话结束后 | Squish 保存精华记忆。Longhand 保存完整会话记录以备回放。 |
| 🚀 下次启动 | Squish 加载之前的重要记忆。AI 自动知道之前的上下文。 |

---

## 六、常用命令

### Squish 命令

```bash
# 记忆管理
squish remember "信息" --type decision    # 保存
squish recall "关键词"                    # 搜索
squish list                               # 列表
squish context --json                     # 上下文

# 状态
squish status                             # 状态
squish logs                               # 日志
squish reset                              # 重置
```

### Longhand 命令

```bash
# 会话管理
longhand status                           # 状态
longhand list                             # 列出
longhand search "关键词"                  # 搜索

# 会话操作
longhand inspect <id>                     # 详情
longhand replay <id>                      # 回放
longhand export <id>                      # 导出

# 维护
longhand clean --older-than 30d           # 清理
longhand reindex                          # 重建索引
```

---

## 七、使用示例

### 场景 1：项目开发

```bash
# Day 1
squish remember "Next.js + Supabase" --type tech-stack
squish remember "RESTful + OpenAPI 3.0" --type convention

# Day 2 — AI 自动加载记忆
squish recall "项目技术栈"    # → 自动知道使用 Next.js
longhand search "API 设计"    # → 查看昨天的完整讨论
```

### 场景 2：Bug 修复

```bash
squish remember "状态更新时序问题" --type bug-fix
squish remember "解决方案：乐观更新" --type solution

# 下次遇到类似问题
squish recall "状态更新"      # → 快速找到之前的解决方案
longhand inspect abc123       # → 查看完整的修复过程
```

### 场景 3：代码审查

```bash
squish remember "所有函数必须有类型注解" --type coding-style
squish remember "使用 camelCase 命名" --type naming

squish recall "代码规范"      # → AI 自动应用规范
longhand replay def456        # → 回放审查过程
```

---

## 八、高级配置

### 性能优化

| 优化项 | 配置 | 效果 |
|--------|------|------|
| 本地嵌入 | `EMBEDDINGS_PROVIDER=local` | 1-5ms, 免费 |
| 定期清理 | `LONGHAND_CLEAN_INTERVAL=7d` | 自动清理 7 天前的旧会话 |
| 知识图谱 | `GRAPH_ENABLED=true` | 启用实体关系图谱 |
| 多模型支持 | 配置多个 LLM provider | 不同场景使用不同模型 |

---

## 九、与 Hermes Agent 的对比

| 维度 | Squish + Longhand | Hermes Agent |
|------|-------------------|-------------|
| **定位** | 通用 AI 工具记忆层 | 完整 AI Agent 框架 |
| **记忆方式** | MCP 服务器 + 本地存储 | 内置 memory 工具 + MemOS |
| **会话记录** | Longhand 记录工具调用 | session_search 检索会话 |
| **知识图谱** | Squish 内置 | ChromaDB + MemOS |
| **适用场景** | Claude Code / Cursor 等 | 全平台 Agent（飞书、微信、CLI） |
| **部署复杂度** | 低（npm + pip） | 中（需配置 gateway、profile 等） |

### 是否可以共存？

**可以！** 两者定位不同：
- **Squish + Longhand**：作为 Claude Code / Cursor 等工具的 MCP 记忆层
- **Hermes Agent**：作为独立 AI Agent 框架，有自己的记忆系统

---

## 相关链接

- [[AI 记忆系统]]
- [[MCP 服务器]]
- [[Hermes Agent]]
- [[MemOS]]

## 来源

- 微信公众号文章
