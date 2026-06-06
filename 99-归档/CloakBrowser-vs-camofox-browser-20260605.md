---
title: CloakBrowser vs camofox-browser：反检测浏览器选型对比
created: 2026-06-05
tags: [反检测浏览器, CloakBrowser, camofox, Camoufox, 反爬, AI代理]
status: draft
sources: ["https://mp.weixin.qq.com/s/byJX2o2aewnbGOv61Gg5wA"]
source_url: https://mp.weixin.qq.com/s/byJX2o2aewnbGOv61Gg5wA
author: 未知
category: articles
---

# CloakBrowser vs camofox-browser：反检测浏览器选型对比

## 核心观点

标准自动化（Playwright/Puppeteer）的问题不是脚本不够像人，而是浏览器本身在出卖自动化身份（CDP 痕迹、navigator.webdriver、指纹）。JS 级补丁不够，需要 **C++ 源码级修改**。

## CloakBrowser：反检测之王

- Chromium 146 基础，23k+ Star，MIT 协议
- 58 个 C++ 补丁覆盖 Canvas、WebGL、Audio、字体、GPU、屏幕分辨率、WebRTC、网络时序、CDP 输入
- **直接替代 Playwright/Puppeteer**：`pip install cloakbrowser`，API 兼容
- **Humanize 模式**：贝塞尔曲线鼠标运动、键盘时序偏差、随机滚动，reCAPTCHA v3 得分 0.9
- 支持 Headless（批量抓取）和 Headed（调试）
- 自带 GUI Manager 管理多 profile、Cookie、localStorage、代理

## camofox-browser：AI Agent 浏览器

- 基于 Camoufox（Firefox fork）+ C++ 指纹修改，6k+ Star，MIT 协议
- **面向 AI Agent 而非人式爬虫**
- 使用 Accessibility Snapshots（保留语义，页面缩小 90%）
- 稳定元素引用（e1, e2, e3...），不随 CSS/HTML 变化失效
- **空闲内存 ~40MB**，适合树莓派、廉价 VPS
- REST API 接口，不支持 DOM 操作
- 内置搜索宏（@google_search, @youtube_search）

## 选型对比

| 维度 | CloakBrowser | camofox-browser |
|------|-------------|-----------------|
| 引擎 | Chromium 146 | Firefox (Camoufox) |
| 反检测 | 58 C++ 补丁 | C++ 指纹修改 |
| 目标 | 通过反爬检测（人式） | AI Agent 高效控制 |
| API | Playwright/Puppeteer | REST API |
| 交互 | DOM 操作 | 语义快照 + 引用 |
| 内存 | 标准 Chromium | ~40MB 空闲 |
| 安装 | pip / npm | Docker / npm |

## 选型建议

- **CloakBrowser**：构建爬虫/自动化测试、需要绕过 Cloudflare Turnstile/reCAPTCHA/FingerprintJS、偏好 Playwright 工作流
- **camofox-browser**：构建 AI Agent 浏览器、需要语义快照而非脆弱 DOM 选择器、资源有限、需要多实例并行

## 与现有工具链对比

我们的工具链中：
- Camoufox 对应 camofox-browser 的引擎部分，但缺少 camofox-browser 的 REST API + 语义快照
- Scrapling StealthyFetcher 需要 Playwright Chromium，目前 Ubuntu 26.04 不支持

CloakBrowser 是目前我们没有的反检测方案——基于 Chromium、58 个 C++ 补丁、reCAPTCHA 0.9 分。
