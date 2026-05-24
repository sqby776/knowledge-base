---
title: Camoufox
created: 2026-05-24
updated: 2026-05-24
tags: ["tool", "automation"]
status: active
sources: []
---

# Camoufox

## 定义

Camoufox — 基于 Firefox 的网页抓取工具，专为绕过反爬虫机制设计，支持重度 JavaScript 渲染页面。

## 核心特点

| 特点 | 说明 |
|:-----|:-----|
| **反检测** | 模拟真实浏览器指纹，绕过 Cloudflare 等反爬 |
| **JS 渲染** | 完整执行 JavaScript，获取动态内容 |
| ** stealth 模式** | 隐藏自动化特征，避免被识别为机器人 |

## 技术架构

```
Camoufox
    ↓
Firefox (Gecko 引擎)
    ↓
CDP (Chrome DevTools Protocol)
    ↓
网页内容提取
```

## 使用场景

| 场景 | 适用性 |
|:-----|:-----|
| 微信公众号文章 | ⭐⭐⭐⭐⭐ |
| 社交媒体（X/Twitter） | ⭐⭐⭐⭐⭐ |
| 电商网站 | ⭐⭐⭐⭐ |
| 新闻网站 | ⭐⭐⭐⭐ |
| 静态页面 | ⭐⭐（建议用 scrapling） |

## 安装配置

```bash
pip install camoufox
```

## 与 crawl4ai 对比

| 维度 | Camoufox | crawl4ai |
|:-----|:-----|:-----|
| **反爬能力** | 强 | 中 |
| **速度** | 慢（浏览器启动） | 快 |
| **JS 支持** | 完整 | 完整 |
| **资源消耗** | 高 | 中 |

## 相关链接

- [[crawl4ai]]
- [[scrapling]]
- [[web-scraping]]

## 来源

- Camoufox 官方文档
- 本系统实际使用经验

---

> [!NOTE] 待验证
> 具体配置参数需根据实际使用调整
