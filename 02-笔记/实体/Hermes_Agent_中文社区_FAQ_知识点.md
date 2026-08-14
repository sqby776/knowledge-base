---
title: Hermes Agent 中文社区 FAQ 知识点
created: 2026-08-10
updated: 2026-08-11
tags: [knowledge-base, hermes-agent, faq, chinese, auto-compiled]
status: active
sources: [auto-capture]
---

# Hermes Agent 中文社区 FAQ 知识点

> 抓取自 https://hermesagent.org.cn/docs/reference/faq，2026-08-10

## 核心信息

- 中文社区维护的镜像安装入口，优先走国内可直连链路
- 镜像版安装器精简了部分国人不常用/易受外网影响的可选组件

## 安装方式（国内镜像）

- **Windows 原生 PowerShell**: `irm https://res1.hermesagent.org.cn/install.ps1 | iex`
- **WSL2/Linux**: `curl -fsSL https://res1.hermesagent.org.cn/install.sh | bash`
- **Android/Termux**: `curl -fsSL https://res1.hermesagent.org.cn/install.sh | bash`

## 支持的 LLM 提供商

- OpenRouter（推荐，一密钥数百模型）
- Nous Portal（Nous Research 推理端点）
- OpenAI（GPT-4o/o1/o3）
- Anthropic（Claude，通过 OpenRouter）
- Google（Gemini，通过 OpenRouter）
- 智谱AI（GLM 模型）
- Kimi/Moonshot AI
- MiniMax（全球及中国端点）
- 本地模型（Ollama/vLLM/llama.cpp/SGLang/兼容 OpenAI 服务器）

## 常见问题

- **离线使用**: 支持，可配置自定义端点使用本地模型
- **多用户共享**: 支持，通过消息网关白名单控制
- **记忆 vs 技能**: 记忆=事实存储，技能=操作流程
- **Python 库集成**: 支持 `from run_agent import AIAgent`
- **数据隐私**: API 调用仅发送至配置的 LLM 提供商，不收集遥测数据
- **成本**: Hermes 本身免费开源（MIT），只需支付 LLM API 费用

## 故障排除要点

- 安装后 `hermes: command not found` → `source ~/.bashrc` 或检查 PATH
- Python 要求 3.11+
- API 密钥无效 → `hermes config show` 检查配置
- 速率限制 429 → 切换模型或提供商
- 上下文长度超限 → `/compress` 压缩会话
- 命令被阻止为危险操作 → 审查后输入 `y` 确认
- Docker 后端无法连接 → 检查 Docker 守护进程和用户组
- 机器人不响应 → `hermes gateway status` 检查网关