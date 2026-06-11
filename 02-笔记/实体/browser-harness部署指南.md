---
title: browser-harness 部署指南
created: 2026-05-30
updated: 2026-05-30
tags: ["browser-harness", "browser-automation", "cdp", "tool"]
status: active
sources: [https://mp.weixin.qq.com/s/6bZshgptd0cY4CxaczffOQ]
---

# browser-harness 部署指南

> 来源：微信公众号
> GitHub: https://github.com/browser-use/browser-harness（~5k stars）

## 概述

browser-harness 是一个超级轻量、自愈式的浏览器遥控器（只有 592 行 Python 代码），通过 Chrome DevTools Protocol（CDP）直接连接正在运行的 Chrome 浏览器，让 AI 像真人一样操作浏览器。

## 核心特性

1. **自愈式设计**：页面改版时 AI 自动修改代码继续工作
2. **CDP 直连**：直接控制本地 Chrome 浏览器
3. **零框架**：不依赖 Selenium/Playwright 等重型框架
4. **自进化**：任务成功后自动生成 domain-skills

## 应用场景

| 场景 | 用途 |
|:-----|:-----|
| 日常生产力 | 自动爬竞品、查价格、填表格、发邮件 |
| 内容运营 | GitHub Trending 监控、社媒批量发帖 |
| 电商/副业 | 领券、下单监控、评论回复 |
| 企业办公 | 自动登录 OA 系统、填日报、抓数据 |

## 部署步骤

### 前置准备

1. 安装最新版 Google Chrome
2. 安装 Python 3.11+
3. 安装 uv：
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

### Chrome 远程调试设置

打开 Chrome → 地址栏输入：`chrome://inspect/#remote-debugging` → 勾选"Enable remote debugging"

### Linux 部署

```bash
sudo apt update && sudo apt install -y python3-pip git
cd ~
git clone https://github.com/browser-use/browser-harness
cd browser-harness
uv tool install -e .
```

### 测试连接

```bash
browser-harness --setup
```

成功会显示：浏览器已连接。

## 与 Hermes Agent 深度结合

### 为什么结合后很强？

- **Hermes Agent**：自成长、自学习的 AI 大脑（长期记忆、自创 skill、多 Agent 协作）
- **browser-harness**：最灵活的浏览器身体（自愈式、零框架、实时进化）

**1+1 > 2**：Hermes 负责想和学，browser-harness 负责干和修

### 注册为 Hermes Skill

```bash
# 1. 创建文件夹
mkdir -p ~/.hermes/skills/browser-harness

# 2. 注册 SKILL.md
ln -sf ~/browser-harness/SKILL.md ~/.hermes/skills/browser-harness/SKILL.md

# 3. 注册 interaction-skills
ln -sf ~/browser-harness/interaction-skills ~/.hermes/skills/browser-harness/interaction-skills

# 4. 注册 domain-skills
ln -sf ~/browser-harness/domain-skills ~/.hermes/skills/browser-harness/domain-skills
```

### 测试指令

在 Hermes 聊天框直接说：
- "用 browser-harness 打开百度首页，搜索 browser-harness 并截图给我"
- "用 browser-harness 打开 GitHub trending，总结前 5 个最火的仓库"

## 与内置 browser_automation 对比

| 方案 | 协议 | 语言 | 状态 |
|:-----|:-----|:-----|:-----|
| browser_automation (内置) | Puppeteer/Playwright | Python + Node.js | 需手动启用 |
| browser-harness | CDP 直连 | Python | ✅ 推荐 |

**建议**：两套方案功能重叠，建议**二选一**，避免维护负担。

## 合规提醒

- 只用于你有权限的网站
- 遵守网站服务条款
- 禁止刷票、薅羊毛、批量注册假号等违法行为

## 冷知识

- 整个项目仅 592 行 Python 代码
- AI 每次成功都会自动生成 domain-skills，越用越聪明
- 支持后台 daemon 模式，多浏览器并行

## 相关链接

- [[Hermes_Agent.md]]
- [[browser-harness]]
- [[Agent 浏览器自动化 Chrome DevTools MCP 接入实战.md]]

## 来源

- GitHub: https://github.com/browser-use/browser-harness
- 微信公众号文章
