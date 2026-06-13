# 中文社区FAQ (hermesagent.org.cn)
> Source: https://hermesagent.org.cn/docs/reference/faq
> Fetch time: 2026-06-12

## 核心概览
- 免费开源 (MIT)，仅支付LLM提供商API费用
- 不收集遥测、使用数据或分析信息
- 对话记录、记忆、技能本地存储在 ~/.hermes/

## 支持的LLM提供商
- 推荐: OpenRouter (一个API密钥访问数百种模型)
- 其他: Nous Portal, OpenAI (GPT-4o, o1, o3), Anthropic (Claude), Google (Gemini), z.ai (GLM), Kimi, MiniMax
- 本地模型: Ollama, vLLM, llama.cpp, SGLang

## Python 集成示例
```python
from run_agent import AIAgent
agent = AIAgent(model="openrouter/nous/hermes-3-llama-3.1-70b")
response = agent.chat("Explain quantum computing briefly")
```

## 安装
- **Windows**: `irm https://res1.hermesagent.org.cn/install.ps1 | iex` (原生PowerShell)
- **WSL2**: `curl -fsSL https://res1.hermesagent.org.cn/install.sh | bash`
- **Android/Termux**: 支持，需 `.[termux]` 附加功能

## 常见安装故障
- `hermes: command not found` → `source ~/.bashrc`
- Python 要求 3.11+
- `uv: command not found` → 安装uv
- 不要用sudo运行安装程序

## 配置文件 (Profiles)
- 彼此隔离的配置空间（类似"工作号/个人号"）
- 独立模型、记忆、技能和会话
- 不共享记忆或会话（除非 `--clone-all`）
- 导出/导入: `hermes profile export/work ./work-backup.tar.gz`

## 消息网关
- Telegram特定优化: `display.tool_progress: "off"` 隐藏推理细节
- Telegram斜杠命令限制100个，可用 `platform_disabled` 禁用

## 性能与Token管理
- `/compress` 压缩当前会话
- `/usage` 检查Token使用情况
- `/continue` 恢复旧会话

## MCP问题
- 连接失败: `uv pip install -e ".[mcp]"`
- 工具未显示: `/reload-mcp`
- 超时: 检查服务器日志

## 多模型委派
```yaml
delegation:
  model: "google/gemini-3-flash-preview"
  provider: "openrouter"
```

## 首次运行400错误
- 原因: 模型名称不匹配或API密钥无权
- 解决: `hermes model` 重新选择，或测试 `hermes chat -q "hello" --model anthropic/claude-sonnet-4.6`
