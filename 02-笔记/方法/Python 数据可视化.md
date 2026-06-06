---
title: Python 数据可视化
created: 2026-06-02
updated: 2026-06-02
tags: ["python", "data-visualization", "matplotlib", "seaborn", "method"]
status: active
sources: [https://realpython.com/python-data-visualization/]
---

# Python 数据可视化

> 来源：RealPython - Python Data Visualization

## 核心工具栈

| 工具 | 特点 | 适用场景 |
|------|------|----------|
| Matplotlib | 基础、灵活 | 通用绘图 |
| Seaborn | 统计图表 | 数据分析可视化 |
| Plotly | 交互式 | Web 交互图表 |
| Bokeh | 大规模数据 | 实时数据流 |

## Matplotlib 基础

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y, label='sin(x)')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('正弦函数')
ax.legend()
plt.show()
```

## Seaborn 统计图表

```python
import seaborn as sns

sns.histplot(data, kde=True)
sns.boxplot(x='category', y='value', data=df)
sns.heatmap(correlation_matrix, annot=True)
```

## 与 pandas 集成

```python
import pandas as pd
df = pd.read_csv('data.csv')

# DataFrame 直接绘图
df.plot(x='date', y='value', kind='line')

# 分组统计图
df.groupby('category')['value'].mean().plot(kind='bar')
```

## 相关链接

- [[Matplotlib 快速入门]]
- [[Pandas 快速入门]]
- [[Python csv 库]]
