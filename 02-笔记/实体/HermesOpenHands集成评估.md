---
title: Hermes + OpenHands 集成评估
created: 2026-05-30
updated: 2026-05-30
tags: ["hermes", "openhands", "integration", "evaluation"]
status: active
sources: [https://mp.weixin.qq.com/s/kddlLnc6FEc_tXtacfZfHQ]
---

# Hermes + OpenHands 集成评估

> 来源：微信公众号「极客 BIM 设计工坊」，2026-05-26

## 核心定位

Hermes Agent 新增可选技能 **OpenHands**，定位是：

| 角色 | 职责 |
|:-----|:-----|
| **Hermes** | 入口、记忆、跨平台调度、技能管理 |
| **OpenHands** | 进入代码仓库，读项目、改代码、跑测试、验证 |

## 安装方式

```bash
hermes update
hermes skills install official/autonomous-ai-agents/openhands
```

使用时可以直接说：
```
用 OpenHands 检查这个仓库的测试失败原因
```

## 角色分工

### Hermes（总入口）

- 管"什么时候、用什么工具、按什么习惯做事"
- 记住偏好，加载技能，从 Telegram、命令行、Discord 等地方接收任务
- 跑终端、读文件、写计划、定时执行

### OpenHands（执行团队）

- 管"进入代码仓库后，怎么理解需求、改代码、跑验证"
- 更偏工程执行的 agent
- 官方定位：AI-driven development

## 核心功能

适合放进真实工作流的三类任务：**有上下文、有文件、有验证**

1. **代码修改**：修 bug、补测试、改配置、迁移小模块
2. **项目理解**：让 agent 读 README、目录、issue，再给出改法
3. **多 agent 分工**：Hermes 可把 OpenHands 与 Claude Code、Codex、OpenCode 放在同一套技能入口下

## 适合谁 / 不适合谁

### 适合 ✅

- AI 创业者、独立开发者、技术团队负责人
- 多项目开发、工具链试验、自动化修 bug、研发流程评估
- 已经有一堆自动化脚本但缺统一入口的人

### 不适合 ❌

- 普通 AI web 用户（写文案、做总结、问知识）
- 没有本地环境、不愿看 diff、不跑测试、只想要一次性答案

## 试用建议

**别从复杂任务开始**：

| 步骤 | 操作 |
|:-----|:-----|
| 第一天 | 只读不改，看它能否准确理解项目 |
| 第二步 | 只改小文件，必须跑测试 |
| 第三步 | 让 Hermes 比较不同 agent 的结果，而不是盲信一个答案 |

**避坑**：
- 不要把它当搜索引擎：给明确任务、仓库路径、验收标准
- 不要省略验证：要求它跑测试、列出改动文件、说明没覆盖的风险
- 不要第一天就让它改生产配置、账单逻辑或权限系统

## 判断

> **如果你只是问问题，不需要 OpenHands。**
> **如果你要改一个真实项目，OpenHands 才开始有价值。**
> **如果你想把不同 agent 串成流程，Hermes 才是重点。**

## 相关链接

- [[Hermes-Agent]]
- [[OpenHands]]
- [[Claude Code]]
- [[Codex]]
- [[OpenCode]]

## 来源

- Teknium X post: https://x.com/teknium/status/2059038964552745378
- Hermes Agent GitHub: https://github.com/NousResearch/hermes-agent
- OpenHands GitHub: https://github.com/OpenHands/OpenHands (7.4 万+ stars)
- OpenHands Docs: https://docs.openhands.dev/
