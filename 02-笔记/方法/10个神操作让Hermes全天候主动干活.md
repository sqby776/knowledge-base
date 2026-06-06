---
title: 10个神操作，让Hermes全天候主动干活
source: 智东西 / 毕伟豪
url: https://mp.weixin.qq.com/s/7YexgxrySREcn1tBffLjVg
date: 2026-06-05
status: active
type: note
category: methods
tags: [Hermes, 自动化, Cron, Kanban, 多Agent, 工作流, Sharbel, Mission Control, Webhook, Slash Goal]
sources: ["https://mp.weixin.qq.com/s/7YexgxrySREcn1tBffLjVg"]
---

# 10个神操作，让Hermes全天候主动干活

> **编译时间**: 2026-06-05
> **来源**: 智东西 6月5日，作者毕伟豪，编辑漠影
> **核心作者**: Sharbel（YouTube开源博主）

## 核心观点

把Hermes从"对话工具"升级为"24小时AI助手"的10个实操方案。原文来自Sharbel的YouTube视频。

**建议：如果只做一个操作，从Cron开始。**

## 10个操作详解

### 1. Mission Control：任务控制中心

做一个总控面板（Max HQ），可视化所有Agent工作状态：什么在跑、什么在等、什么被堵住。把Hermes嵌入面板，可以直接看到任务进度。

- **项目**: [openclaw-mission-control](https://github.com/sharbelxyz/openclaw-mission-control)
- **适用**: 多Agent场景下追踪任务状态
- **类比**: 类似Kanban看板但更可视化

### 2. 监控看板变化（Notion/飞书/企微）

Hermes每隔几分钟扫描看板，发现选题状态变化时自动生成简报。

- **适配**: 飞书多维表格、企业微信、Trello 同理
- **实现**: Cron + web_extract + 差量检测
- **核心逻辑**: 当工作流中某处状态变化时，Hermes自动知道下一步做什么

### 3. Cron定时任务

让信息在开口之前就送到：

- 每天早上发AI圈新闻
- 每几小时扫X平台找值得引用的帖子
- 每周审计选题库
- 每周五总结卡住选题

**核心观点**: 这是让Hermes变成24小时助理最快的方式。

### 4. Slash Goal：模糊提示词出模糊结果

`/goal` 命令让Agent朝着目标持续推进。模板：

1. 明确结果（如"决定本周最值得拍的选题"）
2. 给出信息源（VidIQ数据、竞品动态、历史表现）
3. 约束条件（避开重复角度、避开套路）
4. 明确交付物（标题、钩子、Demo清单）

### 5. 子Agent研究团队

三个Agent同时工作：一个看关键词信号，一个看竞品数据，一个看历史表现。汇总成一个拍摄建议。

### 6. Telegram话题分组当工作区

不同事进不同房间，维持独立上下文。每个话题跑不同工作流。

### 7. 看板追踪任务

不要让Agent任务消失在对话里。Kanban让每项任务都有位置：待办、进行中、已完成、谁负责、什么被堵住。

### 8. Skills即SOP

任何要解释两遍的工作流，就该变成Skill。Sharbel有115个skills，最典型的是Nova（YouTube专属Agent），掌握完整视频制作SOP。

### 9. Webhooks事件驱动

Cron是因为时间流动，Webhook是因为世界变了。来了新客户、GitHub开了PR、竞品发了视频——事件触发Hermes自动处理。

### 10. 按工种分Agent

不要让一个Agent做所有事。不同Agent配不同模型、工具、权限。有些用最强模型，有些每小时查个页面就行。

## 与现有系统的关联

- 与 `[[ai-agent持续工作流]]` 互补 — 本文提供具体操作清单，工作流笔记侧重方法论
- 与 `[[Kanban 工作流]]` 互补 — Kanban是第7个操作的具体实现
- 与 `[[定时抓取]]` 相关 — 第3个Cron操作的落地实践
- 与 `[[long-term-memory-management]]` 相关 — 多Agent分工（第10条）涉及记忆隔离

## 可落地行动项

| 优先级 | 行动 | 说明 |
|--------|------|------|
| P0 | 加强Cron任务配置 | 检查现有cron任务是否覆盖日常推送场景 |
| P0 | 实现看板监控 | 对飞书/Notion看板做增量检测 |
| P1 | 推进Skills化 | 重复两次以上的流程固化为Skill |
| P1 | 探索Webhook | 为关键事件（如PR、客户变化）配置触发 |
| P2 | 实验Slash Goal | `/goal` 命令测试复杂任务推进 |
| P2 | 探索Mission Control | 评估是否需要可视化面板 |
