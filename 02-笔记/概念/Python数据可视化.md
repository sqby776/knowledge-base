---
title: Python数据可视化
created: 2026-08-25
updated: 2026-08-25
tags: [python, visualization, matplotlib, seaborn, bokeh, pandas]
status: compiled
sources: [https://realpython.com/python-data-visualization/]
---

# Python数据可视化

> 来源: Real Python Learning Path
> 抓取时间: 2026-08-25

## 核心要点

- **基础绘图**: pandas DataFrame 直接 plotting，histogram 用 NumPy/Matplotlib/Seaborn
- **Matplotlib**: 最基础的底层库，控制每个图形元素，支持所有图表类型
- **Seaborn**: 基于 Matplotlib 的高级统计绘图，语法更简洁
- **Bokeh**: 交互式可视化，适合 Web 应用
- **ggplot (plotnine)**: 基于 R 的 ggplot2 语法，适合熟悉 Grammar of Graphics 的用户
- **Dash**: 构建交互式数据可视化 Web 应用
- **Folium**: 生成 Web 地图，结合 Leaflet.js

## 技术栈关系

```
pandas.plot() → Matplotlib (底层)
                    ↓
Seaborn → 统计图表 (热图、配对图、分布图)
                    ↓
Bokeh/ggplot → 高级/交互式
                    ↓
Dash/Folium → Web应用/地图
```

## 来源

- Real Python: Data Visualization With Python Learning Path
- Matplotlib 官方文档
- Seaborn 文档
