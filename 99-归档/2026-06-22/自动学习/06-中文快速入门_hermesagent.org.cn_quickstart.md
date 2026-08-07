---
source: https://hermesagent.org.cn/docs/getting-started/quickstart
date: 2026-06-22
tier: Tier 2
tags: [hermes-agent, 中文快速入门, 安装, 配置, 命令参考]
---

# Hermes 中文快速入门指南 — 结构化知识点

## 1. 中文社区安装命令
- **类 Unix**（含 WSL2/Android Termux）: `curl -fsSL https://res1.hermesagent.org.cn/install.sh | bash`
- **Windows 原生 PowerShell**: `irm https://res1.hermesagent.org.cn/install.ps1 | iex`
- 国内镜像加速，精简了非必需的可选组件以提高成功率

## 2. LLM 提供商列表（含中国特有）
- **Nous Portal** — 基于订阅，零配置 OAuth
- **OpenAI Codex** — ChatGPT OAuth/Codex 模型
- **Anthropic** — Claude Pro/Max 或 API 密钥
- **OpenRouter** — 多提供商路由
- **z.ai / GLM** — 智谱 GLM 模型
- **Kimi / Moonshot** — Kimi 聊天和代码模型
- **MiniMax / MiniMax 中国区** — 国际和中国端点
- **阿里云 DashScope** — Qwen 模型
- **Hugging Face** — 20+ 开源模型（Qwen/DeepSeek/Kimi）
- **Kilo Code / OpenCode Zen / OpenCode Go**
- **DeepSeek** — DeepSeek API
- **GitHub Copilot / Copilot ACP**
- **Vercel AI Gateway** / **自定义端点**

## 3. 快速命令参考
| 命令 | 描述 |
|------|------|
| `hermes` | 开始对话 |
| `hermes model` | 选择 LLM 提供商和模型 |
| `hermes tools` | 配置工具 |
| `hermes setup` | 完整设置向导 |
| `hermes doctor` | 诊断问题 |
| `hermes update` | 更新 |
| `hermes gateway` | 启动消息网关 |
| `hermes --continue` | 恢复上次会话 |

## 4. CLI 命令
- `/help` — 所有可用命令
- `/tools` — 列出可用工具
- `/model` — 交互式切换模型
- `/personality pirate` — 尝试有趣的人格模式
- `/save` — 保存对话
- `/new` 或 `/reset` — 开始新对话
- `/retry` / `/undo` — 重试/撤销
- `/compress` / `/usage` / `/insights` — 上下文管理
- `/skills` — 浏览技能
- `/voice on` — 启用语音模式
- `/stop` — 中断任务

## 5. 进阶探索
- 设置沙箱终端: `hermes config set terminal.backend docker|ssh`
- 连接消息平台: `hermes gateway setup`
- 语音模式: `pip install "hermes-agent[voice]"` + `faster-whisper`
- 技能安装: `hermes skills search <keyword> --source skills-sh`
- ACP 编辑器集成: `pip install -e '.[acp]'` → `hermes acp`
- MCP 服务器: 添加 `mcp_servers` 到 `config.yaml`

## 6. Limited provider list per current system
当前系统使用的是 `custom` provider 配合 DeepSeek-V4 Flash 模型，此信息记录供参考。