---
title: openpyxl 快速开始
created: 2026-06-17
updated: 2026-06-17
tags: ["python", "excel", "openpyxl", "automation", "method"]
status: archived
sources: [https://openpyxl.readthedocs.io/en/latest/tutorial.html]
confidence: low
trust_score: 0.17
---
# openpyxl 快速开始

> 来源：openpyxl 官方教程

## 核心概念

- **Workbook**：整个 Excel 工作簿文件
- **Worksheet**：工作簿中的单个工作表
- **Cell**：表格中的单元格，通过行列定位

## 安装

```bash
pip install openpyxl
# 如需处理图片
pip install pillow
```

## 创建 Workbook

```python
from openpyxl import Workbook

wb = Workbook()
ws = wb.active  # 获取默认工作表，默认 Sheet

# 修改工作表名称
ws.title = "数据"

# 创建新工作表
ws1 = wb.create_sheet("新表")        # 追加到末尾
ws2 = wb.create_sheet("最前表", 0)   # 插入到最前
ws3 = wb.create_sheet("倒数第二", -1)  # 倒数第二位置

# 保存
wb.save('output.xlsx')
```

## 读写单元格

```python
# 直接通过坐标访问
ws['A1'] = 42
ws['B1'] = "Hello"

# 通过行列号访问（1-indexed）
d = ws.cell(row=4, column=2, value=10)

# 读取
print(ws['A1'].value)

# 获取多个单元格
cell_range = ws['A1':'C2']

# 获取整行/整列
col_c = ws['C']
row_10 = ws[10]
```

## 遍历数据

```python
# 遍历行
for row in ws.iter_rows(min_row=1, max_col=3, max_row=2):
    for cell in row:
        print(cell.value)

# 只取数值
for row in ws.values:
    for value in row:
        print(value)

# 遍历所有行
for row in ws.rows:
    for cell in row:
        print(cell)
```

## 读取已有文件

```python
from openpyxl import load_workbook

wb = load_workbook('data.xlsx')
ws = wb['Sheet1']
print(ws['D18'].value)

# 常用参数
wb = load_workbook('data.xlsx', 
    data_only=True,     # 读取公式计算结果而非公式本身
    read_only=True,     # 只读模式，省内存
    keep_vba=True)      # 保留 VBA 宏
```

## 常用操作

| 操作 | 方法 |
|------|------|
| 创建/打开工作簿 | `Workbook()` / `load_workbook()` |
| 选择工作表 | `wb['Sheet1']` / `wb.active` |
| 创建工作表 | `wb.create_sheet(name, pos)` |
| 读写单元格 | `ws['A1'] = value` / `ws.cell(row, col)` |
| 保存 | `wb.save('file.xlsx')` |
| 遍历行 | `ws.iter_rows()` / `ws.rows` |
| 仅获取值 | `ws.values` / `values_only=True` |

## 注意事项

- **不要全范围遍历**：`for x in range(1,101): for y in range(1,101): ws.cell(row=x, column=y)` 会在内存中创建 100×100 个空单元格
- **保存会覆盖**：`wb.save()` 会静默覆盖已存在的文件
- **扩展名需匹配**：.xlsx 模板保存为 .xlsm 会导致 Excel 无法打开
- **形状会丢失**：openpyxl 不支持读取图表/形状，重新保存会丢失

## 相关链接

- [[Pandas 快速入门]]
- [[Excel自动化]]
- [[Python办公库]]