---
title: Agent 工具选择失败分析 — MCP/Skills 不可见问题
created: 2026-05-30
updated: 2026-05-30
tags: ["hermes", "mcp", "skills", "agent", "debugging"]
status: archived
sources: [https://developer.microsoft.com/blog/how-ai-coding-agents-actually-use-your-technology]
trust_score: 0.17
confidence: low
---
# Agent 工具选择失败分析 — MCP/Skills 不可见问题

> 来源：微软开发者博客
> 核心观点：配置了 MCP 和 Skills，Agent 可能压根没选它

## 核心问题

**关键结论：** 配置了 MCP 和 Skills，装好了测通了，但 Agent 可能压根没选它。或者选了，用错了。而你完全不知道。

## Agent 使用工具的 7 步拆解

### 第 1 步：Harness 层组装上下文

- 系统提示、工作区文件、MCP 描述、对话历史全部塞到一起
- **问题：** 上下文窗口有限。装了 20 个 MCP 扩展，harness 根据相关性排序，可能只保留一部分。工具描述太长被截掉。

### 第 2 步：模型决策

- 模型决定是直接写代码还是先调工具
- **问题：** 如果模型在训练数据里见过你的技术，它有自己的判断（哪怕是过时的）。有的模型喜欢调工具，有的喜欢依赖自身知识。

### 第 3 步：工具选择（最关键）

- 模型靠**语义匹配**选工具，不是关键词搜索
- 给 Agent 说"加个 authentication"，工具描述写的是"configure identity provider settings"，模型得自己 bridge 语义 gap
- **问题：** bridge 不上，工具就被跳过。即使描述匹配，模型也可能不选，因为它觉得自己已经知道答案了（用半年前的旧 API）

### 第 4-6 步：工具调用与结果返回

- 返回 3000 token 的文档，实际只需要 200 token → 2800 token 挤掉其他上下文
- 返回内容格式混乱 → 模型解析错误，生成完全不正确的实现
- **drag 现象：** 工具被调用了，返回了内容，但从外面看一切正常，实际上模型 latched onto wrong paragraph

### 第 7 步：错误处理

- **关键转变：** 错误信息现在是给 Agent 看的，不是给人看的
- CLI 报"Error: operation failed" → Agent 没有直觉，直接理解为字面意思，然后开始瞎猜
- **要求：** 错误信息需要用"给 Agent 读"的标准设计：具体错误码 + 修复建议 + 足够 context

## 对我们的启示

### 1. MCP/Skill 描述优化

检查 6 个 MCP + 160 个技能的描述，确保：
- 用自然语言描述用途（不是技术参数）
- 匹配用户可能的表达方式
- 描述精简，避免被截断

### 2. 错误信息 Agent 友好化

后续开发脚本时，错误信息格式：
```
[ERR_CODE] 简短描述
建议修复: 具体操作步骤
```

### 3. 工具返回精简

- 控制返回内容的 token 数
- 结构化返回（JSON/Markdown），避免格式混乱

## 调试建议

| 问题 | 检查点 | 解决方案 |
|:-----|:-----|:-----|
| 工具不出现 | 上下文窗口 | 精简工具描述，优先保留高频工具 |
| 工具选错 | 语义匹配 | 用用户语言表达工具用途 |
| 结果错误 | 返回格式 | 结构化返回，控制 token 数 |
| 错误不理解 | 错误信息 | 给 Agent 友好的错误格式 |

## 相关链接

- ../实体/Hermes_Agent.md
- [[Agent 浏览器自动化 Chrome DevTools MCP 接入实战]]
- [[HermesSkills效率翻倍指南]]

## 来源

- 微软开发者博客：https://developer.microsoft.com/blog/how-ai-coding-agents-actually-use-your-technology
- OpenAI BYO MCP：https://x.com/OpenAIDevs/status/2059703536825565499

---

> [!NOTE] 重要发现
> 这是理解 Agent 工具调用失败的关键文档，建议团队全员阅读。
