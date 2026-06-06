---
title: 2026-05-26 Hermes Skills 安装评估
created: 2026-05-26
updated: 2026-05-26
tags: [hermes-agent, decision, skills]
status: active
sources:
  - 01-收件箱/文章/2026-05-26_Hermes Skills效率翻倍.md
  - 06-查询/2026-05-26_Hermes技能升级评估.md
---

# 2026-05-26 Hermes Skills 安装评估

> 基于《我用了3个月 Hermes agent，这几个 Skills 让我效率翻倍》的评估结论

---

## 文章介绍的 8 个 Skills

| # | Skill | 安装方式 | 你的情况 | 建议 |
|---|-------|---------|---------|------|
| 1 | excalidraw | `hermes skills install excalidraw` | 新媒体运营，可能需要画流程图 | ⚠️ 可选 |
| 2 | find-skills | `hermes skills install vercel-labs/find-skills` | 新手，不知道装什么 | ✅ 推荐 |
| 3 | github-pr-workflow | 内置，`/github-pr-workflow` | 非开发者，不用 GitHub PR | ❌ 不需要 |
| 4 | docker-management | `hermes skills install official/devops/docker-management` | 不用 Docker | ❌ 不需要 |
| 5 | duckduckgo-search | `hermes skills install official/research/duckduckgo-search` | 已有（web 工具集） | ❌ 不需要 |
| 6 | scrapling | `hermes skills install official/research/scrapling` | 新媒体运营，可能需要抓取数据 | ⚠️ 可选 |
| 7 | plan | 内置，`/plan` | 已有 | ❌ 不需要安装 |
| 8 | claude-code | 内置（需 Claude CLI） | 非开发者 | ❌ 不需要 |

---

## 详细分析

### ✅ 推荐安装

#### find-skills

**理由**：
- 文章明确推荐为"所有新手的第一个 Skills"
- 帮你把需求翻译成技能组合
- 不知道装什么时，让它帮你规划
- 安装后问："我想做 XXX，该装什么 Skills？"它会给出清单和安装命令

**安装**：
```bash
hermes skills install vercel-labs/find-skills
```

---

### ⚠️ 可选安装

#### excalidraw

**理由**：
- 画流程图、架构图、思维导图
- 新媒体运营可能需要画内容结构图、工作流程图
- **⚠️ 坑**：纯命令行环境下看不到渲染效果，需要接 Web UI（如 hermes-workspace）

**建议**：如果你没有 Web UI 环境，装了也看不到效果，先不装。

#### scrapling

**理由**：
- 绕过反爬检测的数据抓取
- 新媒体运营可能需要抓取竞品网站数据、招聘数据等
- 支持隐身浏览器模式，模拟真实用户行为

**⚠️ 注意**：抓取前请确认目标网站允许爬取（查看 robots.txt），遵守合规要求。

**建议**：等你有具体抓取需求时再装，现在可以先不装。

---

### ❌ 不需要安装

| Skill | 理由 |
|-------|------|
| github-pr-workflow | 非开发者，不用 GitHub PR 流程 |
| docker-management | 不用 Docker，没有容器管理需求 |
| duckduckgo-search | 已有 web 工具集，功能已覆盖 |
| plan | 内置技能，无需安装，直接用 `/plan` |
| claude-code | 非开发者，不用代码重构 |

---

## 核心结论

> **先装 find-skills，让它帮你规划后续需要装什么。**

> **excalidraw 和 scrapling 等你有具体需求时再装。**

> **其他 5 个不需要装。**

---

## 安装命令

```bash
# 第一步：先装 find-skills
hermes skills install vercel-labs/find-skills

# 之后问它：
# "我想做 XXX，该装什么 Skills？"
```

---

## 后续行动

- [ ] 安装 find-skills
- [ ] 用 find-skills 规划后续需要装什么
- [ ] 有具体需求时再装 excalidraw 或 scrapling