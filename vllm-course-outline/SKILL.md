---
name: vllm-course-outline
description: 为 vLLM 生成中文课程总纲、课程目录、学习大纲、知识地图和学习路径。适用于系统梳理 vLLM 项目总览、技术发展、架构全景、核心组件、关键特性、分布式并行、offloading、attention backend、structured outputs、工具调用、重要模型结构，以及按“单课单主题”原则设计主课程或专题高阶课程的场景。
---

# vLLM 课程总纲与课程目录整理

## 核心约束速查

> 上下文压缩时优先保留本节。

1. **单课单主题**：同一课只讲一个重要主题；标题中出现多个不同问题域，优先拆课。
2. **主课程保持主线**：标准版主课程默认 15 课，严格按执行流排序，不塞高阶专题。
3. **高阶主题下放专题营**：Speculative Decoding、所有并行维度、Offloading、PD 分离、Attention Backend、Structured Outputs/工具调用、模型结构、LoRA、多模态默认不进主课程。
4. **不重复计算**：已在专题高阶课程独立成课的主题，主课程不再保留同名独立课时。
5. **版本先核对再写**：用户提到"最新版本/指定版本/最近代码"时，必须先查官方 release，再写课纲，并显式写明版本号和发布日期。
6. **中文优先**：正文、章节名、课时标题默认中文；代码标识符、路径保留英文原名。

---

## 总体说明

这个 skill 用来把 vLLM 整理成可教学、可分享、可沉淀的中文课程材料，而不是零散知识点列表。默认目标是产出一份结构完整、语言统一、能直接用于课程讲授、内部培训或文档沉淀的 Markdown 内容。

除非用户明确要求英文，否则正文、章节名、课程名、学习目标和说明文字都必须使用中文；代码标识符、目录名和文件路径保留英文原名。

本 skill 的默认教学设计原则已经升级为：`主课程讲主线，专题课程讲深水区`。

## 适用场景

当用户有下面这些需求时使用本 skill：

- 要 vLLM 课程总纲
- 要 vLLM 学习大纲
- 要 vLLM 课程目录
- 要 vLLM 知识体系或知识地图
- 要按课时拆分的培训提纲、分享提纲或 onboarding 材料
- 要把 vLLM 仓库整理成中文教学版文档
- 要围绕 vLLM 分布式并行、KV 管理、offloading、PD 分离、attention backend、structured outputs、工具调用、模型结构做系统课程设计
- 要把“大而全课纲”重构成“主课程 + 专题高阶课程”的模板体系

如果用户只是问某个模型文件、某个算子或某个局部实现细节，本 skill 不是首选，应改用更聚焦的专题分析方式。

## 工作流程

1. 先判断输出模式：
   - `课程总纲`：按章节组织，适合长文档
   - `课程目录`：按“第几课”组织，适合 lesson 化教学
   - `学习路径`：按阅读顺序组织
   - `知识地图`：按系统模块关系组织
2. 再判断课程包装方式：
   - `母版总纲`：完整知识地图，给讲师和课程设计者使用
   - `主课程`：用于真正授课，默认严格执行“单课单主题”
   - `专题高阶课程`：把分布式、offloading、PD 分离、attention backend、agent serving 等深水区主题拆开单讲
3. 再判断课程深度：
   - `标准版主课程`：默认 15 课
   - `扩展版`：在标准版主课程后追加专题高阶课程
4. 再判断目标读者：
   - 新人入门
   - 推理服务工程师
   - 要做二次开发的开发者
   - 要做专项优化的高阶研发
5. 默认叙事顺序保持为：
   - 项目定位
   - 技术发展
   - 架构全景
   - 请求生命周期
   - 核心组件
   - 单课单主题的关键能力
   - 分布式与运行时专题
   - 模型结构与系统演进
6. 先从仓库级材料建立全景，再深入源码。标注 `【必读】` 的是每次生成课纲都应覆盖的，标注 `【按需】` 的只在用户明确要求相关专题时查阅：
   - `【必读】` `README.md`
   - `【必读】` `docs/design/arch_overview.md`
   - `【必读】` `docs/usage/v1_guide.md`
   - `【必读】` `docs/configuration/optimization.md`
   - `【必读】` `vllm/entrypoints/`
   - `【必读】` `vllm/v1/`
   - `【必读】` `vllm/engine/`
   - `【必读】` `vllm/model_executor/`
   - `【必读】` `vllm/v1/worker/`
   - `【必读】` `vllm/v1/attention/`
   - `【必读】` `vllm/sequence.py`
   - `【必读】` `vllm/sampling_params.py`
   - `【必读】` `vllm/logits_process.py`
   - `【按需】` `RELEASE.md`（版本演进或指定版本时查阅）
   - `【按需】` `docs/design/paged_attention.md`（KV Cache / PagedAttention 课时查阅）
   - `【按需】` `docs/design/prefix_caching.md`（Prefix Caching 课时查阅）
   - `【按需】` `docs/design/model_runner_v2.md`（执行路径专题营时查阅）
   - `【按需】` `docs/design/mm_processing.md`（多模态专题营时查阅）
   - `【按需】` `docs/design/torch_compile.md`（编译优化专题营时查阅）
   - `【按需】` `docs/design/fused_moe_modular_kernel.md`（编译优化专题营时查阅）
   - `【按需】` `docs/features/structured_outputs.md`（Agent Serving 专题营时查阅）
   - `【按需】` `docs/features/tool_calling.md`（Agent Serving 专题营时查阅）
   - `【按需】` `docs/features/reasoning_outputs.md`（Reasoning Outputs 专题营时查阅）
   - `【按需】` `docs/features/disagg_prefill.md`（PD 分离专题营时查阅）
   - `【按需】` `docs/features/disagg_encoder.md`（多模态解耦专题时查阅）
   - `【按需】` `docs/design/attention_backends.md`（Attention Backend 专题营时查阅）
   - `【按需】` `docs/features/lora.md`（LoRA 专题营时查阅）
   - `【按需】` `docs/features/multimodal_inputs.md`（多模态专题营时查阅）
   - `【按需】` `docs/serving/parallelism_scaling.md`（并行专题营时查阅）
   - `【按需】` `docs/serving/data_parallel_deployment.md`（并行专题营时查阅）
   - `【按需】` `docs/serving/expert_parallel_deployment.md`（并行专题营时查阅）
   - `【按需】` `docs/serving/context_parallel_deployment.md`（并行专题营时查阅）
   - `【按需】` `vllm/distributed/`（分布式专题营时查阅）
   - `【按需】` `vllm/distributed/parallel_state.py`（分布式接线专题时查阅）
   - `【按需】` `vllm/distributed/kv_transfer/`（KV Transfer / PD 分离专题时查阅）
   - `【按需】` `vllm/model_executor/offloader/`（Weight Offloading 专题时查阅）
   - `【按需】` `vllm/v1/kv_offload/`（KV Offloading 专题时查阅）
   - `【按需】` `vllm/v1/structured_output/`（Structured Outputs 专题时查阅）
   - `【按需】` `vllm/parser/`（Structured Outputs / Parser 专题时查阅）
   - `【按需】` `vllm/tool_parsers/`（Tool Parser 专题时查阅）
   - `【按需】` `vllm/reasoning/`（Reasoning Outputs / Parser 专题时查阅）
   - `【按需】` `vllm/lora/`（LoRA 专题营时查阅）
   - `【按需】` `vllm/multimodal/`（多模态专题营时查阅）
   - `【按需】` `vllm/entrypoints/serve/disagg/`（Disaggregated Serving 专题时查阅）
7. 如果用户要求“技术发展”或“演进路线”，优先使用“能力演进主线”，不要在没有核对过版本和日期时硬写精确时间线。
8. 对于每一章或每一课，都说明：
   - 这一部分为什么重要
   - 推荐先看哪些文件
   - 和前后内容如何衔接
9. 如果用户提到“最新版本”“当前版本”或明确指定某个版本号时，必须先核对官方 release 信息，再写课纲。对版本相关结论要显式写明：
   - 版本号
   - 官方发布日期
   - 本课纲中哪些专题是该版本特别值得新增或强化的内容
10. 如果用户要求“20 节课程”或“深度版”，不要引入额外的中间模板，直接输出 `标准版主课程 + 专题高阶课程` 的组合，并继续遵守“单课单主题”。

完整覆盖要求见 [topic-map.md](./references/topic-map.md)。按 lesson 组织课程时，优先参考 [syllabus-patterns.md](./references/syllabus-patterns.md)。

## 核心教学规则：单课单主题

这是本 skill 当前最重要的写作约束。

### 主规则

- 同一课默认只讲 `一个重要主题`
- 一个主题可以带少量紧邻子点，但不能跨不同问题域
- 如果一个标题里出现多个并列主题，优先怀疑这个标题是否应该拆成多课

### 可以作为同一课内部子点的情况

下面这些可以放在同一课里，但前提是它们只能作为同一主题内部的展开点，不能并列写进课时标题：

- `KV Cache` 一课里带出 block 生命周期与分配策略
- `EP` 一课里带出 token dispatch、all-to-all 与专家路由
- `Structured Outputs` 一课里带出 grammar backend 与 `StructuredOutputManager`
- `Tool Calling` 一课里带出接口语义与调度约束
- `Mamba 状态模型` 一课里带出 state cache 与 hybrid 适配边界

### 默认必须拆开的情况

下面这些默认应拆开：

- `Quantization` 和 `Speculative Decoding`
- `CUDA Graph` 和 `torch.compile`
- `torch.compile` 和 `ModelRunnerV2`
- `Kernel Fusions` 和 `ModelRunnerV2`
- `Speculative Decoding` 和 `DBO`
- `Attention Backend` 和 `重要模型结构`
- `Structured Outputs` 和 `Tool Calling`
- `Tool Calling` 和 `Tool Parser`
- `Reasoning Outputs` 和 `Reasoning Parser`
- `Weight Offloading` 和 `KV Offloading`
- `KV Offloading` 和 `KV Transfer`
- `DCP / PCP` 和 `Weight/KV Offloading`
- `PD 分离` 和 `多模态执行`
- `多模态执行` 和 `Transformers v5 兼容`
- `Dense` 和 `MoE`
- `Pooling` 和 `Reranker`

### 触发拆课的判断规则

只要满足任意一条，就优先拆课：

- 主题分别属于 `缓存/调度`、`编译/执行路径`、`分布式`、`offloading`、`输出控制`、`模型结构` 这几个不同问题域
- 主题各自都足以支撑 3 个以上核心知识点
- 主题分别对应不同源码入口或不同维护角色
- 把它们合在一起会让“为什么这一课重要”变得不够聚焦

### 主题过多时的处理方式

不要继续压缩到主课程里，优先：

1. 放入 `专题高阶课程`
2. 放入 `可选扩展课`
3. 放入 `母版总纲`，但不要强行塞进标准版主课程

### 主课程的实质内容约束

标准版主课程默认必须满足：

- 每一课都要有具体模块、具体链路、具体接口或具体运行能力作为主体
- 不能用纯包装性质的课题凑课时
- 标准版主课程默认只保留 vLLM 强链路主线与核心运行时
- 标准版主课程默认围绕 `模型初始化 -> 请求提交 -> engine client -> engine core -> scheduler -> continuous batching / chunked prefill -> worker/executor -> model runner -> kv cache / prefix caching / paged attention -> sampling / output` 组织
- `项目定位` 与 `版本演进` 默认写入课程说明、导论或 `架构全景` 开场，不单独列课
- `配置体系` 默认并入 `架构全景` 的附录或补充阅读
- `服务入口层` 默认并入 `请求生命周期` 或课程附录
- `输入处理与请求封装` 默认并入 `请求生命周期`
- `EngineCoreRequest 预处理与入队` 与 `RequestOutput 聚合与流式返回` 默认并入 `EngineClient 请求提交与输出回收`
- `核心数据对象` 默认并入对应功能课，不单独列课
- `源码阅读路径` 默认并入每课的 `推荐阅读文件` 和课程末尾附录，不单独列课
- 标题如果只有 `定位`、`演进`、`概览`、`入口` 这类导论词，而没有绑定具体模块或执行链路，默认不应进入标准版主课程
- `消息流`、`Serving`、`调优` 这类标题如果没有落实到具体通信机制、请求对象、入队路径、输出对象或 profiling 手段，也不应直接进入标准版主课程
- `LoRA / Multi-LoRA` 与 `多模态处理` 默认下放到专题高阶课程，不占标准版主课程课时
- `Continuous Batching`、`Chunked Prefill`、`Prefix Caching` 与 `PagedAttention` 已提升到标准版主课程，相关专题营中不再重复保留这些独立课时

### 模板课程与高阶课程去重规则

如果已经把某个主题下放到专题高阶课程，则：

- 主课程里不要再保留该主题的独立课时
- 主课程最多只保留一层导论性概览
- 如果课程由“主课程 + 专题营”组合而成，不要重复统计相同主题

## 必须覆盖的四大块

### 1. vLLM 项目总览与技术发展

至少回答下面这些问题：

- vLLM 是什么
- 它解决什么问题
- 它相比一般推理脚本或简单 serving 框架的价值是什么
- 它如何从单点优化演进成更完整的推理与服务平台

### 2. vLLM 总体架构全景

至少覆盖：

- 用户入口：Python `LLM`、CLI、OpenAI-compatible server
- 进程架构：API Server、Engine Core、GPU Worker、DP Coordinator
- 运行链路：请求进入、输入处理、调度、执行、输出回传
- 执行层级：entrypoint -> engine -> worker/executor -> model runner -> model

### 3. 核心重要组件

不能只列目录，必须解释职责、上下游关系和重要性。默认优先覆盖：

- `entrypoints`
- `engine` / `v1/engine`
- scheduler
- KV cache 与 block 管理
- worker / executor / model runner
- `model_executor`
- `distributed`
- `multimodal`
- `logits_process.py`、`sampling_params.py`、`sequence.py`
- `attention`、`kernels`、`compilation`

### 4. 重要特性

默认优先覆盖（括号标注归属层级）：

- PagedAttention（主课程）
- continuous batching（主课程）
- prefix caching（主课程）
- chunked prefill（主课程）
- quantization（专题营）
- speculative decoding（专题营）
- 分布式并行策略（专题营）
- 多模态支持（专题营）
- LoRA / Multi-LoRA（专题营）
- OpenAI-compatible serving（并入架构全景或请求生命周期）
- 编译与 kernel 优化（专题营）
- Weight Offloading 与 KV Offloading（专题营）
- PD 分离（专题营）
- Structured Outputs 与工具调用（专题营）
- Attention Backend 体系（专题营）
- 重要模型结构（专题营）

如果课纲明确对齐 `v0.19.0`，还应优先考虑把这些新版重点纳入高级专题：

- zero-bubble async scheduling + speculative decoding
- Model Runner V2 成熟化
- ViT full CUDA graphs
- 通用 CPU KV cache offloading
- DBO 泛化到通用模型
- Transformers v5 compatibility
- Gemma 4 support

## 分布式专题必须覆盖

只要用户要求“深度版”“20 节课”“系统梳理分布式”“源码级课程”，分布式部分默认不能只写 `TP / DP / EP` 三项，而应至少覆盖：

- `TP`：张量并行如何切分 attention / MLP 与通信位置
- `DP`：serving 场景下的数据并行、DP coordinator、engine core per DP rank
- `PP`：pipeline 切层、pipeline bubble、与 batch queue / runner 的关系
- `EP`：MoE serving、token dispatch、all-to-all、与 TP / DP 的组合
- `Elastic EP`：动态扩缩、world 初始化与服务连续性
- `EPLB`：专家负载均衡、冗余专家、eplb state
- `SP`：sequence parallel 的使用边界
- `DCP`：decode context parallel、KV cache 分片与长上下文 decode
- `PCP`：prefill context parallel、长上下文 prefill 切分

写作时默认说明三件事：

- 这个并行维度解决什么瓶颈
- 它改变了哪些通信或缓存布局
- 它和其他并行维度、调度策略、MoE / 长上下文 / KV cache 之间如何组合

如果用户明确要求主课程也纳入分布式部分，优先用 `分布式基础课 + 长上下文并行课 + 高阶分布式专题营` 的方式组织，不要在一课里把所有并行维度讲完。

## Attention Backend 与非标准注意力专题

如果用户要求“重要特性”“架构高级专题”“源码深读”，默认把 attention backend 单独成章，而不是并入 PagedAttention 一节。

至少覆盖：

- 常规 attention backend：FlashAttention、FlashInfer、MLA 等后端选择逻辑
- backend metadata builder 与 block size / kernel block size 约束
- 线性注意力或相关变体：例如 GDN / linear attention 路径
- Mamba / hybrid attention-state 模型
- attention cache 与 mamba state cache 的差异
- 后端选择如何影响 cache 布局、compile、CUDA graph、distributed communication

不要把 “attention backend” 误写成单纯的第三方库清单；重点是 vLLM 里的抽象层、元数据、约束传播和模型适配。

如果还想讲 `重要模型结构`，默认拆成下一课或下一专题，不和 backend 课强行合并。

## Offloading 与解耦执行专题

默认把下面这些主题视为运行时高级能力，而不是可选边角料：

- Weight Offloading：UVA zero-copy、prefetch、group-based layer offloading、selective parameter offloading
- KV Offloading：native CPU KV offloading、LMCache 相关后端、offloading manager 与缓存策略
- Weight Offloading 与 KV Offloading 的问题差异和性能权衡
- KV Transfer 与 connector 生态
- Prefill / Decode 分离，也就是 `PD 分离`
- Disaggregated Serving、Proxy / Router、实例发现、request_id 与路由关系

如果用户要求深度版课纲，Weight Offloading / KV Offloading 与 `PD 分离` 默认至少各占独立课时或独立一级专题。

## Structured Outputs、工具调用与输出控制专题

如果用户关心 OpenAI-compatible serving、agent、函数调用、受约束解码，默认覆盖：

- structured outputs 的业务动机
- grammar / bitmask / constrained decoding
- `StructuredOutputManager`
- tool calling
- named function calling / required tool choice 等典型接口语义
- reasoning outputs 与 structured outputs / tool calling 的组合边界
- parser / tool parser / reasoning parser 体系

不要把 tool calling 单独写成 API 使用说明，要把它放回 sampler、scheduler、输出解析和后端约束里讲。

如果还想讲 agent serving 的业务场景，默认放入同一专题营，而不是插入主课程任意一课。

## 重要模型结构必须覆盖

课程若面向“理解 vLLM 支持边界与模型适配”，默认把“重要模型结构”单独整理，而不是散落在模型支持列表中。

至少覆盖这些结构视角：

- Dense decoder-only Transformer
- MoE 模型
- Hybrid attention + mamba / linear attention 模型
- 多模态模型
- pooling / embedding / reranker 类模型
- reasoning / tool-calling 友好模型与 parser 差异
- 不同模型结构对 KV cache、attention backend、并行维度、structured outputs 的影响

## 课程目录模式

当用户要求“课程目录”“课纲”“第几课”“lesson 版大纲”“按课时拆分”时，优先使用课程目录模式。

### 课程目录默认格式

课程目录默认必须使用中文编号格式：

- `第1课-...`
- `第2课-...`
- `第3课-...`

不要默认写成：

- `Lesson 1`
- `Part 1`
- `Chapter 1`

默认采用这样的标题风格：

- `第1课-vLLM 环境搭建`
- `第2课-vLLM 架构全景`
- `第3课-vLLM 模型加载与初始化`
- `第4课-vLLM 请求生命周期`

### 每一课默认应包含

- `课程主题`
- `为什么这一课重要`
- `核心知识点`
- `学习目标`
- `推荐阅读文件`
- `建议练习或演示`

### 课程目录默认输出优先级

如果用户没有特别指定，默认优先输出：

1. `标准版主课程`
2. `专题高阶课程列表`
3. `母版总纲`

不要在没有要求时直接输出“大而全 20 课总纲”。
如果用户要求“严格单课单主题”，优先输出 `标准版主课程 + 专题高阶课程`。
如果用户只说“扩展到 20 节课”，默认理解为“标准版主课程后追加专题高阶课程”，而不是引入单独的深度版模板。

## 默认输出结构

如果用户要求正式文档、课程总纲或 lesson 化课纲，默认最终产出应为 Markdown 文档。

### 章节式课程总纲默认结构

1. `课程定位与适用对象`
2. `先修知识`
3. `vLLM 项目总览与技术发展`
4. `vLLM 总体架构全景`
5. `请求生命周期`
6. `核心重要组件`
7. `重要特性专题`
8. `分布式与运行时高级专题`
9. `重要模型结构与模型适配`
10. `推荐学习路径与源码入口`
11. `总结`

### 课程目录默认结构

如果用户明确要“课程目录”或“第几课”形式，默认输出：

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

### 默认课时规模

如果用户没有指定课时数，默认选择：

- `标准版主课程`：默认 15 课
- `专题高阶课程`：每营 3 到 6 课

如果用户明确要求“扩展到 20 节课程”，优先生成：

- `15 节标准版主课程 + 1 个 5 节专题营`

## 写作规则

- 最终正文默认必须用中文
- 课程名、章节名、每一课标题默认必须用中文
- 如果是课程目录模式，课时标题默认必须写成 `第X课-主题`
- 如果课纲对齐具体版本，开头默认写明 `基于 vLLM vX.Y.Z` 和该版本的官方发布日期
- 优先讲系统主线，不要一上来陷入单个模型或单个 kernel 细节
- 优先解释组件职责和请求链路，不要只罗列目录名
- 不要把特性写成营销清单
- 尽量把每一课都落到具体文档或源码入口
- 主课程中，默认一课只讲一个重要主题
- 如果一个课时标题里出现两个以上不同问题域，优先拆成多个课时
- 如果主题过多，优先分配到 `专题高阶课程`，不要硬塞进标准版主课程
- 如果某个主题已经在专题高阶课程中独立成课，主课程中不要重复保留该主题的独立课时
- `Quantization`、`CUDA Graph`、`torch.compile`、`Kernel Fusions`、`ModelRunnerV2` 默认视为五个不同问题域，优先拆成独立课时
- 深度版课纲里，不要把 `chunked prefill`、`TP/DP/PP/EP/Elastic EP/EPLB/SP/DCP/PCP`、`Weight/KV Offloading`、`PD 分离`、`Attention Backend`、`Structured Outputs / 工具调用`、`重要模型结构` 压缩进一两个大章节
- 如果用户要求“结合最新版本”，优先说明哪些专题是该版本需要强化的新重点

更细的覆盖维度、课程拆分模式和常见偏题点，见：

- [topic-map.md](./references/topic-map.md)
- [syllabus-patterns.md](./references/syllabus-patterns.md)
