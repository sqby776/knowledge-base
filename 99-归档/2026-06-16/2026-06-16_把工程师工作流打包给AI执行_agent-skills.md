---
title: "把工程师工作流打包给AI执行，让AI按规范写代码，这个项目6万star"
source: "微信公众号-量子元"
url: "https://mp.weixin.qq.com/s/3CqQnd3beLB7bPQjhlNJPg"
created: 2026-06-16
tags: [inbox, ai-agent, development-workflow, agent-skills]
---

# 把工程师工作流打包给AI执行

> 原文：微信公众号「量子元」2026-06-15

## 概述

GitHub 项目 **agent-skills**（Addy Osmani 开发，6万 star）— 把工程开发流程打包成「技能」，让 AI 每次都能走一遍完整规范流程。

## 核心内容

### 7 个斜杠命令

覆盖从「想法」到「上线」的完整链路：

| 命令 | 用途 |
|------|------|
| `/spec` | 规格说明 |
| `/plan` | 计划 |
| `/build` | 构建 |
| `/test` | 测试 |
| `/review` | 代码审查 |
| `/code-simplify` | 代码简化 |
| `/ship` | 发布上线 |

> `/build auto`：AI 生成计划后用户确认一次，后续自动跑完，失败或有风险才暂停。

### 24 个 SKILL.md 文件

每个文件结构化：触发条件 → 步骤 → 常见借口（及反驳）→ 验证要求。

亮点设计：
- **反借口机制**：比如测试技能里明确列出「以后再加测试」「逻辑太简单不用测」等理由并说明为什么是错的
- **doubt-driven-development**：对每个非显而易见的决策做对抗性检查
- **source-driven-development**：每个框架用法必须有官方文档出处
- **context-engineering**：让 Agent 在正确时机拿到正确信息

### 安装方式

- **Claude Code**：`/plugin marketplace add addyosmani/agent-skills` → `/plugin install agent-skills@addy-agent-skills`
- **Cursor**：复制 SKILL.md 到 `.cursor/rules/`
- 也支持 Gemini CLI、Windsurf 等

## 分析

这篇文章和我们当前的工作方式高度相关：
1. 我们已经在用 **SKILL.md 体系**（Hermes 技能系统）管理工作流
2. 文章提到的「反借口」「验证检查点」等设计思路值得借鉴
3. Addy Osmani 的 agent-skills 偏工程开发场景（代码编写/审查/测试），与我们的办公自动化/公文处理技能互补
4. 对单人/小团队价值最大，大团队有 CI 流程兜底

## 相关链接

- [[Hermes_Agent]]
- [[技能系统]] — Hermes SKILL.md 体系
- GitHub: github.com/addyosmani/agent-skills
