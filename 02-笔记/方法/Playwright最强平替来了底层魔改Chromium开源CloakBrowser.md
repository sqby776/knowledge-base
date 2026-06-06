---
title: [[Playwright]] 最强平替来了，底层魔改 Chromium 开源 — [[CloakBrowser]]
source: 微信公众号
url: https://mp.weixin.qq.com/s/cSiyubzxraNObBOguHW0IQ
date: 2026-06-02
status: compiled
type: article
category: 方法
tags: [公众号文章, 2026-06-02抓取]
---

# [[Playwright]] 最强平替来了，底层魔改 Chromium 开源 — [[CloakBrowser]]

> 来源: 微信公众号
原文链接: https://mp.weixin.qq.com/s/cSiyubzxraNObBOguHW0IQ
> 抓取时间: 2026-06-02

## 核心要点

- - 网站通过浏览器指纹、图形渲染、网络时序、自动化痕迹识别并拦截自动化工具
- - 传统 stealth 插件：运行时临时伪装，Chrome 升级后容易失效
- - undetected-chromedriver：继续和浏览器版本打补丁战
- - Canvas 图像绘制、WebGL 图形环境
- - `navigator.webdriver` 从 `true` → `false`
- - UA 不再泄露 `HeadlessChrome`
- - 通过 BrowserScan、FingerprintJS、Cloudflare Turnstile、reCAPTCHA v3 检测
- - CDP 事件隔离封装，不自写鼠标轨迹模拟器
- - 不同代理、不同持久会话、不同 cookie 和 localStorage
- - 容器启动后 `http://localhost:8080` 管理面板
- - 支持 `launch_persistent_context()` 保留 cookie/localStorage
- - 之前分析 29 篇公众号文章时 P3 推荐过 [[CloakBrowser]]（可选装）
- - 现在看到详细介绍，核心价值是源码级反检测，比 stealth 插件更长期
- - [[CloakBrowser]] = Chromium 源码改造（更稳定，维护成本低）
- - [[Camoufox]] = Firefox 改造 + Docker 部署（部署更复杂）
- - 与 Chrome DevTools MCP 对比：
- - [[CloakBrowser]] 解决"不被检测"
- - 安装：pip install cloakbrowser（仅 Linux x86_64）
- - 当前 [[Playwright]] 后端够用，但如果遇到 Cloudflare/fingerprintJS 拦截时可以换

## 原始内容

---
title: [[Playwright]] 最强平替来了，底层魔改 Chromium 开源 — [[CloakBrowser]]
source: 微信公众号（摸鱼挖开源）
url: https://mp.weixin.qq.com/s/cSiyubzxraNObBOguHW0IQ
date: 2026-06-02
status: inbox
type: article
tags: [cloakbrowser, chromium, anti-detection, playwright, puppeteer, automation]
category: 浏览器自动化
---

# [[Playwright]] 最强平替来了，底层魔改 Chromium 开源 — [[CloakBrowser]]（摘要）

## 核心定位
[[CloakBrowser]] — 改过 Chromium 源码的浏览器二进制 + [[Playwright]]/Puppeteer 薄封装，让自动化脚本看起来像正常人在用浏览器。

开源地址：https://github.com/CloakHQ/[[CloakBrowser]]

## 解决的核心问题
- 网站通过浏览器指纹、图形渲染、网络时序、自动化痕迹识别并拦截自动化工具
- 传统 stealth 插件：运行时临时伪装，Chrome 升级后容易失效
- undetected-chromedriver：继续和浏览器版本打补丁战

## 三大核心能力

### 1. 源码级反检测
不是表面配置，而是 Chromium 源码级补丁，覆盖多项检测面：
- Canvas 图像绘制、WebGL 图形环境
- 音频指纹、字体、GPU、屏幕信息
- WebRTC、网络 timing
- 自动化信号、CDP 输入行为
- `navigator.webdriver` 从 `true` → `false`
- UA 不再泄露 `HeadlessChrome`
- 通过 BrowserScan、FingerprintJS、Cloudflare Turnstile、reCAPTCHA v3 检测

### 2. Humanize 行为模拟
`humanize=True` 配置开关：
- 鼠标贝塞尔曲线轨迹（不是直线）
- 逐字符输入节奏（不是瞬间完成）
- 真实滚动模式（不是匀速）
- CDP 事件隔离封装，不自写鼠标轨迹模拟器

### 3. Browser Profile Manager（对标 Multilogin）
- 自托管浏览器画像管理器
- 不同代理、不同持久会话、不同 cookie 和 localStorage
- 容器启动后 `http://localhost:8080` 管理面板
- noVNC 远程操作
- 支持 `launch_persistent_context()` 保留 cookie/localStorage

## 与传统方案对比

| 维度 | stealth 插件 | undetected-chromedriver | [[CloakBrowser]] |
|------|-------------|------------------------|-------------|
| 伪装层级 | 运行时 JS 注入 | 驱动层补丁 | 浏览器源码级 |
| 稳定性 | Chrome 升级后失效 | Chrome 升级后失效 | 相对稳定 |
| 行为模拟 | 需额外工具 | 需额外工具 | 内置 humanize |
| Profile 管理 | 无 | 无 | 内置（对标 Multilogin） |
| 维护成本 | 高（不断打补丁） | 高（不断打补丁） | 低（源码级） |
| 迁移成本 | 低 | 中 | 低（[[Playwright]]/Puppeteer 兼容） |

## 不足之处
- 生产环境观测失败原因不够
- 版本升级回滚机制不清晰
- 站点级对抗定位文档不足
- 个人折腾 OK，团队落地需补验证

## 对当前系统的参考价值
- 之前分析 29 篇公众号文章时 P3 推荐过 [[CloakBrowser]]（可选装）
- 现在看到详细介绍，核心价值是源码级反检测，比 stealth 插件更长期
- 与 [[Camoufox]] 对比：
  - [[CloakBrowser]] = Chromium 源码改造（更稳定，维护成本低）
  - [[Camoufox]] = Firefox 改造 + Docker 部署（部署更复杂）
- 与 Chrome DevTools MCP 对比：
  - [[CloakBrowser]] 解决"不被检测"
  - MCP 解决"复用登录态"
  - 两者互补，不冲突
- 安装：pip install cloakbrowser（仅 Linux x86_64）
- 当前 [[Playwright]] 后端够用，但如果遇到 Cloudflare/fingerprintJS 拦截时可以换