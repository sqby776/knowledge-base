---
title: 让 AI Agent 实现 Self-Evolution：通过 Skill 自优化实现能力跃迁
source: 微信公众号
url: https://mp.weixin.qq.com/s/VTAwjgWJ5QR2bsaUuNh_hQ
date: 2026-06-02
status: archived
type: article
tags:
related: [[Darwin-Skill]], [[Darwin-Skill]], [[EmbodiSkill]]] [skill, self-evolution, hermes, research, [[Darwin-Skill]], [[Darwin-Skill]]]
category: 思维框架
confidence: medium
---

# 让 AI Agent 实现 Self-Evolution：通过 Skill 自优化实现能力跃迁（摘要）

## 核心论点
AI 能力提升不一定靠更强的模型，而是通过"Skill 自优化"框架实现迭代提升。Agent 审计并改进自己的操作指令，性能就能显著升级。

## 三大主角

### [[Darwin-Skill]]（评测者）
- 微软研究院启发
- **9 维评分系统**（满分 100 分）
- 关键机制：
  - **棘轮机制（Ratchet）**：分数只能升不能降，降级自动回滚
  - **独立评测**：修改 Skill 的人和评测的人必须是不同 Agent（AI 自评准确率仅 46.4%，接近抛硬币）
  - 维度：Frontmatter 质量、工作流清晰度、失败模式编码、检查点设计、可执行性、反面案例/黑名单

### [[Darwin-Skill]]（进化者）
- 清华研究，在 Hermes Agent 中实现
- 核心哲学：**角色分离、闭环进化**
  - 作者 Agent 写 Skill
  - 执行 Agent 用 Skill（不知作者意图）
  - 信息不对称暴露 Skill 缺陷
- 三阶段：
  1. **策略多样化**：同一任务生成 3-4 个不同执行策略
  2. **对比更新**：成功 vs 失败轨迹对比，找到第一个分歧点（"分叉点"），patch 式修订
  3. **独立审计**：新 AI Session 按 9 条规则独立审计

### [[EmbodiSkill]]（裁判）
- 南京大学 + 微软 + 清华 AIR
- 贡献：**四类失败归因**
  1. Skill 缺陷 → 需要改 Skill
  2. 执行错误 → 记录附录，不改 Skill
  3. 关键洞察：区分这两者防止因偶发执行错误污染正确的 Skill

## 互优化实验（4 轮迭代）

| 指标 | [[Darwin-Skill]] | [[Darwin-Skill]] |
|------|-------------|-------------|
| 初始分数 | 61.0/100 | 81.5/100 |
| 最终分数 | **79.1/100** (+18.1) | **84.7/100** (+3.2) |
| 关键改进 | 新增 9 个 if-then 失败场景、7 个反面案例、3 个检查点 | 决策逻辑从二元改为四向分支 |

## 关键洞察

1. **模型强度不是唯一瓶颈** — 同一模型仅通过改进 Skill 就提升显著
2. **闭环进化系统**：
   - [[Darwin-Skill]]：定义 **如何改进**（方法论）
   - [[Darwin-Skill]]：定义 **何时停止+如何评分**（评估）
   - [[EmbodiSkill]]：定义 **为什么失败**（诊断）
3. **生物进化类比**：变异（策略多样化）→ 选择（评分）→ 遗传（棘轮机制）

## 对当前系统的参考价值
- 我们的 Skill 体系已有基础，但缺乏自动评测和改进机制
- 棘轮机制很有价值——Skill 改进应该"只升不降"，避免退化
- 独立评测原则：改 Skill 的人和评 Skill 的人必须不同
- 失败归因区分（Skill 缺陷 vs 执行错误）—— 这个我们目前完全没做
- 建议：为我们的核心 Skill（如 browser-fallback、data-analysis-zh）引入改进流程