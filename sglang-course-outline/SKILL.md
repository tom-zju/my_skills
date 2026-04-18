---
name: sglang-course-outline
description: 为 SGLang 生成中文课程总纲、课程目录、学习大纲、知识地图和学习路径。适用于系统梳理 SGLang 项目总览、技术发展、双层体系架构、SRT 运行时主链、调度与缓存机制、RadixAttention、前缀缓存、Chunked Prefill、注意力后端、并行体系、Speculative Decoding、Quantization、PD/EPD 解耦、HiCache，以及大模型结构、长文本优化和性能优化端到端流程，并按“单课单主题”原则设计主课程或专题高阶课程的场景。
---

# SGLang 课程总纲与课程目录整理

## 核心约束速查

> 上下文压缩时优先保留本节。

1. **单课单主题**：同一课只讲一个重要主题；标题中出现多个不同问题域，优先拆课。
2. **主课程保持主线**：标准版主课程默认 19 课，按“介绍与上手 -> 运行时主链 -> 并行体系 -> 执行优化 -> 解耦与缓存”组织。
3. **高阶主题重新分层**：`并行体系总览 + 并行机制细讲`、`Speculative Decoding`、`Quantization 基础与原理`、`Quantization 模块解析与实践`、`PD Disaggregation`、`HiCache` 默认进入主课程；`大模型结构`、`长文本优化`、`端到端性能优化` 默认进入专题高阶课程。
4. **不重复计算**：已在专题高阶课程独立成课的主题，主课程不再保留同名独立课时。
5. **版本先核对再写**：用户提到"最新版本/main/最近代码"时，必须先查官方 release/tag，再写课纲，并显式写明版本号。
6. **中文优先**：正文、章节名、课时标题默认中文；代码标识符、路径保留英文原名。

---

## 总体说明

这个 skill 用来把 SGLang 整理成可教学、可分享、可沉淀的中文课程材料，而不是零散知识点列表。默认目标是产出一份结构完整、语言统一、能直接用于课程讲授、内部培训或文档沉淀的 Markdown 内容。

除非用户明确要求英文，否则正文、章节名、课程名、学习目标和说明文字都必须使用中文；代码标识符、目录名和文件路径保留英文原名。

本 skill 的默认教学设计原则：

- `单课单主题`：同一课时只保留一个重要主题，出现多个不同问题域时优先拆课
- `主课程讲主线，专题课程讲深水区`

## 适用场景

当用户有下面这些需求时使用本 skill：

- 要 SGLang 课程总纲
- 要一份详细的 SGLang 课程大纲
- 要 SGLang 学习大纲
- 要 SGLang 课程目录
- 要 SGLang 知识体系或知识地图
- 要按课时拆分的培训提纲、分享提纲或 onboarding 材料
- 要把 SGLang 官方仓库与文档整理成中文教学版文档
- 要围绕 SGLang 的 SRT runtime、调度、缓存、解耦式 serving、并行与执行优化做系统课程设计
- 要围绕 DeepSeek / Kimi / Qwen 做模型结构教学设计
- 要梳理长文本场景下从模型到 SGLang / vLLM 再到算子的优化点
- 要总结 LLM 模型性能优化的端到端流程
- 要把“大而全课纲”重构成“主课程 + 专题高阶课程”的模板体系

如果用户只是问某个算子、某个 patch 或某个局部实现细节，本 skill 不是首选，应改用更聚焦的专题分析方式。

## 工作流程

1. 先判断输出模式：
   - `课程总纲`：按章节组织，适合长文档
   - `课程目录`：按“第几课”组织，适合 lesson 化教学
   - `学习路径`：按阅读顺序组织
   - `知识地图`：按系统模块关系组织
2. 再判断课程包装方式：
   - `母版总纲`：完整知识地图，给讲师和课程设计者使用
   - `主课程`：用于真正授课，默认严格执行“单课单主题”
   - `专题高阶课程`：把大模型结构、长文本优化、端到端性能优化等专题主题拆开单讲
3. 再判断课程深度：
   - `标准版主课程`：默认 19 课，包含 `并行体系总览 + 并行机制细讲` 与 `Quantization 两课`
   - `扩展版`：在主课程后追加专题高阶课程
4. 再判断目标读者：
   - 新人入门
   - 推理服务工程师
   - 要做二次开发的开发者
   - 要做专项优化的高阶研发
5. 默认叙事顺序保持为：
   - 项目定位
   - 技术发展
   - 双层体系架构
   - 请求生命周期
   - 调度与缓存主链
   - 单课单主题的关键能力
   - 解耦与并行专题
   - 模型能力与系统演进
6. 先从官方文档和主仓库建立全景，再深入代码。标注 `【必读】` 的是每次生成课纲都应覆盖的，标注 `【按需】` 的只在用户明确要求相关专题时查阅：
   - `【必读】` 官方文档首页与安装文档
   - `【必读】` `OpenAI-Compatible APIs`
   - `【必读】` `Offline Engine API`
   - `【必读】` `SGLang Native APIs`
   - `【必读】` `Attention Backend`
   - `【必读】` `Speculative Decoding`
   - `【必读】` `Quantization`
   - `【必读】` `PD Disaggregation`
   - `【必读】` `Hierarchical KV Caching (HiCache)`
   - `【必读】` `python/sglang/srt/entrypoints/`
   - `【必读】` `python/sglang/srt/managers/`
   - `【必读】` `python/sglang/srt/mem_cache/`
   - `【必读】` `python/sglang/srt/layers/attention/`
   - `【必读】` `python/sglang/srt/model_executor/`
   - `【必读】` `python/sglang/srt/distributed/`
   - `【必读】` `python/sglang/srt/speculative/`
   - `【按需】` `Sampling Parameters`（并入请求生命周期时查阅）
   - `【必读】` `Expert Parallelism`（主课程中的并行机制细讲默认查阅）
   - `【必读】` `DP, DPA and SGLang DP Router`（主课程中的并行机制细讲默认查阅）
   - `【必读】` `Pipeline Parallelism for Long Context`（主课程中的并行机制细讲默认查阅）
   - `【按需】` `python/sglang/srt/models/`（DeepSeek / Kimi / Qwen 模型结构专题时查阅）
   - `【按需】` `python/sglang/srt/disaggregation/`（PD / EPD 专题时查阅）
   - `【按需】` `Quantized KV Cache`（长文本或量化扩展专题时查阅）
   - `【按需】` `vLLM 官方文档与源码`（长文本框架对比专题时查阅）
   - `【按需】` 输出控制、函数调用与解析器相关文档和源码（仅在用户单独要求相关补充专题时查阅）
7. 如果用户要求“技术发展”或“演进路线”，优先使用“能力演进主线”，不要在没有核对过版本、tag 或主分支状态时硬写精确时间线。
8. 对于每一章或每一课，都说明：
   - 这一部分为什么重要
   - 推荐先看哪些文档或源码位置
   - 和前后内容如何衔接
9. 如果用户提到“最新版本”“当前版本”“main”“最近代码”之类的版本化要求，必须先核对 SGLang 官方 GitHub release/tag 与主仓库代码，再写课纲。对版本相关结论要显式写明：
   - 实际核对到的版本号或 tag
   - 实际核对到的官方发布日期
   - 是否同时参考了 `main` 主线代码结构
   - 本课纲中哪些专题是该阶段特别值得新增或强化的内容
10. 如果用户要求“20 到 22 节左右课程”，默认先输出 `19 节标准版主课程`，再按用户关心的专题补充 1 到 3 节专题高阶课程。
11. 如果用户要求“一份详细的 SGLang 课程大纲”，默认同时输出 `标准版主课程 + 专题高阶课程`，并使用 Markdown 文档组织；每一课至少包含：
   - `课程主题`
   - `为什么重要`
   - `核心知识点`
   - `学习目标`
   - `推荐阅读文件资料`
   - `建议练习或演示`
12. 详细课纲中的 `推荐阅读文件资料` 必须尽量给出真实可靠、可核验的官方文档页、官方 GitHub 仓库路径或源码文件链接；不要编造链接，也不要只写模糊目录名。

完整覆盖要求见 [topic-map.md](./references/topic-map.md)。按 lesson 组织课程时，优先参考 [syllabus-patterns.md](./references/syllabus-patterns.md)。

## 核心教学规则：单课单主题

### 主规则

- 同一课默认只讲 `一个重要主题`
- 一个主题可以带少量紧邻子点，但不能跨不同问题域
- 如果一个标题里出现多个并列主题，优先怀疑这个标题是否应该拆成多课

### 可以作为同一课内部子点的情况

- `RadixAttention` 一课里带出 radix tree 命中路径与 page/block 组织
- `PD Disaggregation` 一课里带出 prefill / decode 路由与实例协同
- `Quantization` 一课里带出权重量化、KV cache 量化入口与部署约束
- `HiCache` 一课里带出多级 KV cache 的冷热分层与迁移策略
- `SGLang 介绍、环境搭建与快速上手` 一课里带出项目定位、安装路径与第一个 demo
- `并行机制细讲` 一课里带出 `TP / DP / DPA / DP Router / SP / EP / PP` 的切分、通信与路由差异
- `Quantization 模块解析与实践` 一课里带出模块入口、配置方式与部署实践

### 默认必须拆开的情况

- `Speculative Decoding` 和 `Chunked Prefill`
- `RadixAttention` 和 `HiCache`
- `Attention Backend` 和 `Quantization`
- `PD Disaggregation` 和 `按需补充专题`
- `并行机制细讲` 和 `按需补充专题`
- `大模型结构专题` 和 `长文本优化专题`
- `长文本优化专题` 和 `端到端性能优化专题`

标准版主课程中的默认例外：

- `SGLang 介绍、环境搭建与快速上手` 可以作为一节 onboarding 课存在
- `并行体系总览（TP / DP / SP / PP / EP）` 可以作为一节概览课存在，但必须明确这是“全景导论”
- `并行机制细讲` 可以作为一节机制对比课存在，但必须围绕“切分方式、通信路径、路由策略、适用场景”组织
- 如果用户要求源码级分布式专题，则应进一步拆开为 `TP`、`DP / DPA / DP Router`、`SP`、`PP`、`EP`

### 触发拆课的判断规则

- 主题分别属于 `调度/缓存`、`执行/编译`、`并行/解耦`、`输出控制`、`模型结构/长文本/性能优化` 这几个不同问题域
- 主题各自都足以支撑 3 个以上核心知识点
- 主题分别对应不同源码入口或不同维护角色
- 把它们合在一起会让“为什么这一课重要”变得不够聚焦

### 主题过多时的处理方式

1. 放入 `专题高阶课程`
2. 放入 `可选扩展课`
3. 放入 `母版总纲`，但不要强行塞进标准版主课程

### 主课程的实质内容约束

标准版主课程默认必须满足：

- 每一课都要有具体模块、具体链路、具体接口或具体运行能力作为主体
- 不能用纯包装性质的课题凑课时
- 标准版主课程默认覆盖 SGLang 强链路主线、并行体系、执行优化与解耦缓存
- 标准版主课程默认围绕 `介绍与快速上手 -> 架构与入口 -> 请求进入 -> tokenizer / scheduler -> schedule batch -> continuous batching / chunked prefill -> radix attention / prefix reuse -> worker / model runner -> attention backend -> parallelism overview / detail -> speculative decoding -> quantization basics / practice -> disaggregation / hicache` 组织
- `项目定位` 与 `版本演进` 默认写入课程说明、导论或 `双层体系架构全景` 开场，不单独列课
- `Server Arguments` 默认并入 `环境搭建` 或 `架构全景` 的附录，不单独列课
- `OpenAI-Compatible APIs`、`Offline Engine API`、`SGLang Native APIs` 默认并入 `架构全景` 与 `请求生命周期`，不单独列课
- `Sampling Parameters` 默认并入 `请求生命周期` 或量化/生成相关说明，不单独列课
- `源码阅读路径` 默认并入每课的 `推荐阅读文件资料` 和课程末尾附录，不单独列课
- `并行体系总览`、`并行机制细讲`、`Speculative Decoding`、`Quantization 基础与原理`、`Quantization 模块解析与实践`、`PD Disaggregation` 与 `HiCache` 默认进入标准版主课程

### 模板课程与高阶课程去重规则

- 主课程里不要再保留已经下放到专题高阶课程的独立课时
- 主课程最多只保留一层导论性概览
- 如果课程由“主课程 + 专题营”组合而成，不要重复统计相同主题

## 必须覆盖的五大块

### 1. SGLang 项目总览与技术发展

至少回答下面这些问题：

- SGLang 是什么
- 它相比普通 serving 框架的独特价值是什么
- 它为什么既是 frontend language，也是 serving runtime
- 它如何从单机高性能推理逐步演进到大规模解耦与并行 serving 体系

### 2. SGLang 双层体系架构

至少覆盖：

- Frontend Language 与 Backend Runtime 的分层
- OpenAI-compatible API、Offline Engine API、Native APIs 三类入口
- SRT runtime 的核心进程与模块
- `entrypoint -> tokenizer manager -> scheduler -> tp worker -> model runner -> model` 的主链

### 3. 核心运行时主链

不能只列目录，必须解释职责、上下游关系和重要性。默认优先覆盖：

- `python/sglang/srt/entrypoints`
- `python/sglang/srt/server_args.py`
- `python/sglang/srt/managers/tokenizer_manager.py`
- `python/sglang/srt/managers/scheduler.py`
- `python/sglang/srt/managers/schedule_batch.py`
- `python/sglang/srt/managers/tp_worker.py`
- `python/sglang/srt/mem_cache`
- `python/sglang/srt/layers/attention`
- `python/sglang/srt/model_executor`
- `python/sglang/srt/disaggregation`
- `python/sglang/srt/distributed`

### 4. 重要特性

主课程主线默认优先覆盖：

- SGLang 介绍、环境搭建与快速上手
- RadixAttention
- prefix reuse / radix cache
- continuous batching
- chunked prefill
- 并行体系总览
- 并行机制细讲
- speculative decoding
- quantization basics
- quantization practice
- PD disaggregation（主课程强特性）
- HiCache
- attention backend

下列主题默认下放到专题高阶课程，只有用户明确要求相关专题或需要扩展版补充时再覆盖：

- DeepSeek 系列模型结构
- Kimi 系列模型结构
- Qwen 系列模型结构
- 长文本优化专题
- SGLang 性能优化端到端专题
- 其他按需扩展主题

### 5. 并行与解耦高级专题

标准版主课程现在默认至少覆盖：

- `并行体系总览（TP / DP / SP / PP / EP）`
- `并行机制细讲（TP / DP / DPA / DP Router / SP / EP / PP）`
- `Speculative Decoding`
- `Quantization 基础与原理`
- `Quantization 模块解析与实践`
- `PD Disaggregation`
- `HiCache`

如果用户要求“深度版”“系统梳理分布式”“源码级课程”，再额外强化：

- `TP`
- `DP / DPA / DP Router`
- `SP`
- `Pipeline Parallelism for Long Context`
- `EP`
- 解耦式 serving 的按需扩展主题

写作时默认说明三件事：

- 这个机制解决什么瓶颈
- 它改变了哪些通信、缓存或路由布局
- 它和调度、缓存、模型结构之间如何组合

## 按需补充专题

如果用户单独要求非默认主题，可作为按需补充专题覆盖，但这些内容不属于当前默认的三大特性专项模板，也不要自动塞回标准版主课程。

## 课程目录模式

当用户要求“课程目录”“课纲”“第几课”“lesson 版大纲”“按课时拆分”时，优先使用课程目录模式。

### 课程目录默认格式

- `第1课-...`
- `第2课-...`
- `第3课-...`

不要默认写成：

- `Lesson 1`
- `Part 1`
- `Chapter 1`

### 每一课默认应包含

- `课程主题`
- `为什么这一课重要`
- `核心知识点`
- `学习目标`
- `推荐阅读文件资料`
- `建议练习或演示`

### 课程目录默认输出优先级

1. `标准版主课程`
2. `专题高阶课程列表`
3. `母版总纲`

如果用户明确要求“详细课纲”“详细课程大纲”“完整教学版大纲”，默认优先输出 `标准版主课程 + 专题高阶课程` 的完整 Markdown 文档，而不是只给主课程。
如果用户要求“严格单课单主题”，优先输出 `19 节标准版主课程 + 专题高阶课程`，并显式说明第 1 课、并行两课与量化实践课是教学包装上的例外。
如果用户只说“扩展到 20 到 22 节左右”，默认先输出 `19 节标准版主课程`，再根据用户关心的专题补充 1 到 3 节专题课。

## 默认输出结构

如果用户要求正式文档、课程总纲或 lesson 化课纲，默认最终产出应为 Markdown 文档。

### 章节式课程总纲默认结构

1. `课程定位与适用对象`
2. `先修知识`
3. `SGLang 项目总览与技术发展`
4. `SGLang 双层体系架构`
5. `请求生命周期`
6. `核心运行时主链`
7. `重要特性专题`
8. `并行与解耦高级专题`
9. `大模型结构、长文本与性能优化专题`
10. `推荐学习路径与源码入口`
11. `总结`

### 课程目录默认结构

- `课程说明`
- `课程总目标`
- `课程阶段划分`
- `标准版主课程`
- `专题高阶课程`
- `第1课-...`
- `第2课-...`
- `第3课-...`
- ...
- `推荐配套阅读顺序`
- `课程压缩与扩展建议`

如果用户要求“详细课程大纲”，则默认要求：

- 同时给出 `标准版主课程` 与 `专题高阶课程`
- 最终产出为结构完整的 Markdown 文档
- 每一课都包含 `课程主题`、`为什么重要`、`核心知识点`、`学习目标`、`推荐阅读文件资料`、`建议练习或演示`
- `推荐阅读文件资料` 尽量附真实可靠的官方文档链接、官方仓库链接或可定位的源码路径

### 默认课时规模

- `标准版主课程`：默认 19 课
- `专题高阶课程`：当前默认每营 3 课；用户明确要求扩展时再增加

如果用户明确要求“20 到 22 节左右课程”，优先生成：

- `19 节标准版主课程 + 1 到 3 节专题课`

如果用户明确要求必须压缩到 `18 到 20 节`，优先说明压缩掉的是哪个专题或哪一层细讲，再给出精简版。

## 写作规则

- 最终正文默认必须用中文
- 课程名、章节名、每一课标题默认必须用中文
- 如果是课程目录模式，课时标题默认必须写成 `第X课-主题`
- 如果课纲对齐具体版本，开头默认写明 `基于 SGLang vX.Y.Z` 或 `基于 SGLang main + release tag`
- 优先讲系统主线，不要一上来陷入单个模型或单个 kernel 细节
- 优先解释组件职责和请求链路，不要只罗列目录名
- 不要把特性写成营销清单
- 尽量把每一课都落到具体文档页或源码入口
- 如果用户要求详细课纲，优先给出可直接点击或核验的官方文档链接与仓库链接
- 主课程中，默认一课只讲一个重要主题
- 如果一个课时标题里出现两个以上不同问题域，优先拆成多个课时
- 如果主题过多，优先分配到 `专题高阶课程`
- 如果某个主题已经在专题高阶课程中独立成课，主课程中不要重复保留该主题的独立课时
- 如果用户要求“结合最新版本”或“结合最新代码”，优先说明本次是否按官方 release、tag 还是 `main` 主分支进行核对

更细的覆盖维度、课程拆分模式和常见偏题点，见：

- [topic-map.md](./references/topic-map.md)
- [syllabus-patterns.md](./references/syllabus-patterns.md)
