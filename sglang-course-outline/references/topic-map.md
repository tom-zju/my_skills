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
   - onboarding / quickstart
   - radixattention
   - continuous batching
   - chunked prefill
   - parallelism overview / detail
   - speculative decoding
   - quantization basics / practice
   - PD
   - hicache
   - attention backend
5. `特性专项层`
   - DeepSeek 系列模型结构
   - Kimi 系列模型结构
   - Qwen 系列模型结构
   - LLM 长文本优化专题
   - SGLang 性能优化端到端专题

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
9. `python/sglang/srt/entrypoints/`
10. `python/sglang/srt/server_args.py`
11. `python/sglang/srt/managers/`
12. `python/sglang/srt/mem_cache/`
13. `python/sglang/srt/layers/attention/`
14. `python/sglang/srt/model_executor/`
15. `python/sglang/srt/distributed/`
16. `Speculative Decoding`
17. `Quantization`

按需补充专题再查阅：

18. `python/sglang/srt/models/`
19. `python/sglang/srt/speculative/`
20. `python/sglang/srt/disaggregation/`
21. `vLLM 官方文档与源码`
22. 输出控制、函数调用与解析器相关文档和源码
23. `Sampling Parameters`

如果用户要求对齐“最新版本”或“最新代码”，还应补充查阅：

- 官方 release/tag 页面：`https://github.com/sgl-project/sglang/releases`
- 主仓库 `main` 分支当前代码结构

## 三、课程设计优先级

本 skill 的课程设计优先级如下：

1. `同一课只讲一个重要主题`
2. `主课程保持主线连贯`
3. `高阶主题拆到专题课程`
4. `最后才考虑总课时数是否好看`
5. `用户要求详细课纲时，优先同时给出主课程与专题课程，并附真实可核验的阅读资料`

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

标准版主课程默认至少覆盖：

- `并行体系总览（TP / DP / SP / PP / EP）`
- `并行机制细讲（TP / DP / DPA / DP Router / SP / EP / PP）`
- `PD Disaggregation`

如果用户要求“深度版”或“源码版课程”，再额外覆盖：

- `TP`
- `DP / DPA / DP Router`
- `SP`
- `Pipeline Parallelism for Long Context`
- `EP`
- 解耦式 serving 的按需扩展主题
- `DPA / DP Router` 的源码级路由细节

### 4. 大模型结构专题

只有当用户明确要求模型结构专题时，才默认覆盖：

- `DeepSeek 系列`
- `Kimi 系列`
- `Qwen 系列`
- `python/sglang/srt/models/` 中对应实现与适配点

不要为了“覆盖面完整”把这些模型结构专题自动回填到标准版主课程。

### 5. 长文本优化专题

只有当用户明确要求长文本专题时，才默认覆盖：

- `长文本场景的问题定义与背景`
- `模型侧、框架侧与算子侧的优化点和解决方案`
- `长文本优化中的工程落地、方案选型与排障补充`

### 6. 端到端性能优化专题

只有当用户明确要求专项、扩展版或源码深讲时，再覆盖：

- `SGLang 性能优化流程与步骤`
- `Profiling 与瓶颈定位`
- `性能优化中的关键专项与实战补充`

### 7. 按需补充专题

只有当用户单独要求相关内容时，再补充：

- `输出控制、函数调用与解析器相关扩展`
- `路由治理、观测与工程化补充`
- `多模态、LoRA 与解耦扩展主题`

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
- 默认按 `19 课` 组织
- 每一课都必须有具体模块、具体链路、具体接口或具体运行能力作为主体
- 标准版主课程默认覆盖 SGLang 强链路主线、并行体系、执行优化与解耦缓存
- 标准版主课程默认按 `介绍与快速上手 -> 架构与入口 -> 请求进入 -> tokenizer / scheduler -> schedule batch -> continuous batching / chunked prefill -> radix attention / cache -> worker / model runner -> attention backend -> parallelism overview / detail -> speculative decoding -> quantization basics / practice -> disaggregation / hicache` 的执行流排序
- `项目定位`、`版本演进`、`Server Arguments`、`OpenAI-Compatible APIs`、`Offline Engine API`、`SGLang Native APIs`、`Sampling Parameters`、`源码阅读路径` 默认不单独列课
- `大模型结构专题`、`LLM 长文本优化专题营`、`LLM 模型性能优化端到端专题营` 默认放到专题高阶课程
- `并行体系总览（TP / DP / SP / PP / EP）`、`并行机制细讲`、`Speculative Decoding`、`Quantization 基础与原理`、`Quantization 模块解析与实践`、`PD Disaggregation` 与 `HiCache` 默认进入标准版主课程

### 2. 专题高阶课程

适合：

- 大模型结构专题
- LLM 长文本优化专题
- LLM 模型性能优化端到端专题
- 按需补充专题

默认要求：

- 每营只保留一条技术主线
- 每课继续执行单课单主题
- 当前默认专题高阶课程以 `DeepSeek / Kimi / Qwen 模型结构`、`LLM 长文本优化专题营`、`LLM 模型性能优化端到端专题营` 为主
- 输出控制、工程治理、多模态和其他扩展主题仅在用户单独要求时作为按需补充专题追加，不属于当前默认三大专项

### 3. 详细课纲输出

如果用户明确要求“一份详细的 SGLang 课程大纲”，默认应：

- 同时输出 `标准版主课程` 与 `专题高阶课程`
- 使用结构完整的 Markdown 文档组织内容
- 每一课至少包含 `课程主题`、`为什么重要`、`核心知识点`、`学习目标`、`推荐阅读文件资料`、`建议练习或演示`
- `推荐阅读文件资料` 优先使用官方文档、官方 GitHub 仓库和可核验的源码路径

## 七、常见偏题点

- 只讲 OpenAI-Compatible API，不讲 SRT runtime 主链
- 只讲前端语言语法，不讲 serving runtime
- 只列 feature 名字，不解释这些 feature 在系统中的位置
- 未核实就写成精确版本时间线
- 把 `DeepSeek / Kimi / Qwen`、`长文本优化`、`端到端性能优化` 全压回主课程
- 把 `PD`、`EPD`、`HiCache` 全压成”高级特性”一节
- 把 `RadixAttention` 写成单纯的 prefix cache 口号，而不讲 radix cache / reuse 路径

## 八、反例 vs 正例对比

### 反例：把 DeepSeek / Kimi / Qwen 压成一课

```
第X课-DeepSeek、Kimi 与 Qwen 模型结构
核心知识点：
- DeepSeek 结构特征
- Kimi 长上下文设计
- Qwen 服务适配差异
```

**问题**：DeepSeek、Kimi、Qwen 各自对应不同结构重点、适配策略和阅读路径，强行压成一课后“为什么这一课重要”很难聚焦，也不利于后续延展到长文本和性能优化专题。

### 正例：拆成三课

```
第X课-DeepSeek 系列模型结构与推理特征
为什么重要：DeepSeek 系列在推理模型、MoE 组织和部署约束上有鲜明特征。
核心知识点：核心结构、推理特征、对 serving 的影响
推荐阅读：`python/sglang/srt/models/` 中相关模型实现与适配逻辑

第X+1课-Kimi 系列模型结构与长上下文设计
为什么重要：Kimi 系列的长上下文设计与 KV 管理思路直接影响长文本专题的展开。
核心知识点：长上下文结构、缓存压力、服务适配
推荐阅读：对应模型实现、长文本设计说明与相关适配入口

第X+2课-Qwen 系列模型结构与服务适配
为什么重要：Qwen 系列在社区落地广，理解其结构与服务适配对工程教学价值高。
核心知识点：结构特征、常见 serving 适配点、部署差异
推荐阅读：对应模型实现与配置适配入口
```

### 反例：把模型结构、长文本优化、端到端性能优化压成一节

```
第X课-高级特性：模型结构、长文本优化与性能优化
```

**问题**：三类专题分别对应模型认知、长文本瓶颈、性能优化流程三个不同问题域，合并后无法形成清晰的学习路径，也很难落到具体阅读材料。

### 正例：按问题域拆课并分配到合适层级

```
主课程：
  第18课-PD Disaggregation（主线强特性，进主课程）
  第19课-HiCache（主线强特性，进主课程）

专题高阶课程（大模型结构专题营）：
  第1课-DeepSeek 系列模型结构与推理特征

专题高阶课程（LLM 长文本优化专题营）：
  第2课-模型侧、框架侧与算子侧的优化点和解决方案

专题高阶课程（LLM 模型性能优化端到端专题营）：
  第2课-Profiling 链路与瓶颈定位
```
