---
title: Hermes Skills 效率翻倍指南
created: 2026-05-30
updated: 2026-05-30
tags: ["hermes", "skills", "productivity", "tutorial"]
status: active
sources: [https://mp.weixin.qq.com/s/KZwLXt9YjxfVYAbpGQ6rQg]
---

# Hermes Skills 效率翻倍指南

> 来源：微信公众号「科技奇遇寨」，2026-05-26 抓取

## 核心观点

> Skills 不是插件，是「按需加载的知识文档」。它告诉 Agent：遇到这类任务，按什么流程走。
> 没任务的时候它就躺着，不占 Token，不拖速度。
> 装 20 个 Skills 跟装 5 个，运行速度几乎没差别。
> 真正有差别的是——你遇到问题时，Agent 有没有现成的「经验」可以调。

## 8 个推荐 Skills

### 1. excalidraw — 流程图不用再画了

**安装**：`hermes skills install excalidraw`

**用途**：画流程图、架构图、思维导图

**⚠️ 坑**：纯命令行环境下看不到渲染效果，需要接 Web UI（如 hermes-workspace）

### 2. find-skills — 我不知道该装什么，让它帮我找

**安装**：`hermes skills install vercel-labs/find-skills`

**用途**：把需求翻译成技能组合

**本质**：帮你把需求翻译成技能组合。先装它，再让它帮你规划其他的。

### 3. github-pr-workflow — 写 PR 这件事我再也不想手动做了

**安装**：内置，无需安装，直接 `/github-pr-workflow`

**用途**：从建分支到提 PR 的完整流程

### 4. docker-management — 再也不用背 docker 命令了

**安装**：`hermes skills install official/devops/docker-management`

**用途**：容器/镜像/Compose 全生命周期管理

### 5. duckduckgo-search — 零成本的「实时情报员」

**安装**：`hermes skills install official/research/duckduckgo-search`

**用途**：无需 API Key 的免费搜索

**特点**：
- 支持文本/新闻/图片/视频四种搜索模式
- 完全免费，不用注册任何 API

### 6. scrapling — 反爬虫？它根本不怕

**安装**：`hermes skills install official/research/scrapling`

**用途**：绕过反爬检测的数据抓取

**⚠️ 注意**：抓取前请确认目标网站允许爬取（查看 robots.txt），遵守合规要求。

### 7. plan — 复杂任务先「想清楚」再动手

**安装**：内置，无需安装，直接 `/plan`

**用途**：执行前生成结构化任务计划，防止 Agent 没有规划就乱跑

### 8. claude-code — 让 Hermes 当「项目经理」，Claude Code 当「程序员」

**安装**：内置（需本地安装 Claude CLI），直接 `/claude-code`

**用途**：多 Agent 协作

## Skills 选择策略

> 装多不如装准。

**先装一个 find-skills**：帮你找其他 Skills

**plan 和 github-pr-workflow 内置，不用装**

**按主场景补充**：

| 你的角色 | 重点装这些 |
|:-----|:-----|
| 开发者 | docker-management + claude-code |
| 运营/内容 | excalidraw + duckduckgo-search + scrapling |
| 数据分析 | scrapling + google-workspace |
| 安全研究 | sherlock + scrapling |

## 核心结论

> Skills 不是越多越好，是越用越精。
> 用过一段时间你会发现，真正高频用到的，也就那 5-8 个。

## 相关链接

- [[Hermes-Agent]]
- [[Skills 管理]]
- [[find-skills]]
- [[scrapling]]

## 来源

- 微信公众号「科技奇遇寨」：https://mp.weixin.qq.com/s/KZwLXt9YjxfVYAbpGQ6rQg
