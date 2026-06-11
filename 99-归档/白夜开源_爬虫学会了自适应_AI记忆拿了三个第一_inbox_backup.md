![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/xeyMv0CewrZE5P45lYtCslBaU1ROQAMwh9s6JYNauAmTwAjew1icric9RytBG0gib2wuQGteMRHuSibMuibF48PZ6QngU8Z2LJefeZSTIoX94twM/0?wx_fmt=jpeg)

# 白夜开源：爬虫学会了自适应，AI记忆拿了三个第一

旧时白夜

在小说阅读器中沉浸阅读

## 01 | Scrapling：网站改版它不怕，反爬系统它绕过

做爬虫最烦什么？网站一改版，选择器全废。Cloudflare一升级，请求全被拦。

Scrapling解决这两个痛点的方式很暴力：选择器会"自适应"——网站改了结构，它能自动重新定位元素。反爬系统？内置StealthyFetcher，Cloudflare Turnstile直接绕过。

我研究了一下它的架构，发现它不只是个爬虫库，是个完整的爬虫框架。Scrapy风格的Spider API、并发控制、断点续爬、代理轮换、MCP Server给AI用——一条龙。Python写的，92%测试覆盖率，实战打磨了一年多。

跟CloakBrowser那种浏览器级隐身不同，Scrapling走的是"快+聪明"路线。HTTP请求模拟浏览器TLS指纹，不需要启动真实浏览器，速度比Playwright快一个量级。

⭐ 58,240+ | Python | BSD-3-Clause

🔗 github.com/D4Vinci/Scrapling

---

## 02 | Supermemory：AI记忆引擎，三个Benchmark全第一

你的AI每次聊天都从零开始，像金鱼一样只有7秒记忆。Supermemory就是给AI装个脑子。

它自动从对话中提取事实、构建用户画像、处理知识更新和矛盾、遗忘过期信息。LongMemEval、LoCoMo、ConvoMem三个AI记忆Benchmark全是第一。

我注意到一个细节：它区分了"记忆"和"RAG"。RAG是搜文档，谁搜都一样。记忆是记住"这个用户刚从纽约搬到了旧金山"，下次聊天自动更新。两者合一，一次查询同时返回知识库文档和个性化上下文。

一行代码接入：`npx install-mcp`装好MCP，Claude Code、Cursor、Windsurf全支持。也有Python/JS SDK，Vercel AI SDK、LangChain、OpenAI Agents SDK都有集成。

⭐ 24,092+ | TypeScript | MIT License

🔗 github.com/supermemoryai/supermemory

---

## 03 | Heretic：一键移除AI审查，社区已产出3000+模型

这个项目争议性拉满。Heretic能全自动移除语言模型的安全审查（censorship），不需要任何专业知识，一行命令搞定。

原理是directional ablation——找到模型内部"拒绝回答"的方向，然后把那个方向抹掉。关键是它用Optuna做参数优化，自动找到"移除审查但保留智能"的最佳平衡点。实测结果：Gemma-3-12b-it移除审查后，拒绝率从97%降到3%，但KL散度只有0.16——比手动调的版本损伤小得多。

说实话我不知道该怎么评价这个项目。技术上是真厉害，全自动、低损伤、支持MoE和混合架构。但用途……社区已经用Heretic产出了3000+个去审查模型。这把刀太锋利了。

⭐ 23,084+ | Python | AGPL-3.0

🔗 github.com/p-e-w/heretic

---

## 04 | oh-my-pi：把IDE完整接入AI编程Agent

现在的AI编程Agent，要么只能读写文件，要么得靠shell命令调外部工具。oh-my-pi不一样——它把LSP、DAP调试器、浏览器、Python/JS运行时全接入了Agent。

我试了一下它的LSP集成：让Agent重命名一个变量，它走的是workspace/willRenameFiles，所有引用自动更新。不是正则替换，是语义级别的重构。调试器也是真的——C程序segfault了，Agent自动attach lldb，步进到坏指针，读调用栈。

Rust写的核心，27k行，32个内置工具。一行命令安装，macOS/Linux/Windows原生支持，不依赖WSL。40+模型提供商，每个模型的提示词都单独调过。

⭐ 9,531+ | Rust | MIT License

🔗 github.com/can1357/oh-my-pi

---

## 05 | VoxCPM2：无Tokenizer语音生成，30种语言48kHz

大多数TTS系统先把语音切成离散token，再让语言模型预测。VoxCPM2跳过了这一步——直接在连续潜空间里生成语音，用扩散自回归架构。

效果：30种语言直接合成，不需要指定语言标签。Voice Design功能可以用自然语言描述来创建全新声音——"年轻女性，温柔甜美"，不需要参考音频。可控声音克隆：给一段参考音频，再用文字控制情绪和语速。48kHz输出，不需要外部上采样器。

2B参数，200万小时多语言数据训练。RTX 4090上实时率0.3，用Nano-vLLM加速到0.13。Apache 2.0开源，可商用。

⭐ 24,373+ | Python | Apache-2.0

🔗 github.com/OpenBMB/VoxCPM
