---
title: Flask工资系统开发方法论
created: 2026-07-14
updated: 2026-07-14
tags: [flask, workflow, architecture]
status: active
confidence: high
sources: [01-收件箱/archive/工资管理系统开发记录]
---

# Flask 工资系统开发方法论

## 项目结构

标准 Flask 多蓝图结构：

```
SalarySystem_Flask/
├── app.py                  # 应用工厂 + before_request
├── models/__init__.py      # 所有 SQLAlchemy 模型
├── blueprints/             # 蓝图路由
│   ├── helpers.py          # 公共工具函数
│   ├── auth.py             # 登录认证
│   ├── departments.py      # 科室管理
│   ├── employees.py        # 员工管理
│   ├── module_calc.py      # 工资计算引擎
│   ├── modules_view.py     # 工资表视图
│   ├── modules_export.py   # Excel/PDF 导出
│   ├── reports.py          # 报表中心
│   └── ...
├── templates/              # Jinja2 模板
├── static/                 # CSS/JS/图片
└── data/                   # 数据文件
```

## 核心模式

### 1. 大文件拆分（1800+ → <600 行）

**触发条件**：一个蓝图文件超过 800 行，必须拆分。

**步骤**：

1. 分析结构：`grep -n '^def \|^@app.route\|^class ' big_file.py`
2. 识别独立功能组（如 `cover_templates` 6 个路由、`_export_module_excel` 600 行）
3. 共享常量（如 `STANDARD_FIELD_MAP`）→ 移到 `helpers.py`
4. 创建新文件，保留 `from app import app` 和 `from models import ...`
5. **必须在 app.py 添加 import 新文件**（Flask 路由通过 `@app.route` 装饰器注册，不 import 不会注册）
6. 验证：`python3 -c "from app import app; print('OK')"` + 检查路由是否注册

**检验标准**：拆分后旧文件 ≤ 600 行，新文件 100~575 行，职责单一。

### 2. 增量修复（而不是批量大改）

**铁律**：每改 2-3 个文件就验证一次。**严禁一次性改 18 个文件再测试。**

```bash
# ❌ 错误
patch file1.py file2.py ... file18.py  # 全改完才测
pytest  # 崩溃，不知道谁引起的

# ✅ 正确
# 批1: helpers.py + 安全函数 → python3 -c "from app import app; print('OK')"
# 批2: module_calc.py N+1优化 → pytest -v --tb=short
# 批3: modules_view.py None保护 → 浏览器实测
```

### 3. 装饰器顺序

```python
@app.route('/path')                         # 1. 路由（最上）
@login_required                              # 2. 登录（离路由最近）
@permission_required('module:action')        # 3. 权限（最下，最靠近函数）
def my_route():
```

Flask 从下往上包裹，所以这个顺序确保：身份认证 → 权限校验。

### 4. 权限架构（RBAC 四层）

| 层级 | 组件 | 用途 |
|------|------|------|
| L1 | `permissions.py` 权限树 | 定义所有权限.code |
| L2 | 用户管理 UI | 管理员勾选权限 |
| L3 | `@permission_required()` | 后端路由保护 |
| L4 | `{% if user_can('code') %}` | 模板按钮显隐 |

**权限自动隐含规则**：细粒度按钮权限（如 `salary:edit-cell`）应自动授予所有有模块权限的用户，避免管理员漏配。

## 数据库设计模式

### 金额字段用 Numeric，不用 Float

```python
# ❌ Float 有精度问题
amount = db.Column(db.Float, default=0)

# ✅ Numeric(12,2) 精确到分
amount = db.Column(db.Numeric(12, 2), default=Decimal('0.00'))
```

### 迁移策略（SQLite 不支持 ALTER COLUMN）

```python
# 1. 新建表 _new
# 2. INSERT INTO ... SELECT CAST(...) FROM 旧表
# 3. DROP 旧表
# 4. ALTER TABLE _new RENAME TO 旧表名
```

### 索引检查（大数据量必做）

```python
from sqlalchemy import inspect
inspector = inspect(engine)
indexes = inspector.get_indexes('table_name')
```

## 前端模式

### SPA 式 AJAX 导航

- 侧边栏点击 → `fetch()` 获取页面 HTML
- 提取 `#pageContent` 的 innerHTML → `replaceChild` 刷新主区域
- 重新执行 `<script>` 块（浏览器不会自动执行 innerHTML 中的脚本）
- **必须设置 `X-Requested-With: XMLHttpRequest` 头**，否则权限装饰器返回 302 重定向

```javascript
fetch('/salary/module-table/', {
    headers: {'X-Requested-With': 'XMLHttpRequest'}
}).then(r => r.text()).then(html => {
    document.getElementById('pageContent').innerHTML = html;
});
```

### 动态表单 CSRF 豁免

JS 动态创建的 `<form>` 无法预置 `csrf_token`，必须在全局 `before_request` 豁免：

```python
@app.before_request
def global_csrf_protect():
    if request.method in ('POST', 'PUT', 'DELETE'):
        # 豁免：有 @login_required + @permission_required 的路由
        if request.path.startswith('/salary/') and ...:
            return
```

**核心原则**：双重保护（登录认证 + 权限校验）即可豁免 CSRF。

## 常见陷阱

| 陷阱 | 表现 | 排查 |
|------|------|------|
| 文件拆分后忘记 import | 路由 404，但 Python 语法正确 | `python3 -c "from app import app; app.url_map"` |
| before_request 漏 import session | 所有请求 500（包括 CSS/JS） | 对比 before_request 中的引用 vs import 行 |
| Jinja2 `<script>` 块中 `{{ var }}` 自动转义 | JS SyntaxError，`&#34;` 实体 | 加 `|safe` 过滤器 |
| AJAX 没设 X-Requested-With | fetch 拿到登录页 HTML 而不是 JSON | JS 加 headers |
| request.json 为 None | AttributeError: 'NoneType' | `data = request.json or {}` |
| 合计行修改误伤数据行 | 整列数据空白 | 确认改的是 `finance_totals` 还是 `dept_rows` |

## 参考链接

- [[工资管理系统]] — 项目实体
- [[工资系统安全架构]] — 安全模式
- [[openpyxl-企业导出优化]] — Excel 导出
- [[WeasyPrint-PDF生成配置]] — PDF 生成