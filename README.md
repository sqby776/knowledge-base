# Obsidian + Web Clipper 配置指南

## 1. 启用 Obsidian CLI

打开 Obsidian → 设置 → 通用 → 高级 → 启用「命令行界面」

启用后验证：
```bash
obsidian --version
```

---

## 2. 配置知识库路径

知识库已创建在 `~/workspace/knowledge/`

Obsidian → 设置 → 文件与链接：
- **库路径**：已指向 `~/workspace/knowledge/`
- **附件默认路径**：`raw/`
- **新笔记默认存放路径**：`knowledge/`
- **子文件夹中的附件**：勾选「显示」
- **自动更新内部链接**：勾选

---

## 3. 安装 Web Clipper 插件

Obsidian → 设置 → 第三方插件 → 浏览 → 搜索 `Web Clipper` → 安装

安装后需启用，并在插件设置里：

| 设置项 | 值 |
|--------|-----|
| 保存路径 | `raw/` |
| 文件名格式 | `{{title}}` |
| 保存格式 | Markdown |
| 移除脚本标签 | 勾选 |
| 下载图片 | 勾选 |

---

## 4. 浏览器剪藏操作

打开微信公众号文章 → 点击浏览器工具栏 Web Clipper 图标 → 选择 `raw/` 保存 → 确认

**剪藏后自动流程**：
```
剪藏完成 → raw/ 出现 md 文件 → 标记 #todo-ingest → 定期 Ingest 到 knowledge/
```

---

## 5. Hermes 自动化集成（高级）

如果希望 Hermes 自动监控 `raw/` 目录并 Ingest：

编辑 `~/workspace/knowledge/scripts/auto-ingest.sh`（后续创建），通过 cronjob 每周日自动跑一遍 `raw/` 目录。
