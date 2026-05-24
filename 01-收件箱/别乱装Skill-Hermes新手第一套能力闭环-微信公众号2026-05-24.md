---
title: 别乱装 Skill：Hermes Agent 新手的第一套能力闭环
source: https://mp.weixin.qq.com/s/MrNesthFH4AeqFGzuSXOpQ
date: 2026-05-24
tags: [Hermes-Agent, Skill, 系统设计, 能力闭环]
value: ⭐⭐⭐
---

# 别乱装 Skill：Hermes Agent 新手的第一套能力闭环

> 来源：微信公众号，2026-05-24 抓取

---

## 核心观点

Hermes 的 Skill 不是"插件"，是 Agent 的**程序性记忆**——告诉 Agent 遇到某类任务时应该按什么流程做。

新手不该问"装多少个 Skill"，而该问"先让 Agent 学会哪几种基础工作能力"。

---

## 推荐的 7 个 Skill（能力闭环）

| 能力 | Skill | 作用 |
|------|-------|------|
| 规划 | `plan` | 执行前先想清楚：目标、约束、路径、验收标准 |
| 工具连接 | `native-mcp` | 接入外部工具/数据源，从"会聊天"走向"能行动" |
| 工程协作 | `github-pr-workflow` | 分支→commit→PR→review→CI→合并，进入真实工程流程 |
| 问题排查 | `systematic-debugging` | 先定位再修复：确认现象→复现→假设→实验→改代码 |
| 结果验证 | `test-driven-development` | 先定义"做对的标准"，用测试保护已有功能 |
| 资料研究 | 搜索/研究类 Skill | 输出前先查现实：文档、社区、版本、反例 |
| 表达优化 | `humanizer` | 最后一遍表达处理，把正确内容改得更自然、有人味 |

### 闭环逻辑

```
plan → native-mcp → github-pr-workflow → systematic-debugging
   → test-driven-development → 研究类 Skill → humanizer
```

---

## 关键论点

1. **不会规划的 Agent 越能执行越危险**——勤快地把错误方向推进得更远
2. **没有工具的 Agent 还是坐在房间里给建议的人**
3. **调试考验的不是"会不会改代码"，而是"能不能尊重事实"**
4. **TDD 不是形式主义**，是先回答"什么叫做做对了"
5. **语言能力 ≠ 事实能力**——写文章、做技术选型必须有外部资料支撑
6. **最后一公里是表达**——段落整齐句子正确，但没有真实判断 = 没有人味

---

## 对我系统的启示

- [ ] plan Skill 是否已配置？
- [ ] native-mcp 是否已配置 MCP 服务器？
- [ ] github-pr-workflow 是否已启用？
- [ ] systematic-debugging 是否已启用？
- [ ] test-driven-development 是否已启用？
- [ ] 搜索/研究类 Skill 是否齐全？（duckduckgo-search、arxiv、blogwatcher 等）
- [ ] humanizer 是否已安装？
