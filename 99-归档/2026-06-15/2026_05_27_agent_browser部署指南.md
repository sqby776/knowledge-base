---
title: 2026-05-27_agent-browser部署指南.md
created: 2026-05-30
updated: 2026-05-30
tags: [knowledge-base, auto-compiled]
status: draft
sources: [auto-capture]
---

# 2026-05-27_agent-browser部署指南.md

> [!INFO] 编译信息
> 来源: 自动抓取 | 编译时间: 2026-05-30 20:42 | 类型: entity

## 核心要点

- **从零到一，手把手教你部署 Hermes Agent 浏览器自动化引擎**
- **纯 Rust 编写**，底层走 CDP（Chrome DevTools Protocol）直连
- **精简无障碍树**替换 HTML 解析，上下文开销仅 **200-400 tokens**
- 每个元素带 `@eN` 编号，操作直接引用
- **等待元素出现**
- **等待特定文本**
- **等待 URL 变化**
- **等待网络空闲（SPA 万能钥匙）**
- **DOM 加载完成**
- **JavaScript 条件**

## 相关链接


## 来源

- 原始文章: 2026-05-27_agent-browser部署指南.md
