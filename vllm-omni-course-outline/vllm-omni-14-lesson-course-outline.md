# vLLM-Omni 14 课权威硬核主课程说明文档

## 1. 课程定位

本课程是一套面向源码导读、架构理解与工程实现的 `vLLM-Omni 14 课权威硬核主课程`。

课程不以外围生态、API 使用演示或产品化包装为中心，而是围绕 vLLM-Omni 最核心的系统问题展开：

- vLLM-Omni 为什么不是普通多模态服务封装层
- AR 与 Diffusion 双路径为什么必须在统一框架中协同
- 多阶段 pipeline 如何由 stage configs、engine 与 orchestrator 驱动
- 多模态 payload、hidden state、中间表示与跨 stage artifact 如何流动
- Diffusion Attention、Parallelism、Cache 为什么必须进入主课程
- Qwen3-Omni 这类模型如何真正接入并跑通整条执行链路

## 2. 适用对象

本课程适用于以下人群：

- 需要系统理解 `vLLM-Omni` 源码结构与执行主线的研发工程师
- 需要为团队搭建多模态推理服务研发培训体系的技术负责人
- 需要理解 `AR + Diffusion + 多阶段编排` 的系统设计者
- 需要完成 `Qwen3-Omni` 或相近 omni 模型接入、调试与优化的工程人员

本课程不以以下目标为主：

- 单纯学习 OpenAI API 调用方式
- 只想快速上手一个 demo 而不关心源码
- 只关注 ComfyUI、Helm、benchmark、metrics 或部署脚本
- 只想研究单一局部模块而不建立系统全景

## 3. 课程目标

完成课程后，学习者应具备以下能力：

- 能解释 vLLM-Omni 的整体系统定位与核心架构分层
- 能读懂 stage configs，并理解它如何驱动异构多阶段 pipeline
- 能跟踪请求从 `AsyncOmniEngine` 进入，到 `Orchestrator` 编排，再到各 stage runtime 执行的主链
- 能理解 AR runtime 与 Diffusion runtime 的职责差异与协同关系
- 能说明多模态 payload、hidden state 与中间表示在跨 stage 流程中的作用
- 能解释 `Diffusion Attention`、`Diffusion Parallelism`、`TeaCache/cache-dit` 在系统中的工程价值
- 能理解 `OmniConnector`、`CFG Companion Flow` 与 fully disaggregated serving 的设计目标
- 能结合 `Qwen3-Omni` 案例完成从输入处理到最终输出的全链路复盘

## 4. 学习前置要求

- 熟悉 Python 工程项目结构与基本调试方法
- 对 LLM serving、scheduler、worker、model runner 等基础概念有基本认知
- 对 Diffusion 模型、并行训练或推理有基本概念性了解
- 能阅读 YAML 配置、Markdown 设计文档与 Python 源码

## 5. 课程设计原则

- 默认采用 `14 课` 主课程结构
- 严格遵守 `单课单主题`
- 主课程优先覆盖源码级、架构级、runtime 级硬核内容
- `Diffusion Attention`、`Diffusion Parallelism`、`TeaCache/cache-dit` 全部纳入主课程
- `环境搭建` 纳入第 1 课，但定位为源码运行基线，而不是普通安装教程
- `OmniConnector` 作为主课程硬核内容，与 `CFG Companion Flow` 和 fully disaggregated serving 一并讲解
- 不默认拆出专题营
- 不默认把外围生态内容挤入主课程

## 6. 课程结构总览

1. 第1课-vLLM-Omni 环境搭建、源码结构与运行基线
2. 第2课-vLLM-Omni 项目定位与总体架构
3. 第3课-Stage Configs 与异构多阶段 Pipeline 建模
4. 第4课-AsyncOmniEngine 请求提交主链
5. 第5课-Orchestrator 多阶段编排机制
6. 第6课-多阶段输出路由与中间表示设计
7. 第7课-AR Runtime：Scheduler、Worker 与执行主流程
8. 第8课-AR ModelRunner、多模态 Payload 与 Hidden State 暴露
9. 第9课-Diffusion Runtime：Engine、Scheduler 与 Pipeline
10. 第10课-Diffusion Attention：Backend、Ring 与 Ulysses
11. 第11课-Diffusion Parallelism：TP、SP、CFG、HSDP 与 VAE Patch Parallel
12. 第12课-Diffusion Cache 加速：TeaCache 与 cache-dit
13. 第13课-OmniConnector、CFG Companion Flow 与 Fully Disaggregated Serving
14. 第14课-Stage Input Processor 与 Qwen3-Omni 全链路案例

## 7. 14 课详细说明

### 第1课-vLLM-Omni 环境搭建、源码结构与运行基线

**课程主题**

建立源码学习、最小运行、日志定位与调试的统一工程基线。

**为什么这一课重要**

如果环境、目录结构和最小运行链路没有稳定建立，后续架构分析和源码追踪都会失去抓手。这一课是后面 13 课的运行前提。

**核心知识点**

- 安装路径与依赖结构
- 快速启动方式与最小运行样例
- 仓库目录分层
- `engine`、`model_executor`、`diffusion`、`distributed` 的职责边界
- 示例脚本与调试入口

**学习目标**

- 能独立完成基础环境准备
- 能跑通至少一个 `qwen3_omni` 相关示例
- 能说清仓库中的核心目录应该从哪里开始阅读
- 能找到关键日志与调试入口

**推荐阅读文件**

- `README.md`
- `docs/getting_started/installation/README.md`
- `docs/getting_started/quickstart.md`
- `examples/online_serving/qwen3_omni/README.md`

**建议练习**

- 在本地跑通一个 `qwen3_omni` 示例
- 画出“入口命令 -> engine -> stage config -> model”最小调用路径

### 第2课-vLLM-Omni 项目定位与总体架构

**课程主题**

理解 vLLM-Omni 的系统定位、设计目标与全局架构分层。

**为什么这一课重要**

如果把 vLLM-Omni 误解成普通多模态 API 封装层，后续对 stage pipeline、AR runtime、Diffusion runtime 和 connector 的理解都会失真。

**核心知识点**

- omni-modality serving 的目标
- AR 与 Diffusion 双路径协同
- 异构多阶段 pipeline 的总体形态
- 输出模态与执行分层
- 与纯 LLM serving 或纯 diffusion serving 的区别

**学习目标**

- 能解释 vLLM-Omni 的系统定位
- 能概述核心模块之间的关系
- 能说明它与普通多模态服务框架的关键区别

**推荐阅读文件**

- `docs/design/architecture_overview.md`
- `docs/source/architecture/qwen3-omni-async-chunk.png`
- `docs/source/architecture/qwen3-omni-non-async-chunk.png`

**建议练习**

- 画出一张高层架构图，标出入口层、编排层、AR 路径、Diffusion 路径和输出层

### 第3课-Stage Configs 与异构多阶段 Pipeline 建模

**课程主题**

理解 stage configs 如何把模型结构、执行单元与系统编排连接起来。

**为什么这一课重要**

stage configs 不是简单的 YAML 参数说明，而是整个异构多阶段系统的控制面入口。看不懂 stage configs，就看不懂系统如何运行。

**核心知识点**

- stage schema
- stage 间依赖关系
- worker 与 scheduler 的配置绑定
- pipeline 的组织方式
- 不同模型的 stage config 差异

**学习目标**

- 能读懂一个完整的 stage config
- 能解释每个 stage 的功能与上下游关系
- 能说明 stage config 如何驱动 runtime 行为

**推荐阅读文件**

- `docs/configuration/stage_configs.md`
- `vllm_omni/config/stage_config.py`
- `vllm_omni/model_executor/stage_configs/qwen3_omni_moe.yaml`
- `vllm_omni/model_executor/stage_configs/qwen3_omni_moe_async_chunk.yaml`

**建议练习**

- 对比 `qwen3_omni_moe.yaml` 与 `qwen3_omni_moe_async_chunk.yaml`
- 总结 async chunk 对 pipeline 拆分与调度的影响

### 第4课-AsyncOmniEngine 请求提交主链

**课程主题**

理解请求如何从入口进入异步多阶段执行系统。

**为什么这一课重要**

这一课定义了请求进入系统时的生命周期起点，是理解 engine、orchestrator 和 stage 执行协作的入口。

**核心知识点**

- `AsyncOmniEngine` 的角色
- 请求提交与封装
- engine 初始化与 stage 启动
- 异步执行主链
- 输出模态相关入口控制

**学习目标**

- 能从入口代码跟踪一次请求如何进入系统
- 能理解 `AsyncOmniEngine` 在整体架构中的职责
- 能区分 engine 与 orchestrator 的边界

**推荐阅读文件**

- `vllm_omni/engine/async_omni_engine.py`
- `vllm_omni/engine/arg_utils.py`
- `vllm_omni/engine/stage_init_utils.py`

**建议练习**

- 从一个 serving 示例出发，整理“请求进入 engine”这一段的关键调用栈

### 第5课-Orchestrator 多阶段编排机制

**课程主题**

理解 Orchestrator 如何在多阶段系统中协调请求推进与阶段切换。

**为什么这一课重要**

Orchestrator 是多阶段执行的总控中心。理解它，才能理解为什么 vLLM-Omni 不是简单的串行 stage 调用。

**核心知识点**

- Orchestrator 的职责边界
- 请求状态推进
- stage 间切换逻辑
- handler 循环
- 输出汇聚与阶段完成条件

**学习目标**

- 能解释 Orchestrator 为什么是系统核心对象
- 能梳理一次多 stage 请求的状态推进过程
- 能描述 orchestrator 与 stage engine core 之间的协作

**推荐阅读文件**

- `vllm_omni/engine/orchestrator.py`
- `vllm_omni/engine/stage_engine_core_client.py`
- `vllm_omni/engine/stage_engine_core_proc.py`

**建议练习**

- 选取一个跨两个以上 stage 的请求，画出请求状态流转图

### 第6课-多阶段输出路由与中间表示设计

**课程主题**

理解 stage 之间如何通过中间表示、输出路由与序列化机制协同工作。

**为什么这一课重要**

多阶段系统的扩展能力，很大程度上取决于中间表示是否稳定、输出路由是否清晰、数据传递是否结构化。

**核心知识点**

- 中间 artifact
- 输出路由
- 序列化与反序列化
- 多模态输出封装
- scheduler output 与 model runner output 中的附加信息

**学习目标**

- 能说明中间表示的系统价值
- 能理解输出对象如何被上游生产、下游消费
- 能解释 output processor 在链路中的作用

**推荐阅读文件**

- `vllm_omni/engine/mm_outputs.py`
- `vllm_omni/engine/output_processor.py`
- `vllm_omni/engine/serialization.py`
- `vllm_omni/core/sched/output.py`

**建议练习**

- 选择一个 stage 间传递对象，梳理其完整生命周期

### 第7课-AR Runtime：Scheduler、Worker 与执行主流程

**课程主题**

进入 AR 路径的 runtime 主链，理解 scheduler、worker 和执行循环。

**为什么这一课重要**

AR runtime 是理解文本推理、多模态前段处理与前向执行机制的关键部分。它为后续 hidden state 和多阶段协同打基础。

**核心知识点**

- `OmniARScheduler`
- `GPUARWorker`
- worker 基类与运行循环
- AR 路径的执行组织方式
- scheduler 与 worker 的职责分离

**学习目标**

- 能讲清 AR runtime 主流程
- 能理解 scheduler 和 worker 在 AR 路径中的分工
- 能将 AR stage 与 stage config 对应起来

**推荐阅读文件**

- `vllm_omni/core/sched/omni_ar_scheduler.py`
- `vllm_omni/worker/gpu_ar_worker.py`
- `vllm_omni/worker/base.py`

**建议练习**

- 结合一个 stage config，说明 AR stage 为什么绑定当前 scheduler 与 worker

### 第8课-AR ModelRunner、多模态 Payload 与 Hidden State 暴露

**课程主题**

理解 AR 路径中 model runner 如何处理多模态 payload，并暴露 hidden state 供后续 stage 使用。

**为什么这一课重要**

这一层决定了多模态输入如何真正进入模型，也决定了后续 stage 能否获得足够的中间语义表示。

**核心知识点**

- `GPUARModelRunner`
- `OmniGPUModelRunner`
- payload 注入
- hidden state 更新与暴露
- omni-specific runner output

**学习目标**

- 能说明 payload 如何被注入 runner
- 能解释 hidden state 为何重要
- 能理解 AR 路径为何要暴露额外中间结果

**推荐阅读文件**

- `vllm_omni/worker/gpu_ar_model_runner.py`
- `vllm_omni/worker/gpu_model_runner.py`
- `vllm_omni/inputs/data.py`

**建议练习**

- 跟踪一个 payload 字段从输入到 runner 输出的传播过程

### 第9课-Diffusion Runtime：Engine、Scheduler 与 Pipeline

**课程主题**

理解 Diffusion 路径的 engine、scheduler、worker 与 stepwise pipeline。

**为什么这一课重要**

Diffusion runtime 是 vLLM-Omni 覆盖图像、视频、音频生成类能力的核心基础，也是它区别于普通 LLM serving 的关键一环。

**核心知识点**

- `DiffusionEngine`
- request scheduler 与 step scheduler
- `DiffusionWorker`
- `DiffusionModelRunner`
- stepwise execution

**学习目标**

- 能说明 Diffusion runtime 的主要对象及职责
- 能解释 diffusion request 如何被调度与推进
- 能对比 AR runtime 和 Diffusion runtime 的根本差异

**推荐阅读文件**

- `vllm_omni/diffusion/diffusion_engine.py`
- `vllm_omni/diffusion/sched/request_scheduler.py`
- `vllm_omni/diffusion/sched/step_scheduler.py`
- `vllm_omni/diffusion/worker/diffusion_worker.py`
- `vllm_omni/diffusion/worker/diffusion_model_runner.py`

**建议练习**

- 画出一个 diffusion request 从入队到 step 执行完成的状态推进图

### 第10课-Diffusion Attention：Backend、Ring 与 Ulysses

**课程主题**

理解 diffusion attention 的 backend 抽象与并行后端实现。

**为什么这一课重要**

attention backend 是 diffusion 性能扩展的关键支点。不了解这一层，就无法真正理解 diffusion runtime 的性能设计。

**核心知识点**

- attention backend 抽象
- backend selector
- Ring attention
- Ulysses
- backend 适用场景与切换逻辑

**学习目标**

- 能解释 diffusion attention 为什么要独立设计
- 能比较 Ring 和 Ulysses 的问题指向
- 能理解 backend 选择如何影响性能与扩展性

**推荐阅读文件**

- `docs/user_guide/diffusion_features.md`
- `vllm_omni/diffusion/attention/selector.py`
- `vllm_omni/diffusion/attention/parallel/ring.py`
- `vllm_omni/diffusion/attention/parallel/ulysses.py`
- `vllm_omni/diffusion/attention/backends/registry.py`

**建议练习**

- 比较 Ring 与 Ulysses 的设计目标与适用场景

### 第11课-Diffusion Parallelism：TP、SP、CFG、HSDP 与 VAE Patch Parallel

**课程主题**

系统理解 diffusion 路径中的多种并行策略。

**为什么这一课重要**

Diffusion 的系统级性能扩展依赖并行切分策略。只有理解 TP、SP、CFG、HSDP 和 VAE patch parallel 的差异，才能设计真正可扩展的部署方案。

**核心知识点**

- tensor parallel
- sequence parallel
- CFG parallel
- HSDP
- VAE patch parallel
- 分布式通信与协调机制

**学习目标**

- 能概括各类并行策略的定位
- 能根据任务形态选择合适的组合
- 能理解并行策略与系统资源结构的关系

**推荐阅读文件**

- `docs/user_guide/diffusion/parallelism/overview.md`
- `docs/user_guide/diffusion/parallelism/tensor_parallel.md`
- `docs/user_guide/diffusion/parallelism/sequence_parallel.md`
- `docs/user_guide/diffusion/parallelism/cfg_parallel.md`
- `docs/user_guide/diffusion/parallelism/hsdp.md`
- `docs/user_guide/diffusion/parallelism/vae_patch_parallel.md`

**建议练习**

- 为一个大分辨率图像或视频生成场景设计并行策略组合，并说明理由

### 第12课-Diffusion Cache 加速：TeaCache 与 cache-dit

**课程主题**

理解 diffusion 路径中的缓存加速机制与其系统影响。

**为什么这一课重要**

TeaCache 与 cache-dit 并不是边角优化，而是影响 step execution 成本结构的重要机制，是“硬核版”课程不可缺少的一环。

**核心知识点**

- TeaCache 的设计目标
- cache-dit 的加速思路
- 缓存命中与状态管理
- 收益、限制与潜在副作用

**学习目标**

- 能说明两类缓存机制分别解决什么问题
- 能理解缓存策略对执行效率与结果质量的影响
- 能识别适合引入缓存优化的场景

**推荐阅读文件**

- `docs/user_guide/diffusion/cache_acceleration/teacache.md`
- `docs/user_guide/diffusion/cache_acceleration/cache_dit.md`
- `docs/design/feature/teacache.md`
- `vllm_omni/diffusion/cache/teacache/backend.py`
- `vllm_omni/diffusion/cache/cache_dit_backend.py`

**建议练习**

- 对比 TeaCache 与 cache-dit 的缓存粒度、触发条件与潜在风险

### 第13课-OmniConnector、CFG Companion Flow 与 Fully Disaggregated Serving

**课程主题**

理解跨 stage、跨进程、跨节点的数据传输抽象与解耦执行机制。

**为什么这一课重要**

这门课回答了 vLLM-Omni 如何稳定地在异构多阶段系统中传递 artifact、条件信息与中间状态，是系统扩展能力的关键。

**核心知识点**

- `OmniConnectorBase`
- connector 工厂与不同 connector 实现
- transfer adapter
- metadata 与 artifact 传输
- `CFG Companion Flow`
- fully disaggregated serving

**学习目标**

- 能解释 OmniConnector 的系统定位
- 能理解 connector 不是普通序列化工具
- 能说明它与 fully disaggregated serving 的关系

**推荐阅读文件**

- `docs/design/feature/disaggregated_inference.md`
- `docs/design/feature/omni_connectors/shared_memory_connector.md`
- `docs/design/feature/omni_connectors/mooncake_transfer_engine_connector.md`
- `vllm_omni/distributed/omni_connectors/connectors/base.py`
- `vllm_omni/distributed/omni_connectors/factory.py`
- `vllm_omni/distributed/omni_connectors/transfer_adapter/chunk_transfer_adapter.py`

**建议练习**

- 结合 multiconnector 配置，梳理一次跨 stage artifact 的完整传输过程

### 第14课-Stage Input Processor 与 Qwen3-Omni 全链路案例

**课程主题**

以 Qwen3-Omni 为案例，把前 13 课的架构、配置、runtime 与连接器机制收口成完整闭环。

**为什么这一课重要**

如果没有真实案例复盘，前面的知识点会停留在局部。案例课负责把配置、输入处理、执行链路与输出回到一条真实路径上。

**核心知识点**

- stage input processor 的职责
- Qwen3-Omni 的输入规整与路由
- 模型接入路径
- stage 间切换与执行闭环
- 端到端链路复盘

**学习目标**

- 能结合 Qwen3-Omni 说明完整执行路径
- 能解释 stage input processor 在模型接入中的作用
- 能把前 13 课知识串成一条系统主线

**推荐阅读文件**

- `docs/user_guide/examples/online_serving/qwen3_omni.md`
- `examples/online_serving/qwen3_omni/README.md`
- `vllm_omni/model_executor/stage_input_processors/qwen3_omni.py`
- `vllm_omni/model_executor/models/qwen3_omni/qwen3_omni.py`
- `vllm_omni/model_executor/stage_configs/qwen3_omni_moe.yaml`

**建议练习**

- 从 `qwen3_omni` 示例出发，写一份全链路执行解剖，覆盖输入处理、stage 切换、AR 路径与生成路径

## 8. 建议授课节奏

- 适合按 `14 次课` 讲授，每次 2 到 3 小时
- 如果面向源码训练营，可采用 `讲解 90 分钟 + 源码 walkthrough 45 分钟 + 练习讨论 30 分钟`
- 如果面向团队 onboarding，可优先保证前 9 课完整，再安排第 10 到第 14 课作为高阶强化段

## 9. 建议配套实践

- 每课至少安排一个源码跟踪练习
- 第 3、5、9、13、14 课建议要求输出流程图或状态图
- 第 10、11、12 课建议要求对比不同优化机制的适用条件
- 结课建议安排一次 `Qwen3-Omni 全链路复盘` 作为综合作业

## 10. 不纳入主课程的内容

以下内容可以按需补充，但默认不占用主课程课时：

- OpenAI-compatible API 基础调用
- ComfyUI 集成
- Helm、部署脚本与生产化运维细节
- benchmark、metrics、profiler 的系统化专题
- 非核心生态集成说明

## 11. 结语

这套 14 课课程的目标，不是把 vLLM-Omni 讲成一个“功能列表”，而是把它讲成一套真正可解释、可调试、可扩展、可接入的 omni serving 系统。

如果继续扩展，最自然的下一步不是再加外围课程，而是围绕本主课程继续补充：

- 讲师版讲稿
- 课堂源码 walkthrough 提纲
- 每课配套图示
- 结课考核题
