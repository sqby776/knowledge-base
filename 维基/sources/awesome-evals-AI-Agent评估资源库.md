---
title: awesome-evals — AI Agent 评估资源库
type: source
tags: [llmwiki]
sources: [03_Resources/awesome-evals.md]
credibility: 80%
contradicts: []
created: 2026-06-29
updated: 2026-06-29
---

# awesome-evals — AI Agent 评估资源库

**项目**: BenchFlow awesome-evals (github.com/benchflow-ai/awesome-evals)  
**收录**: 443+ 资源链接，146 篇深度笔记，10 大主题领域

## 摘要

开源 AI Agent 评估资源聚合库，包含 10 个实用评估模式的 Python 实现（PATTERNS.md），覆盖 Agent 能力测试、LLM-as-Judge、错误分析驱动修复等关键方法。维护方为 BenchFlow (benchflow.ai)。

## 要点

- PATTERNS.md 提供可执行的评估代码模板：LLM-as-Judge (二值 PASS/FAIL)、pass@k、确定性评估、回归测试等
- Agent 能力 60% 来自脚手架（工具/框架/评估），不是底层 LLM 本身
- 错误分析是最高 ROI 的评估活动：不要依赖通用框架，先看实际数据
- 推荐工具：promptfoo（YAML + 断言的技能测试）、LangSmith、Arize Phoenix
- 可直接用于改善 darwin-scan 技能评估、技能自动化测试、错误分析驱动修复

## 可信度说明

开源项目，有活跃的 GitHub 维护和社区贡献。内容引用自行业专家（Han-Chung Lee, Hamel Husain），可信度较高。

## 提及的实体

- [[BenchFlow]]
- [[promptfoo]]
- [[LangSmith]]

## 相关概念

- [[AI Agent 评估]]
- [[LLM-as-Judge]]
- [[技能测试]]
