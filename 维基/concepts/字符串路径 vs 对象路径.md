---
title: 字符串路径 vs 对象路径
type: concept
tags: [llmwiki, Python]
sources: [pathlib模块.md]
created: 2026-06-29
updated: 2026-06-29
---

# 字符串路径 vs 对象路径

## 概览

Python 中两种路径处理方式的对比：传统字符串路径（`os.path` 模块）与现代对象路径（`pathlib.Path` 类）。pathlib 提供面向对象的路径操作方法（`/` 拼接、`.exists()`、`.glob()`、`.read_text()`），比字符串拼接更安全、可读性更强，自 Python 3.4 起为标准库推荐路径处理方式。

## 要点

- `pathlib.Path` 优于 `os.path` 字符串操作
- 支持 `/` 运算符路径拼接（跨平台）
- `.glob()` 支持递归文件搜索
- `.read_text()/.write_text()` 直接读写文件

## 来源

[[pathlib模块]]