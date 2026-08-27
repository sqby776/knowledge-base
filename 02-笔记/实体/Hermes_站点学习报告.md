---
title: Hermes 站点学习报告
created: 2026-07-22
updated: 2026-08-18
tags: [knowledge-base, hermes-agent, learning-report]
status: active
sources: [https://hermes-agent.nousresearch.com/, https://github.com/NousResearch/hermes-agent, https://hermesagent.org.cn]
---

# Hermes 站点学习报告

> 最近一轮: 2026-08-17 抓取，版本 **v0.20.2**（8-03 v0.20.0 → 8-13 v0.20.1 → 8-16 v0.20.2 三连发）

## 版本基线

| 指标 | v0.17.0 (2026-07) | v0.20.0 (2026-08-03) | 变化 |
|------|-------------------|---------------------|------|
| 版本号 | v0.17.0 | **v0.20.0** | +3 个版本 |
| GitHub Stars | 约 200k (估算) | **228,097** | 显著增长 |
| Forks | 约 40k (估算) | **44,812** | 显著增长 |
| 文档框架 | Docusaurus v3.9.2 | Docusaurus v3.10.2 | 升级 |
| 开发量 | — | ~3,650 commits · ~1,400 PRs · ~1,200 issues closed · 650+ 贡献者 | 重大 |
| 代码变更 | — | 559k 插入 + 405k 删除 (65万+ 行) | 重大 |

## 核心亮点 (v0.20.0)

1. **实时语音对话** — 流式 TTS + barge-in（打断）+ 唤醒词 + 免提控制。从"语音邮件"到"真正对话"的质变
2. **出站 Webhooks** — HMAC 签名生命周期事件主动推送到任意 HTTP 端点，可接入 CI/CD、家居自动化、仪表盘
3. **带引证的深度研究** — `grounded-citations` skill，可验证来源
4. **A2A v1.0** — Agent-to-Agent 通信协议
5. **桌面应用平台化** — artifacts 实时预览、插件 SDK、多窗口、全局快捷入口
6. **CLI 新命令** — `!` shell 模式、`/init`、`/diff`、`/context`、`/focus`
7. **工具自恢复** — 工具从自身失败中恢复，不让模型猜测

## 文档体系扩展（相对 v0.17 新增 30+ 页）

- **新功能页 (15+)**: Checkpoints & Rollback、Nix Setup、Git Worktrees、TUI (Ink)、Voice Mode、TTS Reference、ACP、API Server、Batch Processing、Kanban、Goals、Hooks、Context References、Built-in Plugins
- **新指南 (7+)**: Daily Briefing Bot、Team Telegram Assistant、Automate with Cron、GitHub PR Review Agent、Use Voice Mode、Use SOUL.md、Delegation Patterns、Work with Skills
- **新开发者文档 (5+)**: Provider Runtime、Gateway Internals、Prompt Assembly、Adding Providers、Adding Tools、Extending the CLI
- **新参考 (6)**: Slash Commands、Tools Reference、Toolsets Reference、MCP Config Reference、Skills Catalog (~90)、Optional Skills Catalog (~60)
- **新增消息平台**: LINE、Raft、Webhooks、Photon
- **新增中文支持**: 官方文档 `/docs/zh-Hans/` 简体中文路径；中文社区 FAQ `hermesagent.org.cn` 国内可直连

## 站点状态

| 站点 | URL | 状态 |
|------|-----|------|
| 官网首页 | hermes-agent.nousresearch.com/ | ✅ 正常 |
| 官方文档 | hermes-agent.nousresearch.com/docs | ✅ Docusaurus v3.10.2, llms.txt 完整 |
| GitHub | github.com/NousResearch/hermes-agent | ✅ 228k stars / 44.8k forks |
| 中文文档 | hermes.xaapi.ai | ❌ DNS 解析失败（域名可能过期/迁移）|
| 中文 FAQ | hermesagent.org.cn | ✅ 国内可直连镜像 |

## 信息缺口

1. **v0.18.0 / v0.19.0 Release Notes** — 中间版本未被知识库捕获，可从 GitHub releases 页逐个查看
2. **hermes.xaapi.ai 中文文档站** — 域名不可达，替代为官方 `/docs/zh-Hans/`
3. **v0.20.0 性能数据** — Release Notes 无推理速度/响应时间测试数据

## 参考

- 完整版本细节: [[Hermes_Agent_v0200_Herald_Release]]
- 实体主笔记: [[Hermes_Agent]]
- 原始抓取归档: `01-收件箱/archive/自动学习/2026-08-10/学习报告_2026-08-10.md`

## 2026-08-17 第3轮捕获（v0.20.1 / v0.20.2 增量）⭐

### 版本节奏
- **v0.20.0 The Herald Release**（8-03）：~3,650 commits / ~1,400 PRs / ~1,200 issues / 650+ 贡献者
- **v0.20.1**（8-13）：patch，~656 PRs
- **v0.20.2**（8-16）：patch，~967 commits / ~397 PRs。要点：桌面多网关 Connections 注册表、profile 级刷新、MCP 健康检查与 deep links；CLI Windows 更新探测、Kitty 键盘协议、chat -c 加固；gateway 持久化模型路由、/loop 完成、Telegram DM topics；**LiteLLM Claude 走 OpenAI wire 的 prompt caching**；cron 加固；auth 按 profile scope 解析；Linux/Windows 安装器加固

### 新变化（相对 8-10 轮次）
- ⚠️ **llms.txt 路径迁移**：根路径 `/llms.txt`、`/llms-full.txt` → `/docs/assets/files/llms-<hash>.txt`；llms-full 更新为 `9595dc2b...`（3.78MB，含 8 月文档变化）
- 🆕 官方中文文档 `/docs/zh-Hans/` 全分区上线（替代已死的 xaapi.ai）
- 🆕 Windows 原生安装（PowerShell 早期测试版）：`iex (irm https://hermes-agent.nousresearch.com/install.ps1)`
- 🆕 Android/Termux 官方支持（`.[termux]`，voice 不可用）
- GitHub：**231,687 ⭐**；近期提交主线 MCP sanitization / tool-result annotations（scout-slate 波次）
- 中文社区：主推 Deepseek-V4 / GLM-5.2 / Minimax-M2.7 / Kimi-k2.6；国内镜像安装器 res1.hermesagent.org.cn

### 站点状态变化
| 站点 | 状态 |
|------|------|
| hermes.xaapi.ai（中文文档） | ❌ 超时疑似**下线**，从站点清单移除 |
| 官方 /docs/zh-Hans/ | ✅ 新增强权中文源 |

### 行动建议
- 本地 Hermes v0.20.1 → `hermes update` 至 v0.20.2（cron 加固、prompt caching 直接受益）
- 重新摄取 llms-full.txt（9595dc2b）同步 8 月新文档到 ChromaDB/知识图谱
- Tavily web_extract 401 → 检查 API key；urllib 直连备用方案已验证可行

---
*最后更新：2026-08-18（本轮维护，采用 2026-08-17 学习报告内容）*
