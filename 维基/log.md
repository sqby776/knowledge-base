## 2026-06-22

### 摄取
- **来源**: 6 个来自 03_Resources/公众号文章/ + 6 个来自 01-收件箱/自动学习/
- **新建 source 页**: 12 个
- **新建 entity 页**: 7 个（ATS、Agent Reach、Agnes、Office、SQLite、Git、Docker）
- **更新 entity 页**: 3 个（Hermes、Nous-Research、Skills）
- **跳过**: 10 个自动捕获重复文件（主题已覆盖，仅更新哈希）
- **工具**: qmd 不可用，使用 search_files 替代

### 新增内容类别
1. 微信公众号资源（6篇）: 简历AI提示词、Agent Reach联网神器、Agnes模型集成、SQLite经营分析数据基座、build-your-own-x造轮子指南、OfficeCLI自动化工具
2. Hermes Agent 自动学习（6篇）: 官网核心信息、官方文档导航、GitHub仓库统计（199k Stars）、中文文档站、中文社区FAQ、中文快速入门

### 归档
- 待归档: 10 个自动学习 + 10 个自动捕获文件
- 03_Resources 为资源收藏，暂不归档

### 注意
- 10 个自动捕获文件（2026-06-22版）内容与旧版不同但主题已覆盖，未重新处理
- qmd 未安装，搜索功能受限

---
title: 维护日志
updated: 2026-06-12
---

# 维护日志

## 2026-06-12

### 归档
- 归档 18 个收件箱文件到 99-归档/2026-06-12/
  - 自动学习: agentskills.md, discord.md, github.md, hermes-cn-docs.md, hermes-cn-faq.md, hermes-docs.md, hermes-home.md, huasheng.md, runoob.md, x-post.md, 学习报告_2026-06-12.md
  - 自动捕获: 7 个 Python 文档源文件
  - 01_inbox/articles: 8 个文件（其中 7 个与自动捕获重复，1 个内容不同）

### 去重清理
- 删除 21 个碎片化"_学习要点"文件（<1200 bytes，信息密度零）
- 删除 3 个 Hermes Agent 标题完全重复文件：
  - Hermes_Agent_2026-06-10.md（重复）
  - HermesAgent.md（重复）
  - Hermes_Agent.md（重复）
  - 保留 Hermes-Agent.md（概念/，12613 bytes，信息最完整）

### 收件箱状态
- 所有 5 个收件箱位置已清空（0 个 .md 文件）

### 笔记目录统计
- 实体/: 96 个文件
- 概念/: 38 个文件
- 方法/: 46 个文件
- 架构/: 1 个文件

### 待处理
- 维基 23 个 source 页面中，约 20 个没有对应的 02-笔记（多为测试文件和旧文章）
- 地图文件 wikilinks 未更新（但地图本身不需要每次维护都刷新）

## 2026-06-13

### 编译
- 编译 Hermes Agent 官方文档首页到维基
  - 来源: 01_inbox/articles/2026-06-13_Hermes_Agent.md（hermes-agent.nousresearch.com/docs）
  - 新建维基 source 页: Hermes-Agent-官方文档首页.md
  - 自动编译到 02-笔记/概念/Hermes-Agent.md

### 归档
- 归档 10 个收件箱文件到 99-归档/2026-06-13/
  - 01_inbox/articles: 10 个文件（9 个为重复捕获，1 个 Hermes_Agent.md）
  - 跨目录去重: 删除 9 个 archive/自动捕获/ 中的重复文件

### 去重清理
- 删除 9 个碎片化 _学习要点 文件（<1200 bytes，实体/目录残留）

### 笔记目录统计
- 实体/: 96 个文件（删除 9 个碎片）
- 概念/: 38 个文件
- 方法/: 46 个文件
- 架构/: 1 个文件

### 收件箱状态
- 所有收件箱位置已清空（0 个 .md 文件）
## 2026-06-22

### llmwiki-ingest 维护记录

- **新建来源页面**: 17 个
  - 自动学习/ → 7 个 source 页面
  - 自动捕获/ → 10 个 source 页面
- **Manifest**: 重建，已从 24 条旧条目（全部死引用）迁移为索引新来源
- **Index**: 重建，统一格式

注：旧 manifest 中 `01-收件箱/文章/` 下 24 个源文件路径已无法恢复（源文件已删除/迁移），已全部清理。

## 2026-06-29 (周一维护)

- **健康检查**: 执行完整巡检
- **增量摄取**: 新增 1 个来源页面 (awesome-evals)
- **来源漂移**: 30 个 manifest 条目源文件在归档后失效（标准漂移）
- **损坏链接**: 12 个断裂 wikilinks（6 个 Python/pandas 概念缺页，6 个来源标题不匹配）
- **状态**: 索引同步率 98/99（1 个 README 未入索引），无内容矛盾


---

## 2026-06-29

- **摄取**: 6 个新来源（03_Resources/公众号文章）
  - Agent Reach（AI Agent联网）
  - Agnes-2.0-Flash（多模态集成）
  - AI写简历15个提示词（ATS优化）
  - Python+SQLite（经营分析数据基座）
  - build-your-own-x（造轮子地图）
  - OfficeCLI（Agent原生Office）
- **更新实体页**: Agent Reach、Agnes、ATS、Office、SQLite
- **总计**: 37 sources tracked, 107 wiki pages

## 2026-07-13 (周一维护)

### 健康检查
- **损坏链接**: 0（上周12个，已全部修复 ✅）
- **孤立页面**: 13个（多为source页，入链偏少，但均为normal pattern）
- **缺frontmatter**: 11页（6个entity + 5个source，缺少title/type/created/updated）
- **短页面**: 10个stub + 46个skeleton（大部分concept页为骨架）
- **索引**: 2页未入索引（contradictions/README + awesome-evals source页）
- **来源漂移**: 22个manifest条目源文件已归档（继续保留ARCHIVED标记）
- **未解决矛盾**: 1个（README占位文件）
- **健康评分**: 85/100（无损坏链接是亮点，缺frontmatter和短页面为老问题）

### 增量摄取
- **跳过所有候选文件**（31个候选 → 0个处理）：
  - 9个自动捕获 + 9个inbox重复文件：均为已覆盖Python主题的重复抓取
  - 1个Hermes_Agent文件：已有16个Hermes source页面覆盖
  - 6个03_Resources文件：哈希标记不同但内容未实质变更
- **归档**: 10个文件移到 99-归档/2026-07-13/

### 建议
- 优先修复11个缺frontmatter的页面（6 entities + 5 sources）
- 考虑补充高引用概念页的骨架内容（pandas、Matplotlib、Agent等）
- awesome-evals未入索引 → 需更新index.md
