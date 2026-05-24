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

### 微信自动汇报

新增知识库日报微信汇报功能：

| 项目 | 内容 |
|:-----|:-----|
| **脚本** | `~/workspace/scripts/daily-report.sh` |
| **调度** | 每天 8:00 自动运行（crontab） |
| **发送条件** | 有新内容/待编译/双链断裂时发送 |
| **日报文件** | `~/workspace/data/daily-report-YYYYMMDD.md` |
| **日志** | `~/workspace/data/knowledge-daily-report.log` |

**汇报内容：**
- 📊 知识库概览（总文件/今日新增/待编译/待完善）
- 🔗 双链状态（总链接/断裂链接）
- 🧠 记忆系统（MEMORY.md 条目数）
- 📝 近期 Git 提交

**测试验证：**
- ✅ `hermes send` 微信发送成功
- ✅ `daily-report.sh` 脚本运行正常
- ✅ crontab 配置生效（每天 8:00）

### 更新

- `index.md` — 新增 Dataview 数据面板（4 组查询）
- `.obsidian/linter-config.json` — Linter 规则配置
- `.obsidian/quickadd-config.json` — QuickAdd 宏配置
- `templates/` — 4 个 Templater 模板

---

## 2026-05-24 双链修复

### 问题
发现 54 个断裂双链链接

### 修复方案

| 类型 | 数量 | 处理方式 |
|:-----|:-----|:---------|
| 模板占位符 | 5 | 替换为真实链接 |
| 路径格式链接 | 4 | 去掉 `.md` 后缀 |
| 模板示例 | 3 | 替换为真实链接 |
| 真实缺失页面 | 32 | 创建占位页面 |
| 其他断裂 | 10 | 创建页面或重定向 |

### 创建页面

**entities (15 个):**
- 版本管理、个人知识库、工作流自动化、批量处理、批量转换、数据汇总
- 双链链接、微信日报、文档处理、文档格式、文档归档、文件编码
- 智能报表、智能文档、AI 文档生成、OCR 识别、Office 工具链、python-docx
- LibreOffice、Python Office 库

**concepts (13 个):**
- 文本分块、知识编译流程、知识图谱、Milvus、Pinecone、Qdrant
- hermes-agent、MemOS 记忆宫殿、Obsidian、web-scraping
- Awesome Hermes Agent、Hermes 能力地图、Agentic RAG、Hermes Agent、Python Office 库、Tesseract OCR

**links (2 个):**
- PDF 资源索引、wikilink

**methods (1 个):**
- 定时抓取

**projects (1 个):**
- 当前项目

**moc (1 个):**
- 办公自动化地图

### 结果
✅ 所有双链断裂已修复，0 个剩余断裂链接

| `01_inbox/articles/2026-05-24_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-05-24_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-05-24_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-05-24_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-05-24_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-05-24_未命名文章.md` | 未命名文章 | 自动抓取 |

| `01_inbox/articles/2026-05-24_404_Not_Found.md` | `404` — Not Found 😢🐍 | 自动抓取 |

| `01_inbox/articles/2026-05-24_404_Not_Found.md` | `404` — Not Found 😢🐍 | 自动抓取 |

| `01_inbox/articles/2026-05-24_python_docxhttpspython_docxreadthedocsioenlatestpython_docx_.md` | python-docx[¶](https://python-docx.readthedocs.io/en/latest/#python-docx "Permalink to this headline") | 自动抓取 |

| `01_inbox/articles/2026-05-24_openpyxl_A_Python_library_to_readwrite_Excel_2010_xlsxxlsm_f.md` | openpyxl - A Python library to read/write Excel 2010 xlsx/xlsm files[](https://openpyxl.readthedocs.io/en/latest/#openpyxl-a-python-library-to-read-write-excel-2010-xlsx-xlsm-files "Link to this heading") | 自动抓取 |

| `01_inbox/articles/2026-05-24_python_pptxhttpspython_pptxreadthedocsioenlatestpython_pptx_.md` | python-pptx[¶](https://python-pptx.readthedocs.io/en/latest/#python-pptx "Permalink to this headline") | 自动抓取 |

---

## 2026-05-24 知识库完善

### 文章迁移

- `raw/卡兹克文风skill与知识库构建-微信公众号2026-05-24.md` → `01_inbox/articles/2026-05-24_卡兹克文风skill与知识库构建.md`
- raw 目录清空，所有文章统一归入 01_inbox/articles/

### 目录结构完善

创建缺失目录：
- `03_resources/documents/` — 文档资源索引（README.md）
- `03_resources/templates/` — 模板资源索引（README.md）

### 双链修复（第二轮）

修复 16 个缺失概念页面：

| 页面 | 位置 | 说明 |
|:-----|:-----|:-----|
| 版本管理 | 02_notes/concepts/ | Git 管理文档 |
| 工作流自动化 | 02_notes/concepts/ | 端到端流程自动化 |
| 智能报表 | 02_notes/concepts/ | 数据驱动报告 |
| 智能文档生成 | 02_notes/concepts/ | LLM 辅助写作 |
| AI 文档生成 | 02_notes/concepts/ | AI 辅助文档 |
| 定时抓取 | 02_notes/concepts/ | Cron Job 定时任务 |
| 微信日报 | 02_notes/concepts/ | 自动汇报功能 |
| 文本分块 | 02_notes/concepts/ | RAG 文本处理 |
| 文档处理 | 02_notes/concepts/ | Word/Excel/PPT 处理 |
| 文档格式 | 02_notes/concepts/ | 文档基础格式 |
| 文档归档 | 02_notes/concepts/ | 文件分类存储 |
| 文件编码 | 02_notes/concepts/ | UTF-8 与兼容性 |
| 批量处理 | 02_notes/concepts/ | 多文件操作 |
| 批量转换 | 02_notes/concepts/ | 格式转换脚本 |
| 数据汇总 | 02_notes/concepts/ | Excel 数据处理 |
| 智能文档 | 02_notes/concepts/ | 模板化生成 |

### 当前状态

- 总 Markdown 文件：77 个（新增 17 个）
- 概念页面：26 个
- 实体页面：13 个
- 方法页面：2 个
- MOC 地图：6 个
- 文章/草稿：9 个

---

*维护者：Hermes Agent + 船长*
