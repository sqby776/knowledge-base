# 个人本地知识库搭建方案

> 综合四篇微信文章最佳实践 + 本系统现有工具链优化

---

## 一、方案总览

```
┌─────────────────────────────────────────────────────────────────┐
│                    个人知识库工作流                              │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐ │
│  │  信息获取 │───→│  知识编译 │───→│  知识存储 │───→│  反馈汇报 │ │
│  └──────────┘    └──────────┘    └──────────┘    └──────────┘ │
│       │               │               │               │        │
│   Camoufox        Hermes Agent     Obsidian      微信/飞书     │
│   crawl4ai        LLM Wiki Skill   本地文件      日报推送      │
│   scrapling       自动分类         双链图谱                    │
│   AutoCLI         节点关联                                       │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 本系统已有能力 vs 方案需求

| 能力 | 本系统状态 | 方案利用 |
|:----|:----|:----|
| **Camoufox** | ✅ v0.4.11 + browser v135 | 重度 JS 页面抓取（微信公众号、社交媒体） |
| **crawl4ai** | ✅ v0.8.6 | 通用批量抓取 + 指令提取 |
| **scrapling** | ✅ v0.4.8 | 轻量静态页面快速抓取 |
| **Hermes Agent** | ✅ 已运行 | 知识编译核心、自动分类、节点关联 |
| **RTK** | ✅ 已集成 | 代理加速、反检测 |
| **Nginx + Docker** | ✅ 已配置 | 服务部署、反向代理 |
| **Feishu** | ✅ 已连接 | 可作为知识库协作平台 |

---

## 二、目录结构（Hermes-Wiki）

> 融合「超级猛」的节点分离 + 「徒手开榴莲」的实用目录

```
~/workspace/knowledge/                    # WIKI_PATH
├── SCHEMA.md                             # 规则文件（最重要！）
├── index.md                              # 总入口
├── log.md                                # 更新日志
├── 01_inbox/                             # 收集箱（对应 01_收集箱）
│   ├── articles/                         # 网页文章
│   ├── papers/                           # 论文
│   ├── transcripts/                      # 转录稿
│   └── assets/                           # 图片/截图
├── 02_notes/                             # 长期笔记（对应 02_笔记）
│   ├── concepts/                         # 概念页（RAG、MOC、知识飞轮...）
│   ├── entities/                         # 实体页（Obsidian、Hermes、工具...）
│   └── methods/                          # 方法论/模板
├── 03_resources/                         # 外部资料（对应 03_资料）
│   ├── pdfs/
│   └── links/
├── 04_projects/                          # 项目内容（对应 04_项目）
│   └── current/                          # 进行中项目
├── 05_comparisons/                       # 比较页（Hermes vs Claude Code...）
├── 06_queries/                           # 值得保留的问答
├── 07_moc/                               # 主题地图（Map of Content）
│   ├── 知识库地图.md
│   └── AI技术地图.md
├── 08_drafts/                            # 输出草稿
└── 99_archive/                           # 归档
```

---

## 三、核心规则文件

### 3.1 SCHEMA.md

```markdown
# SCHEMA.md — 知识库规则

## 目录规则
- `01_inbox/` — 原始资料，只追加不修改
- `02_notes/concepts/` — 概念页，跨资料沉淀的长期知识节点
- `02_notes/entities/` — 实体页，工具/人名/公司
- `02_notes/methods/` — 方法论和模板
- `03_resources/` — 外部参考资料
- `04_projects/` — 具体项目内容
- `05_comparisons/` — 对比分析页
- `06_queries/` — 重要问答沉淀
- `07_moc/` — 主题地图（理解路线图）
- `08_drafts/` — 输出草稿
- `99_archive/` — 暂存/归档

## 双链规则
- 重要概念必须使用 [[wikilink]]
- 概念页之间互相链接
- 概念页连实体页
- 实体页连 MOC
- 关键结论必须标注来源：[[01_inbox/articles/xxx]]

## 质量规则
- 不确定内容必须标记为 `> [!WARNING] 待验证`
- 每次重要修改后更新 `log.md`
- 新增重要页面后更新 `index.md`
- raw 原始资料只追加只读，不让 AI 改写

## 工作流
1. 信息抓取 → 放入 `01_inbox/`
2. 让 Agent 编译 → 生成概念/实体/MOC 页
3. Agent 用 wikilink 建立关联
4. 更新 `log.md` 和 `index.md`
5. 定期生成日报推送
```

### 3.2 index.md

```markdown
# 个人知识库 Index

## 核心概念
- [[RAG]]
- [[Agentic RAG]]
- [[LLM Wiki]]
- [[MOC]]
- [[知识飞轮]]
- [[双链交叉引用]]
- [[Source-first]]

## 工具与实体
- [[Hermes Agent]]
- [[Obsidian]]
- [[Camoufox]]
- [[crawl4ai]]
- [[scrapling]]

## 主题地图
- [[知识库地图]]
- [[AI技术地图]]

## 最近更新
待更新
```

---

## 四、自动化工作流

### 4.1 定时抓取（Cron Job）

```bash
# 每天下午 5 点抓取 AI 相关新闻
# 使用 hermes cronjob 创建

# 步骤1：创建抓取脚本
cat > ~/.hermes/scripts/daily-crawl.sh << 'EOF'
#!/usr/bin/env bash
# 每日 AI 资讯抓取

URLS=(
  "https://www.theverge.com/ai-artificial-intelligence"
  "https://techcrunch.com/category/artificial-intelligence/"
)

for url in "${URLS[@]}"; do
  /usr/bin/python3 /home/sqby776/.hermes/scripts/hermes_scraper.py \
    "$url" --backend crawl4ai \
    --prompt "提取文章标题、核心观点、关键数据，输出为Markdown" \
    --format json
done
EOF
chmod +x ~/.hermes/scripts/daily-crawl.sh
```

### 4.2 知识编译流程

```
文章放入 01_inbox/articles/
    ↓
Hermes 读取文章
    ↓
提取核心主题 → 创建/更新概念页（02_notes/concepts/）
提取实体 → 创建/更新实体页（02_notes/entities/）
生成 MOC 更新（07_moc/）
    ↓
强制使用 [[wikilink]] 建立关联
    ↓
更新 log.md + index.md
    ↓
（可选）生成日报推送微信/飞书
```

### 4.3 一键编译命令

在 Hermes 中输入：

```
请编译这篇文章：01_inbox/articles/文章标题.md

要求：
1. 读取文章内容，提取核心主题
2. 根据内容创建或更新对应的 Wiki 页面
3. 重要概念使用 [[wikilink]]
4. 关键结论必须标注来源
5. 如果某些内容是总结归纳，明确标记
6. 更新 index.md 和 log.md
7. 列出本次新增和更新了哪些文件
```

---

## 五、Obsidian 配置

### 5.1 打开方式

```
Obsidian → Open folder as vault → ~/workspace/knowledge/
```

> ⚠️ 注意：选择整个 `knowledge/` 文件夹，不要选子目录

### 5.2 推荐插件

| 插件 | 作用 | 安装方式 |
|:----|:----|:----|
| **Obsidian Git** | 自动同步到 GitHub | 社区插件市场搜索 "Git" |
| **Dataview** | 查询和可视化知识库 | 社区插件市场搜索 "Dataview" |
| **Advanced Tables** | 表格编辑增强 | 社区插件市场搜索 "Tables" |
| **Omnisearch** | 本地 OCR + 智能搜索 | 社区插件市场搜索 "Omnisearch" |
| **Calendar** | 每日笔记 | 社区插件市场搜索 "Calendar" |

### 5.3 Git 同步配置

```bash
# 在 knowledge 目录初始化 Git
cd ~/workspace/knowledge
git init
git add .
git commit -m "init knowledge base"
git branch -M main
git remote add origin https://github.com/你的用户名/knowledge.git
git push -u origin main
```

然后在 Obsidian 中安装 **Obsidian Git** 插件，设置自动同步间隔（建议 15 分钟）。

---

## 六、多端同步

### 6.1 方案对比

| 方案 | 优点 | 缺点 | 推荐 |
|:----|:----|:----|:----|
| **GitHub + Obsidian Git** | 免费、版本控制 | 手机端需手动 | ⭐⭐⭐⭐⭐ |
| **Syncthing** | 完全本地、实时 | 需额外软件 | ⭐⭐⭐⭐ |
| **iCloud Drive** | 苹果生态无缝 | 仅限 Apple | ⭐⭐⭐ |
| **Remotely Save** | 支持 S3/WebDAV | 配置复杂 | ⭐⭐⭐ |

### 6.2 推荐方案：GitHub + Working Copy（手机）

```
电脑端：Obsidian + Obsidian Git 插件 → 自动 push 到 GitHub
手机端：Working Copy → clone GitHub 仓库 → Obsidian 打开文件夹
```

---

## 七、自动化增强（进阶）

### 7.1 自动入库 + 微信汇报

参考「芋头小宝」的方案，用 Hermes Cron + 微信推送：

```yaml
# ~/.hermes/config.yaml 中添加 cron 任务
# 每天下午 6 点：抓取 + 编译 + 汇报
```

### 7.2 微信接入

Hermes 已连接 Feishu，可以直接用 Feishu 接收日报：

```
在 Hermes 中输入：
"请配置每天下午 6 点向我发送知识库日报，内容包括：
1. 今日总览（新增/更新页面数）
2. 今日重点（3 条关键信息摘要）
3. 报告位置（knowledge/log.md 的最新条目）"
```

---

## 八、快速启动清单

- [ ] 创建 `~/workspace/knowledge/` 目录结构
- [ ] 写入 `SCHEMA.md`、`index.md`、`log.md`
- [ ] 在 Obsidian 中打开该文件夹作为 Vault
- [ ] 安装 Obsidian Git 插件并配置自动同步
- [ ] 在 Hermes 中设置 `WIKI_PATH` 环境变量
- [ ] 测试：放入一篇文章到 `01_inbox/articles/`
- [ ] 让 Hermes 编译，检查生成的页面和双链
- [ ] 在 Obsidian 图谱中验证知识网络形成
- [ ] （可选）配置定时抓取 + 日报推送

---

## 九、避坑指南

1. **不要一上来全自动**：先用 3-5 篇文章测试，确认命名、双链、MOC 规则稳定后再扩大
2. **raw 原始资料只读**：不让 AI 改写原文，保证可追溯
3. **每次生成后看 log.md**：确认改了什么，哪些是原文结论，哪些是 AI 归纳
4. **不确定内容标"待验证"**：`> [!WARNING] 待验证`
5. **不要在电脑和手机同时修改同一个文件**：先同步再编辑，减少冲突
6. **Obsidian 和 Hermes 必须指向同一个文件夹**：路径不对后面会困惑
7. **WIKI_PATH 在 WSL/Ubuntu 中设置**：Windows + WSL 用户用 `/mnt/c/Users/...`

---

*方案制定时间：2026-05-23*
*参考来源：超级猛、桃哥、徒手开榴莲、芋头小宝（微信公众号）*
