# Hermes Agent 官方文档
> Source: https://hermes-agent.nousresearch.com/docs
> Fetch time: 2026-06-12

## 开发者
Nous Research | 许可证: MIT

## 核心身份
自主自我改进AI智能体，内置学习闭环。不同于静态编码助手或简单聊天封装，Hermes 从经验中创建技能，使用中改进，构建跨会话的持久用户模型。

## 安装命令
```bash
# Linux/macOS/WSL2/Android(Termux)
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
# Windows (Native PowerShell)
iex (irm https://hermes-agent.nousresearch.com/install.ps1)
```

## 初始设置
```bash
hermes setup --portal   # OAuth覆盖模型+4个工具网关
```
> 一个OAuth覆盖一个模型和四个工具网关（网页搜索、图像生成、TTS、浏览器）。

## 机器可读文档
- 精简索引 (~17KB): `/llms.txt` 或 `/docs/llms.txt`
- 完整文档 (~1.8MB): `/llms-full.txt` 或 `/docs/llms-full.txt`

## 核心功能模块

### 🧠 自我学习闭环
- 从使用体验中自主创建和改进技能
- 周期性记忆引导以持久化知识
- FTS5跨会话召回 + LLM摘要
- Honcho辩证用户建模

### 🌐 平台支持
- **消息网关 (20+平台)**: CLI, Telegram, Discord, Slack, WhatsApp, Signal, Matrix, Mattermost, Email, SMS, DingTalk, 飞书, 企业微信, 微信, QQ Bot, Yuanbao, BlueBubbles, Home Assistant, Microsoft Teams, Google Chat
- **部署后端 (6种)**: 本地、Docker、SSH、Daytona、Singularity、Modal（Daytona/Modal支持无服务器持久化）
- **模型提供商**: Nous Portal, OpenRouter, OpenAI, 或任意自定义端点
- **工具生态**: 60+内置工具，MCP集成，Skills Hub

### 🛠️ 高级功能
- **语音模式**: CLI、Telegram、Discord、Discord语音频道实时语音交互
- **人格设定**: 全局SOUL.md定义默认语音/人格，项目级上下文文件
- **安全**: 命令审批工作流、授权控制、容器隔离
- **自动化**: 内置cron调度器
- **研究就绪**: 批量轨迹生成、轨迹压缩、Atropos RL训练

## 快速导航文档链接
- Getting Started: Installation, Quickstart, Learning Path
- Configuration: Config File, Messaging Gateway
- Features: Tools & Toolsets, Memory System, Skills System, MCP Integration, Voice Mode, Personality
