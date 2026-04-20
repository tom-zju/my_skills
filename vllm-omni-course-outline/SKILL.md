---
name: vllm-omni-course-outline
description: 为 vLLM-Omni 生成中文权威硬核课程总纲、课程目录、学习大纲、知识地图和学习路径。适用于系统梳理 vLLM-Omni 环境基线、项目定位、AR/DiT 异构多阶段架构、stage configs、AsyncOmniEngine、Orchestrator、多阶段输出路由、中间表示设计、AR runtime、Diffusion runtime、Diffusion Attention、Diffusion Parallelism、TeaCache/cache-dit、OmniConnector、CFG Companion Flow、Fully Disaggregated Serving、Stage Input Processor、Qwen3-Omni 全链路案例，并按“单课单主题”原则设计 14 课硬核主课程的场景。
---

# vLLM-Omni 权威硬核课程大纲

## 核心约束速查

> 上下文压缩时优先保留本节。

1. **默认 14 课硬核主课程**：除非用户明确要求别的课时数，默认输出 `14 课权威硬核主课程`，不再默认拆专题营。
2. **单课单主题**：一课只讲一个重要主题；标题中出现多个问题域，优先拆课或改名。
3. **主课程只保留硬核内容**：环境基线、总体架构、stage configs、AsyncOmniEngine、Orchestrator、中间表示、AR runtime、Diffusion runtime、Diffusion Attention、Diffusion Parallelism、Diffusion Cache、OmniConnector/CFG、Stage Input Processor/Qwen3-Omni。
4. **外围内容默认不独立成课**：API 使用教学、ComfyUI、Helm、benchmark、metrics、profiler、模型列表综述、生态介绍默认不占独立主课。
5. **Diffusion 优化进入主课程**：Diffusion Attention、Diffusion Parallelism、TeaCache/cache-dit 默认进入 14 课主课程，不再作为可选专题营。
6. **版本先核对再写**：用户提到“最新版本/当前版本/指定版本/main 分支”时，先核对官方 release/tag、README Latest News、本地 tag/commit，再写课纲，并显式写明版本信息。
7. **中文优先**：正文、章节名、课时标题默认中文；代码标识符、路径、类名和配置字段保留英文原名。

---

## 总体说明

这个 skill 用来把 vLLM-Omni 整理成可教学、可分享、可沉淀的中文硬核课程材料。默认目标不是“大而全功能清单”，而是一份围绕源码主线和系统机制的权威课程大纲。

除非用户明确要求英文，否则正文、章节名、课程名、学习目标和说明文字都必须使用中文；代码标识符、目录名、文件路径、类名和配置字段保留英文原名。

本 skill 的默认教学设计原则是：`用 14 课主课程讲透 vLLM-Omni 的工程基线、异构多阶段执行、AR/DiT 双 runtime、Diffusion 优化、解耦连接器和模型适配闭环`。

## 适用场景

当用户有下面这些需求时使用本 skill：

- 要 vLLM-Omni 权威硬核课程大纲
- 要 vLLM-Omni 课程目录、学习大纲、学习路径或知识地图
- 要按课时拆分的团队培训、源码导读、内部分享或 onboarding 材料
- 要把 vLLM-Omni 仓库整理成中文教学版文档
- 要围绕 AsyncOmniEngine、Orchestrator、stage configs、AR/DiT runtime、Diffusion Attention/Parallelism/Cache、OmniConnector、CFG Companion Flow、Stage Input Processor 做系统课程设计
- 要把松散专题重新收敛成一套硬核主课程

如果用户只是问某个局部模块、某个类、某个 connector、某个模型 patch、某个 API 或某个实现细节，本 skill 不是首选，应改用更聚焦的专题分析方式。

## 默认 14 课主课程

课程目录模式下，默认直接使用下面这套主课程，不再默认输出专题营。

1. `第1课-vLLM-Omni 环境搭建、源码结构与运行基线`
2. `第2课-vLLM-Omni 项目定位与总体架构`
3. `第3课-Stage Configs 与异构多阶段 Pipeline 建模`
4. `第4课-AsyncOmniEngine 请求提交主链`
5. `第5课-Orchestrator 多阶段编排机制`
6. `第6课-多阶段输出路由与中间表示设计`
7. `第7课-AR Runtime：Scheduler、Worker 与执行主流程`
8. `第8课-AR ModelRunner、多模态 Payload 与 Hidden State 暴露`
9. `第9课-Diffusion Runtime：Engine、Scheduler 与 Pipeline`
10. `第10课-Diffusion Attention：Backend、Ring 与 Ulysses`
11. `第11课-Diffusion Parallelism：TP、SP、CFG、HSDP 与 VAE Patch Parallel`
12. `第12课-Diffusion Cache 加速：TeaCache 与 cache-dit`
13. `第13课-OmniConnector、CFG Companion Flow 与 Fully Disaggregated Serving`
14. `第14课-Stage Input Processor 与 Qwen3-Omni 全链路案例`

## 工作流程

1. 先判断输出模式：
   - `课程目录`：默认使用 14 课硬核主课程
   - `课程总纲`：围绕 14 课主课程展开章节式说明
   - `学习路径`：按“运行基线 -> 架构 -> 编排 -> runtime -> diffusion 优化 -> connector -> 案例”排序
   - `知识地图`：按系统模块关系组织
2. 再判断目标读者：
   - 新人入门但要读源码
   - 推理服务工程师
   - 多模态/生成式模型工程师
   - 要做 vLLM-Omni 二次开发的开发者
   - 要做扩散加速、解耦部署或模型接入的高阶研发
3. 默认叙事顺序保持为：
   - 工程运行基线
   - 项目定位与架构全景
   - stage configs 与异构 pipeline
   - AsyncOmniEngine 与 Orchestrator
   - 中间表示与输出路由
   - AR runtime
   - Diffusion runtime
   - Diffusion Attention / Parallelism / Cache
   - OmniConnector / CFG / Fully Disaggregated Serving
   - Stage Input Processor 与 Qwen3-Omni 案例
4. 先从仓库级材料建立全景，再深入源码。标注 `【必读】` 的是生成 14 课大纲时默认应覆盖的，标注 `【按需】` 的只在用户明确要求扩展时查阅：
   - `【必读】` `README.md`
   - `【必读】` `docs/getting_started/installation/`
   - `【必读】` `docs/getting_started/quickstart.md`
   - `【必读】` `docs/design/architecture_overview.md`
   - `【必读】` `docs/configuration/stage_configs.md`
   - `【必读】` `docs/design/module/async_omni_architecture.md`
   - `【必读】` `docs/design/module/ar_module.md`
   - `【必读】` `docs/design/module/dit_module.md`
   - `【必读】` `docs/design/feature/tensor_parallel.md`
   - `【必读】` `docs/design/feature/sequence_parallel.md`
   - `【必读】` `docs/design/feature/cfg_parallel.md`
   - `【必读】` `docs/design/feature/hsdp.md`
   - `【必读】` `docs/design/feature/vae_parallel.md`
   - `【必读】` `docs/design/feature/cache_dit.md`
   - `【必读】` `docs/design/feature/teacache.md`
   - `【必读】` `docs/design/feature/disaggregated_inference.md`
   - `【必读】` `docs/models/supported_models.md`
   - `【必读】` `vllm_omni/engine/`
   - `【必读】` `vllm_omni/core/sched/`
   - `【必读】` `vllm_omni/worker/`
   - `【必读】` `vllm_omni/diffusion/`
   - `【必读】` `vllm_omni/distributed/omni_connectors/`
   - `【必读】` `vllm_omni/model_executor/stage_input_processors/`
   - `【按需】` `docs/serving/`
   - `【按需】` `docs/features/comfyui.md`
   - `【按需】` `benchmarks/`
5. 对于每一课，都默认说明：
   - `课程主题`
   - `为什么这一课重要`
   - `核心知识点`
   - `学习目标`
   - `推荐阅读文件`
   - `建议练习或演示`
6. 如果用户要求“技术发展”或“演进路线”，优先使用“能力演进主线”，不要在没有核对版本和日期时硬写精确时间线。
7. 如果用户要求“最新版本/指定版本/main 分支”，按 [version-check-patterns.md](./references/version-check-patterns.md) 的模板先核对版本再写。

完整覆盖要求见 [topic-map.md](./references/topic-map.md)。按 lesson 组织课程时，优先参考 [syllabus-patterns.md](./references/syllabus-patterns.md)。涉及版本化要求时，优先参考 [version-check-patterns.md](./references/version-check-patterns.md)。

## 核心教学规则：单课单主题

### 主规则

- 同一课默认只讲 `一个重要主题`
- 一个主题可以带少量紧邻子点，但不能跨不同问题域
- 如果一个标题里出现多个并列主题，优先怀疑这个标题是否应该拆成多课
- 14 课主课程已经是默认权威模板，不要再自动拆出专题营

### 可以作为同一课内部子点的情况

- `环境搭建、源码结构与运行基线` 一课可以同时覆盖安装、目录、最小样例和调试入口，因为它们共同服务于源码课基线
- `Diffusion Attention` 一课可以带出 backend 与 Ring/Ulysses，因为它们都属于 attention 执行层
- `Diffusion Parallelism` 一课可以带出 TP、SP、CFG、HSDP、VAE Patch Parallel，因为它们共同回答 diffusion 路径的系统级切分
- `Diffusion Cache` 一课可以同时讲 TeaCache 与 cache-dit，因为它们共同回答 step execution 中的缓存加速
- `OmniConnector、CFG Companion Flow 与 Fully Disaggregated Serving` 一课可以合并，因为它们共同回答跨 stage artifact 与条件信息如何传递

### 默认必须拆开的情况

- `AsyncOmniEngine` 和 `Orchestrator`
- `Orchestrator` 和 `多阶段输出路由与中间表示设计`
- `AR Runtime 执行主流程` 和 `AR ModelRunner / Payload / Hidden State`
- `Diffusion Runtime` 和 `Diffusion Attention`
- `Diffusion Attention` 和 `Diffusion Parallelism`
- `Diffusion Parallelism` 和 `Diffusion Cache`
- `OmniConnector/CFG` 和 `Stage Input Processor/Qwen3-Omni 案例`
- `环境搭建` 和 `普通 API 使用教学`
- `Benchmark/Metrics/Profiler` 和 `硬核主课程`

## 必须覆盖的硬核主线

### 1. 工程运行基线

至少覆盖：

- 安装入口
- 仓库结构
- `vllm_omni/` 主目录
- offline / online 最小运行样例
- 后续源码调试基线

### 2. 架构全景

至少覆盖：

- vLLM-Omni 与 vLLM 的关系
- omni-modality
- AR + DiT
- heterogeneous outputs
- EntryPoints
- AsyncOmniEngine
- Orchestrator
- AR runtime
- Diffusion runtime
- OmniConnector

### 3. 多阶段建模与编排

至少覆盖：

- stage configs
- `stage_args`
- `engine_args`
- `runtime.edges`
- `engine_input_source`
- `prompt_expand_func`
- `cfg_kv_collect_func`
- `AsyncOmniEngine.add_request`
- `Orchestrator._request_handler`
- `_route_output`
- `_forward_to_next_stage`

### 4. 中间表示与输出路由

至少覆盖：

- `output_processor.py`
- `mm_outputs.py`
- `output_modality.py`
- `serialization.py`
- latent / hidden states / audio / text 的中间表示
- final output aggregation

### 5. AR Runtime

至少覆盖：

- `OmniARScheduler`
- `OmniGenerationScheduler`
- `GPUARWorker`
- `GPUGenerationWorker`
- `OmniGPUModelRunner`
- `GPUARModelRunner`
- prompt embedding overlay
- additional information serialization
- hidden state exposure
- `MultimodalOutputProcessor`

### 6. Diffusion Runtime 与优化

至少覆盖：

- `DiffusionEngine`
- diffusion scheduler
- worker process
- pipeline forward
- step execution
- VAE decode
- attention backend
- Ring / Ulysses
- TP / SP / CFG / HSDP / VAE Patch Parallel
- TeaCache
- cache-dit

### 7. 解耦执行与模型适配

至少覆盖：

- `OmniConnectorBase`
- artifact transfer
- metadata passing
- SharedMemory / Mooncake / Yuanrong
- CFG Companion Flow
- Fully Disaggregated Serving
- `stage_input_processors`
- Qwen3-Omni Thinker / Talker / Code2wav

## 默认不独立成课的内容

以下内容可以在相关课程中点到，但默认不独立占课时：

- OpenAI-compatible API 使用说明
- ComfyUI
- Helm
- benchmark
- metrics
- profiler
- custom pipeline
- 大而全模型支持列表
- LoRA
- CPU offload
- 单独的 quantization 课程

## 课程目录模式

当用户要求“课程目录”“课纲”“第几课”“lesson 版大纲”“按课时拆分”时，默认使用 14 课权威硬核主课程。

### 课程目录默认格式

课程目录默认必须使用中文编号格式：

- `第1课-vLLM-Omni 环境搭建、源码结构与运行基线`
- `第2课-vLLM-Omni 项目定位与总体架构`
- `第3课-Stage Configs 与异构多阶段 Pipeline 建模`

不要默认写成：

- `Lesson 1`
- `Part 1`
- `Chapter 1`

## 默认输出结构

如果用户要求正式文档、课程总纲或 lesson 化课纲，默认最终产出应为 Markdown 文档。

### 课程目录默认结构

- `课程说明`
- `课程总目标`
- `课程阶段划分`
- `14 课权威硬核主课程`
- `推荐配套阅读顺序`
- `课程压缩与扩展建议`

### 默认课时规模

如果用户没有指定课时数，默认选择：

- `权威硬核主课程`：默认 14 课

如果用户明确要求压缩：

- `8 课`：只保留架构、stage configs、AsyncOmniEngine、Orchestrator、AR、Diffusion、OmniConnector、Qwen3-Omni 案例
- `10 课`：保留中间表示与 Diffusion 优化总课
- `12 课`：拆出 Diffusion Attention 与 Parallelism，但可合并 Cache

## 写作规则

- 最终正文默认必须用中文
- 课程名、章节名、每一课标题默认必须用中文
- 如果是课程目录模式，课时标题默认必须写成 `第X课-主题`
- 如果课纲对齐具体版本，开头默认写明 `基于 vLLM-Omni vX.Y.Z` 和该版本的官方发布日期
- 优先讲系统主线，不要一上来陷入单个模型或单个 kernel 细节
- 优先解释组件职责和请求链路，不要只罗列目录名
- 不要把特性写成营销清单
- 尽量把每一课都落到具体文档或源码入口
- 主课程中，默认一课只讲一个重要主题
- 如果一个课时标题里出现两个以上不同问题域，优先拆成多个课时
- 如果主题过多，优先压缩外围内容，不要删掉硬核主线

更细的覆盖维度、课程拆分模式和常见偏题点，见：

- [topic-map.md](./references/topic-map.md)
- [syllabus-patterns.md](./references/syllabus-patterns.md)
- [version-check-patterns.md](./references/version-check-patterns.md)
