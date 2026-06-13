# GitHub: NousResearch/hermes-agent
> Source: https://github.com/NousResearch/hermes-agent
> Fetch time: 2026-06-12

## 项目概述
Hermes Agent 是 Nous Research 开发的自改进开源AI智能体，具备闭环学习系统，从经验创建技能，跨会话持久化知识，适配用户偏好。

## 安装命令
```bash
# Linux, macOS, WSL2, Termux
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
# Windows (Native PowerShell)
iex (irm https://hermes-agent.nousresearch.com/install.ps1)
```
> Windows安装器自动处理Python 3.11、Node.js、ripgrep、ffmpeg、便携Git Bash。

## 快速启动
```bash
hermes              # 启动交互式CLI
hermes model        # 选择LLM提供商/模型
hermes tools        # 配置启用工具
hermes gateway      # 启动消息网关
hermes setup        # 运行完整设置向导
hermes claw migrate # 从OpenClaw迁移
hermes update       # 更新到最新版本
```

## Nous Portal 集成
- 统一订阅替代逐个API密钥收集
- 300+模型访问
- Tool Gateway: 网页搜索、图像生成、TTS、云浏览

## CLI vs 消息斜杠命令对比
| 操作 | CLI | 消息平台 |
|------|-----|----------|
| 新对话 | /new 或 /reset | /new 或 /reset |
| 切换模型 | /model [provider:model] | /model [provider:model] |
| 设置人格 | /personality [name] | /personality [name] |
| 重试/撤销 | /retry, /undo | /retry, /undo |
| 压缩上下文 | /compress, /usage | /compress, /usage |
| 浏览技能 | /skills 或 /<skill> | /<skill> |
| 中断 | Ctrl+C | /stop |

## 核心能力
- **自我改进循环**: 从复杂任务创建技能，使用中改进，FTS5跨会话召回+LLM摘要
- **模型无关**: 支持 Nous Portal、OpenRouter (200+模型)、NovitaAI、NVIDIA NIM、小米MiMo、z.ai/GLM、Kimi/Moonshot、MiniMax、Hugging Face、OpenAI及自定义端点
- **多平台**: Telegram、Discord、Slack、WhatsApp、Signal、Home Assistant、Email、SMS
- **终端接口**: 完整TUI，多行编辑、斜杠命令自动补全、对话历史、中断重定向、流式工具输出
- **定时自动化**: 内置cron调度器
- **委派**: 隔离子Agent并行工作流，Python脚本RPC折叠多步骤流水线
- **架构**: 6种终端后端，Daytona/Modal无服务器持久化，$5 VPS即可运行
- **研究就绪**: 批量轨迹生成与压缩

## 桌面应用
- Electron基础，支持Windows/macOS/Linux
- OAuth优先入门 (Nous Portal)
- 内建终端（Solarized配色、WebGL渲染）
- KaTeX LaTeX数学渲染
- 编排队列（Cursor风格）
- 实时子Agent树可视化
- MCP设置管理和插件市场

## 技能与工具
- 兼容 agentskills.io 开放标准的技能系统
- 40+内置工具
- MCP集成（含Nous审批MCP服务器目录）

## 从OpenClaw迁移
- 自动检测 ~/.openclaw 并提供迁移向导
- 手动: `hermes claw migrate`
