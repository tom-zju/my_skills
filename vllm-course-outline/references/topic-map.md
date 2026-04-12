# vLLM 课程覆盖地图

这个参考文件用于保证课程总纲或课程目录不会退化成单一模型分析，或者只是一串特性名称。

## 一、最低覆盖面

一份完整的 vLLM 课程材料，默认至少覆盖五层：

1. `项目层`
   - vLLM 是什么
   - 为什么需要它
   - 它解决哪些 serving / inference 问题
   - 它的能力如何演进
2. `架构层`
   - 从入口到执行的总体结构
   - 多进程组织方式
   - 请求生命周期
3. `组件层`
   - scheduling
   - KV cache
   - worker / model runner
   - model executor
   - distributed
   - multimodal
   - sampling / logits
4. `特性层`
   - throughput
   - memory efficiency
   - caching
   - parallelism
   - multimodality
   - quantization
   - speculative decoding
   - service interfaces
5. `高级运行时层`
   - offloading
   - PD 分离
   - attention backend
   - structured outputs / tool calling
   - 重要模型结构

## 二、推荐阅读顺序

默认按这个顺序建立全景：

1. `README.md`
2. `RELEASE.md`
3. `docs/design/arch_overview.md`
4. `docs/design/paged_attention.md`
5. `docs/design/prefix_caching.md`
6. `docs/design/model_runner_v2.md`
7. `docs/design/mm_processing.md`
8. `docs/design/torch_compile.md`
9. `docs/configuration/optimization.md`
10. `docs/usage/v1_guide.md`
11. `docs/features/structured_outputs.md`
12. `docs/features/tool_calling.md`
13. `docs/serving/parallelism_scaling.md`
14. `docs/serving/data_parallel_deployment.md`
15. `docs/serving/expert_parallel_deployment.md`
16. `docs/serving/context_parallel_deployment.md`
17. `vllm/entrypoints/`
18. `vllm/v1/`
19. `vllm/model_executor/`
20. `vllm/distributed/`

如果用户要求对齐 `v0.19.0`，还应补充查阅官方 release：

21. `https://github.com/vllm-project/vllm/releases/tag/v0.19.0`

并优先检查这些新版主题是否应进入课程：

- zero-bubble async scheduling
- Model Runner V2
- ViT full CUDA graphs
- CPU KV cache offloading
- DBO generalization
- Transformers v5 compatibility

## 三、课程设计优先级

本 skill 的课程设计优先级如下：

1. `同一课只讲一个重要主题`
2. `主课程保持主线连贯`
3. `高阶主题拆到专题课程`
4. `最后才考虑总课时数是否好看`

如果这四条冲突，优先级从上到下依次更高。

## 四、专题覆盖清单

### 1. 基础主线

默认至少回答：

- vLLM 的定位、价值与演进路径
- 从 API / CLI / `LLM` 到 engine / worker / model 的执行主链路
- scheduler、KV cache、model runner、sampling 的互相耦合关系

### 2. 缓存与调度

默认至少覆盖：

- PagedAttention
- KV cache block 管理
- prefix caching
- `chunked prefill`
- continuous batching
- speculative decoding

这部分不要只写“提升吞吐”；要说明：

- token budget 如何影响调度
- chunked prefill 与 prefix caching 的关系
- chunked prefill 与 multimodal / pooling / PD 分离的边界

如果采用专题营模式，建议将下面这些继续拆开：

- `Chunked Prefill`
- `Prefix Caching`
- `Speculative Decoding`
- `DBO`

### 3. 分布式并行

深度版或源码版课程默认至少覆盖：

- `TP`
- `DP`
- `PP`
- `EP`
- `Elastic EP`
- `EPLB`
- `SP`
- `DCP`
- `PCP`

写作时建议从三条线讲：

- 切分对象：参数、层、token、KV cache、专家
- 通信形态：all-reduce、all-gather、reduce-scatter、all-to-all
- 运行时影响：scheduler、KV cache duplication、MoE dispatch、长上下文

### 4. Offloading 与解耦执行

默认至少覆盖：

- `Weight Offloading`
- `KV Offloading`
- `KV Transfer`
- `PD 分离`
- `Disaggregated Serving`

要明确区分：

- weight offload 主要针对权重驻留问题
- KV offload 主要针对 KV cache 容量与冷热管理
- PD 分离解决的是 prefill / decode 负载与 SLO 解耦

### 4.5 编译与执行路径

如果用户要求更细的高阶课程，建议把下面这些主题分别独立成课：

- `Quantization`
- `CUDA Graph`
- `torch.compile`
- `Kernel Fusions`
- `ModelRunnerV2`
- `执行路径重构`

### 5. Attention Backend 与状态模型

默认至少覆盖：

- 常规 attention backend 抽象
- FlashAttention / FlashInfer / MLA 等典型后端
- linear attention / GDN 路径
- `mamba`
- hybrid attention + state 模型
- attention cache 与 mamba state cache 的差异

如果整理成课程目录，默认拆成：

- `Attention Backend 抽象`
- `Dense Attention Backend 选择`
- `Linear Attention`
- `Mamba 状态模型`
- `Hybrid Attention 模型`

### 6. 输出控制与交互接口

默认至少覆盖：

- `Structured Outputs`
- grammar / bitmask / constrained decoding
- `StructuredOutputManager`
- `tool calling`
- `tool parser`
- `reasoning outputs`
- `reasoning parser`

如果整理成课程目录，默认拆成独立课时，不要把 `Structured Outputs`、`Tool Calling`、`Parser`、`Reasoning Outputs` 压回一课。

### 7. 重要模型结构

默认至少覆盖：

- Dense decoder-only
- MTP
- MoE
- hybrid attention
- mamba / linear attention 状态模型
- multimodal
- pooling
- reranker
- reasoning / tool-calling 友好模型

如果整理成课程目录，默认不要把 `Dense`、`MTP`、`MoE`、`Pooling`、`Reranker`、`多模态结构` 合并成单课。

## 五、单课单主题检查清单

在输出课程目录前，逐课检查下面这些问题：

- 这一课能不能用一句话说明“只解决哪个核心问题”
- 这课的推荐阅读文件是否集中在一个问题域
- 这课的核心知识点是否都围绕同一条执行链路
- 如果把其中一半内容删掉，剩下的一半是否还能独立成课

如果以上任一项回答不稳，说明这课大概率过宽，需要拆课。

## 六、默认课程包装方式

### 1. 主课程

适合：

- onboarding
- 工程入门
- 系统主线培训

默认要求：

- 单课单主题
- 优先连贯主线
- 高阶专题尽量下放
- 默认按 `15 课` 组织
- 每一课都必须有具体模块、具体链路、具体接口或具体运行能力作为主体
- 标准版主课程默认只保留 vLLM 强链路主线与核心运行时
- 标准版主课程默认按 `模型初始化 -> 请求提交 -> engine client -> engine core -> scheduler -> continuous batching / chunked prefill -> worker/executor -> model runner -> kv cache / prefix caching / paged attention -> sampling / output` 的执行流排序
- `项目定位`、`版本演进`、`配置体系`、`服务入口层`、`输入处理与请求封装`、`核心数据对象`、`源码阅读路径` 默认不单独列课，而是并入相邻功能课或课程附录
- 标题如果只有 `定位`、`演进`、`概览`、`入口` 这类导论词，而没有绑定具体模块或执行链路，默认不应进入标准版主课程
- `消息流`、`Serving`、`调优` 这类标题如果没有落实到具体通信机制、请求对象、入队路径、输出对象或 profiling 手段，也不应直接进入标准版主课程
- `LoRA / Multi-LoRA` 与 `多模态处理` 默认下放到专题高阶课程，不占标准版主课程课时
- `Continuous Batching`、`Chunked Prefill`、`Prefix Caching` 与 `PagedAttention` 已提升到标准版主课程，相关专题营中不再重复保留这些独立课时
- `EngineCoreRequest 预处理与入队` 与 `RequestOutput 聚合与流式返回` 若进入主课程，优先合并到 `EngineClient 请求提交与输出回收` 一课，而不是各自拆成独立主课

### 2. 专题高阶课程

适合：

- 分布式专项
- 调度与缓存专项
- 高级 serving 专项
- attention backend / 模型结构专项
- agent serving 专项

默认要求：

- 每营只保留一条技术主线
- 每课继续执行单课单主题

### 3. 母版总纲

适合：

- 课程设计者
- 讲师备课
- 全景知识盘点

默认要求：

- 允许覆盖更全
- 但仍不鼓励同一课混装多个不相邻主题
- 母版若需要控制在固定课时数内，优先写成“主课程 + 专题营组合”，不要为了课时好看重新并课

## 七、主课程与专题课程去重规则

如果采用“主课程 + 专题高阶课程”模式，输出前检查：

- 主课程中是否还保留了专题营里同名或同问题域的独立课时
- 是否把“导论概览”和“独立深讲课时”混为一谈
- 深度版组合是否重复统计了同一主题

默认做法是：

- 主课程保留主线
- 专题课程保留深讲
- 不在两个模板里重复安排同一主题的独立课时

## 八、常见偏题点

- 只讲单个模型实现，不讲项目和系统架构
- 只列 feature 名字，不解释这些 feature 在系统中的位置
- 只列目录结构，不讲请求生命周期
- 未核实就写成精确版本时间线
- 想写课程目录，结果只输出普通章节标题
- 写了 lesson 版课纲，却没有分布式、优化、系统演进这些高级运行时专题
- 用户明确要求“结合最新版本”，却没有核对官方 release 就直接沿用旧模板
- 把 `chunked prefill`、`TP/DP/PP/EP/Elastic EP/EPLB/SP/DCP/PCP`、`Weight/KV Offloading`、`PD 分离`、`Attention Backend`、`Structured Outputs / 工具调用`、`重要模型结构` 全都压成“高级特性”一节
- 讲 attention backend 时只报第三方库名，不讲 vLLM 的抽象层和约束传播
- 讲 tool calling 时只讲接口用法，不讲 structured outputs backend、parser 与 decoding 约束
- 为了凑课时数，把不同问题域硬塞进同一课
- 主课程没有降噪，导致标准班和专题营的边界不清
- 把 `Quantization`、`CUDA Graph`、`torch.compile`、`Kernel Fusions`、`ModelRunnerV2` 重新并回一课
- 把 `Dense / MoE / Pooling / Reranker / 多模态结构` 重新并成“重要模型结构”一课
- 把 `Structured Outputs / Tool Calling / Parser / Reasoning Outputs` 重新并成“Agent Serving 高级特性”一课
