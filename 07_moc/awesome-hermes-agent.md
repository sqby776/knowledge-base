# Awesome Hermes Agent 🤖

> 精选的 Hermes Agent 资源集合，涵盖官方文档、技能、工具、社区和最佳实践。

---

## 📚 官方资源

| 资源 | 链接 | 说明 |
|:-----|:-----|:-----|
| **官方文档** | https://hermes-agent.nousresearch.com/docs/ | 完整用户指南和 API 参考 |
| **GitHub 仓库** | https://github.com/NousResearch/hermes-agent | 源代码、Issues、PRs |
| **技能市场** | https://agentskills.io/ | 第三方技能集合 |
| **中文文档** | https://hermes.xaapi.ai/ | 中文用户指南 |
| **中文社区** | https://hermesagent.org.cn/ | 中文 FAQ 和讨论 |
| **橙皮书** | https://huasheng.ai/orange-books/ | 进阶教程和最佳实践 |

---

## 🛠️ 核心工具集

### 基础工具

| 工具集 | 用途 | 启用命令 |
|:-------|:-----|:---------|
| `terminal` | Shell 命令和进程管理 | `hermes tools enable terminal` |
| `file` | 文件读写、搜索、补丁 | 默认启用 |
| `code_execution` | 沙箱 Python 执行 | 默认启用 |
| `web` | 网页搜索和内容提取 | `hermes tools enable web` |
| `browser` | 浏览器自动化 | `hermes tools enable browser` |
| `search` | 纯网页搜索（web 子集） | `hermes tools enable search` |
| `vision` | 图像分析 | `hermes tools enable vision` |
| `image_gen` | AI 图像生成 | `hermes tools enable image_gen` |
| `video` | 视频分析和生成 | `hermes tools enable video` |
| `tts` | 文本转语音 | `hermes tools enable tts` |

### 高级工具

| 工具集 | 用途 | 启用命令 |
|:-------|:-----|:---------|
| `skills` | 技能浏览和管理 | 默认启用 |
| `memory` | 跨会话持久记忆 | `hermes tools enable memory` |
| `session_search` | 搜索历史对话 | `hermes tools enable session_search` |
| `delegation` | 子代理任务委派 | `hermes tools enable delegation` |
| `cronjob` | 定时任务调度 | `hermes tools enable cronjob` |
| `clarify` | 澄清问题 | 默认启用 |
| `messaging` | 跨平台消息发送 | `hermes tools enable messaging` |
| `todo` | 任务规划和跟踪 | `hermes tools enable todo` |
| `kanban` | 多代理工作队列 | `hermes tools enable kanban` |
| `debugging` | 调试工具（默认关闭） | `hermes tools enable debugging` |

### 平台集成工具

| 工具集 | 用途 |
|:-------|:-----|
| `discord` | Discord 集成 |
| `discord_admin` | Discord 管理/审核 |
| `feishu_doc` | 飞书文档工具 |
| `feishu_drive` | 飞书云盘工具 |
| `yuanbao` | 元宝集成 |
| `spotify` | Spotify 播放控制 |
| `homeassistant` | 智能家居控制 |

---

## 📦 技能分类

### Autonomous AI Agents（自主 AI 代理）

| 技能 | 用途 |
|:-----|:-----|
| `hermes-agent` | Hermes 配置和扩展 |
| `claude-code` | 委托给 Claude Code CLI |
| `codex` | 委托给 OpenAI Codex CLI |
| `opencode` | 委托给 OpenCode CLI |
| `kanban-codex-lane` | Kanban + Codex 工作流 |

### Creative（创意内容）

| 技能 | 用途 |
|:-----|:-----|
| `architecture-diagram` | SVG 架构图/云图 |
| `ascii-art` | ASCII 艺术 |
| `baoyu-article-illustrator` | 文章插图 |
| `baoyu-comic` | 知识漫画 |
| `baoyu-infographic` | 信息图 |
| `claude-design` | HTML 设计原型 |
| `comfyui` | ComfyUI 图像/视频生成 |
| `design-md` | Google DESIGN.md 规范 |
| `excalidraw` | Excalidraw 手绘图表 |
| `manim-video` | Manim 数学动画 |
| `p5js` | p5.js 创意编码 |
| `pixel-art` | 像素艺术 |
| `songwriting-and-ai-music` | 歌词和 AI 音乐 |
| `touchdesigner-mcp` | TouchDesigner 控制 |

### Data Science（数据科学）

| 技能 | 用途 |
|:-----|:-----|
| `jupyter-live-kernel` | 交互式 Jupyter 内核 |

### DevOps

| 技能 | 用途 |
|:-----|:-----|
| `kanban-orchestrator` | Kanban 编排 playbook |
| `kanban-worker` | Kanban 工作员指南 |
| `webhook-subscriptions` | Webhook 订阅 |

### Email（邮件）

| 技能 | 用途 |
|:-----|:-----|
| `himalaya` | Himalaya CLI 邮件管理 |

### GitHub

| 技能 | 用途 |
|:-----|:-----|
| `codebase-inspection` | 代码库检查（pygount） |
| `github-auth` | GitHub 认证设置 |
| `github-code-review` | PR 代码审查 |
| `github-issues` | GitHub Issues 管理 |
| `github-pr-workflow` | PR 生命周期管理 |
| `github-repo-management` | 仓库管理 |

### MCP（Model Context Protocol）

| 技能 | 用途 |
|:-----|:-----|
| `native-mcp` | MCP 客户端配置 |

### Media（媒体）

| 技能 | 用途 |
|:-----|:-----|
| `gif-search` | Tenor GIF 搜索 |
| `heartmula` | Suno 风格歌曲生成 |
| `songsee` | 音频频谱/特征分析 |
| `spotify` | Spotify 播放管理 |
| `youtube-content` | YouTube 转录和博客 |

### MLOps

| 技能 | 用途 |
|:-----|:-----|
| `audiocraft-audio-generation` | AudioCraft 音乐/音效 |
| `dspy` | DSPy 声明式 LM 程序 |
| `evaluating-llms-harness` | LLM 基准测试 |
| `huggingface-hub` | HuggingFace CLI |
| `llama-cpp` | llama.cpp 本地推理 |
| `obliteratus` | LLM 拒绝 abliterate |
| `segment-anything-model` | SAM 图像分割 |
| `serving-llms-vllm` | vLLM 模型服务 |
| `weights-and-biases` | W&B 实验跟踪 |

### Note-taking（笔记）

| 技能 | 用途 |
|:-----|:-----|
| `obsidian` | Obsidian 笔记操作 |

### Productivity（生产力）

| 技能 | 用途 |
|:-----|:-----|
| `airtable` | Airtable REST API |
| `google-workspace` | Google Workspace 集成 |
| `knowledge-base` | 本地知识库（Obsidian + Hermes） |
| `linear` | Linear 问题管理 |
| `maps` | OpenStreetMap/OSRM 地理编码 |
| `memory-palace` | MemOS 记忆宫殿 |
| `nano-pdf` | PDF 文本编辑 |
| `notion` | Notion API + CLI |
| `ocr-and-documents` | PDF/扫描件文字提取 |
| `office-toolchain` | LibreOffice + Python Office |
| `personal-knowledge-base` | 个人知识库搭建 |
| `powerpoint` | PowerPoint 操作 |
| `teams-meeting-pipeline` | Teams 会议总结 |

### Research（研究）

| 技能 | 用途 |
|:-----|:-----|
| `arxiv` | arXiv 论文搜索 |
| `blogwatcher` | 博客和 RSS 监控 |
| `llm-wiki` | Karpathy LLM Wiki |
| `polymarket` | Polymarket 查询 |
| `research-paper-writing` | ML 论文写作 |
| `web-scraping` | 多后端网页抓取 |

### Smart Home（智能家居）

| 技能 | 用途 |
|:-----|:-----|
| `openhue` | Philips Hue 控制 |

### Social Media（社交媒体）

| 技能 | 用途 |
|:-----|:-----|
| `xurl` | X/Twitter CLI |

### Software Development（软件开发）

| 技能 | 用途 |
|:-----|:-----|
| `debugging-hermes-tui-commands` | Hermes TUI 命令调试 |
| `hermes-agent-skill-authoring` | SKILL.md 编写 |
| `node-inspect-debugger` | Node.js 调试 |
| `plan` | 计划模式 |
| `python-debugpy` | Python 调试 |
| `requesting-code-review` | 预提交审查 |
| `spike` | 原型实验 |
| `subagent-driven-development` | 子代理驱动开发 |
| `systematic-debugging` | 系统化调试 |
| `test-driven-development` | TDD |
| `writing-plans` | 实现计划编写 |

---

## 🌐 模型提供商

| 提供商 | 认证方式 | 环境变量 |
|:-------|:---------|:---------|
| OpenRouter | API Key | `OPENROUTER_API_KEY` |
| Anthropic | API Key | `ANTHROPIC_API_KEY` |
| Nous Portal | OAuth | `hermes auth` |
| OpenAI Codex | OAuth | `hermes auth` |
| GitHub Copilot | Token | `COPILOT_GITHUB_TOKEN` |
| Google Gemini | API Key | `GOOGLE_API_KEY` |
| DeepSeek | API Key | `DEEPSEEK_API_KEY` |
| xAI / Grok | API Key | `XAI_API_KEY` |
| Hugging Face | Token | `HF_TOKEN` |
| Z.AI / GLM | API Key | `GLM_API_KEY` |
| MiniMax | API Key | `MINIMAX_API_KEY` |
| Kimi / Moonshot | API Key | `KIMI_API_KEY` |
| Alibaba / DashScope | API Key | `DASHSCOPE_API_KEY` |
| Xiaomi MiMo | API Key | `XIAOMI_API_KEY` |
| Kilo Code | API Key | `KILOCODE_API_KEY` |
| AI Gateway (Vercel) | API Key | `AI_GATEWAY_API_KEY` |
| Qwen OAuth | OAuth | `hermes login --provider qwen-oauth` |
| Custom Endpoint | Config | `model.base_url` + `model.api_key` |

---

## 📱 平台集成

| 平台 | 说明 |
|:-----|:-----|
| Telegram | 完整工具支持，支持 DM 主题 |
| Discord | 机器人集成，需要 Message Content Intent |
| Slack | 支持 DM 和频道订阅 |
| WhatsApp | 通过 API 集成 |
| Signal | 通过信号协议 |
| Email | IMAP/SMTP 邮件 |
| SMS | 短信集成 |
| Matrix | 去中心化聊天 |
| Mattermost | 自托管聊天 |
| Home Assistant | 智能家居联动 |
| DingTalk (钉钉) | 企业集成 |
| Feishu (飞书) | 企业集成，含文档/云盘工具 |
| WeCom (企业微信) | 企业集成 |
| BlueBubbles (iMessage) | macOS iMessage |
| Weixin (微信) | 微信集成 |
| API Server | Open WebUI 连接 |
| Webhooks | 自定义 Webhook 触发 |

---

## 🧠 记忆系统

| 系统 | 说明 |
|:-----|:-----|
| **MemOS** | 本地记忆宫殿（智能去重、混合检索、自动预检索） |
| **ChromaDB** | 向量数据库存储 |
| **知识图谱** | SQLite 存储实体关系三元组 |
| **Holographic** | 外部记忆 Provider（可选） |
| **Honcho** | Honcho 记忆集成（需插件） |

---

## 🔧 关键路径

```
~/.hermes/config.yaml          # 主配置文件
~/.hermes/.env                 # API 密钥和 secrets
~/.hermes/skills/              # 已安装技能
~/.hermes/sessions/            # 会话记录
~/.hermes/state.db             # 会话存储 (SQLite + FTS5)
~/.hermes/logs/                # 日志文件
~/.hermes/auth.json            # OAuth tokens 和凭证池
~/.hermes/memos-plugin/        # MemOS 配置
~/.hermes/profiles/            # 多配置文件
```

---

## 📖 学习路径

### 入门

1. 阅读 [[Hermes Agent]] 技能文档
2. 运行 `hermes setup` 交互式配置向导
3. 运行 `hermes doctor` 检查依赖和配置
4. 学习常用 CLI 命令和 Slash 命令

### 进阶

1. 掌握技能管理：`hermes skills list/install/update`
2. 配置多平台 Gateway：`hermes gateway setup`
3. 学习子代理委派：`delegate_task` 和 Cron Job
4. 配置 MCP 服务器：`hermes mcp add/list`

### 专家

1. 贡献技能：编写 SKILL.md 并发布
2. 自定义工具：扩展 tools/ 目录
3. 多代理协作：tmux + hermes -w 工作树模式
4. 深度调试：使用 debugging 工具集

---

## 🔗 相关资源

- [[Hermes Agent]] — 核心技能文档
- [[Hermes 能力地图]] — 生态系统可视化
- [[个人知识库]] — 知识库搭建指南
- [[MemOS 记忆宫殿]] — 记忆系统配置
- [[Office 工具链]] — 办公自动化配置

---

## 📝 贡献

欢迎提交 PR 添加新资源！遵循以下格式：

```markdown
| 资源名称 | 链接 | 说明 |
```

---

*最后更新：2026-05-24*
*维护者：Hermes Agent + 船长*
