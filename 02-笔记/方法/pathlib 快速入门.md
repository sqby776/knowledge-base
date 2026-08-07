---
title: pathlib 快速入门
created: 2026-06-17
updated: 2026-06-17
tags: ["python", "pathlib", "filesystem", "path", "method"]
status: archived
sources: [https://docs.python.org/3/library/pathlib.html]
confidence: low
trust_score: 0.17
---
# pathlib 快速入门

> 来源：Python 官方文档 - pathlib 面向对象文件系统路径

## 核心概念

- **PurePath**：纯路径操作（不涉及文件 I/O），跨平台
- **Path**：具体路径（继承 PurePath），支持文件读写等操作
- 日常使用只需 `Path` 类，它会自适应当前操作系统

## 基本路径操作

```python
from pathlib import Path

# 创建路径对象
p = Path('/home/user/docs/file.txt')
p = Path('relative/path')
p = Path()  # 当前目录

# 路径属性
p.name       # 'file.txt'
p.stem       # 'file'（无扩展名）
p.suffix     # '.txt'
p.parent     # '/home/user/docs'
p.parents    # [Path('/home/user/docs'), Path('/home/user'), ...]
p.root       # '/'
p.anchor     # '/'

# 路径拼接
new_path = Path('/base') / 'sub' / 'file.txt'
```

## 读写文件

```python
p = Path('data.txt')

# 读写文本（自动处理编码）
p.write_text('Hello World')
content = p.read_text()

# 读写二进制
p.write_bytes(b'binary data')
data = p.read_bytes()
```

## 目录操作

```python
p = Path('/home/user')

# 创建目录
p.mkdir(exist_ok=True)           # 创建单层
p.mkdir(parents=True, exist_ok=True)  # 创建多层

# 列出目录内容
for child in p.iterdir():
    print(child.name)

# 使用 glob 匹配文件
for py in p.glob('*.py'):        # 当前目录
    print(py)
for py in p.rglob('*.py'):      # 递归搜索子目录
    print(py)
```

## 查询文件状态

```python
p = Path('data.txt')

p.exists()        # 是否存在
p.is_file()       # 是否是文件
p.is_dir()        # 是否是目录
p.stat().st_size  # 文件大小（字节）
p.stat().st_mtime # 最后修改时间

# 获取绝对路径
p.resolve()       # 解析为绝对路径
p.absolute()      # 获取绝对路径（不解析符号链接）
```

## 文件操作

```python
from pathlib import Path

src = Path('source.txt')
dst = Path('dest.txt')

# 复制（pathlib 无内置 copy，使用 shutil）
import shutil
shutil.copy(src, dst)

# 移动/重命名
src.rename('new_name.txt')
src.replace('target.txt')  # 替换目标

# 删除
p.unlink()       # 删除文件
p.rmdir()        # 删除空目录
import shutil
shutil.rmtree('/path/to/dir')  # 删除非空目录

# 创建软链接
p.symlink_to(target)
```

## 对比旧式 os.path

| 操作 | pathlib | os.path |
|------|---------|---------|
| 拼接路径 | `Path('a') / 'b'` | `os.path.join('a', 'b')` |
| 获取文件名 | `p.name` | `os.path.basename(p)` |
| 获取扩展名 | `p.suffix` | `os.path.splitext(p)[1]` |
| 判断文件 | `p.is_file()` | `os.path.isfile(p)` |
| 列出目录 | `p.iterdir()` | `os.listdir(p)` |
| Glob 匹配 | `p.glob('*.py')` | `glob.glob('*.py')` |
| 读写文本 | `p.read_text()` | 需要 `open()` |
| 创建目录 | `p.mkdir()` | `os.makedirs()` |

## 相关链接

- [[Python办公库]]
- [[CSV数据处理]]
- [[JSON数据交换]]