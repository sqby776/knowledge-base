# Agnes-2.0-Flash: 免费使用 & 8大Agent工具集成指南

## 1. 产品概述
Agnes是多模态AI实验室，核心产品 Agnes-2.0-Flash 是免费开放的OpenAI兼容文本模型。

## 2. 模型能力与基准
- **文本** Agnes-2.0-Flash：在Claw-Eval（Agent专用基准）排名靠前，超过Gemini 3 Flash和MiniMax M2.7
- **图片** Agnes-Image-2.0-Flash：Artificial Analysis盲测基准，可与GPT Image竞争
- **视频** Agnes-Video-2.0：Artificial Analysis文生视频基准
- **综合排名**：多模态基准全球第9

## 3. 价格（免费前）
- 文本：$0.03/1M输入token，$0.15/1M输出token
- 图片：$3/1000张（竞品约$30）
- 视频：$0.30/分钟
- **当前状态：全部免费**

## 4. 接入信息
- **API Gateway**: `https://apihub.agnes-ai.com/v1`
- **API Key**: platform.agnes-ai.com 创建
- **文本模型名**: agnes-2.0-flash
- **连接类型**：
  1. 直接OpenAI兼容：OpenClaw, Hermes, WorkBuddy, Cherry Studio, Opencode, Codex++
  2. Anthropic协议需转换：Claude Code, Claude Desktop（需cc-switch）

## 5. 各工具接入步骤

### 5.1 OpenClaw (CLI)
```
openclaw config openclaw → Local → Model → Custom Provider
API Base URL: https://apihub.agnes-ai.com/v1
API Key: [你的Key]
Model: agnes-2.0-flash
```

### 5.2 HermesAgents (CLI)
```bash
hermes config set model.provider custom
hermes config set model.base_url https://apihub.agnes-ai.com/v1
hermes config set model.api_key YOUR_API_KEY
hermes config set model.default agnes-2.0-flash
```

### 5.3 WorkBuddy (桌面)
- 文本：Auto → Configure Custom Model → Other
- 接口地址：https://apihub.agnes-ai.com/v1
- 图片/视频：用Skills方式

### 5.4 Cherry Studio (桌面)
- 添加Provider → Type: OpenAI → Name: Agnes
- Base URL: https://apihub.agnes-ai.com/v1
- Fetch models → 选 agnes-2.0-flash

### 5.5 Opencode
文件: ~/.config/opencode/opencode.jsonc
配置provider agnes，baseURL和apiKey

### 5.6 Codex++ (第三方)
- Provider: Agnes
- Model: agnes-2.0-flash
- Base URL: https://apihub.agnes-ai.com/v1
- Upstream: Chat Completions

### 5.7 Claude Code / Claude Desktop
- Anthropic协议，需cc-switch转换
- 或使用官方Claude Code集成

### 5.8 Google Workspace
- 通过MCP或直接API调用

## 6. 图片生成（WorkBuddy Skills）
- 提示词："我想要使用Agnes Image 2.0模型生成图像，用Agnes Video V2.0生视频，访问它的API平台https://agnes-ai.com/doc/overview，并将它打包成两个Skills。"

## 7. 官方文档
- 首页: https://agnes-ai.com
- 文档: https://agnes-ai.com/doc/overview
- 平台: https://platform.agnes-ai.com/
