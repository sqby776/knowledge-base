---
site: "https://github.com/NousResearch/hermes-agent"
title: "Hermes Agent GitHub 仓库 README"
fetched_at: "2026-06-29"
status: "success"
tags: [hermes, github, README, 安装, 功能, 社区]
---

# 知识点清单

## 1. 仓库概况
- **标题**: GitHub 仓库基本信息
- **摘要**: NousResearch/hermes-agent，MIT 许可证，由 Nous Research 构建。文档位于 hermes-agent.nousresearch.com/docs。社区入口：Discord、Skills Hub、Issues。
- **标签**: #hermes #github #repo

## 2. Windows 安装细节
- **标题**: Windows 原生安装与防病毒白名单
- **摘要**: Windows PowerShell 安装器自动处理 uv、Python 3.11、Node.js、ripgrep、ffmpeg 和便携式 MinGit。`uv.exe` 可能被 Windows Defender/Bitdefender 误报为恶意软件——README 提供了官方验证脚本和文件夹白名单方案。
- **标签**: #hermes #windows #antivirus #fals-positive

## 3. uv.exe 误报验证方法
- **标题**: 验证 uv.exe 真实性
- **摘要**: 通过 GitHub CLI 的 `gh attestation verify` 验证 uv zip 包签名，然后比对哈希值。白名单建议按文件夹而非文件哈希白名单（因为版本更新哈希会变）。
- **标签**: #hermes #uv #verification #security

## 4. 贡献者开发流程
- **标题**: 开发者快速开始
- **摘要**: 推荐标准安装器→从 $HERMES_HOME/hermes-agent 工作。`uv pip install -e ".[all,dev]"` 安装全部依赖。也支持手动 clone 方式。
- **标签**: #hermes #contributing #development

## 5. 项目可读性
- **标题**: 多语言 README
- **摘要**: 提供中文(README.zh-CN.md)、乌尔都语(README.ur-pk.md)、西班牙语(README.es.md)等多语言版本。
- **标签**: #hermes #i18n #multilingual

## 6. CLI 命令速查
- **标题**: Hermes 命令行大全
- **摘要**: `hermes`（交互 CLI）、`hermes model`（选模型）、`hermes tools`（配置工具）、`hermes config set`（设置）、`hermes gateway`（消息网关）、`hermes setup`（安装向导）、`hermes claw migrate`（从 OpenClaw 迁移）、`hermes update`（更新）、`hermes doctor`（诊断）。
- **标签**: #hermes #cli #commands
