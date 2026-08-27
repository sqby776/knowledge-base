# 站点5：中文社区 FAQ（hermesagent.org.cn/docs/reference/faq）

> 抓取日期：2026-08-17 ｜ 状态：✅ 成功（HTTP 200） ｜ 信源层级：Tier 3（社区维护，内容翻译/镜像自官方）

## 知识点：国产模型生态 ✅ 变化
- **标题**：中文社区主推国产模型 Deepseek-V4 / GLM-5.2 / Minimax-M2.7 / Kimi-k2.6
- **摘要**：社区站点头部横幅在推广 Deepseek-V4、GLM-5.2、Minimax-M2.7、Kimi-k2.6 四个国产模型，并接入"优云智算 Agent Plan 套餐（49 元/月起，按次调用）"。FAQ 支持列表含 z.ai/ZhipuAI（GLM）、Kimi/Moonshot、MiniMax（全球及中国端点）。本机当前使用 deepseek-v4-flash 与主推模型线一致。
- **标签**：#模型 #国产 #deepseek #glm #kimi #minimax

## 知识点：国内镜像安装路径
- **标题**：res1.hermesagent.org.cn 镜像安装器
- **摘要**：Windows 原生：`irm https://res1.hermesagent.org.cn/install.ps1 | iex`；Linux/WSL2/Termux：`curl -fsSL https://res1.hermesagent.org.cn/install.sh | bash`。镜像版默认精简掉部分受外网影响的可选组件以提高成功率，装完后可要求 Hermes 补装。Termux（Android）官方支持，但 voice 附加功能不可用（faster-whisper→ctranslate2 无 Android wheels），须用 `.[termux]` 附加功能。
- **标签**：#安装 #镜像 #termux #windows

## 知识点：数据隐私与本地模型
- **标题**：无遥测 + 完整本地模型支持
- **摘要**：API 调用仅发往用户配置的 LLM 提供商；不收集遥测/使用/分析数据；对话、记忆、技能存本地 ~/.hermes/。本地模型支持 Ollama/vLLM/llama.cpp/SGLang/LocalAI，`hermes model` 选"自定义端点"或 config.yaml 配 `provider: custom`；本地端点自动放宽流式超时（读取 120s→1800s），可用 HERMES_STREAM_READ_TIMEOUT=1800 手动调整；Ollama 注意 num_ctx 与 Hermes 上下文长度一致（/api/show 报的是最大而非有效值）。
- **标签**：#隐私 #本地模型 #ollama #超时

## 知识点：多用户与 Python 库
- **标题**：多用户共用实例 + AIAgent Python 库
- **摘要**：消息网关支持多用户共用实例，白名单（用户 ID）/私信配对控制访问。Python 项目可 `from run_agent import AIAgent` 直接调用。
- **标签**：#多用户 #python库 #gateway

## 知识点：常见故障排除
- **标题**：安装/启动/模型三个高频问题
- **摘要**：① hermes: command not found → source ~/.bashrc 或确认 ~/.local/bin 在 PATH（安装器不要求 sudo）；② Python 过旧 → 要求 3.11+；③ uv not found → `curl -LsSf https://astral.sh/uv/install.sh | sh`；④ API key 无效 → hermes model 重配；还有本地模型超时、Ollama num_ctx 等技术细节。
- **标签**：#故障排除 #安装 #troubleshooting
