# Firecrawl — AI Agent 专用 Web 数据提取工具

> 来源: https://mp.weixin.qq.com/s/Vzyo2yjjfflZ9SwdUf07vw
> 日期: 2026-06-03
> 类型: 开源项目推荐
> GitHub Stars: 125K+

---

## 简介

Firecrawl 是一款专为 AI Agent 设计的 **Web 数据提取工具**，将任意 URL 变成 AI 应用可用的干净数据。

## 三大核心能力

| 能力 | 说明 |
|------|------|
| **Search** | 输入关键词，实时搜索全网并返回页面内容 |
| **Scrape** | 输入 URL，直接转成 Markdown / JSON / 截图 |
| **Crawl** | 给定一个网站，自动发现并抓取所有子页面 |

## 技术亮点

- **LLM-Ready**：输出干净、结构化、token 友好，AI 应用直接消费，无需二次清洗
- **智能渲染引擎**：自动处理 JS 重度页面，无需手动启动无头浏览器
- **代理池 + 速率限制**：内置轮换代理与并发控制，不怕被封
- **P95 延迟 3.4 秒**：全量场景下平均不到 4 秒返回结果
- **96% 网站覆盖率**：市面上少有的高成功率
- **多格式输出**：Markdown、HTML、JSON、元数据、截图一键切换
- **支持 Actions**：点击、滚动、输入、等待后再提取，真正模拟人类操作
- 开源版覆盖核心抓取能力，云端版额外提供 Agent 级智能交互与高级反爬绕过

## 应用场景

- **AI 搜索应用**：接入 Search API，快速构建支持实时网络回答的问答机器人
- **AI Agent 数据采集**：配合 MCP 协议，让 Claude Code、OpenCode 等 Agent 自主浏览网页、提取目标信息
- **竞品情报系统**：批量抓取竞品官网、文档、定价页面，结构化入库
- **知识库构建**：Crawl 整个文档站点，一次性转为 Markdown 语料库
- **PDF/DOCX 内容提取**：直接解析网络托管的文件内容

## 安装

```bash
pip install firecrawl-py
```

```python
from firecrawl import Firecrawl
app = Firecrawl(api_key="fc-YOUR_API_KEY")
doc = app.scrape("https://firecrawl.dev", formats=["markdown"])
print(doc.markdown)
```

Node.js 同样简洁：

```bash
npm install @mendable/firecrawl-js
```

```javascript
import Firecrawl from '@mendable/firecrawl-js';
const app = new Firecrawl({ apiKey: "fc-YOUR_API_KEY" });
const doc = await app.scrape('https://firecrawl.dev', { formats: ['markdown'] });
console.log(doc.markdown);
```

## 相关链接

- [GitHub](https://github.com/firecrawl/firecrawl)
- [官方文档](https://docs.firecrawl.dev)
- [Playground](https://firecrawl.dev/playground)
