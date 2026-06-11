# 商汤 SenseNova-Skills — 开源办公自动化 Skill 系统

**来源**: 商汤科技
**URL**: https://mp.weixin.qq.com/s/-eaXA4eFI7iE5CoD2DcCwg
**日期**: 2026-06-08
**GitHub**: https://github.com/OpenSenseNova/SenseNova-Skills/

---

## 核心能力

### 场景1: Office 数据分析
- 多文件 Excel → 员工绩效分析报告
- 数据清洗 → 分层统计 → 自动生成图表 → Word报告+HTML可视化
- 支持大文件分块流式处理 + OCR识别图片表格

### 场景2: 自动化深度研究
- 单句提示 → 专业行业报告
- 自动构建框架 → 多源证据采集 → 数据冲突交叉验证 → 结构化结论
- 支持断点恢复和研究过程归档

### 场景3: 多 Skill 链式 PPT 生成
- Deep Research + Data Analysis + PPT Generation 链式调用
- 受众优先锁定 → 叙事线构建 → 像素级视觉质量检查
- standard/creative 双模式

## 架构特点
- 模块化 SKILL.md 设计，独立文件夹
- 兼容主流 Agent 框架，无厂商锁定
- 行业知识封装为"工作手册"

## 与 Hermes 的关系
- **完全兼容**: 商汤 Skills 是标准 SKILL.md 格式，可直接放入 Hermes 技能库
- **互补性强**: Hermes 有 powerpoint/skill，商汤有 Office 数据分析 + 深度研究链式工作流
- **建议**: 值得安装测试，补充 Hermes 在 Office 自动化方面的能力

## 安装方式
```bash
# 克隆到技能目录
git clone https://github.com/OpenSenseNova/SenseNova-Skills/ ~/.hermes/skills/sensenova/
# 或从 agentskills.io 搜索安装
```

## 潜在价值
1. **Office 数据分析**: 直接填补我们 Office 办公场景的数据处理空白
2. **链式工作流**: 研究→分析→报告→PPT 全自动，当前 Hermes 需要手动编排
3. **模块化**: SKILL.md 设计符合我们的规范，可直接复用
