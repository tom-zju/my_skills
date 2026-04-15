# FlashInfer 主题索引

这个文件给 `flashinfer-course-outline` skill 提供按需索引。生成课程时，不必一次性全读；只在相关专题被用户点名时展开。

## 目录

- `0.` 版本与使用说明
- `1.` 仓库级入口
- `2.` Attention 主线
- `3.` KV-Cache 与布局
- `4.` Cascade / Shared Prefix
- `5.` MLA
- `6.` Sampling
- `7.` MoE / GEMM
- `8.` Communication
- `9.` JIT / Attention Variants
- `10.` 性能与基准
- `11.` 对比课程

## 0. 版本与使用说明

- 若用户指定“最新版本”或某个明确版本，先以官方 release 与当前文档站为准，再决定课程边界。
- 若当前无法实时访问仓库或文档，这份 topic map 仍可作为教学分解模板使用，但输出时必须明确说明“未实时核对具体版本”。
- 下面每个主题都给出“更适合主课程还是专题课”的建议，避免同一主题在主线和专题中被重复展开。
- 若要给真实的推荐阅读链接，统一优先从 [link-map.md](./link-map.md) 取链接；本文件主要负责主题归类和按需展开，不再作为 URL 真相源。

## 1. 仓库级入口

对应：6 课主线第 1 课；也可作为母版总纲的总入口。

- GitHub 仓库首页与 `README.md`
- `docs/` 或官方文档站 `docs.flashinfer.ai`
- `flashinfer/`
- `include/flashinfer/`
- `csrc/`
- `tests/`
- `benchmarks/`
- `profiler/`

## 2. Attention 主线

适用问题：

- FlashInfer 的 attention API 如何分层
- prefill / decode / append 有何差异
- wrapper 的 `plan/run` 为什么存在
- POD-Attention 为什么是 FlashInfer 在 mixed batching 场景下的标志性能力

对应：

- 6 课主线第 3 课：`Prefill vs Decode`
- 6 课主线第 4 课：`POD-Attention`
- 6 课主线第 5 课：`plan() / run() / workspace`
- 6 课主线第 6 课：`Cascade / Shared Prefix`
- 12 课扩展版第 4 到第 10 课
- 若用户要“attention 主线总览”或“mixed batching 专题”，优先从这里展开

优先材料：

- `link-map` 中的 `Attention API 总览`
- `link-map` 中的 `KV-Cache Layout 教程`
- `link-map` 中的 `Recursive Attention 教程`
- `link-map` 中的仓库目录 `flashinfer/`

补充提醒：

- 若用户要求“FlashInfer 与普通 attention 库的差异”“FlashInfer 的代表性创新点”或“mixed batching 专题”，应显式覆盖 `POD-Attention (fused prefill + decode)`，不要只笼统写成 prefill/decode 共存。

## 3. KV-Cache 与布局

适用问题：

- paged KV-Cache 是什么
- ragged tensor 怎么表示
- `NHD / HND` 布局的差异
- `indptr / indices / last_page_len` 的角色

对应：

- 6 课主线第 2 课
- 12 课扩展版第 2 到第 4 课
- 若用户只问缓存抽象、布局格式、page table，可直接基于本节生成局部课程

优先材料：

- `link-map` 中的 `KV-Cache Layout 教程`
- `link-map` 中的 `Page API`
- `link-map` 中的 `append_paged_kv_cache`
- `link-map` 中的 `append_paged_mla_kv_cache`

## 4. Cascade / Shared Prefix

适用问题：

- shared prefix 为什么能节省内存带宽
- `merge_state / merge_states` 的语义是什么
- 多层级 cascade wrapper 如何组织
- 它与 wrapper 的 `workspace / partial state` 有什么依赖关系

对应：

- 6 课主线第 6 课
- 12 课扩展版第 10 课
- 专题课可扩展为“prefix reuse / merge state / cascade wrapper”三段式

优先材料：

- `link-map` 中的 `Cascade API`
- `link-map` 中与 cascade wrapper 对应的 API 入口

补充提醒：

- 讲 `merge_state / merge_states` 时，默认回接主课程第 5 课的 `workspace / partial state`，说明 cascade 依赖的是已有运行时状态，而不是独立于 wrapper 的另一套机制。

## 5. MLA

适用问题：

- FlashInfer 如何支持 DeepSeek MLA
- `ckv / kpe` 缓存是什么
- paged MLA attention 和普通 attention 有什么不同

对应：

- 默认放到专题高阶课程
- 除非用户明确要求“主课程含 MLA 版本”，否则不要塞回 12 课主线

优先材料：

- `link-map` 中的 `Attention API 总览` 里的 MLA 相关部分
- `link-map` 中与 MLA wrapper 对应的 attention API 入口

## 6. Sampling

适用问题：

- FlashInfer 为什么要做 sorting-free sampling
- Top-K / Top-P / Min-P 的 fused kernel 设计
- speculative sampling 如何融入生成流程

对应：

- 默认放到专题高阶课程
- 当用户明确问“生成阶段后处理”或“采样算子族”时再展开

优先材料：

- `link-map` 中的 `Sampling API`
- `link-map` 中的 `Top-K API`

## 7. MoE / GEMM

适用问题：

- FlashInfer 为什么从 attention 扩展到 GEMM 与 MoE
- CUTLASS / TRT-LLM 后端各自解决什么问题
- FP8 / FP4 / block scaling 如何进入算子实现

对应：

- 默认放到专题高阶课程
- 12 课扩展版第 12 课可以做能力边界点名，但不要在默认 6 课主线中回灌成单独讲授内容

优先材料：

- `link-map` 中的 `Fused MoE API`
- `link-map` 中的仓库 `README`

## 8. Communication

适用问题：

- FlashInfer 为什么还做通信内核
- AllReduce、MNNVL、NVSHMEM 在推理系统中的角色

对应：

- 默认放到专题高阶课程
- 若用户要“分布式 serving 支撑能力”或“attention 之外的系统算子”，再从这里展开

优先材料：

- `link-map` 中的 `Communication API`
- `link-map` 中的仓库 `README`
- `link-map` 中的仓库目录 `flashinfer/`

## 9. JIT / Attention Variants

适用问题：

- FlashInfer 为什么是 kernel generator
- attention variants 如何通过模板/JIT 扩展
- wrapper 中的 `backend='auto'`、`jit_args`、`jit_kwargs` 有何意义

对应：

- 默认放到专题高阶课程
- 若用户明确要求“FlashInfer 与固定 attention 库的区别”或“kernel generator 机制”，从这里展开

优先材料：

- `link-map` 中的仓库 `README`
- `link-map` 中的 `Attention API 总览`，重点看 wrapper 的 `backend` / `jit_args` / `jit_kwargs`

## 10. 性能与基准

适用问题：

- 如何理解 FlashInfer 的性能定位
- 何时看 benchmarks，何时看 profiler

对应：

- 可作为母版总纲的收尾模块
- 也可作为专题高阶课程的性能实验附录

优先材料：

- `link-map` 中的仓库目录 `benchmarks/`
- `link-map` 中的仓库目录 `profiler/`
- `link-map` 中的仓库 `README`

## 11. 对比课程

对应：SKILL.md 中“输出合同”里的 `对比课程` 结构；生成时两处规则同时适用。

适用问题：

- `FlashInfer vs vLLM`
- `FlashInfer vs FlashAttention`
- 以 FlashInfer 为主对象，说明它与其他库在定位、抽象和适用场景上的差异

推荐对比维度：

- 项目定位：推理算子/runtime 库 vs 完整 serving 系统 vs 纯 attention kernel 库
- 数据抽象：KV-cache、page/ragged、状态写入路径
- 运行时组织：wrapper、`plan/run`、workspace、调度模型
- 代表性能力：POD-Attention、Cascade、JIT/variants、多后端
- 适用场景：什么时候更适合作为底层能力库，什么时候更适合作为完整框架

优先材料：

- `link-map` 中的 FlashInfer 仓库 `README`
- `link-map` 中的 FlashInfer 官方文档首页
- 对比对象的官方 `README` / docs 首页
- 与对比维度直接相关的官方页面，例如 attention、KV-cache、runtime、serving 架构说明

补充提醒：

- 适合进课程主线的对比，应围绕 FlashInfer 的定位、抽象和能力边界
- 不适合进主课程正文的细节，可降到附录，例如逐 API 枚举式差异、零散 benchmark 罗列
- 若用户真正要的是双向中立技术比较，而不是以 FlashInfer 为主对象的课程，应退出本 skill 的课程模板
