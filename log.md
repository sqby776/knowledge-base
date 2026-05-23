# 知识库更新日志

## 2026-05-23

### 初始化

- **新增**：知识库目录结构创建完成
- **新增**：`SCHEMA.md` — 知识库规则文件
- **新增**：`index.md` — 总入口
- **新增**：`log.md` — 更新日志
- **新增**：`README.md` — 完整搭建方案文档

### Git 初始化

- **commit cce0306** — 初始提交：知识库结构 + 核心规则文件（7 files, 593 insertions）
- 分支：`main`
- 作者：sqby776 <sqby776@users.noreply.github.com>

### 测试文章编译

- **来源**：`01_inbox/articles/2026-05-23_RAG技术简析.md`
- **新增页面**：
  - `02_notes/concepts/Agentic-RAG.md` — Agentic RAG 概念页
  - `02_notes/concepts/向量数据库.md` — 向量数据库概念页
  - `02_notes/concepts/嵌入模型.md` — 嵌入模型概念页
- **更新页面**：
  - `02_notes/concepts/RAG.md` — 补充组件表格、演进路线、双链
- **更新**：
  - `index.md` — 添加新概念和实体链接
  - `07_moc/知识库地图.md` — 补充阅读路径

### 双链验证

编译后形成的双链网络：
```
RAG ←→ Agentic RAG
RAG ←→ 向量数据库
RAG ←→ 嵌入模型
RAG ←→ LLM Wiki
RAG ←→ 知识飞轮
向量数据库 ←→ 嵌入模型
Agentic RAG ←→ Hermes Agent
```

### 下一步

- [x] 在 Obsidian 中打开 `~/workspace/knowledge/` 作为 Vault
- [ ] 安装 Obsidian Git 插件并配置自动同步
- [ ] 在 Hermes 中设置 `WIKI_PATH` 环境变量
- [ ] 测试：放入一篇文章到 `01_inbox/articles/`
- [ ] 让 Hermes 编译，检查生成的页面和双链

---

*最后更新：2026-05-23*
