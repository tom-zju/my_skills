# FlashInfer 课程大纲

## 文档定位

本文档整理 `FlashInfer 6 课硬核主线 + 5 门精简专题课`。

- 面向对象：`LLM serving 工程师`、`kernel / runtime 开发者`、需要系统理解 FlashInfer 的高阶研发
- 默认目标：先建立 FlashInfer 的 attention serving 主线，再进入最有辨识度、最值得深挖的硬核专题
- 默认课时建议：
  - 主课程：`6 课`，每课 `1 小时`
  - 专题课：每门 `1 到 1.5 小时`
- 使用方式：
  - 若目标是快速建立整体认知，先学 `6 课硬核主线`
  - 若目标是做二次开发、性能优化或专题分享，再按需选修 `5 门专题课`

## 课程总目标

完成本套课程后，学习者应能回答以下问题：

1. FlashInfer 为什么存在，它和 FlashAttention、vLLM、TensorRT-LLM 分别处在什么层次。
2. FlashInfer 如何通过 `KV-Cache`、`page table`、`wrapper plan/run`、`workspace` 把 attention serving 组织成 runtime 闭环。
3. 为什么 serving 中必须区分 `prefill` 与 `decode`，为什么 `POD-Attention` 与 `Cascade` 是 FlashInfer 的标志性能力。
4. 当需要继续深入时，应该从 attention API、KV layout、cascade、JIT variants、MLA 这几个专题里如何扩展。

## 推荐学习顺序

1. 先完成 `6 课硬核主线`
2. 再按下面顺序选修专题：
   - `专题一 Attention API 全景`
   - `专题二 KV Layout 与 Page Table`
   - `专题三 Cascade 与 Shared Prefix`
   - `专题四 JIT 与 Attention Variants`
   - `专题五 MLA Attention`

---

## 第一部分：6 课硬核主线

### 第1课 FlashInfer 的项目定位与问题定义：它为什么不是“又一个 attention kernel”

- 课程主题：
  从 serving 第一性原理出发，理解 FlashInfer 为什么要做成 `推理内核库 + kernel generator`，而不是单一 attention kernel 集合。
- 为什么这一课重要：
  如果不先建立项目定位，后面的课程很容易退化成 API 导读，或者把 FlashInfer 和 FlashAttention、vLLM、TensorRT-LLM 混成同一层能力。
- 核心知识点：
  - LLM serving 的核心瓶颈是什么
  - prefill、decode、mixed batching 的区别
  - FlashInfer 在 serving 技术栈中的角色
  - FlashInfer 与 FlashAttention、cuDNN、CUTLASS、TensorRT-LLM 的关系
- 学习目标：
  - 能解释 FlashInfer 解决的核心问题
  - 能说明它面向的主要场景
  - 能讲清它在完整 serving 栈中的位置
- 建议课堂展开：
  - 从“模型推理慢在哪里”切入，而不是先讲 API
  - 用一张 serving 栈分层图建立项目定位
  - 对比“底层算子库”和“完整 serving 框架”的责任边界
- 推荐阅读：
  - [FlashInfer README](https://github.com/flashinfer-ai/flashinfer/blob/main/README.md)
  - [官方文档首页](https://docs.flashinfer.ai/)
  - [GitHub Releases](https://github.com/flashinfer-ai/flashinfer/releases)
- 与前后课的衔接：
  本课先回答“为什么需要 FlashInfer”，下一课转入“它靠什么状态抽象组织 attention serving”。

### 第2课 KV-Cache 与状态模型：Paged / Ragged / Layout / Append / Page API 如何构成统一抽象

- 课程主题：
  把 `KV-Cache` 看成 FlashInfer attention serving 的状态层，理解 paged、ragged、layout、append/page API 为什么需要一起建模。
- 为什么这一课重要：
  这是整个 attention serving 主线的数据模型基础。不理解 page table 和布局，后续 prefill、decode、POD、cascade 都会失去抓手。
- 核心知识点：
  - paged KV-Cache 的基本思想
  - ragged tensor / ragged KV-Cache 的表达方式
  - `NHD / HND` 的布局差异
  - `indptr / indices / last_page_len` 的角色
  - `append_paged_kv_cache` 与 `append_paged_mla_kv_cache` 的状态写入语义
- 学习目标：
  - 能解释 FlashInfer 如何表示变长请求
  - 能解释 page table 如何把逻辑序列映射到物理页
  - 能理解新 K/V 如何进入缓存
- 建议课堂展开：
  - 从“为什么 padding 浪费严重”切入 ragged/paged
  - 画出 page table 与 cache page 的示意图
  - 把 append/page API 放回状态写入路径中讲
- 推荐阅读：
  - [KV-Cache Layout 教程](https://docs.flashinfer.ai/tutorials/kv_layout.html)
  - [Page API](https://docs.flashinfer.ai/api/page.html)
  - [`append_paged_kv_cache`](https://docs.flashinfer.ai/generated/flashinfer.page.append_paged_kv_cache.html)
  - [`append_paged_mla_kv_cache`](https://docs.flashinfer.ai/generated/flashinfer.page.append_paged_mla_kv_cache.html)
- 与前后课的衔接：
  本课建立“状态如何表示”，下一课进入“为什么在同样基于 KV-Cache 的前提下，prefill 和 decode 必须拆开看”。

### 第3课 Attention 主线：为什么 serving 中必须区分 Prefill 和 Decode

- 课程主题：
  这一课把 `Prefill` 和 `Decode` 放在一起，不是为了并讲两个实现，而是为了讲清 serving 中为什么必须把它们当作两类不同计算问题。
- 为什么这一课重要：
  这是 FlashInfer attention 主线最核心的分流课。只有把 prefill 和 decode 的问题性质讲清楚，后面的 POD-Attention 和 wrapper 两阶段执行才有意义。
- 核心知识点：
  - prefill 的长序列并行特征
  - decode 的单步增量特征
  - 两者在 IO、缓存复用、调度目标上的不同
  - `BatchPrefillWithPagedKVCacheWrapper` 与 `BatchDecodeWithPagedKVCacheWrapper` 的职责差异
- 学习目标：
  - 能说明为什么 serving 不能只依赖“统一 attention kernel”思维
  - 能解释 prefill / decode 的核心差异
  - 能讲清 FlashInfer 为什么为两条路径提供不同 wrapper
- 建议课堂展开：
  - 用“长上下文处理”和“逐 token 生成”两种 workload 对照
  - 强调这一课的核心主题是“为什么拆开”，不是“实现细节大全”
  - 在结尾引出 mixed batching 问题
- 推荐阅读：
  - [Attention API 总览](https://docs.flashinfer.ai/api/attention.html)
  - [KV-Cache Layout 教程](https://docs.flashinfer.ai/tutorials/kv_layout.html)
  - [仓库 `flashinfer/`](https://github.com/flashinfer-ai/flashinfer/tree/main/flashinfer)
- 与前后课的衔接：
  本课解释“为什么有两条路径”，下一课解释“为什么 mixed batching 下需要把两条路径进一步组织起来”。

### 第4课 POD-Attention：mixed batching 下的 fused prefill + decode 为什么是 FlashInfer 的辨识度

- 课程主题：
  理解 `POD-Attention` 为什么是 FlashInfer 在 mixed batching 场景下的标志性能力，以及它解决的是批处理组织问题，而不只是单个 kernel 优化。
- 为什么这一课重要：
  这是 FlashInfer 与普通 attention 库最容易拉开差异的一课。没有这课，课程会失去项目辨识度。
- 核心知识点：
  - mixed batching 的现实场景
  - fused prefill + decode 的动机
  - POD-Attention 如何减少调度碎片与切换开销
  - 为什么它是 serving 场景问题，而不是单一 kernel 技巧
- 学习目标：
  - 能解释 POD-Attention 面向的 workload
  - 能说明它如何建立在 prefill / decode 分流基础之上
  - 能理解它为什么是 FlashInfer 的代表性能力
- 建议课堂展开：
  - 先定义 mixed batching 问题
  - 再解释为什么简单地“同时支持 prefill 和 decode”还不够
  - 最后回到 FlashInfer 的工程价值，而不是停在概念名词
- 推荐阅读：
  - [Attention API 总览](https://docs.flashinfer.ai/api/attention.html)
  - [Recursive Attention 教程](https://docs.flashinfer.ai/tutorials/recursive_attention.html)
  - [FlashInfer README](https://github.com/flashinfer-ai/flashinfer/blob/main/README.md)
- 与前后课的衔接：
  本课回答“为什么要融合组织两条路径”，下一课进一步进入 `plan()/run()`，解释这种组织方式如何真正落成 runtime 闭环。

### 第5课 Wrapper 两阶段执行：plan() / run() / workspace / partial state 怎样构成 runtime 闭环

- 课程主题：
  把 `plan()`、`run()`、`workspace`、`partial state` 放在同一个 runtime 闭环里理解，而不是把它们拆成孤立 API。
- 为什么这一课重要：
  FlashInfer 的核心价值不只在 kernel 本身，还在于它怎样把执行规划、状态复用和运行阶段拆开，以兼顾吞吐、延迟与复用。
- 核心知识点：
  - 为什么要两阶段执行
  - `plan()` 产出什么辅助结构
  - `run()` 消费什么状态
  - workspace 保存了哪些中间状态
  - partial state 为什么重要
- 学习目标：
  - 能从 runtime 视角解释 wrapper 的存在意义
  - 能理解 plan/run 的职责分工
  - 能说明 workspace 与 partial state 的地位
- 建议课堂展开：
  - 先给出“只调 kernel 不够”的反例
  - 再讲 FlashInfer 如何把 planning 与 execution 拆开
  - 最后为 cascade 的 merge state 埋下伏笔
- 推荐阅读：
  - [Attention API 总览](https://docs.flashinfer.ai/api/attention.html)
  - [Recursive Attention 教程](https://docs.flashinfer.ai/tutorials/recursive_attention.html)
  - [仓库 `flashinfer/`](https://github.com/flashinfer-ai/flashinfer/tree/main/flashinfer)
  - [仓库 `csrc/`](https://github.com/flashinfer-ai/flashinfer/tree/main/csrc)
- 与前后课的衔接：
  本课建立 runtime 闭环；下一课在此基础上解释 shared prefix / cascade 为什么是“已有状态的复用与合并”，而不是凭空出现的新机制。

### 第6课 Cascade / Shared Prefix：服务端前缀复用为什么值得单独建模

- 课程主题：
  把 `Cascade / Shared Prefix` 看成服务端状态复用问题，而不是 attention API 的附属功能。
- 为什么这一课重要：
  这是 FlashInfer 从“快 attention”推进到“懂 serving 状态复用”的关键一课，也是 runtime 思维最强的一课。
- 核心知识点：
  - shared prefix 的收益来源
  - multi-level cascade 的基本结构
  - `merge_state / merge_states` 的语义
  - 它与 `workspace / partial state` 的关系
- 学习目标：
  - 能解释 cascade 解决的核心问题
  - 能理解状态是如何被合并和复用的
  - 能说明为什么这类能力对真实 serving 系统有价值
- 建议课堂展开：
  - 从“重复算相同前缀”切入
  - 再解释 cascade 不是“多一个 API”，而是“多一种 runtime 复用策略”
  - 讲 merge state 时显式回接上一课的 workspace
- 推荐阅读：
  - [Cascade API](https://docs.flashinfer.ai/api/cascade.html)
  - [Recursive Attention 教程](https://docs.flashinfer.ai/tutorials/recursive_attention.html)
  - [FlashInfer README](https://github.com/flashinfer-ai/flashinfer/blob/main/README.md)
- 与前后课的衔接：
  这课收束 `6 课主线`。学完后再进入专题课，会更清楚哪些是“主线延伸”，哪些是“深水区能力”。

---

## 第二部分：5 门精简专题课

### 专题一 FlashInfer Attention API 全景

- 主题定位：
  从主课程的 attention 主线继续下沉到接口层，系统梳理 single request、batch、paged、ragged、wrapper 的 API 分层与使用边界。
- 为什么重要：
  主课程回答“为什么这样设计”，这一课回答“具体 API 怎么选、怎么接、怎么避免误用”。
- 学习目标：
  - 能按请求形态和缓存形态选择合适 attention API
  - 能解释 wrapper 与底层 API 的关系
  - 能区分 prefill / decode / paged / ragged 的接口职责
- 核心知识点：
  - attention API 分层
  - single request vs batch
  - paged vs ragged
  - wrapper 与函数级 API 的边界
  - API 选择背后的 serving 约束
- 建议子章节：
  1. FlashInfer attention API 的分层地图
  2. Single request、batch、paged、ragged 的问题边界
  3. Prefill / Decode API 的职责差异与常见误用
  4. 什么时候直接调 API，什么时候走 wrapper
- 推荐阅读：
  - [Attention API 总览](https://docs.flashinfer.ai/api/attention.html)
  - [FlashInfer README](https://github.com/flashinfer-ai/flashinfer/blob/main/README.md)
  - [仓库 `flashinfer/`](https://github.com/flashinfer-ai/flashinfer/tree/main/flashinfer)
- 与主课程衔接：
  承接主课程第 3 到第 5 课，把 attention 主线从概念推进到具体接口设计。

### 专题二 KV Layout 与 Page Table

- 主题定位：
  专门深挖 FlashInfer attention serving 的状态模型，聚焦 KV-Cache 的布局、page table 和写入路径。
- 为什么重要：
  这是 FlashInfer 最核心的数据抽象深水区。很多性能、正确性和接口理解问题，最终都要回到这层。
- 学习目标：
  - 能解释 paged KV-Cache 的物理组织
  - 能理解 `NHD / HND` 的差异
  - 能解释 page table 在 API 中的角色
  - 能看懂 append/page 写入路径
- 核心知识点：
  - paged KV-Cache
  - ragged 表示
  - `NHD / HND`
  - `indptr / indices / last_page_len`
  - append API 与 page API
- 建议子章节：
  1. 从逻辑序列到 page table
  2. `indptr / indices / last_page_len` 的统一语义
  3. `NHD / HND` 与布局选择的工程含义
  4. append/page 接口如何连接状态写入路径
- 推荐阅读：
  - [KV-Cache Layout 教程](https://docs.flashinfer.ai/tutorials/kv_layout.html)
  - [Page API](https://docs.flashinfer.ai/api/page.html)
  - [`append_paged_kv_cache`](https://docs.flashinfer.ai/generated/flashinfer.page.append_paged_kv_cache.html)
  - [`append_paged_mla_kv_cache`](https://docs.flashinfer.ai/generated/flashinfer.page.append_paged_mla_kv_cache.html)
- 与主课程衔接：
  承接主课程第 2 课，把“KV-Cache 是什么”深化成“KV-Cache 到底怎么表示、怎么写入、怎么影响 attention 执行”。

### 专题三 Cascade 与 Shared Prefix

- 主题定位：
  把 shared prefix 复用与 cascade attention 拉出来单独讲，说明它为什么本质上是服务端状态复用问题。
- 为什么重要：
  这是 FlashInfer 最体现 runtime / serving 思维的专题之一。它把“重复计算前缀”转成“复用已有运行时状态”。
- 学习目标：
  - 能解释 shared prefix 的收益来源
  - 能理解 multi-level cascade 的结构
  - 能理解 `merge_state / merge_states` 为什么依赖 workspace / partial state
- 核心知识点：
  - shared prefix
  - multi-level cascade
  - `merge_state / merge_states`
  - 与 wrapper runtime state 的关系
- 建议子章节：
  1. Shared prefix 在 serving 中节省了什么
  2. Cascade attention 的分层状态模型
  3. `merge_state / merge_states` 的语义与状态合并路径
  4. 从 workspace 到 prefix reuse 的 runtime 闭环
- 推荐阅读：
  - [Cascade API](https://docs.flashinfer.ai/api/cascade.html)
  - [Recursive Attention 教程](https://docs.flashinfer.ai/tutorials/recursive_attention.html)
  - [Attention API 总览](https://docs.flashinfer.ai/api/attention.html)
- 与主课程衔接：
  承接主课程第 5、6 课；默认先理解 `plan/run/workspace`，再进入这门专题。

### 专题四 JIT 与 Attention Variants

- 主题定位：
  专门解释 FlashInfer 为什么不只是 kernel collection，而是 `kernel generator`，以及 attention variants 如何通过模板 / JIT 扩展。
- 为什么重要：
  这是 FlashInfer 和固定实现 attention 库最不一样的地方之一，也是很多 kernel / runtime 开发者最关心的能力边界。
- 学习目标：
  - 能解释 JIT 在 FlashInfer 中解决的问题
  - 能理解 `backend='auto'`、`jit_args`、`jit_kwargs` 的意义
  - 能理解 variants 如何从抽象落到专用 kernel
- 核心知识点：
  - kernel generator 思路
  - 模板展开
  - JIT
  - backend 选择
  - attention variants 的扩展路径
- 建议子章节：
  1. 为什么 FlashInfer 需要 kernel generator
  2. `backend='auto'` 的意义与后端选择
  3. `jit_args` / `jit_kwargs` 在扩展路径中的角色
  4. 从 attention variant 抽象到专用 kernel 的生成链路
- 推荐阅读：
  - [Attention API 总览](https://docs.flashinfer.ai/api/attention.html)
  - [FlashInfer README](https://github.com/flashinfer-ai/flashinfer/blob/main/README.md)
  - [仓库 `flashinfer/`](https://github.com/flashinfer-ai/flashinfer/tree/main/flashinfer)
- 与主课程衔接：
  这是主课程之后的“扩展能力”专题，默认放在主线理解完成之后再学。

### 专题五 MLA Attention

- 主题定位：
  聚焦 FlashInfer 对 DeepSeek 类 MLA 模型的专用 attention 支持，讲清它与普通 attention 的差异。
- 为什么重要：
  如果想理解 FlashInfer 如何面向新型模型结构演进，这门课很有代表性；它也是最值得保留的模型特化专题。
- 学习目标：
  - 能解释 MLA 的问题定义
  - 能理解 `ckv / kpe` 缓存
  - 能理解 paged MLA attention 与普通 attention 的差异
  - 能说明 MLA 为什么不适合直接塞进默认主线
- 核心知识点：
  - MLA 的设计背景
  - `ckv / kpe`
  - paged MLA attention
  - MLA wrapper 的接口与使用边界
- 建议子章节：
  1. MLA 为什么需要单独的 attention 抽象
  2. `ckv / kpe` 的状态含义与缓存组织
  3. paged MLA attention 与普通 paged attention 的差异
  4. MLA 在 FlashInfer 中的接口位置与边界
- 推荐阅读：
  - [Attention API 总览](https://docs.flashinfer.ai/api/attention.html)
  - [FlashInfer README](https://github.com/flashinfer-ai/flashinfer/blob/main/README.md)
  - [GitHub Releases](https://github.com/flashinfer-ai/flashinfer/releases)
- 与主课程衔接：
  默认放在主课程之后学习。最好先学完普通 attention 主线，再进入 MLA，否则很容易直接落入模型特化细节。

---

## 第三部分：授课建议

### 如果目标是团队 onboarding

- 只讲 `6 课硬核主线`
- 专题课只保留 `Attention API 全景` 和 `KV Layout 与 Page Table`

### 如果目标是 kernel / runtime 开发者培养

- 先讲 `6 课硬核主线`
- 再讲 `5 门专题课`
- 推荐顺序：
  1. Attention API 全景
  2. KV Layout 与 Page Table
  3. Cascade 与 Shared Prefix
  4. JIT 与 Attention Variants
  5. MLA Attention

### 如果目标是内部技术分享

- 可压缩为：
  - `主线 3 课`：项目定位、KV-Cache、Prefill/Decode/POD
  - `专题 2 课`：Cascade、JIT/Variants

## 附：最小阅读集合

- [FlashInfer README](https://github.com/flashinfer-ai/flashinfer/blob/main/README.md)
- [官方文档首页](https://docs.flashinfer.ai/)
- [Attention API 总览](https://docs.flashinfer.ai/api/attention.html)
- [KV-Cache Layout 教程](https://docs.flashinfer.ai/tutorials/kv_layout.html)
- [Page API](https://docs.flashinfer.ai/api/page.html)
- [Cascade API](https://docs.flashinfer.ai/api/cascade.html)
- [Recursive Attention 教程](https://docs.flashinfer.ai/tutorials/recursive_attention.html)

