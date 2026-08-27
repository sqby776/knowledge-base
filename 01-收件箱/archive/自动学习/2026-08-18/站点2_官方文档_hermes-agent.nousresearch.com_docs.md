# 站点2：官方文档（hermes-agent.nousresearch.com/docs）

> 抓取日期：2026-08-17 ｜ 状态：✅ 成功 ｜ 信源层级：Tier 1

## 知识点：文档站结构（36 个链接）
- **标题**：文档分区目录
- **摘要**：Getting Started（quickstart/installation/platform-support/learning-path）、User Guide（cli/features: overview,tools,memory,skills,mcp,voice-mode,personality,context-files/configuration/messaging/security）、Integrations（nous-portal 等）、Guides（run-nemotron-3-ultra-free、use-mcp-with-hermes、use-voice-mode-with-hermes、tips）、Developer Guide（architecture/contributing）、Reference（cli-commands/faq）。
- **标签**：#文档 #结构 #导航

## 知识点：官方简体中文文档上线 ✅ 新增
- **标题**：/docs/zh-Hans/ 官方中文版
- **摘要**：官方站在英文版之外正式提供简体中文文档（此前只有英文）。中文版覆盖 Getting Started、Using Hermes、Features、Messaging、Integrations、Guides、Developer Guide、Reference 全部分区，含"Windows 原生（PowerShell）早期测试版"与"Android（Termux）"安装说明。中文用户查文档的权威来源从"无"变为"有"。
- **标签**：#中文文档 #zh-Hans #新增

## 知识点：llms.txt / llms-full.txt 路径迁移 ✅ 变化
- **标题**：机器可读文档从根路径迁移到带内容 hash 的静态文件
- **摘要**：根路径 `/llms.txt`、`/llms-full.txt` 均返回 404（此前可直接访问）。新路径：`/docs/assets/files/llms-<contenthash>.txt`。文件名内嵌 SHA 前缀：llms-`faaf9398`aa5828403fd56f6be7989c9f（内容与 2026-08-01 记录一致，稳定）与 llms-full-`9595dc2b`bf3e7e986e462807f6de2433（内容已更新，3.78 MB）。即：索引文件不变，全文版有 8 月新内容。
- **标签**：#llms.txt #知识摄取 #迁移

## 知识点：Windows 原生安装（早期测试版）✅ 新增
- **标题**：PowerShell 原生安装路径
- **摘要**：官方提供 Windows 原生安装（此前需 WSL2）：`iex (irm https://hermes-agent.nousresearch.com/install.ps1)`，标记为"早期测试版"。安装器自动检测 Termux（Android）。
- **标签**：#Windows #PowerShell #安装

## 知识点：部署形态
- **标题**：可部署在任何地方
- **摘要**：官方文档称 Hermes 可部署在 5 美元 VPS、GPU 集群或 serverless 基础设施（Daytona、Modal），不依赖本地电脑；支持 Telegram 上对话 + 云端虚拟机干活。
- **标签**：#部署 #serverless #VPS
