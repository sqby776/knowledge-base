---
title: Hermes 站点学习报告
created: 2026-07-22
updated: 2026-08-15
tags: [knowledge-base, hermes-agent, learning-report]
status: active
sources: [https://hermes-agent.nousresearch.com/, https://github.com/NousResearch/hermes-agent, https://hermesagent.org.cn]
---

# Hermes 站点学习报告

> 最近一轮: 2026-08-10 抓取，版本 **v0.20.0 Herald Release**（2026-08-03 发布，自 v0.17.0 跨 3 个版本）

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

---
*最后更新：2026-08-15（本轮维护，采用 2026-08-10 学习报告内容）*