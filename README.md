# Obsidian 知识库配置

**项目路径**: `~/workspace/knowledge/`
**创建时间**: 2026-05-24

## 目录结构

```
knowledge/
├── raw/          ← 原始文档（剪藏、爬取、导出）
├── knowledge/    ← 知识卡片（提炼后的概念、方法论）
├── skills/       ← 写作/工作 Skill（可复用的 AI 指令集）
├── drafts/       ← 草稿（AI 辅助创作的半成品）
├── archive/      ← 归档（旧版本文档）
└── README.md     ← 本文件
```

## Obsidian 设置建议

打开 Obsidian → 设置 → 文件与链接：
- **附件默认路径**：`raw/`（剪藏文章直接丢进 raw/）
- **新笔记默认存放路径**：`knowledge/`
- **子文件夹中的附件**：勾选「显示」
- **自动更新内部链接**：勾选

## 插件推荐

| 插件 | 用途 |
|------|------|
| Obsidian Web Clipper | 微信文章一键剪藏到 `raw/` |
| Excalidraw | 手绘流程图、选题框架 |
| Dataview | 自动列出所有 skill、知识卡片 |
| Templates | 写作模板、知识卡片模板 |

## 知识库使用原则

1. **raw 层只进不出**：原始材料统一扔 raw/，再加工到 knowledge/
2. **knowledge 是精华**：提炼、归纳、可复用，不要复制粘贴
3. **skills 是可执行的**：不仅是笔记，是可以调用的 AI Prompt
4. **定期清理 drafts → knowledge**：半成品最终沉淀
