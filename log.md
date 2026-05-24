# 知识库更新日志

## 2026-05-24

### 补充规范体系（对照微信文章优化）

统编前端元数据（Frontmatter）+ 标签体系 + 页面生命周期管理，补齐了文章建议的规范缺口：

#### SCHEMA.md 新增章节
- **Frontmatter 规范** — 所有页面必须包含 `title/created/updated/tags/status/sources` YAML 头
- **标签治理** — 每页 1-3 个小写英文标签，按用途打标，新标签需注册
- **页面生命周期** — `draft → active → frozen → archived` 四阶段流转
- **编译工作流关键检查点** — Frontmatter 完整度 + 标签注册 + wikilink + 日志更新

#### index.md 新增
- **标签注册表** — 10 个已注册标签的索引表

#### 全库 Frontmatter 覆盖（44/46 页面）
- 10 个概念页添加 tags + status: active
- 13 个实体页添加 tags + status: active
- 6 个 MOC 页、5 个 README 页、5 个文章/方法页全覆盖
- 剩余 2 个空文件（LLM Wiki.md / 知识库集成.md）填充内容

### 自动化抓取体系搭建

#### 路线A：Camoufox/crawl4ai 网页抓取
- `scripts/auto-ingest.py` — 通用网页抓取入库脚本（支持 crawl4ai 后端）
- 测试通过：成功抓取 example.com 并保存到 `01_inbox/articles/`
- 支持手工触发：`python3 auto-ingest.py <URL> [--category articles|papers|transcripts]`

#### 路线B：OpenCLI + Python 微信抓取
- `scripts/auto-cli-capture.py` — 多源抓取脚本（微信文章/X趋势/公开搜索）
- OpenCLI v1.8.0 已安装（含 twitter/weixin/arxiv/v2ex 等 150+ 站点适配器）
- 微信文章 Python 直连抓取已测试通过
- 支持手工触发：`python3 auto-cli-capture.py <wechat_url>`

#### 编译工作流
- `scripts/compile-workflow.py` — 将 inbox 原始内容编译为结构化知识节点
- 支持预览模式（--dry-run）和单文件编译（--file <path>）

#### 定时任务
- Hermes cronjob `知识库每日自动抓取` — 每天 8:00 执行
- 使用 no_agent=True 模式 + daily-capture.sh 脚本
- 集成现有 `hermes_learner.sh`（6:00 检查版本更新）

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

### 检索功能测试

- **双链跳转**：index → RAG → Agentic RAG → RAG 双向链完整，28 个关联链接 0 缺失
- **跨会话记忆**：持久记忆写入 MEMORY.md 成功，系统 prompt 自动注入
- **新内容写入**：新增 `02_notes/methods/MemOS-实操笔记.md`
- **内容检索验证**：关键词"智能去重"命中新文件，检索正常

### 空目录填充（P1-P3）

7 个空目录全部填充完成：

| 目录 | 文件 | 说明 |
|:-----|:-----|:-----|
| `03_resources/pdfs/README.md` | PDF 资源索引 | 待下载 PDF 列表 + 使用规范 |
| `03_resources/links/README.md` | 外部链接索引 | 10 个学习站点完整链接 |
| `04_projects/current/README.md` | 当前项目 | 4 个项目追踪 + 里程碑 |
| `05_comparisons/README.md` | 工具对比 | 5 组对比（Hermes/Claude、嵌入模型、抓取工具等） |
| `06_queries/README.md` | 常见问题 FAQ | 15 个常见问题解答 |
| `08_drafts/README.md` | 草稿 | 草稿规范 + 模板 |
| `99_archive/README.md` | 归档 | 归档规则 + 目录结构 |

### 更新

- `index.md` — 补充目录说明表格，更新最近更新

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

### 自动入库 (2026-05-24)

| 文件 | 标题 | 来源 |
|:----|:----|:----|

| `01_inbox/articles/2026-05-24_Example_Domain.md` | Example Domain | 自动抓取 |

### Obsidian 插件配置

7 个社区插件已安装并配置：

| 插件 | 版本 | 配置内容 |
|:-----|:----:|:---------|
| **Dataview** | 0.5.68 | 4 组查询嵌入 index.md（最近修改/状态统计/标签分组/待完善） |
| **Omnisearch** | 1.29.2 | 全文搜索 + OCR 识别 |
| **Templater** | 2.20.5 | 4 个模板（概念页/实体页/MOC 页/收件箱）→ `templates/` |
| **QuickAdd** | 2.12.2 | 4 个宏（一键新建概念/实体/MOC/收件箱） |
| **Linter** | 1.31.2 | 6 条规则（Frontmatter/标题/列表/链接/行尾/文件末尾） |
| **Advanced Tables** | 0.23.2 | 表格编辑增强 |
| **Paste URL into selection** | 1.11.4 | URL 快捷插入 |

### 更新

- `index.md` — 新增 Dataview 数据面板（4 组查询）
- `.obsidian/linter-config.json` — Linter 规则配置
- `.obsidian/quickadd-config.json` — QuickAdd 宏配置
- `templates/` — 4 个 Templater 模板
