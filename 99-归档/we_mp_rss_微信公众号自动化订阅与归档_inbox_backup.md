# 分享一个我原创的小工具：让你的 Agent 从此搜索不花钱

作者：段诗闻

（这篇文章实际上讲的是 we-mp-rss 这个工具）

## 核心问题

微信公众号内容没有 RSS/API，导致信息过载时容易错过有价值的内容，AI Agent 也难以自动处理。

## we-mp-rss 解决方案

自托管工具，将微信公众号内容转化为标准 RSS 或 PDF/Word/HTML 文件。

### 核心功能

- **RSS 生成** — 订阅公众号后生成标准 RSS feed
- **多格式导出** — PDF（推荐，保留格式）、Word、HTML
- **Agent 集成** — 通过 RSS 喂给 Agent，或通过 Access Key 让 Agent 自主调用 API
- **无需手动抓 Cookie** — 用微信公众号后台扫码授权

### 部署方式（Docker）

```yaml
services:
  werss:
    image: rachelos/we-mp-rss:latest
    ports:
      - "8001:8001"
    volumes:
      - /share/Container/werss:/app/data
    restart: unless-stopped
```

默认登录：admin / admin@123

### 使用流程

1. 打开 Web UI，微信扫码授权
2. 订阅管理 → 搜索公众号 → 添加
3. 主页 → 导出 → 选 PDF
4. 或生成 RSS Link 集成到 RSS 阅读器 / Agent

### 终极知识库工作流

1. 公众号更新 → we-mp-rss 检测到新文章
2. 生成 RSS 或 PDF
3. Hermes Agent 获取文章 → 下载 PDF → 可选做 Embedding
4. LLM 生成摘要 → 飞书推送通知

## 评价

**价值判断：这是我们目前最缺的能力。** 我们之前一直用 web_extract 抓取微信公众号，但：
- 会触发验证码，无法稳定抓取
- 需要每次都手动发链接过来
- 无法自动监控新文章

we-mp-rss 通过公众号后台授权方式，从根本上绕过了反爬问题。而且支持 RSS，可以无缝接入我们的自动化流程。

**唯一限制**：需要 Docker 环境来部署。
