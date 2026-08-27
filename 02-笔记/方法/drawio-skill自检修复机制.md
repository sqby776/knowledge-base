---
title: drawio-skill — AI画图自动修复
created: 2026-07-14
updated: 2026-07-14
tags: [diagram, skill, workflow]
status: archived
confidence: low
trust_score: 0.19
source: 公众号 Jack-Liu
---
# drawio-skill — AI 画图自检+修复机制

> 1.8k Star · MIT · 支持 Claude Code/Cursor/Copilot/Codex/Hermes
> GitHub: https://github.com/Agents365-ai/drawio-skill

## 核心价值：自检+自动修复

不是生成一次就完事，而是：

```
生成 .drawio XML → 导出 PNG → 自检6类问题 → 发现问题 → 自动修复 → 再检查 → 最多2轮
```

**六类自检项：**
1. 重叠形状 — 两个元素挤在一起
2. 文字截断 — 文字被边框裁掉
3. 连线断开 — 连线没有正确连接
4. 离屏 — 元素跑到画布外面
5. 连线穿越形状 — 连线穿过其他元素
6. 堆叠连线 — 多条线重叠在一起

两轮自动修复能解决 90% 的常见问题。

## 七色语义配色

蓝=服务、绿=数据库、黄=队列、橙=网关、红=错误、灰=外部、紫=安全

## 六种图预设

ERD、UML类图、序列图、架构图、ML/DL图、流程图

## 样式学习

从现有的 .drawio 文件或图片中学习自定义风格。

## 对我们系统的改进

| 之前 | 之后 |
|:----|:----|
| svg-flowchart 生成一次就完事 | ✅ 增加 4.5 步自检+自动修复循环 |
| 发现重叠/截断只能手动提意见重新生成 | ✅ 自动检测并修复，最多2轮 |
| 无离屏检测 | ✅ viewBox自动扩展 |

**不装 drawio-skill 的原因：** 它是面向 Claude Code/CodeX 的，虽然支持 Hermes 但需要适配。我们的 svg-flowchart 已经覆盖了主要场景，把自检机制吸收进去更轻量、更可控。