# SGLang 课程覆盖地图

这个参考文件用于保证课程总纲或课程目录不会退化成单一接口说明，或者只是一串 feature 名称。

## 一、最低覆盖面

一份完整的 SGLang 课程材料，默认至少覆盖五层：

1. `项目层`
   - SGLang 是什么
   - 为什么它既是 frontend language，也是 serving runtime
   - 它解决哪些 serving、agent、multimodal 与 rollout 问题
   - 它的能力如何演进
2. `架构层`
   - 从前端语言到 SRT runtime 的双层结构
   - 从入口到执行的总体结构
   - 请求生命周期
3. `组件层`
   - tokenizer manager
   - scheduler
   - schedule batch
   - tp worker
   - model runner
   - radix cache / hicache
   - attention backend
4. `特性层`
   - radixattention
   - continuous batching
   - chunked prefill
   - structured outputs
   - PD/EPD
   - parallelism
   - quantization
   - lora
5. `高级运行时层`
   - hicache
   - tool parser / reasoning parser
   - deterministic inference
   - multimodal encoder dp / cuda graph
   - model gateway

## 二、推荐阅读顺序

默认按这个顺序建立全景：

1. 官方文档首页：`https://docs.sglang.io/`
2. 官方仓库：`https://github.com/sgl-project/sglang`
3. `README.md`
4. `Install SGLang`
5. `OpenAI-Compatible APIs`
6. `Offline Engine API`
7. `SGLang Native APIs`
8. `Sampling Parameters`
9. `Attention Backend`
10. `Structured Outputs`
11. `Tool Parser`
12. `Reasoning Parser`
13. `PD Disaggregation`
14. `Hierarchical KV Caching (HiCache)`
15. `python/sglang/srt/entrypoints/`
16. `python/sglang/srt/server_args.py`
17. `python/sglang/srt/managers/`
18. `python/sglang/srt/mem_cache/`
19. `python/sglang/srt/layers/attention/`
20. `python/sglang/srt/models/`
21. `sgl-model-gateway/`

如果用户要求对齐“最新版本”或“最新代码”，还应补充查阅：

22. 官方 release/tag 页面：`https://github.com/sgl-project/sglang/releases`
23. 主仓库 `main` 分支当前代码结构

## 三、课程设计优先级

本 skill 的课程设计优先级如下：

1. `同一课只讲一个重要主题`
2. `主课程保持主线连贯`
3. `高阶主题拆到专题课程`
4. `最后才考虑总课时数是否好看`

## 四、专题覆盖清单

### 1. 基础主线

默认至少回答：

- SGLang 的定位、价值与演进路径
- Frontend Language 与 SRT runtime 的关系
- 从 API / Offline Engine 到 tokenizer manager / scheduler / tp worker / model runner 的执行主链

### 2. 调度与缓存

默认至少覆盖：

- zero-overhead cpu scheduler
- schedule batch
- continuous batching
- chunked prefill
- radixattention
- prefix reuse / radix cache
- hicache

### 3. 并行与解耦

深度版或源码版课程默认至少覆盖：

- `TP`
- `DP / DPA / DP Router`
- `EP`
- `Pipeline Parallelism for Long Context`
- `PD Disaggregation`
- `EPD Disaggregation`

### 4. 输出控制与推理模型

默认至少覆盖：

- `Structured Outputs`
- `Structured Outputs For Reasoning Models`
- `Tool Parser`
- `Reasoning Parser`
- `Deterministic Inference`

### 5. 执行优化与能力扩展

默认至少覆盖：

- `Speculative Decoding`
- `Attention Backend`
- `Quantization`
- `Quantized KV Cache`
- `LoRA Serving`
- `多模态 Encoder DP / CUDA Graph`
- `Model Gateway`
- `Observability`

## 五、单课单主题检查清单

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
- 标准版主课程默认只保留 SGLang 强链路主线与核心运行时
- 标准版主课程默认按 `启动与入口 -> 请求进入 -> tokenizer / scheduler -> schedule batch -> continuous batching / chunked prefill -> radix attention / cache -> worker / model runner -> attention backend -> structured generation -> disaggregation / hicache` 的执行流排序
- `项目定位`、`版本演进`、`Server Arguments`、`OpenAI-Compatible APIs`、`Offline Engine API`、`SGLang Native APIs`、`Sampling Parameters`、`源码阅读路径` 默认不单独列课
- `Speculative Decoding`、`并行细分维度`、`EPD Disaggregation`、`Model Gateway`、`多模态扩展` 默认下放到专题高阶课程

### 2. 专题高阶课程

适合：

- 并行与解耦专项
- 输出控制专项
- 缓存与执行优化专项
- 多模态与能力扩展专项

默认要求：

- 每营只保留一条技术主线
- 每课继续执行单课单主题

## 七、常见偏题点

- 只讲 OpenAI-Compatible API，不讲 SRT runtime 主链
- 只讲前端语言语法，不讲 serving runtime
- 只列 feature 名字，不解释这些 feature 在系统中的位置
- 未核实就写成精确版本时间线
- 把 `structured outputs`、`tool parser`、`reasoning parser` 重新并成一课
- 把 `PD`、`EPD`、`HiCache`、`Model Gateway` 全压成“高级特性”一节
- 把 `RadixAttention` 写成单纯的 prefix cache 口号，而不讲 radix cache / reuse 路径
