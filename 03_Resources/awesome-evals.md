# awesome-evals — AI Agent 评估资源库

**项目地址**: https://github.com/benchflow-ai/awesome-evals  
**核心文件**: [README.md](https://github.com/benchflow-ai/awesome-evals/blob/main/README.md) | [PATTERNS.md](https://github.com/benchflow-ai/awesome-evals/blob/main/PATTERNS.md)  
**维护方**: BenchFlow (benchflow.ai)  
**收录**: 443+ 资源链接，146 篇深度笔记，10 大主题领域

## 对我们系统最有价值的部分

### 1. PATTERNS.md — 可执行评估代码模板
包含 10 个实用评估模式，每个模式都附带 Python 代码：
- **LLM-as-Judge** — 二值 PASS/FAIL 评估器（带 few-shot 批评示例）
- **pass@k/pass^k** — 无偏估计器（可靠性 vs 能力评估）
- **Code-based assertions** — 确定性断言测试（regex/JSON/DB 状态检查）
- **Error analysis** — 开放式编码→轴式编码→优先级排序
- **Trajectory & tool-use evaluation** — 轨迹匹配 + LLM 判断
- **Outcome / environment-state grading** — 最终状态差异对比
- **CI gating** — 回归测试套件
- **Verifiable reward** — RL 环境评估

### 2. promptfoo — 开源评估工具
已被 OpenAI 收购，仍 MIT 许可开源。  
**适用场景**: 为技能编写自动化测试用例  
**特性**: YAML 配置、确定性断言、LLM-as-Judge、CI/CD 集成  
**安装**: `npm install -g promptfoo` 或 `pip install promptfoo`

### 3. 核心方法论
- **评估比训练更重要**（Shunyu Yao）：瓶颈从"解决问题"转向"定义和评估问题"
- **验证的能力 == 创建 RL 环境的能力**（Jason Wei）：能自动化验证什么，就能训练什么
- **Agent 能力 60% 来自脚手架，不是模型**（Han-Chung Lee）：工具/框架/评估比底层 LLM 更重要
- **错误分析是最高 ROI 的活动**（Hamel Husain）：不要依赖通用框架，先看你的数据

## 对我们系统的直接应用

1. **改善 darwin-scan**：当前是静态正则评分，可引入 LLM-as-Judge 做技能实际效果的二值评估
2. **技能自动化测试**：用 promptfoo 为技能写测试用例（YAML + 断言），替代纯静态检查
3. **错误分析驱动修复**：先分析技能失败的维度→分类→优先级→针对性修复，而不是批量加模板
