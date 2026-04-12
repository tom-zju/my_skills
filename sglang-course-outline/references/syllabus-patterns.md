# SGLang 课程目录模板

这个参考文件用于生成“第几课”形式的课程目录，而不是普通章节式文档。

## 来源说明

本文件综合了三类来源：

- SGLang 官方文档：`https://docs.sglang.io/`
- SGLang 官方 GitHub 仓库：`https://github.com/sgl-project/sglang`
- SGLang 官方 release/tag 页面与 `main` 主线代码结构

本次模板升级创建时，已核对：

- 官方 release tag：`v0.5.10.post1`
- 官方发布日期：`2026-04-09`
- 以及主仓库 `main` 的当前代码结构

如果用户要求“结合最新版本”“结合最新代码”“main 分支”“最近实现”，优先重新核对官方 release/tag 与主仓库代码，再写课程。

## 课程目录输出总规则

只要用户要求“课程目录”“课纲”“学习大纲”“按课时拆分”，默认优先输出 lesson 化课程目录。

### 标题格式要求

课程目录默认必须使用下面这种标题格式：

1. `第1课-...`
2. `第2课-...`
3. `第3课-...`

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

1. `第1课-SGLang 最新版环境搭建`
2. `第2课-SGLang 双层体系架构全景`
3. `第3课-SGLang 请求生命周期与 TokenizerManager`
4. `第4课-SGLang Scheduler 主流程`
5. `第5课-SGLang ScheduleBatch 组批与状态推进`
6. `第6课-SGLang Continuous Batching`
7. `第7课-SGLang Chunked Prefill`
8. `第8课-SGLang RadixAttention`
9. `第9课-SGLang Radix Cache 前缀复用`
10. `第10课-SGLang TPWorker 执行编排`
11. `第11课-SGLang ModelRunner 执行主链`
12. `第12课-SGLang Attention Backend`
13. `第13课-SGLang Structured Outputs`
14. `第14课-SGLang PD Disaggregation`
15. `第15课-SGLang HiCache`

说明：

- 标准版主课程默认固定为 `15 课`
- 标准版主课程默认只保留 SGLang 强链路主线与核心组件
- 标准版主课程默认围绕 `启动与入口 -> 请求进入 -> tokenizer / scheduler -> schedule batch -> continuous batching / chunked prefill -> radix attention / prefix reuse -> worker / model runner -> attention backend -> structured generation -> disaggregation / hicache` 组织
- `项目定位`、`版本演进`、`Server Arguments`、`OpenAI-Compatible APIs`、`Offline Engine API`、`SGLang Native APIs`、`Sampling Parameters`、`源码阅读路径` 默认并入相邻功能课或附录
- `Speculative Decoding`、`Quantization`、`并行细分维度`、`EPD Disaggregation`、`Model Gateway`、`多模态扩展` 默认不进入标准版主课程，应下放到专项课程
- `Structured Outputs`、`PD Disaggregation` 与 `HiCache` 是 SGLang 强特性，允许进入标准版主课程

## 模板三：专题高阶课程

### A. 并行与解耦专题营

1. `第1课-Tensor Parallel 切分与通信`
2. `第2课-DP / DPA / DP Router`
3. `第3课-Expert Parallelism`
4. `第4课-Pipeline Parallelism for Long Context`
5. `第5课-EPD Disaggregation`

### B. 输出控制专题营

1. `第1课-Structured Outputs For Reasoning Models`
2. `第2课-Tool Parser`
3. `第3课-Reasoning Parser`
4. `第4课-Deterministic Inference`
5. `第5课-OpenAI Responses / 高级输出接口`

### C. 缓存与执行优化专题营

1. `第1课-Speculative Decoding`
2. `第2课-Quantization`
3. `第3课-Quantized KV Cache`
4. `第4课-Piecewise / Breakable CUDA Graph`

### D. 多模态与能力扩展专题营

1. `第1课-LoRA Serving`
2. `第2课-Query VLM with Offline Engine`
3. `第3课-DP for Multi-Modal Encoder`
4. `第4课-CUDA Graph for Multi-Modal Encoder`

### E. Serving 生态专题营

1. `第1课-SGLang Model Gateway`
2. `第2课-Observability`
3. `第3课-Checkpoint Engine Integration`

## 拆课规则

- 主课程先保持纯净，再决定需要补哪些专题营
- 如果用户要求 18 到 20 节，直接在 `15 节标准版主课程` 后追加合适的专题营，不单独引入“模板二”
- `Speculative Decoding`、`Quantization`、`Quantized KV Cache` 默认优先进入专题营
- `TP / DP / DPA / DP Router / EP / Pipeline Parallelism / EPD` 默认优先进入专题营
- `Tool Parser`、`Reasoning Parser`、`Structured Outputs For Reasoning Models` 默认优先进入专题营
- `LoRA Serving`、`多模态 Encoder DP / CUDA Graph` 默认优先进入专题营
- `Model Gateway`、`Observability`、`Checkpoint Engine Integration` 默认优先进入专题营

## 每一课默认结构

- `课程主题`
- `为什么这一课重要`
- `核心知识点`
- `学习目标`
- `推荐阅读文件`
- `建议练习或演示`
