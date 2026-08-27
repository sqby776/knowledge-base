---
title: JSON 数据交换
type: concept
tags: [python, json, 数据序列化]
sources: [https://docs.python.org/3/library/json.html]
created: 2026-06-05
updated: 2026-08-27
status: compiled
confidence: high
trust_score: 0.8
---
# JSON 数据交换

## 概览

JSON（JavaScript Object Notation）是最广泛的数据交换格式，由 RFC 7159 和 ECMA-404 标准化。

## Python json 模块核心 API

- **序列化**：`json.dumps(obj)` → 字符串，`json.dump(obj, f)` → 文件
- **反序列化**：`json.loads(s)` ← 字符串，`json.load(f)` ← 文件
- **类型映射**：
  - Python dict ↔ JSON object `{}`
  - Python list/tuple ↔ JSON array `[]`
  - Python str ↔ JSON string
  - Python int/float ↔ JSON number
  - Python True/False ↔ JSON true/false
  - Python None ↔ JSON null

## 关键参数

- `indent`：格式化缩进（调试用）
- `sort_keys`：按 key 排序输出
- `ensure_ascii`：默认 True（转义非 ASCII），设为 False 保留中文
- `separators`：自定义分隔符，如 `(',', ':')` 压缩输出
- `default`：自定义序列化函数（处理 datetime 等）

## 安全警告

- `json.loads()` 仅解析 JSON，不执行任意代码（与 `eval()` 不同）
- 从不可信来源解析时需限制数据大小，防止 DoS

## 相关概念

- [[CSV数据处理]]
- [[数据序列化]]
- [[数据交换]]

## 来源

- Python 官方 json 文档
