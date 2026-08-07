---
title: 8个必装Hermes Agent Skill（分类推荐）
created: 2026-07-14
updated: 2026-07-14
tags: [hermes-agent, skill, workflow]
status: active
confidence: high
trust_score: 0.9
source: 公众号 阿西-出海
---

# 8 个必装 Hermes Agent Skill

> 来源：公众号「阿西-出海」— 作者：阿西
> 链接：https://mp.weixin.qq.com/s/wuRd7fhYBgdmHxeArldj5Q

## 一、基础类（扩展 Agent 能力边界）

### 1. Skill Creator
- **来源**：Anthropic 官方出品
- **功能**：创建 Skill 的 Skill。让你把重复的工作流封装成可反复调用的 Skill
- **用法**：告诉它你要做什么 Skill → 它会先问几个问题确认需求细节 → 按规范创建
- **示例**：作者用它做了个自动化生成 PPT 的 Skill

### 2. Find Skills
- **功能**：Skill 搜索引擎
- **用法**：直接给任务，它拆成关键词，按分类/Star数/更新时间全网搜索
- **示例**：说"帮我找一个配图 Skill" → 推荐几个备选 → 选好后自动安装

## 二、产品开发类

### 3. Superpowers ⭐（21万 Star）
- **GitHub**：已斩获 21 万 Star
- **功能**：开发流程规范化套装
- **工作流**：需求梳理 → 方案确认 → 实施计划 → 写代码（subagent 并行）
- **特色**：每步做代码审查，全部完成后整体检查 + 自动 git 提交
- **适合**：已经大概知道要做什么的人

### 4. gstack
- **作者**：YC 总裁 Gary Tan（YC = Airbnb/Dropbox 孵化器）
- **功能**：内置 23 个工程专家角色（CEO/PM/设计师/工程师...）
- **特色命令**：
  - `/office-hours` — 写代码前先拷问需求
  - `/plan -ceo-review` — CEO + 工程师双视角审方案
  - `/qa` — 通过浏览器真实使用测试产品
- **适合**：动手前先把方向想清楚

**Superpowers vs gstack：**
| | Superpowers | gstack |
|:----|:----------|:-------|
| 核心 | 告诉你怎么做 | 告诉你该不该做、做什么 |
| 适合 | 已有方向，要落地 | 方向模糊，要先想清楚 |

### 5. Frontend Design
- **来源**：Anthropic 官方出品
- **功能**：去 AI 感的前端设计
- **解决**：蓝紫色渐变、千篇一律圆角卡片的 AI 味
- **效果**：配色、字体、间距一键优化，输出专业级设计

### 6. ui-ux-pro-max
- **功能**：完整设计资源库
- **内置**：50 种设计风格、97 种配色方案、9 个技术栈
- **用法**：想要什么风格直接拿来用

## 三、内容创作类

### 7. baoyu-skills
- **作者**：宝玉老师
- **内容**：将近 20 个 Skill 的技能包
- **核心**：封面图、信息图、PPT、长文排版
- **作者用得最多**：文章配图 Skill — 读完文章 → 找出适合配图的段落 → 生成插图 → 直接放到对应位置

### 8. NotebookLM Skill
- **功能**：打通 Agent 和 NotebookLM
- **效果**：在 Agent 里直接查询/分析 NotebookLM 中的所有文档
- **价值**：NotebookLM 文档处理能力天花板级别
- **附加**：减少 AI 幻觉，相当于给 Agent 接上超强长期记忆外挂

## 对我们知识库的启示

| 现状 | 可以做的 |
|------|---------|
| 我们主要用工资系统相关 Skill | 可以装 Skill Creator 和 Find Skills 来扩展 |
| 前端设计靠手写 CSS | 装 Frontend Design 或 ui-ux-pro-max 提升效率 |
| 没有设计资源库 | baoyu-skills 直接拿来用 |

## 参考

- [[Hermes Agent]] — 宿主工具
- [[Flask工资系统开发]] — 当前主要开发项目