# 知识库更新日志

## 2026-05-24

### 双链修复（P0 紧急）

修复 20 个双链断裂问题，创建缺失页面：

#### 概念页（6 个）

- `02_notes/concepts/LLM-Wiki.md` — LLM Wiki 定义与实现
- `02_notes/concepts/MOC.md` — Map of Content 主题地图
- `02_notes/concepts/知识飞轮.md` — 知识自我进化机制
- `02_notes/concepts/双链交叉引用.md` — 双向链接机制
- `02_notes/concepts/Source-first.md` — 源头优先原则
- `02_notes/concepts/本地知识库.md` — 本地知识库概念

#### 实体页（12 个）

- `02_notes/entities/Camoufox.md` — 反爬网页抓取工具
- `02_notes/entities/crawl4ai.md` — 批量抓取框架
- `02_notes/entities/scrapling.md` — 轻量静态抓取
- `02_notes/entities/MemOS.md` — 记忆操作系统
- `02_notes/entities/MemPalace.md` — 记忆宫殿管理
- `02_notes/entities/Chroma.md` — 向量数据库
- `02_notes/entities/BGE.md` — 智源嵌入模型
- `02_notes/entities/M3E.md` — Moka 混合嵌入模型
- `02_notes/entities/LibreOffice.md` — 开源办公套件
- `02_notes/entities/Tesseract-OCR.md` — OCR 引擎
- `02_notes/entities/Python-Office-库.md` — Python Office 库集合

#### 主题地图（2 个）

- `07_moc/AI 技术地图.md` — AI 技术领域导航
- `07_moc/Hermes 技能地图.md` — Hermes 技能分类导航

### 新增内容

- `07_moc/awesome-hermes-agent.md` — Hermes 资源总入口
- `07_moc/hermes-ecosystem.md` — Hermes 能力地图
- `02_notes/methods/office-automation.md` — 办公自动化方法库
- `02_notes/entities/office-tools.md` — 办公工具实体页
- `07_moc/办公自动化地图.md` — 办公自动化主题地图

### 技能安装

- `web-search-enhanced` — 增强版网页搜索
- `meeting-notes` — 会议转写整理

### 测试验证

- `meeting-notes` 技能测试成功，输出高质量会议纪要

### 更新

- `index.md` — 补充嵌入模型分类，添加新实体页链接
- `log.md` — 记录本次修复

---

## 2026-05-23

### 新增

- 知识库基础结构创建
- `01_inbox/` — 原始资料目录
- `02_notes/concepts/` — 概念页目录
- `02_notes/entities/` — 实体页目录
- `02_notes/methods/` — 方法论目录
- `03_resources/` — 外部资料目录
- `04_projects/` — 项目内容目录
- `05_comparisons/` — 比较页目录
- `06_queries/` — 问答目录
- `07_moc/` — 主题地图目录
- `08_drafts/` — 草稿目录
- `99_archive/` — 归档目录
- `SCHEMA.md` — 知识库规则文件
- `index.md` — 总入口索引
- `log.md` — 更新日志
- `README.md` — 完整配置指南
- `07_moc/知识库地图.md` — AI 技术主题地图

### 编译测试

- 测试文章编译 → 3 个新概念页 + RAG 页更新
- 新增：[[Agentic RAG]]、[[向量数据库]]、[[嵌入模型]]
- 20+ 双链建立

---

*维护者：Hermes Agent + 船长*
