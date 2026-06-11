---
title: Hermes Agent Profile 创建与使用指南
source: 微信公众号
url: https://mp.weixin.qq.com/s/cZEBk8761AHmA7Mnxu_4FQ
date: 2026-06-02
status: compiled
type: article
category: 方法
tags: [公众号文章, 2026-06-01抓取]
---

# Hermes Agent Profile 创建与使用指南

> 来源: 微信公众号
原文链接: {url}
> 抓取时间: 2026-06-01

## 核心要点

- - 网关状态（gateway state）
- - **Hermes Agent 的 Windows 版本支持创建独立智能体（Profile）**
- - 原生 Windows 支持是 **2026年5月** 才加入的功能
- 1. **每日定时搜索**：每天早上 9 点，使用 DuckDuckGo 搜索国内 AI 新闻
- 2. **多源聚合**：从以下渠道获取新闻：
- 3. 如果遇到 CAPTCHA 验证，直接跳过，换下一个新闻渠道
- 4. **智能去重**：只显示今天发布的新闻，同一事件只保留最早或最权威的来源
- 5. **结构化输出**：每条新闻包含标题、摘要、来源链接、发布时间

## 原始内容

---
title: Hermes Agent Profile 创建与使用指南
source: 微信公众号
url: https://mp.weixin.qq.com/s/cZEBk8761AHmA7Mnxu_4FQ
date: 2026-06-01
status: inbox
type: article
category: Hermes系统
tags: [公众号文章, 2026-06-01抓取]
---

---
title: Hermes Agent 独立智能体 Profile 创建与使用指南
created: 2026-06-01
updated: 2026-06-01
tags: ["hermes", "profile", "agent", "tutorial"]
status: active
sources: [https://mp.weixin.qq.com/s/V-pJUnnGC9hDPp0Cyc3lGw]
---

# Hermes Agent 独立智能体 Profile 创建与使用指南

> 来源：微信公众号

## 一、Profile 概述

**Profile 是 Hermes 的独立智能体目录**，每个 Profile 拥有完全隔离的：

- `config.yaml`（配置）
- `.env`（API 密钥）
- `SOUL.md`（人格/个性）
- 记忆（memories）
- 会话历史（sessions）
- 技能（skills）
- 定时任务（cron jobs）
- 网关状态（gateway state）

> ⚠️ **重要特性**：创建 Profile 后，会自动生成同名命令，例如创建 `daily_ai_news` 后，拥有 `daily_ai_news chat`、`daily_ai_news setup`、`daily_ai_news gateway start` 等命令

---

## 二、Windows 版本注意事项

### 支持情况
- **Hermes Agent 的 Windows 版本支持创建独立智能体（Profile）**
- 原生 Windows 支持是 **2026年5月** 才加入的功能

### 常见问题排查

| 问题 | 可能原因 | 解决方案 |
|------|----------|----------|
| `hermes profile create` 报错 | 版本过旧 | 运行 `hermes update` 更新 |
| 路径问题 | 安装位置不同 | 原生版：`%LOCALAPPDATA%\hermes`，WSL2版：`~/.hermes` |
| 命令未生效 | 环境变量未刷新 | 重启 PowerShell 或执行 `refreshenv` |

---

## 三、创建智能体详细步骤

### 步骤 1：创建空白 Profile

```bash
hermes profile create daily_ai_news --description "每日 AI 新闻聚合，使用免费搜索和浏览器抓取国内新闻源"
```

**命名规则**：
- ✅ 小写字母、数字、下划线
- ❌ 禁止空格和大写

**创建后输出**：
```
Profile 'daily_ai_news' created at C:\Users\xiao\AppData\Local\hermes\profiles\daily_ai_news
Next steps:
  daily_ai_news setup      Configure API keys and model
  daily_ai_news chat       Start chatting
  daily_ai_news gateway start  Start the messaging gateway
⚠ This profile has no API keys yet. Run 'daily_ai_news setup' first
```

### 步骤 2：切换到该 Profile

```bash
hermes profile use daily_ai_news
```

### 步骤 3：运行配置向导

```bash
hermes -p daily_ai_news setup
```

**配置向导选项**：

| 选项 | 说明 |
|------|------|
| 1 | Quick setup — provider, model & messaging（推荐） |
| 2 | Full setup — configure everything |

**推理提供商选择**（部分示例）：

```
(●)  1. Nous Portal (Nous Research subscription)
(○)  2. OpenRouter (100+ models, pay-per-use)
(○)  3. NovitaAI (AI-native cloud)
(○)  4. LM Studio (local desktop app with built-in model server)
(○)  5. Anthropic (Claude models)
(○)  6. OpenAI Codex
(○)  7. Qwen Cloud / DashScope Coding
(○)  8. xAI Grok OAuth
(○)  9. Xiaomi MiMo
(○) 10. Tencent TokenHub
...（共 38+ 选项）
```

**终端后端选择**：

```
(○)  1. Local - run directly on this machine (default)
(○)  2. Docker - isolated container with configurable resources
(○)  3. Modal - serverless cloud sandbox
(○)  4. SSH - run on a remote machine
(○)  5. Daytona - persistent cloud development environment
(○)  6. Vercel Sandbox - cloud microVM
(●)  7. Keep current (local)
```

**消息平台**：可选择跳过，后续用 `hermes setup gateway` 配置

### 步骤 4：配置 SOUL.md（中文人格）

**文件路径**：
```
C:\Users\xiao\AppData\Local\hermes\profiles\daily_ai_news\SOUL.md
```

**核心职责配置**：

```markdown
# 新闻助手人格
你是一个专业的 AI 新闻聚合助手，专注于收集和整理国内 AI 领域的最新动态。

## 核心职责
1. **每日定时搜索**：每天早上 9 点，使用 DuckDuckGo 搜索国内 AI 新闻
2. **多源聚合**：从以下渠道获取新闻：
   - 知乎 AI 话题
   - 36 氪 AI 板块
   - 机器之心
   - 量子位
   - 极客公园
   - 虎嗅 AI
   - CSDN AI 专栏
3. 如果遇到 CAPTCHA 验证，直接跳过，换下一个新闻渠道
4. **智能去重**：只显示今天发布的新闻，同一事件只保留最早或最权威的来源
5. **结构化输出**：每条新闻包含标题、摘要、来源链接、发布时间
6. **分类标签**：Research（研究）、Product（产品）、Policy（政策）、Funding（融资）
```

**新闻源配置表**：

| 网站 | URL | 编码 | 抓取方式 |
|------|-----|------|----------|
| 机器之心 | jiqizhixin.com | UTF-8 | browser_navigate |
| 量子位 | qbitai.com | UTF-8 | browser_navigate |
| 36 氪 | 36kr.com | UTF-8 | browser_navigate |
| 虎嗅 | huxiu.com | UTF-8 | browser_navigate |
| 极客公园 | geekpark.net | UTF-8 | browser_navigate |
| 知乎 | zhihu.com | GBK | Python 脚本 |
| CSDN | csdn.net | UTF-8/GBK | Python 脚本备用 |

**编码处理规则**：
1. 优先使用 UTF-8 网站
2. 404 错误跳过该源
3. GBK 编码网站使用 Python 脚本抓取并转码

**Python 抓取脚本模板**：
```python
import urllib.request
import sys

url = "目标 URL"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
req = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(req)
html_bytes = response.read()

# 尝试 UTF-8
try:
    html = html_bytes.decode('utf-8')
    print("UTF-8 解码成功")
except UnicodeDecodeError:
    # 回退到 GBK
    html = html_bytes.decode('gbk', errors='ignore')
    print("GBK 解码成功")

print(html[:10000])  # 输出前 10000 字符
```

**输出格式模板**：
```markdown
📰 今日 AI 新闻汇总（YYYY-MM-DD）
🔬 研究动态（X 条）
• [标题] — 来源 | 时间
  摘要：...
  链接：https://...
  分类：Research

🚀 产品发布（X 条）
📋 政策法规（X 条）
💰 融资动态（X 条）

📊 统计：共收集 X 条新闻
🔍 数据来源：...
⏰ 生成时间：HH:MM
```

### 步骤 5：安装 Skills

```bash
hermes -p daily_ai_news skills install official/research/duckduckgo-search
```

> **duckduckgo-search**：免费网页搜索，无需 API Key，社区使用频率很高

---

## 四、验证和测试

### 进入聊天模式

```bash
hermes -p daily_ai_news chat
```

### 测试指令

```
搜索'AI 人工智能 今日新闻'，抓取前 10 条结果，按分类整理成日报，必须严格按照格式输出
```

### 输出示例

```
📰 AI 人工智能今日新闻汇总（2026-05-25）

🔬 研究动态（8 条）
• [DeepSeek V4 还能更省！新工具缓存命中率高达 99.82%，2 折稳定到手] — 量子位 | 2026/05/24
  摘要：DeepSeek V4 推出新的推理优化工具，通过智能缓存机制将重复请求的处理效率提升至 99.82%
  链接：https://www.qbitai.com/
  分类：Research

• [蚂蚁灵波 LingBot-VA 论文被机器人顶会 RSS 2026 接收] — 量子位 | 2026/05/24
  摘要：阿里巴巴达摩院蚂蚁灵波团队研发的多模态推理模型 LingBot-VA 获得国际顶级会议 RSS 2026 接收
  链接：https://www.qbitai.com/
  分类：Research

🚀 产品发布（4 条）
• [小米 YU7 GT 发布，38.99 万元] — 极客公园 | 2026/05/24
  摘要：雷军亲自打造的 YU7 GT 车型正式上市，定价 38.99 万元
  链接：https://www.geekpark.net/
  分类：Product

💰 融资动态（5 条）
• [华为具身大脑一号位创业，获亿元级融资] — 量子位 | 2026/05/24
  摘要：前华为具身智能技术负责人创立新公司，专注于基于认知科学的具身世界模型研究
  链接：https://www.qbitai.com/
  分类：Funding

📊 统计：共收集 17 条新闻
```

---

## 五、Profile 管理命令

| 命令 | 说明 |
|------|------|
| `hermes profile list` | 列出所有 Profile |
| `hermes profile create <name>` | 创建新 Profile |
| `hermes profile use <name>` | 切换到指定 Profile |
| `hermes profile delete <name>` | 删除 Profile |
| `hermes -p <name> chat` | 进入指定 Profile 的聊天模式 |
| `hermes -p <name> setup` | 运行指定 Profile 的配置向导 |

---

## 六、多 Profile 协作场景

### 场景 1：新闻聚合 + 内容创作

```
daily_ai_news (research profile) → 收集新闻 → 推送给 content_writer
content_writer (general profile) → 撰写文章 → 发布到公众号
```

### 场景 2：代码审查 + 开发

```
reviewer (reviewer profile) → 审查代码 → 提交 PR
coder (coding profile) → 根据审查意见修改代码
```

### 场景 3：定时任务 + 即时响应

```
daily_report (worker profile) → 每天 9 点生成日报
assistant (default profile) → 即时响应用户聊天
```

---

## 相关链接

- [[Hermes_Agent.md]]
- [[Hermes Agent Profile 创建与使用指南.md]]
- [[HermesSkills效率翻倍指南.md]]
- [[Cron 定时任务]]

## 来源

- 微信公众号文章
