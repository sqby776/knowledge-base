---
site: hermesagent.org.cn (中文社区FAQ)
title: Hermes Agent 中文社区 FAQ 常见问题与故障排除
date: 2026-07-20
tags: [hermes-agent, faq, chinese, 中文社区, troubleshooting, mcp, performance, auto-compiled]
---

# Hermes Agent 中文社区 FAQ 常见问题与故障排除

## 摘要

中文社区 FAQ 页面提供的常见问题解答包含：

配置问题：
- 支持的 LLM 提供商：OpenRouter, Nous Portal, OpenAI, 本地模型 (Ollama/vLLM/llama.cpp/SGLang) 等兼容 OpenAI API 的端点
- 上下文长度自动检测与自定义配置
- 自定义提供商配置示例

终端问题：
- 危险命令安全防护（rm -rf, DROP TABLE 等需确认）
- sudo 通过消息网关不可用（需配置免密 sudo 或使用 CLI）
- Docker 后端连接问题排查

消息通信问题：
- 机器人不响应消息的排查步骤
- 消息无法送达的可能原因
- 允许列表三种模式：允许列表 / 私信配对 / 公开
- 网关无法启动的依赖检查
- macOS 网关中 Node.js/ffmpeg 找不到的问题（PATH 被 launchd 精简）

性能问题：
- 响应缓慢的优化建议（换小模型/减少工具集）
- Token 使用量过高的解决方案（/compress, /usage）
- 会话过长的处理

MCP 问题：
- MCP 服务器无法连接的处理
- MCP 工具不显示的排查
- MCP 超时错误处理

中文社区 Docusaurus 网站，多语言支持（简体/繁体/英文），含广告横幅

## 标签

hermes-agent, faq, chinese, 中文社区, troubleshooting, mcp, performance
