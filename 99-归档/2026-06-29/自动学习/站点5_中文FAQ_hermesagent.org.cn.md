---
site: "https://hermesagent.org.cn/docs/reference/faq"
title: "Hermes Agent 中文社区 FAQ"
fetched_at: "2026-06-29"
status: "success"
tags: [hermes, FAQ, 中文, 故障排除, 配置, 模型, 消息网关, MCP]
---

# 知识点清单

## 1. FAQ 覆盖范围
- **标题**: FAQ 全部问题清单
- **摘要**: 涵盖 LLM 提供商支持、Windows 安装（原生 PowerShell + WSL2 双路径）、Android/Termux 安装、数据隐私策略、离线/本地模型使用、使用成本、多用户共享、记忆与技能区别、Python 库集成、以及详细故障排除（安装/提供商/终端/消息/MCP/性能/配置文件）。
- **标签**: #hermes #faq #coverage

## 2. LLM 提供商支持
- **标题**: 支持的模型提供商
- **摘要**: 支持任何兼容 OpenAI API 的提供商：OpenRouter（推荐）、Nous Portal、OpenAI、Anthropic（通过 OpenRouter）、Google Gemini、z.ai/ZhipuAI（GLM 模型）、Kimi/Moonshot AI、MiniMax（全球+中国端点）、本地模型（Ollama/vLLM/llama.cpp/SGLang）。
- **标签**: #hermes #providers #llm

## 3. Windows 安装（中文镜像）
- **标题**: 中文镜像版安装
- **摘要**: 提供国内直连镜像：
  - 原生 PowerShell: `irm https://res1.hermesagent.org.cn/install.ps1 | iex`
  - WSL2 + Ubuntu: `curl -fsSL https://res1.hermesagent.org.cn/install.sh | bash`
  - 镜像版会精简部分不常用组件以提高安装成功率
- **标签**: #hermes #windows #mirror #chinese

## 4. 数据隐私
- **标题**: 数据不会发送到何处
- **摘要**: Hermes Agent 不收集遥测数据、使用数据或分析信息。对话、记忆和技能全部本地存储在 ~/.hermes/ 目录。API 调用仅发送至用户配置的 LLM 提供商。
- **标签**: #hermes #privacy #data

## 5. 本地模型配置
- **标题**: 离线/本地模型详细配置
- **摘要**: 通过 `hermes model` 选择自定义端点，或直接在 config.yaml 中配置 `provider: custom`。支持 Ollama、vLLM、llama.cpp、SGLang、LocalAI。提供 Ollama 的 num_ctx 匹配提示，和本地模型超时调整（`HERMES_STREAM_READ_TIMEOUT=1800`）。
- **标签**: #hermes #local-model #offline #ollama

## 6. 故障排除详细方案
- **标题**: 详细故障排除
- **摘要**: 
  - **安装**: command not found → reload shell / 检查 PATH
  - **Python**: 需 3.11+
  - **uv**: 未安装 → `curl -LsSf https://astral.sh/uv/install.sh | sh`
  - **权限**: 不要在安装程序中使用 sudo
  - **API 密钥**: `hermes config show` 检查 + `hermes model` 重新配置
  - **模型不可用**: `hermes model` 列出可用模型
  - **429 限流**: 等待/切换模型/切换提供商
  - **上下文超长**: `/compress` 压缩 / 增大 context_length 配置
  - **命令被阻止**: 审查并确认 / 参考安全文档
  - **Docker 不可连**: `docker info` → `usermod -aG docker`
  - **机器人不响应**: `hermes gateway status` + 检查日志
  - **macOS 网关 PATH 问题**: launchd 使用精简 PATH → `hermes gateway install` 重新捕获
  - **响应缓慢**: 使用更小模型 / 减少工具集 / 检查网络延迟
  - **Token 使用过高**: `/compress` 压缩对话
  - **MCP 无法连接**: 测试命令 / 检查 tools/include/exclude 配置
  - **MCP 超时**: 检查服务器自身日志 / 增加超时
- **标签**: #hermes #troubleshooting #FAQ

## 7. 配置文件（Profiles）
- **标题**: 配置文件系统
- **摘要**: 配置文件是 HERMES_HOME 之上的管理层。支持 `hermes profile create/clone/export/import`。配置文件之间不共享记忆/会话。每个配置文件需要独立的机器人 token。`hermes update` 自动同步技能到所有配置文件。无硬性配置文件数量限制。
- **标签**: #hermes #profiles #multi-instance

## 8. 工作流与模式
- **标题**: 多模型工作流
- **摘要**: 通过 delegation config 实现子 Agent 路由到不同模型。例如主模型用 GPT-5.4，子 Agent 用 Gemini。在 config.yaml 中配置 `delegation.model` 和 `delegation.provider`。`/model` 命令可临时切换当前会话模型。
- **标签**: #hermes #workflow #multi-model #delegation

## 9. MCP 中文诊断指南
- **标题**: MCP 故障排查
- **摘要**: MCP 服务器工具未显示→检查日志/filters配置/服务器 capabilities。提供了一个完整的 MCP 配置示例（npx filesystem server）。`/reload-mcp` 热重载。
- **标签**: #hermes #mcp #troubleshooting #chinese
