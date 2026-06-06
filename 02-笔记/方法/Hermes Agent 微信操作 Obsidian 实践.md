# Hermes Agent 实践：让微信 AI 接管 Obsidian

**作者**：Original Sophia  
**公众号**：地球美好不  
**发布时间**：2026年5月28日 07:07

---

## 引言

装上 Hermes Agent 后，希望它能提高效率。Obsidian 用了一个多月，感觉很实用。心想：既然都装了 Hermes Agent，能不能直接让它来操作 Obsidian？

试了一下，还真可以。

---

## 一、安装 Hermes Agent

安装很简单，一行命令：

```bash
curl -fsSL https://res1.hermesagent.org.cn/install.sh | bash
```

常用命令：

| 命令 | 用途 |
|------|------|
| `hermes` | 启动对话界面 |
| `hermes gateway` | 启动消息网关（连接微信要用） |
| `hermes gateway start` | 后台运行网关 |

> ⚠️ **踩坑**：对话和网关是独立进程，得分开启动。

---

## 二、把 Hermes 装进微信

步骤比想象简单：

1. 运行 `hermes gateway setup`，在列表中找到「微信」选中
2. 弹出二维码链接，复制到浏览器打开，用手机微信扫码
3. 微信里给 bot 发一条消息，它会回复配对码，例如：
   ```
   Pairing code: PIGX5N9I Run: hermes pairing approve weixin PIGX5N9I
   ```
4. 在终端运行配对命令，看到 `Approved!` 完成
5. 在微信里发 `/sethome`，告诉它哪个聊天窗口是「家」

> **价值**：从「在电脑前用AI工作」到「随时随地用AI工作」的分水岭。不需要打开 Terminal，不需要开 Web 界面，就在最常用的 App 里发消息就行。

---

## 三、安装 AI 新闻 Skill

Skill 是 Agent 的「外挂」，可以做特定的事。

### Skill 1：aihot（卡兹克制作）

专门查中文 AI 资讯。每天跑一下，就知道今天 AI 圈发生了什么。

```bash
hermes skill add aihot
```

### Skill 2：follow-builders（Zara Zhang）

质量更高。持续追踪 AI 领域的关键人物，抓他们的推文、爬最新播客的转录文本，全部翻译成中文，按固定格式整理成摘要输出。

```bash
hermes skill add zarazhangrui/follow-builders
```

> **效果**：每天早上起来，在微信里跟 Hermes 说「今天 AI 圈有什么」，它就去跑这两个 Skill，把全球 AI 大牛的动态整理成一份中文简报。连翻墙都省了。

这就是**信息差的磨平**。

---

## 四、在微信里操作 Obsidian

这是折腾这一整套东西的初心。

### 用法

在微信里发：
```
/obsidian 帮我搜索关于语音模型微调的笔记
```

Hermes 会自动加载 obsidian skill，去 Obsidian vault 里搜索，然后返回结果。

### 能力

- ✅ 搜索笔记
- ✅ 生成文档
- ✅ 整理思路
- ✅ 写大纲

> **体验**：就像有一个记忆力极好的助手，只需要说「那个啥来着」，它就已经把东西放你面前了。不需要自己先翻文档再看。

---

## 五、踩坑记录

### 问题 1：Hermes 在微信里不干活

发 `/obsidian 帮我搜索关于语音模型微调的笔记`，它返回一段代码。

**原因**：
1. 用了 `deepseek-v4` 模型，多了 `reasoning_content` 参数格式，调用工具时必须把那个参数回传回去
2. 工具集里没配 `file`、`terminal` 和 `skills`，缺了这些没办法实际调用工具

### 解决：给微信单独配工具

编辑 `~/.hermes/config.yaml`，在 `platform_toolsets` 下加一段 `weixin` 的配置：

```yaml
platform_toolsets:
  weixin:
    - file      # 搜本地 Obsidian、读文件
    - terminal  # 如果 skill 需要跑命令
    - skills    # 使用 /obsidian 等 skill
    - web       # 联网搜索
    - vision    # 微信里发图片让它看图
    - memory    # 记住长期信息
    - no_mcp    # 不自动加载 MCP server
```

改完重启 Gateway，微信里发个 `/new` 开新对话。

---

## 六、实操演示

### 1. 在手机上直接操作 Obsidian

要求 Hermes 在 Obsidian 里创建一个文档，内容是 voxcpm 的微调内容。

Obsidian 里自动增加了文章，都生成好了。

### 2. AI 新闻整理

用 follow-builders 和 aihot 技能整理 AI 新闻，质量很不错。

---

## 七、下一步

目前已搞定：
- ✅ Hermes Agent 装好了
- ✅ 微信连接成功，手机上能用了
- ✅ AI 新闻 Skill 装上，每天能看行业动态
- ✅ 微信里能写 Obsidian 了

**下一步计划**：

看看**幕布（Mubu）**有没有开放接口，因为每天的工作临时记录都放在幕布里，想让 Hermes 去抓幕布里的内容做分类整理，然后自动写到 Obsidian 里。这样就不需要自己手动整理了。

---

*来源：https://mp.weixin.qq.com/s/ugXO_Y43TX9XSxuXNygwjA*
