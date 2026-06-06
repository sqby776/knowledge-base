---
title: 配了一堆MCP-Skills-Agent可能根本不会选
source: 微信公众号
url: N/A
date: 2026-06-02
status: compiled
type: article
category: 方法
tags: [公众号文章, 2026-06-01抓取]
---

# 配了一堆MCP-Skills-Agent可能根本不会选

> 来源: 微信公众号

> 抓取时间: 2026-06-01

## 核心要点

- - 系统提示、工作区文件、MCP描述、对话历史全部塞到一起
- - **问题：** 上下文窗口有限。装了20个MCP扩展，harness根据相关性排序，可能只保留一部分。工具描述太长被截掉。
- - **问题：** 如果模型在训练数据里见过你的技术，它有自己的判断（哪怕是过时的）。有的模型喜欢调工具，有的喜欢依赖自身知识。
- - 模型靠**语义匹配**选工具，不是关键词搜索
- - 给Agent说"加个authentication"，工具描述写的是"configure identity provider settings"，模型得自己bridge语义gap
- - **问题：** bridge不上，工具就被跳过。即使描述匹配，模型也可能不选，因为它觉得自己已经知道答案了（用半年前的旧API）
- - 返回3000 token的文档，实际只需要200 token → 2800 token挤掉其他上下文
- - 返回内容格式混乱 → 模型解析错误，生成完全不正确的实现

## 原始内容

---
title: 配了一堆MCP-Skills-Agent可能根本不会选
source: 微信公众号
url: N/A
date: 2026-06-01
status: inbox
type: article
category: MCP/技能
tags: [公众号文章, 2026-06-01抓取]
---

---
title: 你配了一堆MCP、Skills，Agent可能根本不会选
source: 微信公众号-探索AGI
url: https://mp.weixin.qq.com/s/KeF2b_fa24DTAoHiULrlJA
date: 2026-05-29
status: inbox
type: article
tags: [Hermes, MCP, Skills, Agent, 工具调用]
---

# 你配了一堆的MCP、Skills，Agent可能根本不会选

来源：探索AGI（猕猴桃）

## 核心观点

微软博客拆解了 AI Coding Agent 从"用户敲 prompt"到"生成代码"之间发生的7步过程。每一步都可能失败，且失败完全不可见。

**关键结论：** 配置了 MCP 和 Skills，装好了测通了，但 Agent 可能压根没选它。或者选了，用错了。而你完全不知道。

## Agent 使用工具的7步拆解

### 第1步：Harness 层组装上下文
- 系统提示、工作区文件、MCP描述、对话历史全部塞到一起
- **问题：** 上下文窗口有限。装了20个MCP扩展，harness根据相关性排序，可能只保留一部分。工具描述太长被截掉。

### 第2步：模型决策
- 模型决定是直接写代码还是先调工具
- **问题：** 如果模型在训练数据里见过你的技术，它有自己的判断（哪怕是过时的）。有的模型喜欢调工具，有的喜欢依赖自身知识。

### 第3步：工具选择（最关键）
- 模型靠**语义匹配**选工具，不是关键词搜索
- 给Agent说"加个authentication"，工具描述写的是"configure identity provider settings"，模型得自己bridge语义gap
- **问题：** bridge不上，工具就被跳过。即使描述匹配，模型也可能不选，因为它觉得自己已经知道答案了（用半年前的旧API）

### 第4-6步：工具调用与结果返回
- 返回3000 token的文档，实际只需要200 token → 2800 token挤掉其他上下文
- 返回内容格式混乱 → 模型解析错误，生成完全不正确的实现
- **drag现象：** 工具被调用了，返回了内容，但从外面看一切正常，实际上模型latched onto wrong paragraph

### 第7步：错误处理
- **关键转变：** 错误信息现在是给Agent看的，不是给人看的
- CLI报"Error: operation failed" → Agent没有直觉，直接理解为字面意思，然后开始瞎猜
- **要求：** 错误信息需要用"给Agent读"的标准设计：具体错误码 + 修复建议 + 足够context

## 对我们可用的功能点

### 1. MCP/Skill 描述优化
检查6个MCP + 160个技能的描述，确保：
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
- 控制返回内容的token数
- 结构化返回（JSON/Markdown），避免格式混乱

### 4. 深入学习
微软博客原文：https://developer.microsoft.com/blog/how-ai-coding-agents-actually-use-your-technology
OpenAI BYO MCP：https://x.com/OpenAIDevs/status/2059703536825565499

## 参考
- 微软开发者博客：[How AI coding agents actually use your technology](https://developer.microsoft.com/blog/how-ai-coding-agents-actually-use-your-technology)
- OpenAI BYO MCP：[推文](https://x.com/OpenAIDevs/status/2059703536825565499)