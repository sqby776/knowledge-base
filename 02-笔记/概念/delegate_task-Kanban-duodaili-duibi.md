---
title: delegate_task 与 Kanban 的多代理协作对比
created: 2026-06-05
updated: 2026-06-05
tags: [delegate_task, kanban, 多代理, 工作队列, 任务管理, 状态机]
status: active
sources: ["https://mp.weixin.qq.com/s/jObS8xmcrrVoizArKXRtTg"]
source_url: https://mp.weixin.qq.com/s/jObS8xmcrrVoizArKXRtTg
related: [[Kanban]], [[delegate_task]]
---

# delegate_task 与 Kanban 的多代理协作对比

> 来源：微信公众号「量子智元」

## 核心区别

delegate_task 本质是 RPC 阻塞调用——父 agent 发请求，阻塞等回复，子 agent 没有名字，干完就走。Kanban 是持久化工作队列 + 状态机——fire-and-forget，发完就走，数据活在磁盘上，机器重启任务还在。

## 关键差异对比

| 维度 | delegate_task | Kanban |
|------|--------------|--------|
| 通信模型 | RPC 阻塞调用 | fire-and-forget 持久化队列 |
| 失败处理 | 子 agent 挂了，全部重来 | dispatcher 自动 reclaim，连续失败 block 让人介入 |
| 状态持久化 | 无，干完就消失 | SQLite 持久化，重启任务还在 |
| 人机通信 | 无中间可见性 | comment thread 可追溯，人可介入 |
| 适用场景 | 简单一次性任务 | 长时间、多步、有失败恢复诉求的任务 |

## Worker 操作方式

Worker 通过 Python 工具调用直接读写 kanban.db（适合跑在远端 Docker/Modal 等无 hermes CLI 的环境）：

- `kanban_show()` — 读当前任务（环境变量自带 task id）
- `kanban_heartbeat()` — 长操作报活
- `kanban_complete()` — 写 summary
- `kanban_block()` — 请求人工介入
- `kanban_create()` — 创建子任务
- `kanban_link()` — 设依赖

## 值得用的场景

1. **研究型多步工作流** — 几个研究员并行查资料，分析师综合，写手出稿，中间随时可能有人需要问问题
2. **定时维护任务** — 每天跑的东西不希望状态消失，积累几周 journal 比任何监控面板有说服力
3. **工程管线** — 拆任务 -> 并行实现 -> review -> 迭代 -> PR，依赖链用 parent-child link 表达
4. **数字分身** — 每个人可以有长期运行的 agent（inbox-triage、ops-review），有自己的记忆

## 不适用的场景

简单一次性任务，delegate_task 三行代码搞定。工具不贵，选错工具贵。
