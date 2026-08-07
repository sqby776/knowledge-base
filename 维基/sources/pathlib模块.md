---
title: pathlib 模块 — 面向对象文件系统路径
type: source
tags: [llmwiki, python, pathlib, 文件操作]
sources: ["01-收件箱/文章/2026-06-04_pathlib_Object_oriented_filesystem_paths.md", 01-收件箱/自动捕获/2026-06-08_pathlib_Object_oriented_filesystem_paths.md]
created: 2026-06-05
updated: 2026-06-08
2026-06-05
status: archived
confidence: low
trust_score: 0.17
---
# `pathlib` 模块 — 面向对象文件系统路径

## 摘要

Python 标准库 `pathlib` 模块，提供面向对象的文件系统路径操作。取代传统的 `os.path` 字符串操作，提供更直观的路径操作接口。

## 要点

- **Path 类**：`Path` 是抽象基类，`PurePath` 是无操作的纯路径类
- **构造路径**：`Path('/') / 'home' / 'user'` 使用 `/` 运算符拼接
- **路径属性**：`name`（文件名）、`suffix`（扩展名）、`stem`（无扩展名）、`parent`（父目录）
- **路径操作**：`exists()`、`is_file()`、`is_dir()`、`is_symlink()`、`is_absolute()`
- **目录遍历**：`iterdir()`、`glob()`、`rglob()`
- **路径读取**：`read_text()`、`read_bytes()`、`write_text()`、`write_bytes()`
- **路径解析**：`resolve()` 解析符号链接和相对路径
- **跨平台**：`WindowsPath`、`PosixPath`、`PurePath` 自动适配

## 提及的实体

- [[Python]]

## 相关概念

- [[文件操作]]
- [[路径管理]]
- [[字符串路径 vs 对象路径]]

## 来源

- 原始 URL: https://docs.python.org/3/library/pathlib.html
- 抓取日期: 2026-06-04
