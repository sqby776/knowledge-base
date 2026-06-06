---
title: browser-harness - AI 浏览器自动化工具
created: 2026-05-26
tags: [browser-harness, 浏览器自动化, AI工具, Hermes集成, CDP]
status: draft
sources: [https://github.com/browser-use/browser-harness]
---

# browser-harness - AI 浏览器自动化工具

## 概述

**browser-harness** 是一个超级轻量、自愈式的浏览器遥控器，通过 Chrome DevTools Protocol（CDP）直接连接本地 Chrome 浏览器，让 AI 像真人一样操作浏览器。

| 特性 | 说明 |
|------|------|
| 代码量 | 仅 592 行 Python |
| 协议 | Chrome DevTools Protocol (CDP) |
| 依赖 | 无需 Selenium/Playwright |
| 自愈性 | 页面改版时 AI 自动修复代码 |
| 自进化 | 任务成功自动生成 domain-skills |

## 核心优势

1. **真实浏览器控制**：直接操作本地 Chrome，非模拟
2. **自愈式设计**：按钮位置变化时 AI 自动修改代码
3. **零重型框架**：不依赖 Selenium/Playwright
4. **与 Hermes 深度集成**：Hermes 负责决策学习，browser-harness 负责执行

## 部署路径

### 前置条件
- Google Chrome（最新版）
- Python 3.11+
- uv 包管理器

### 关键配置
Chrome 远程调试必须启用：`chrome://inspect/#remote-debugging` → "Enable remote debugging"

### 多平台部署
| 平台 | 难度 | 备注 |
|------|------|------|
| macOS | ⭐ 最简单 | git clone + uv install |
| Linux | ⭐⭐ | 需安装 chromium-browser |
| WSL | ⭐⭐⭐ | 需配置 GUI 支持 |
| Termux | ⭐⭐⭐⭐ | 官方不支持 |

## 与 Hermes Agent 集成

### 注册流程
```bash
mkdir -p ~/.hermes/skills/browser-harness
ln -sf ~/browser-harness/SKILL.md ~/.hermes/skills/browser-harness/SKILL.md
ln -sf ~/browser-harness/interaction-skills ~/.hermes/skills/browser-harness/interaction-skills
ln -sf ~/browser-harness/domain-skills ~/.hermes/skills/browser-harness/domain-skills
```

### 测试指令
- "用 browser-harness 打开百度首页，搜索 browser-harness 并截图给我"
- "用 browser-harness 打开 GitHub trending，总结前 5 个最火的仓库"

## 应用场景

| 类别 | 具体用途 |
|------|----------|
| 生产力 | 竞品监控、价格查询、表单填写、邮件发送 |
| 内容运营 | GitHub Trending、社媒批量发帖 |
| 电商 | 领券、下单监控、评论回复 |
| 办公 | OA 系统登录、日报填写、数据抓取 |

## 合规提醒

⚠️ **重要**：只用于有权限的网站，遵守服务条款。禁止刷票、薅羊毛、批量注册等行为。

## 相关资源

- GitHub: https://github.com/browser-use/browser-harness
- 官方文档: 项目内 README
- Hermes 集成指南: 本文档


> **补充来源**: [2026-05-26_browser-harness 完整部署指南.md](../01-收件箱/文章/2026-05-26_browser-harness 完整部署指南.md)

## 新增要点

- browser-harness 完整部署指南
- 1. 更新系统
- 2. 安装依赖
- 3. 安装 uv
- 4. 安装 browser-harness


> **补充来源**: [2026-05-26_browser-harness 完整部署指南.md](../01-收件箱/文章/2026-05-26_browser-harness 完整部署指南.md)

## 新增要点

- browser-harness 完整部署指南
- 1. 更新系统
- 2. 安装依赖
- 3. 安装 uv
- 4. 安装 browser-harness
