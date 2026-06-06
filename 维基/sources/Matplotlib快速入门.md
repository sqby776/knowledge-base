---
title: Matplotlib 快速入门指南
type: source
tags: [llmwiki, python, matplotlib, 数据可视化]
sources: ["01-收件箱/文章/2026-06-04_Quick_start_guide.md"]
created: 2026-06-05
updated: 2026-06-05
---

# Matplotlib 快速入门指南

## 摘要

Matplotlib 官方快速入门指南，介绍使用 matplotlib 进行可视化的基本流程和核心概念。

## 要点

- **pyplot 接口**：`import matplotlib.pyplot as plt`，类似 MATLAB 的命令式接口
- **Figure 和 Axes**：Figure 是画布容器，Axes 是绘图区域
- **创建图表**：`plt.figure()` → `ax = fig.add_subplot()` → `ax.plot()/ax.scatter()/ax.bar()`
- **样式**：`plt.style.use()` 可切换内置样式
- **标注**：`set_title()`、`set_xlabel()`、`set_ylabel()`、`legend()`
- **保存**：`plt.savefig()` 支持 PNG、PDF、SVG 等格式
- **交互模式**：`plt.ion()` 启用交互式绘图

## 提及的实体

- [[Matplotlib]]

## 相关概念

- [[数据可视化]]
- [[图表类型]]
- [[绘图接口]]

## 来源

- 原始 URL: https://matplotlib.org/stable/users/explain/quick_start.html
- 抓取日期: 2026-06-04
