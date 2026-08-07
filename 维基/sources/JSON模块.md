---
title: json 模块 — JSON 编码器和解码器
type: source
tags: [llmwiki, python, json, 数据序列化]
sources: ["01-收件箱/文章/2026-06-04_json_JSON_encoder_and_decoder.md", 01-收件箱/自动捕获/2026-06-08_json_JSON_encoder_and_decoder.md]
created: 2026-06-05
updated: 2026-06-08
2026-06-05
status: archived
confidence: low
trust_score: 0.17
---
# `json` 模块 — JSON 编码器和解码器

## 摘要

Python 标准库 `json` 模块，提供 JSON 编码（序列化）和解码（反序列化）功能。支持基本数据类型到 JSON 的转换、自定义编解码器、流式处理。

## 要点

- **`json.dumps()`**：将 Python 对象编码为 JSON 字符串
- **`json.loads()`**：将 JSON 字符串解码为 Python 对象
- **`json.dump()`**：写入文件
- **`json.load()`**：从文件读取
- **类型映射**：dict→object, list/tuple→array, str→string, int/float→number, True→true, False→false, None→null
- **自定义编码器**：继承 `json.JSONEncoder` 重写 `default()` 方法
- **安全解码**：`json.loads()` 仅解析 JSON，不会执行任意代码（对比 `eval()`）
- **参数**：`indent`（缩进）、`sort_keys`（排序键）、`ensure_ascii`（ASCII 转义）

## 提及的实体

- [[Python]]

## 相关概念

- [[JSON格式]]
- [[数据序列化]]
- [[数据交换]]

## 来源

- 原始 URL: https://docs.python.org/3/library/json.html
- 抓取日期: 2026-06-04
