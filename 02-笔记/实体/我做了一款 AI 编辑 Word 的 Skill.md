---

sources: [01-收件箱/文章/2026-05-29_AI编辑Word的Skill.md]
title: 我做了一款 AI 编辑 Word 的 Skill
source: 微信公众号-AI干货家老明
url: https://mp.weixin.qq.com/s/Fnp8Ly9qv9QCweqpmWqyaw
date: 2026-05-29
status: active
type: article
tags: [Word, Skill, 排版, 办公自动化, GitHub]
confidence: medium
---

# 我做了一款 AI 编辑 word 的 skill，推荐给你试试，效果惊艳

作者：干货老明

## 核心信息

- GitHub开源：https://github.com/sgsss998/AI-Word-Skill
- 功能：AI 自动编辑/排版 Word 文档
- 核心价值：节省大量手工排版时间
- 技术立场：母版副本 + 尽量只动 `run.text` + 表格别漏

## 价值维度

| 维度 | 价值 |
|------|------|
| 时间 | 少做一整轮"全篇重排"或"手工对齐到哭" |
| 质量 | 合同、纪要、公文、标书等场景下，版式稳定≈专业度 |
| 可解释 | 出问题能对上 OOXML / run / 样式的原因 |
| 核心抓手 | 母版副本 + 尽量只动 run.text + 表格别漏 |

## 对我们可用的功能点

### 1. 安装 AI-Word-Skill（P0）
直接关联我们的公文排版需求，可以试装
```bash
hermes skills install https://github.com/sgsss998/AI-Word-Skill
```

### 2. 阅读源代码（P1）
了解其 SOP 和 python-docx 操作模式，看是否能与我们的公文模板结合

### 3. 技术理念借鉴
"母版副本"概念 — 和我们已有的公文模板思路一致，可互相补充