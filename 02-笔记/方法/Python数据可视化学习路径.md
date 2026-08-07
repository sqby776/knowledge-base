---
title: Python 数据可视化学习路径
created: 2026-05-30
updated: 2026-05-30
tags: ["python", "visualization", "learning-path", "method"]
status: archived
sources: [https://realpython.com/python-data-visualization/]
trust_score: 0.17
confidence: low
---
# Python 数据可视化学习路径

> 来源：Real Python 数据可视化学习路径

## 学习路径概览

```
pandas 基础绘图 → Matplotlib/Seaborn → Bokeh 交互 → Dash 应用 → Folium 地图
```

## 核心技能栈

| 库 | 用途 | 难度 |
|:-----|:-----|:-----|
| **pandas** | 基础绘图、数据探索 | ⭐ |
| **Matplotlib** | 生产级静态图表 | ⭐⭐ |
| **Seaborn** | 统计图表、美观默认 | ⭐⭐ |
| **Bokeh** | 交互式可视化 | ⭐⭐⭐ |
| **ggplot/plotnine** | 语法一致性 | ⭐⭐ |
| **Dash** | Web 应用构建 | ⭐⭐⭐ |
| **Folium** | 地理信息地图 | ⭐⭐ |

## 学习顺序

### 第 1 阶段：基础入门

1. **pandas 绘图基础**
   - `df.plot()` 快速探索
   - 直方图、箱线图、散点图
   - 数据探索性分析

2. **Matplotlib 核心**
   - Figure/Axes/Artist 概念
   - 面向对象 vs pyplot 风格
   - 样式定制

### 第 2 阶段：进阶可视化

3. **Seaborn 统计图表**
   - 分布图、关系图
   - 分类数据可视化
   - 多变量分析

4. **Bokeh 交互图表**
   - 悬停提示
   - 缩放/平移
   - 联动图表

### 第 3 阶段：应用构建

5. **Dash 数据应用**
   - 交互式仪表板
   - 回调函数
   - 部署发布

6. **Folium 地理可视化**
   -  choropleth 地图
   - 标记点
   - 热力图

## 推荐资源

| 资源 | 类型 | 链接 |
|:-----|:-----|:-----|
| Plot With pandas | 课程 | Real Python |
| Histogram Plotting | 课程 | Real Python |
| Python Plotting With Matplotlib | 课程 | Real Python |
| Visualizing Data With Seaborn | 教程 | Real Python |
| Interactive Data Visualization With Bokeh | 课程 | Real Python |
| Data Visualization Interfaces With Dash | 课程 | Real Python |

## 最佳实践

1. **先探索再展示**：用 pandas 快速查看数据分布
2. **选择合适的图表**：根据数据类型和目的选择
3. **保持简洁**：避免过度装饰
4. **考虑受众**：技术 vs 非技术受众
5. **可复现性**：保存代码和配置

## 相关链接

- [[Matplotlib]]
- [[Python办公库]]
- [[Seaborn]]
- [[Bokeh]]

## 来源

- Real Python: https://realpython.com/python-data-visualization/
