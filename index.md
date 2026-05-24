# 个人知识库 Index

## 核心概念

- [[RAG]]
- [[Agentic RAG]]
- [[LLM Wiki]]
- [[MOC]]
- [[知识飞轮]]
- [[双链交叉引用]]
- [[Source-first]]
- [[本地知识库]]
- [[向量数据库]]
- [[嵌入模型]]

## 嵌入模型

- [[BGE]] — 智源嵌入模型
- [[M3E]] — Moka 混合嵌入模型

## 工具与实体

- [[Hermes Agent]]
- [[Obsidian]]
- [[Camoufox]]
- [[crawl4ai]]
- [[scrapling]]
- [[MemOS]]
- [[MemPalace]]
- [[Chroma]]
- [[LibreOffice]]
- [[Tesseract OCR]]
- [[Python Office 库]]

## 主题地图

- [[知识库地图]]
- [[AI 技术地图]]
- [[Hermes 技能地图]]
- [[Hermes 能力地图]] — 生态系统全景
- [[Awesome Hermes Agent]] — 精选资源目录

## 办公自动化

- [[办公自动化]] — 文档处理工作流
- [[LibreOffice]] — 开源办公套件
- [[Obsidian]] — 本地知识库
- [[Tesseract OCR]] — 文字识别
- [[Python Office 库]] — 自动化核心
- [[办公自动化地图]] — 学习路线图

## 标签注册表

> 所有标签必须先在此注册，新增标签请追加到列表末尾。

| 标签 | 用途 | 状态 |
|:----|:----|:----:|
| `rag` | 检索增强生成相关 | ✅ |
| `knowledge-base` | 知识库搭建相关 | ✅ |
| `workflow` | 工作流/流程 | ✅ |
| `config` | 配置相关 | ✅ |
| `tutorial` | 教程/操作方法 | ✅ |
| `tool` | 工具介绍 | ✅ |
| `ai-agent` | AI Agent 相关 | ✅ |
| `automation` | 自动化相关 | ✅ |
| `draft` | 草稿/待完善 | ✅ |
| `archived` | 已归档 | ✅ |

## 数据面板 (Powered by Dataview)

> 以下内容在 Obsidian 中实时渲染，显示知识库的动态数据。

### 最近修改的 10 个页面

```dataview
TABLE file.frontmatter.tags AS 标签, file.mday AS 最后修改
FROM "02_notes" OR "07_moc"
SORT file.mday DESC
LIMIT 10
```

### 各状态页面统计

```dataview
TABLE length(rows) AS 数量
FROM "02_notes" OR "01_inbox" OR "07_moc"
GROUP BY status
SORT status ASC
```

### 按标签分组

```dataview
TABLE rows.file.link AS 页面列表
FROM "02_notes"
FLATTEN tags AS tag
GROUP BY tag
SORT tag ASC
```

### 待完善页面（status=draft）

```dataview
TABLE file.frontmatter.tags AS 标签, file.cday AS 创建日期
FROM "02_notes" OR "07_moc"
WHERE status = "draft"
SORT file.cday ASC
```

## 最近更新

> 2026-05-24：修复 20 个双链断裂页面，填充 7 个空目录全部内容

### 目录说明

| 目录 | 内容 | 状态 |
|:-----|:-----|:-----|
| `01_inbox/` | 原始资料、文章 | ✅ 已启用 |
| `02_notes/` | 知识节点（概念/实体/方法） | ✅ 已启用 |
| `03_resources/pdfs/` | 核心文章 PDF 索引 | 📥 待下载文件 |
| `03_resources/links/` | 外部资源链接 | ✅ 已填充 |
| `04_projects/current/` | 当前项目追踪 | ✅ 已填充 |
| `05_comparisons/` | 工具对比分析 | ✅ 已填充 |
| `06_queries/` | 常见问题 FAQ | ✅ 已填充 |
| `07_moc/` | 主题地图 | ✅ 已填充 |
| `08_drafts/` | 草稿 | ✅ 已填充 |
| `99_archive/` | 归档 | ✅ 已填充 |

---

*最后更新：2026-05-24*
