---
title: 路径处理 pathlib
type: concept
tags: [python, pathlib, 文件操作]
sources: [https://docs.python.org/3/library/pathlib.html]
created: 2026-08-27
updated: 2026-08-27
status: compiled
confidence: high
trust_score: 0.8
---
# 路径处理 pathlib

## 概览

`pathlib` 是 Python 标准库中的面向对象路径处理模块（Python 3.4+），替代传统的 `os.path`。

## 核心类

- **Path**：通用路径类，自动适配操作系统（Windows/macOS/Linux）
- **PurePath**：纯路径（不做 I/O 操作），用于字符串处理
- **PosixPath / WindowsPath**：子类，根据运行平台自动选择

## 常用操作

```python
from pathlib import Path

p = Path('/home/user/docs/file.txt')

# 属性
p.name          # 'file.txt'
p.stem          # 'file'
p.suffix        # '.txt'
p.parent        # Path('/home/user/docs')
p.parts         # ('/', 'home', 'user', 'docs', 'file.txt')
p.anchor        # '/'

# 路径组合
p / 'subdir' / 'other.txt'  # 使用 / 运算符

# 文件操作
p.exists()
p.is_file()
p.is_dir()
p.read_text()
p.write_text('content')
p.read_bytes()
p.write_bytes(b'data')

# 遍历目录
Path('.').iterdir()      # 列出子项
Path('.').rglob('*.py')  # 递归查找
```

## 与 os.path 对比

| os.path | pathlib |
|:--------|:--------|
| `os.path.join()` | `Path / Path` |
| `os.path.exists()` | `Path.exists()` |
| `os.path.abspath()` | `Path.resolve()` |
| `os.path.dirname()` | `Path.parent` |
| `os.path.basename()` | `Path.name` |

## 适用场景

- 跨平台路径处理
- 文件读写操作封装
- 路径比较和拼接
- 递归目录遍历

## 相关概念

- [[文件操作]]
- [[数据序列化]]

## 来源

- Python 官方 pathlib 文档
