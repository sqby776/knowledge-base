# 知识库更新日志

## 2026-05-23

### 初始化

- **新增**：知识库目录结构创建完成
- **新增**：`SCHEMA.md` — 知识库规则文件
- **新增**：`index.md` — 总入口
- **新增**：`log.md` — 更新日志
- **新增**：`README.md` — 完整搭建方案文档

### 来源

- 参考四篇微信公众号文章：
  - 超级猛：《我又把 Obsidian 知识库升级了：现在它能自己长出知识网络》
  - 桃哥：《我如何用 AI Agent 管理个人知识库：Hermes + Obsidian + LLM Wiki》
  - 徒手开榴莲：《Obsidian 个人知识库搭建实录：安装、配置与同步全流程》
  - 芋头小宝：《Hermes+AutoCLI+Obsidian：打造自动入库、自动整理、自动微信汇报的知识系统》

### 新增页面

- **02_notes/concepts/RAG.md** — RAG 概念页
- **02_notes/entities/Hermes-Agent.md** — Hermes Agent 实体页
- **07_moc/知识库地图.md** — 知识库主题地图

### Git 初始化

- **commit cce0306** — 初始提交：知识库结构 + 核心规则文件（7 files, 593 insertions）
- 分支：`main`
- 作者：sqby776 <sqby776@users.noreply.github.com>

### 下一步

- [ ] 在 Obsidian 中打开 `~/workspace/knowledge/` 作为 Vault
- [ ] 安装 Obsidian Git 插件并配置自动同步
- [ ] 在 Hermes 中设置 `WIKI_PATH` 环境变量
- [ ] 测试：放入一篇文章到 `01_inbox/articles/`
- [ ] 让 Hermes 编译，检查生成的页面和双链
