---
title: 深度使用Hermes后的总结：15 个被忽略的 Agent 高级能力
source: 微信公众号「王二AI进化论」
url: https://mp.weixin.qq.com/s/aHrJBiDIDunr_TJFILJjPQ
tags: [Hermes, Agent, 教程, 最佳实践, auto-compiled]
date: 2026-05-30
---

# 深度使用Hermes后的总结：15 个被忽略的 Agent 高级能力

> 来源：微信公众号「王二AI进化论」| 整理：星尘 | 2026-05-30

## 核心观点

Hermes 真正有价值的地方，不在于"回答得更聪明"，而在于它围绕长期记忆、会话状态、文件回滚、多模型路由、多平台触达、定时任务、Webhook、Skills 工作流，搭了一套完整的 **Agent Harness**。

---

## 一、最容易被跳过的基础设置：让 Agent 先"成为一个人"

### 1. /personality + SOUL.md

很多人每次开启新对话，第一句都是："你是一个资深架构师……"

但在 Hermes 里，这类长期设定应该沉淀到 **SOUL.md**。SOUL.md 是 Hermes 启动时读取的核心人格文件，可以定义 Agent 的说话风格、边界、目标用户、默认判断方式。

`/personality` 则允许你在不同人格之间切换。

**实际怎么用：** 把 SOUL.md 写成一次写入、终身生效的配置。多个使用场景可分别定义不同 personality，用 /personality 切换。

### 2. MEMORY.md + USER.md

Hermes 用 FTS5 和 LLM 摘要机制帮助检索历史记忆。几周前的项目背景，今天仍然可以被带回当前会话。

- **MEMORY.md**：记录项目事实（系统架构、业务背景、长期决策、历史约束）
- **USER.md**：记录用户偏好（角色、表达风格、取舍倾向、工作上下文）

**实际怎么用：** 每周复盘结束后，让 Hermes 帮你筛选哪些内容值得写回 MEMORY.md。

### 3. /insights [days]

`/insights 30` 可以查看最近 30 天的使用分析：哪些项目消耗 token 最多，哪些模型成本最高，Agent 经常卡在哪些任务上。

**实际怎么用：** 建议把 `/insights 7` 变成每周一的固定动作。

### 4. /snapshot

`/snapshot` 可以保存当前 Hermes 的配置和状态。改坏了配置后，可以通过 `/snapshot restore <id>` 回到之前的稳定状态。

**实际怎么用：** 凡是要动长期配置前，先做一次快照。

---

## 二、会话过程中的控制能力：不要一错就重开

### 5. /branch / /fork

保留当前主线，然后分叉出一条支线去探索。可以在支线上尝试风险更高的方案，如果结果不好，再回到主线。

### 6. /rollback

Hermes 会记录它动过的文件检查点。当 Agent 进行了破坏性修改，可以用 `/rollback` 恢复。

### 7. /btw

`/btw` 可以使用当前上下文回答一个临时问题，但不会调用工具，也不会持久化到主会话。

### 8. /steer 和 /queue

`/steer` 给下一步工具调用注入修正指令，而不中断当前任务。`/queue` 可以把下一轮要做的事排队。

### 9. /yolo、/fast、/reasoning

- `/yolo`：跳过危险命令审批，适合非常信任的环境
- `/fast`：切换到更低延迟的处理模式
- `/reasoning`：调整推理模型的 reasoning effort

---

## 三、多模型和多供应商：别被单一模型锁死

### 10. /model [--provider] [--global]

Hermes 设计上是 provider-agnostic 的。可以在不中断 Agent 状态的情况下切换模型和供应商。

### 11. Auxiliary models

Agent 还要做上下文压缩、会话总结、标题生成等辅助工作。Hermes 支持给这些辅助任务单独配置模型。

---

## 四、触达和自动化：Agent 不应该只待在一个聊天窗口里

### 12. 17 个平台网关

Hermes 支持 Telegram、Discord、Slack、WhatsApp、Signal、Email、SMS、Matrix、Mattermost、飞书、企业微信、钉钉等多个平台。

### 13. /voice

Hermes 支持 CLI、Telegram DM、Discord 频道、Discord 语音频道里的实时语音。

### 14. Cron + /webhook-subscriptions

- **Cron**：用自然语言描述计划任务
- `/webhook-subscriptions`：外部系统把事件推给 Hermes

---

## 五、真正的分水岭：Skills 不是插件，是可复用工作流

### 15. Skills are slash commands

Hermes 的 Skills 都可以作为 slash commands 使用。内置了大量技能，你也可以写自己的 Skill。

---

## 总结

Hermes 真正卖的不是聊天能力，而是 **Agent Harness**。

> 风口会过去，系统会复利。把判断变成系统，把 AI 变成生产力。
