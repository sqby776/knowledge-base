---
title: Matplotlib 快速开始
created: 2026-06-17
updated: 2026-06-17
tags: ["python", "matplotlib", "data-visualization", "chart", "method"]
status: archived
sources: [https://matplotlib.org/stable/users/explain/quick_start.html]
confidence: low
trust_score: 0.17
---
# Matplotlib 快速开始

> 来源：Matplotlib 官方快速入门指南

## 核心概念

- **Figure（画布）**：整个绘图窗口，可包含多个子图
- **Axes（坐标系）**：实际绘图区域，包含数据、刻度、标签
- **Artist（元素）**：所有可见元素（线、标签、图例等）

## 基本用法

```python
import matplotlib.pyplot as plt
import numpy as np

# 方式1：pyplot 直接绘图（快速）
x = np.linspace(0, 2, 100)
plt.plot(x, x, label='linear')
plt.plot(x, x**2, label='quadratic')
plt.xlabel('x label')
plt.ylabel('y label')
plt.title("Simple Plot")
plt.legend()
plt.show()

# 方式2：面向对象 API（更规范）
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(x, x, label='linear')
ax.plot(x, x**2, label='quadratic')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title("Simple Plot")
ax.legend()
plt.show()
```

## 图形类型

```python
# 折线图
plt.plot(x, y)

# 散点图
plt.scatter(x, y, c='red', s=10)

# 柱状图
plt.bar(categories, values)

# 直方图
plt.hist(data, bins=30)

# 饼图
plt.pie(sizes, labels=labels, autopct='%1.1f%%')

# 箱线图
plt.boxplot(data)

# 热力图
plt.imshow(matrix, cmap='viridis')
plt.colorbar()
```

## 子图布局

```python
# 规则网格
fig, axes = plt.subplots(2, 3, figsize=(12, 6))
axes[0, 0].plot(x, y)

# 不规则布局（subplot_mosaic）
fig, ax_dict = plt.subplot_mosaic([
    ['left', 'right_top'],
    ['left', 'right_bottom']
])
ax_dict['left'].plot(x, y)
```

## 样式与美化

```python
# 设置样式
plt.style.use('seaborn-v0_8')
# 或查看可用样式
print(plt.style.available)

# 线条样式
ax.plot(x, y, linestyle='--', linewidth=2, color='#FF5733')

# 自定义图例
ax.legend(['label1', 'label2'], loc='upper right', frameon=True)

# 刻度控制
ax.set_xticks([0, 1, 2])
ax.set_xticklabels(['零', '一', '二'])
ax.tick_params(axis='x', rotation=45)

# 添加文字标注
ax.annotate('峰值', xy=(3, 7), xytext=(4, 8),
            arrowprops=dict(arrowstyle='->'))
```

## 与 pandas 集成

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

# DataFrame 直接绘图
df.plot(x='date', y='value', kind='line', ax=ax)
df['value'].plot(kind='hist', bins=20)
df.groupby('category')['value'].mean().plot(kind='bar')
```

## 保存图片

```python
plt.savefig('output.png', dpi=300, bbox_inches='tight')
plt.savefig('output.pdf', format='pdf')  # 矢量图
plt.savefig('output.svg', format='svg')  # 网页用
```

## 相关链接

- [[Python 数据可视化]]
- [[Pandas 快速入门]]
- [[Python办公库]]
- [[Python数据可视化学习路径]]