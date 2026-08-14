### 2026-08-15 07:00:00 后台维护

#### 抓取编译
| 操作 | 详情 |
|:----|:------|
| 收件箱扫描 | 01-收件箱/自动捕获 与 01_inbox/articles 各 6 个捕获文件（pandas/Data_Visualization/Quick_start_guide/csv/json/pathlib），跨收件箱 MD5 完全一致（双路径例行写入） |
| 内容比对 | 6 个捕获与 2026-08-14 存档归一化比对：全部内容一致（规范化 hash 相同），均无实质变化。csv 的 08-13 版为 Sniffer 结构性更新唯一版本（保留），08-14/08-15 内容相同 |
| 编译判断 | 全部为已知来源例行捕获，无新知识点，不触发编译/实体笔记更新 |

#### 整理归档
| 操作 | 详情 |
|:----|:------|
| 两份归档 | 01-收件箱/archive/自动捕获/2026-08-15/ 与 01_inbox/archive/articles/2026-08-15/ 各 6 文件 |
| 收件箱状态 | 全部清空（01-收件箱/ 各子目录、01_inbox/articles/ 均无待处理 md） |
| 重复副本删除 | 02-笔记/实体/学习报告_2026_08_10md.md 为 archive/自动学习/2026-08-10/学习报告_2026-08-10.md 的字节相同副本（md5: b91bebad...），auto-compile 错误命名产物，删除 |

#### 去重归纳
| 操作 | 详情 |
|:----|:------|
| 归档精确去重 | 内容规范化 hash 去重：01-收件箱/archive/自动捕获 删 11 份（08-13/08-14 重复→保留 08-15），01_inbox/archive/articles 删 11 份，共 22 份。csv 08-13 唯一版（Sniffer 更新）保留 |
| Hermes_Agent | 66 份归档中 65 组内容唯一（每日 llms hash 引用变化），按参考规范不修剪，保持现状 |
| 小文件验证 | 13 个 <1KB 文件逐一检查：12 个合法速查卡/概念卡（结构化内容保留），Quick_start_guide.md 为已知自动重建 stub（方案A跳过，enriched 版 Quickstart-Guide.md 70KB 兜底） |
| 补充笔记 | Hermes_站点学习报告.md 从 v0.17 stub（774B）升级为 v0.20.0 完整版（3695B，含版本基线/亮点/文档体系/站点状态/信息缺口），落实 08-10 学习报告建议 |
| 地图更新 | 07_moc/知识地图.md 实体统计 62→61，updated → 2026-08-15 |

#### 知识库统计
| 分类 | 文件数 | 变动 |
|:----|:------|:-----|
| 实体 | 61 | -1（删除重复副本） |
| 概念 | 39 | 不变 |
| 方法 | 50 | 不变 |
| 学习要点 | 0 | 不变 |

#### 跟踪文件
| 操作 | 详情 |
|:----|:------|
| _hash_tracker.md | 上次更新 2026-08-01，今天无 Hermes_Agent 捕获，无需更新 |
| .last-compile | 更新中 |

---

### 2026-08-14 07:00:00 后台维护

#### 抓取编译
| 操作 | 详情 |
|:----|:------|
| 收件箱扫描 | 01-收件箱/自动捕获 与 01_inbox/articles 各 6 个捕获文件（pandas/Data_Visualization/Quick_start_guide/csv/json/pathlib） |
| 内容比对 | 6 个捕获与 2026-08-13 存档归一化比对：10_minutes_to_pandas、Data_Visualization_With_Python、Quick_start_guide 内容完全一致；json/pathlib 仅"Last updated"日期变化（无实质性）；csv 有结构性变化——Sniffer 类文档更新（硬编码优先顺序列表→引用 `preferred` 属性，新增 `Sniffer` 类属性说明） |
| 实体笔记更新 | csv 实体笔记已有 10 处 Sniffer 引用且已包含 preferred 属性，不触发更新 |

#### 整理归档
| 操作 | 详情 |
|:----|:------|
| 两份归档 | 01-收件箱/archive/自动捕获/2026-08-14/ 与 01_inbox/archive/articles/2026-08-14/ 各 6 文件，MD5 完全一致（双路径例行写入） |
| 收件箱状态 | 全部清空（01-收件箱/ 各子目录、01_inbox/articles/ 均空） |

#### 去重归纳
| 操作 | 详情 |
|:----|:------|
| 归档重复 | 01_inbox/archive/articles/ 中 Hermes_Agent 累计 66 份（较上次 41 份增 25 份），建议择机修剪 |
| 内容验证 | 6 个文件仅 csv 有实质更新（Sniffer 类文档改进），其余无实质性内容变化 |
| 补充笔记 | 0 篇（无新知识点） |
| 地图更新 | 否（例行捕获，无新领域/新知识点） |

#### 知识库统计
| 分类 | 文件数 | 变动 |
|:----|:------|:-----|
| 实体 | 62 | 不变 |
| 概念 | 39 | 不变 |
| 方法 | 50 | 不变 |
| 学习要点 | 0 | 不变 |

#### 跟踪文件
| 操作 | 详情 |
|:----|:------|
| _hash_tracker.md | 上次更新 2026-08-01，今天无 Hermes_Agent 捕获，无需更新 |
| .last-compile | 更新中 |

---

### 2026-08-13 20:03:38 后台维护（补充）

#### 抓取编译
| 操作 | 详情 |
|:----|:------|
| 收件箱扫描 | 所有活跃目录为空（01-收件箱/自动学习/仅_hash_tracker.md、自动捕获/空、已处理/空、文章/空、_from_user/空；01_inbox/articles/空） |
| 内容比对 | 6 个捕获文件（08-13 07:00）与 2026-07-16 存档版本内容归一化对比：Data_Visualization_With_Python 仅登录参数变化，csv/json/pathlib 仅 Python 版本号 3.14.6→3.14.7，Quick_start_guide 仅 Matplotlib 版本号 3.11.0→3.11.1，均无实质性内容变化 |
| 小文件检查 | 13 个 <1KB 文件逐一验证：12 个为合法速查卡（含 wikilinks/表格/结构化内容/archived 状态），Quick_start_guide.md 为已知自动重建 stub（指向 Quickstart-Guide.md 70KB enriched 版） |

#### 整理归档
| 操作 | 详情 |
|:----|:------|
| 两份归档 | 01-收件箱/archive/自动捕获/2026-08-13/ 与 01_inbox/archive/articles/2026-08-13/ 各 6 文件，MD5 完全一致（双路径例行写入） |
| 收件箱状态 | 全部清空（01-收件箱/ 各子目录、01_inbox/articles/ 均空） |

#### 去重归纳
| 操作 | 详情 |
|:----|:------|
| 归档重复 | 01_inbox/archive/articles/ 中 Hermes_Agent 累计 41 份（含 v2/v3 变体），建议下次修剪；Python 文档各 2-4 份可接受 |
| 内容验证 | 6 个文件无实质性内容变化（仅版本号/导航链接微小差异），不触发实体笔记更新 |
| 补充笔记 | 0 篇（无新知识点） |
| 地图更新 | 否（例行捕获，无新领域/新知识点） |

#### 知识库统计
| 分类 | 文件数 | 变动 |
|:----|:------|:-----|
| 实体 | 62 | 不变 |
| 概念 | 39 | 不变 |
| 方法 | 50 | 不变 |
| 架构 | 1 | 不变 |
| 学习要点 | 0 | 不变 |

#### 跟踪文件
| 操作 | 详情 |
|:----|:------|
| _hash_tracker.md | 上次更新 2026-08-01，今天无 Hermes_Agent 捕获，无需更新 |
| .last-compile | 两个路径均已更新至 2026-08-13 20:03:38 |

---

### 2026-08-13 07:00:00 后台维护

#### 抓取编译
| 操作 | 详情 |
|:----|:------|
| 收件箱扫描 | 01-收件箱/自动捕获 与 01_inbox/articles 各 6 个捕获文件（pandas/Data_Visualization/Quick_start_guide/csv/json/pathlib） |
| 内容比对 | 6 个捕获与 2026-08-12 存档归一化比对：10_minutes_to_pandas、Data_Visualization_With_Python、Quick_start_guide 内容完全一致；csv/json/pathlib 仅 frontmatter 创建日期变化（08-12→08-13），正文无结构性变更 |
| hash_tracker | 无新捕获（Hermes Agent 未捕获），_hash_tracker.md 上次更新 2026-08-01，无待处理条目 |

#### 整理归档
| 操作 | 详情 |
|:----|:------|
| 已归档 | 01-收件箱/archive/自动捕获/2026-08-13/ 6 文件 |
| 已归档 | 01_inbox/archive/articles/2026-08-13/ 6 文件 |
| 收件箱状态 | 全部清空（01-收件箱/ 各子目录、01_inbox/articles/ 均空） |

#### 去重归纳
| 操作 | 详情 |
|:----|:------|
| 归档去重（内容归一化 hash） | 01-收件箱/archive/自动捕获/ 删 78 重复 → 余 19 文件；01_inbox/archive/articles/ 删 69 重复 → 余 95 文件 |
| 小文件检查 | 12 个 <1KB 文件逐一验证：全部为合法速查卡（含 wikilinks/表格/结构化内容），无空壳 stub |
| 补充笔记 | 0 篇（无新知识点，均为例行捕获） |
| 陈旧备份 | 0 个（99-归档/ 无 .bak 文件） |

#### 知识库统计
| 分类 | 文件数 | 变动 |
|:----|:------|:-----|
| 实体 | 62 | 不变 |
| 概念 | 39 | 不变 |
| 方法 | 50 | 不变 |

### 2026-08-12 07:04:00 后台维护

#### 抓取编译
| 操作 | 详情 |
|:----|:------|
| 收件箱扫描 | 01-收件箱/自动捕获 与 01_inbox/articles 各 7 个捕获文件（pandas/Data_Visualization/Getting_Started/Quick_start_guide/csv/json/pathlib） |
| 内容比对 | 6 个常规捕获与 2026-08-11 存档归一化比对：内容完全一致，仅 frontmatter created/updated 日期变化（08-11→08-12），无结构性变更；Getting_Started.md（python-pptx 快速入门）为新增捕获，实体笔记已存在（8KB），无新增知识点 |

#### 整理归档
| 操作 | 详情 |
|:----|:------|
| 已归档 | 01-收件箱/archive/自动捕获/2026-08-12/ 7 文件 |
| 已归档 | 01_inbox/archive/articles/2026-08-12/ 7 文件 |
| 收件箱状态 | 全部清空（01-收件箱/ 各子目录、01_inbox/articles/ 均空） |

#### 去重归纳
| 操作 | 详情 |
|:----|:------|
| 重复文件 | 0 个（Quick_start_guide.md 840B 为已知自动重建 stub，跳过；Quickstart-Guide.md 70KB enriched 版为引用目标） |
| 小文件检查 | 12 个 <1KB 文件逐一验证：11 个为合法速查卡（含 wikilinks/表格/结构化内容），Quick_start_guide.md 为已知 stub |
| 归档去重 | 无需处理（前几轮已清理，本轮无 _N 后缀目录） |
| 补充笔记 | 0 篇（无新知识点，均为例行捕获） |
| 陈旧备份 | 0 个（99-归档/ 无 .bak/.bak.old/_old.md） |

#### 统计更新
| 操作 | 详情 |
|:----|:------|
| 实体 | 62 篇 |
| 概念 | 39 篇 |
| 方法 | 50 篇 |
| 地图 | 07_moc/知识地图.md 实体统计 57→62 修正，updated → 2026-08-12（无新领域，主题地图本身无需变更） |

#### 最终状态
- 收件箱全部清空：01-收件箱/（各子目录）、01_inbox/articles/ 均空
- last-compile 同步: 是（knowledge/.last-compile 与 01_inbox/.last-compile 均已更新至 2026-08-12 07:04:17）

### 2026-08-11 07:02:54 后台维护

#### 抓取编译
| 操作 | 详情 |
|:----|:------|
| 收件箱扫描 | 所有收件箱目录为空（01-收件箱/ 各子目录、01_inbox/articles/ 均无待处理文件） |
| 自动捕获 | 6 个标准捕获文件已直接归档到 01-收件箱/archive/自动捕获/2026-08-11/（pandas/Data_Visualization/Quick_start_guide/csv/json/pathlib） |

#### 整理归档
| 操作 | 详情 |
|:----|:------|
| 双路径归档 | 01-收件箱/archive/自动捕获/2026-08-11/ ✓（06:00 捕获脚本直接写入） |
| 双路径补齐 | 01_inbox/archive/articles/2026-08-11/ 6 文件（从 自动捕获 复制以保持双路径一致） |

#### 去重归纳
| 操作 | 详情 |
|:----|:------|
| 重复文件 | 0 个（Quick_start_guide.md 为已知自动重建 stub，840B，已跳过） |
| 小文件检查 | 实体 7 个 + 概念 5 个 + 架构 1 个 <1KB，均为合法速查卡（status: archived/含结构化表格），无需处理 |
| 补充笔记 | 0 篇（无新知识点，均为例行捕获） |
| 归档二次去重 | 5 天（08-06/08-08/08-09/08-10/08-11）X 6 文件 = 30 个归档条目，文件大小一致，属正常连续捕获，跳过归档去重 |
| Hermes_Agent 追踪 | 上次捕获 2026-08-01，`_hash_tracker.md` 已重置，本轮无新捕获，无需更新 |

#### 统计更新
| 操作 | 详情 |
|:----|:------|
| 实体 | 62 篇 |
| 概念 | 39 篇 |
| 方法 | 50 篇 |
| 架构 | 1 篇 |
| 地图 | 无需更新（无新实体/概念/方法，三个地图均为 status: archived） |

#### 最终状态
- 收件箱全部清空：01-收件箱/（各子目录）、01_inbox/articles/ 均空
- last-compile 同步: 是（knowledge/.last-compile 与 01_inbox/.last-compile 均已更新至 2026-08-11 07:02:54，由捕获脚本自动更新）

### 2026-08-10 07:02:54 后台维护

#### 抓取编译
| 操作 | 详情 |
|:----|:------|
| 收件箱扫描 | 01-收件箱/自动捕获 与 01_inbox/articles 各 6 个标准捕获（pandas/Data_Visualization/Quick_start_guide/csv/json/pathlib） |
| 内容比对 | 与 2026-08-06 存档内容归一化比对：全部 6 个文件内容一致，仅 footer "Last updated" 时间戳变化（Aug 05→Aug 09），无结构性变更 |

#### 整理归档
| 操作 | 详情 |
|:----|:------|
| 已归档 | 01-收件箱/archive/自动捕获/2026-08-10/ 6 文件 |
| 已归档 | 01_inbox/archive/articles/2026-08-10/ 6 文件 |
| 重复草稿 | 99-归档/2026-08-10/实体-重复草稿/Quick_start_guide.md (840B) — 已知自动重建 stub，已隔离 |

#### 去重归纳
| 操作 | 详情 |
|:----|:------|
| 重复文件 | 1 个（Quick_start_guide.md stub，跨收件箱 6 对文件均为字节相同，各归档一份） |
| 小文件检查 | 实体 6 个 + 概念 5 个 <1KB，均为合法速查卡（status: archived/含结构化表格），无需处理 |
| 补充笔记 | 0 篇（无新知识点，均为例行捕获） |

#### 统计更新
| 操作 | 详情 |
|:----|:------|
| 实体 | 57 篇 |
| 概念 | 39 篇 |
| 方法 | 50 篇 |
| 地图 | 无需更新（无新实体/概念/方法） |

#### 最终状态
- 收件箱全部清空：01-收件箱/（各子目录）、01_inbox/articles/ 均空
- last-compile 同步: 是（knowledge/.last-compile 与 01_inbox/.last-compile 均已更新至 2026-08-10 07:02:54）

### 2026-08-09 13:03:43 后台维护

#### 抓取编译
| 操作 | 详情 |
|:----|:------|
| 收件箱扫描 | 所有收件箱目录为空（01-收件箱/ 各子目录、01_inbox/articles/、articles/ 均无待处理文件） |
| 预报告 | 新抓取 1 / 待编译 0 — 实际对应 7 个标准捕获已归档（见下） |

#### 整理归档
| 操作 | 详情 |
|:----|:------|
| 已归档 | 01-收件箱/archive/自动捕获/2026-08-09/ 7 个标准捕获（pandas/Data_Visualization/Getting_Started/Quick_start_guide/csv/json/pathlib）已在上一轮处理 |
| 重复草稿 | 99-归档/2026-08-09/实体-重复草稿/Quick_start_guide.md (840B) — 已知自动重建 stub，已隔离 |

#### 去重归纳
| 操作 | 详情 |
|:----|:------|
| 重复文件 | 0 个（无跨收件箱重复） |
| 小文件检查 | 实体 5 个 + 概念 5 个 <1KB，均为合法速查卡（status: archived，含结构化表格/定义），无需处理 |
| 补充笔记 | 0 篇（无新知识点，均为例行捕获） |
| 过期备份 | 清理 1 个：维基/.manifest.json.bak (6909B) |

#### 统计更新
| 操作 | 详情 |
|:----|:------|
| 07_moc/知识地图.md | 实体 58→57（因 Quick_start_guide stub 移入归档），概念 39 / 方法 50 不变，updated 同步至 2026-08-09 |
| last-compile 同步 | 两个 .last-compile 更新至 2026-08-09 13:03:43 |

#### 无操作
- 地图主题更新：无需更新（无新领域/实体信息，Hermes-能力地图.md 例行捕获无结构变化）

### 2026-08-08 13:02:55 后台维护

#### 抓取编译
| 操作 | 详情 |
|:----|:------|
| 新抓取 | 6 个（pandas/Data_Visualization/Quick_start_guide/csv/json/pathlib） |
| 编译 | 全部 6 个已有编译笔记（02-笔记/下均已存在），无新内容 |

#### 整理归档
| 操作 | 详情 |
|:----|:------|
| 字节级去重 | 01_inbox/articles/ 6 个文件与 01-收件箱/archive/自动捕获/2026-08-08/ 字节完全相同，已删除 inbox 副本 |

#### 去重归纳
| 操作 | 详情 |
|:----|:------|
| 重复文件 | 0 个（仅清理跨收件箱重复的 raw 副本） |
| 补充笔记 | 0 篇（无新知识点） |

#### 统计更新
| 操作 | 详情 |
|:----|:------|
| 07_moc/知识地图.md | 实体 58 / 概念 39 / 方法 50（与前次一致，无变化） |
| last-compile 同步 | 两个 .last-compile 更新至 2026-08-08 13:02:55 |

#### 无操作
- 地图更新：无需更新（无新领域/实体信息）

### 2026-08-07 20:00 后台维护

#### 检查
| 操作 | 详情 |
|:----|:------|
| 收件箱扫描 | 所有收件箱目录为空，无待处理文件 |
| 小文件检查 | 13 个 < 1KB 文件，均为合法速查卡或已知自动重建 stub，无需处理 |
| 过期备份 | 0 个待清理 |

#### 统计更新
| 操作 | 详情 |
|:----|:------|
| 07_moc/知识地图.md | 实体 56→58，概念 40→39，更新日期同步至 2026-08-07 |
| last-compile 同步 | .last-compile + 01_inbox/.last-compile 已更新至 2026-08-07 20:03 |

#### 无操作
- 抓取编译：无新文件
- 整理归档：无待归档文件
- 去重归纳：无重复文件
- 地图更新：无需更新（Hermes-能力地图.md 上次更新 2026-06-22，无新领域信息）

### 2026-08-06 07:07 后台维护

#### 修复
- `daily-capture.sh` 依赖全面修复：安装 html2text, scrapling, curl_cffi, playwright, browserforge
- `office-venv/bin/python3` symlink 已确认指向 `/usr/bin/python3` (3.14.4)

#### 抓取
| 操作 | 详情 |
|:----|:------|
| 重跑抓取 | 9/12 成功（3 个站点仍失败：python-docx table.html、obsidian help 页面） |
| 新入库 | 9 个文件 → 01_inbox/archive/articles/2026-08-06/ |

#### 编译
| 操作 | 详情 |
|:----|:------|
| auto-compile-fast.py | 9 个文件处理完成 |
| 新编译笔记 | 2 个：Data_Visualization_With_Python.md（827B）、Quick_start_guide.md（840B） |
| 跳过（已存在） | 7 个已知页面（内容无变化） |

#### 归档
| 操作 | 详情 |
|:----|:------|
| 01_inbox/articles/ → archive | 9 个文件移至 01_inbox/archive/articles/2026-08-06/ |
| 同步到自动捕获 | 9 个文件同步到 01-收件箱/自动捕获/ |

#### 去重
| 操作 | 详情 |
|:----|:------|
| 小文件扫描 | 13 个 < 1KB 文件，全部为合法笔记或已知自动重建 stub，无需处理 |
| 异常文件 | 无异常 |

#### 最终状态
- 收件箱：全部清空
- 02-笔记：实体 58 + 概念 39 + 方法 50 = 147 个文件
- 07-地图：无变更
- 依赖：系统 Python3 已修复

### 2026-08-01 20:10 后台维护（第2轮）

| 操作 | 详情 |
|:----|:------|
| 编译 | 01_inbox/articles/ 第2个新文件 (Hermes Agent 2026-08-01 v2) — 同一来源，llms-full.txt hash 从 `3f7f7630...` 变更为 `af56719b...`，页面内容无结构性变化，仅 llms-full 聚合文件重新生成 |
| 实体补充 | 知识库/02-笔记/概念/Hermes-Agent.md body hash 更新：llms-full.txt 从 `3f7f7630...` → `af56719b...`；knowledge/02-笔记/实体/Hermes_Agent.md 同步更新 |
| 日期断层回填 | 自 2026-07-24 以来 changelog 冻结，回填 07-26 ~ 08-01 共 9 条 hash-only 记录（含 07-28 结构性更新），合并为批量总结条目 |
| 归档 | 01_inbox/articles/2026-08-01_Hermes_Agent.md → archive/articles/2026-08-01/2026-08-01_Hermes_Agent_v2.md ✅ |
| 去重检查 | 02-笔记/ 无新精确重复（实体 56 + 概念 40 + 方法 50 = 146）；无 stub 草稿；无陈旧备份 |
| 地图检查 | 07-地图/ 3 个文件无变更（routine re-capture，hash-only 变更，无新实体/概念） |

### 2026-08-01 07:02 后台维护

| 操作 | 详情 |
|:----|:------|
| 编译 | 01_inbox/articles/ 1 个新文件 (Hermes Agent 2026-08-01) — 同一来源，hash 与 07-31 相同（llms.txt `faaf9398...`、llms-full.txt `3f7f7630...`），无结构性变化 |
| 实体补充 | 知识库/02-笔记/概念/Hermes-Agent.md body hash 更新：llms.txt 从 `96828202...`（陈旧）→ `faaf9398...`；frontmatter updated 更新至 2026-08-01 |
| 归档 | 01_inbox/articles/2026-08-01_Hermes_Agent.md → archive/articles/2026-08-01/ ✅ |
| 去重检查 | 02-笔记/ 无新精确重复（实体 56 + 概念 40 + 方法 50 = 146）；无 stub 草稿；无学习要点垃圾文件；无陈旧备份 |
| 地图检查 | 07-地图/ 3 个文件无变更（routine re-capture，hash 与昨日相同，无新实体/概念） |

最终状态：
- 01_inbox/articles: 0（已全部归档）✅
- 01-收件箱/所有子目录: 空 ✅（仅 _hash_tracker.md 跟踪文件）
- 02-笔记 合计 146 个文件（实体 56 + 概念 40 + 方法 50）
- 知识库/02-笔记 合计 17 个文件（实体 8 + 概念 4 + 方法 5）
- 01_inbox/archive/articles/2026-08-01/: 1 个文件
- 07-地图/ 3 个文件无变更
- .last-compile 已刷新

### 2026-07-31 07:03 后台维护

| 操作 | 详情 |
|:----|:------|
| 编译 | 01_inbox/articles/ 1 个新文件 (Hermes Agent 2026-07-31) — 同一来源，llms-full.txt hash 与昨日 v2 相同 (`3f7f7630...`)，无结构性变化 |
| 实体补充 | 知识库/02-笔记/概念/Hermes-Agent.md body hash 更新至 `3f7f7630...`（从 `66f5f767...`）；frontmatter updated 更新至 2026-07-31；changelog 冻结态继续（18+ 连续 hash-only），hash 追踪重定向至 _hash_tracker.md |
| 归档 | 01_inbox/articles/2026-07-31_Hermes_Agent.md → archive/articles/2026-07-31/ ✅ |
| 去重检查 | 02-笔记/ 无新精确重复（实体 56 + 概念 40 + 方法 50 = 146）；无 stub 草稿；无学习要点垃圾文件；无陈旧备份 |
| 地图检查 | 07-地图/ AI技术地图 + 办公自动化地图 — 均为 archived 状态，无需更新（routine re-capture，hash 与昨日相同，无新实体/概念） |

最终状态：
- 01_inbox/articles: 0（已全部归档）✅
- 01-收件箱/所有子目录: 空 ✅（仅 _hash_tracker.md 跟踪文件）
- 02-笔记 合计 146 个文件（实体 56 + 概念 40 + 方法 50）
- 知识库/02-笔记 合计 17 个文件（实体 8 + 概念 4 + 方法 5）
- 01_inbox/archive/articles/2026-07-31/: 1 个文件
- 07-地图/ 5 个文件无变更（AI技术地图、办公自动化地图、知识地图、Hermes-能力地图、结晶摘要）
- .last-compile 已刷新

### 2026-07-30 07:04 后台维护

| 操作 | 详情 |
|:----|:------|
| 编译 | 01_inbox/articles/ 2 个新文件 (Hermes Agent 2026-07-29 第2轮 + 2026-07-30 例行捕获) — 07-29 第2轮 llms.txt hash 从 `8c526336...` 变更为 `faaf9398...`（结构性变更），llms-full.txt 从 `69431bab...` 变更为 `d4be4eec...`；07-30 例行捕获 llms.txt `faaf9398...` 保持稳定，llms-full.txt `07bdf65d...`（例行部署） |
| 实体补充 | 实体/Hermes_Agent.md body hash 更新至 llms.txt=`faaf9398...`、llms-full.txt=`07bdf65d...`；changelog 追加 2026-07-30 例行捕获条目；`最后更新` 日期更新至 2026-07-30 |
| 归档 | 01_inbox/articles/2026-07-29_Hermes_Agent.md → archive/articles/2026-07-29/_v2 ✅ |
| | 01_inbox/articles/2026-07-30_Hermes_Agent.md → archive/articles/2026-07-30/ ✅ |
| 去重检查 | 02-笔记/ 无新精确重复（实体 56 + 概念 40 + 方法 50 = 146）；无 stub 草稿；无学习要点垃圾文件；无陈旧备份 |
| 地图检查 | 07-地图/ AI技术地图 + 办公自动化地图 — 均为 archived 状态，无需更新（routine re-capture，无新实体/概念） |

最终状态：
- 01_inbox/articles: 0（已全部归档）✅
- 01-收件箱/所有子目录: 空 ✅（仅 _hash_tracker.md 跟踪文件）
- 02-笔记 合计 146 个文件（实体 56 + 概念 40 + 方法 50）
- 01_inbox/archive/articles/2026-07-29/: 2 个文件（07:00 + 20:00 v2）
- 01_inbox/archive/articles/2026-07-30/: 1 个文件（07:00）
- 07-地图/ 3 个文件无变更（均已 archived）
- .last-compile 已刷新

### 2026-07-28 20:00 后台维护

| 操作 | 详情 |
|:----|:------|
| 编译 | 01_inbox/articles/ 1 个新文件 (Hermes Agent 2026-07-28 第3轮 20:00) — 字节级不同（md5 不同），llms-full.txt hash 从 `25649c0e...` 变更为 `f20bdddc...`（当日第3次部署，无结构性变化），llms.txt `96828202...` 保持稳定（第 19 天） |
| 实体补充 | 实体/Hermes_Agent.md body hash 更新至 `f20bdddc...`；changelog 追加 2026-07-28 第3轮捕获条目（非冻结态，因结构性更新已打破连续 hash-only） |
| 归档 | 01_inbox/articles/2026-07-28_Hermes_Agent.md → archive/articles/2026-07-28/2026-07-28_Hermes_Agent_v3.md ✅ |
| 去重检查 | 02-笔记/ 无新精确重复（实体 56 + 概念 40 + 方法 50 = 146）；无 stub 草稿；无学习要点垃圾文件；无 read_file 污染；无陈旧备份 |
| 地图检查 | 07-地图/ AI技术地图 + 办公自动化地图 — 均为 archived 状态，无需更新（routine re-capture，仅 llms-full hash 增量，无新实体/概念） |

最终状态：
- 01_inbox/articles: 0（已全部归档）✅
- 01-收件箱/所有子目录: 空 ✅（仅 _hash_tracker.md 跟踪文件）
- 02-笔记 合计 146 个文件（实体 56 + 概念 40 + 方法 50）
- 01_inbox/archive/articles/2026-07-28/: 3 个文件（07:00 + 13:00 v2 + 20:00 v3）
- 07-地图/ 3 个文件无变更（均已 archived）
- .last-compile 已刷新

### 2026-07-28 13:00 后台维护

| 操作 | 详情 |
|:----|:------|
| 编译 | 01_inbox/articles/ 1 个新文件 (Hermes Agent 2026-07-28 第2轮 13:00) — 字节级不同（md5 不同），llms-full.txt hash 从 `52d2365a...` 变更为 `25649c0e...`（当日第2次部署，无结构性变化），llms.txt `96828202...` 保持稳定 |
| 实体补充 | 实体/Hermes_Agent.md body hash 更新至 `25649c0e...`；changelog 保持冻结，hash 变更记录至 01-收件箱/自动学习/_hash_tracker.md |
| 归档 | 01_inbox/articles/2026-07-28_Hermes_Agent.md → archive/articles/2026-07-28/2026-07-28_Hermes_Agent_v2.md ✅ |
| 去重检查 | 02-笔记/ 无新精确重复（实体 56 + 概念 40 + 方法 50 = 146）；无 stub 草稿；无学习要点垃圾文件；无 read_file 污染；无陈旧备份 |
| 地图检查 | 07-地图/ AI技术地图 + 办公自动化地图 — 均为 archived 状态，无需更新（routine re-capture，仅 llms-full hash 增量，无新实体/概念） |

最终状态：
- 01_inbox/articles: 0（已全部归档）✅
- 01-收件箱/所有子目录: 空 ✅（仅 _hash_tracker.md 跟踪文件）
- 02-笔记 合计 146 个文件（实体 56 + 概念 40 + 方法 50）
- 01_inbox/archive/articles/2026-07-28/: 2 个文件（07:03 + 13:00 v2）
- 07-地图/ 3 个文件无变更（均已 archived）
- .last-compile 已刷新

### 2026-07-28 07:00 后台维护

| 操作 | 详情 |
|:----|:------|
| 编译 | 01_inbox/articles/ 1 个新文件 (Hermes Agent 2026-07-28) — **llms.txt hash 19 天稳定后首次变更**：`96828202...` → `8c526336...`，llms-full.txt: `52d2365a...` → `678d61cf...`，新增 20+ 文档页面（Curator/Kanban/Persistent Goals/Hooks/Batch Processing/Browser/Vision/ImageGen/TTS/ACP/API Server/Provider Routing/Memory Providers/Context References/Built-in Plugins/Profile Commands/Tools Reference/Toolsets Reference/MCP Config Reference/Model Catalog/Skills Catalogs 等），结构性更新 |
| 实体补充 | 实体/Hermes_Agent.md: 关键功能列表新增 10 项功能（Curator/API Server/ACP/Provider Routing/Memory Providers/Context References/Built-in Plugins/Kanban/Persistent Goals/Hooks），快速链接表扩展 10 行，changlog 追加 2026-07-28 结构性更新记录，updated 更新至 2026-07-28 |
| 归档 | 01_inbox/articles/2026-07-28_Hermes_Agent.md → archive/articles/2026-07-28/ ✅ |
| 去重检查 | 02-笔记/ 无新精确重复（实体 56 + 概念 40 + 方法 50 = 146）；无 stub 草稿；无学习要点垃圾文件；无 read_file 污染；无陈旧备份 |
| 地图检查 | 07-地图/ AI技术地图 + 办公自动化地图 — 均为 archived 状态，无需更新（entity 更新，无新实体/概念文件） |
| 地图统计 | 07_moc/知识地图 maintenance 记录已追加 |

最终状态：
- 01_inbox/articles: 0（已全部归档）✅
- 01-收件箱/所有子目录: 空 ✅（仅 _hash_tracker.md 跟踪文件）
- 02-笔记 合计 146 个文件（实体 56 + 概念 40 + 方法 50）
- 01_inbox/archive/articles/2026-07-28/: 1 个文件
- 07-地图/ 3 个文件无变更（均已 archived）
- .last-compile 已刷新

### 2026-07-27 20:03 后台维护

| 操作 | 详情 |
|:----|:------|
| 编译 | 01_inbox/articles/ 1 个新文件 (Hermes Agent 2026-07-27) — llms-full.txt hash 从 `b8408b4b...` 变更为 `52d2365a...`（当日部署，无结构性变化），llms.txt `96828202...` 保持稳定（第 19 天），页面无结构性变化 |
| 实体补充 | 实体/Hermes_Agent.md body hash 更新至 `52d2365a...`，updated 更新至 2026-07-27；changelog 保持冻结，hash 变更记录至 01-收件箱/自动学习/_hash_tracker.md |
| 归档 | 01_inbox/articles/2026-07-26_Hermes_Agent.md 为重复（与 archive v2 同 md5），已删除；01_inbox/articles/2026-07-27_Hermes_Agent.md → archive/articles/2026-07-27/ ✅ |
| 去重检查 | 02-笔记/ 无新精确重复（实体 56 + 概念 40 + 方法 50 = 146）；无 stub 草稿；无学习要点垃圾文件；无 read_file 污染；无陈旧备份 |
| 地图检查 | 07-地图/ AI技术地图 + 办公自动化地图 — 均为 archived 状态，无需更新（routine re-capture，仅 llms-full hash 增量，无新实体/概念） |

最终状态：
- 01_inbox/articles: 0（已全部归档）✅
- 01-收件箱/所有子目录: 空 ✅（仅 _hash_tracker.md 跟踪文件）
- 02-笔记 合计 146 个文件（实体 56 + 概念 40 + 方法 50）
- 01_inbox/archive/articles/2026-07-27/: 1 个文件
- 07-地图/ 3 个文件无变更（均已 archived）
- .last-compile 已刷新

### 2026-07-25 07:00 后台维护

| 操作 | 详情 |
|:----|:------|
| 编译 | 01_inbox/articles/ 1 个新文件 (Hermes Agent 2026-07-25) — llms-full.txt hash 从 `32445adb...` 变更为 `7e76a20c...`（当日部署，无结构性变化），llms.txt `96828202...` 保持稳定（第 17 天），页面无结构性变化 |
| 实体补充 | 实体/Hermes_Agent.md updated 更新至 2026-07-25；hash 变更记录至 01-收件箱/自动学习/_hash_tracker.md |
| 归档 | 01_inbox/articles/2026-07-25_Hermes_Agent.md → archive/articles/2026-07-25/ ✅ |
| 去重检查 | 02-笔记/ 无新精确重复（实体 56 + 概念 40 + 方法 50 + 架构 1 = 147）；无 stub 草稿 |
| 地图检查 | 07-地图/ AI技术地图 + 办公自动化地图 — 已有覆盖，无需更新（routine re-capture，仅 llms-full hash 增量，无新实体/概念） |

最终状态：
- 01_inbox/articles: 0（已全部归档）✅
- 01_inbox/已处理: 0 ✅
- 01-收件箱/所有子目录: 空 ✅
- 02-笔记 合计 147 个文件（实体 56 + 概念 40 + 方法 50 + 架构 1）
- 01_inbox/archive/articles/2026-07-25/: 1 个文件
- 07-地图/ 3 个文件无变更
- .last-compile 已刷新

### 2026-07-23 07:00 后台维护

| 操作 | 详情 |
|:----|:------|
| 编译 | 01_inbox/articles/ 1 个新文件 (Hermes Agent 2026-07-23) — llms-full.txt hash 从 `9780f652...` 变更为 `1c6beb4a...`（当日部署，无结构性变化），llms.txt `96828202...` 保持稳定（第 15 天），页面无结构性变化 |
| 实体补充 | 实体/Hermes_Agent.md updated 更新至 2026-07-23；changelog 已冻结（10+ 连续 hash-only 条目），hash 变更重定向至 01-收件箱/自动学习/_hash_tracker.md |
| 归档 | 01_inbox/articles/2026-07-23_Hermes_Agent.md → archive/articles/2026-07-23/ ✅ |
| 去重检查 | 02-笔记/ 无新精确重复（实体 56 + 概念 40 + 方法 50 + 架构 1 = 147）；跨目录标题重复检查通过；13 个小文件(<1KB)均为合法笔记（结构化定义+wikilinks），无 stub 草稿 |
| 地图检查 | 07-地图/ AI技术地图 + 办公自动化地图 — 已有覆盖，无需更新（routine re-capture，仅 llms-full hash 增量，无新实体/概念） |
| 地图统计 | 07_moc/知识地图 stats 已同步：实体 62→56, 概念 40→40, 方法 53→50 |

最终状态：
- 01_inbox/articles: 0（已全部归档）✅
- 01_inbox/已处理: 0 ✅
- 01-收件箱/所有子目录: 空 ✅
- 02-笔记 合计 147 个文件（实体 56 + 概念 40 + 方法 50 + 架构 1）
- 01_inbox/archive/articles/2026-07-23/: 1 个文件
- 07-地图/ 3 个文件无变更
- 07_moc/知识地图 stats 已更新
- .last-compile 已刷新

### 2026-07-20 14:00 后台维护

| 操作 | 详情 |
|:----|:------|
| 编译 | 01_inbox/articles/ 1 个新文件 (Hermes Agent 2026-07-20 第2轮) — llms-full.txt hash 从 `6252dac2...` 变更为 `3c60cae2...`（当日第2次部署，第12天），llms.txt `96828202...` 保持稳定（第 12 天），页面无结构性变化 |
| 实体补充 | 实体/Hermes_Agent.md: llms-full hash 同步至 `3c60cae2...`，资源表 hash 更新，追加 changelog |
| 归档 | 01_inbox/articles/2026-07-20_Hermes_Agent.md → archive/articles/2026-07-20/2026-07-20_Hermes_Agent_v2.md ✅ |
| 去重检查 | 02-笔记/ 无新精确重复（实体 53 + 概念 40 + 方法 50 + 架构 1 + 学习要点 0 = 144）；跨目录同名文件检查通过；无小文件(<1KB) stub |
| 地图检查 | 07-地图/ AI技术地图 + 办公自动化地图 — 已有覆盖，无需更新（routine re-capture，仅 llms-full hash 增量，无新实体/概念） |

最终状态：
- 01_inbox/articles: 0（已全部归档）✅
- 01_inbox/已处理: 0 ✅
- 01-收件箱/所有子目录: 空 ✅
- 02-笔记 合计 144 个文件（实体 53 + 概念 40 + 方法 50 + 架构 1 + 学习要点 0）
- 01_inbox/archive/articles/2026-07-20/: 2 个文件（v1 + v2）
- 07-地图/ 3 个文件无变更
- .last-compile 已刷新

### 2026-07-19 13:00 后台维护（第2轮）

| 操作 | 详情 |
|:----|:------|
| 编译 | 01_inbox/articles/ 1 个新文件 (Hermes Agent 2026-07-19 第2轮) — llms-full.txt hash 从 `f0567943...` 变更为 `225ba2ea...`（当日首次部署，第 11 天首次变更），llms.txt `96828202...` 保持稳定（第 11 天），页面无结构性变化 |
| 实体补充 | 实体/Hermes_Agent.md: llms-full hash 同步至 `225ba2ea...`，资源表 hash 更新，追加 changelog |
| 归档 | 01_inbox/articles/2026-07-19_Hermes_Agent.md → archive/articles/2026-07-19/2026-07-19_Hermes_Agent_v2.md ✅ |
| 去重检查 | 02-笔记/ 无新精确重复（实体 58 + 概念 40 + 方法 53 + 架构 1 + 学习要点 0 = 152）；跨目录同名文件检查通过；所有小文件(<1KB)均为合法笔记（含结构化定义+wikilinks），非 stub 草稿 |
| 地图检查 | 07-地图/ AI技术地图 + 办公自动化地图 — 已有覆盖，无需更新（routine re-capture，无新实体/概念） |

最终状态：
- 01_inbox/articles: 0（已全部归档）✅
- 01_inbox/已处理: 0 ✅
- 01-收件箱/所有子目录: 空 ✅
- 02-笔记 合计 152 个文件（实体 58 + 概念 40 + 方法 53 + 架构 1 + 学习要点 0）
- 01_inbox/archive/articles/2026-07-19/: 2 个文件（v1 + v2）
- 07-地图/ 3 个文件无变更
- .last-compile 已刷新

### 2026-07-19 07:00 后台维护

| 操作 | 详情 |
|:----|:------|
| 编译 | 01_inbox/articles/ 1 个新文件 (Hermes Agent 2026-07-19) — 已存在完整实体页 实体/Hermes_Agent.md，llms-full.txt hash `f0567943...` 无变化（第 10 天连续稳定），llms.txt `96828202...` 第 10 天稳定，跳过新编译 |
| 实体补充 | 实体/Hermes_Agent.md — updated 更新至 2026-07-19，追加例行检查 changelog 记录 |
| 归档 | 01_inbox/articles/2026-07-19_Hermes_Agent.md → archive/articles/2026-07-19/ ✅ |
| 去重清理 | 删除 5 个零引用 draft 实体草稿 stub（内容已被主笔记全面覆盖）：github.md（385B，GitHub 仓库 stub）、hermes-xaapi.md（393B，中文文档 stub）、hermes-agent-cn.md（397B，中文FAQ stub）、Quick_start_guide.md（840B，已由 Quickstart-Guide.md 70KB 替代）、Data_Visualization_With_Python.md（813B，已由概念版覆盖）→ 移入 99-归档/2026-07-19/实体-重复草稿/ |
| 地图检查 | 07-地图/ AI技术地图 + 办公自动化地图 — 已有覆盖，无需更新（routine re-capture，无新实体/概念） |

最终状态：
- 01_inbox/articles: 0（已全部归档）✅
- 01_inbox/已处理: 0（已全部归档）✅
- 01-收件箱/所有子目录: 空 ✅
- 02-笔记 合计 153 个文件（实体 58 + 概念 40 + 方法 53 + 架构 1 + 学习要点 0）
- 01_inbox/archive/articles/2026-07-19/: 1 个文件
- 07-地图/ 2 个文件无变更
- .last-compile 已刷新

### 2026-07-18 20:09 后台维护

| 操作 | 详情 |
|:----|:------|
| 编译 | 01_inbox/articles/ 1 个新文件 (Hermes Agent 第2轮捕获) — llms-full.txt hash 从 `d76867fb...` 变更为 `f0567943...`（当日第2次部署，无结构性变化），llms.txt 保持稳定 `96828202...`（第 9 天） |
| 实体补充 | 实体/Hermes_Agent.md：同步 llms-full hash 至 `f0567943...`（资源表 + changelog），追加第2轮捕获记录 |
| 归档 | 01_inbox/articles/2026-07-18_Hermes_Agent.md → archive/articles/2026-07-18/2026-07-18_Hermes_Agent_v2.md ✅ |
| 归档 | 01_inbox/已处理/2026-07-18_Hermes_Agent.md → archive/articles/2026-07-18/2026-07-18_Hermes_Agent_compiled_v2.md ✅ |
| 去重清理 | 方法/Python-docx 快速开始.md (1.8KB, needs-review) 与 实体/Quickstart.md (14KB, active) 来源相同，移入 99-归档/2026-07-18/ |
| 地图修复 | 办公自动化地图 `[[Python-docx 快速开始]]` → `[[Quickstart]]`（修复因去重产生的破损 wikilink） |
| 实体补充 | 实体/Quickstart.md：添加 3 个相关链接（AI编辑WordSkill技术解析、办公自动化、Python-pptx 快速开始）并更新日期 |
| 地图统计 | 07_moc/知识地图 stats 同步：实体 69→62, 概念 39→40, 方法 54→53 |

最终状态：
- 01_inbox/articles: 0（已全部归档）✅
- 01_inbox/已处理: 0（已全部归档）✅
- 01-收件箱/所有子目录: 空 ✅
- 02-笔记 合计 155 个文件（实体 62 + 概念 40 + 方法 53）
- 01_inbox/archive/articles/2026-07-18/: 3 个文件（+ v2 + compiled_v2）
- 07-地图/ 2 个文件 + 07_moc/知识地图 1 个
- .last-compile 已刷新

### 2026-07-18 13:02 后台维护

| 操作 | 详情 |
|:----|:------|
| 编译 | 01_inbox/articles/ 1 个新文件 (Hermes Agent 2026-07-18) — 已存在完整实体页 实体/Hermes_Agent.md，页面已更新至 2026-07-18，跳过重新编译 |
| 归档 | 01_inbox/articles/2026-07-18_Hermes_Agent.md → 01_inbox/已处理/ ✅ |
| 去重清理 | 删除 6 个 Hermes 实体页草稿重复（零引用，内容已被 实体/Hermes_Agent.md 全面覆盖）：Hermes_Agent_安装指南与平台支持、官方文档索引、官网、站点学习报告、中文社区 FAQ、GitHub 仓库 → 移入 99-归档/2026-07-18/实体-重复草稿/ |
| 抓取故障 | ⚠️ daily-capture.sh 所有 12 个站点抓取失败 — `/home/sqby776/office-venv/bin/python3` 路径不存在。需要重建 office-venv 或修复脚本中的 python3 路径为可用环境 |
| 地图检查 | 07-地图/ AI技术地图 + 办公自动化地图 — 已有覆盖，无需更新（routine re-capture，无新实体/概念） |

最终状态：
- 01_inbox/articles: 0（已全部归档）✅
- 01-收件箱/所有子目录: 空 ✅
- 01_inbox/已处理: 1 文件（2026-07-18_Hermes_Agent.md）
- 02-笔记 合计 158 个文件（实体 63 + 概念 40 + 方法 54 + 架构 1）
- 07-地图/ 3 个文件无变更
- .last-compile 已刷新

### 2026-07-18 07:07:29 后台维护

| 操作 | 详情 |
|:----|:------|
| 抓取 | 2 个 Hermes Agent 日捕获（07-17 + 07-18）— 均来自 hermes-agent.nousresearch.com/docs，llms-full.txt hash 两次例行部署变更（07-17: 8e47b9bb..., 07-18: d76867fb...），llms.txt 保持稳定 `96828202...`（连续第 9 天），页面无结构性变化 |
| 概念补充 | 实体/Hermes_Agent.md 追加 07-18 hash 变更记录，同步 llms-full hash（`34a78544...` → `d76867fb...`）；updated 字段更新至 07-18 |
| 归档 | 01_inbox/articles/2026-07-17_Hermes_Agent.md → archive/articles/2026-07-17/ ✅ |
| 归档 | 01_inbox/articles/2026-07-18_Hermes_Agent.md → archive/articles/2026-07-18/ ✅ |
| 去重检查 | 实体 69 + 概念 40 + 方法 54 + 架构 1 = 164 笔记文件；2 组跨目录标题重复属已知类型：Quick_start_guide 自动重建 stub（已跳过）、python-docx 快速开始（实体 vs 方法，不同内容，保留双方） |
| 学习要点 | 02-笔记/学习要点/ 仍为空（上轮已批量清理） |
| 地图更新 | 07_moc/知识地图 stats 已同步（实体 59→69，方法 48→54）；无新实体/概念添加，无需结构性更新 |
| read_file 污染 | 全库检查：无污染文件 ✅ |
| 过期备份 | 99-归档/ 无过期备份文件 |

最终状态：
- 01-收件箱/所有子目录: 空 ✅
- 01_inbox/articles: 0 待处理 ✅
- 01-收件箱/archive/自动捕获: 11 个日期目录（50 文件）
- 01_inbox/archive/articles: 25 个日期目录（98 文件，新增 07-17 + 07-18）
- 02-笔记 合计 164 个文件（实体 69 + 概念 40 + 方法 54 + 架构 1）
- 07-地图/ 3 个文件 + 07_moc/知识地图 1 个
- .last-compile 已刷新

### 2026-07-17 13:05:42 后台维护

| 操作 | 详情 |
|:----|:------|
| 抓取 | 预报告告 新抓取:1 待编译:1，但所有收件箱路径均为空 — 假阳性（上一轮已处理完毕） |
| 归档 | 无文件需归档 — 所有收件箱子目录已空 |
| 去重检查 | 实体 69 + 概念 40 + 方法 54 = 163 笔记文件；2 组跨目录标题重复属已知类型：Quick_start_guide 自动重建 stub（已跳过）、python-docx 快速开始（实体 vs 方法，不同内容，保留双方） |
| 学习要点 | 02-笔记/学习要点/ 仍为空（上轮已批量清理） |
| 地图更新 | 无新实体/概念添加，routine 无需更新地图 |
| read_file 污染 | 全库检查：无污染文件 ✅ |
| 过期备份 | 99-归档/ 无 .bak 过期备份文件 |

最终状态：
- 01-收件箱/所有子目录: 空 ✅
- 01_inbox/articles: 0 待处理 ✅
- 01-收件箱/archive/自动捕获: 11 个日期目录（50 文件）
- 01_inbox/archive/articles: 23 个日期目录（96 文件）
- 01-收件箱/archive/自动学习: 2 个日期目录（12 文件）
- 02-笔记 合计 163 个文件（实体 69 + 概念 40 + 方法 54）
- 07-地图/ 3 个文件（AI技术地图 2420B, 办公自动化地图 2435B, 结晶摘要 3204B）
- .last-compile 已刷新

### 2026-07-14 07:09:06 后台维护

| 操作 | 详情 |
|:----|:------|
| 抓取 | 9 标准站 + 1 Hermes Agent 日捕获 — 9 标准文件与昨日尺寸完全一致（无内容变化） |
| 概念补充 | Hermes-Agent.md 追加 07-14 hash 变更：llms.txt 稳定（连续第10天 `96828202...`），llms-full.txt 从 `0ec259c6...` → `80577b0f...`；资源表 hash 已同步 |
| 归档 | 01-收件箱/自动捕获/ 9 文件 → archive/自动捕获/2026-07-14/ ✅ |
| 归档 | 01_inbox/articles/ 10 文件 → archive/articles/2026-07-14/ ✅ |
| 去重检查 | 02-笔记/ 无新精确重复；3 组跨目录标题重复属已知分工（Hermes Agent 实体/概念、Data Visualization 实体/概念、python-docx 实体/方法），无需操作 |
| 学习要点 | 02-笔记/学习要点/ 为空（上次已批量清理） |
| 地图更新 | 无新实体/概念添加，routine re-capture 无需更新地图 |

最终状态：
- 01-收件箱/自动捕获: 空 ✅
- 01_inbox/articles: 空 ✅
- 01-收件箱/自动学习: 空 ✅
- 01-收件箱/archive/自动捕获: 9 个日期目录（93 文件，新增 2026-07-14）
- 01_inbox/archive/articles: 22 个日期目录（115 文件，新增 2026-07-14）
- 02-笔记/概念/Hermes-Agent.md: 已追加 07-14 hash 记录，资源表已同步
- 02-笔记 合计 154 个文件（实体 66 + 概念 39 + 方法 48 + 架构 1）
- 07-地图/ 无结构性变更
- .last-compile 已刷新

### 2026-07-14 13:12 后台维护（第2轮）

| 操作 | 详情 |
|:----|:------|
| 抓取 | 1 文件捕获（Hermes Agent 官网第2轮）— 与07:09归档文件完全一致（hash 80577b0f... 相同），无内容变化 |
| 概念补充 | 无需补充 — hash 07:09 已追踪，llms.txt 稳定第10天 |
| 归档 | 01_inbox/articles/ 1 文件 → archive/articles/2026-07-14/ 作为 _v2（去重归档）✅ |
| 去重检查 | 02-笔记/ 无新精确重复；跨目录标题重复与07:09一致（已知分工），无需操作 |
| 地图更新 | 无新实体/概念添加，routine re-capture 无需更新 |

最终状态：
- 01-收件箱/所有子目录: 空 ✅
- 01_inbox/articles: 0 待处理 ✅
- 01_inbox/archive/articles: 21 日期目录（116 文件，新增 2026-07-14 v2）
- 02-笔记 合计 154 个文件（实体 66 + 概念 39 + 方法 48 + 架构 1）
- 07-地图/ 无结构性变更
- .last-compile 已刷新

### 2026-07-13 20:13:28 后台维护

| 操作 | 详情 |
|:----|:------|
| 抓取 | 1 站第2轮捕获 (Hermes Agent) — llms-full.txt hash 从 `ace192bd...` → `0ec259c6...`，页面无结构性变化 |
| 概念补充 | Hermes-Agent.md 追加 07-13 第2轮 hash 变更记录：llms.txt 稳定（连续第9天 `96828202...`），llms-full.txt 更新；资源表 hash 已同步 |
| 学习存档 | 01-收件箱/自动学习/ 6 个 Hermes Agent 学习笔记 → archive/自动学习/2026-07-13/（含 5 学习笔记 + 1 学习报告） |
| 归档 | 01_inbox/articles/ 1 个 Hermes Agent 第2轮文件 → archive/articles/2026-07-13/_v2（hash 差异仅 llms-full.txt 引用） |
| 去重检查 | 02-笔记/ 无新精确重复（实体 60 + 概念 39 + 方法 48 + 架构 1 = 148）；学习要点为空；99-归档/ 无过期备份 |
| 地图更新 | 07_moc/知识地图 stats 已同步：实体 58→59 |

最终状态：
- 01-收件箱/所有子目录: 空 ✅
- 01_inbox/articles: 0 个待处理文件 ✅
- 01-收件箱/archive/自动学习: 新目录 2026-07-13（6 文件）
- 01_inbox/archive/articles: 20 个日期目录（105 文件，新增 07-13 v2）
- 01-收件箱/archive/自动捕获: 8 个日期目录（84 文件，新增 07-13 第二批）
- 02-笔记/概念/Hermes-Agent.md: 已追加 07-13 第2轮 hash 记录，资源表已同步
- 02-笔记 合计 148 个文件（实体 60 + 概念 39 + 方法 48 + 架构 1）
- 07-地图/ 两份地图无结构性变更（routine re-capture，无新实体/概念）
- .last-compile 已刷新

### 2026-07-13 13:00 后台维护

| 操作 | 详情 |
|:----|:------|
| 抓取 | 1 站捕获 (Hermes Agent) — 已知来源日重复，llms-full.txt hash 从 `1602b963...` → `ace192bd...`，页面无结构性变化 |
| 概念补充 | Hermes-Agent.md 追加 07-13 hash 变更记录：llms.txt 稳定（连续第8天 `96828202...`），llms-full.txt 更新；资源表 hash 已同步 |
| 归档 | 99-归档/2026-07-13/ 已创建（含 9 标准捕获 + 1 Hermes Agent） |
| 归档 | 01-收件箱/archive/自动捕获/2026-07-13/ 已创建（9 标准捕获） |
| 归档 | 01_inbox/archive/articles/2026-07-13/ 已创建（1 Hermes Agent） |
| 去重检查 | 02-笔记/ 无精确重复（实体 60 + 概念 39 + 方法 48 + 架构 1 = 148）；学习要点已清空 |

最终状态：
- 01-收件箱/所有子目录: 空 ✅
- 01_inbox/articles: 0 个待处理文件 ✅
- 01_inbox/archive/articles: 20 个日期目录（104 文件，新增 07-13）
- 01-收件箱/archive/自动捕获: 8 个日期目录（75 文件，新增 07-13）
- 02-笔记/概念/Hermes-Agent.md: 已追加 07-13 hash 记录，资源表 hash 已同步
- 02-笔记 合计 148 个文件（实体 60 + 概念 39 + 方法 48 + 架构 1）
- 07-地图/ 两份地图无变更（routine re-capture，无新实体/概念）
- .last-compile 已刷新

### 2026-07-12 13:08 后台维护

| 操作 | 详情 |
|:----|:------|
| 抓取 | 1 站捕获 (Hermes Agent) — 已知来源日重复，llms-full.txt hash 从 `205a0c4a...` → `a69c8575...`，页面无结构性变化 |
| 编译 | 01_inbox/articles/ 1 个文件检查完毕 — 今日 archive 已存在同名文件，body 内容一致，删除 inbox 副本 |
| 概念补充 | Hermes-Agent.md 追加 07-12 hash 变更记录：llms.txt 稳定（连续第6天 `96828202...`），llms-full.txt 更新；资源表 hash 已同步 |
| 去重检查 | 02-笔记/ 无精确重复（实体 58 + 概念 39 + 方法 48 + 架构 1 = 146）；学习要点已清空 |

最终状态：
- 01-收件箱/所有子目录: 空 ✅
- 01_inbox/articles: 0 个待处理文件（已删除重复副本）✅
- 01_inbox/archive/articles: 19 个日期目录（103 文件，保留 07-12 已有归档）
- 02-笔记/概念/Hermes-Agent.md: 已追加 07-12 hash 记录，资源表 hash 已同步
- 02-笔记 合计 146 个文件（实体 58 + 概念 39 + 方法 48 + 架构 1）
- 07-地图/ 两份地图无变更（routine re-capture，无新实体/概念）
- .last-compile 已刷新

### 2026-07-12 07:00 后台维护

| 操作 | 详情 |
|:----|:------|
| 抓取 | 10 站捕获（9 常规 + 1 Hermes Agent）— 全为已知来源日重复 |
| 编译 | 10 个文件检查完毕，全部页面已存在，跳过新编译 |
| 归档 | 01-收件箱/自动捕获/ 10 个文件 → archive/自动捕获/2026-07-12/ |
| 归档 | 01_inbox/articles/ 10 个文件 → archive/articles/2026-07-12/ |
| 去重 | 移除 2 个旧版残留薄 stub：实体/Quick_start_guide.md（840B，已由 Quickstart-Guide.md 70KB 替代）、实体/Data_Visualization_With_Python.md（813B，已由概念版 14KB 替代） |
| 地图检查 | 07_moc/知识地图 stats 已同步（原 54→57 实体，51→48 方法），无需结构性更新 |

最终状态：
- 01-收件箱/所有子目录: 空 ✅
- 01_inbox/articles: 空 ✅
- 01_inbox/archive/articles: 19 个日期目录（102 文件，新增 07-12）
- 01-收件箱/archive/自动捕获: 7 个日期目录（66 文件，新增 07-12）
- 02-笔记 合计 145 个文件（实体 57 + 概念 39 + 方法 48 + 架构 1）
- 07_moc/知识地图 stats 已更新
- .last-compile 已刷新

### 2026-07-11 07:00 后台维护

| 操作 | 详情 |
|:----|:------|
| 抓取 | 9 站捕获（8 常规 + 1 Hermes Agent）— 全为已知来源日重复 |
| 编译 | 11 个文件检查完毕，全部页面已存在，跳过新编译 |
| 概念补充 | Hermes-Agent.md — llms-full.txt hash 从 `8b89e1d3...` → `205a0c4a...`，llms.txt 稳定（连续第5天 `96828202...`），页面无结构性变化；资源表 hash 同步更新 |
| 归档 | 01-收件箱/自动捕获/ 9 个文件 → archive/自动捕获/2026-07-11/ |
| 归档 | 01_inbox/articles/ 11 个文件（含 07-10 遗留 Hermes_Agent 副本 + 10 今日文件）→ archive/articles/2026-07-11/ |
| 去重检查 | 02-笔记/ 无精确重复（实体 60 + 概念 39 + 方法 48 + 架构 1 = 148）；学习要点 已清理完毕 0 个 |
| 地图检查 | 07-地图/ 两份地图 + 07_moc/知识地图 已有覆盖，无需更新（routine re-capture，无新实体/概念） |

最终状态：
- 01-收件箱/所有子目录: 空 ✅
- 01_inbox/articles: 空 ✅
- 01_inbox/archive/articles: 18 个日期目录（92 文件，新增 07-11）
- 01-收件箱/archive/自动捕获: 6 个日期目录（56 文件，新增 07-11）
- 02-笔记/概念/Hermes-Agent.md: 已追加 07-11 hash 记录，资源表 hash 已同步
- 02-笔记 合计 148 个文件（实体 60 + 概念 39 + 方法 48 + 架构 1）
- 07-地图/ 两份地图 + 07_moc/知识地图 无变更
- .last-compile 已刷新

### 2026-07-10 13:00 后台维护

| 操作 | 详情 |
|:----|:------|
| 抓取 | 9 站捕获（8 常规 + 1 Hermes Agent）— 全为已知来源日重复 |
| 编译 | 10 个文件检查完毕，全部页面已存在，跳过新编译 |
| 概念补充 | Hermes-Agent.md — 无新内容：llms.txt 稳定（连续第4天 `96828202...`），llms-full.txt 稳定（`8b89e1d3...` 与 07-09 相同），页面无结构性变化 |
| 归档 | 01-收件箱/自动捕获/ 9 个文件 → archive/自动捕获/2026-07-10/ |
| 归档 | 01_inbox/articles/ 1 个文件 (Hermes_Agent v2，与已归档的 07-10 版本仅 frontmatter 不同) → archive/articles/2026-07-10/2026-07-10_Hermes_Agent_v2.md |
| 去重检查 | 02-笔记/ 无精确重复（实体 60 + 概念 39 + 方法 48 + 架构 1 = 148）；学习要点 已清理完毕 0 个 |
| 地图检查 | 07-地图/ 两份地图 + 07_moc/知识地图 已有覆盖，无需更新（routine re-capture，无新实体/概念） |

最终状态：
- 01-收件箱/所有子目录: 空 ✅
- 01_inbox/articles: 空 ✅
- 01_inbox/archive/articles: 17 个日期目录（81 文件，新增 07-10 的第2副本）
- 01-收件箱/archive/自动捕获: 5 个日期目录（47 文件，新增 07-10）
- 02-笔记/概念/Hermes-Agent.md: 无新增 changelog — hash 与 07-09 完全一致
- 02-笔记 合计 148 个文件（实体 60 + 概念 39 + 方法 48 + 架构 1）
- 07-地图/ 两份地图 + 07_moc/知识地图 无变更
- .last-compile 已刷新

### 2026-07-09 07:08 后台维护

| 操作 | 详情 |
|:----|:------|
| 抓取 | 9 站捕获（9 例行 + 1 Hermes Agent）— 全为已知来源日重复，内容仅 llms-full.txt hash 级差异 |
| 编译 | 11 个文件检查完毕，全部页面已存在，跳过新编译 |
| 概念补充 | Hermes-Agent.md 追加 07-09 hash 变更记录 — llms.txt 稳定（连续第2天 `96828202...`），llms-full.txt 从 `06e8a7a3...` → `8b89e1d3...`，页面无结构性变化 |
| 实体增强 | 实体/Hermes_Agent.md 从 751B 薄编译增强至 4.5KB 完整文档内容（含安装、功能列表、快速链接、LLM入口） |
| 去重清理 | 删除 6 个垃圾编译文件（坏文件名副本，~3KB腾出） |
| 去重清理 | 删除 16 个无价值 学习要点 文件（随机关键词列表，~17KB腾出） |
| 去重清理 | 删除 2 个薄实体编译（Quick_start_guide.md + Data_Visualization_With_Python.md，概念/方法版已存在） |
| 归档 | 01-收件箱/自动捕获/ 9 个文件 → archive/自动捕获/2026-07-09/ |
| 归档 | 01_inbox/articles/ 11 个文件（含 07-08 遗留的 Hermes_Agent + 10 今日文件）→ archive/articles/2026-07-09/ |

最终状态：
- 01-收件箱/所有子目录: 空 ✅
- 01_inbox/articles: 空 ✅
- 01_inbox/archive/articles: 16 个日期目录（新增 07-09）
- 01-收件箱/archive/自动捕获: 4 个日期目录（10+10+9+9 = 38 文件）
- 02-笔记/概念/Hermes-Agent.md: 已追加 07-09 hash 记录，已增强 实体/Hermes_Agent.md
- 02-笔记 合计 146 个文件（实体 57 + 概念 39 + 方法 49 + 架构 1）
- 07-地图/ 两份地图 无变更（routine re-capture，无新实体/概念）
- .last-compile 已刷新

### 2026-07-07 07:07 后台维护

| 操作 | 详情 |
|:----|:------|
| 抓取 | 9 站捕获（10 例行 + 0 新）— 全为已知来源日重复，内容仅 llms-full.txt hash 级差异 |
| 编译 | 17 个文件检查完毕，全部页面已存在，跳过编译 |
| 概念补充 | Hermes-Agent.md 追加 07-07 hash 变更记录（llms-full：`3cc1f036...` → `85605f39...`）— 页面无结构性变化 |
| 归档 | 01-收件箱/自动捕获/ 10 个文件 → archive/自动捕获/2026-07-07/ |
| 归档 | 01-收件箱/自动学习/ 8 个文件 → archive/自动学习/2026-07-07/ |
| 归档 | 01_inbox/articles/ 11 个文件 → archive/articles/2026-07-07/ |
| 去重检查 | 02-笔记/ 无精确重复（实体 60 + 概念 39 + 方法 51 + 架构 1 = 151） |
| 地图检查 | 07-地图/ 两份地图 + 07_moc/知识地图 已有覆盖，无需更新（routine re-capture，无新实体/概念） |

最终状态：
- 01-收件箱/所有子目录: 空 ✅
- 01_inbox/articles: 空 ✅
- 01_inbox/archive/articles: 14 个日期目录
- 01-收件箱/archive/自动捕获: 2 个日期目录（10+10 = 20 文件）
- 02-笔记/概念/Hermes-Agent.md: 已追加 07-07 hash 记录
- 02-笔记 合计 151 个文件（实体 60 + 概念 39 + 方法 51 + 架构 1）
- 07-地图/ 两份地图 + 07_moc/知识地图 无变更
- .last-compile 已刷新


### 2026-07-08 07:07 后台维护

| 操作 | 详情 |
|:----|:------|
| 抓取 | 9 站捕获（8 常规 + 1 Hermes Agent）— 全为已知来源日重复 |
| 编译 | 11 个文件检查完毕，全部页面已存在，跳过新编译 |
| 概念补充 | Hermes-Agent.md 追加 07-08 hash 变更记录 — **双 hash 同时变更**：llms.txt 自 06-21 以来首次变化（`c03199c2...` → `96828202...`），llms-full.txt 从 `85605f39...` → `aabe720e...`，页面无结构性变化 |
| 归档 | 01-收件箱/自动捕获/ 9 个文件（pandas/csv/json/pathlib/matplotlib等标准文档）→ archive/自动捕获/2026-07-08/ |
| 归档 | 01_inbox/articles/ 11 个文件（含 07-07 遗留的 Hermes_Agent + 10 今日文件）→ archive/articles/2026-07-08/ |
| 去重检查 | 02-笔记/ 无精确重复（实体 66 + 概念 39 + 方法 49 = 154） |
| 地图检查 | 07-地图/ 两份地图 + 07_moc/知识地图 已有覆盖，无需更新（routine re-capture，无新实体/概念） |

最终状态：
- 01-收件箱/所有子目录: 空 ✅
- 01_inbox/articles: 空 ✅
- 01_inbox/archive/articles: 15 个日期目录（新增 07-08）
- 01-收件箱/archive/自动捕获: 3 个日期目录（10+10+9 = 29 文件）
- 02-笔记/概念/Hermes-Agent.md: 已追加 07-08 hash 记录
- 02-笔记 合计 154 个文件（实体 66 + 概念 39 + 方法 49）
- 07-地图/ 两份地图 + 07_moc/知识地图 无变更
- .last-compile 已刷新


### 2026-07-06 07:00 后台维护

| 操作 | 详情 |
|:----|:------|
| 抓取 | 11 站捕获（10 例行 + 1 遗留 07-05 Hermes_Agent 第2轮）— 全为已知来源日重复，内容仅 llms-full.txt hash 级差异 |
| 编译 | 概念笔记 Hermes-Agent.md 追加 07-05 第2轮 + 07-06 hash 变更记录（llms-full：`708a4f8d...` → `3cc1f036...`）— 页面无结构性变化 |
| 归档 | 01_inbox/articles/ 11 个文件 → archive/articles/2026-07-06/（含 07-05 遗留文件以 _v2 命名） |
| 归档 | 01-收件箱/自动捕获/ 11 个文件 → archive/自动捕获/2026-07-06/ |
| 去重 | 01_inbox/archive/articles/ 去重 7 个 -> 41 文件（Hermes_Agent 19→18 副本）；01-收件箱/archive/自动捕获/ 去重 36 个 -> 10 文件（精简 78%），清理 8 个空目录 |
| 去重检查 | 02-笔记/ 无精确重复；99-归档/ 无过期备份文件需清理 |
| 地图检查 | 07-地图/ 两份地图 + 07_moc/知识地图 已有覆盖，无需更新（routine re-capture，无新实体/概念） |

最终状态：
- 01-收件箱/所有子目录: 空 ✅
- 01_inbox/articles: 空 ✅
- 01_inbox/archive/articles: 41 个文件（13 个日期目录）
- 01-收件箱/archive/自动捕获: 10 个文件（精简 78%）
- 02-笔记/概念/Hermes-Agent.md: 已追加 07-05 第2轮 + 07-06 hash 记录
- 02-笔记 合计 145 个文件（实体 54 + 概念 39 + 方法 51 + 架构 1）
- 07-地图/ 两份地图 + 07_moc/知识地图 无变更
- 01_inbox/.last-compile 污染修复 ✅
- .last-compile 已刷新


### 2026-07-04 07:10 后台维护

| 操作 | 详情 |
|:----|:------|
| 抓取 | 11 站捕获（10 例行 + 1 遗留 Hermes_Agent）— 全为已知来源日重复，内容 metadata 级差异（footer 时间戳 / 版本号如 pandas 3.0.3→3.0.4） |
| 归档 | 01_inbox/articles/ 11 个文件 → archive/articles/2026-07-04/ |
| 归档裁剪 | 01-收件箱/archive/自动捕获/ 70→16 文件（去重 54），01_inbox/archive/articles/ 97→26 文件（去重 71）— 内容标准化 hash 后每组仅保留最新版本 |
| 去重检查 | 02-笔记/ 无精确重复文件（实体 54 + 概念 39 + 方法 51 + 架构 1 = 145 文件）；_学习要点 garbage 文件已清空 |
| 地图检查 | 07-地图/ 两份地图已有覆盖，无需更新（routine re-capture，无新实体/概念） |

最终状态：
- 01-收件箱/自动捕获: 10 个活跃文件（今日最新）
- 01-收件箱/archive/自动捕获: 16 个唯一内容存档（精简 77%）
- 01_inbox/articles: 空 ✅
- 01_inbox/archive/articles: 26 个唯一内容存档（精简 73%）
- 02-笔记 合计 145 个文件（实体 54 + 概念 39 + 方法 51 + 架构 1）
- 07-地图/ 两份地图无变更
- .last-compile 已刷新


### 2026-07-03 07:08 后台维护

| 操作 | 详情 |
|:----|:------|
| 抓取 | 12 站点 → 9 成功 / 3 失败（Obsidian help ×2、python-docx table 404）；新捕获全为已知来源日重复 |
| 编译 | 扫描 59 文件，0 待编（目标文件均已存在） |
| 归档 | 01-收件箱/自动捕获/ 10 个文件 → archive/自动捕获/2026-07-03/ |
| 归档 | 01_inbox/articles/ 11 个文件清理（含 07-02 遗留 Hermes_Agent） |
| 笔记补全 | 9 个薄弱笔记从原始捕获提取全量文档内容更新 — 平均从 781B → 28,908B（37x）：pandas 10分钟入门、csv/json/pathlib 模块文档、Matplotlib 快速开始、python-pptx/openpyxl/python-docx 教程 |
|| 地图检查 | 07-地图/ 两份地图已有覆盖，无需更新 |

### 2026-07-03 13:00 后台维护 (第二轮)

| 操作 | 详情 |
|:----|:------|
| 编译 | 01_inbox/articles/ 1 个新文件 (Hermes Agent 2026-07-03 第二轮) — 同一来源 (hermes-agent.nousresearch.com/docs)，llms-full.txt hash 从 `23221f7bfd767039d8a3e5a4215c8185` → `dc1c09bb4fb184345926ad82432edfb5`，页面内容无结构性变化 |
| 归档 | 01_inbox/articles/ 1 个文件 → archive/articles/2026-07-03/2026-07-03_Hermes_Agent.md |
| 概念补充 | Hermes-Agent.md 追加 07-03 第二轮 hash 变更记录 |
| 去重检查 | 02-笔记/ 无需要合并的重复：实体 54 + 概念 39 + 方法 51 + 架构 1 = 145 文件 (Quickstart.md/Tutorial.md 为 curated note+raw source 互补对) |
| 地图检查 | 07-地图/ 两份地图已有覆盖，无需更新 (routine hash 增量) |

最终状态：
- 01-收件箱/所有子目录: 空 ✅
- 01_inbox/articles: 空 ✅
- 02-笔记/概念/Hermes-Agent.md: 已追加 07-03 第二轮 hash 记录
- 02-笔记 合计 145 个文件 (实体 54 + 概念 39 + 方法 51 + 架构 1)
- 07-地图/ 两份地图无变更

### 2026-07-01 06:00 后台维护

| 操作 | 详情 |
|:----|:------|
| 归档 | 01-收件箱/自动捕获/ 10 个文件 → archive/自动捕获/2026-07-01/ — 均为已知日重复来源，内容与 06-30 完全一致
| 归档 | 01_inbox/articles/ 10 个文件 → archive/articles/2026-07-01/ — 与中文收件箱 10/10 md5 匹配 |
| 概念补充 | Hermes-Agent.md 追加 07-01 hash 变更记录: `2fb28cd0...`（从 `7d9ac679...`）|
| 去重检查 | 02-笔记/ 无精确重复（实体 54 + 概念 39 + 方法 51 + 架构 1）|
| 地图检查 | 07-地图/ 两份地图 — 已有覆盖，无需更新（routine re-capture，仅 llms-full hash 更新）|

最终状态：
- 01-收件箱/自动捕获: 0（已全部归档）
- 01_inbox/articles: 0（已全部归档）
- 02-笔记/概念/Hermes-Agent.md: 已追加 07-01 hash 记录
- 02-笔记 合计 145 个文件（实体 54 + 概念 39 + 方法 51 + 架构 1）
- 07-地图/ 两份地图无变更

### 2026-06-30 20:00 后台维护

| 操作 | 详情 |
|:----|:------|
| 编译 | 01_inbox/articles/ 1 个新文件 (Hermes Agent 2026-06-30 第3轮捕获) — 同一来源 (hermes-agent.nousresearch.com/docs)，llms-full.txt hash 从 `fb26490645...` 变更为 `01742c6c48...`，页面内容无结构性变化 |
| 概念笔记补充 | Hermes-Agent.md 追加第3轮 hash 变更记录 |
| 归档 | 01_inbox/articles/ 1 个文件 → archive/articles/2026-06-30/2026-06-30_Hermes_Agent_v3.md |
| 去重检查 | 与同日归档文件仅 llms-full hash 不同，页面内容一致 |
| 地图检查 | 07-地图/ 两份地图 — 已有覆盖，无需更新（routine re-capture） |

最终状态：
- 01_inbox/articles: 0（已全部归档）
- 01-收件箱: 所有子目录均为空
- 02-笔记/概念/Hermes-Agent.md: 已追加第3轮 hash 记录
- 07-地图/ 两份地图无变更


### 2026-06-30 07:00 后台维护

| 操作 | 详情 |
|:----|:------|
| 编译 | 01-收件箱/自动捕获/ 10 个文件 — 均为已知来源（Hermes Agent 文档 + Python 标准库 + pandas/RealPython）；Hermes Agent llms-full.txt hash 从 `1e45778b...` → `7d9ac679...`（第5天连续增量更新），首页主体无结构性变化 |
| 概念笔记补充 | Hermes-Agent.md 追加 2026-06-30 hash 变更记录，updated 字段更新至 2026-06-30 |
| 归档 | 01-收件箱/自动捕获/ 10 个文件 → archive/自动捕获/2026-06-30/ |
| 归档 | 01_inbox/articles/ 10 个文件 → archive/articles/2026-06-30/ |
| 去重检查 | 两目录文件完全一致（10/10 md5 匹配），均归入各自 archive；02-笔记/ 无精确重复 |
| 地图检查 | 07-地图/ 两份地图 — 已有覆盖，无需更新（routine re-capture，仅 llms-full hash 更新） |

最终状态：
- 01_inbox/articles: 0（已全部归档）
- 01-收件箱: 所有子目录均为空
- 02-笔记/概念/Hermes-Agent.md: 已追加 2026-06-30 hash 记录
- 02-笔记 合计 145 个文件（实体 54 + 概念 39 + 方法 51 + 架构 1）
- 07-地图/ 两份地图无变更

### 2026-06-29 13:22 后台维护

| 操作 | 详情 |
|:----|:------|
| 编译 | 01_inbox/articles/ 最新 Hermes Agent 捕获 (13:00, llms-full hash `1db8e1c3...`) — 同一来源 (hermes-agent.nousresearch.com/docs)，第2轮捕获较第1轮 (`84be2f38...`) hash 再次变更，页面内容无结构性变化 |
| 概念笔记补充 | Hermes-Agent.md 追加 2026-06-29 第1轮 + 第2轮 hash 变更记录，updated 字段更新至 2026-06-29 |
| 归档 | 01_inbox/articles/ 文件已由外部流程自动处理归档（收件箱已清空） |
| 归档目录合并 | 2026-06-27_v2/ → 2026-06-27/（Hermes_Agent_v2.md），删除空 _v2 目录 |
| 空目录清理 | 删除 01_inbox/archive/articles/ 中 6 个空目录（2026-06-18~21, 06-23, 06-24）+ 01-收件箱/archive/自动捕获/2026-06-24 |
| 去重检查 | 02-笔记/ 无精确重复；archive 同名文件 hash 不同（同日多轮捕获），均为有效记录 |
| 地图检查 | 07-地图/ 办公自动化地图 + AI技术地图 — 已有覆盖，无需更新（routine re-capture） |

最终状态：
- 01_inbox/articles: 0（已全部归档）
- 01-收件箱: 所有子目录均为空
- 02-笔记/概念/Hermes-Agent.md: 已追加 06-29 两轮 hash 记录
- 02-笔记 合计 155 个文件（实体 64 + 概念 39 + 方法 51 + 架构 1）
- 07-地图/ 两份地图无变更
- 知识库/ 遗留 14 个孤立文件待人工合并

### 2026-06-29 07:00 后台维护

| 操作 | 详情 |
|:----|:------|
| 编译 | auto-compile-enhanced.py 处理 01-收件箱/自动捕获/ 9 文件 — 重新生成学习要点并同步到 ChromaDB（learning-points 842 块不变） |
| 归档 | 01_inbox/articles/10 文件 → archive/articles/2026-06-29/ |
| 清理同步副本 | 01-收件箱/自动捕获/ 9 个重复文件已删除 |
| 去重 | 06-29 捕获内容与 06-28 归档 hash 不同（同页面、不同时间戳），但主题完全相同 — 无新学习要点 |
| 已有笔记检查 | 10 个主题的学习要点已全部存在，本次覆盖后内容一致无变化 |
| 地图检查 | 07-地图/ 办公自动化地图 + AI技术地图 — 已有覆盖，无需更新 |

最终状态：
- 01_inbox/articles: 0（已全部归档）
- 01-收件箱/自动捕获: 清空
- 02-笔记 合计 155 个文件（实体 64 + 概念 39 + 方法 51 + 架构 1）
- 07-地图/ 两份地图无变更

### 2026-06-24 06:00 后台维护

| 操作 | 详情 |
|:----|:------|
-
### 2026-06-24 06:00 后台维护

| 操作 | 详情 |
|:----|:------|
| 编译 Hermes Agent 06-24 捕获 | 01_inbox/articles/ 1 个新文件，llms-full.txt hash `cdb9d5f9...`（从 `9bb4c2e9...` 变更）→ 补充概念笔记 changelog |
| 归档 | 01_inbox/articles/2026-06-23_Hermes_Agent.md → 01_inbox/archive/articles/2026-06-23/ |
| 归档 | 01_inbox/articles/2026-06-24_Hermes_Agent.md → 01_inbox/archive/articles/2026-06-24/ |
| 概念补充 | Hermes-Agent.md 追加 06-24 hash 变更记录 |
| 去重 | 02-笔记/ 无新重复；01_inbox 06-23 和 06-24 互相同源且与已有笔记重复 |
| 地图状态 | 07-地图/ 两份地图均无需更新 — hash 增量变更，非新领域 |

最终状态：
- 01_inbox: 0 个待处理文件（已全部归档）
- 01-收件箱: 所有子目录均为空
- 02-笔记/概念/Hermes-Agent.md: 已追加 06-24 hash 记录
- 02-笔记 合计 154 个文件（实体 64 + 概念 39 + 方法 51）

### 2026-06-27 06:00 后台维护

### 2026-06-27 06:00 后台维护

| 操作 | 详情 |
|:----|:------|
| 编译 Hermes Agent 06-27 第2轮捕获 | 01_inbox/articles/ 1 个新文件 → 概念笔记追加 changelog：llms-full.txt hash `f23a0121...`（从 `34a90a10...` 变更）；发现结构性微调：新增 Platform Support 链接、底部 GitHub Discussions→Issues、新增 Desktop Download 链接 |
| 归档 | 01_inbox/articles/2026-06-27_Hermes_Agent.md → 01_inbox/archive/articles/2026-06-27_v2/ |
| 去重清理 | 02-笔记/ 无精确重复（实体 64 + 概念 39 + 方法 51 + 架构 1）；清理 99-归档/ 中 48 个过期 .old.md 备份文件（1.6 MB） |
| 地图状态 | 07-地图/ 两份地图均无需更新 — hash 增量变更，非新领域 |

最终状态：
- 01_inbox: 0 个待处理文件（已全部归档）
- 01-收件箱: 所有子目录均为空
- 02-笔记/概念/Hermes-Agent.md: 已追加 06-27 第2轮 hash 记录 + 结构性变化备注
- 02-笔记 合计 155 个文件（实体 64 + 概念 39 + 方法 51 + 架构 1）

### 2026-06-23 06:33 后台维护

| 操作 | 详情 |
|:----|:------|
| 编译 Hermes Agent 06-23 捕获 | 01_inbox/articles/ 1 个新文件，llms-full.txt hash `2c3fb33f...`（从 `78469c45...` 变更）→ 补充概念笔记 changelog |
| 归档 | 01_inbox/articles/2026-06-23_Hermes_Agent.md → 01_inbox/archive/articles/2026-06-23/ |
| 归档合并 | 01_inbox/archive/articles/2026-06-22_2/ 合并至 2026-06-22/（Hermes_Agent_v2.md），删除空目录 |
| 概念补充 | Hermes-Agent.md 追加 06-23 hash 变更记录 |
| 去重 | 02-笔记/ 无精确重复；清理 99-归档/ 中 28 个过期 .bak 备份文件（371 KB）|
| 地图状态 | 07-地图/ 两份地图均无需更新 — hash 增量变更，非新领域 |

最终状态：
- 01_inbox: 0 个待处理文件（已全部归档）
- 01-收件箱: 所有子目录均为空
- 02-笔记/概念/Hermes-Agent.md: 已追加 06-23 hash 记录
- 02-笔记 合计 157 个文件（实体 64 + 概念 39 + 方法 51 + 架构 1 + 07-地图 2）
### 2026-06-22 19:08 后台维护

| 操作 | 详情 |
|:----|:----|
| 编译 Hermes Agent 第2轮捕获 | 01_inbox/articles/ 1 个新文件，llms-full.txt hash `78469c45...`（从 `aa5cd62b...` 变更）→ 补充概念笔记 changelog |
| 归档已处理 | 01-收件箱/已处理/ 10 个文件 → 01-收件箱/archive/articles/2026-06-22/ |
| 归档原始文件 | 01_inbox/articles/ 9 个文件 → 01_inbox/archive/articles/2026-06-22/ |
| 归档新编译 | 01_inbox/articles/2026-06-22_Hermes_Agent.md → 01_inbox/archive/articles/2026-06-22_2/ |
| 概念补充 | Hermes-Agent.md 追加 06-22 hash 变更记录 |
| 去重检查 | 02-笔记/实体/ 中 _学习要点 10 个 + flat copies 52 个，无精确重复 |
| 地图状态 | 07-地图/ 两份地图均无需更新 — 内容仅为 hash 增量变更，非新领域 |

最终状态：
- 01_inbox: 0 个待处理文件（已全部归档）
- 01-收件箱: 所有子目录均为空
- 02-笔记/概念/Hermes-Agent.md: 已追加 06-22 hash 记录

### 2026-06-15 04:05 后台维护

| 操作 | 详情 |
|:----|:----|
| 抓取编译 | 01_inbox/articles/ 2 个文件 (Hermes Agent 2026-06-14 + 06-15) — 均为同一来源，内容已被现有笔记覆盖 |
| 归档收件箱 | 2 个文件 → 99-归档/2026-06-15/ |
| 去重 | 2 个收件箱文件互相重复，且与已有概念笔记 Hermes-Agent.md (source_url 相同) 重复，不保留副本 |
| 实体补充 | 无需补充 — Hermes_Agent.md 和 Hermes-Agent.md 已覆盖全部要点 |
### 2026-06-18 12:07 后台维护

| 操作 | 详情 |
|:----|:----|
| 抓取编译 | 01_inbox/articles/ 1 个文件 (Hermes Agent 2026-06-18 第2轮) — 同一来源 (hermes-agent.nousresearch.com/docs)，llms-full.txt hash 从 `1fd95a836e3a50458dd176331d7e8437` 变更为 `a7774fddbb545729650179b373c807d3`，页面内容无结构性变化 |
| 归档收件箱 | 1 个文件 → 01_inbox/archive/articles/2026-06-18_2/ |
| 概念补充 | Hermes-Agent.md 追加 2026-06-18 第2轮 llms-full.txt hash 更新记录 |
| 实体补充 | Hermes_Agent.md 时间戳对齐，无需内容变更 |
| 地图状态 | 无需更新 |

最终状态：
- 01_inbox: 0 个待处理文件
- 01-收件箱: 所有子目录均为空
- 02-笔记/概念/Hermes-Agent.md: 已追加 06-18 第2轮 hash 记录

### 2026-06-19 04:05 后台维护

| 操作 | 详情 |
|:----|:----|
| 抓取编译 | 01_inbox/articles/ 1 个文件 (Hermes Agent 2026-06-19) — 同一来源 (hermes-agent.nousresearch.com/docs)，llms-full.txt hash 从 `a7774fddbb545729650179b373c807d3` 变更为 `1972cd64364e964ea2d8bbc1d6e59bff`，页面内容无结构性变化 |
| 归档收件箱 | 1 个文件 → 01_inbox/archive/articles/2026-06-19/ |
| 概念补充 | Hermes-Agent.md 追加 2026-06-19 hash 更新记录 |
| 地图状态 | 无需更新 |

最终状态：
- 01_inbox: 0 个待处理文件
- 01-收件箱: 所有子目录均为空
- 02-笔记/概念/Hermes-Agent.md: 已追加 06-19 hash 记录

### 2026-06-15 04:05 后台维护

| 操作 | 详情 |
|:----|:----|
| 抓取编译 | 01_inbox/articles/ 1 个文件 (Hermes Agent) — 已编译为实体/已存在 |
| 归档收件箱 | 01_inbox/articles/ 1 个文件 + archive/duplicate_names/ 10 个文件 → 99-归档/ |
| 归档自动捕获 | archive/自动捕获/ 9 个文件已存在于 99-归档/，无重复移动 |
| 归档 .hermes 收件箱 | crawl4ai-50k-star-llm-friendly-crawler 1 个文件 → 99-归档/ |
| 实体去重 | 删除 5 个完全相同标题的重复学习要点碎片 |
| 实体补充 | Hermes_Agent.md 补充 2026-06-11 抓取新信息 (多平台网关/Voice/Serverless) |
| 地图状态 | 无需更新，Hermes Agent 已在 AI技术地图中覆盖 |

最终状态：
- 实体/ 112 个文件 (删除 5 个)
- 概念/ 38 个文件
- 方法/ 53 个文件
- 地图/ 2 个文件
- 归档/ 新增 12 个文件

| 收件箱状态 | 01_inbox/articles: 0, 自动捕获: 0, .hermes: 0 |

# 知识库变更日志


### 自动入库 (2026-05-26)

| 文件 | 标题 | 来源 |
|:----|:----|:----|

| `01_inbox/articles/2026-05-26_Example_Domain.md` | Example Domain | 自动抓取 |

| `01_inbox/articles/2026-05-26_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-05-26_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-05-26_python_docxhttpspython_docxreadthedocsioenlatestpython_docx_.md` | python-docx[¶](https://python-docx.readthedocs.io/en/latest/#python-docx "Permalink to this headline") | 自动抓取 |

| `01_inbox/articles/2026-05-26_openpyxl_A_Python_library_to_readwrite_Excel_2010_xlsxxlsm_f.md` | openpyxl - A Python library to read/write Excel 2010 xlsx/xlsm files[](https://openpyxl.readthedocs.io/en/latest/#openpyxl-a-python-library-to-read-write-excel-2010-xlsx-xlsm-files "Link to this heading") | 自动抓取 |

| `01_inbox/articles/2026-05-26_python_pptxhttpspython_pptxreadthedocsioenlatestpython_pptx_.md` | python-pptx[¶](https://python-pptx.readthedocs.io/en/latest/#python-pptx "Permalink to this headline") | 自动抓取 |

| `01_inbox/articles/2026-05-26_10_minutes_to_pandashttpspandaspydataorgdocsuser_guide10minh.md` | 10 minutes to pandas[#](https://pandas.pydata.org/docs/user_guide/10min.html#minutes-to-pandas "Link to this heading") | 自动抓取 |

| `01_inbox/articles/2026-05-26_Home.md` | Home | 自动抓取 |

| `01_inbox/articles/2026-05-26_csv_CSV_File_Reading_and_Writinghttpsdocspythonorg3librarycs.md` | `csv` — CSV File Reading and Writing[¶](https://docs.python.org/3/library/csv.html#module-csv "Link to this heading") | 自动抓取 |

| `01_inbox/articles/2026-05-26_json_JSON_encoder_and_decoderhttpsdocspythonorg3libraryjsonh.md` | `json` — JSON encoder and decoder[¶](https://docs.python.org/3/library/json.html#module-json "Link to this heading") | 自动抓取 |

| `01_inbox/articles/2026-05-26_未命名文章.md` | 未命名文章 | 自动抓取 |

| `01_inbox/articles/2026-05-26_未命名文章.md` | 未命名文章 | 自动抓取 |

| `01_inbox/articles/2026-05-26_Quickstarthttpspython_docxreadthedocsioenlatestuserquickstar.md` | Quickstart[¶](https://python-docx.readthedocs.io/en/latest/user/quickstart.html#quickstart "Permalink to this headline") | 自动抓取 |

| `01_inbox/articles/2026-05-26_quickstarthtml.md` | quickstart.html | 自动抓取 |

| `01_inbox/articles/2026-05-26_Home.md` | Home | 自动抓取 |

| `01_inbox/articles/2026-05-26_pathlib_Object_oriented_filesystem_pathshttpsdocspythonorg3l.md` | `pathlib` — Object-oriented filesystem paths[¶](https://docs.python.org/3/library/pathlib.html#module-pathlib "Link to this heading") | 自动抓取 |

| `01_inbox/articles/2026-05-26_Builtinplugins.md` | Builtin+plugins | 自动抓取 |

| `01_inbox/articles/2026-05-26_Quick_start_guidehttpsmatplotliborgstableusersexplainquick_s.md` | Quick start guide[#](https://matplotlib.org/stable/users/explain/quick_start.html#quick-start-guide "Link to this heading") | 自动抓取 |

| `01_inbox/articles/2026-05-26_Page_not_found.md` | Page not found | 自动抓取 |

| `01_inbox/articles/2026-05-26_Data_Visualization_With_Python.md` | Data Visualization With Python | 自动抓取 |

| `01_inbox/articles/2026-05-26_Quickstarthttpspython_docxreadthedocsioenlatestuserquickstar.md` | Quickstart[¶](https://python-docx.readthedocs.io/en/latest/user/quickstart.html#quickstart "Permalink to this headline") | 自动抓取 |

| `01_inbox/articles/2026-05-26_tablehtml.md` | table.html | 自动抓取 |

| `01_inbox/articles/2026-05-26_tutorialhtml.md` | tutorial.html | 自动抓取 |

| `01_inbox/articles/2026-05-26_worksheet_cellshtml.md` | worksheet_cells.html | 自动抓取 |

| `01_inbox/articles/2026-05-26_quickstarthtml.md` | quickstart.html | 自动抓取 |

| `01_inbox/articles/2026-05-26_shapeshtml.md` | shapes.html | 自动抓取 |

| `01_inbox/articles/2026-05-26_quickstarthtml.md` | quickstart.html | 自动抓取 |

| `01_inbox/articles/2026-05-26_tablehtml.md` | table.html | 自动抓取 |

| `01_inbox/articles/2026-05-26_tutorialhtml.md` | tutorial.html | 自动抓取 |

| `01_inbox/articles/2026-05-26_quickstarthtml.md` | quickstart.html | 自动抓取 |

| `01_inbox/articles/2026-05-26_10_minutes_to_pandashttpspandaspydataorgdocsuser_guide10minh.md` | 10 minutes to pandas[#](https://pandas.pydata.org/docs/user_guide/10min.html#minutes-to-pandas "Link to this heading") | 自动抓取 |

| `01_inbox/articles/2026-05-26_Quick_start_guidehttpsmatplotliborgstableusersexplainquick_s.md` | Quick start guide[#](https://matplotlib.org/stable/users/explain/quick_start.html#quick-start-guide "Link to this heading") | 自动抓取 |

| `01_inbox/articles/2026-05-26_csv_CSV_File_Reading_and_Writinghttpsdocspythonorg3librarycs.md` | `csv` — CSV File Reading and Writing[¶](https://docs.python.org/3/library/csv.html#module-csv "Link to this heading") | 自动抓取 |

| `01_inbox/articles/2026-05-26_json_JSON_encoder_and_decoderhttpsdocspythonorg3libraryjsonh.md` | `json` — JSON encoder and decoder[¶](https://docs.python.org/3/library/json.html#module-json "Link to this heading") | 自动抓取 |

| `01_inbox/articles/2026-05-26_pathlib_Object_oriented_filesystem_pathshttpsdocspythonorg3l.md` | `pathlib` — Object-oriented filesystem paths[¶](https://docs.python.org/3/library/pathlib.html#module-pathlib "Link to this heading") | 自动抓取 |

| `01_inbox/articles/2026-05-26_Home.md` | Home | 自动抓取 |

| `01_inbox/articles/2026-05-26_Data_Visualization_With_Python.md` | Data Visualization With Python | 自动抓取 |

| `01_inbox/articles/2026-05-26_quickstarthtml.md` | quickstart.html | 自动抓取 |

| `01_inbox/articles/2026-05-26_tablehtml.md` | table.html | 自动抓取 |

| `01_inbox/articles/2026-05-26_Tutorialhttpsopenpyxlreadthedocsioenlatesttutorialhtmltutori.md` | Tutorial[](https://openpyxl.readthedocs.io/en/latest/tutorial.html#tutorial "Link to this heading") | 自动抓取 |

| `01_inbox/articles/2026-05-26_quickstarthtml.md` | quickstart.html | 自动抓取 |

| `01_inbox/articles/2026-05-26_10_minutes_to_pandashttpspandaspydataorgdocsuser_guide10minh.md` | 10 minutes to pandas[#](https://pandas.pydata.org/docs/user_guide/10min.html#minutes-to-pandas "Link to this heading") | 自动抓取 |

| `01_inbox/articles/2026-05-26_Quick_start_guidehttpsmatplotliborgstableusersexplainquick_s.md` | Quick start guide[#](https://matplotlib.org/stable/users/explain/quick_start.html#quick-start-guide "Link to this heading") | 自动抓取 |

| `01_inbox/articles/2026-05-26_csv_CSV_File_Reading_and_Writinghttpsdocspythonorg3librarycs.md` | `csv` — CSV File Reading and Writing[¶](https://docs.python.org/3/library/csv.html#module-csv "Link to this heading") | 自动抓取 |

| `01_inbox/articles/2026-05-26_json_JSON_encoder_and_decoderhttpsdocspythonorg3libraryjsonh.md` | `json` — JSON encoder and decoder[¶](https://docs.python.org/3/library/json.html#module-json "Link to this heading") | 自动抓取 |

| `01_inbox/articles/2026-05-26_pathlib_Object_oriented_filesystem_pathshttpsdocspythonorg3l.md` | `pathlib` — Object-oriented filesystem paths[¶](https://docs.python.org/3/library/pathlib.html#module-pathlib "Link to this heading") | 自动抓取 |

| `01_inbox/articles/2026-05-26_Home.md` | Home | 自动抓取 |

| `01_inbox/articles/2026-05-26_Data_Visualization_With_Python.md` | Data Visualization With Python | 自动抓取 |

| `01_inbox/articles/2026-05-26_Quickstarthttpspython_docxreadthedocsioenlatestuserquickstar.md` | Quickstart[¶](https://python-docx.readthedocs.io/en/latest/user/quickstart.html#quickstart "Permalink to this headline") | 自动抓取 |

| `01_inbox/articles/2026-05-26_tablehtml.md` | table.html | 自动抓取 |

| `01_inbox/articles/2026-05-26_tutorialhtml.md` | tutorial.html | 自动抓取 |

| `01_inbox/articles/2026-05-26_quickstarthtml.md` | quickstart.html | 自动抓取 |

| `01_inbox/articles/2026-05-26_10_minutes_to_pandashttpspandaspydataorgdocsuser_guide10minh.md` | 10 minutes to pandas[#](https://pandas.pydata.org/docs/user_guide/10min.html#minutes-to-pandas "Link to this heading") | 自动抓取 |

| `01_inbox/articles/2026-05-26_Quick_start_guidehttpsmatplotliborgstableusersexplainquick_s.md` | Quick start guide[#](https://matplotlib.org/stable/users/explain/quick_start.html#quick-start-guide "Link to this heading") | 自动抓取 |

| `01_inbox/articles/2026-05-26_csv_CSV_File_Reading_and_Writinghttpsdocspythonorg3librarycs.md` | `csv` — CSV File Reading and Writing[¶](https://docs.python.org/3/library/csv.html#module-csv "Link to this heading") | 自动抓取 |

| `01_inbox/articles/2026-05-26_json_JSON_encoder_and_decoderhttpsdocspythonorg3libraryjsonh.md` | `json` — JSON encoder and decoder[¶](https://docs.python.org/3/library/json.html#module-json "Link to this heading") | 自动抓取 |

| `01_inbox/articles/2026-05-26_pathlib_Object_oriented_filesystem_pathshttpsdocspythonorg3l.md` | `pathlib` — Object-oriented filesystem paths[¶](https://docs.python.org/3/library/pathlib.html#module-pathlib "Link to this heading") | 自动抓取 |

| `01_inbox/articles/2026-05-26_Home.md` | Home | 自动抓取 |

| `01_inbox/articles/2026-05-26_Data_Visualization_With_Python.md` | Data Visualization With Python | 自动抓取 |

| `01_inbox/articles/2026-05-26_json_JSON_encoder_and_decoderhttpsdocspythonorg3libraryjsonh.md` | `json` — JSON encoder and decoder[¶](https://docs.python.org/3/library/json.html#module-json "Link to this heading") | 自动抓取 |

### 自动入库 (2026-05-27)

| 文件 | 标题 | 来源 |
|:----|:----|:----|

| `01_inbox/articles/2026-05-27_quickstarthtml.md` | quickstart.html | 自动抓取 |

| `01_inbox/articles/2026-05-27_tablehtml.md` | table.html | 自动抓取 |

| `01_inbox/articles/2026-05-27_tutorialhtml.md` | tutorial.html | 自动抓取 |

| `01_inbox/articles/2026-05-27_quickstarthtml.md` | quickstart.html | 自动抓取 |

| `01_inbox/articles/2026-05-27_10_minutes_to_pandashttpspandaspydataorgdocsuser_guide10minh.md` | 10 minutes to pandas[#](https://pandas.pydata.org/docs/user_guide/10min.html#minutes-to-pandas "Link to this heading") | 自动抓取 |

| `01_inbox/articles/2026-05-27_Quick_start_guidehttpsmatplotliborgstableusersexplainquick_s.md` | Quick start guide[#](https://matplotlib.org/stable/users/explain/quick_start.html#quick-start-guide "Link to this heading") | 自动抓取 |

| `01_inbox/articles/2026-05-27_csv_CSV_File_Reading_and_Writinghttpsdocspythonorg3librarycs.md` | `csv` — CSV File Reading and Writing[¶](https://docs.python.org/3/library/csv.html#module-csv "Link to this heading") | 自动抓取 |

| `01_inbox/articles/2026-05-27_json_JSON_encoder_and_decoderhttpsdocspythonorg3libraryjsonh.md` | `json` — JSON encoder and decoder[¶](https://docs.python.org/3/library/json.html#module-json "Link to this heading") | 自动抓取 |

| `01_inbox/articles/2026-05-27_pathlib_Object_oriented_filesystem_pathshttpsdocspythonorg3l.md` | `pathlib` — Object-oriented filesystem paths[¶](https://docs.python.org/3/library/pathlib.html#module-pathlib "Link to this heading") | 自动抓取 |

| `01_inbox/articles/2026-05-27_Home.md` | Home | 自动抓取 |

| `01_inbox/articles/2026-05-27_Data_Visualization_With_Python.md` | Data Visualization With Python | 自动抓取 |

| `01_inbox/articles/2026-05-27_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

### 自动入库 (2026-05-28)

| 文件 | 标题 | 来源 |
|:----|:----|:----|

| `01_inbox/articles/2026-05-28_quickstarthtml.md` | quickstart.html | 自动抓取 |

| `01_inbox/articles/2026-05-28_tablehtml.md` | table.html | 自动抓取 |

| `01_inbox/articles/2026-05-28_tutorialhtml.md` | tutorial.html | 自动抓取 |

| `01_inbox/articles/2026-05-28_quickstarthtml.md` | quickstart.html | 自动抓取 |

| `01_inbox/articles/2026-05-28_10_minutes_to_pandashttpspandaspydataorgdocsuser_guide10minh.md` | 10 minutes to pandas[#](https://pandas.pydata.org/docs/user_guide/10min.html#minutes-to-pandas "Link to this heading") | 自动抓取 |

| `01_inbox/articles/2026-05-28_Quick_start_guidehttpsmatplotliborgstableusersexplainquick_s.md` | Quick start guide[#](https://matplotlib.org/stable/users/explain/quick_start.html#quick-start-guide "Link to this heading") | 自动抓取 |

| `01_inbox/articles/2026-05-28_csv_CSV_File_Reading_and_Writinghttpsdocspythonorg3librarycs.md` | `csv` — CSV File Reading and Writing[¶](https://docs.python.org/3/library/csv.html#module-csv "Link to this heading") | 自动抓取 |

| `01_inbox/articles/2026-05-28_json_JSON_encoder_and_decoderhttpsdocspythonorg3libraryjsonh.md` | `json` — JSON encoder and decoder[¶](https://docs.python.org/3/library/json.html#module-json "Link to this heading") | 自动抓取 |

| `01_inbox/articles/2026-05-28_pathlib_Object_oriented_filesystem_pathshttpsdocspythonorg3l.md` | `pathlib` — Object-oriented filesystem paths[¶](https://docs.python.org/3/library/pathlib.html#module-pathlib "Link to this heading") | 自动抓取 |

| `01_inbox/articles/2026-05-28_Home.md` | Home | 自动抓取 |

| `01_inbox/articles/2026-05-28_Data_Visualization_With_Python.md` | Data Visualization With Python | 自动抓取 |

### 自动入库 (2026-05-29)

| 文件 | 标题 | 来源 |
|:----|:----|:----|

| `01_inbox/articles/2026-05-29_quickstarthtml.md` | quickstart.html | 自动抓取 |

| `01_inbox/articles/2026-05-29_tablehtml.md` | table.html | 自动抓取 |

| `01_inbox/articles/2026-05-29_tutorialhtml.md` | tutorial.html | 自动抓取 |

| `01_inbox/articles/2026-05-29_quickstarthtml.md` | quickstart.html | 自动抓取 |

| `01_inbox/articles/2026-05-29_10_minutes_to_pandashttpspandaspydataorgdocsuser_guide10minh.md` | 10 minutes to pandas[#](https://pandas.pydata.org/docs/user_guide/10min.html#minutes-to-pandas "Link to this heading") | 自动抓取 |

| `01_inbox/articles/2026-05-29_Quick_start_guidehttpsmatplotliborgstableusersexplainquick_s.md` | Quick start guide[#](https://matplotlib.org/stable/users/explain/quick_start.html#quick-start-guide "Link to this heading") | 自动抓取 |

| `01_inbox/articles/2026-05-29_csv_CSV_File_Reading_and_Writinghttpsdocspythonorg3librarycs.md` | `csv` — CSV File Reading and Writing[¶](https://docs.python.org/3/library/csv.html#module-csv "Link to this heading") | 自动抓取 |

| `01_inbox/articles/2026-05-29_json_JSON_encoder_and_decoderhttpsdocspythonorg3libraryjsonh.md` | `json` — JSON encoder and decoder[¶](https://docs.python.org/3/library/json.html#module-json "Link to this heading") | 自动抓取 |

| `01_inbox/articles/2026-05-29_pathlib_Object_oriented_filesystem_pathshttpsdocspythonorg3l.md` | `pathlib` — Object-oriented filesystem paths[¶](https://docs.python.org/3/library/pathlib.html#module-pathlib "Link to this heading") | 自动抓取 |

| `01_inbox/articles/2026-05-29_Home.md` | Home | 自动抓取 |

| `01_inbox/articles/2026-05-29_Data_Visualization_With_Python.md` | Data Visualization With Python | 自动抓取 |

| `01_inbox/articles/2026-05-29_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-05-29_Quickstarthttpspython_docxreadthedocsioenlatestuserquickstar.md` | Quickstart[¶](https://python-docx.readthedocs.io/en/latest/user/quickstart.html#quickstart "Permalink to this headline") | 自动抓取 |

| `01_inbox/articles/2026-05-29_tablehtml.md` | table.html | 自动抓取 |

| `01_inbox/articles/2026-05-29_Tutorialhttpsopenpyxlreadthedocsioenlatesttutorialhtmltutori.md` | Tutorial[](https://openpyxl.readthedocs.io/en/latest/tutorial.html#tutorial "Link to this heading") | 自动抓取 |

| `01_inbox/articles/2026-05-29_Getting_Startedhttpspython_pptxreadthedocsioenlatestuserquic.md` | Getting Started[¶](https://python-pptx.readthedocs.io/en/latest/user/quickstart.html#getting-started "Permalink to this headline") | 自动抓取 |

| `01_inbox/articles/2026-05-29_10_minutes_to_pandashttpspandaspydataorgdocsuser_guide10minh.md` | 10 minutes to pandas[#](https://pandas.pydata.org/docs/user_guide/10min.html#minutes-to-pandas "Link to this heading") | 自动抓取 |

| `01_inbox/articles/2026-05-29_Quick_start_guidehttpsmatplotliborgstableusersexplainquick_s.md` | Quick start guide[#](https://matplotlib.org/stable/users/explain/quick_start.html#quick-start-guide "Link to this heading") | 自动抓取 |

| `01_inbox/articles/2026-05-29_csv_CSV_File_Reading_and_Writinghttpsdocspythonorg3librarycs.md` | `csv` — CSV File Reading and Writing[¶](https://docs.python.org/3/library/csv.html#module-csv "Link to this heading") | 自动抓取 |

| `01_inbox/articles/2026-05-29_json_JSON_encoder_and_decoderhttpsdocspythonorg3libraryjsonh.md` | `json` — JSON encoder and decoder[¶](https://docs.python.org/3/library/json.html#module-json "Link to this heading") | 自动抓取 |

| `01_inbox/articles/2026-05-29_pathlib_Object_oriented_filesystem_pathshttpsdocspythonorg3l.md` | `pathlib` — Object-oriented filesystem paths[¶](https://docs.python.org/3/library/pathlib.html#module-pathlib "Link to this heading") | 自动抓取 |

| `01_inbox/articles/2026-05-29_Home.md` | Home | 自动抓取 |

| `01_inbox/articles/2026-05-29_Data_Visualization_With_Python.md` | Data Visualization With Python | 自动抓取 |

### 自动入库 (2026-05-30)

| 文件 | 标题 | 来源 |
|:----|:----|:----|

| `01_inbox/articles/2026-05-30_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

### 自动入库 (2026-05-31)

| 文件 | 标题 | 来源 |
|:----|:----|:----|

| `01_inbox/articles/2026-05-31_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-05-31_Quickstarthttpspython_docxreadthedocsioenlatestuserquickstar.md` | Quickstart[¶](https://python-docx.readthedocs.io/en/latest/user/quickstart.html#quickstart "Permalink to this headline") | 自动抓取 |

| `01_inbox/articles/2026-05-31_tablehtml.md` | table.html | 自动抓取 |

| `01_inbox/articles/2026-05-31_Tutorialhttpsopenpyxlreadthedocsioenlatesttutorialhtmltutori.md` | Tutorial[](https://openpyxl.readthedocs.io/en/latest/tutorial.html#tutorial "Link to this heading") | 自动抓取 |

| `01_inbox/articles/2026-05-31_Getting_Startedhttpspython_pptxreadthedocsioenlatestuserquic.md` | Getting Started[¶](https://python-pptx.readthedocs.io/en/latest/user/quickstart.html#getting-started "Permalink to this headline") | 自动抓取 |

| `01_inbox/articles/2026-05-31_10_minutes_to_pandashttpspandaspydataorgdocsuser_guide10minh.md` | 10 minutes to pandas[#](https://pandas.pydata.org/docs/user_guide/10min.html#minutes-to-pandas "Link to this heading") | 自动抓取 |

| `01_inbox/articles/2026-05-31_Quick_start_guidehttpsmatplotliborgstableusersexplainquick_s.md` | Quick start guide[#](https://matplotlib.org/stable/users/explain/quick_start.html#quick-start-guide "Link to this heading") | 自动抓取 |

| `01_inbox/articles/2026-05-31_csv_CSV_File_Reading_and_Writinghttpsdocspythonorg3librarycs.md` | `csv` — CSV File Reading and Writing[¶](https://docs.python.org/3/library/csv.html#module-csv "Link to this heading") | 自动抓取 |

| `01_inbox/articles/2026-05-31_json_JSON_encoder_and_decoderhttpsdocspythonorg3libraryjsonh.md` | `json` — JSON encoder and decoder[¶](https://docs.python.org/3/library/json.html#module-json "Link to this heading") | 自动抓取 |

| `01_inbox/articles/2026-05-31_pathlib_Object_oriented_filesystem_pathshttpsdocspythonorg3l.md` | `pathlib` — Object-oriented filesystem paths[¶](https://docs.python.org/3/library/pathlib.html#module-pathlib "Link to this heading") | 自动抓取 |

| `01_inbox/articles/2026-05-31_Home.md` | Home | 自动抓取 |

| `01_inbox/articles/2026-05-31_Data_Visualization_With_Python.md` | Data Visualization With Python | 自动抓取 |

| `01_inbox/articles/2026-05-31_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-05-31_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-05-31_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

### 自动入库 (2026-06-02)

| 文件 | 标题 | 来源 |
|:----|:----|:----|

| `01_inbox/articles/2026-06-02_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-06-02_Example_Domain.md` | Example Domain | 自动抓取 |

### 自动入库 (2026-06-03)

| 文件 | 标题 | 来源 |
|:----|:----|:----|

| `01_inbox/articles/2026-06-03_csv_CSV_File_Reading_and_Writing.md` | `csv` — CSV File Reading and Writing¶ | 自动抓取 |

| `01_inbox/articles/2026-06-03_Quickstart.md` | Quickstart¶ | 自动抓取 |

| `01_inbox/articles/2026-06-03_Tutorial.md` | Tutorial | 自动抓取 |

| `01_inbox/articles/2026-06-03_Getting_Started.md` | Getting Started¶ | 自动抓取 |

| `01_inbox/articles/2026-06-03_10_minutes_to_pandas.md` | 10 minutes to pandas# | 自动抓取 |

| `01_inbox/articles/2026-06-03_Quick_start_guide.md` | Quick start guide# | 自动抓取 |

| `01_inbox/articles/2026-06-03_csv_CSV_File_Reading_and_Writing.md` | `csv` — CSV File Reading and Writing¶ | 自动抓取 |

| `01_inbox/articles/2026-06-03_json_JSON_encoder_and_decoder.md` | `json` — JSON encoder and decoder¶ | 自动抓取 |

| `01_inbox/articles/2026-06-03_pathlib_Object_oriented_filesystem_paths.md` | `pathlib` — Object-oriented filesystem paths¶ | 自动抓取 |

| `01_inbox/articles/2026-06-03_Data_Visualization_With_Python.md` | Data Visualization With Python | 自动抓取 |

| `01_inbox/articles/2026-06-03_Quickstart.md` | Quickstart¶ | 自动抓取 |

| `01_inbox/articles/2026-06-03_Tutorial.md` | Tutorial | 自动抓取 |

| `01_inbox/articles/2026-06-03_Getting_Started.md` | Getting Started¶ | 自动抓取 |

| `01_inbox/articles/2026-06-03_10_minutes_to_pandas.md` | 10 minutes to pandas# | 自动抓取 |

| `01_inbox/articles/2026-06-03_Quick_start_guide.md` | Quick start guide# | 自动抓取 |

| `01_inbox/articles/2026-06-03_csv_CSV_File_Reading_and_Writing.md` | `csv` — CSV File Reading and Writing¶ | 自动抓取 |

| `01_inbox/articles/2026-06-03_json_JSON_encoder_and_decoder.md` | `json` — JSON encoder and decoder¶ | 自动抓取 |

| `01_inbox/articles/2026-06-03_pathlib_Object_oriented_filesystem_paths.md` | `pathlib` — Object-oriented filesystem paths¶ | 自动抓取 |

| `01_inbox/articles/2026-06-03_Data_Visualization_With_Python.md` | Data Visualization With Python | 自动抓取 |

| `01_inbox/articles/2026-06-03_Quickstart.md` | Quickstart¶ | 自动抓取 |

| `01_inbox/articles/2026-06-03_Tutorial.md` | Tutorial | 自动抓取 |

| `01_inbox/articles/2026-06-03_Getting_Started.md` | Getting Started¶ | 自动抓取 |

| `01_inbox/articles/2026-06-03_10_minutes_to_pandas.md` | 10 minutes to pandas# | 自动抓取 |

| `01_inbox/articles/2026-06-03_Quick_start_guide.md` | Quick start guide# | 自动抓取 |

| `01_inbox/articles/2026-06-03_csv_CSV_File_Reading_and_Writing.md` | `csv` — CSV File Reading and Writing¶ | 自动抓取 |

| `01_inbox/articles/2026-06-03_json_JSON_encoder_and_decoder.md` | `json` — JSON encoder and decoder¶ | 自动抓取 |

| `01_inbox/articles/2026-06-03_pathlib_Object_oriented_filesystem_paths.md` | `pathlib` — Object-oriented filesystem paths¶ | 自动抓取 |

| `01_inbox/articles/2026-06-03_Data_Visualization_With_Python.md` | Data Visualization With Python | 自动抓取 |

| `01_inbox/articles/2026-06-03_Quickstart.md` | Quickstart¶ | 自动抓取 |

| `01_inbox/articles/2026-06-03_Tutorial.md` | Tutorial | 自动抓取 |

| `01_inbox/articles/2026-06-03_Getting_Started.md` | Getting Started¶ | 自动抓取 |

| `01_inbox/articles/2026-06-03_10_minutes_to_pandas.md` | 10 minutes to pandas# | 自动抓取 |

| `01_inbox/articles/2026-06-03_Quick_start_guide.md` | Quick start guide# | 自动抓取 |

| `01_inbox/articles/2026-06-03_csv_CSV_File_Reading_and_Writing.md` | `csv` — CSV File Reading and Writing¶ | 自动抓取 |

| `01_inbox/articles/2026-06-03_json_JSON_encoder_and_decoder.md` | `json` — JSON encoder and decoder¶ | 自动抓取 |

| `01_inbox/articles/2026-06-03_pathlib_Object_oriented_filesystem_paths.md` | `pathlib` — Object-oriented filesystem paths¶ | 自动抓取 |

| `01_inbox/articles/2026-06-03_Data_Visualization_With_Python.md` | Data Visualization With Python | 自动抓取 |

| `01_inbox/articles/2026-06-03_Quickstart.md` | Quickstart¶ | 自动抓取 |

| `01_inbox/articles/2026-06-03_Tutorial.md` | Tutorial | 自动抓取 |

| `01_inbox/articles/2026-06-03_Getting_Started.md` | Getting Started¶ | 自动抓取 |

| `01_inbox/articles/2026-06-03_10_minutes_to_pandas.md` | 10 minutes to pandas# | 自动抓取 |

| `01_inbox/articles/2026-06-03_Quick_start_guide.md` | Quick start guide# | 自动抓取 |

| `01_inbox/articles/2026-06-03_csv_CSV_File_Reading_and_Writing.md` | `csv` — CSV File Reading and Writing¶ | 自动抓取 |

| `01_inbox/articles/2026-06-03_json_JSON_encoder_and_decoder.md` | `json` — JSON encoder and decoder¶ | 自动抓取 |

| `01_inbox/articles/2026-06-03_pathlib_Object_oriented_filesystem_paths.md` | `pathlib` — Object-oriented filesystem paths¶ | 自动抓取 |

| `01_inbox/articles/2026-06-03_Data_Visualization_With_Python.md` | Data Visualization With Python | 自动抓取 |

| `01_inbox/articles/2026-06-03_Quickstart.md` | Quickstart¶ | 自动抓取 |

| `01_inbox/articles/2026-06-03_Tutorial.md` | Tutorial | 自动抓取 |

| `01_inbox/articles/2026-06-03_Getting_Started.md` | Getting Started¶ | 自动抓取 |

| `01_inbox/articles/2026-06-03_10_minutes_to_pandas.md` | 10 minutes to pandas# | 自动抓取 |

| `01_inbox/articles/2026-06-03_Quick_start_guide.md` | Quick start guide# | 自动抓取 |

| `01_inbox/articles/2026-06-03_csv_CSV_File_Reading_and_Writing.md` | `csv` — CSV File Reading and Writing¶ | 自动抓取 |

| `01_inbox/articles/2026-06-03_json_JSON_encoder_and_decoder.md` | `json` — JSON encoder and decoder¶ | 自动抓取 |

| `01_inbox/articles/2026-06-03_pathlib_Object_oriented_filesystem_paths.md` | `pathlib` — Object-oriented filesystem paths¶ | 自动抓取 |

| `01_inbox/articles/2026-06-03_Data_Visualization_With_Python.md` | Data Visualization With Python | 自动抓取 |

| `01_inbox/articles/2026-06-03_Quickstart.md` | Quickstart¶ | 自动抓取 |

| `01_inbox/articles/2026-06-03_Tutorial.md` | Tutorial | 自动抓取 |

| `01_inbox/articles/2026-06-03_Getting_Started.md` | Getting Started¶ | 自动抓取 |

| `01_inbox/articles/2026-06-03_10_minutes_to_pandas.md` | 10 minutes to pandas# | 自动抓取 |

| `01_inbox/articles/2026-06-03_Quick_start_guide.md` | Quick start guide# | 自动抓取 |

| `01_inbox/articles/2026-06-03_csv_CSV_File_Reading_and_Writing.md` | `csv` — CSV File Reading and Writing¶ | 自动抓取 |

| `01_inbox/articles/2026-06-03_json_JSON_encoder_and_decoder.md` | `json` — JSON encoder and decoder¶ | 自动抓取 |

| `01_inbox/articles/2026-06-03_pathlib_Object_oriented_filesystem_paths.md` | `pathlib` — Object-oriented filesystem paths¶ | 自动抓取 |

| `01_inbox/articles/2026-06-03_Data_Visualization_With_Python.md` | Data Visualization With Python | 自动抓取 |

### 自动入库 (2026-06-04)

| 文件 | 标题 | 来源 |
|:----|:----|:----|

| `01_inbox/articles/2026-06-04_Quickstart.md` | Quickstart¶ | 自动抓取 |

| `01_inbox/articles/2026-06-04_Tutorial.md` | Tutorial | 自动抓取 |

| `01_inbox/articles/2026-06-04_Getting_Started.md` | Getting Started¶ | 自动抓取 |

| `01_inbox/articles/2026-06-04_10_minutes_to_pandas.md` | 10 minutes to pandas# | 自动抓取 |

| `01_inbox/articles/2026-06-04_Quick_start_guide.md` | Quick start guide# | 自动抓取 |

| `01_inbox/articles/2026-06-04_csv_CSV_File_Reading_and_Writing.md` | `csv` — CSV File Reading and Writing¶ | 自动抓取 |

| `01_inbox/articles/2026-06-04_json_JSON_encoder_and_decoder.md` | `json` — JSON encoder and decoder¶ | 自动抓取 |

| `01_inbox/articles/2026-06-04_pathlib_Object_oriented_filesystem_paths.md` | `pathlib` — Object-oriented filesystem paths¶ | 自动抓取 |

| `01_inbox/articles/2026-06-04_Data_Visualization_With_Python.md` | Data Visualization With Python | 自动抓取 |

| `01_inbox/articles/2026-06-04_Quickstart.md` | Quickstart¶ | 自动抓取 |

| `01_inbox/articles/2026-06-04_Tutorial.md` | Tutorial | 自动抓取 |

| `01_inbox/articles/2026-06-04_Getting_Started.md` | Getting Started¶ | 自动抓取 |

| `01_inbox/articles/2026-06-04_10_minutes_to_pandas.md` | 10 minutes to pandas# | 自动抓取 |

| `01_inbox/articles/2026-06-04_Quick_start_guide.md` | Quick start guide# | 自动抓取 |

| `01_inbox/articles/2026-06-04_csv_CSV_File_Reading_and_Writing.md` | `csv` — CSV File Reading and Writing¶ | 自动抓取 |

| `01_inbox/articles/2026-06-04_json_JSON_encoder_and_decoder.md` | `json` — JSON encoder and decoder¶ | 自动抓取 |

| `01_inbox/articles/2026-06-04_pathlib_Object_oriented_filesystem_paths.md` | `pathlib` — Object-oriented filesystem paths¶ | 自动抓取 |

| `01_inbox/articles/2026-06-04_Data_Visualization_With_Python.md` | Data Visualization With Python | 自动抓取 |
2026-06-04 12:14:10 知识库后台维护完成: 抓取9个站点(成功9/失败3), 归档9个(已有对应笔记, 移至已处理), 去重删除93个(双扩展名21+学习要点重复30+占位符42), 剩余笔记141个

### 自动入库 (2026-06-05)

| 文件 | 标题 | 来源 |
|:----|:----|:----|

| `01_inbox/articles/2026-06-05_Quickstart.md` | Quickstart¶ | 自动抓取 |

| `01_inbox/articles/2026-06-05_Tutorial.md` | Tutorial | 自动抓取 |

| `01_inbox/articles/2026-06-05_Getting_Started.md` | Getting Started¶ | 自动抓取 |

| `01_inbox/articles/2026-06-05_10_minutes_to_pandas.md` | 10 minutes to pandas# | 自动抓取 |

| `01_inbox/articles/2026-06-05_Quick_start_guide.md` | Quick start guide# | 自动抓取 |

| `01_inbox/articles/2026-06-05_csv_CSV_File_Reading_and_Writing.md` | `csv` — CSV File Reading and Writing¶ | 自动抓取 |

| `01_inbox/articles/2026-06-05_json_JSON_encoder_and_decoder.md` | `json` — JSON encoder and decoder¶ | 自动抓取 |

| `01_inbox/articles/2026-06-05_pathlib_Object_oriented_filesystem_paths.md` | `pathlib` — Object-oriented filesystem paths¶ | 自动抓取 |

| `01_inbox/articles/2026-06-05_Data_Visualization_With_Python.md` | Data Visualization With Python | 自动抓取 |

| `01_inbox/articles/2026-06-05_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-06-05_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

### 自动入库 (2026-06-06)

| 文件 | 标题 | 来源 |
|:----|:----|:----|

| `01_inbox/articles/2026-06-06_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-06-06_Quickstart.md` | Quickstart¶ | 自动抓取 |

| `01_inbox/articles/2026-06-06_Tutorial.md` | Tutorial | 自动抓取 |

| `01_inbox/articles/2026-06-06_Getting_Started.md` | Getting Started¶ | 自动抓取 |

| `01_inbox/articles/2026-06-06_10_minutes_to_pandas.md` | 10 minutes to pandas# | 自动抓取 |

| `01_inbox/articles/2026-06-06_Quick_start_guide.md` | Quick start guide# | 自动抓取 |

| `01_inbox/articles/2026-06-06_csv_CSV_File_Reading_and_Writing.md` | `csv` — CSV File Reading and Writing¶ | 自动抓取 |

| `01_inbox/articles/2026-06-06_json_JSON_encoder_and_decoder.md` | `json` — JSON encoder and decoder¶ | 自动抓取 |

| `01_inbox/articles/2026-06-06_pathlib_Object_oriented_filesystem_paths.md` | `pathlib` — Object-oriented filesystem paths¶ | 自动抓取 |

| `01_inbox/articles/2026-06-06_Data_Visualization_With_Python.md` | Data Visualization With Python | 自动抓取 |

| `01_inbox/articles/2026-06-06_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-06-06_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

### 自动入库 (2026-06-07)

| 文件 | 标题 | 来源 |
|:----|:----|:----|

| `01_inbox/articles/2026-06-07_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-06-07_Quickstart.md` | Quickstart¶ | 自动抓取 |

| `01_inbox/articles/2026-06-07_Tutorial.md` | Tutorial | 自动抓取 |

| `01_inbox/articles/2026-06-07_Getting_Started.md` | Getting Started¶ | 自动抓取 |

| `01_inbox/articles/2026-06-07_10_minutes_to_pandas.md` | 10 minutes to pandas# | 自动抓取 |

| `01_inbox/articles/2026-06-07_Quick_start_guide.md` | Quick start guide# | 自动抓取 |

| `01_inbox/articles/2026-06-07_csv_CSV_File_Reading_and_Writing.md` | `csv` — CSV File Reading and Writing¶ | 自动抓取 |

| `01_inbox/articles/2026-06-07_json_JSON_encoder_and_decoder.md` | `json` — JSON encoder and decoder¶ | 自动抓取 |

| `01_inbox/articles/2026-06-07_pathlib_Object_oriented_filesystem_paths.md` | `pathlib` — Object-oriented filesystem paths¶ | 自动抓取 |

| `01_inbox/articles/2026-06-07_Data_Visualization_With_Python.md` | Data Visualization With Python | 自动抓取 |

| `01_inbox/articles/2026-06-07_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-06-07_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

### 自动入库 (2026-06-08)

| 文件 | 标题 | 来源 |
|:----|:----|:----|

| `01_inbox/articles/2026-06-08_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-06-08_Quickstart.md` | Quickstart¶ | 自动抓取 |

| `01_inbox/articles/2026-06-08_Tutorial.md` | Tutorial | 自动抓取 |

| `01_inbox/articles/2026-06-08_Getting_Started.md` | Getting Started¶ | 自动抓取 |

| `01_inbox/articles/2026-06-08_10_minutes_to_pandas.md` | 10 minutes to pandas# | 自动抓取 |

| `01_inbox/articles/2026-06-08_Quick_start_guide.md` | Quick start guide# | 自动抓取 |

| `01_inbox/articles/2026-06-08_csv_CSV_File_Reading_and_Writing.md` | `csv` — CSV File Reading and Writing¶ | 自动抓取 |

| `01_inbox/articles/2026-06-08_json_JSON_encoder_and_decoder.md` | `json` — JSON encoder and decoder¶ | 自动抓取 |

| `01_inbox/articles/2026-06-08_pathlib_Object_oriented_filesystem_paths.md` | `pathlib` — Object-oriented filesystem paths¶ | 自动抓取 |

| `01_inbox/articles/2026-06-08_Data_Visualization_With_Python.md` | Data Visualization With Python | 自动抓取 |

| `01_inbox/articles/2026-06-08_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-06-08_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

### 自动入库 (2026-06-09)

| 文件 | 标题 | 来源 |
|:----|:----|:----|

| `01_inbox/articles/2026-06-09_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-06-09_Quickstart.md` | Quickstart¶ | 自动抓取 |

| `01_inbox/articles/2026-06-09_Tutorial.md` | Tutorial | 自动抓取 |

| `01_inbox/articles/2026-06-09_Getting_Started.md` | Getting Started¶ | 自动抓取 |

| `01_inbox/articles/2026-06-09_10_minutes_to_pandas.md` | 10 minutes to pandas# | 自动抓取 |

| `01_inbox/articles/2026-06-09_Quick_start_guide.md` | Quick start guide# | 自动抓取 |

| `01_inbox/articles/2026-06-09_csv_CSV_File_Reading_and_Writing.md` | `csv` — CSV File Reading and Writing¶ | 自动抓取 |

| `01_inbox/articles/2026-06-09_json_JSON_encoder_and_decoder.md` | `json` — JSON encoder and decoder¶ | 自动抓取 |

| `01_inbox/articles/2026-06-09_pathlib_Object_oriented_filesystem_paths.md` | `pathlib` — Object-oriented filesystem paths¶ | 自动抓取 |

| `01_inbox/articles/2026-06-09_Data_Visualization_With_Python.md` | Data Visualization With Python | 自动抓取 |

| `01_inbox/articles/2026-06-09_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-06-09_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

### 2026-06-09 后台维护

| 操作 | 详情 |
|:----|:----|
| 归档自动学习 | 26 个 06-08 抓取文件 → 02-笔记/实体/ (17) + 方法/ (9) |
| 归档 _from_user | 4 个用户文件，3 新 → 实体/，1 已存在 → 归档 |
| 归档 duplicate_names | 6 个 → 99-归档（已有对应实体） |
| 清理 inbox | 01_inbox/articles 30 个全归档（内容已编译入实体/） |
| 清理 auto-capture | 20 个旧 Python doc → 99-归档 |
| 去重 entity/ | 合并 Getting Started, csv, json, pathlib 的 ¶/无¶ 变体 |
| 去重 entity/ | 合并 从流水线到蜂巢, 国产模型, 得物 AI Harness 的日期变体 |
| 去重 method/ | 合并 架构变更案例, 3个维度的日期格式变体 |
| 归档 Node.js 重复 | 392b vs 614b 两个版本，保留大的 |
| 归档 Quickstart 重复 | 1723b vs 999b，保留大的 |
| 归档 csv 重复 | 1126b vs 1126b，保留一个 |

最终状态：
- 实体/ 132 个文件
- 方法/ 55 个文件  
- 概念/ 38 个文件
- 归档/ 81 个文件（含本次归档的备份）
- 收件箱：清空

### 自动入库 (2026-06-10)

| 文件 | 标题 | 来源 |
|:----|:----|:----|

| `01_inbox/articles/2026-06-10_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

### 2026-06-10 后台维护

| 操作 | 详情 |
|:----|:----|
| 编译新入库 | 1 个：Hermes Agent 官方文档 → 实体/Hermes_Agent_2026-06-10.md |
| 归档重复 | 7 个：AnySearch/All-MiniLM/商汤Skills/10minutes/Quickstart/DataViz 的学习要点变体 |
| 去重删除 | 3 个：文件名微小差异（空格/# 变体） |
| 收件箱清理 | 清空 01_inbox/articles/ |

最终状态：
- 实体/ 122 个文件
- 概念/ 38 个文件
- 方法/ 53 个文件
- 地图/ 2 个文件
- 归档/ 85 个文件
- 收件箱：清空

---

| `01_inbox/articles/2026-06-10_Quickstart.md` | Quickstart¶ | 自动抓取 |

| `01_inbox/articles/2026-06-10_Tutorial.md` | Tutorial | 自动抓取 |

| `01_inbox/articles/2026-06-10_Getting_Started.md` | Getting Started¶ | 自动抓取 |

| `01_inbox/articles/2026-06-10_10_minutes_to_pandas.md` | 10 minutes to pandas# | 自动抓取 |

| `01_inbox/articles/2026-06-10_Quick_start_guide.md` | Quick start guide# | 自动抓取 |

| `01_inbox/articles/2026-06-10_csv_CSV_File_Reading_and_Writing.md` | `csv` — CSV File Reading and Writing¶ | 自动抓取 |

| `01_inbox/articles/2026-06-10_json_JSON_encoder_and_decoder.md` | `json` — JSON encoder and decoder¶ | 自动抓取 |

| `01_inbox/articles/2026-06-10_pathlib_Object_oriented_filesystem_paths.md` | `pathlib` — Object-oriented filesystem paths¶ | 自动抓取 |

| `01_inbox/articles/2026-06-10_Data_Visualization_With_Python.md` | Data Visualization With Python | 自动抓取 |

| `01_inbox/articles/2026-06-10_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

### 2026-06-10 12:10 后台维护

| 操作 | 详情 |
|:----|:----|
| 编译验证 | Hermes Agent 已于 07:00 编译完成 → 实体/Hermes_Agent_2026-06-10.md |
| 归档收件箱 | 01_inbox/articles/ 10 个重复文件 → 99-归档/ |
| 归档自动捕获 | 01-收件箱/自动捕获/ 9 个重复文件 → 99-归档/ |
| 实体去重 | 删除 3 个完全相同重复 (json/10minutes/Quickstart guide 的 #/¶ 变体) |
| 实体合并 | 合并 2 个大小不同重复 (Quickstart 999b→1723b, Tutorial 975b→1674b) |
| 地图状态 | 无需更新，Hermes Agent 已在 AI技术地图中覆盖 |

最终状态：
- 实体/ 121 个文件
- 概念/ 38 个文件
- 方法/ 53 个文件
- 地图/ 2 个文件
- 归档/ 新增 19 个文件
- 收件箱：已清空

| `01_inbox/articles/2026-06-10_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

### 自动入库 (2026-06-11)

| 文件 | 标题 | 来源 |
|:----|:----|:----|

| `01_inbox/articles/2026-06-11_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-06-11_Quickstart.md` | Quickstart¶ | 自动抓取 |

| `01_inbox/articles/2026-06-11_Tutorial.md` | Tutorial | 自动抓取 |

| `01_inbox/articles/2026-06-11_Getting_Started.md` | Getting Started¶ | 自动抓取 |

| `01_inbox/articles/2026-06-11_10_minutes_to_pandas.md` | 10 minutes to pandas# | 自动抓取 |

| `01_inbox/articles/2026-06-11_Quick_start_guide.md` | Quick start guide# | 自动抓取 |

| `01_inbox/articles/2026-06-11_csv_CSV_File_Reading_and_Writing.md` | `csv` — CSV File Reading and Writing¶ | 自动抓取 |

| `01_inbox/articles/2026-06-11_json_JSON_encoder_and_decoder.md` | `json` — JSON encoder and decoder¶ | 自动抓取 |

| `01_inbox/articles/2026-06-11_pathlib_Object_oriented_filesystem_paths.md` | `pathlib` — Object-oriented filesystem paths¶ | 自动抓取 |

| `01_inbox/articles/2026-06-11_Data_Visualization_With_Python.md` | Data Visualization With Python | 自动抓取 |

| `01_inbox/articles/2026-06-11_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-06-11_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

### 自动入库 (2026-06-12)

| 文件 | 标题 | 来源 |
|:----|:----|:----|

| `01_inbox/articles/2026-06-12_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

### 自动维护 (2026-06-12)

| 操作 | 详情 |
|:----|:----|
| 归档自动捕获 | 01-收件箱/archive/自动捕获/ 9 个文件 → 99-归档/2026-06-12/ |
| 归档 01_inbox | 2026-06-12_Hermes_Agent.md → 99-归档/2026-06-12/ |
| 收件箱 | 已清空 |
| 实体去重 | 删除 1 个 pandas 重复 (_学习要点.md vs _学习要点.md) |
| 实体去重 | 删除 1 个 从流水线到蜂巢 重复 (双后缀坏文件) |
| 实体去重 | 删除 1 个 Getting Started¶_学习要点.md (已由 python-pptx 编译覆盖) |
| 实体去重 | 删除 1 个 方法索引_学习要点.md (错放至实体目录) |
| 实体去重 | 删除 1 个 知识库集成 (350 bytes 空占位) |
| 空壳清理 | 删除 10 个 <500 bytes 空壳实体文件 |
| 空壳清理 | 删除 1 个 <500 bytes 空壳方法文件 |
| 空壳清理 | 删除 1 个 方法/index.md (79 bytes 自动生成) |
| 重命名修复 | 架构变更案例: _学习要点_学习要点 → _学习要点 |

最终状态：
- 实体/ 97 个文件 (原112, 减少15)
- 概念/ 38 个文件
- 方法/ 46 个文件 (原50, 减少4)
- 地图/ 2 个文件
- 归档/ 新增 11 个文件

| `01_inbox/articles/2026-06-12_Getting_Started.md` | Getting Started¶ | 自动抓取 |

| `01_inbox/articles/2026-06-12_10_minutes_to_pandas.md` | 10 minutes to pandas# | 自动抓取 |

| `01_inbox/articles/2026-06-12_Quick_start_guide.md` | Quick start guide# | 自动抓取 |

| `01_inbox/articles/2026-06-12_csv_CSV_File_Reading_and_Writing.md` | `csv` — CSV File Reading and Writing¶ | 自动抓取 |

| `01_inbox/articles/2026-06-12_json_JSON_encoder_and_decoder.md` | `json` — JSON encoder and decoder¶ | 自动抓取 |

| `01_inbox/articles/2026-06-12_pathlib_Object_oriented_filesystem_paths.md` | `pathlib` — Object-oriented filesystem paths¶ | 自动抓取 |

| `01_inbox/articles/2026-06-12_Data_Visualization_With_Python.md` | Data Visualization With Python | 自动抓取 |

| `01_inbox/articles/2026-06-12_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-06-12_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

### 自动入库 (2026-06-13)

| 文件 | 标题 | 来源 |
|:----|:----|:----|

| `01_inbox/articles/2026-06-13_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-06-13_Quickstart.md` | Quickstart¶ | 自动抓取 |

| `01_inbox/articles/2026-06-13_Tutorial.md` | Tutorial | 自动抓取 |

| `01_inbox/articles/2026-06-13_Getting_Started.md` | Getting Started¶ | 自动抓取 |

| `01_inbox/articles/2026-06-13_10_minutes_to_pandas.md` | 10 minutes to pandas# | 自动抓取 |

| `01_inbox/articles/2026-06-13_Quick_start_guide.md` | Quick start guide# | 自动抓取 |

| `01_inbox/articles/2026-06-13_csv_CSV_File_Reading_and_Writing.md` | `csv` — CSV File Reading and Writing¶ | 自动抓取 |

| `01_inbox/articles/2026-06-13_json_JSON_encoder_and_decoder.md` | `json` — JSON encoder and decoder¶ | 自动抓取 |

| `01_inbox/articles/2026-06-13_pathlib_Object_oriented_filesystem_paths.md` | `pathlib` — Object-oriented filesystem paths¶ | 自动抓取 |

| `01_inbox/articles/2026-06-13_Data_Visualization_With_Python.md` | Data Visualization With Python | 自动抓取 |

| `01_inbox/articles/2026-06-13_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-06-13_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

### 自动入库 (2026-06-14)

| 文件 | 标题 | 来源 |
|:----|:----|:----|

| `01_inbox/articles/2026-06-14_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-06-14_Quickstart.md` | Quickstart¶ | 自动抓取 |

| `01_inbox/articles/2026-06-14_Tutorial.md` | Tutorial | 自动抓取 |

| `01_inbox/articles/2026-06-14_Getting_Started.md` | Getting Started¶ | 自动抓取 |

| `01_inbox/articles/2026-06-14_10_minutes_to_pandas.md` | 10 minutes to pandas# | 自动抓取 |

| `01_inbox/articles/2026-06-14_Quick_start_guide.md` | Quick start guide# | 自动抓取 |

| `01_inbox/articles/2026-06-14_csv_CSV_File_Reading_and_Writing.md` | `csv` — CSV File Reading and Writing¶ | 自动抓取 |

| `01_inbox/articles/2026-06-14_json_JSON_encoder_and_decoder.md` | `json` — JSON encoder and decoder¶ | 自动抓取 |

| `01_inbox/articles/2026-06-14_pathlib_Object_oriented_filesystem_paths.md` | `pathlib` — Object-oriented filesystem paths¶ | 自动抓取 |

| `01_inbox/articles/2026-06-14_Data_Visualization_With_Python.md` | Data Visualization With Python | 自动抓取 |

| `01_inbox/articles/2026-06-14_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-06-14_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

### 自动入库 (2026-06-15)

| 文件 | 标题 | 来源 |
|:----|:----|:----|

| `01_inbox/articles/2026-06-15_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-06-15_Quickstart.md` | Quickstart¶ | 自动抓取 |

| `01_inbox/articles/2026-06-15_Tutorial.md` | Tutorial | 自动抓取 |

| `01_inbox/articles/2026-06-15_Getting_Started.md` | Getting Started¶ | 自动抓取 |

| `01_inbox/articles/2026-06-15_10_minutes_to_pandas.md` | 10 minutes to pandas# | 自动抓取 |

| `01_inbox/articles/2026-06-15_Quick_start_guide.md` | Quick start guide# | 自动抓取 |

| `01_inbox/articles/2026-06-15_csv_CSV_File_Reading_and_Writing.md` | `csv` — CSV File Reading and Writing¶ | 自动抓取 |

| `01_inbox/articles/2026-06-15_json_JSON_encoder_and_decoder.md` | `json` — JSON encoder and decoder¶ | 自动抓取 |

| `01_inbox/articles/2026-06-15_pathlib_Object_oriented_filesystem_paths.md` | `pathlib` — Object-oriented filesystem paths¶ | 自动抓取 |

| `01_inbox/articles/2026-06-15_Data_Visualization_With_Python.md` | Data Visualization With Python | 自动抓取 |

| `01_inbox/articles/2026-06-15_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

### 2026-06-15 后台维护

| 操作 | 详情 |
|:----|:----|
| 归档自动捕获 | 9 个文件 → 99-归档/2026-06-15/ |
| 归档自动学习 | 7 个文件（5 JSON + 学习报告 + _fetch_summary.json）→ 99-归档/2026-06-15/ |
| 实体去重清理 | 34 个学习要点模板（内容空洞自动生成）→ 归档 |
| 实体去重清理 | 37 个 draft 状态小文件（<2000 bytes，status: draft）→ 归档 |
| 实体目录精简 | 从 106 个 → 34 个（保留高质量完整实体） |
| 收件箱 | 自动捕获/ 清空，自动学习/ 仅保留学习报告 |

最终状态：
- 实体/ 34 个文件（含 8 个完整编译 >5KB + 26 个轻量实体 1-5KB）
- 概念/ 39 个文件
- 方法/ 46 个文件
- 地图/ 2 个文件
- 归档/2026-06-15/ 90 个文件
- 收件箱：已清空

关键发现：
- 自动捕获的9个Python文档（pandas/csv/json/pathlib等）已有完整编译实体（2026-05-31版本）
- 34个学习要点模板是低质量自动生成的占位符，已清理
- 37个draft小文件是早期编译半成品，已清理
- 学习报告指出Hermes Agent v0.16.0有Desktop App、远程网关等新功能

| `01_inbox/articles/2026-06-15_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

### 自动入库 (2026-06-16)

| 文件 | 标题 | 来源 |
|:----|:----|:----|

| `01_inbox/articles/2026-06-16_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-06-16_Quickstart.md` | Quickstart¶ | 自动抓取 |

| `01_inbox/articles/2026-06-16_Tutorial.md` | Tutorial | 自动抓取 |

| `01_inbox/articles/2026-06-16_Getting_Started.md` | Getting Started¶ | 自动抓取 |

| `01_inbox/articles/2026-06-16_10_minutes_to_pandas.md` | 10 minutes to pandas# | 自动抓取 |

| `01_inbox/articles/2026-06-16_Quick_start_guide.md` | Quick start guide# | 自动抓取 |

| `01_inbox/articles/2026-06-16_csv_CSV_File_Reading_and_Writing.md` | `csv` — CSV File Reading and Writing¶ | 自动抓取 |

| `01_inbox/articles/2026-06-16_json_JSON_encoder_and_decoder.md` | `json` — JSON encoder and decoder¶ | 自动抓取 |

| `01_inbox/articles/2026-06-16_pathlib_Object_oriented_filesystem_paths.md` | `pathlib` — Object-oriented filesystem paths¶ | 自动抓取 |

| `01_inbox/articles/2026-06-16_Data_Visualization_With_Python.md` | Data Visualization With Python | 自动抓取 |

| `01_inbox/articles/2026-06-16_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

### 2026-06-16 12:20 后台维护

| 操作 | 详情 |
|:----|:----|
| 编译 | Agent-Skills — 60k star 项目，将工程开发流程打包为 AI 技能 → 02-笔记/实体/Agent-Skills.md |
| 归档自动捕获 | 01-收件箱/自动捕获/ 10 个重复文件 → 99-归档/2026-06-16/ |
| 归档旧管道 | 01_inbox/articles/ 20 个重复文件（06-15 ×9 + 06-16 ×11）→ 99-归档/2026-06-16/ |
| 实体去重 | 10 个自动生成的 _学习要点.md 占位符（<2000 bytes，空内容）→ 归档 |
| 地图更新 | AI技术地图 新增 [[Agent-Skills]] 条目，updated 更新至 2026-06-16 |

最终状态：
- 实体/ 35 个文件（原44，去重-10，新增+1）
- 概念/ 39 个文件
- 方法/ 46 个文件
- 地图/ 2 个文件
- 归档/2026-06-16/ 新增 30 个文件
- 收件箱：已清空（含新旧管道）

| `01_inbox/articles/2026-06-16_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

### 自动入库 (2026-06-17)

| 文件 | 标题 | 来源 |
|:----|:----|:----|

| `01_inbox/articles/2026-06-17_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

### 2026-06-17 06:10 后台维护

| 操作 | 详情 |
|:----|:----|
| 抓取编译 | `articles/15个被忽略的Agent高级能力-王二AI进化论.md` — 内容已在 `02-笔记/方法/` 中存在，无需重复编译 |
| 归档收件箱 | 01_inbox/articles/ 2 个 Heremes Agent 重复文件 + articles/ 1 个方法重复文件 → 99-归档/2026-06-17/ |
| 去重 | 3 个文件均为已编译笔记的重复捕获，全部归档不保留副本 |
| 实体补充 | 无需补充 — 概念/Hermes-Agent.md 和 07-地图/AI技术地图.md 均已引用此文章 |
| 地图状态 | [[15个被忽略的Agent高级能力-王二AI进化论]] 引用已在之前维护中建立，无需更新 |

最终状态：
- 实体/ 35 个文件（无变化）
- 概念/ 39 个文件（无变化）
- 方法/ 46 个文件（无变化）
- 地图/ 2 个文件（无变化）
- 归档/2026-06-17/ 新增 3 个文件
- 收件箱：已清空

| `01_inbox/articles/2026-06-17_Quickstart.md` | Quickstart¶ | 自动抓取 |

| `01_inbox/articles/2026-06-17_Tutorial.md` | Tutorial | 自动抓取 |

| `01_inbox/articles/2026-06-17_Getting_Started.md` | Getting Started¶ | 自动抓取 |

| `01_inbox/articles/2026-06-17_10_minutes_to_pandas.md` | 10 minutes to pandas# | 自动抓取 |

| `01_inbox/articles/2026-06-17_Quick_start_guide.md` | Quick start guide# | 自动抓取 |

| `01_inbox/articles/2026-06-17_csv_CSV_File_Reading_and_Writing.md` | `csv` — CSV File Reading and Writing¶ | 自动抓取 |

| `01_inbox/articles/2026-06-17_json_JSON_encoder_and_decoder.md` | `json` — JSON encoder and decoder¶ | 自动抓取 |

| `01_inbox/articles/2026-06-17_pathlib_Object_oriented_filesystem_paths.md` | `pathlib` — Object-oriented filesystem paths¶ | 自动抓取 |

| `01_inbox/articles/2026-06-17_Data_Visualization_With_Python.md` | Data Visualization With Python | 自动抓取 |

| `01_inbox/articles/2026-06-17_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-06-17_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

### 自动入库 (2026-06-18)

| 文件 | 标题 | 来源 |
|:----|:----|:----|

| `01_inbox/articles/2026-06-18_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-06-18_Quickstart.md` | Quickstart¶ | 自动抓取 |

| `01_inbox/articles/2026-06-18_Tutorial.md` | Tutorial | 自动抓取 |

| `01_inbox/articles/2026-06-18_Getting_Started.md` | Getting Started¶ | 自动抓取 |

| `01_inbox/articles/2026-06-18_10_minutes_to_pandas.md` | 10 minutes to pandas# | 自动抓取 |

| `01_inbox/articles/2026-06-18_Quick_start_guide.md` | Quick start guide# | 自动抓取 |

| `01_inbox/articles/2026-06-18_csv_CSV_File_Reading_and_Writing.md` | `csv` — CSV File Reading and Writing¶ | 自动抓取 |

| `01_inbox/articles/2026-06-18_json_JSON_encoder_and_decoder.md` | `json` — JSON encoder and decoder¶ | 自动抓取 |

| `01_inbox/articles/2026-06-18_pathlib_Object_oriented_filesystem_paths.md` | `pathlib` — Object-oriented filesystem paths¶ | 自动抓取 |

| `01_inbox/articles/2026-06-18_Data_Visualization_With_Python.md` | Data Visualization With Python | 自动抓取 |

| `01_inbox/articles/2026-06-18_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-06-18_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

### 自动入库 (2026-06-19)

| 文件 | 标题 | 来源 |
|:----|:----|:----|

| `01_inbox/articles/2026-06-19_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-06-19_Quickstart.md` | Quickstart¶ | 自动抓取 |

| `01_inbox/articles/2026-06-19_Tutorial.md` | Tutorial | 自动抓取 |

| `01_inbox/articles/2026-06-19_Getting_Started.md` | Getting Started¶ | 自动抓取 |

| `01_inbox/articles/2026-06-19_10_minutes_to_pandas.md` | 10 minutes to pandas# | 自动抓取 |

| `01_inbox/articles/2026-06-19_Quick_start_guide.md` | Quick start guide# | 自动抓取 |

| `01_inbox/articles/2026-06-19_csv_CSV_File_Reading_and_Writing.md` | `csv` — CSV File Reading and Writing¶ | 自动抓取 |

| `01_inbox/articles/2026-06-19_json_JSON_encoder_and_decoder.md` | `json` — JSON encoder and decoder¶ | 自动抓取 |

| `01_inbox/articles/2026-06-19_pathlib_Object_oriented_filesystem_paths.md` | `pathlib` — Object-oriented filesystem paths¶ | 自动抓取 |

| `01_inbox/articles/2026-06-19_Data_Visualization_With_Python.md` | Data Visualization With Python | 自动抓取 |

| `01_inbox/articles/2026-06-19_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

### 2026-06-19 12:01 后台维护

| 操作 | 详情 |
|:----|:----|
| 抓取编译 | 01-收件箱/自动捕获/ 10 个文件 → 02-笔记/实体/ 10 篇 `_学习要点.md`（pandas/csv/json/pathlib/pptx/Tutorial/Hermes Agent 等）|
| 归档去重 | 01_inbox/articles/ 10 个文件（与 01-收件箱/自动捕获/ 内容完全重复）→ 01_inbox/archive/articles/2026-06-19_2/ |
| 归档自动捕获 | 01-收件箱/自动捕获/ 10 个文件（已编译）→ 01-收件箱/archive/自动捕获/2026-06-19/ |
| 实体去重 | 02-笔记/实体/ 中 flat copies 与 _学习要点 内容各异，无精确重复，保留 |
| 概念补充 | Hermes-Agent.md 已在 04:05 追加 06-19 hash 记录，无需再改 |
| 地图状态 | 07-地图/ 两份地图均无需更新 — 新增内容为 Python 标准库/工具文档，非新领域 |

| `01_inbox/articles/2026-06-19_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

### 自动入库 (2026-06-20)

| 文件 | 标题 | 来源 |
|:----|:----|:----|

| `01_inbox/articles/2026-06-20_Quickstart.md` | Quickstart¶ | 自动抓取 |

| `01_inbox/articles/2026-06-20_Tutorial.md` | Tutorial | 自动抓取 |

| `01_inbox/articles/2026-06-20_Getting_Started.md` | Getting Started¶ | 自动抓取 |

| `01_inbox/articles/2026-06-20_10_minutes_to_pandas.md` | 10 minutes to pandas# | 自动抓取 |

| `01_inbox/articles/2026-06-20_Quick_start_guide.md` | Quick start guide# | 自动抓取 |

| `01_inbox/articles/2026-06-20_csv_CSV_File_Reading_and_Writing.md` | `csv` — CSV File Reading and Writing¶ | 自动抓取 |

| `01_inbox/articles/2026-06-20_json_JSON_encoder_and_decoder.md` | `json` — JSON encoder and decoder¶ | 自动抓取 |

| `01_inbox/articles/2026-06-20_pathlib_Object_oriented_filesystem_paths.md` | `pathlib` — Object-oriented filesystem paths¶ | 自动抓取 |

| `01_inbox/articles/2026-06-20_Data_Visualization_With_Python.md` | Data Visualization With Python | 自动抓取 |

### 自动入库 (2026-06-21)

| 文件 | 标题 | 来源 |
|:----|:----|:----|

| `01_inbox/articles/2026-06-21_Quickstart.md` | Quickstart¶ | 自动抓取 |

| `01_inbox/articles/2026-06-21_Tutorial.md` | Tutorial | 自动抓取 |

| `01_inbox/articles/2026-06-21_Getting_Started.md` | Getting Started¶ | 自动抓取 |

| `01_inbox/articles/2026-06-21_10_minutes_to_pandas.md` | 10 minutes to pandas# | 自动抓取 |

| `01_inbox/articles/2026-06-21_Quick_start_guide.md` | Quick start guide# | 自动抓取 |

| `01_inbox/articles/2026-06-21_csv_CSV_File_Reading_and_Writing.md` | `csv` — CSV File Reading and Writing¶ | 自动抓取 |

| `01_inbox/articles/2026-06-21_json_JSON_encoder_and_decoder.md` | `json` — JSON encoder and decoder¶ | 自动抓取 |

| `01_inbox/articles/2026-06-21_pathlib_Object_oriented_filesystem_paths.md` | `pathlib` — Object-oriented filesystem paths¶ | 自动抓取 |

| `01_inbox/articles/2026-06-21_Data_Visualization_With_Python.md` | Data Visualization With Python | 自动抓取 |

| `01_inbox/articles/2026-06-21_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-06-21_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

### 2026-06-21 19:45 后台维护

| 操作 | 详情 |
|:----|:----|
| 编译 Hermes Agent 第2轮捕获 | 01_inbox/articles/ 1 个文件（llms-full.txt hash `aa5cd62b...`，与第1轮 `6b61486b...` 不同）→ 补充概念笔记 changelog |
| 归档自动捕获 | 01-收件箱/自动捕获/ 9 个文件（已编译）→ 01-收件箱/archive/自动捕获/2026-06-21/ |
| 归档原始文件 | 01_inbox/articles/ 10 个文件 → 01_inbox/archive/articles/2026-06-21/ |
| 实体去重 | 02-笔记/实体/ 中 flat copies 与 _学习要点 内容各异，无精确重复，保留 |
| 概念补充 | Hermes-Agent.md 追加 06-21 第2轮 hash 变更记录 |
| 地图状态 | 07-地图/ 两份地图均无需更新 — 内容为 Python 标准库/工具文档，非新领域 |

### 自动入库 (2026-06-22)

| 文件 | 标题 | 来源 |
|:----|:----|:----|

| `01_inbox/articles/2026-06-22_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-06-22_Quickstart.md` | Quickstart¶ | 自动抓取 |

| `01_inbox/articles/2026-06-22_Tutorial.md` | Tutorial | 自动抓取 |

| `01_inbox/articles/2026-06-22_Getting_Started.md` | Getting Started¶ | 自动抓取 |

| `01_inbox/articles/2026-06-22_10_minutes_to_pandas.md` | 10 minutes to pandas# | 自动抓取 |

| `01_inbox/articles/2026-06-22_Quick_start_guide.md` | Quick start guide# | 自动抓取 |

| `01_inbox/articles/2026-06-22_csv_CSV_File_Reading_and_Writing.md` | `csv` — CSV File Reading and Writing¶ | 自动抓取 |

| `01_inbox/articles/2026-06-22_json_JSON_encoder_and_decoder.md` | `json` — JSON encoder and decoder¶ | 自动抓取 |

| `01_inbox/articles/2026-06-22_pathlib_Object_oriented_filesystem_paths.md` | `pathlib` — Object-oriented filesystem paths¶ | 自动抓取 |

| `01_inbox/articles/2026-06-22_Data_Visualization_With_Python.md` | Data Visualization With Python | 自动抓取 |

| `01_inbox/articles/2026-06-22_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-06-22_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

### 自动入库 (2026-06-23)

| 文件 | 标题 | 来源 |
|:----|:----|:----|

| `01_inbox/articles/2026-06-23_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-06-23_Quickstart.md` | Quickstart¶ | 自动抓取 |

| `01_inbox/articles/2026-06-23_Tutorial.md` | Tutorial | 自动抓取 |

| `01_inbox/articles/2026-06-23_Getting_Started.md` | Getting Started¶ | 自动抓取 |

| `01_inbox/articles/2026-06-23_10_minutes_to_pandas.md` | 10 minutes to pandas# | 自动抓取 |

| `01_inbox/articles/2026-06-23_Quick_start_guide.md` | Quick start guide# | 自动抓取 |

| `01_inbox/articles/2026-06-23_csv_CSV_File_Reading_and_Writing.md` | `csv` — CSV File Reading and Writing¶ | 自动抓取 |

| `01_inbox/articles/2026-06-23_json_JSON_encoder_and_decoder.md` | `json` — JSON encoder and decoder¶ | 自动抓取 |

| `01_inbox/articles/2026-06-23_pathlib_Object_oriented_filesystem_paths.md` | `pathlib` — Object-oriented filesystem paths¶ | 自动抓取 |

| `01_inbox/articles/2026-06-23_Data_Visualization_With_Python.md` | Data Visualization With Python | 自动抓取 |

| `01_inbox/articles/2026-06-23_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-06-23_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

### 自动入库 (2026-06-24)

| 文件 | 标题 | 来源 |
|:----|:----|:----|

| `01_inbox/articles/2026-06-24_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-06-24_Quickstart.md` | Quickstart¶ | 自动抓取 |

| `01_inbox/articles/2026-06-24_Tutorial.md` | Tutorial | 自动抓取 |

| `01_inbox/articles/2026-06-24_Getting_Started.md` | Getting Started¶ | 自动抓取 |

| `01_inbox/articles/2026-06-24_10_minutes_to_pandas.md` | 10 minutes to pandas# | 自动抓取 |

| `01_inbox/articles/2026-06-24_Quick_start_guide.md` | Quick start guide# | 自动抓取 |

| `01_inbox/articles/2026-06-24_csv_CSV_File_Reading_and_Writing.md` | `csv` — CSV File Reading and Writing¶ | 自动抓取 |

| `01_inbox/articles/2026-06-24_json_JSON_encoder_and_decoder.md` | `json` — JSON encoder and decoder¶ | 自动抓取 |

| `01_inbox/articles/2026-06-24_pathlib_Object_oriented_filesystem_paths.md` | `pathlib` — Object-oriented filesystem paths¶ | 自动抓取 |

| `01_inbox/articles/2026-06-24_Data_Visualization_With_Python.md` | Data Visualization With Python | 自动抓取 |

| `01_inbox/articles/2026-06-24_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-06-24_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

### 自动入库 (2026-06-25)

| 文件 | 标题 | 来源 |
|:----|:----|:----|

| `01_inbox/articles/2026-06-25_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

### 自动入库 (2026-06-25)

| 文件 | 标题 | 来源 |
|:----|:-----|:-----|
| `01_inbox/articles/2026-06-25_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

### 后台维护 (2026-06-25)

| 操作 | 详情 |
|:----|:------|
| 编译 | 01_inbox/articles/ 2 个新文件 (Hermes Agent 2026-06-24 + 2026-06-25) — 同一来源 (hermes-agent.nousresearch.com/docs)，仅 llms-full.txt hash 从 `cdb9d5f9...` 变更为 `57c49f3d...`，页面内容无结构性变化 |
| 归档 | 2 个文件 → archive/articles/2026-06-24/ + 2026-06-25/ |
| 去重 | archive 清理 130 个重复文件（Python 文档 x9×15次 + Hermes Agent x15次），每个文档保留最新版本 |
| 概念补充 | Hermes-Agent.md 追加 06-25 hash 变更记录 |
| 地图状态 | 07-地图/Hermes-能力地图.md 仍为空，无需更新（非结构化变更） |

最终状态：
- 01_inbox/articles: 0 个待处理文件
- 01-收件箱 所有子目录: 已清空
- archive 文件数: 从 ~150 精简至 21 个

| `01_inbox/articles/2026-06-25_Quickstart.md` | Quickstart¶ | 自动抓取 |

| `01_inbox/articles/2026-06-25_Tutorial.md` | Tutorial | 自动抓取 |

| `01_inbox/articles/2026-06-25_Getting_Started.md` | Getting Started¶ | 自动抓取 |

| `01_inbox/articles/2026-06-25_10_minutes_to_pandas.md` | 10 minutes to pandas# | 自动抓取 |

| `01_inbox/articles/2026-06-25_Quick_start_guide.md` | Quick start guide# | 自动抓取 |

| `01_inbox/articles/2026-06-25_csv_CSV_File_Reading_and_Writing.md` | `csv` — CSV File Reading and Writing¶ | 自动抓取 |

| `01_inbox/articles/2026-06-25_json_JSON_encoder_and_decoder.md` | `json` — JSON encoder and decoder¶ | 自动抓取 |

| `01_inbox/articles/2026-06-25_pathlib_Object_oriented_filesystem_paths.md` | `pathlib` — Object-oriented filesystem paths¶ | 自动抓取 |

| `01_inbox/articles/2026-06-25_Data_Visualization_With_Python.md` | Data Visualization With Python | 自动抓取 |

| `01_inbox/articles/2026-06-25_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

### 2026-06-25 12:00 后台维护（第2轮）

| 操作 | 详情 |
|:----|:------|
| 归档 | 01_inbox/articles/ 10 个文件 → archive/articles/2026-06-25/（均为已编译的 Python 文档） |
| 归档 | 01-收件箱/自动捕获/ 10 个文件 → archive/自动捕获/2026-06-25/ |
| 去重 | 删除 archive 中 19 个跨日期重复文件（06-24 vs 06-25）| 
| 概念检查 | Hermes-Agent.md 已含 06-25 hash 记录，无需补充 |
| 地图状态 | 07-地图/ 无需更新 |

最终状态：
- 01_inbox: 0 个待处理
- 01-收件箱: 全部清空
- archive 精简 19 个重复
- 02-笔记: 153 篇（不变）

| `01_inbox/articles/2026-06-25_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

### 自动入库 (2026-06-26)

| 文件 | 标题 | 来源 |
|:----|:----|:----|

| `01_inbox/articles/2026-06-26_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

### 2026-06-26 06:00 后台维护

| 操作 | 详情 |
|:----|:------|
| 概念补充 | Hermes-Agent.md 追加 06-25 第2轮 + 06-26 hash 变更记录 |
| 归档 | 01_inbox/articles/ 2 个文件 → archive/articles/2026-06-25/ + 2026-06-26/ |
| 去重 | 2 个 Hermes Agent 文件与已有概念笔记内容重复（仅 llms-full.txt hash 变化），合并为 hash 追踪记录 |
| 地图状态 | 07-地图/ 无需更新 — 同一来源增量 hash 变更，非新领域 |

最终状态：
- 01_inbox: 0 个待处理文件（已全部归档）
- 01-收件箱: 所有子目录均为空
- 02-笔记/概念/Hermes-Agent.md: 已追加 hash 记录
- 02-笔记 合计 155 个文件（实体 64 + 概念 39 + 方法 51）
- 07-地图/ 两份地图无变更

| `01_inbox/articles/2026-06-26_Quickstart.md` | Quickstart¶ | 自动抓取 |

| `01_inbox/articles/2026-06-26_Tutorial.md` | Tutorial | 自动抓取 |

| `01_inbox/articles/2026-06-26_Getting_Started.md` | Getting Started¶ | 自动抓取 |

| `01_inbox/articles/2026-06-26_10_minutes_to_pandas.md` | 10 minutes to pandas# | 自动抓取 |

| `01_inbox/articles/2026-06-26_Quick_start_guide.md` | Quick start guide# | 自动抓取 |

| `01_inbox/articles/2026-06-26_csv_CSV_File_Reading_and_Writing.md` | `csv` — CSV File Reading and Writing¶ | 自动抓取 |

| `01_inbox/articles/2026-06-26_json_JSON_encoder_and_decoder.md` | `json` — JSON encoder and decoder¶ | 自动抓取 |

| `01_inbox/articles/2026-06-26_pathlib_Object_oriented_filesystem_paths.md` | `pathlib` — Object-oriented filesystem paths¶ | 自动抓取 |

| `01_inbox/articles/2026-06-26_Data_Visualization_With_Python.md` | Data Visualization With Python | 自动抓取 |

| `01_inbox/articles/2026-06-26_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-06-26_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

### 自动入库 (2026-06-27)

| 文件 | 标题 | 来源 |
|:----|:----|:----|

| `01_inbox/articles/2026-06-27_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-06-27_Quickstart.md` | Quickstart¶ | 自动抓取 |

| `01_inbox/articles/2026-06-27_Tutorial.md` | Tutorial | 自动抓取 |

| `01_inbox/articles/2026-06-27_Getting_Started.md` | Getting Started¶ | 自动抓取 |

| `01_inbox/articles/2026-06-27_10_minutes_to_pandas.md` | 10 minutes to pandas# | 自动抓取 |

| `01_inbox/articles/2026-06-27_Quick_start_guide.md` | Quick start guide# | 自动抓取 |

| `01_inbox/articles/2026-06-27_csv_CSV_File_Reading_and_Writing.md` | `csv` — CSV File Reading and Writing¶ | 自动抓取 |

| `01_inbox/articles/2026-06-27_json_JSON_encoder_and_decoder.md` | `json` — JSON encoder and decoder¶ | 自动抓取 |

| `01_inbox/articles/2026-06-27_pathlib_Object_oriented_filesystem_paths.md` | `pathlib` — Object-oriented filesystem paths¶ | 自动抓取 |

| `01_inbox/articles/2026-06-27_Data_Visualization_With_Python.md` | Data Visualization With Python | 自动抓取 |

| `01_inbox/articles/2026-06-27_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

### 2026-06-27 12:10 后台维护

| 操作 | 详情 |
|:----|:------|
| 编译 | 01_inbox/articles/ 20 个文件 + 01-收件箱/自动捕获/ 20 个文件 → 学习要点 10 个已更新到 02-笔记/实体/ |
| 归档 | 01_inbox/articles/ 20 个文件 → archive/articles/2026-06-26/ + 2026-06-27/ |
| 归档 | 01-收件箱/自动捕获/ 20 个文件 → archive/自动捕获/2026-06-26/ + 2026-06-27/ |
| 概念补充 | Hermes-Agent.md 追加 06-26 第2轮 + 06-27 llms-full.txt hash 变更记录 |
| 去重 | 9 个 Python 文档跨日期完全重复（06-26 vs 06-27 相同大小），内容已被已有笔记覆盖；20 个跨目录重复（01-收件箱 vs 01_inbox 完全相同） |
| 地图状态 | 07-地图/ 两份地图均无需更新 — 同一来源增量 hash 变更，非新领域 |

最终状态：
- 01_inbox: 0 个待处理文件（已全部归档）
- 01-收件箱: 所有子目录均为空
- 02-笔记/概念/Hermes-Agent.md: 已追加 06-26 第2轮 + 06-27 hash 记录
- 02-笔记 合计 155 个文件（实体 64 + 概念 39 + 方法 51 + 架构 1）
- 07-地图/ 两份地图无变更


| `01_inbox/articles/2026-06-27_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

### 自动入库 (2026-06-28)

| 文件 | 标题 | 来源 |
|:----|:----|:----|

| `01_inbox/articles/2026-06-28_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

### 2026-06-28 06:00 后台维护

| 操作 | 详情 |
|:----|:------|
| 编译 | auto-compile-enhanced.py 扫 30 文件，677 总处理 — 无新学习要点（ChromaDB learning-points 842 块不变） |
| 归档 | `01_inbox/articles/2026-06-28_Hermes_Agent.md` → `archive/articles/2026-06-28/` |
| 去重 | 06-28 捕获与 06-27 第2轮捕获 llms-full.txt hash 完全相同（`f23a0121...`），无新内容；02-笔记 无新增重复 |
| 概念笔记 | Hermes-Agent.md 已记录 06-27 第2轮 hash，06-28 相同 hash，无需更新 |
| 地图状态 | 07-地图/ 两份地图无需更新 — hash 相同，非新领域 |

最终状态：
- 01_inbox: 0 个待处理文件（已全部归档）
- 01-收件箱: 所有子目录均为空
- 02-笔记 合计 155 个文件（实体 64 + 概念 39 + 方法 51 + 架构 1）
- 07-地图/ 两份地图无变更

| `01_inbox/articles/2026-06-28_Quickstart.md` | Quickstart¶ | 自动抓取 |

| `01_inbox/articles/2026-06-28_Tutorial.md` | Tutorial | 自动抓取 |

| `01_inbox/articles/2026-06-28_Getting_Started.md` | Getting Started¶ | 自动抓取 |

| `01_inbox/articles/2026-06-28_10_minutes_to_pandas.md` | 10 minutes to pandas# | 自动抓取 |

| `01_inbox/articles/2026-06-28_Quick_start_guide.md` | Quick start guide# | 自动抓取 |

| `01_inbox/articles/2026-06-28_csv_CSV_File_Reading_and_Writing.md` | `csv` — CSV File Reading and Writing¶ | 自动抓取 |

| `01_inbox/articles/2026-06-28_json_JSON_encoder_and_decoder.md` | `json` — JSON encoder and decoder¶ | 自动抓取 |

| `01_inbox/articles/2026-06-28_pathlib_Object_oriented_filesystem_paths.md` | `pathlib` — Object-oriented filesystem paths¶ | 自动抓取 |

| `01_inbox/articles/2026-06-28_Data_Visualization_With_Python.md` | Data Visualization With Python | 自动抓取 |

| `01_inbox/articles/2026-06-28_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-06-28_Quickstart.md` | Quickstart¶ | 自动抓取 |

| `01_inbox/articles/2026-06-28_Tutorial.md` | Tutorial | 自动抓取 |

| `01_inbox/articles/2026-06-28_Getting_Started.md` | Getting Started¶ | 自动抓取 |

| `01_inbox/articles/2026-06-28_10_minutes_to_pandas.md` | 10 minutes to pandas# | 自动抓取 |

| `01_inbox/articles/2026-06-28_Quick_start_guide.md` | Quick start guide# | 自动抓取 |

| `01_inbox/articles/2026-06-28_csv_CSV_File_Reading_and_Writing.md` | `csv` — CSV File Reading and Writing¶ | 自动抓取 |

| `01_inbox/articles/2026-06-28_json_JSON_encoder_and_decoder.md` | `json` — JSON encoder and decoder¶ | 自动抓取 |

| `01_inbox/articles/2026-06-28_pathlib_Object_oriented_filesystem_paths.md` | `pathlib` — Object-oriented filesystem paths¶ | 自动抓取 |

| `01_inbox/articles/2026-06-28_Data_Visualization_With_Python.md` | Data Visualization With Python | 自动抓取 |

| `01_inbox/articles/2026-06-28_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-06-28_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

### 自动入库 (2026-06-29)

| 文件 | 标题 | 来源 |
|:----|:----|:----|

| `01_inbox/articles/2026-06-29_Quickstart.md` | Quickstart¶ | 自动抓取 |

| `01_inbox/articles/2026-06-29_Tutorial.md` | Tutorial | 自动抓取 |

| `01_inbox/articles/2026-06-29_Getting_Started.md` | Getting Started¶ | 自动抓取 |

| `01_inbox/articles/2026-06-29_10_minutes_to_pandas.md` | 10 minutes to pandas# | 自动抓取 |

| `01_inbox/articles/2026-06-29_Quick_start_guide.md` | Quick start guide# | 自动抓取 |

| `01_inbox/articles/2026-06-29_csv_CSV_File_Reading_and_Writing.md` | `csv` — CSV File Reading and Writing¶ | 自动抓取 |

| `01_inbox/articles/2026-06-29_json_JSON_encoder_and_decoder.md` | `json` — JSON encoder and decoder¶ | 自动抓取 |

| `01_inbox/articles/2026-06-29_pathlib_Object_oriented_filesystem_paths.md` | `pathlib` — Object-oriented filesystem paths¶ | 自动抓取 |

| `01_inbox/articles/2026-06-29_Data_Visualization_With_Python.md` | Data Visualization With Python | 自动抓取 |

| `01_inbox/articles/2026-06-29_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-06-29_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-06-29_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

### 2026-06-29 20:00 后台维护

| 操作 | 详情 |
|:----|:------|
| 编译 | 01_inbox/articles/ 最新 Hermes Agent 第3轮捕获 (20:00, llms-full hash `1e45778b...`) — 同一来源 (hermes-agent.nousresearch.com/docs)，第3轮较第2轮 (`1db8e1c3...`) hash 再次变更，页面无结构性变化 |
| 概念笔记补充 | Hermes-Agent.md 追加 2026-06-29 第3轮 hash 变更记录 |
| 归档 | 01-收件箱/自动学习/ 6 个 Hermes 站点学习文件 → 99-归档/2026-06-29/自动学习/ |
| 归档 | 01_inbox/articles/ Hermes Agent 第3轮捕获 → 99-归档/2026-06-29/ |
| 碎片清理 | 删除 02-笔记/实体/ 下 10 个低质量自动生成的「学习要点」空壳文件（~1000-1200 bytes，无实质内容） |
| 空壳检查 | 02-笔记/ 无其他 < 500 bytes 空壳文件 |
| 去重检查 | 01-收件箱/archive/自动捕获/ 与 01_inbox/archive/articles/ 文件内容不同（不同时间抓取），非重复；02-笔记/ 无精确重复 |
| 地图检查 | 07-地图/AI技术地图 + 办公自动化地图 — 已有覆盖，无需更新（routine hash 变更） |

最终状态：
- 01-收件箱/自动学习: 0（已归档到 99-归档）
- 01-收件箱/自动捕获: 0（active inbox 空）
- 01_inbox/articles: 0（已归档到 99-归档）
- 02-笔记/概念/Hermes-Agent.md: 已追加 06-29 第3轮 hash 记录
- 02-笔记 合计 149 个文件（实体 54 + 概念 39 + 方法 51 + 架构 1）— 清理了 10 个空壳
- 07-地图/ 两份地图无变更

### 自动入库 (2026-06-30)

| 文件 | 标题 | 来源 |
|:----|:----|:----|

| `01_inbox/articles/2026-06-30_Quickstart.md` | Quickstart¶ | 自动抓取 |

| `01_inbox/articles/2026-06-30_Tutorial.md` | Tutorial | 自动抓取 |

| `01_inbox/articles/2026-06-30_Getting_Started.md` | Getting Started¶ | 自动抓取 |

| `01_inbox/articles/2026-06-30_10_minutes_to_pandas.md` | 10 minutes to pandas# | 自动抓取 |

| `01_inbox/articles/2026-06-30_Quick_start_guide.md` | Quick start guide# | 自动抓取 |

| `01_inbox/articles/2026-06-30_csv_CSV_File_Reading_and_Writing.md` | `csv` — CSV File Reading and Writing¶ | 自动抓取 |

| `01_inbox/articles/2026-06-30_json_JSON_encoder_and_decoder.md` | `json` — JSON encoder and decoder¶ | 自动抓取 |

| `01_inbox/articles/2026-06-30_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-06-30_pathlib_Object_oriented_filesystem_paths.md` | `pathlib` — Object-oriented filesystem paths¶ | 自动抓取 |

| `01_inbox/articles/2026-06-30_Data_Visualization_With_Python.md` | Data Visualization With Python | 自动抓取 |

| `01_inbox/articles/2026-06-30_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-06-30_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

### 自动入库 (2026-07-01)

| 文件 | 标题 | 来源 |
|:----|:----|:----|

| `01_inbox/articles/2026-07-01_Quickstart.md` | Quickstart¶ | 自动抓取 |

| `01_inbox/articles/2026-07-01_Tutorial.md` | Tutorial | 自动抓取 |

| `01_inbox/articles/2026-07-01_Getting_Started.md` | Getting Started¶ | 自动抓取 |

| `01_inbox/articles/2026-07-01_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-07-01_10_minutes_to_pandas.md` | 10 minutes to pandas# | 自动抓取 |

| `01_inbox/articles/2026-07-01_Quick_start_guide.md` | Quick start guide# | 自动抓取 |

| `01_inbox/articles/2026-07-01_csv_CSV_File_Reading_and_Writing.md` | `csv` — CSV File Reading and Writing¶ | 自动抓取 |

| `01_inbox/articles/2026-07-01_json_JSON_encoder_and_decoder.md` | `json` — JSON encoder and decoder¶ | 自动抓取 |

| `01_inbox/articles/2026-07-01_pathlib_Object_oriented_filesystem_paths.md` | `pathlib` — Object-oriented filesystem paths¶ | 自动抓取 |

| `01_inbox/articles/2026-07-01_Data_Visualization_With_Python.md` | Data Visualization With Python | 自动抓取 |

| `01_inbox/articles/2026-07-01_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-07-01_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

### 自动入库 (2026-07-02)

| 文件 | 标题 | 来源 |
|:----|:----|:----|

| `01_inbox/articles/2026-07-02_Quickstart.md` | Quickstart¶ | 自动抓取 |

| `01_inbox/articles/2026-07-02_Tutorial.md` | Tutorial | 自动抓取 |

| `01_inbox/articles/2026-07-02_Getting_Started.md` | Getting Started¶ | 自动抓取 |

| `01_inbox/articles/2026-07-02_10_minutes_to_pandas.md` | 10 minutes to pandas# | 自动抓取 |

| `01_inbox/articles/2026-07-02_Quick_start_guide.md` | Quick start guide# | 自动抓取 |

| `01_inbox/articles/2026-07-02_csv_CSV_File_Reading_and_Writing.md` | `csv` — CSV File Reading and Writing¶ | 自动抓取 |

| `01_inbox/articles/2026-07-02_json_JSON_encoder_and_decoder.md` | `json` — JSON encoder and decoder¶ | 自动抓取 |

| `01_inbox/articles/2026-07-02_pathlib_Object_oriented_filesystem_paths.md` | `pathlib` — Object-oriented filesystem paths¶ | 自动抓取 |

| `01_inbox/articles/2026-07-02_Data_Visualization_With_Python.md` | Data Visualization With Python | 自动抓取 |

| `01_inbox/articles/2026-07-02_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

### 2026-07-02 07:00 后台维护

| 操作 | 详情 |
|:----|:------|
| 编译 | daily-capture.sh 已运行 — 9 个站点成功 / 3 个失败（Obsidian 重定向 + python-docx table 404）|
| 编译结果 | auto-compile-fast.py 扫描 10 个待编译文件，全部已存在（⏭️跳过），0 个新笔记创建 |
| 归档 | 01-收件箱/自动捕获/ 9 个文件 → archive/自动捕获/2026-07-02/ |
| 归档 | 01_inbox/articles/ 9 个今日新文件 + 1 个 07-01 残留 → archive/articles/2026-07-02/ + 2026-07-01/ |
| 概念补充 | Hermes-Agent.md 追加 07-02 hash 变更记录: `86aa311e...` → `23221f7b...` |
| 去重检查 | Quickstart.md / Tutorial.md 各在实体/和方法/下存在同名文件，但内容不同（实体为短参考，方法为完整教程），非重复 |
| 地图检查 | 07-地图/ 两份地图均为现有覆盖 — 例行 re-capture，无新领域知识，无需更新 |

最终状态：
- 01-收件箱: 所有子目录均为空（9 个文件已归档）
- 01_inbox: 所有子目录均为空（10 个文件已归档）
- 02-笔记/概念/Hermes-Agent.md: 已追加 07-02 hash 记录
- 02-笔记 合计 145 个文件（实体 54 + 概念 39 + 方法 51 + 架构 1）
- 07-地图/ 两份地图无变更

| `01_inbox/articles/2026-07-02_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-07-02_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

### 自动入库 (2026-07-03)

| 文件 | 标题 | 来源 |
|:----|:----|:----|

| `01_inbox/articles/2026-07-03_Quickstart.md` | Quickstart¶ | 自动抓取 |

| `01_inbox/articles/2026-07-03_Tutorial.md` | Tutorial | 自动抓取 |

| `01_inbox/articles/2026-07-03_Getting_Started.md` | Getting Started¶ | 自动抓取 |

| `01_inbox/articles/2026-07-03_10_minutes_to_pandas.md` | 10 minutes to pandas# | 自动抓取 |

| `01_inbox/articles/2026-07-03_Quick_start_guide.md` | Quick start guide# | 自动抓取 |

| `01_inbox/articles/2026-07-03_csv_CSV_File_Reading_and_Writing.md` | `csv` — CSV File Reading and Writing¶ | 自动抓取 |

| `01_inbox/articles/2026-07-03_json_JSON_encoder_and_decoder.md` | `json` — JSON encoder and decoder¶ | 自动抓取 |

| `01_inbox/articles/2026-07-03_pathlib_Object_oriented_filesystem_paths.md` | `pathlib` — Object-oriented filesystem paths¶ | 自动抓取 |

| `01_inbox/articles/2026-07-03_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-07-03_Data_Visualization_With_Python.md` | Data Visualization With Python | 自动抓取 |

| `01_inbox/articles/2026-07-03_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-07-03_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

### 自动入库 (2026-07-04)

| 文件 | 标题 | 来源 |
|:----|:----|:----|

| `01_inbox/articles/2026-07-04_Quickstart.md` | Quickstart¶ | 自动抓取 |

| `01_inbox/articles/2026-07-04_Tutorial.md` | Tutorial | 自动抓取 |

| `01_inbox/articles/2026-07-04_Getting_Started.md` | Getting Started¶ | 自动抓取 |

| `01_inbox/articles/2026-07-04_10_minutes_to_pandas.md` | 10 minutes to pandas# | 自动抓取 |

| `01_inbox/articles/2026-07-04_Quick_start_guide.md` | Quick start guide# | 自动抓取 |

| `01_inbox/articles/2026-07-04_csv_CSV_File_Reading_and_Writing.md` | `csv` — CSV File Reading and Writing¶ | 自动抓取 |

| `01_inbox/articles/2026-07-04_json_JSON_encoder_and_decoder.md` | `json` — JSON encoder and decoder¶ | 自动抓取 |

| `01_inbox/articles/2026-07-04_pathlib_Object_oriented_filesystem_paths.md` | `pathlib` — Object-oriented filesystem paths¶ | 自动抓取 |

| `01_inbox/articles/2026-07-04_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-07-04_Data_Visualization_With_Python.md` | Data Visualization With Python | 自动抓取 |

| `01_inbox/articles/2026-07-04_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-07-04_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

### 自动入库 (2026-07-05)

| 文件 | 标题 | 来源 |
|:----|:----|:----|

| `01_inbox/articles/2026-07-05_Quickstart.md` | Quickstart¶ | 自动抓取 |

| `01_inbox/articles/2026-07-05_Tutorial.md` | Tutorial | 自动抓取 |

| `01_inbox/articles/2026-07-05_Getting_Started.md` | Getting Started¶ | 自动抓取 |

| `01_inbox/articles/2026-07-05_10_minutes_to_pandas.md` | 10 minutes to pandas# | 自动抓取 |

| `01_inbox/articles/2026-07-05_Quick_start_guide.md` | Quick start guide# | 自动抓取 |

| `01_inbox/articles/2026-07-05_csv_CSV_File_Reading_and_Writing.md` | `csv` — CSV File Reading and Writing¶ | 自动抓取 |

| `01_inbox/articles/2026-07-05_json_JSON_encoder_and_decoder.md` | `json` — JSON encoder and decoder¶ | 自动抓取 |

| `01_inbox/articles/2026-07-05_pathlib_Object_oriented_filesystem_paths.md` | `pathlib` — Object-oriented filesystem paths¶ | 自动抓取 |

| `01_inbox/articles/2026-07-05_Data_Visualization_With_Python.md` | Data Visualization With Python | 自动抓取 |

| `01_inbox/articles/2026-07-05_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-07-05_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-07-05_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

### 自动入库 (2026-07-06)

| 文件 | 标题 | 来源 |
|:----|:----|:----|

| `01_inbox/articles/2026-07-06_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-07-06_Quickstart.md` | Quickstart¶ | 自动抓取 |

| `01_inbox/articles/2026-07-06_Tutorial.md` | Tutorial | 自动抓取 |

| `01_inbox/articles/2026-07-06_Getting_Started.md` | Getting Started¶ | 自动抓取 |

| `01_inbox/articles/2026-07-06_10_minutes_to_pandas.md` | 10 minutes to pandas# | 自动抓取 |

| `01_inbox/articles/2026-07-06_Quick_start_guide.md` | Quick start guide# | 自动抓取 |

| `01_inbox/articles/2026-07-06_csv_CSV_File_Reading_and_Writing.md` | `csv` — CSV File Reading and Writing¶ | 自动抓取 |

| `01_inbox/articles/2026-07-06_json_JSON_encoder_and_decoder.md` | `json` — JSON encoder and decoder¶ | 自动抓取 |

| `01_inbox/articles/2026-07-06_pathlib_Object_oriented_filesystem_paths.md` | `pathlib` — Object-oriented filesystem paths¶ | 自动抓取 |

| `01_inbox/articles/2026-07-06_Data_Visualization_With_Python.md` | Data Visualization With Python | 自动抓取 |

| `01_inbox/articles/2026-07-06_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-07-06_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

### 自动入库 (2026-07-07)

| 文件 | 标题 | 来源 |
|:----|:----|:----|

| `01_inbox/articles/2026-07-07_Quickstart.md` | Quickstart¶ | 自动抓取 |

| `01_inbox/articles/2026-07-07_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-07-07_Tutorial.md` | Tutorial | 自动抓取 |

| `01_inbox/articles/2026-07-07_Getting_Started.md` | Getting Started¶ | 自动抓取 |

| `01_inbox/articles/2026-07-07_10_minutes_to_pandas.md` | 10 minutes to pandas# | 自动抓取 |

| `01_inbox/articles/2026-07-07_Quick_start_guide.md` | Quick start guide# | 自动抓取 |

| `01_inbox/articles/2026-07-07_csv_CSV_File_Reading_and_Writing.md` | `csv` — CSV File Reading and Writing¶ | 自动抓取 |

| `01_inbox/articles/2026-07-07_json_JSON_encoder_and_decoder.md` | `json` — JSON encoder and decoder¶ | 自动抓取 |

| `01_inbox/articles/2026-07-07_pathlib_Object_oriented_filesystem_paths.md` | `pathlib` — Object-oriented filesystem paths¶ | 自动抓取 |

| `01_inbox/articles/2026-07-07_Data_Visualization_With_Python.md` | Data Visualization With Python | 自动抓取 |

| `01_inbox/articles/2026-07-07_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-07-07_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

### 自动入库 (2026-07-08)

| 文件 | 标题 | 来源 |
|:----|:----|:----|

| `01_inbox/articles/2026-07-08_Quickstart.md` | Quickstart¶ | 自动抓取 |

| `01_inbox/articles/2026-07-08_Tutorial.md` | Tutorial | 自动抓取 |

| `01_inbox/articles/2026-07-08_Getting_Started.md` | Getting Started¶ | 自动抓取 |

| `01_inbox/articles/2026-07-08_10_minutes_to_pandas.md` | 10 minutes to pandas# | 自动抓取 |

| `01_inbox/articles/2026-07-08_Quick_start_guide.md` | Quick start guide# | 自动抓取 |

| `01_inbox/articles/2026-07-08_csv_CSV_File_Reading_and_Writing.md` | `csv` — CSV File Reading and Writing¶ | 自动抓取 |

| `01_inbox/articles/2026-07-08_json_JSON_encoder_and_decoder.md` | `json` — JSON encoder and decoder¶ | 自动抓取 |

| `01_inbox/articles/2026-07-08_pathlib_Object_oriented_filesystem_paths.md` | `pathlib` — Object-oriented filesystem paths¶ | 自动抓取 |

| `01_inbox/articles/2026-07-08_Data_Visualization_With_Python.md` | Data Visualization With Python | 自动抓取 |

| `01_inbox/articles/2026-07-08_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-07-08_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-07-08_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

### 自动入库 (2026-07-09)

| 文件 | 标题 | 来源 |
|:----|:----|:----|

| `01_inbox/articles/2026-07-09_Quickstart.md` | Quickstart¶ | 自动抓取 |

| `01_inbox/articles/2026-07-09_Tutorial.md` | Tutorial | 自动抓取 |

| `01_inbox/articles/2026-07-09_Getting_Started.md` | Getting Started¶ | 自动抓取 |

| `01_inbox/articles/2026-07-09_10_minutes_to_pandas.md` | 10 minutes to pandas# | 自动抓取 |

| `01_inbox/articles/2026-07-09_Quick_start_guide.md` | Quick start guide# | 自动抓取 |

| `01_inbox/articles/2026-07-09_csv_CSV_File_Reading_and_Writing.md` | `csv` — CSV File Reading and Writing¶ | 自动抓取 |

| `01_inbox/articles/2026-07-09_json_JSON_encoder_and_decoder.md` | `json` — JSON encoder and decoder¶ | 自动抓取 |

| `01_inbox/articles/2026-07-09_pathlib_Object_oriented_filesystem_paths.md` | `pathlib` — Object-oriented filesystem paths¶ | 自动抓取 |

| `01_inbox/articles/2026-07-09_Data_Visualization_With_Python.md` | Data Visualization With Python | 自动抓取 |

| `01_inbox/articles/2026-07-09_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-07-09_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-07-09_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

### 自动入库 (2026-07-10)

| 文件 | 标题 | 来源 |
|:----|:----|:----|

| `01_inbox/articles/2026-07-10_Quickstart.md` | Quickstart¶ | 自动抓取 |

| `01_inbox/articles/2026-07-10_Tutorial.md` | Tutorial | 自动抓取 |

| `01_inbox/articles/2026-07-10_Getting_Started.md` | Getting Started¶ | 自动抓取 |

| `01_inbox/articles/2026-07-10_10_minutes_to_pandas.md` | 10 minutes to pandas# | 自动抓取 |

| `01_inbox/articles/2026-07-10_Quick_start_guide.md` | Quick start guide# | 自动抓取 |

| `01_inbox/articles/2026-07-10_csv_CSV_File_Reading_and_Writing.md` | `csv` — CSV File Reading and Writing¶ | 自动抓取 |

| `01_inbox/articles/2026-07-10_json_JSON_encoder_and_decoder.md` | `json` — JSON encoder and decoder¶ | 自动抓取 |

| `01_inbox/articles/2026-07-10_pathlib_Object_oriented_filesystem_paths.md` | `pathlib` — Object-oriented filesystem paths¶ | 自动抓取 |

| `01_inbox/articles/2026-07-10_Data_Visualization_With_Python.md` | Data Visualization With Python | 自动抓取 |

| `01_inbox/articles/2026-07-10_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-07-10_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-07-10_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

### 自动入库 (2026-07-11)

| 文件 | 标题 | 来源 |
|:----|:----|:----|

| `01_inbox/articles/2026-07-11_Quickstart.md` | Quickstart¶ | 自动抓取 |

| `01_inbox/articles/2026-07-11_Tutorial.md` | Tutorial | 自动抓取 |

| `01_inbox/articles/2026-07-11_Getting_Started.md` | Getting Started¶ | 自动抓取 |

| `01_inbox/articles/2026-07-11_10_minutes_to_pandas.md` | 10 minutes to pandas# | 自动抓取 |

| `01_inbox/articles/2026-07-11_Quick_start_guide.md` | Quick start guide# | 自动抓取 |

| `01_inbox/articles/2026-07-11_csv_CSV_File_Reading_and_Writing.md` | `csv` — CSV File Reading and Writing¶ | 自动抓取 |

| `01_inbox/articles/2026-07-11_json_JSON_encoder_and_decoder.md` | `json` — JSON encoder and decoder¶ | 自动抓取 |

| `01_inbox/articles/2026-07-11_pathlib_Object_oriented_filesystem_paths.md` | `pathlib` — Object-oriented filesystem paths¶ | 自动抓取 |

| `01_inbox/articles/2026-07-11_Data_Visualization_With_Python.md` | Data Visualization With Python | 自动抓取 |

| `01_inbox/articles/2026-07-11_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-07-11_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-07-11_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

### 自动入库 (2026-07-12)

| 文件 | 标题 | 来源 |
|:----|:----|:----|

| `01_inbox/articles/2026-07-12_Quickstart.md` | Quickstart¶ | 自动抓取 |

| `01_inbox/articles/2026-07-12_Tutorial.md` | Tutorial | 自动抓取 |

| `01_inbox/articles/2026-07-12_Getting_Started.md` | Getting Started¶ | 自动抓取 |

| `01_inbox/articles/2026-07-12_10_minutes_to_pandas.md` | 10 minutes to pandas# | 自动抓取 |

| `01_inbox/articles/2026-07-12_Quick_start_guide.md` | Quick start guide# | 自动抓取 |

| `01_inbox/articles/2026-07-12_csv_CSV_File_Reading_and_Writing.md` | `csv` — CSV File Reading and Writing¶ | 自动抓取 |

| `01_inbox/articles/2026-07-12_json_JSON_encoder_and_decoder.md` | `json` — JSON encoder and decoder¶ | 自动抓取 |

| `01_inbox/articles/2026-07-12_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-07-12_pathlib_Object_oriented_filesystem_paths.md` | `pathlib` — Object-oriented filesystem paths¶ | 自动抓取 |

| `01_inbox/articles/2026-07-12_Data_Visualization_With_Python.md` | Data Visualization With Python | 自动抓取 |

| `01_inbox/articles/2026-07-12_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-07-12_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

### 自动入库 (2026-07-13)

| 文件 | 标题 | 来源 |
|:----|:----|:----|

| `01_inbox/articles/2026-07-13_Quickstart.md` | Quickstart¶ | 自动抓取 |

| `01_inbox/articles/2026-07-13_Tutorial.md` | Tutorial | 自动抓取 |

| `01_inbox/articles/2026-07-13_Getting_Started.md` | Getting Started¶ | 自动抓取 |

| `01_inbox/articles/2026-07-13_10_minutes_to_pandas.md` | 10 minutes to pandas# | 自动抓取 |

| `01_inbox/articles/2026-07-13_Quick_start_guide.md` | Quick start guide# | 自动抓取 |

| `01_inbox/articles/2026-07-13_csv_CSV_File_Reading_and_Writing.md` | `csv` — CSV File Reading and Writing¶ | 自动抓取 |

| `01_inbox/articles/2026-07-13_json_JSON_encoder_and_decoder.md` | `json` — JSON encoder and decoder¶ | 自动抓取 |

| `01_inbox/articles/2026-07-13_pathlib_Object_oriented_filesystem_paths.md` | `pathlib` — Object-oriented filesystem paths¶ | 自动抓取 |

| `01_inbox/articles/2026-07-13_Data_Visualization_With_Python.md` | Data Visualization With Python | 自动抓取 |

| `01_inbox/articles/2026-07-13_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-07-13_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

### 自动入库 (2026-07-14)

| 文件 | 标题 | 来源 |
|:----|:----|:----|

| `01_inbox/articles/2026-07-14_Quickstart.md` | Quickstart¶ | 自动抓取 |

| `01_inbox/articles/2026-07-14_Tutorial.md` | Tutorial | 自动抓取 |

| `01_inbox/articles/2026-07-14_Getting_Started.md` | Getting Started¶ | 自动抓取 |

| `01_inbox/articles/2026-07-14_10_minutes_to_pandas.md` | 10 minutes to pandas# | 自动抓取 |

| `01_inbox/articles/2026-07-14_Quick_start_guide.md` | Quick start guide# | 自动抓取 |

| `01_inbox/articles/2026-07-14_csv_CSV_File_Reading_and_Writing.md` | `csv` — CSV File Reading and Writing¶ | 自动抓取 |

| `01_inbox/articles/2026-07-14_json_JSON_encoder_and_decoder.md` | `json` — JSON encoder and decoder¶ | 自动抓取 |

| `01_inbox/articles/2026-07-14_pathlib_Object_oriented_filesystem_paths.md` | `pathlib` — Object-oriented filesystem paths¶ | 自动抓取 |

| `01_inbox/articles/2026-07-14_Data_Visualization_With_Python.md` | Data Visualization With Python | 自动抓取 |

| `01_inbox/articles/2026-07-14_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-07-14_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

### 2026-07-14 19:00 知识库维护（第3轮 — 置信度体系上线）

| 操作 | 详情 |
|:----|:------|
| 架构更新 | 知识库架构.md 新增 `confidence`/`superseded_by`/`last_confirmed` 字段；`status` 新增 `needs-review`/`superseded` |
| 过期标注 | 批量处理 144 篇 >30天未更新笔记 → `status: needs-review` + `confidence: medium` |
| 结晶摘要 | 07-地图/结晶摘要-2026-07-14.md — 记录本轮工资管理系统优化+知识库置信度体系上线 |
| 验证 | 31页PDF连续编号✅，导出Excel冻结表头+筛选✅，导入双保险提示✅ |


| `01_inbox/articles/2026-07-14_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

### 2026-07-14 19:30 知识库维护（第4轮 — 工资系统经验沉淀）

| 操作 | 详情 |
|:----|:------|
| 新笔记 | **5 篇** — 方法x3 + 概念x1 + 实体x1 |
| 方法 | Flask工资系统开发、WeasyPrint-PDF生成配置、openpyxl-企业导出优化 |
| 概念 | 工资系统安全架构 |
| 实体 | 工资管理系统 |
| 双链 | 5 篇笔记互相链接 14 个引用，形成完整知识簇 |
| 验证 | 组织完整性：方法/概念/实体/地图 四层覆盖 ✅ |


### 2026-07-14 20:00 知识库维护（第5轮 — Memory OS 文章入库）

| 操作 | 详情 |
|:----|:------|
| 来源归档 | 01_inbox/archive/articles/2026-07-14/Memory-OS-Hermes本地长期记忆.md |
| 概念笔记 | 02-笔记/概念/Memory-OS本地长期记忆.md — 7层架构 + 精准注入 + Ground Truth |
| 知识库启发 | 引入 trust scoring、semantic dedup、Ground Truth 层列为下次改进方向 |


### 2026-07-14 20:30 知识库升级 — Ground Truth 层上线 + trust_score 自动衰减

| 操作 | 详情 |
|:----|:------|
| 新增 00-系统/ | SOUL.md + RULEBOOK.md + GROUND_TRUTHS.md — Ground Truth 三层架构 |
| trust_score | 数值化置信度体系上线，0.0~1.0 自动衰减 |
| 衰减脚本 | trust-decay.py 每天6:30自动运行，>30天降权，>90天归档 |
| cron 更新 | 新增 `30 6 * * * trust-decay.py` |
| 架构更新 | 知识库架构.md — 新增 contradiction_with/priority/trust_score 字段 |
| 生命周期 | 新增 needs-review / superseded 阶段，去除 frozen |
| 知识簇 | 工资系统 5 篇 + Memory OS 1 篇 + Ground Truth 3 篇 = 9 篇今日新增 |

最终状态：
- 00-系统/ 3 文件（SOUL + RULEBOOK + GROUND_TRUTHS）✅ 永不衰减
- 02-笔记 159 篇（方法51 + 概念41 + 实体67）
- trust_decay cron 已就绪 ✅
- 知识库 834 个 .md 文件

### 2026-07-14 20:45 知识库维护（第6轮 — LLM Wiki 文章入库）

| 操作 | 详情 |
|:----|:------|
| 来源归档 | 01_inbox/archive/articles/2026-07-14/LLM-Wiki-知识管理三层架构.md |
| 概念笔记 | 02-笔记/概念/LLM-Wiki三层架构.md — RAG vs LLM Wiki 对比 + 三层架构 + 三个习惯 |
| 对照验证 | 我们的知识库（raw/wiki/agents）与 LLM Wiki 三层架构完全对齐 ✅ |
| 差距 | 交叉引用习惯需加强、结晶摘要刚起步 |


### 自动入库 (2026-07-15)

| 文件 | 标题 | 来源 |
|:----|:----|:----|

| `01_inbox/articles/2026-07-15_Quickstart.md` | Quickstart¶ | 自动抓取 |

| `01_inbox/articles/2026-07-15_Tutorial.md` | Tutorial | 自动抓取 |

| `01_inbox/articles/2026-07-15_Getting_Started.md` | Getting Started¶ | 自动抓取 |

| `01_inbox/articles/2026-07-15_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-07-15_10_minutes_to_pandas.md` | 10 minutes to pandas# | 自动抓取 |

| `01_inbox/articles/2026-07-15_Quick_start_guide.md` | Quick start guide# | 自动抓取 |

| `01_inbox/articles/2026-07-15_csv_CSV_File_Reading_and_Writing.md` | `csv` — CSV File Reading and Writing¶ | 自动抓取 |

| `01_inbox/articles/2026-07-15_json_JSON_encoder_and_decoder.md` | `json` — JSON encoder and decoder¶ | 自动抓取 |

| `01_inbox/articles/2026-07-15_pathlib_Object_oriented_filesystem_paths.md` | `pathlib` — Object-oriented filesystem paths¶ | 自动抓取 |

| `01_inbox/articles/2026-07-15_Data_Visualization_With_Python.md` | Data Visualization With Python | 自动抓取 |

| `01_inbox/articles/2026-07-15_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-07-15_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

### 自动入库 (2026-07-16)

| 文件 | 标题 | 来源 |
|:----|:----|:----|

| `01_inbox/articles/2026-07-16_Quickstart.md` | Quickstart¶ | 自动抓取 |

| `01_inbox/articles/2026-07-16_Tutorial.md` | Tutorial | 自动抓取 |

| `01_inbox/articles/2026-07-16_Getting_Started.md` | Getting Started¶ | 自动抓取 |

| `01_inbox/articles/2026-07-16_10_minutes_to_pandas.md` | 10 minutes to pandas# | 自动抓取 |

| `01_inbox/articles/2026-07-16_Quick_start_guide.md` | Quick start guide# | 自动抓取 |

| `01_inbox/articles/2026-07-16_csv_CSV_File_Reading_and_Writing.md` | `csv` — CSV File Reading and Writing¶ | 自动抓取 |

| `01_inbox/articles/2026-07-16_json_JSON_encoder_and_decoder.md` | `json` — JSON encoder and decoder¶ | 自动抓取 |

| `01_inbox/articles/2026-07-16_pathlib_Object_oriented_filesystem_paths.md` | `pathlib` — Object-oriented filesystem paths¶ | 自动抓取 |

| `01_inbox/articles/2026-07-16_Data_Visualization_With_Python.md` | Data Visualization With Python | 自动抓取 |

| `01_inbox/articles/2026-07-16_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

### 2026-07-16 07:11:43 后台维护

| 操作 | 详情 |
|:----|:------|
| 抓取 | 9 标准站 + 1 Hermes Agent 日捕获 — 9 标准文件与昨日尺寸完全一致（无内容变化）；3 失败（python-docx table 404、Obsidian help ×2） |
| 概念补充 | Hermes-Agent.md 追加 07-16 hash 变更：llms.txt 稳定（连续第12天 `96828202...`），llms-full.txt 从 `9a44b206...` → `9c18cca7...`；资源表 hash 已同步 |
| 归档 | 01-收件箱/自动捕获/ 9 文件 → archive/自动捕获/2026-07-16/ ✅ |
| 归档 | 01_inbox/articles/ 10 文件 → archive/articles/2026-07-16/ ✅ |
| 归档 | 01_inbox/已处理/ 1 遗留文件 → archive/articles/2026-07-16/ ✅ |
| 去重检查 | 02-笔记/ 无新精确重复；4 组跨目录标题重复属已知分工（Hermes Agent 实体/概念、Data Visualization 实体/概念、python-docx 实体/方法、Quick start guide 实体/实体），无需操作 |
| 学习要点 | 02-笔记/学习要点/ 为空（上次已批量清理） |
| 地图更新 | 无新实体/概念添加，routine re-capture 无需更新地图 |

最终状态：
- 01-收件箱/自动捕获: 空 ✅
- 01-收件箱/自动学习: 空 ✅
- 01-收件箱/文章: 空 ✅
- 01-收件箱/_from_user: 空 ✅
- 01-收件箱/已处理: 空 ✅
- 01_inbox/articles: 空 ✅
- 01_inbox/已处理: 空 ✅
- 01-收件箱/archive/自动捕获: 11 个日期目录（50 文件，新增 2026-07-16）
- 01_inbox/archive/articles: 23 个日期目录（95 文件，新增 2026-07-16）
- 02-笔记/概念/Hermes-Agent.md: 已追加 07-16 hash 记录，资源表已同步
- 02-笔记 合计 167 个文件（实体 71 + 概念 42 + 方法 54）
- 07-地图/ 无结构性变更
- .last-compile 已刷新

| `01_inbox/articles/2026-07-16_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-07-16_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

### 自动入库 (2026-07-17)

| 文件 | 标题 | 来源 |
|:----|:----|:----|

| `01_inbox/articles/2026-07-17_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-07-17_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-07-17_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

### 自动入库 (2026-07-18)

| 文件 | 标题 | 来源 |
|:----|:----|:----|

| `01_inbox/articles/2026-07-18_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-07-18_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-07-18_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

### 自动入库 (2026-07-19)

| 文件 | 标题 | 来源 |
|:----|:----|:----|

| `01_inbox/articles/2026-07-19_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-07-19_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-07-19_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

### 自动入库 (2026-07-20)

| 文件 | 标题 | 来源 |
|:----|:----|:----|

| `01_inbox/articles/2026-07-20_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-07-20_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-07-20_Hermes_Agent.md` | Hermes Agent | 自动抓取 |


### 2026-07-20 20:00 后台维护

| 操作 | 详情 |
|:----|:------|
| 编译 | 01_inbox/articles/ 1 个新文件 (Hermes Agent 2026-07-20 第3轮) — llms-full.txt hash 从 `3c60cae2...` 变更为 `dcf98e29...`（当日第3次部署，第12天），llms.txt `96828202...` 保持稳定（第 12 天），页面无结构性变化 |
| 实体补充 | 实体/Hermes_Agent.md: llms-full hash 同步至 `dcf98e29...`，资源表 hash 更新，追加 changelog 第3轮记录 |
| 归档 | 01_inbox/articles/2026-07-20_Hermes_Agent.md → archive/articles/2026-07-20/2026-07-20_Hermes_Agent_v3.md ✅ |
| 归档 | 01-收件箱/自动学习/ 6 个文件 → archive/自动学习/2026-07-20/（含 5 学习笔记 + 1 学习报告）✅ |
| 去重检查 | 02-笔记/ 无新精确重复（实体 52 + 概念 40 + 方法 50 = 142）；跨目录标题检查通过；所有小文件(<1KB)均为合法笔记，非 stub 草稿 |
| 地图检查 | 07-地图/ AI技术地图 + 办公自动化地图 — 已有覆盖，无需更新（routine re-capture，仅 llms-full hash 增量，无新实体/概念） |

最终状态：
- 01_inbox/articles: 0（已全部归档）✅
- 01-收件箱/所有子目录: 空 ✅
- 02-笔记 合计 142 个文件（实体 52 + 概念 40 + 方法 50）
- 01_inbox/archive/articles/2026-07-20/: 3 个文件（v1 + v2 + v3）
- 01-收件箱/archive/自动学习: 新增 2026-07-20（6 文件）
- 07-地图/ 3 个文件无变更
- .last-compile 已刷新

### 自动入库 (2026-07-21)

| 文件 | 标题 | 来源 |
|:----|:----|:----|

| `01_inbox/articles/2026-07-21_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-07-21_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-07-21_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

### 自动入库 (2026-07-22)

| 文件 | 标题 | 来源 |
|:----|:----|:----|

| `01_inbox/articles/2026-07-22_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-07-22_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-07-22_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

### 自动入库 (2026-07-23)

| 文件 | 标题 | 来源 |
|:----|:----|:----|

| `01_inbox/articles/2026-07-23_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-07-23_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-07-23_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

### 自动入库 (2026-07-24)

| 文件 | 标题 | 来源 |
|:----|:----|:----|

| `01_inbox/articles/2026-07-24_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-07-24_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-07-24_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

### 自动入库 (2026-07-25)

| 文件 | 标题 | 来源 |
|:----|:----|:----|

| `01_inbox/articles/2026-07-25_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-07-25_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-07-25_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

### 2026-07-25 20:00 后台维护

| 操作 | 详情 |
|:----|:------|
| 编译 | 01_inbox/articles/ 新文件 2026-07-25_Hermes_Agent.md — 字节级重复（MD5 同 v2 存档），直接归档，无 changelog 更新，无 hash 变更 |
| 归档 | 01_inbox/articles/2026-07-25_Hermes_Agent.md → archive/articles/2026-07-25/2026-07-25_Hermes_Agent_v3.md ✅ |
| 去重检查 | 02-笔记/ 无新精确重复（实体 56 + 概念 40 + 方法 50 + 架构 1 = 147）；13 个小文件(<1KB)均为合法笔记（结构化定义+wikilinks），无 stub 草稿 |
| Hash 追踪 | _hash_tracker.md 已清空（07-23/07-24/07-25 条目已回填至实体笔记 changelog） |
| 地图检查 | Hermes-能力地图（date: 2026-06-08）— routine re-capture，仅 llms-full hash 增量，无新实体/概念，无需更新 |

最终状态：
- 01_inbox/articles: 0 ✅
- 01_inbox/已处理: 0 ✅
- 01-收件箱/所有子目录: 空 ✅
- 02-笔记 合计 147 个文件（实体 56 + 概念 40 + 方法 50 + 架构 1）
- 01_inbox/archive/articles/2026-07-25/: 3 个文件（v1, v2, v3）
- 07-地图/ 无变更
- .last-compile 已刷新

### 自动入库 (2026-07-26)

| 文件 | 标题 | 来源 |
|:----|:----|:----|

| `01_inbox/articles/2026-07-26_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-07-26_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

### 2026-07-26 13:04 后台维护

| 操作 | 详情 |
|:----|:------|
| 编译 | 01_inbox/articles/ 1 个新文件 (Hermes Agent 2026-07-26 v2) — 同一来源 (hermes-agent.nousresearch.com/docs)，llms-full.txt hash 从 `b8408b4b...` 变更为 `66f5f767...`，llms.txt hash 更新为 `96828202...`，页面内容无结构性变化 |
| 归档 | 01_inbox/articles/ 1 个文件 → archive/articles/2026-07-26/2026-07-26_Hermes_Agent_v2.md |
| 去重 | 与 07-26 归档文件仅 llms-full.txt hash 不同，均为例行部署增量 |
| 概念补充 | 概念/Hermes-Agent.md body hash 引用同步更新；frontmatter updated → 2026-07-26 |
| hash-tracker | 2026-07-26 第2轮捕获记录至 _hash_tracker.md |
| 地图状态 | 07-地图/ 无需更新 — hash 增量变更，非新领域 |

最终状态：
- 01_inbox: 0 个待处理文件（已全部归档）
- 01-收件箱: 所有子目录均为空（仅保留 _hash_tracker.md）
- 知识库/02-笔记/概念/Hermes-Agent.md: body hash 已同步，hash-tracker 已更新
- knowledge/02-笔记 合计 147 个文件（实体 56 + 概念 40 + 方法 50 + 架构 1）

| `01_inbox/articles/2026-07-26_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

### 自动入库 (2026-07-27)

| 文件 | 标题 | 来源 |
|:----|:----|:----|

| `01_inbox/articles/2026-07-27_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-07-27_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

### 自动入库 (2026-07-28)

| 文件 | 标题 | 来源 |
|:----|:----|:----|

| `01_inbox/articles/2026-07-28_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-07-28_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-07-28_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

### 自动入库 (2026-07-29)

| 文件 | 标题 | 来源 |
|:----|:----|:----|

| `01_inbox/articles/2026-07-29_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-07-29_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-07-29_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

### 自动入库 (2026-07-30)

| 文件 | 标题 | 来源 |
|:----|:----|:----|

| `01_inbox/articles/2026-07-30_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-07-30_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-07-30_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

### 自动入库 (2026-07-31)

| 文件 | 标题 | 来源 |
|:----|:----|:----|

| `01_inbox/articles/2026-07-31_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-07-31_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-07-31_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

### 自动入库 (2026-08-01)

| 文件 | 标题 | 来源 |
|:----|:----|:----|

| `01_inbox/articles/2026-08-01_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

| `01_inbox/articles/2026-08-01_Hermes_Agent.md` | Hermes Agent | 自动抓取 |

### 2026-08-04 07:00 后台维护

| 操作 | 详情 |
|:----|:------|
| 编译 | 01_inbox/ 无新文件 — 收件箱全部为空 ✅ |
| 归档 | 无文件需归档 ✅ |
| 去重检查 | 02-笔记/ 无新精确重复（实体 56 + 概念 39 + 方法 50 + 架构 1 = 146）；无 stub 草稿 |
| 地图检查 | 07-地图/ 3 个文件无变更（均为 archived 状态） |
| ⚠️ 抓取修复 | daily-capture.sh 自 2026-07-18 起所有 12 站点抓取失败 — `/home/sqby776/office-venv/bin/python3` 路径不存在。已创建 symlink: `office-venv/bin/python3 → /usr/bin/python3` |

最终状态：
- 01_inbox/articles: 0 ✅
- 01-收件箱/所有子目录: 空 ✅（仅 _hash_tracker.md 跟踪文件）
- 02-笔记 合计 146 个文件（实体 56 + 概念 39 + 方法 50 + 架构 1）
- 01_inbox/archive/articles/2026-08-01/: 2 个文件
- 07-地图/ 3 个文件无变更
- .last-compile 已刷新

### 自动入库 (2026-08-06)

| 文件 | 标题 | 来源 |
|:----|:----|:----|

| `01_inbox/articles/2026-08-06_csv_CSV_File_Reading_and_Writing.md` | `csv` — CSV File Reading and Writing¶ | 自动抓取 |

| `01_inbox/articles/2026-08-06_Getting_Started.md` | Getting Started¶ | 自动抓取 |

| `01_inbox/articles/2026-08-06_10_minutes_to_pandas.md` | 10 minutes to pandas# | 自动抓取 |

| `01_inbox/articles/2026-08-06_Quick_start_guide.md` | Quick start guide# | 自动抓取 |

| `01_inbox/articles/2026-08-06_csv_CSV_File_Reading_and_Writing.md` | `csv` — CSV File Reading and Writing¶ | 自动抓取 |

| `01_inbox/articles/2026-08-06_json_JSON_encoder_and_decoder.md` | `json` — JSON encoder and decoder¶ | 自动抓取 |

| `01_inbox/articles/2026-08-06_pathlib_Object_oriented_filesystem_paths.md` | `pathlib` — Object-oriented filesystem paths¶ | 自动抓取 |

| `01_inbox/articles/2026-08-06_Data_Visualization_With_Python.md` | Data Visualization With Python | 自动抓取 |

| `01_inbox/articles/2026-08-06_csv_CSV_File_Reading_and_Writing.md` | `csv` — CSV File Reading and Writing¶ | 自动抓取 |

| `01_inbox/articles/2026-08-06_Quickstart.md` | Quickstart¶ | 自动抓取 |

| `01_inbox/articles/2026-08-06_Tutorial.md` | Tutorial | 自动抓取 |

| `01_inbox/articles/2026-08-06_Getting_Started.md` | Getting Started¶ | 自动抓取 |

| `01_inbox/articles/2026-08-06_10_minutes_to_pandas.md` | 10 minutes to pandas# | 自动抓取 |

| `01_inbox/articles/2026-08-06_Quick_start_guide.md` | Quick start guide# | 自动抓取 |

| `01_inbox/articles/2026-08-06_csv_CSV_File_Reading_and_Writing.md` | `csv` — CSV File Reading and Writing¶ | 自动抓取 |

| `01_inbox/articles/2026-08-06_json_JSON_encoder_and_decoder.md` | `json` — JSON encoder and decoder¶ | 自动抓取 |

| `01_inbox/articles/2026-08-06_pathlib_Object_oriented_filesystem_paths.md` | `pathlib` — Object-oriented filesystem paths¶ | 自动抓取 |

| `01_inbox/articles/2026-08-06_Data_Visualization_With_Python.md` | Data Visualization With Python | 自动抓取 |

### 自动入库 (2026-08-08)

| 文件 | 标题 | 来源 |
|:----|:----|:----|

| `01_inbox/articles/2026-08-08_10_minutes_to_pandas.md` | 10 minutes to pandas# | 自动抓取 |

| `01_inbox/articles/2026-08-08_Quick_start_guide.md` | Quick start guide# | 自动抓取 |

| `01_inbox/articles/2026-08-08_csv_CSV_File_Reading_and_Writing.md` | `csv` — CSV File Reading and Writing¶ | 自动抓取 |

| `01_inbox/articles/2026-08-08_json_JSON_encoder_and_decoder.md` | `json` — JSON encoder and decoder¶ | 自动抓取 |

| `01_inbox/articles/2026-08-08_pathlib_Object_oriented_filesystem_paths.md` | `pathlib` — Object-oriented filesystem paths¶ | 自动抓取 |

| `01_inbox/articles/2026-08-08_Data_Visualization_With_Python.md` | Data Visualization With Python | 自动抓取 |

### 自动入库 (2026-08-09)

| 文件 | 标题 | 来源 |
|:----|:----|:----|

| `01_inbox/articles/2026-08-09_Getting_Started.md` | Getting Started¶ | 自动抓取 |

| `01_inbox/articles/2026-08-09_10_minutes_to_pandas.md` | 10 minutes to pandas# | 自动抓取 |

| `01_inbox/articles/2026-08-09_Quick_start_guide.md` | Quick start guide# | 自动抓取 |

| `01_inbox/articles/2026-08-09_csv_CSV_File_Reading_and_Writing.md` | `csv` — CSV File Reading and Writing¶ | 自动抓取 |

| `01_inbox/articles/2026-08-09_json_JSON_encoder_and_decoder.md` | `json` — JSON encoder and decoder¶ | 自动抓取 |

| `01_inbox/articles/2026-08-09_pathlib_Object_oriented_filesystem_paths.md` | `pathlib` — Object-oriented filesystem paths¶ | 自动抓取 |

| `01_inbox/articles/2026-08-09_Data_Visualization_With_Python.md` | Data Visualization With Python | 自动抓取 |

### 知识库维护 (2026-08-09)

| 操作 | 详情 |
|:----|:-----|
| 归档重复捕获 | 7 个 Python 文档（10_minutes_to_pandas、csv、json、pathlib、Data_Visualization、Getting_Started、Quick_start_guide）→ `archive/自动捕获/2026-08-09/` |
| 删除空壳 stub | Quick_start_guide.md（Matplotlib 导航页）→ `99-归档/2026-08-09/实体-重复草稿/` |
| 内容变化 | 无实质内容变化（仅元数据日期差异） |
| 地图更新 | 无需更新 |
| last-compile | 已同步为 2026-08-09 07:05:21 |

### 自动入库 (2026-08-10)

| 文件 | 标题 | 来源 |
|:----|:----|:----|

| `01_inbox/articles/2026-08-10_10_minutes_to_pandas.md` | 10 minutes to pandas# | 自动抓取 |

| `01_inbox/articles/2026-08-10_Quick_start_guide.md` | Quick start guide# | 自动抓取 |

| `01_inbox/articles/2026-08-10_csv_CSV_File_Reading_and_Writing.md` | `csv` — CSV File Reading and Writing¶ | 自动抓取 |

| `01_inbox/articles/2026-08-10_json_JSON_encoder_and_decoder.md` | `json` — JSON encoder and decoder¶ | 自动抓取 |

| `01_inbox/articles/2026-08-10_pathlib_Object_oriented_filesystem_paths.md` | `pathlib` — Object-oriented filesystem paths¶ | 自动抓取 |

| `01_inbox/articles/2026-08-10_Data_Visualization_With_Python.md` | Data Visualization With Python | 自动抓取 |

### 自动入库 (2026-08-11)

| 文件 | 标题 | 来源 |
|:----|:----|:----|

| `01_inbox/articles/2026-08-11_10_minutes_to_pandas.md` | 10 minutes to pandas# | 自动抓取 |

| `01_inbox/articles/2026-08-11_Quick_start_guide.md` | Quick start guide# | 自动抓取 |

| `01_inbox/articles/2026-08-11_csv_CSV_File_Reading_and_Writing.md` | `csv` — CSV File Reading and Writing¶ | 自动抓取 |

| `01_inbox/articles/2026-08-11_json_JSON_encoder_and_decoder.md` | `json` — JSON encoder and decoder¶ | 自动抓取 |

| `01_inbox/articles/2026-08-11_pathlib_Object_oriented_filesystem_paths.md` | `pathlib` — Object-oriented filesystem paths¶ | 自动抓取 |

| `01_inbox/articles/2026-08-11_Data_Visualization_With_Python.md` | Data Visualization With Python | 自动抓取 |

### 自动入库 (2026-08-12)

| 文件 | 标题 | 来源 |
|:----|:----|:----|

| `01_inbox/articles/2026-08-12_Getting_Started.md` | Getting Started¶ | 自动抓取 |

| `01_inbox/articles/2026-08-12_10_minutes_to_pandas.md` | 10 minutes to pandas# | 自动抓取 |

| `01_inbox/articles/2026-08-12_Quick_start_guide.md` | Quick start guide# | 自动抓取 |

| `01_inbox/articles/2026-08-12_csv_CSV_File_Reading_and_Writing.md` | `csv` — CSV File Reading and Writing¶ | 自动抓取 |

| `01_inbox/articles/2026-08-12_json_JSON_encoder_and_decoder.md` | `json` — JSON encoder and decoder¶ | 自动抓取 |

| `01_inbox/articles/2026-08-12_pathlib_Object_oriented_filesystem_paths.md` | `pathlib` — Object-oriented filesystem paths¶ | 自动抓取 |

| `01_inbox/articles/2026-08-12_Data_Visualization_With_Python.md` | Data Visualization With Python | 自动抓取 |

### 自动入库 (2026-08-13)

| 文件 | 标题 | 来源 |
|:----|:----|:----|

| `01_inbox/articles/2026-08-13_10_minutes_to_pandas.md` | 10 minutes to pandas# | 自动抓取 |

| `01_inbox/articles/2026-08-13_Quick_start_guide.md` | Quick start guide# | 自动抓取 |

| `01_inbox/articles/2026-08-13_csv_CSV_File_Reading_and_Writing.md` | `csv` — CSV File Reading and Writing¶ | 自动抓取 |

| `01_inbox/articles/2026-08-13_json_JSON_encoder_and_decoder.md` | `json` — JSON encoder and decoder¶ | 自动抓取 |

| `01_inbox/articles/2026-08-13_pathlib_Object_oriented_filesystem_paths.md` | `pathlib` — Object-oriented filesystem paths¶ | 自动抓取 |

| `01_inbox/articles/2026-08-13_Data_Visualization_With_Python.md` | Data Visualization With Python | 自动抓取 |

### 自动入库 (2026-08-14)

| 文件 | 标题 | 来源 |
|:----|:----|:----|

| `01_inbox/articles/2026-08-14_10_minutes_to_pandas.md` | 10 minutes to pandas# | 自动抓取 |

| `01_inbox/articles/2026-08-14_Quick_start_guide.md` | Quick start guide# | 自动抓取 |

| `01_inbox/articles/2026-08-14_csv_CSV_File_Reading_and_Writing.md` | `csv` — CSV File Reading and Writing¶ | 自动抓取 |

| `01_inbox/articles/2026-08-14_json_JSON_encoder_and_decoder.md` | `json` — JSON encoder and decoder¶ | 自动抓取 |

| `01_inbox/articles/2026-08-14_pathlib_Object_oriented_filesystem_paths.md` | `pathlib` — Object-oriented filesystem paths¶ | 自动抓取 |

| `01_inbox/articles/2026-08-14_Data_Visualization_With_Python.md` | Data Visualization With Python | 自动抓取 |

### 自动入库 (2026-08-15)

| 文件 | 标题 | 来源 |
|:----|:----|:----|

| `01_inbox/articles/2026-08-15_10_minutes_to_pandas.md` | 10 minutes to pandas# | 自动抓取 |

| `01_inbox/articles/2026-08-15_Quick_start_guide.md` | Quick start guide# | 自动抓取 |

| `01_inbox/articles/2026-08-15_csv_CSV_File_Reading_and_Writing.md` | `csv` — CSV File Reading and Writing¶ | 自动抓取 |

| `01_inbox/articles/2026-08-15_json_JSON_encoder_and_decoder.md` | `json` — JSON encoder and decoder¶ | 自动抓取 |

| `01_inbox/articles/2026-08-15_pathlib_Object_oriented_filesystem_paths.md` | `pathlib` — Object-oriented filesystem paths¶ | 自动抓取 |

| `01_inbox/articles/2026-08-15_Data_Visualization_With_Python.md` | Data Visualization With Python | 自动抓取 |
