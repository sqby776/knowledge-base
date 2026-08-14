---
title: Hermes Agent v0.20.0 Herald Release
created: 2026-08-10
updated: 2026-08-11
tags: [knowledge-base, hermes-agent, release, v0.20.0, auto-compiled]
status: active
sources: [auto-capture]
---

# Hermes Agent v0.20.0 — Herald Release

> 抓取自官网和 GitHub Release。发布日期：2026-08-03

## 版本信息

- **版本**: v0.20.0 (v2026.8.3)
- **代号**: "Herald Release"（信使）
- **自 v0.19.0 以来**: ~3,650 commits · ~1,400 merged PRs · ~5,200 files changed · ~559,000 insertions · ~405,000 deletions · **~1,200 issues closed** · 650+ contributors
- **GitHub**: 228k stars, 44.8k forks
- **官网新版本号**: 页脚显示 "Hermes Agent v0.20.0"

## 核心亮点

1. **实时语音对话** — 流式 TTS + barge-in（打断），支持 CLI、桌面、网关平台。说话可打断，智能静音检测
2. **唤醒词和免提控制** — 自定义唤醒词（"hey Hermes" 等），设备端运行，多 profile 语音路由
3. **全平台语音** — 语音消息在 WhatsApp、飞书、钉钉、LINE、QQ、Photon、微信上收发
4. **带引证的深度研究** — `grounded-citations` skill，可验证来源，事实核查模式
5. **出站 Webhooks** — HMAC 签名生命周期事件推送，可接入 CI/家居自动化/仪表盘
6. **A2A v1.0** — Agent-to-Agent 通信协议
7. **桌面应用平台化** — artifacts 实时预览、插件 SDK、多窗口、全局快捷入口
8. **CLI 新命令** — `!` shell 模式、`/init`、`/diff`、`/context`、`/focus`
9. **工具自恢复** — 工具从自身失败中恢复，不再让模型猜测

## 新增文档页面（相对 v0.17.0）

### 新功能
- Checkpoints & Rollback（快照回滚保护）
- Nix Setup（Nix 安装部署）
- Git Worktrees（多 agent 安全运行）
- TUI (Ink terminal UI)（现代化终端 UI）
- Context References（@-语法内联引用）
- Built-in Plugins（内置插件）
- Kanban（SQLite 任务板）
- Goals（持久目标）
- Hooks（生命周期钩子）
- Batch Processing（批量轨迹生成）
- Voice Mode（实时语音）
- TTS（文本转语音参考）
- ACP（Agent Context Protocol 编辑器集成）
- API Server（OpenAI 兼容 API）

### 新指南
- Daily Briefing Bot（每日简报机器人）
- Team Telegram Assistant（团队 Telegram 助手）
- Automate with Cron（自动化模式）
- GitHub PR Review Agent（PR 审阅机器人）
- Use Voice Mode / Use SOUL.md / Use MCP
- Delegation Patterns（子代理模式）
- Work with Skills（技能使用指南）

### 新开发者文档
- Provider Runtime（provider 运行时）
- Gateway Internals（网关内部）
- Prompt Assembly（提示词组装）
- Adding Providers / Adding Tools
- Extending the CLI

### 新参考文档
- Slash Commands（斜杠命令完整参考）
- Tools Reference（工具参考）
- Toolsets Reference（工具集参考）
- MCP Config Reference（MCP 配置参考）
- Skills Catalog（~90 内置技能目录）
- Optional Skills Catalog（~60 可选技能目录）

## 新增消息平台
- LINE
- Raft
- Webhooks（作为消息平台）
- Photon

## 中文文档
- 官方文档现支持简体中文版本：`/docs/zh-Hans/`
- 中文社区镜像站点：`hermesagent.org.cn`（国内可直连）

## 安装方式（更新）
- 桌面版安装器：macOS (Hermes-Setup.dmg build=628372de4696)、Windows (Hermes-Setup.exe)
- 终端安装：`curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash`
- Windows 原生：`iex (irm https://hermes-agent.nousresearch.com/install.ps1)`
- 中文镜像版：`curl -fsSL https://res1.hermesagent.org.cn/install.sh | bash`
- Nix 安装：`nix run github:NousResearch/hermes-agent`

## 信源
- 官网: https://hermes-agent.nousresearch.com/ [Tier 1]
- 官方文档: https://hermes-agent.nousresearch.com/docs/ [Tier 1]
- GitHub Release: https://github.com/NousResearch/hermes-agent/releases/latest [Tier 1]
- 中文 FAQ: https://hermesagent.org.cn/docs/reference/faq [Tier 3]