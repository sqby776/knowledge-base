---
title: Hermes Agent 接入 Browse.sh 浏览器技能目录
source: 微信公众号
url: https://mp.weixin.qq.com/s/BmM_7a2ETDPMR_TL4icU3w
date: 2026-06-02
status: compiled
type: article
category: 方法
tags: [公众号文章, 2026-06-01抓取]
---

# Hermes Agent 接入 Browse.sh 浏览器技能目录

> 来源: 微信公众号
原文链接: {url}
> 抓取时间: 2026-06-01

## 核心要点

- - [[CloakBrowser vs camofox-browser：反检测浏览器选型对比_学习要点.md]]

## 原始内容

---
title: Hermes Agent 接入 Browse.sh 浏览器技能目录
source: 微信公众号
url: https://mp.weixin.qq.com/s/BmM_7a2ETDPMR_TL4icU3w
date: 2026-06-01
status: inbox
type: article
category: 浏览器
tags: [公众号文章, 2026-06-01抓取]
---

---
title: Hermes Agent 接入 Browse.sh 面向 Agentic 未来的浏览器技能目录
created: 2026-05-27
updated: 2026-06-01
tags: ["hermes", "browse.sh", "browser", "skills", "agent", "automation"]
status: active
author: One 掌柜
sources: [https://mp.weixin.qq.com/s/BmM_7a2ETDPMR_TL4icU3w]
---

# Hermes Agent 接入 Browse.sh 面向 Agentic 未来的浏览器技能目录

> 作者：One 掌柜（One 的 AI 工具箱）
> 来源：微信公众号
> 日期：2026-05-27

---

今天看到 Browserbase 发了一个新东西，叫 **Browse.sh**。

原文标题：`Browse.sh, a catalog of browser skills for the Agentic future`

翻成人话：**Browse.sh 想做一个面向 Agentic 未来的浏览器技能目录。**

这个定位比单纯"浏览器自动化工具"更重要。因为如果未来 Agent 真的要替人操作网页，那网页本身就不能只被当成一个临时打开、临时理解、临时点击的界面。它需要一层可以被复用的操作知识。

---

## 一、Browse.sh 是什么？

Browse.sh 有两层东西：

| 层级 | 说明 |
|------|------|
| **Browse.sh Catalog** | 可以在里面搜索真实网站和真实任务，看有没有现成的 browser skill |
| **Browse CLI** | 安装命令 `npm i -g browse`，可以给 Agent 安装不同网站的 skill |

```bash
browse skills add alltrails.com
browse skills add recreation.gov
browse skills add weather.gov
browse skills add plugshare.com
browse skills add ramp.com
```

这就像早期插件市场，但又不完全一样。**插件通常是软件给用户用的，Browse.sh 的 skill 是网站操作经验给 Agent 用的。**

---

## 二、Skill 的本质

Browse.sh 里的 skill，本质上是一个 **SKILL.md**，再加一些必要脚本。

一个好的 browser skill，应该让人能看懂，也让 Agent 能执行。它要写清楚：

| 内容 | 说明 |
|------|------|
| 任务类型 | 适合走浏览器，还是适合走 API |
| 稳定入口 | 网站有哪些稳定入口 |
| 靠谱 selector | 哪些 CSS selector 稳定 |
| 隐藏 API | 哪些接口可以直接请求 |
| 反常识坑 | 哪些坑要避开 |
| Fallback | 出问题时有什么备用方案 |

**这其实是在给网页加一层 Agent 可读的操作语义。**

过去网页主要是给人看的（搜索框、按钮、筛选器、分页、弹窗），但 Agent 来操作网页时，它需要的不是"好不好看"，而是**最稳定、最低成本、最少歧义的路径**。

---

## 三、Catalog 的价值

官网截图里已经能看到一些具体例子：

| 网站 | 任务 | 方式 |
|------|------|------|
| ABC7 | 加州高速交通 | API |
| AllTrails | 路线搜索 | Browser |
| Amazon | 商品搜索 | Browser |
| Airbnb | 房源搜索 | Browser |
| Craigslist | listing 搜索 | API |
| NASA | 每日一图 | API |

Browse.sh 的野心：**不是只服务某一个垂直场景，而是想把 Web 上那些高频、碎片化、但又很难标准化的任务，慢慢变成 Agent 可以调用的技能。**

搜索商品、查房源、找路线、查交通、抓取政府数据、操作企业 SaaS——这些任务单个看都不大，但如果都能沉淀成 skill，Agent 的能力边界就会慢慢扩出去。

---

## 四、和传统 API 生态的区别

| 维度 | API 生态 | Browser Skill |
|------|---------|--------------|
| 能力来源 | 网站主动开放 | Agent 从真实网页总结 |
| 使用方式 | 调用接口 | 加载 skill 执行 |
| 覆盖范围 | 有 API 的网站 | 所有网站（有 API 用 API，无 API 走 Browser） |
| 数据获取 | 结构化响应 | 可从 XHR/JSON API/ DOM 多途径获取 |

**原则**：有 API 就用 API，没有 API 就走 Browser。能从页面请求里拿到结构化数据，就别硬看 DOM。必须点页面，就把路径写清楚。

---

## 五、为什么适合 Hermes Agent

Nous Research 说，Hermes Agent 现在可以通过 Browse.sh hub 使用几百个 browser skills。

这个组合是顺的：

| Hermes Agent | Browse.sh |
|-------------|-----------|
| 长期任务、上下文、执行入口 | 具体网站的操作经验 |
| Memory + Skills + 工具 | Browser skills catalog |
| Feishu/Telegram/Discord 集成 | 可安装的网站 skill |
| 定时任务、多 profile | 外部技能目录 |

**Agent 在中间负责判断**：现在该加载哪个 skill，什么时候直接走 API，什么时候用浏览器，什么时候需要 fallback。

---

## 六、使用场景举例

### 产品研究

不只是搜 Google，可以调用 Amazon、Airbnb、Craigslist、Zillow 这类网站的 skill，拿到更结构化的市场信息。

### 运营监控

不只是每天打开网页看一眼，可以加载对应网站的 skill，按稳定路径抓取变化。

### 数据抓取

政府数据、企业 SaaS、社交媒体——有 skill 就直接用，没有就自己写一个沉淀下来。

---

## 七、总结

> Browse.sh 想做的，不是另一个浏览器自动化工具，而是一个**面向 Agentic 未来的浏览器技能目录**。

Skill 不是炫技，是一种新的网页抽象层。它把"工程师脑子里的经验"、"散落在脚本里的代码"、"每个 Agent 运行时自己摸索的路径"，变成一个**公开、可复用、可安装**的目录。

这和 Hermes Agent 的长期工作流理念天然契合。Hermes 负责上下文和执行，Browse.sh 负责把网页操作经验整理成可安装的技能。

**未来 Agent 的能力边界，不在于模型有多聪明，而在于它有多少可复用的技能可以调用。**

---

## 相关链接

- [[Hermes_Agent.md]]
- [[CloakBrowser vs camofox-browser：反检测浏览器选型对比_学习要点.md]]
- [[我做了一款 AI 编辑 Word 的 Skill.md]]
- [[Hermes Agent 接入 Browse.sh 浏览器技能目录.md]]

## 来源

- 微信公众号文章
- 作者：One 掌柜
- 发布日期：2026-05-27
