---
title: Agnes Video V2.0 API 官方文档
source: 微信公众号
url: https://agnes-ai.com/doc/agnes-video-v20
date: 2026-06-02
status: compiled
type: article
category: 方法
tags: [公众号文章, 2026-06-02抓取]
confidence: medium
---

# Agnes Video V2.0 API 官方文档

> 来源: 微信公众号
原文链接: https://agnes-ai.com/doc/agnes-video-v20
> 抓取时间: 2026-06-02

## 核心要点

- - 文本到视频（从文本提示词直接生成视频）
- - 图像到视频（将静态图像动画化为动态视频）
- - 多图像视频（使用多张参考图像引导生成）
- - 关键帧动画（生成多个关键帧之间的平滑过渡）
- - 场景运动控制（通过提示词控制主体移动、镜头运动、动态效果）
- - 视觉一致性（保持主体、风格、场景跨帧连贯性）
- 1. **创建任务**：POST 请求 → 收到 `task_id`
- 2. **轮询结果**：GET 请求 + `task_id` → 获取状态、进度、最终视频 URL
- - name: apihub.agnes-video.ai

## 原始内容

---
title: Agnes Video V2.0 API 官方文档
source: agnes-ai.com
url: https://agnes-ai.com/doc/agnes-video-v20
date: 2026-06-02
status: inbox
type: article
tags: [agnes, api, video, model]
category: API
---

# Agnes Video V2.0 官方文档摘要

## 概述
Agnes Video V2.0 是 Sapiens AI 推出的新一代视频生成模型，在 Artificial Analysis 视频排行榜中位居 Top 10。支持文本到视频、图像到视频、多图像视频和关键帧动画。

## 能力特性
- 文本到视频（从文本提示词直接生成视频）
- 图像到视频（将静态图像动画化为动态视频）
- 多图像视频（使用多张参考图像引导生成）
- 关键帧动画（生成多个关键帧之间的平滑过渡）
- 场景运动控制（通过提示词控制主体移动、镜头运动、动态效果）
- 视觉一致性（保持主体、风格、场景跨帧连贯性）
- 电影级输出（高保真、专业的视频内容）

## ⚠️ 重要：异步 API 模式（非标准 OpenAI 格式）

与文本/图像模型不同，视频 API 采用**异步任务模式**：

### 端点
| 操作 | 方法 | 端点 |
|------|------|------|
| 创建任务 | POST | `https://apihub.agnes-ai.com/v1/videos` |
| 查询结果 | GET | `https://apihub.agnes-ai.com/v1/videos/{task_id}` |

### 工作流程
1. **创建任务**：POST 请求 → 收到 `task_id`
2. **轮询结果**：GET 请求 + `task_id` → 获取状态、进度、最终视频 URL

### 请求参数（创建任务）
| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `model` | string | 是 | 固定为 `agnes-video-v2.0` |
| `prompt` | string | 是 | 视频描述 |
| `image` | string/array | 否 | 输入图片URL(s) |
| `mode` | string | 否 | 生成模式（如 `ti2vid`、`keyframes`）|
| `height` | integer | 否 | 默认 768 |
| `width` | integer | 否 | 默认 1152 |
| `num_frames` | integer | 否 | ≤ 441 且满足 8n+1（如 81、121、161、241、441）|
| `num_inference_steps` | integer | 否 | 推理步数 |
| `seed` | integer | 否 | 随机种子 |
| `frame_rate` | number | 否 | 1-60 |
| `negative_prompt` | string | 否 | 禁止内容 |
| `extra_body.image` | array | 否 | 多图像/关键帧模式的图片URL数组 |
| `extra_body.mode` | string | 否 | 额外模式设置（如 `keyframes`）|

## 注意（2026-06-02 配置修复记录）
当前 Hermes 配置中，`apihub.agnes-video.ai` 被错误地配置为标准聊天 completions provider：
```yaml
- name: apihub.agnes-video.ai
  base_url: https://apihub.agnes-ai.com/v1
  model: agnes-video-v2.0
```
实际上视频 API 使用异步端点 `/v1/videos`，请求体完全不同（非 `messages` 格式）。
**已修复**：移除该 provider，后续通过 Gateway media 端点或专用脚本处理视频生成。
