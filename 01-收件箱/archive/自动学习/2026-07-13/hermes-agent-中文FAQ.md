---
title: Hermes Agent 中文社区 FAQ
source: https://hermesagent.org.cn/docs/reference/faq
fetched: 2026-07-13
tier: Tier 2 (中文社区维护)
tags: [hermes-agent, FAQ, 中文, 故障排除, 配置, auto-compiled]
---

# Hermes Agent 中文 FAQ 知识点

## 支持的 LLM 提供商
- **OpenRouter** — 推荐（灵活，数百模型）
- **Nous Portal** — Nous Research 自有推理端点
- **OpenAI** — GPT-4o, o1, o3
- **Anthropic** — Claude（通过 OpenRouter 或兼容代理）
- **Google** — Gemini（通过 OpenRouter）
- **z.ai / ZhipuAI** — GLM 模型
- **Kimi / Moonshot AI** — Kimi 模型
- **MiniMax** — 全球及中国端点
- **本地模型** — Ollama, vLLM, llama.cpp, SGLang

## Windows 安装
两条路径：
1. **原生 PowerShell**（推荐）：`irm https://res1.hermesagent.org.cn/install.ps1 | iex`
2. **WSL2**：`curl -fsSL https://res1.hermesagent.org.cn/install.sh | bash`

镜像版安装器精简了部分可选组件以提高安装成功率。

## Android / Termux 支持
- 已提供经过测试的 Termux 安装路径
- 不支持完整的 `.[all]` 附加功能（voice 依赖 faster-whisper → ctranslate2 无法在 Android 编译）
- 使用经过测试的 `.[termux]` 附加功能

## 数据隐私
- API 调用仅发送到用户配置的 LLM 提供商
- 不收集遥测数据、使用数据或分析信息
- 对话、记忆、技能本地存储在 `~/.hermes/`

## Profiles（配置文件）系统
### 核心能力
- 创建独立配置：`hermes profile create <name>`
- 克隆配置：`hermes profile create newname --clone-all`
- 导出/导入：`hermes profile export` / `hermes profile import`
- 配置文件之间**完全隔离**（记忆、会话、技能不共享）
- 配置文件不能共享同一个机器人令牌
- 无硬性限制，每个配置文件是 `~/.hermes/profiles/<name>/` 下的目录

### 升级行为
- `hermes update` 拉取最新代码并安装依赖一次
- 自动将更新技能同步到所有配置文件

## 工作流模式

### 多模型工作流
通过 Delegation Config 实现子 Agent 使用不同模型：
```yaml
delegation:
  model: "google/gemini-3-flash-preview"
  provider: "openrouter"
```

### WhatsApp 多 Agent 限制
- 每个配置文件需要独立 WhatsApp 号码
- 无法将多个配置文件绑定到同一 WhatsApp 的不同聊天
- Baileys 桥接器每个号码仅支持一个认证会话
- 替代方案：人格切换 / crontab / 换 Telegram 或 Discord

### Telegram 显示控制
- `display.tool_progress` 控制显示级别（off/new/all/verbose）
- Telegram 建议使用 `off` 或 `new`

### Telegram 技能管理
- Telegram 斜杠命令限制 100 个
- 可通过 `skills.platform_disabled` 按平台禁用技能
- 描述过长的技能会被截断到 40 字符
- 修改后需要重启网关

### 共享线程会话
- Telegram: 按用户 ID 键控
- Discord: 按频道键控
- Slack: 按线程键控（最自然的共享方式）

## 配置详解

### 上下文长度检测
- Hermes 自动检测模型上下文长度
- CLI 启动时会显示检测到的上下文长度
- 可通过 `config.yaml` 手动设置 `context_length`
- 自定义端点可按模型单独配置

### 本地模型配置
```yaml
model:
  default: qwen3.5:27b
  provider: custom
  base_url: http://localhost:11434/v1
```
- 本地端点自动检测并放宽流式传输超时（120s → 1800s）
- 可在 `.env` 设置 `HERMES_STREAM_READ_TIMEOUT=1800`

## MCP 故障排除
- 确保安装了 MCP 依赖：`uv pip install -e ".[mcp]"`
- 确保 Node.js 可用（基于 npm 的服务器需要）
- 手动测试：`npx -y @modelcontextprotocol/server-filesystem /tmp`
- 使用 `/reload-mcp` 重新加载 MCP 配置
- MCP 服务器崩溃时 Hermes 报告超时，需检查服务器自身日志

## 其他关键知识点
- **费用**：Hermes Agent 本身免费开源（MIT），仅需支付 LLM API 使用费
- **多人共用**：支持多个用户通过消息网关与同一实例交互
- **记忆 vs 技能**：记忆存事实，技能存操作流程
- **Python 库使用**：可 `from run_agent import AIAgent` 在项目中使用
- **Blank Slate 模式**：最小化安装，仅开启 File Operations 和 Terminal，适合完全受控场景