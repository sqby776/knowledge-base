# AI Agent 的万能遥控器：[[CLI-Anything]] 让所有软件都能被智能体直接调用

来源: 时之AI测评 | 来源URL: https://mp.weixin.qq.com/s/wHr19Ay1_OW4qTnzqqEINQ
分类: 开源工具/AI Agent | 日期: 2026-06-02
标签: [AI Agent, CLI, 开源, HKUDS, 软件自动化, Claude Code]

---

## 项目概述

[HKUDS/[[CLI-Anything]]](https://github.com/HKUDS/[[CLI-Anything]]) 是香港大学开源项目，核心功能：用 AI 自动生成任意 GUI/API 软件的命令行封装，让 AI Agent 能通过 CLI 直接操控专业软件。

## 解决的问题

AI Agent 能写代码、调 API，但对 GUI 软件无能为力。Claude Code、Pi 等 Agent 只能通过命令行交互，而 Blender、GIMP、FreeCAD 等专业软件没有 CLI 接口。

## 工作原理

1. **分析** — 扫描软件源代码或 API，把 GUI 操作映射为可调用的功能
2. **设计** — 规划命令组、状态模型和输出格式
3. **实现** — 用 Python Click 生成 CLI 代码，自带 REPL、JSON 输出、撤销/重做
4. **测试** — 自动生成测试套件，超 2280 个测试 100% 通过
5. **文档** — 更新 SKILL.md 技能定义，让 Agent 能自动发现
6. **发布** — 生成 setup.py，安装到 PATH

用户只需一条命令（如 `/cli-anything ./gimp`），AI 代理自动完成全部流程。

## CLI-Hub 生态

配套集中式仓库，`pip install cli-anything-hub` 安装后浏览管理所有 CLI 封装：

- **Blender CLI** — 3D 建模与渲染自动化
- **GIMP CLI** — 图像处理
- **FreeCAD CLI** — 工业设计（258 条命令、17 个命令组）
- **Zotero CLI** — 文献管理
- **Obsidian CLI** — 知识库操作
- **Kdenlive CLI** — 视频编辑
- **Safari CLI** — 浏览器自动化（基于 [[Agent 浏览器自动化 Chrome DevTools MCP 接入实战]]）
- **Godot CLI** — 游戏引擎控制
- **MuseScore CLI** — 乐谱编辑

每个 CLI 有 CI 测试和 SKILL.md，支持 pip/npm/brew 安装。

## 为什么用 CLI 路线

- **结构化** — JSON 输出，LLM 易于处理
- **轻量** — 无图形依赖，适合服务器/无头环境
- **自描述** — `--help` 就是天然文档
- **确定** — 输出格式固定，Agent 不需要猜
- **通用** — Claude Code 每天通过 CLI 运行成千上万真实工作流

## 与当前 Hermes 系统的关联

### 直接参考价值
1. **技能定义标准化** — SKILL.md 让 Agent 自动发现 CLI 能力，与现有 skills 体系理念一致
2. **角色分离** — 作者写 CLI，执行者只通过 CLI 接口操作，信息不对称暴露缺陷
3. **测试驱动** — 每个封装都有 CI 测试，确保稳定性

### 可能的集成方向
1. **[[Agent 浏览器自动化 Chrome DevTools MCP 接入实战]] + CLI 互补** — 现有 chrome-devtools-mcp 控制浏览器，[[CLI-Anything]] 补充桌面软件
2. **技能自动发现** — SKILL.md 模式可直接复用到 Hermes skills 体系
3. **CLI 封装现有工具** — 我们的 officecli、wx-cli 等本身就是这种思路的产物

## 关键洞察

[[CLI-Anything]] 的核心洞见：**CLI 是人和 Agent 都能理解的通用界面**。它不改变软件本身，而是在外面包一层命令行壳。这比 [[Agent 浏览器自动化 Chrome DevTools MCP 接入实战]] 更轻量，比 GUI 自动化更可靠。

AI Agent 正在从"只会聊天"进化到"能干实事"，CLI 封装层可能是关键的桥梁。

## 参考资料

- 项目地址: https://github.com/HKUDS/[[CLI-Anything]]
- CLI-Hub: `pip install cli-anything-hub`
- 原文: https://mp.weixin.qq.com/s/wHr19Ay1_OW4qTnzqqEINQ
