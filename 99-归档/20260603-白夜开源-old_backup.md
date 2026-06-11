# 白夜开源：爬虫学会了自适应，AI记忆拿了三个第一

旧时白夜，2026-06-03

## 摘要

本期盘点 5 个 AI/爬虫/开发工具开源项目：

1. **Scrapling** — 自适应爬虫框架，选择器自动重建，绕过 Cloudflare Turnstile
2. **Supermemory** — AI 记忆引擎，三个 benchmark 全第一，区分记忆和 RAG
3. **Heretic** — 一键移除 AI 模型安全审查，社区产出 3000+ 模型
4. **oh-my-pi** — 完整 IDE 接入 AI 编程 Agent（LSP + DAP + 浏览器）
5. **VoxCPM2** — 无 Tokenizer 语音生成，30 语言 48kHz，Voice Design 功能

---

## Scrapling — 自适应爬虫

- GitHub: ⭐ 58,240+ | Python | BSD-3-Clause
- 核心特点：选择器自动适应网站改版，内置 StealthyFetcher 绕过 Cloudflare
- 比 Playwright 快一个量级，HTTP 级请求模拟 TLS 指纹
- 提供 Scrapy 风格 Spider API、并发控制、断点续爬、代理轮换、MCP Server

**点评：** 爬虫界的"自动驾驶"，适合需要长期维护的爬取任务。

## Supermemory — AI 记忆引擎

- GitHub: ⭐ 24,092+ | TypeScript | MIT License
- 核心特点：自动从对话提取事实、构建用户画像、知识更新/矛盾处理、过期遗忘
- LongMemEval、LoCoMo、ConvoMem 三个 benchmark 全第一
- 区分"记忆"（个性化上下文）和 RAG（知识库文档），两者合一

**点评：** AI 终于有"脑子"了，一行代码接入 Claude Code / Cursor / Windsurf。

## Heretic — 移除 AI 审查

- GitHub: ⭐ 23,084+ | Python | AGPL-3.0
- 核心特点：directional ablation 移除审查方向，Optuna 自动优化参数
- Gemma-3-12b-it 拒绝率从 97% 降到 3%，KL 散度仅 0.16
- 支持 MoE 和混合架构，社区已产出 3000+ 去审查模型

**点评：** 技术上厉害，但用途争议大。这把刀太锋利。

## oh-my-pi — 完整 IDE 接入 AI Agent

- GitHub: ⭐ 9,531+ | Rust | MIT License
- 核心特点：LSP + DAP + 浏览器 + Python/JS 运行时全接入 Agent
- 语义级别重构（非正则替换），真正的调试器集成
- Rust 核心 27k 行，32 个内置工具，40+ 模型提供商

**点评：** 目前最完整的 IDE-to-Agent 方案，语义重构比纯文本编辑靠谱得多。

## VoxCPM2 — 无 Tokenizer 语音生成

- GitHub: ⭐ 24,373+ | Python | Apache-2.0
- 核心特点：连续潜空间生成，跳过 Tokenizer，扩散自回归架构
- 30 种语言无需标签，Voice Design 用自然语言创建声音
- 可控声音克隆 + 情绪/语速控制，48kHz 输出
- 2B 参数，200 万小时多语言数据训练

**点评：** 语音合成领域的"端到端"尝试，Voice Design 功能特别有意思。

---

*来源：微信公众号「旧时白夜」*
