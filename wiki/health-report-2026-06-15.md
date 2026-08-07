---
title: LLM Wiki 健康检查报告
type: report
date: 2026-06-15
---

# LLM Wiki 健康检查报告

**检查时间**: 2026-06-15
**Wiki 路径**: `~/workspace/knowledge/维基/`
**搜索后端**: qmd 未安装，跳过索引状态检查

---

## 一、宏观指标

| 指标 | 数值 |
|------|------|
| 总页面数 | **61** |
| ├── sources（来源摘要） | 24 |
| ├── entities（实体） | 18 |
| ├── concepts（概念） | 17 |
| ├── index | 1 |
| └── log | 1 |
| 总 wikilinks | 355 |
| 损坏链接数 | **~160+ occurrences**（涉及约 75 个唯一目标） |
| 孤立页面 (入链为零) | **0** |
| 过时页面 (>10 天无更新) | **18** (14 sources + 4 concepts) |
| 内容过短页面 (<300 字) | **22** |
| 来源漂移问题 | **26** (22 已删除 + 1 移动+哈希变更 + 1 内容变更 + 2 签到条) |
| 未跟踪来源 | 18 |
| 索引不同步 | 4 页未入索引 |
| 索引重复条目 | 6 个 wikilink 各出现 2 次 |

---

## 二、按优先级排序的问题

### 🔴 Critical

#### C1. 损坏双链 — 时间戳前缀不匹配（83 处引用，涉及 ~27 个唯一目标）

**根因**: 实体/概念页面的 wikilinks 指向了源文件在收件箱中的时间戳前缀名（如 `[[2026-05-27_HermesAgent工具详解]]`），但实际 wiki 中对应的 source 页面文件名不包含时间戳前缀。

**影响范围**: 几乎所有 entity 和 concept 页面受影响，尤其：
- `entities/Agent.md`（11 个损坏 link）
- `entities/Hermes.md`（9 个）
- `entities/浏览器自动化.md`（5 个）
- `concepts/Agent.md`（12 个）
- `concepts/自动化.md`（9 个）
- `concepts/配置.md`（6 个）

**修复方案**: 运行 `llmwiki-ingest` 重新摄取，让 ingest 重建正确的 wikilinks。也可批量搜索替换：将 `[[2026_05_27_xxx]]` 或 `[[2026-05-27_xxx]]` 格式替换为对应的 source 页面名。

**严重度**: **Critical** — 大量链接断裂，知识图谱连通性严重受损

#### C2. 缺少实体/概念页面（46 处引用，涉及 ~30 个唯一概念）

Source 页面中引用了大量外部工具/库作为 wikilinks，但对应页面不存在：

| 缺失页面 | 来源文件 | 建议类型 |
|----------|----------|----------|
| `[[Matplotlib]]` | `Matplotlib快速入门.md`, `Python数据可视化指南.md`, `图表类型.md`, `绘图接口.md` | entity |
| `[[openpyxl]]` | `openpyxl教程.md` | entity |
| `[[pandas]]` | `10分钟到Pandas入门教程.md`, `pandas-10分钟入门教程.md` | entity |
| `[[NumPy]]` | `10分钟到Pandas入门教程.md`, `pandas-10分钟入门教程.md` | entity |
| `[[DataFrame]]` | `10分钟到Pandas入门教程.md`, `pandas-10分钟入门教程.md` | concept |
| `[[Series]]` | 同上 | concept |
| `[[python-docx]]` / `[[python-pptx]]` | 对应 source | entity |
| `[[Seaborn]]`, `[[Plotly]]` | `Python数据可视化指南.md` | entity |
| `[[Excel自动化]]`, `[[Office自动化]]` | `openpyxl教程.md`, `python-docx快速入门.md` | concept |
| `[[电子表格]]`, `[[数据可视化]]` | 多个 source | concept |
| `[[文件操作]]`, `[[路径管理]]` | `pathlib模块.md` | concept |
| `[[时间序列]]`, `[[数据清洗]]`, `[[透视表]]` | `pandas-10分钟入门教程.md` | concept |

**修复方案**: 创建 stub 页面（entity/concept），含 frontmatter + 概览 + 反向链接。这些大多是 Python 生态常见工具，建议优先补 pandas/Matplotlib/openpyxl 三页。

**严重度**: **Critical** — source 页面的内部引用全部断裂

#### C3. 来源严重漂移 — 收件箱目录迁移（24 条 manifest 问题 + 18 条未跟踪来源）

**诊断结果**:
- `01-收件箱/文章/` 目录已被完全删除（所有 22 个源文件路径失效）
- 文件迁移至 `01-收件箱/自动捕获/`（2026-06-08 后）
- 另有 18 个新来源（2026-06-15 捕获）未在 manifest 中跟踪
- `articles/` 目录下的 1 个源的哈希已变更（内容已修改但未重摄取）
- `01_inbox/articles/` 中的文件与 `99-归档/` 中已有 hash 冲突

**修复方案**: 运行 `llmwiki-ingest` 重新扫描收件箱，自动发现新文件并关联已有 wiki 页面。

**严重度**: **Critical** — manifest 与实际文件系统严重不同步

---

### 🟠 Warning

#### W1. 内容过短 — 骨架页面（22 页）

以下页面内容和 frontmatter 齐全但正文过短（<300 字符），实质是未完成的骨架页：

**Entities** (11 页): Chrome, Claude, DevTools, Kanban, Nous-Research, OCR, OpenHands, RAG, Rust, CDP, 向量检索, 浏览器自动化

**Concepts** (10 页): CDP, DevTools-Protocol, OCR, RAG, 向量检索, 技能系统, 智能体框架, 浏览器自动化, 知识库, 部署

**影响**: 这些页面基本只有 1-2 句概览，无法提供有价值的参考信息

**修复方案**: 查阅对应的 source 页面，补充每个 entity 的核心描述、关键特性、使用场景

---

#### W2. 概念页面集体过时（14 页 13 天无更新）

以下 concepts 页面最后修改日期均为 2026-06-01，已连续 13 天未更新：

Agent, CDP, DevTools-Protocol, OCR, RAG, 向量检索, 技能系统, 智能体框架, 浏览器自动化, 知识库, 自动化, 部署, 配置

**同期收件箱中有 Hermes 相关新资料**（2026-06-08 的 Python 生态资料已摄取，但 Hermes 核心概念未更新）。

**修复方案**: 检查这些概念是否需要补充新信息；新摄入的 source 内容可能包含可提炼的新知识

---

#### W3. 缺失来源文件引用（24 条）

Source 页面 frontmatter 的 `sources` 字段指向的文件已不存在：

```
sources: ["01-收件箱/文章/2026-05-27_HermesAgent工具详解.md"]  # 路径已失效
```

这与 C3 同根因（目录迁移），manifest 未更新导致 source 页与实际源路径脱节。

**修复方案**: 运行 `llmwiki-ingest` 时重新关联 source 路径；如手动修复，将 `01-收件箱/文章/` → `01-收件箱/自动捕获/`

---

#### W4. frontmatter 缺少必须字段（2 页）

- `index.md`: 缺少 created, updated
- `log.md`: 缺少 type, created

---

#### W5. 索引不同步（4 页未入索引）

以下页面文件存在但未被 `index.md` 收录：
- `CSV格式` (`concepts/CSV格式.md`)
- `图表类型` (`concepts/图表类型.md`)
- `数据序列化` (`concepts/数据序列化.md`)
- `绘图接口` (`concepts/绘图接口.md`)

---

#### W6. 索引中 6 个页面重复出现

以下 wikilink 在 index.md 的 entities 和 concepts 两个分类下各出现一次：
`[[Agent]]`, `[[CDP]]`, `[[OCR]]`, `[[RAG]]`, `[[向量检索]]`, `[[浏览器自动化]]`

这是合理的（同一概念既有 entity 页又有 concept 页），但可能反映需要明确区分 entity 和 concept 的边界。

---

### 🟡 Info

#### I1. 缺失知识域覆盖

当前 wiki 集中在 Hermes Agent 和 Python 基础库，以下领域无独立页面：
- **Excel/VBA 办公自动化** — 仅有零散 source 引用
- **AI 视频/图片生成** (Agnes Video/Image) — 有多篇笔记但未抽象为 wiki 页面
- **Seafile/文件服务器运维** — 配置笔记存在但无 wiki 页
- **Office 文档处理生态** (openpyxl, python-docx, python-pptx) — 只有 source 页

#### I2. qmd 未安装

搜索后端不可用，无法进行向量检索。安装 `qmd` 后可启用语义搜索。

#### I3. 实体/概念命名风格待统一

部分 pages 使用英文名 (Agent, CDP, Chrome)，部分使用中文 (向量检索, 浏览器自动化, 知识库, 智能体框架)。无统一规范。

---

## 三、健康评分

**基数**: 100 分

| 扣分项 | 扣分 | 说明 |
|--------|------|------|
| 损坏链接 (大规模) | -15 | 83 处引用，影响整体图谱连通性 |
| 缺少页面 | -10 | 46 处指向不存在的概念/实体 |
| 来源漂移 | -10 | Manifest 与实际文件系统严重不同步 |
| 未跟踪来源 | -5 | 18 个新文件待摄取 |
| 骨架页面 | -8 | 22 页内容极少 |
| 概念过时 | -5 | 14 页 13 天无更新 |
| 索引不同步 | -3 | 4 页未入索引 |
| frontmatter 缺失 | -1 | 2 页缺少关键字段 |

**总分: 43 / 100** ⚠️ 需要重点关注

---

## 四、修复建议

### 优先执行

1. **运行 `llmwiki-ingest`**（最高优先级）
   - 重新扫描收件箱，修复 manifest 漂移
   - 追踪 18 个未跟踪的新来源
   - ingest 会重建 wikilinks，可能修复 C1 约 80% 的断裂链接
   - 建议指令: `hermes run llmwiki-ingest`

2. **补建缺失实体页**（3 个核心）
   - `[[pandas]]` (entity, 被 2 个 source 引用)
   - `[[Matplotlib]]` (entity, 被 4 个 source 引用)
   - `[[openpyxl]]` (entity, 被 1 个 source 引用)
   - 使用 stub 模板：带 frontmatter + 概览 + 反向链接

3. **修复索引同步**
   - 将 `CSV格式`, `图表类型`, `数据序列化`, `绘图接口` 加入 index.md

### 后续优化

4. **运行 `llmwiki-optimize`**
   - 补充 22 页骨架页面的内容
   - 处理 entity/concept 边界定义（6 页同时出现在两个分类）
   - 统一命名风格（英文 vs 中文）

5. **安装 `qmd`**
   - 启用语义搜索和向量检索能力

### 总结路线图

```
先跑 llmwiki-ingest  →  修复 C1(断裂链接) + C3(来源漂移)
       ↓
补核心实体页      →  修复 C2(缺失页面)
       ↓
跑 llmwiki-optimize →  修复 W1(骨架) + W2(过时) + W5(索引)
```

---

*报告由 llmwiki-health 自动生成*
