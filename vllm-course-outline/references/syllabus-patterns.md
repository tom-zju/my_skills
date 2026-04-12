# vLLM 课程目录模板

这个参考文件用于生成“第几课”形式的课程目录，而不是普通章节式文档。

## 来源说明

本文件综合了两类来源：

- 当前 vLLM 仓库的文档与代码结构
- 仓库内已有的课程化整理材料

另外，本次模板升级已核对官方 GitHub Release：

- `vLLM v0.19.0`
- 官方发布日期：`2026-04-03`
- 官方来源：`https://github.com/vllm-project/vllm/releases/tag/v0.19.0`

如果用户要求“结合最新版本”或直接提到 `v0.19.0`，优先按该 release 的新增重点更新课程。

## 课程目录输出总规则

只要用户要求“课程目录”“课纲”“学习大纲”“按课时拆分”，默认优先输出 lesson 化课程目录。

### 标题格式要求

课程目录默认必须使用下面这种标题格式：

1. `第1课-...`
2. `第2课-...`
3. `第3课-...`

不要默认使用英文标题格式，例如：

- `Lesson 1`
- `Week 1`
- `Chapter 1`

### 最重要规则：单课单主题

课程目录默认必须遵守：

- 一课只讲一个重要主题
- 如果一课标题中出现多个不同问题域，应优先拆课
- 模板主课程不负责吞掉所有高级专题
- 高阶主题应优先拆到专题课程

### 重要约束：模板课程与高阶课程不重复

如果采用“模板主课程 + 专题高阶课程”的组织方式，必须遵守：

- 已经下放到专题高阶课程的主题，不要再在模板主课程里保留同名独立课时
- 模板主课程可以保留“导论性概览”，但不能再保留“独立深讲课时”
- 深度版若由主课程加专题营组合而成，也不要重复计算相同主题

## 模板一：标准版主课程

适用于：

- 团队培训
- 工程入门课
- 需要真正拿去讲的主课程

推荐课时：

- `15 课`

默认目录：

1. `第1课-vLLM v0.19.0 环境搭建`
2. `第2课-vLLM 架构全景`
3. `第3课-vLLM 模型加载与初始化`
4. `第4课-vLLM 请求生命周期`
5. `第5课-vLLM EngineClient 请求提交与输出回收`
6. `第6课-vLLM Engine Core`
7. `第7课-vLLM 调度主流程`
8. `第8课-vLLM Continuous Batching`
9. `第9课-vLLM Chunked Prefill`
10. `第10课-vLLM Worker 与 Executor`
11. `第11课-vLLM ModelRunner 执行主链`
12. `第12课-vLLM KV Cache 管理`
13. `第13课-vLLM Prefix Caching`
14. `第14课-vLLM PagedAttention`
15. `第15课-vLLM Sampling 与输出生成`

说明：

- 标准版主课程默认固定为 `15 课`
- 标准版主课程默认只保留 vLLM 强链路主线与核心组件
- 标准版主课程默认围绕 `模型初始化 -> 请求提交 -> engine client -> engine core -> scheduler -> continuous batching / chunked prefill -> worker/executor -> model runner -> kv cache / prefix caching / paged attention -> sampling / output` 组织
- 每一课都必须落到具体链路、模块、接口或运行能力，不能用只有包装意义的元信息课凑课时
- `项目定位` 与 `版本演进` 不再单独成课，默认写入课程说明、导论或 `架构全景` 的开场部分
- `配置体系` 不再单独成课，默认作为 `架构全景` 的附录或补充阅读
- `服务入口层` 不再单独成课，默认并入 `请求生命周期` 或课程附录
- `输入处理与请求封装` 不再单独成课，默认并入 `请求生命周期`
- `EngineCoreRequest 预处理与入队` 与 `RequestOutput 聚合与流式返回` 默认并入 `EngineClient 请求提交与输出回收`
- `核心数据对象` 不再单独成课，默认并入 `请求生命周期`、`调度主流程`、`Sampling 与输出生成`、`KV Cache 管理` 等具体功能课
- `源码阅读路径` 不再单独成课，默认分散到每一课的 `推荐阅读文件`，并在课程末尾统一给出阅读顺序附录
- 标题如果只有 `定位`、`演进`、`概览`、`入口` 这类导论词，而没有绑定具体模块或执行链路，默认不应进入标准版主课程
- `LoRA / Multi-LoRA` 与 `多模态处理` 默认不进入标准版主课程，应下放到专项课程
- `Continuous Batching`、`Chunked Prefill`、`Prefix Caching` 与 `PagedAttention` 已提升到标准版主课程，相关专题营中不再重复保留这些独立课时
- `消息流`、`Serving`、`调优` 这类标题如果没有落实到具体通信机制、请求对象、入队路径、输出对象或 profiling 手段，也不应直接进入标准版主课程
- 下面这些主题不再作为主课程独立课时：
  - `Speculative Decoding`
  - `DBO`
  - `Quantization`
  - `CUDA Graph`
  - `torch.compile`
  - `Kernel Fusions`
  - `ModelRunnerV2`
  - `Attention Backend`
  - `Structured Outputs`
  - `Tool Calling`
  - `Reasoning Outputs`
  - `TP / PP / DP / EP / Elastic EP / EPLB / SP / DCP / PCP`
  - `LoRA / Multi-LoRA`
  - `多模态处理`
  - `Weight Offloading / KV Offloading / KV Transfer`
  - `PD 分离 / Disaggregated Serving / Sleep Mode`
  - `Dense / MTP / MoE / Pooling / Reranker / 多模态结构`
  - `Transformers v5 compatibility`
  - `parallel_state 与分布式执行接线`
  - `Metrics 与 Profiling`

## 模板三：专题高阶课程

适用于：

- 不希望主课程过载
- 需要把高阶主题拆开讲深
- 团队内部专项培训

专题课程默认每营 `3 到 6 课`，并继续执行单课单主题。

### A. 调度专题营

1. `第1课-Scheduler token budget 分配`
2. `第2课-RequestQueue 与优先级队列`
3. `第3课-Speculative Decoding`
4. `第4课-DBO 批间重叠执行`

说明：

- 本专题营接管所有调度深讲主题
- 如果 `Continuous Batching` 与 `Chunked Prefill` 已提升到标准版主课程，本专题营中不再重复保留这些独立课时
- 模板主课程中不再重复保留这些主题的独立课时

### B. 缓存专题营

1. `第1课-Block Table`
2. `第2课-Slot Mapping`
3. `第3课-Block 回收与重用`

说明：

- 本专题营接管缓存机制深讲
- 如果 `Prefix Caching` 与 `PagedAttention` 已提升到标准版主课程，本专题营中不再重复保留这些独立课时
- 模板主课程中保留的是 `KV Cache 管理` 这一层系统主线，不再单独深讲这里的其他主题

### C. 基础并行专题营

1. `第1课-Tensor Parallel 切分与通信`
2. `第2课-Pipeline Parallel 分层与气泡`
3. `第3课-Data Parallel Serving 编排`
4. `第4课-Expert Parallel 路由与通信`

说明：

- 本专题营接管基础并行维度深讲
- 模板主课程中只保留“分布式推理概览”

### D. 高阶并行专题营

1. `第1课-Elastic EP 动态扩缩`
2. `第2课-EPLB 专家负载均衡`
3. `第3课-Sequence Parallel 激活切分`
4. `第4课-DCP Decode Context Parallel`
5. `第5课-PCP Prefill Context Parallel`

说明：

- 本专题营接管高阶并行与长上下文并行
- 模板主课程中不再重复保留这些主题的独立课时

### E. Offloading 专题营

1. `第1课-Weight Offloading 权重预取与驻留`
2. `第2课-KV Offloading 冷热迁移`
3. `第3课-KV Transfer Connector`

说明：

- 本专题营接管混合内存与缓存迁移

### F. 解耦式 Serving 专题营

1. `第1课-PD 分离 请求拆分与路由`
2. `第2课-Disaggregated Serving 实例发现与转发`
3. `第3课-Sleep Mode 显存让渡与恢复`

说明：

- 本专题营接管解耦式运行时主题

### G. Attention Backend 专题营

1. `第1课-Attention Backend 抽象与元数据构建`
2. `第2课-Dense Attention Backend 选择与约束传播`
3. `第3课-Linear Attention 执行路径`
4. `第4课-Mamba 状态模型执行`
5. `第5课-Hybrid Attention/State 模型适配`

说明：

- 本专题营接管 attention backend 与非标准注意力

### H. 模型结构专题营

1. `第1课-Dense Decoder-Only 结构`
2. `第2课-MTP 家族结构`
3. `第3课-MoE 结构`
4. `第4课-Pooling 结构`
5. `第5课-Reranker 结构`
6. `第6课-多模态模型结构`

说明：

- 本专题营接管重要模型结构

### I. Agent Serving 专题营

1. `第1课-Structured Outputs`
2. `第2课-Constrained Decoding`
3. `第3课-Tool Calling`
4. `第4课-Tool Parser`
5. `第5课-Reasoning Outputs`
6. `第6课-Reasoning Parser`

说明：

- 本专题营接管 agent serving 输出控制主题

### J. 编译优化专题营

1. `第1课-Quantization`
2. `第2课-CUDA Graph`
3. `第3课-torch.compile`

说明：

- 本专题营接管编译优化与量化

### K. 执行路径专题营

1. `第1课-Kernel Fusions 融合算子路径`
2. `第2课-ModelRunnerV2 执行改造`
3. `第3课-BatchExecutionDescriptor 批执行编排`

说明：

- 本专题营接管执行路径重构主题

### L. LoRA 专题营

1. `第1课-LoRA Adapter 注册与热加载`
2. `第2课-Multi-LoRA 批内路由`
3. `第3课-LoRA 状态注册与批内切换`

说明：

- 本专题营接管 LoRA 与适配器相关主题

### M. 多模态专题营

1. `第1课-多模态输入预处理`
2. `第2课-多模态 Encoder 执行`
3. `第3课-多模态 Encoder Cache`

说明：

- 本专题营接管多模态处理主链

## 拆课规则

如果用户没有点名课时数，但明确要求“系统性整理”“源码深读”“涵盖分布式与高级特性”，优先按下面的拆课原则组织：

- 主课程先保持纯净，再决定需要补哪些专题营
- 如果用户要求 18 到 20 节，直接在 `15 节标准版主课程` 后追加合适的专题营，不单独引入“模板二”
- `Speculative Decoding`、`DBO` 默认优先进入专题营
- `TP / PP / DP / EP / Elastic EP / EPLB / SP / DCP / PCP` 默认优先进入专题营
- `Weight Offloading`、`KV Offloading`、`KV Transfer`、`PD 分离`、`Disaggregated Serving`、`Sleep Mode` 默认优先进入专题营
- `Attention Backend`、`Linear Attention`、`Mamba`、`Hybrid Attention` 默认优先进入专题营
- `LoRA / Multi-LoRA`、`多模态处理` 默认优先进入专题营
- `Dense / MTP / MoE / Pooling / Reranker / 多模态结构` 默认优先进入专题营
- `Structured Outputs`、`Constrained Decoding`、`Tool Calling`、`Tool Parser`、`Reasoning Outputs`、`Reasoning Parser` 默认优先进入专题营
- `Quantization`、`CUDA Graph`、`torch.compile`、`Kernel Fusions`、`ModelRunnerV2` 默认优先进入专题营
- 若用户显式要求某个高阶主题进入主课程，则需要同步从对应专题营中移除该独立课时，避免重复

## 每一课默认结构

课程目录模式下，每一课默认应包含：

- `课程主题`
- `为什么这一课重要`
- `核心知识点`
- `学习目标`
- `推荐阅读文件`
- `建议练习或演示`
