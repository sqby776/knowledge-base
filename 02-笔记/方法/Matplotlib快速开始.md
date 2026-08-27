---
title: Matplotlib快速开始
created: 2026-08-25
updated: 2026-08-25
tags: [python, matplotlib, visualization, tutorial]
status: compiled
sources: [https://matplotlib.org/stable/users/explain/quick_start.html]
---

# Matplotlib快速开始

> 来源: Matplotlib官方文档 Quick Start Guide
> 抓取时间: 2026-08-25

## 核心要点

- **Figure/Axes 模型**: Figure 是容器，Axes 是实际的绘图区域
- **两种接口**: OO风格（显式创建Figure/Axes）和 pyplot 风格（隐式管理）
- **基本绘图**: `plt.subplots()` → `ax.plot()` → `plt.show()`
- **数据类型**: 期望 numpy.array 输入，pandas DataFrame 可通过 data 参数使用
- **样式设置**: 颜色、线型、标记大小、标签、标题、图例
- **坐标轴**: 支持线性/对数刻度、日期、字符串分类
- **颜色映射**: pcolormesh/contourf/imshow/scatter 支持 colormap + normalization
- **多子图**: `plt.subplots(n,m)` 或 `plt.subplot_mosaic()`

## 关键代码模式

```python
# 基本示例
fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])
plt.show()

# OO风格
fig, ax = plt.subplots(figsize=(5, 2.7))
ax.plot(x, x, label='linear')
ax.plot(x, x**2, label='quadratic')
ax.set_xlabel('x'); ax.set_ylabel('y')
ax.legend()
```

## 来源

- Matplotlib 3.11.1 官方文档
