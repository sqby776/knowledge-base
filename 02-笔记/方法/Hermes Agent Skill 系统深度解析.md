---
title: Hermes Agent Skill 系统深度解析
source: 微信公众号
url: https://mp.weixin.qq.com/s/hm4iETm_v5MdmKCDNxAWLA
date: 2026-06-02
status: compiled
type: article
category: 方法
tags: [公众号文章, 2026-06-02抓取]
confidence: medium
---

# Hermes Agent Skill 系统深度解析

> 来源: 微信公众号
原文链接: https://mp.weixin.qq.com/s/hm4iETm_v5MdmKCDNxAWLA
> 抓取时间: 2026-06-02

## 核心要点

- - **自动创建**：Hermes 完成复杂任务后自动总结生成
- - **社区/手动**：从 agentskills.io 安装或自己编写
- 1. SQL 查询本周新增用户（users 表，created_at 分组）
- 3. SQL 查询本周 DAU（user_sessions 表，DISTINCT user_id）
- 5. 生成双轴折线图（品牌色 #6366F1）
- - v1.1.0（2周后）：累计用户数 + 节假日标注
- - v1.2.0（1个月后）：分批查询 + 月度对比
- - `hermes skill list` — 查看已装技能
- - `hermes skill install <name>` — 安装社区技能
- - `hermes skill search "keywords"` — 搜索
- - `hermes skill stats` — 使用统计
- - `hermes cron add` — 定时触发 Skill

## 原始内容

---
title: Hermes Agent Skill 系统深度解析
source: 微信公众号
url: https://mp.weixin.qq.com/s/hm4iETm_v5MdmKCDNxAWLA
date: 2026-06-02
status: inbox
type: article
tags: [hermes, skills, tutorial]
category: 教程
---

# Hermes Agent Skill 系统深度解析完整摘要

## 一、核心概念

Skill = 程序性记忆（流程），存于 `~/.hermes/skills/<name>/SKILL.md`

### 三种来源
- **内置技能**：40+ 开箱即用
- **自动创建**：Hermes 完成复杂任务后自动总结生成
- **社区/手动**：从 agentskills.io 安装或自己编写

### Skill vs Memory
| | Memory | Skill |
|---|---|---|
| 存什么 | 事实和偏好 | 流程和步骤 |
| 类比 | 知道同事的电话号码 | 知道怎么办理入职手续 |

## 二、实战案例：用户增长周报 Skill

### 完整流程（7步）
1. SQL 查询本周新增用户（users 表，created_at 分组）
2. SQL 查询上周新增用户（环比用）
3. SQL 查询本周 DAU（user_sessions 表，DISTINCT user_id）
4. 计算环比（涨绿跌红）
5. 生成双轴折线图（品牌色 #6366F1）
6. 生成文字摘要（模板化）
7. 发送到 #经营周报群

### 踩坑记录（5条）
- SQL 日期语法差异
- DAU 定义对齐
- 群 ID 不要搞混
- 图表配色规范
- 周一界定确认

### 迭代实践
- v1.1.0（2周后）：累计用户数 + 节假日标注
- v1.2.0（1个月后）：分批查询 + 月度对比
- 用 git 管理 Skill 版本

## 三、常用命令
- `hermes skill list` — 查看已装技能
- `hermes skill install <name>` — 安装社区技能
- `hermes skill search "keywords"` — 搜索
- `hermes skill stats` — 使用统计
- `hermes cron add` — 定时触发 Skill
