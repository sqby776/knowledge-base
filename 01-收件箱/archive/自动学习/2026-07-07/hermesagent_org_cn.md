# Hermes Agent 中文社区 FAQ

> 提取时间：2026-07-06_16-03-16

## 知识点摘要

### [LLM 提供商] 支持哪些模型提供商

支持任何兼容 OpenAI 的 API。包括：OpenRouter(推荐灵活性)、Nous Portal(推荐新用户，一次 OAuth 300+模型)、OpenAI(GPT-5.4/GPT-5-codex/GPT-4.1/GPT-4o)、Anthropic(Claude 系列)、Google(Gemini)、z.ai/GML(智谱AI)、Kimi/Moonshot、MiniMax(全球和中国端点)、本地模型(Ollama/vLLM/llama.cpp/SGLang)

### [平台支持] Win/Android/Termux 支持

完整的平台可用性矩阵见 Platform Support 文档

### [WSL2 浏览器] WSL2 中控制 Windows Chrome

推荐使用 MCP 桥接而非 /browser connect。在 WSL2 内运行 Hermes，在 Windows 使用正常 Chrome，通过 chrome-devtools-mcp 添加为 MCP 服务器

### [数据隐私] 数据不会外泄

API 调用仅发送到配置的 LLM 提供商。Hermes Agent 不收集遥测数据、使用数据或分析数据。对话、记忆和技能都本地存储在 ~/.hermes/ 中

### [离线使用] 支持离线/本地模型

可运行 `hermes model` 选择 Custom endpoint 并输入本地服务器 URL。示例配置：qwen3.5:27b 通过 localhost:11434/v1。配置持久化在 config.yaml 中

### [平台限流] 平台限流(rate limit)处理

带有详细限流排查指导

### [社区促销] 优云智算 Agent Plan

支持 GLM-5.2，49元/月起，按次调用

