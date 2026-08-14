---
title: Hermes Agent 文档页面列表（llms.txt）
created: 2026-08-10
updated: 2026-08-11
tags: [knowledge-base, hermes-agent, docs, auto-capture, auto-compiled]
status: active
sources: [auto-capture]
---

# Hermes Agent 文档页面列表（llms.txt 提取）

> 抓取自 llms.txt，2026-08-10

## 文档结构（按分类）

### Getting Started
- Installation: 安装指南（Linux/macOS/WSL2/Windows native/Android Termux）
- Quickstart: 5分钟快速上手
- Learning Path: 学习路径选择
- Updating: 更新与卸载
- Termux (Android): 手机运行指南
- Nix Setup: Nix 安装部署

### Using Hermes
- CLI: 终端界面命令/键绑定/个性
- TUI: Ink 终端 UI（鼠标友好、富覆盖层）
- Configuration: config.yaml 配置
- Configuring Models: 模型配置
- Sessions: 会话持久化/恢复/搜索
- Profiles: 多 profile 管理
- Git Worktrees: 多 agent 安全共仓
- Docker Backend: Docker 运行
- Security: 安全模型/命令批准/容器隔离
- Checkpoints & Rollback: 快照回滚保护

### Core Features
- Tools: 60+ 内置工具概览
- Skills System: 技能系统（渐进式文档）
- Curator: 技能后台维护（使用追踪/过时检测/归档）
- Memory: 跨会话记忆（MEMORY.md/USER.md/session_search）
- Memory Providers: 8 种外部记忆插件
- Context Files: 项目上下文文件
- Context References: @-语法内联引用
- Personality: SOUL.md 个性定制
- Plugins: 插件系统
- Built-in Plugins: 内置插件
- Cron: 自然语言调度
- Delegation: 隔离子代理
- Kanban: SQLite 任务板
- Goals: 持久目标
- Code Execution: execute_code RPC
- Hooks: 生命周期钩子
- Batch Processing: 批量轨迹生成
- Voice Mode: 实时语音
- TTS: 文本转语音

### Messaging Platforms（20+ 平台）
- Telegram, Discord, Slack, WhatsApp, Signal, SMS, Email, Home Assistant, Mattermost, Matrix, DingTalk, Yuanbao, Microsoft Teams, LINE, Raft, Webhooks
- 原生 19 平台 + IRC/Teams 插件 + 新增平台

### Integrations
- MCP: MCP 服务器连接
- ACP: 编辑器内 Agent 嵌入
- API Server: OpenAI 兼容 API
- Honcho: 辩证用户建模

### Guides
- Tips & Best Practices
- Local LLM on Mac
- Daily Briefing Bot
- Team Telegram Assistant
- Python Library
- Use MCP with Hermes
- Use Voice Mode
- Use SOUL.md
- Automate with Cron
- Work with Skills
- Delegation Patterns
- GitHub PR Review Agent

### Developer Guide
- Contributing, Architecture, Agent Loop, Prompt Assembly, Gateway Internals, Provider Runtime, Adding Tools, Adding Providers, Creating Skills, Extending the CLI

### Reference
- CLI Commands, Slash Commands, Environment Variables, Tools Reference, Toolsets Reference, MCP Config Reference, Skills Catalog (~90), Optional Skills Catalog (~60), FAQ

## 关键数据
- **llms.txt**: ~17KB（文档索引）
- **llms-full.txt**: ~1.8MB（所有文档页面合并）
- **内置技能**: ~90 个
- **可选安装技能**: ~60 个
- **消息平台**: 19 原生 + 2 插件 + 新增
- **终端后端**: 6 个（local/Docker/SSH/Daytona/Modal/Singularity）