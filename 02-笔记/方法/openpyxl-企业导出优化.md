---
title: openpyxl 企业导出优化
created: 2026-07-14
updated: 2026-07-14
tags: [tool, workflow, tutorial]
status: active
confidence: high
---

# openpyxl 企业导出优化

## 列宽计算

### 核心公式

```python
from openpyxl.utils import get_column_letter

# 列宽 = 最大字符数 × 系数 + 基值
COL_WIDTH_COEFF = 0.8      # 系数（px/字符）
COL_WIDTH_BASE = 3.0       # 基值（字符数）
COL_WIDTH_MIN = 8          # 下限
COL_WIDTH_MAX = 35         # 上限

for i, col_name in enumerate(columns, 1):
    max_chars = max(len(str(col_name)), max(len(str(row[i-1])) for row in data))
    width = max(COL_WIDTH_MIN, min(max_chars * COL_WIDTH_COEFF + COL_WIDTH_BASE, COL_WIDTH_MAX))
    ws.column_dimensions[get_column_letter(i)].width = width
```

**注意**：
- openpyxl 的 width 单位是"字符数"（非像素）
- 中文每个字符约 2.1 个宽度单位
- 8pt 字体下，系数 0.8 + 基值 3.0 经验证效果良好

### 🔴 不要用 chr(64 + i)（仅支持 26 列）

```python
# ❌ 只支持 A-Z（26列），超过 Z 返回 'A'
for i in range(1, 31):
    ws.column_dimensions[chr(64 + i) if i <= 26 else 'A'].width = 12

# ✅ get_column_letter() 支持任意列（A→Z→AA→AB→...）
from openpyxl.utils import get_column_letter
for i in range(1, 31):
    ws.column_dimensions[get_column_letter(i)].width = 12
```

## 行高

```python
# 数据行统一高度
ws.row_dimensions[1].height = 18    # 表头
for row in range(2, len(data) + 2):
    ws.row_dimensions[row].height = 18  # 数据行
```

## 字号

| 用途 | pt | px 近似 | 说明 |
|------|:--:|:-------:|------|
| 标题 | 11pt | 15px | 居中加粗 |
| 表头 | 8pt | 10px | 加粗浅灰底色 |
| 数据 | 8pt | 10px | 居中对齐 |
| 合计 | 8pt | 10px | 加粗 |

```python
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side

title_font = Font(name='微软雅黑', size=11, bold=True)
header_font = Font(name='微软雅黑', size=8, bold=True)
data_font = Font(name='微软雅黑', size=8)
total_font = Font(name='微软雅黑', size=8, bold=True)
```

## 样式常量化

### 🔴 不重复定义样式

多个导出函数各自定义 `Font()`、`Border()`、`PatternFill()` → 修改表头颜色要改 N 个文件。

**推荐**：抽取公共样式模块 `excel_styles.py`

```python
# excel_styles.py — 所有导出函数共享
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side

FONT_DEFAULT = '微软雅黑'
SIZE_HEADER = 8
SIZE_DATA = 8
SIZE_TITLE = 11

header_font = Font(name=FONT_DEFAULT, size=SIZE_HEADER, bold=True)
data_font = Font(name=FONT_DEFAULT, size=SIZE_DATA)
total_font = Font(name=FONT_DEFAULT, size=SIZE_DATA, bold=True)

thin_border = Border(
    left=Side(style='thin'),
    right=Side(style='thin'),
    top=Side(style='thin'),
    bottom=Side(style='thin'),
)

header_fill = PatternFill(start_color='F2F2F2', end_color='F2F2F2', fill_type='solid')
center_align = Alignment(horizontal='center', vertical='center', wrap_text=True)
```

## 高级功能

### 冻结表头

```python
ws.freeze_panes = 'A2'  # 冻结第一行
```

### 自动筛选

```python
ws.auto_filter.ref = f'A1:{get_column_letter(max_col)}{max_row}'
```

### 金额千分位格式

```python
# openpyxl 的数字格式
ws.cell(row=r, column=c).number_format = '#,##0.00'
```

## 完整导出模板

```python
def export_to_excel(columns, data_rows, title, output_path):
    wb = Workbook()
    ws = wb.active
    ws.title = title

    # 表头
    for ci, col in enumerate(columns, 1):
        cell = ws.cell(row=1, column=ci, value=col)
        cell.font = header_font
        cell.fill = header_fill
        cell.alignment = center_align
        cell.border = thin_border

    # 数据
    for ri, row in enumerate(data_rows, 2):
        for ci, val in enumerate(row, 1):
            cell = ws.cell(row=ri, column=ci, value=val)
            cell.font = data_font
            cell.alignment = center_align
            cell.border = thin_border

    # 冻结 + 筛选
    ws.freeze_panes = 'A2'
    ws.auto_filter.ref = f'A1:{get_column_letter(len(columns))}{len(data_rows) + 1}'

    # 列宽
    for ci in range(1, len(columns) + 1):
        col_letter = get_column_letter(ci)
        max_chars = max(len(str(columns[ci-1])), max(len(str(r[ci-1])) for r in data_rows))
        ws.column_dimensions[col_letter].width = max(8, min(max_chars * 0.8 + 3.0, 35))

    wb.save(output_path)
```

## 参考

- [[Flask工资系统开发]] — 导出模块架构
- [[WeasyPrint-PDF生成配置]] — PDF 替代方案