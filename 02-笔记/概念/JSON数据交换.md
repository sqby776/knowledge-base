---
title: JSON 数据交换
type: concept
tags: [llmwiki, python, json, 数据序列化]
sources: ["维基/sources/JSON模块.md"]
created: 2026-06-05
updated: 2026-06-05
status: archived
confidence: low
trust_score: 0.17
---
# JSON 数据交换

## 概览

JSON（JavaScript Object Notation）是最广泛的数据交换格式。Python 标准库 `json` 提供编解码支持。

## 关键信息

- **类型映射**：dict↔object, list↔array, str↔string, int/float↔number, True/False↔true/false, None↔null
- **核心函数**：`dumps()`（序列化）、`loads()`（反序列化）、`dump()`/`load()`（文件）
- **安全**：`json.loads()` 仅解析 JSON，不执行任意代码
- **参数**：`indent` 格式化输出、`sort_keys` 排序、`ensure_ascii` 控制中文显示

## 相关概念

- [[数据序列化]]
- [[数据交换]]
- [[CSV数据处理]]

## 来源

- [[JSON模块]]
