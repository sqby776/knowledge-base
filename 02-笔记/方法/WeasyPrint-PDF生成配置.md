---
title: WeasyPrint PDF生成配置
created: 2026-07-14
updated: 2026-07-14
tags: [flask, workflow, tutorial]
status: needs-review
confidence: medium
trust_score: 0.41
---
# WeasyPrint PDF 生成配置

## 安装

```bash
pip install weasyprint
# Linux 依赖
sudo apt install libpango-1.0-0 libpangoft2-1.0-0 libharfbuzz0b libgdk-pixbuf2.0-0  # Ubuntu
```

## HTML → PDF 核心用法

```python
from weasyprint import HTML
html_str = render_template('template.html', **context)
doc = HTML(string=html_str).render()
doc.write_pdf(target=output_path)
```

## 🔴 页码方案（最大坑点）

### ❌ 方案1：CSS counter（不稳定）

```css
@page { @bottom-center { content: counter(page) " / " counter(pages); } }
@page cover { counter-reset: page 0; }
```

**问题**：WeasyPrint 版本不同导致 `@page cover` 对 `counter(pages)` 行为不一致。封面页有时会意外重置总页数，或计数器在名称页不生效。

### ✅ 方案2：Python 计算 + HTML 显式渲染（稳定）

**核心思路**：完全放弃 CSS 计数器，在 Python 中计算全局页码，通过 HTML 显式写入每个页面。

```python
# 1. 计算总页数：先渲染不带页码的 PDF，量长度
doc = HTML(string=html_str).render()
total_pages = len(doc.pages)

# 2. 渲染带页码的 HTML，用 Jinja2 传递总页数
html_with_pages = render_template('template.html', total_pages=total_pages, **context)

# 3. 用 CSS 控制每页显示的内容
@page cover {
    @bottom-left { content: none; }
    @bottom-center { content: none; }
}
@page {
    @bottom-center { content: none; }  # 清空 CSS 计数器
}

# 4. 在每个 tbody 或 div 后用 page-break-before/after 分页
# 5. 在每页的 footer 中用 Jinja2 渲染当前页码
```

**Jinja2 模板中的实现**（WeasyPrint 不支持 `counter(page)` 显式渲染，需要在 Python 端计算）：

```html
<div class="page-footer">
  <span>第 {{ page_num }} 页 / 共 {{ total_pages }} 页</span>
</div>
```

## 纸张设置

### HTML 方式（推荐，浏览器打印也能用）

```html
<style>
@page {
  size: A4 landscape;  /* A4 横向 */
  margin: 15mm;
}
@page cover {
  size: A4 portrait;   /* 封面纵向 */
}
</style>
```

### 注意：去掉 CSS `@page { size: ... }` 约束

用浏览器打印时，`@page size` 的 CSS 约束会锁定纸张设置，用户无法在打印对话框中选择纸张和方向。如果用户需要自由设置：

```html
<!-- ❌ 锁定 -->
<style>@page { size: A4 landscape; }</style>

<!-- ✅ 交给打印对话框 -->
<!-- 不设 @page size，只在打印对话框选 -->
```

## 表格分页

```css
/* 防止行内分页 */
tr { page-break-inside: avoid; }

/* 大段换页 */
.page-break { page-break-before: always; }
```

## 字体问题

WeasyPrint 使用系统字体。中文推荐：

```css
body { font-family: 微软雅黑, 'Microsoft YaHei', SimSun, sans-serif; }
```

## 性能

- 50 页左右：2-3 秒
- 避免用透明度、渐变等复杂 CSS（卡死）
- 图片用 base64 嵌入，不要外部 URL

## 参考

- [[Flask工资系统开发]] — 整套方法论
- [[openpyxl-企业导出优化]] — Excel 替代方案