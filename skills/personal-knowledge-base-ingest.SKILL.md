---
name: personal-knowledge-base-ingest
description: 个人知识库 Ingest 流程——把原始素材（剪藏、爬取、导出文档）按 raw→AI ingest→knowledge→skills 路径流转，构建可自进化的知识库。
tags: [知识库, ingest, Obsidian, 知识管理]
---

# 个人知识库 Ingest 流程

> 来源：《数字生命卡兹克文风复刻 skill 深度拆解》
> 参考架构：Karpathy LLM Wiki → Obsidian + Markdown

---

## 系统架构

```
原始素材 → raw/ → AI ingest → knowledge/  → 调用写作
     ↑                                    ↓
  剪藏/爬取                          skills/
                                  调用知识卡片
```

---

## 目录角色定义

| 目录 | 用途 | 写入规则 |
|------|------|---------|
| `raw/` | 原始文档（抓取、剪藏、导出） | 只进不出，不修改 |
| `knowledge/` | 知识卡片（提炼后的概念、方法论） | 从 raw/ Ingest 后产出 |
| `skills/` | 可执行 AI Prompt | 从 knowledge 中提取可执行规则 |
| `drafts/` | 草稿（AI 辅助创作的半成品） | 草稿完成后移到 archive/ |
| `archive/` | 归档（旧版本文档） | 定期整理，按主题分类 |

---

## Ingest 流程

### 入口：素材入库

素材来源：
- **微信公众号** → Obsidian Web Clipper 直接剪藏到 `raw/`
- **网页文章** → 爬虫抓取后保存到 `raw/`
- **PDF/电子书** → OCR 提取后保存到 `raw/`

### 步骤 1：AI Ingest

把 `raw/` 中未处理的新文档发给 AI，要求：

```
请按以下方式处理这个原始素材：
1. 提取核心观点（3-5 条）
2. 提取可复用的方法论/框架
3. 提取写作/表达技巧
4. 标注对我知识库的价值等级（⭐⭐⭐ 高价值 / ⭐⭐ 参考 / ⭐ 备查）
5. 建议存放到哪个知识卡片分类
```

### 步骤 2：写入 knowledge/

根据 Ingest 结果，提炼后写入 `knowledge/`：

```markdown
---
tags: [标签1, 标签2]
value: ⭐⭐⭐
source: raw/原文文件名.md
ingested: 2026-05-24
---

# 卡片标题

## 核心观点
...

## 方法论
...

## 可复用片段
...
```

### 步骤 3：提取可执行 Skill

如果某个知识卡片包含**可复用的操作流程**，进一步提取为 Skill：

```
knowledge/某方法论.md  →  skills/某技能.SKILL.md
```

### 步骤 4：写作时调用

写文章前，先检索 `knowledge/` 和 `skills/`：

```
"让我先查一下知识库中关于 XX 的素材和方法论"
→ 快速浏览相关 knowledge 卡片
→ 参考对应 skills 的写作规范
→ 开始写作
```

---

## Ingest 触发时机

- [ ] 剪藏新文章到 `raw/` 时标记 `#todo-ingest`
- [ ] 每周日检查 `raw/` 中待处理文档
- [ ] 写完文章后，将新素材 Ingest 进知识库
- [ ] 知识库满 50 张卡片时做一次全面整理
