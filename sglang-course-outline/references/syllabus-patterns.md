# SGLang 课程目录模板

这个参考文件用于生成“第几课”形式的课程目录，而不是普通章节式文档。

## 来源说明

本文件综合了三类来源：

- SGLang 官方文档：`https://docs.sglang.io/`
- SGLang 官方 GitHub 仓库：`https://github.com/sgl-project/sglang`
- SGLang 官方 release/tag 页面与 `main` 主线代码结构

本模板不固化某一个“当前最新版本号”。

如果用户要求“结合最新版本”“结合最新代码”“main 分支”“最近实现”，必须在生成课程前重新核对：

- 官方 release/tag
- 该版本的官方发布日期
- 主仓库 `main` 的当前代码结构

## 课程目录输出总规则

只要用户要求“课程目录”“课纲”“学习大纲”“按课时拆分”，默认优先输出 lesson 化课程目录。
如果用户明确要求“详细课程大纲”或“完整教学版课纲”，默认同时输出 `标准版主课程 + 专题高阶课程`，并整理为 Markdown 文档。

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

- `19 课`

默认目录：

1. `第1课-SGLang 介绍、环境搭建与快速上手`
2. `第2课-SGLang 双层体系架构全景`
3. `第3课-SGLang 请求生命周期`
4. `第4课-SGLang Scheduler 主流程`
5. `第5课-SGLang ScheduleBatch 组批与状态推进`
6. `第6课-SGLang Continuous Batching`
7. `第7课-SGLang Chunked Prefill`
8. `第8课-SGLang RadixAttention`
9. `第9课-SGLang Radix Cache 前缀复用`
10. `第10课-SGLang TPWorker 执行编排`
11. `第11课-SGLang ModelRunner 执行主链`
12. `第12课-SGLang Attention Backend`
13. `第13课-SGLang 并行体系总览（TP / DP / SP / PP / EP）`
14. `第14课-SGLang 并行机制细讲（TP / DP / DPA / DP Router / SP / EP / PP）`
15. `第15课-SGLang Speculative Decoding`
16. `第16课-SGLang Quantization 基础与原理`
17. `第17课-SGLang Quantization 模块解析与实践`
18. `第18课-SGLang PD Disaggregation`
19. `第19课-SGLang HiCache`

说明：

- 标准版主课程默认固定为 `19 课`
- 标准版主课程默认覆盖 SGLang 强链路主线、并行体系、执行优化与核心解耦缓存
- `第1课` 允许合并 `SGLang 项目介绍 + 环境搭建 + 快速上手 demo`，作为 onboarding 入口课
- 标准版主课程默认围绕 `介绍与快速上手 -> 架构与入口 -> 请求进入 -> tokenizer / scheduler -> schedule batch -> continuous batching / chunked prefill -> radix attention / prefix reuse -> worker / model runner -> attention backend -> parallelism overview / detail -> speculative decoding -> quantization basics / practice -> disaggregation / hicache` 组织
- `项目定位`、`版本演进`、`Server Arguments`、`OpenAI-Compatible APIs`、`Offline Engine API`、`SGLang Native APIs`、`Sampling Parameters`、`源码阅读路径` 默认并入相邻功能课或附录
- `并行体系总览` 负责建立全景，`并行机制细讲` 负责解释 `TP / DP / DPA / DP Router / SP / EP / PP` 的切分方式、通信路径与适用场景；如果用户要求源码级分布式专题，应在专题高阶课程中继续拆开
- `Quantization 基础与原理` 负责建立量化概念与方案认知，`Quantization 模块解析与实践` 负责梳理 SGLang 中的模块入口、配置路径与部署实践
- `并行体系总览`、`并行机制细讲`、`Speculative Decoding`、`Quantization 基础与原理`、`Quantization 模块解析与实践`、`PD Disaggregation` 与 `HiCache` 默认进入标准版主课程
- 如需补充输出控制、函数调用或推理模型输出格式，默认作为按需补充专题单独追加，不纳入当前三大默认特性专项

## 模板二：专题高阶课程

### A. 大模型结构专题营

1. `第1课-DeepSeek 系列模型结构与推理特征`
2. `第2课-Kimi 系列模型结构与长上下文设计`
3. `第3课-Qwen 系列模型结构与服务适配`

### B. LLM 长文本优化专题营

1. `第1课-长文本场景的问题定义与背景`
2. `第2课-模型侧、框架侧与算子侧的优化点和解决方案`
3. `第3课-长文本优化中的工程落地、方案选型与排障补充`

### C. LLM 模型性能优化端到端专题营

1. `第1课-SGLang 性能优化流程与步骤`
2. `第2课-Profiling 链路与瓶颈定位`
3. `第3课-SGLang 性能优化中的关键专项与实战补充`

## 拆课规则

- 主课程先保持纯净，再决定需要补哪些专题营
- 如果用户要求 20 到 22 节，应先说明当前标准版主课程默认是 `19 节`
- 如果用户需要达到 `20 到 22 节`，优先在 `19 节标准版主课程` 后补充 1 到 3 节专题高阶课程
- `并行体系总览` 与 `并行机制细讲` 默认优先进入标准版主课程；如果用户要求更深的分布式专题，再把 `TP`、`DP / DPA / DP Router`、`SP`、`EP`、`PP` 继续拆开
- `Quantization 基础与原理` 与 `Quantization 模块解析与实践` 默认优先进入标准版主课程
- `DeepSeek / Kimi / Qwen 模型结构`、`LLM 长文本优化专题营`、`LLM 模型性能优化端到端专题营` 默认优先进入专题高阶课程

## 每一课默认结构

- `课程主题`
- `为什么这一课重要`
- `核心知识点`
- `学习目标`
- `推荐阅读文件资料`
- `建议练习或演示`

补充要求：

- `推荐阅读文件资料` 尽量提供真实可靠的官方文档页链接、官方 GitHub 仓库链接或可定位的源码文件路径
- 不要编造链接，不要只写无法核验的笼统描述
