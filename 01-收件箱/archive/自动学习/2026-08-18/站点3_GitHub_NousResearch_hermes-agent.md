# 站点3：GitHub（NousResearch/hermes-agent）

> 抓取日期：2026-08-17 ｜ 状态：✅ 成功（repo + releases + commits API） ｜ 信源层级：Tier 1

## 知识点：仓库基本状态
- **标题**：231,687 ⭐ / 46,109 forks / 32,507 open issues
- **摘要**：MIT 许可，Python 主语言，默认分支 main 未归档，2026-08-17 08:01 UTC 仍有推送（非常活跃）。描述 "The agent that grows with you"。
- **标签**：#github #repo #活跃度

## 知识点：版本三连发（8月3日～16日）✅ 核心变化
- **标题**：v0.20.0 Herald → v0.20.1 → v0.20.2
- **摘要**：
  - **v0.20.0（8-03，The Herald Release）**：自 v0.19.0 以来 ~3,650 commits、~1,400 PRs、~1,200 issues 关闭、650+ 贡献者。主打：① **语音**——流式会话式 TTS + barge-in（说话打断）、设备端唤醒词、全平台（CLI/桌面/网关）语音，WhatsApp/飞书/钉钉/LINE/QQ 语音消息收发+自动 TTS 回复，STT 可配置（gpt-transcribe 支持）；② **A2A v1.0** 智能体间通信协议插件；③ **签名出站 Webhook**；④ **grounded research**（可验证引用+事实核查）；⑤ 桌面 App 平台化——Artifacts（版本化卡片+沙箱实时预览）、插件 SDK、多窗口；⑥ CLI 新命令（`!` shell 模式、/init、/diff、/context、/focus、Ctrl+S 提示暂存、多选 clarify）；⑦ 压缩优化（逐轮 micro-compaction、min_tail_user_messages）；⑧ 工具自恢复（工具自己修复失败，不再让模型猜）。
  - **v0.20.1（8-13）**：patch，~656 PRs。
  - **v0.20.2（8-16）**：patch，~967 commits / ~397 PRs。要点：桌面多网关 Connections 注册表、profile 级刷新、MCP 健康检查与 deep links；CLI Windows 更新探测、Kitty 键盘协议、chat -c 加固；gateway 持久化模型路由、/loop 完成、Telegram DM topics；**LiteLLM Claude 走 OpenAI wire 的 prompt caching**；cron 加固；auth 按 profile scope 解析；Linux/Windows 安装器加固。
- **标签**：#版本 #release #v0.20.0 #v0.20.2

## 知识点：最新提交趋势（8-17）
- **标题**：MCP 与桌面端修复是当前主线
- **摘要**：最近提交集中在：MCP sanitization 与 tool-result annotations（scout-slate 波次）、MCP-Protocol-Version 握手版本种子化、桌面端删除 profile 重生修复、bot-mode 机器人互发路由、文档迁移。MCP 相关改动密集，说明 MCP 层在快速收敛。
- **标签**：#commit #MCP #趋势
