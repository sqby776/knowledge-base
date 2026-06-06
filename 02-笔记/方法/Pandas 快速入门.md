---
title: Pandas 快速入门
created: 2026-06-02
updated: 2026-06-02
tags: ["python", "pandas", "data-analysis", "method"]
status: active
sources: [https://pandas.pydata.org/docs/user_guide/10min.html]
---

# Pandas 快速入门

> 来源：Pandas 官方文档 - 10分钟快速入门

## 核心概念

- **DataFrame（数据框）**：二维表格型数据结构，类似 Excel 表格。
- **Series（序列）**：一维标签数组，可以存储任何数据类型。

## 快速上手

```python
import pandas as pd

# 创建 DataFrame
df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [30, 25, 35],
    'city': ['Beijing', 'Shanghai', 'Guangzhou']
})

# 基本操作
print(df.head())         # 前5行
print(df.describe())     # 统计信息
print(df[['name', 'age']])  # 选列

# 数据筛选
filtered = df[df['age'] > 25]
```

## 数据导入导出

```python
# 读取文件
df = pd.read_csv('data.csv')
df = pd.read_excel('data.xlsx')

# 导出文件
df.to_csv('output.csv', index=False)
df.to_excel('output.xlsx', index=False)
```

## 常用操作

| 操作 | 方法 |
|------|------|
| 排序 | `df.sort_values('column')` |
| 分组 | `df.groupby('column').agg()` |
| 合并 | `pd.merge(df1, df2, on='key')` |
| 透视 | `df.pivot_table()` |
| 缺失值 | `df.dropna()` / `df.fillna()` |

## 与 csv/json 配合

```python
import csv, json
import pandas as pd

# CSV → DataFrame
df = pd.read_csv('data.csv')

# DataFrame → JSON
df.to_json('data.json', orient='records', force_ascii=False)
```

## 相关链接

- [[Python csv 库]]
- [[Python 数据可视化]]
- [[Python 办公库]]
