---
source: https://hermesagent.org.cn/docs/reference/faq
date: 2026-06-22
tier: Tier 2
tags: [hermes-agent, 中文社区, FAQ, 故障排除, 安装指南]
---

# Hermes 中文社区 FAQ — 结构化知识点

## 1. 提供商支持
- **OpenRouter** — 一个 API 密钥访问数百种模型
- **Nous Portal** — Nous Research 自有推理端点
- **OpenAI** — GPT-4o、o1、o3 等
- **Anthropic** — Claude（通过 OpenRouter 或代理）
- **Google** — Gemini（通过 OpenRouter）
- **z.ai/ZhipuAI** — GLM 模型
- **Kimi/Moonshot** — Kimi 模型
- **MiniMax** — 全球及中国端点
- **本地模型** — Ollama、vLLM、llama.cpp、SGLang

## 2. Windows 安装（中文社区镜像）
- **原生 PowerShell**: `irm https://res1.hermesagent.org.cn/install.ps1 | iex`
- **WSL2**: `curl -fsSL https://res1.hermesagent.org.cn/install.sh | bash`
- 镜像版安装器精简了部分可选组件（浏览器自动化、Chromium 下载、WhatsApp 桥接）
- 后续可让 Agent 补装

## 3. Android/Termux 支持
- 安装: `curl -fsSL https://res1.hermesagent.org.cn/install.sh | bash`
- 限制: voice 附加功能不可用（faster-whisper → ctranslate2 无 Android wheel）
- 使用 `.[termux]` 附加功能替代 `.[all]`

## 4. 隐私与安全
- API 调用仅发至配置的 LLM 提供商
- 不收集遥测/使用/分析数据
- 对话、记忆、技能本地存储于 `~/.hermes/`
- 命令白名单、危险操作审查、容器隔离

## 5. 本地模型配置
- 命令: `hermes model` → 选择自定义端点
- 支持 Ollama、vLLM、llama.cpp 服务器、SGLang、LocalAI
- 超时设置: 自动放宽至 1800 秒（`HERMES_STREAM_READ_TIMEOUT`）

## 6. 记忆 vs 技能
- **记忆** — 存储事实（个人信息、项目偏好），根据相关性自动检索
- **技能** — 存储操作流程（分步说明），遇到类似任务时调用

## 7. 故障排除要点
- `hermes: command not found` → `source ~/.bashrc`
- API 密钥无效 → `hermes config show` + `hermes model`
- 上下文长度超出 → `/compress` 命令压缩会话
- 危险命令被阻止 → 审查后输入 `y` 确认
- Docker 无法连接 → `docker info` + `sudo usermod -aG docker`
- macOS 网关 PATH 问题 → `hermes gateway install` 重新捕获 PATH

## 8. MCP 配置
```yaml
mcp_servers:
  filesystem:
    command: "npx"
    args: ["-y", "@modelcontextprotocol/server-filesystem", "/home/user/docs"]
```

## 9. 消息网关授权模式
| 模式 | 工作方式 |
|------|---------|
| 允许列表 | 仅配置中的用户 ID 可交互 |
| 私信配对 | 第一个私信用户获得独占访问权 |
| 公开 | 任何人都可交互（不推荐生产） |

## 10. 中文社区特色
- 推荐使用 WorkBuddy（微信扫码即用）辅助安装
- 中文文档 MCP Server: `https://mcp.hermesagent.org.cn/v1`（Streamable HTTP）
- 国内镜像加速安装（res1.hermesagent.org.cn）
- 社区微信群支持