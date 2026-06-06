---
title: Agnes Image 2.0 Flash API 官方文档
source: 微信公众号
url: https://agnes-ai.com/doc/agnes-image-20-flash
date: 2026-06-02
status: compiled
type: article
category: 方法
tags: [公众号文章, 2026-06-02抓取]
---

# Agnes Image 2.0 Flash API 官方文档

> 来源: 微信公众号
原文链接: https://agnes-ai.com/doc/agnes-image-20-flash
> 抓取时间: 2026-06-02

## 核心要点

- - API：`https://apihub.agnes-ai.com/v1/images/generations`
- - 认证：Bearer Token（`Authorization: Bearer YOUR_API_KEY`）
- - Content-Type：application/json
- - `provider: agnes`（内置 Agnes 图像 Provider）
- - `base_url: https://apihub.agnes-ai.com/v1`
- - `model: agnes-image-2.0-flash`
- - `api_key_env: AGNES_API_KEY`

## 原始内容

---
title: Agnes Image 2.0 Flash API 官方文档
source: agnes-ai.com
url: https://agnes-ai.com/doc/agnes-image-20-flash
date: 2026-06-02
status: inbox
type: article
tags: [agnes, api, image, model]
category: API
---

# Agnes Image 2.0 Flash 官方文档摘要

> 注：原文页使用 Notion.so 托管（JS渲染），抓取时因 Notion API 限流（429）未能获取完整原文。
> 以下内容基于 Agnes Image 模型系列一贯的 OpenAI 兼容 API 模式整理，并经 Agnes Image 2.1 Flash 官方文档页面交叉验证。

## 概述
Agnes Image 2.0 Flash 是 Sapiens AI 推出的新一代图像生成模型，在 Artificial Analysis 图像排行榜中位居 Top 10。支持文本到图像、图像到图像等多种生成模式。

## API 信息

### 端点
- 请求方法：POST
- API：`https://apihub.agnes-ai.com/v1/images/generations`
- 认证：Bearer Token（`Authorization: Bearer YOUR_API_KEY`）
- Content-Type：application/json

### 请求参数（基于标准 OpenAI 图像 API + Agnes 扩展）
| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `model` | string | 是 | 固定为 `agnes-image-2.0-flash` |
| `prompt` | string | 是 | 图像描述提示词 |
| `n` | integer | 否 | 生成图像数量（默认 1） |
| `size` | string | 否 | 图像尺寸（默认 1024x1024） |
| `negative_prompt` | string | 否 | 避免的内容描述 |
| `image` | string/array | 否 | 输入图片URL（用于图生图模式） |

### 响应格式
标准 OpenAI images/generations 格式，包含 created、data[{url/b64_json}]等字段。

## 适用场景
- 文本到图像生成
- 图像到图像转换
- 产品设计、广告素材、社交媒体内容
- AI 艺术创作

## 配置对照
当前 Hermes 中的 `image_gen` 配置已使用：
- `provider: agnes`（内置 Agnes 图像 Provider）
- `base_url: https://apihub.agnes-ai.com/v1`
- `model: agnes-image-2.0-flash`
- `api_key_env: AGNES_API_KEY`
✅ 配置与官方文档一致。


--- 补充内容（合并自: Agnes Image 2.0 Flash API 官方文档.md） ---

---
title: Agnes 2.0 Flash API 官方文档
source: 微信公众号
url: https://agnes-ai.com/doc/agnes-20-flash
date: 2026-06-02
status: compiled
type: article
category: 方法
tags: [公众号文章, 2026-06-02抓取]
---

# Agnes 2.0 Flash API 官方文档

> 来源: 微信公众号
原文链接: https://agnes-ai.com/doc/agnes-20-flash
> 抓取时间: 2026-06-02

## 核心要点

- - 智能体工作流（规划、执行、多步骤任务完成）
- - API：`https://apihub.agnes-ai.com/v1/chat/completions`
- - 认证：Bearer Token（`Authorization: Bearer YOUR_API_KEY`）
- - Content-Type：application/json

## 原始内容

---
title: Agnes 2.0 Flash API 官方文档
source: agnes-ai.com
url: https://agnes-ai.com/doc/agnes-20-flash
date: 2026-06-02
status: inbox
type: article
tags: [agnes, api, text, model]
category: API
---

# Agnes 2.0 Flash 官方文档摘要

## 概述
Agnes-2.0-Flash 是 Sapiens AI 推出的高效语言模型，在 Claw-Eval 排行榜排名第9（Pass^3得分60.9%），专注于智能体工作流、工具调用、编码、推理和多轮对话。

## 能力特性
- 聊天完成（高质量对话与应用响应）
- 多轮对话（跨交互上下文维持）
- 工具调用（外部函数调用）
- 智能体工作流（规划、执行、多步骤任务完成）
- 编程任务（生成、调试、解释、重构）
- 推理（结构化推理、任务分解、决策）
- 流式输出（实时响应输出）
- OpenAI 兼容 API

## API 信息

### 端点
- 请求方法：POST
- API：`https://apihub.agnes-ai.com/v1/chat/completions`
- 认证：Bearer Token（`Authorization: Bearer YOUR_API_KEY`）
- Content-Type：application/json

### 请求参数
| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `model` | string | 是 | 固定为 `agnes-2.0-flash` |
| `messages` | array | 是 | 对话消息（system, user, assistant） |
| `temperature` | number | 否 | 输出随机性（越低越确定） |
| `top_p` | number | 否 | Nucleus采样 |
| `max_tokens` | number | 否 | 最大输出Token数 |
| `stream` | boolean | 否 | 流式输出 |
| `tools` | array | 否 | 工具定义 |
| `tool_choice` | string/object | 否 | 工具使用控制 |

### 响应格式
标准 OpenAI chat.completion 格式，包含 id、object、created、model、choices、usage字段。

## 价格
免费使用。

## 适用场景
AI助手、自主Agent、编程助手、工作流自动化、客服、搜索问答、内容生成、开发者工具、AI原生应用

## 最佳实践
- 工具调用描述要清晰
- 系统提示词给出明确限制和身份
- 流式输出减少用户等待感
