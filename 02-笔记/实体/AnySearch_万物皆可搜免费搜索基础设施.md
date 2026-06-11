# AnySearch "万物皆可搜" — 免费开放的搜索基础设施

**来源**: 智能运维前线
**URL**: https://mp.weixin.qq.com/s/wT_yR7EdPKBND3AkdZulXw
**日期**: 2026-06-08

---

## 核心要点

### 是什么
专门给 AI Agent 和企业级 AI 系统提供的高质量数据接入基础设施。免费开放，零成本。

### 16 个垂直搜索领域
| 领域 | 说明 |
|------|------|
| code | 代码相关（文档、仓库、API） |
| travel | 旅行（航班、酒店、景点） |
| home | 家居 |
| ecommerce | 电商（商品搜索） |
| gaming | 游戏 |
| film | 电影 |
| music | 音乐 |
| finance | 金融（股票、外汇、商品期货） |
| academic | 学术（论文、DOI、arXiv） |
| legal | 法律（案例、法规） |
| business | 商业 |
| ip | 知识产权（专利、商标） |
| health | 医疗健康 |
| geo | 地理/地图 |
| environment | 环境 |
| energy | 能源 |

### 快速上手
1. 注册: https://www.anysearch.com/ （邮箱注册）
2. 获取 API Key: https://www.anysearch.com/console/api-keys/
3. 安装 Skill:
   ```bash
   curl -L -o anysearch-skill.zip https://github.com/anysearch-ai/anysearch-skill/archive/refs/heads/main.zip
   unzip anysearch-skill.zip
   mv anysearch-skill ~/.hermes/skills/anysearch
   ```

### 价值
- 替代 xcurl、浏览器插件、opencli 来回切换
- 自动去除网上噪音，找寻最佳数据源
- 支持接入任意 Agent 工作流
