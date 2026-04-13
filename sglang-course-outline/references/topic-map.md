# SGLang 课程覆盖地图

这个参考文件用于保证课程总纲或课程目录不会退化成单一接口说明，或者只是一串 feature 名称。

## 一、最低覆盖面

一份完整的 SGLang 课程材料，默认至少覆盖四层主线；只有在扩展版、专题版或源码深讲场景下，再追加按需专题层：

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
4. `主线特性层`
   - radixattention
   - continuous batching
   - chunked prefill
   - structured outputs
   - PD
   - hicache
   - attention backend
5. `按需专题层`
   - EPD
   - tool parser / reasoning parser
   - deterministic inference
   - speculative decoding
   - quantization
   - lora
   - multimodal encoder dp / cuda graph
   - model gateway
   - observability

## 二、推荐阅读顺序

默认按这个顺序建立主线全景：

1. 官方文档首页：`https://docs.sglang.io/`
2. 官方仓库：`https://github.com/sgl-project/sglang`
3. `README.md`
4. `Install SGLang`
5. `OpenAI-Compatible APIs`
6. `Offline Engine API`
7. `SGLang Native APIs`
8. `Attention Backend`
9. `Structured Outputs`
10. `PD Disaggregation`
11. `Hierarchical KV Caching (HiCache)`
12. `python/sglang/srt/entrypoints/`
13. `python/sglang/srt/server_args.py`
14. `python/sglang/srt/managers/`
15. `python/sglang/srt/mem_cache/`
16. `python/sglang/srt/layers/attention/`
17. `python/sglang/srt/model_executor/`

按需专题再补充查阅：

18. `Sampling Parameters`
19. `Tool Parser`
20. `Reasoning Parser`
21. `python/sglang/srt/parser/`
22. `python/sglang/srt/function_call/`
23. `python/sglang/srt/disaggregation/`
24. `python/sglang/srt/distributed/`
25. `python/sglang/srt/multimodal/`
26. `python/sglang/srt/lora/`
27. `python/sglang/srt/models/`
28. `python/sglang/srt/speculative/`
29. `sgl-model-gateway/`

如果用户要求对齐“最新版本”或“最新代码”，还应补充查阅：

- 官方 release/tag 页面：`https://github.com/sgl-project/sglang/releases`
- 主仓库 `main` 分支当前代码结构

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

只有当用户明确要求 agent、函数调用、推理模型、受约束解码或输出协议专题时，才默认覆盖：

- `Structured Outputs`（若是标准版主课程，它可作为主线强特性保留）
- `Structured Outputs For Reasoning Models`
- `Tool Parser`
- `Reasoning Parser`
- `Deterministic Inference`

不要为了“覆盖面完整”把这些主题自动回填到 `15 课标准版主课程`。

### 5. 执行优化与能力扩展

只有当用户明确要求专项、扩展版或源码深讲时，才默认覆盖：

- `Speculative Decoding`
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
- `Structured Outputs`、`PD Disaggregation` 与 `HiCache` 允许作为 SGLang 主线强特性进入标准版主课程

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
- 把 `PD`、`EPD`、`HiCache`、`Model Gateway` 全压成”高级特性”一节
- 把 `RadixAttention` 写成单纯的 prefix cache 口号，而不讲 radix cache / reuse 路径

## 八、反例 vs 正例对比

### 反例：把 Tool Parser 和 Reasoning Parser 合并成一课

```
第X课-Tool Parser 与 Reasoning Parser
核心知识点：
- 函数调用格式解析
- 推理模型输出解析
- 两者的共同接口
```

**问题**：Tool Parser 属于”输出格式与函数调用”问题域，Reasoning Parser 属于”推理模型输出控制”问题域，两者源码入口不同、维护角色不同，各自都有 3 个以上核心知识点，合并后”为什么这一课重要”无法聚焦。

### 正例：拆成两课

```
第X课-Tool Parser
为什么重要：函数调用是 agent 场景的核心能力，Tool Parser 负责把模型输出映射成结构化工具调用。
核心知识点：模型输出格式约定、解析边界、与 structured outputs 的关系
推荐阅读：官方文档中的 `Tool Parser` 页面，以及当前仓库中对应的 parser 实现入口

第X+1课-Reasoning Parser
为什么重要：推理模型（如 DeepSeek-R1）输出包含 <think> 段，Reasoning Parser 负责分离推理过程与最终答案。
核心知识点：推理模型输出结构、think/answer 分离逻辑、与 structured outputs for reasoning models 的衔接
推荐阅读：官方文档中的 `Reasoning Parser` 页面，以及当前仓库中对应的 reasoning parser 实现入口
```

### 反例：把 PD / EPD / HiCache / Model Gateway 压成一节

```
第X课-高级特性：PD 解耦、EPD 解耦、HiCache 与 Model Gateway
```

**问题**：四个主题分属”解耦 serving”、”多级缓存”、”服务路由”三个不同问题域，每个都足以支撑独立课时，合并后无法给出聚焦的学习目标和推荐阅读路径。

### 正例：按问题域拆课并分配到合适层级

```
主课程：
  第14课-PD Disaggregation（主线强特性，进主课程）
  第15课-HiCache（主线强特性，进主课程）

专题高阶课程（并行与解耦专题营）：
  第5课-EPD Disaggregation

专题高阶课程（Serving 生态专题营）：
  第1课-SGLang Model Gateway
```
