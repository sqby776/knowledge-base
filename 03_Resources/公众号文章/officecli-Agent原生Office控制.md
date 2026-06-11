# 【SKILL 推荐】OfficeCLI：让 Agent 真正掌控 Word/PPT/Excel

> **"让 AI 写内容容易，让它排版输出就翻车？officecli 把 Office 文档变成 Agent 的原生对象，一条命令创建、读取、修改，还能实时预览。不用装 Office，不用拼 Python 库。"**

## 文章信息
- 来源：微信公众号·AI Zerone
- 链接：https://mp.weixin.qq.com/s/5qOlAY8kIO-9MLGz8DsP_g
- 作者：Zerone Zerone
- 关键词：officecli, Agent, Office自动化, Word/PPT/Excel, AI技能推荐

## 核心内容
### 痛点
1. 排版地狱：AI生成文本没问题，放进.docx或.pptx格式乱七八糟
2. 工具链碎片化：word调python-docx，excel搞openpyxl，ppt用python-pptx，API不一致
3. Agent是"盲人"：生成的文档长什么样AI看不到，无法自查自修

### 解决方案：OfficeCLI
- **GitHub Stars：5,000+**
- **单二进制文件，零依赖，不需要安装Office**
- **内置渲染引擎**：支持HTML/SVG/截图实时预览
- 核心思路：把.docx/.xlsx/.pptx变成Agent可以直接读写的对象

### 核心能力
1. **创建**：officecli create — 一句话生成排版好的文档
2. **修改**：officecli set — 像操作DOM一样精确修改文字/字体/颜色/布局
3. **预览**：officecli view/watch — 改一个字浏览器自动刷新，Agent能自己发现排版问题
4. **批量**：officecli batch — 模板+批量，100份合同一键生成
5. **自动集成**：officecli install — 自动检测Claude Code/Cursor/Codex，安装skill文件

### 价值
从"格式搬运工"到"文档导演"：定结构→审效果→一键交付

### 安装
- Zerone Skill Market搜索officecli
- 或运行 officecli install 自动集成所有AI工具

---
