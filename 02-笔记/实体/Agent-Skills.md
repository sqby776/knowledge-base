---
title: Agent-Skills
created: 2026-06-16
updated: 2026-06-16
tags: [workflow, ai-agent, tutorial]
status: archived
sources: [99-归档/2026-06-16/2026-06-16_把工程师工作流打包给AI执行_agent-skills.md]
confidence: low
trust_score: 0.17
---
# Agent-Skills

> 由 Addy Osmani 开发的 GitHub 项目（60k+ stars），将工程开发流程打包成「技能」，让 AI 每次都能走完整规范流程。

## 核心功能

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
- **反借口机制**：如测试技能里明确列出「以后再加测试」「逻辑太简单不用测」等理由并说明为什么是错的
- **[[../概念/技能迭代法|doubt-driven-development]]**：对每个非显而易见的决策做对抗性检查
- **source-driven-development**：每个框架用法必须有官方文档出处
- **context-engineering**：让 Agent 在正确时机拿到正确信息

### 安装方式

- **Claude Code**：`/plugin marketplace add addyosmani/agent-skills`
- **Cursor**：复制 SKILL.md 到 `.cursor/rules/`
- 也支持 Gemini CLI、Windsurf 等

## 与现有体系的关系

与 [[Hermes_Agent|Hermes Agent]] 技能系统高度相关：
1. 本项目偏工程开发场景（代码编写/审查/测试）
2. 与 Hermes 办公自动化/公文处理技能互补
3. 「反借口」「验证检查点」等设计思路可借鉴到 Hermes SKILL 编写中
4. 对单人/小团队价值最大

## 相关链接

- [GitHub: addyosmani/agent-skills](https://github.com/addyosmani/agent-skills)
- [[Hermes_Agent]]
- [[../概念/技能迭代法]]
