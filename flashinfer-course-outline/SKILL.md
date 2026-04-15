---
name: flashinfer-course-outline
description: 为 FlashInfer 生成中文课程总纲、课程目录、学习路径、知识地图，以及培训计划、内部分享和 onboarding 提纲。适用于系统梳理 FlashInfer 的 attention serving 主线、KV-Cache、prefill/decode/mixed batching、wrapper 的 plan/run，也适用于单独模块课程、模块化 onboarding，以及以 FlashInfer 为主对象、对比仅用于帮助定位的对比课程，并按“单课单主题”原则设计主课程与专题高阶课程；不用于解答单个 API、单个 kernel、单个 bug 或局部实现细节。
---

# FlashInfer 课程总纲与课程目录整理

## 核心约束速查

1. **默认输出骨架**：只有当请求属于“系统课程”且用户未指定其他包装时，才默认输出 `6 课硬核主线`；`12 课` 只作为扩展版或讲师版。
2. **主课/专题分界**：主课程只覆盖“理解 FlashInfer 如何工作所必需的最小知识集”；专题课程覆盖“使用、扩展或优化某个具体能力所需的深度知识”。
3. **单课单主题**：同一课只讲一个核心问题；若必须把两个名词放进同一课，核心主题必须是“它们为何需要一起被建模”，不能变成两个实现并讲。
4. **先定义问题再讲实现**：每一章先回答“FlashInfer 要解决什么 serving 问题”，再讲 API、数据结构和源码实现。
5. **版本与读取能力要交代**：若无法实时读取仓库/文档或核对 release，必须明确说明限制，并降级为教学草案或目录级导读。
6. **灰区请求先分流**：单模块课程、模块化 onboarding、FlashInfer 为主的对比课程，可以继续使用本 skill；单个 API/kernel/bug/局部实现细节，则退出课程模式，改做针对性分析。
7. **推荐阅读必须给真实链接**：只要输出里出现“推荐阅读 / 推荐文档 / 推荐链接”，若无法确认链接真实性，必须降级到目录级或栏目级描述并明确说明；不得给出未经验证的具体 URL。
8. **未核对时不得伪造细节**：若当前未实时核对仓库、文档或版本，不得伪造具体 API 名、类名、函数签名或版本敏感结论；宁可退回模块级描述。
9. **中文优先**：课程说明、课时标题、学习目标默认中文；代码标识符、模块名、路径、API 名保持英文原名。

---

## 总体说明

这个 skill 用来把 FlashInfer 仓库和官方文档整理成可教学、可培训、可 onboarding 的中文课程材料。默认目标不是堆功能清单，而是帮助读者建立下面这条主线：

- FlashInfer 为什么存在
- 它在 LLM serving 中解决什么性能瓶颈
- 它如何以 attention serving 主线为核心，用 KV-Cache 抽象、wrapper 的 `plan/run` 工作流和多后端机制组织注意力计算，并进一步扩展到 GEMM、MoE、sampling 等其他算子族

默认教学设计原则：

- `默认用 6 课讲清 attention serving 主线`
- `专题课程承接高阶能力与实现深水区`

## 适用场景

当用户有下面这些需求时使用本 skill：

- 要 FlashInfer 课程总纲
- 要 FlashInfer 课程目录
- 要 FlashInfer 学习路径
- 要 FlashInfer 知识地图
- 要按课时拆分的培训提纲、分享提纲或 onboarding 文档
- 要 FlashInfer 培训计划、培训路线、内部分享大纲
- 要把 `flashinfer-ai/flashinfer` 仓库整理成教学版中文材料
- 要围绕 paged KV-Cache、prefill/decode、wrapper `plan/run`、MLA、MoE、sampling、communication、JIT attention variants 做系统课程设计
- 要单独做某个模块的课程，例如 `MLA 课程`、`Sampling onboarding`、`JIT variants 专题`
- 要做以 FlashInfer 为主对象、对比主要用于帮助定位的课程，例如 `FlashInfer vs vLLM` 或 `FlashInfer vs FlashAttention`

如果用户只是问单个 API、单个 kernel、单个 bug 或单个模块实现细节，本 skill 不是首选，应退出课程模式并改为针对性分析。

## 工作流程

1. 先一起判断“输出模式 + 课程包装”：
   - `输出模式`：
      - `课程总纲`：强调为什么这样设计，适合完整文档
      - `课程目录`：强调每课讲什么，适合授课排课
      - `学习路径`：强调先后顺序和依赖
      - `知识地图`：强调模块关系和边界
      - 若用户只说“课程大纲”，默认按 `课程目录` 处理；只有出现“课程设计方案 / 课程总纲 / 完整文档 / 为什么这样设计”这类信号时，才切到 `课程总纲`
   - `课程包装`：
     - `母版总纲`：完整能力地图，给讲师或课程设计者
     - `主课程`：默认 6 课，严格执行“单课单主题”
     - `扩展版主课程`：12 课，只在用户明确要求“更细拆分/讲师版/完整版”时使用
     - `专题高阶课程`：MLA、MoE、Sampling、Communication、JIT/Variants、量化 GEMM 等拆开单讲
2. 再判断这个请求属于哪一类：
   - `系统课程`：围绕 FlashInfer 主线展开，继续走主课程/总纲流程
   - `单主题课程`：例如 `MLA 课程`、`Sampling 专题`，直接按专题课程处理
   - `模块化 onboarding`：例如 `只针对 sampling 模块的 onboarding`，按专题 onboarding 处理，不必扩成系统课程
   - `对比课程`：只有当 FlashInfer 是主对象、对比仅用于帮助定位时，继续使用本 skill；若用户核心问题是理解 FlashInfer 的定位，则继续；若核心问题是选型决策、双向评测或中立比较，则改做普通对比分析
   - `局部技术问答`：单个 API/kernel/bug/局部实现细节，退出课程模式，改做针对性分析
3. 再判断目标读者：
   - 推理服务新人
   - LLM serving 工程师
   - 要做二次开发的 kernel / runtime 开发者
   - 要做专项优化的高阶研发
   - 学术研究者
   - 产品/技术管理者
   - 框架集成开发者
4. 根据目标读者调整课程深度：
   - `推理服务新人`：优先讲清问题定义、系统图景、KV-Cache 抽象和 prefill/decode 主线；弱化源码细节，源码目录只点到为止。推荐阅读子集：`README.md`、官方文档首页、attention API 总览
   - `LLM serving 工程师`：在系统图景基础上补充 wrapper `plan/run`、workspace、多后端选择、CUDAGraph 兼容与性能权衡。推荐阅读子集：attention API、KV layout、page/cascade 文档
   - `kernel / runtime 开发者`：默认采用 `6 课主线 + 硬核专题`；显式增加 API 到目录再到实现的映射，要求读 `flashinfer/`、`include/flashinfer/`、`csrc/`、测试与基准。推荐阅读子集：attention API、KV layout、page/cascade、`flashinfer/`、`include/flashinfer/`、`csrc/`、`tests/`
   - `高阶研发`：在 kernel / runtime 开发者路径上，再强化 variants、低精度、MoE、communication、性能调优与后端差异。推荐阅读子集：kernel generator/JIT、fused MoE、GEMM、sampling、communication、benchmarks/profiler
   - `学术研究者`：强调算法思想、attention 变体、POD-Attention 与 cascade 的设计动机；弱化工程接线细节。推荐阅读子集：`README.md`、attention API、Recursive Attention 教程（见 `link-map.md`）；相关论文以官方 `README` 引用为准，不自行补充
   - `产品/技术管理者`：强调项目定位、能力边界、适用场景、与其他库的关系；避免深入 kernel 实现。推荐阅读子集：`README.md`、官方文档首页；若需对比定位，参考 `topic-map.md` section 11 的优先材料
   - `框架集成开发者`：强调 API 稳定性、版本兼容性、后端选择、与上层框架的接口边界。推荐阅读子集：attention API、page/cascade API、版本说明；若需对比定位，参考 `topic-map.md` section 11 的优先材料
5. 默认叙事顺序保持为：
   - 项目定位
   - Serving 问题定义
   - 数据抽象与 KV-Cache
   - Attention 主线
   - Wrapper `plan/run`
   - 多后端与运行时选择
   - 算子扩展能力
   - 专题深水区
   - 这是完整叙事的参考顺序；默认 `6 课主线` 只覆盖其中的子集，`多后端与运行时选择` 默认不进入 6 课
6. 先判断自己有没有仓库/文档读取能力，并决定 fallback：
   - 若当前能读取仓库与官方文档，先建立仓库级全景，再深入 API 和源码。优先阅读：
     - `README.md`
     - 官方文档首页与 attention API
     - KV layout / page / cascade 相关文档
     - `flashinfer/`
     - `include/flashinfer/`
     - `csrc/`
     - `tests/`
     - `benchmarks/`
     - `profiler/`
   - 若当前不能实时读取仓库或官方文档，也可以基于已有知识生成课程，但必须显式标注“本次输出未实时核对仓库/文档版本，适合作为教学草案，不应冒充逐文件考据版导读”。
   - 若用户要求“最新版本/指定版本”但 release 无法核对，不要伪造版本号；应退回到“未核对版本的教学草案”或先说明无法完成版本敏感请求。
   - 读取能力判断完成后，按需加载 [topic-map.md](./references/topic-map.md) 中对应主题，并优先从 [link-map.md](./references/link-map.md) 取已核对的官方链接；不要默认把所有主题都展开，也不要临场猜 URL。
7. 每一章或每一课必须回答至少前三项；若上下文足够，最好四项都回答：
   - 这一课要解决什么 serving 问题
   - FlashInfer 用什么抽象或 API 回答这个问题
   - 推荐先读哪些文档、页面或仓库位置
   - 它与前后课程如何衔接
   - 执行前提：若当前能核对链接，第 3 项优先给真实、具体、可点击链接；若当前未实时核对仓库或文档，第 3 项只能写到“仓库级目录、官方文档栏目或已知公开 API 页面”这一层，不要伪装成逐文件、逐函数、逐测试的精准导读
8. 如果用户提到“最新版本”或具体版本号，先核对官方 release，再显式写：
   - 版本号
   - 官方发布日期
   - 该版本新增或值得强化的专题
   - 如果输出是 `对比课程`，且用户要求“最新版本/指定版本”，则必须同时核对 FlashInfer 与对比对象的版本号、发布日期；若任一侧无法核对，明确说明并降级为非版本敏感课程草案
   - 若核对失败，明确说明失败，并改用“未核对版本的教学草案”或暂停版本敏感结论
9. 输出完成前必须自检：
   - 每一课是否只有一个核心问题
   - 第 3 课若写成 `Prefill vs Decode`，是否明确把核心主题写成“为什么 serving 中必须区分两条 attention 路径”，而不是把两类实现粗暴并讲
   - 主课程是否把 `MoE / GEMM / Sampling / Communication / JIT Variants / MLA` 的深入实现错误塞回主线
   - 默认 `6 课主线` 是否显式覆盖 `项目定位`、`KV-Cache`、`Prefill/Decode`、`POD-Attention`、`plan()/run()`、`Cascade`
   - `多后端 / CUDAGraph / 平台边界` 是否只在用户明确要求时，或在扩展版/附录中展开
   - 若未实时核对仓库或版本，是否已明确写出这一限制
   - 若未实时核对仓库或版本，阅读建议是否仍停留在安全的目录级/文档栏目级，而没有冒充精确源码导读
   - 若已给推荐阅读，是否尽量写成真实、具体、可点击链接，而不是只写“README / docs / flashinfer/”这类裸名字
   - 读者分层是否已明确，且推荐阅读是否与读者深度匹配
   - 输出模式是否与用户需求匹配，专题课程是否与主课程重复展开同一主题

具体主题索引见 [topic-map.md](./references/topic-map.md)，常用官方链接与 release 入口见 [link-map.md](./references/link-map.md)。

## 输出合同

为避免不同输出模式完全依赖临场发挥，默认采用下面的最小结构：

### 1. 课程总纲

- 适合完整课程文档
- 默认结构：`课程定位`、`目标学员`、`先修要求`、`章节列表`、`专题附录`
- 章节列表默认按“问题定义 -> 数据抽象 -> attention 主线 -> runtime -> 平台边界”排序
- 与课程目录的区别：课程总纲要显式回答“为什么这样设计课程”，而不是只枚举每课标题

### 2. 课程目录

- 适合授课排课
- 默认结构：按“第1课-... / 第2课-...”列出
- 每课默认含 6 个字段：`课程主题`、`为什么这一课重要`、`核心知识点`、`学习目标`、`推荐阅读文件/文档`、`与前后课的衔接`
- 与课程总纲的区别：课程目录强调“每课具体讲什么”，必要时可补时长或演示安排
- 当用户要求“课程目录”“课纲”“第几课”“lesson 版大纲”“按课时拆分”时，优先使用这一模式

#### 编号格式要求

课程目录默认必须使用中文编号格式：

- `第1课-...`
- `第2课-...`
- `第3课-...`

不要默认写成：

- `Lesson 1`
- `Part 1`
- `Chapter 1`

### 3. 学习路径

- 适合自学或 onboarding
- 默认按 3 个阶段输出：`入门认知`、`主线深入`、`专题扩展`
- 每个阶段默认给出：`先学什么`、`为什么此时学`、`建议阅读范围`
- 学习路径强调顺序与依赖，不把每个阶段写成完整课时
- 划分标准：`入门认知` 解决“它是什么”；`主线深入` 解决“它如何工作”；`专题扩展` 解决“我如何用/改/优化某个具体能力”

### 4. 知识地图

- 适合快速建立模块关系
- 默认按 `主题 -> 要解决的问题 -> 关键抽象/API -> 相邻主题` 的四列或四项结构输出
- 知识地图强调并列关系、依赖关系和边界，不展开成完整授课话术

### 5. 培训计划 / 内部分享 / onboarding 提纲

- 若用户说的是这三类需求，默认在“课程目录”结构上轻量改写
- 额外补 3 项：`受众`、`时长`、`交付目标`
- 若用户没有指定总时长，默认先按 `1 次分享` 或 `6 课主课程` 两种常见包装给出建议

### 6. 单主题课程 / 专题课程

- 适合 `MLA 课程`、`Sampling 专题`、`JIT variants 专题` 这类只围绕一个能力域展开的请求
- 默认结构：`主题定位`、`为什么值得单独成课`、`知识边界`、`3 到 5 个子章节`、`推荐阅读`
- 子章节仍遵守单课单主题，不要因为是专题课就退回“功能清单”
- 若用户未指定粒度，默认按“1 门专题课”而不是“扩成 6 课主线”
- 使用方式：先使用这里的结构，再到后面的“专题高阶课程建议”里选择对应专题作为内容来源
- 例如：`MLA 课程` 使用这里的结构 + 后文 `专题四` 的主题内容；`Sampling onboarding` 使用这里的结构或模块化 onboarding 结构 + 后文 `专题五` 的内容

### 7. 模块化 Onboarding

- 适合 `只针对 sampling 模块的 onboarding`、`只针对 MLA 的新人导读`
- 默认结构：`对象是谁`、`先修要求`、`先看什么`、`最小工作流`、`常见误区`、`下一步深入方向`
- 模块化 onboarding 强调“快速进入某个模块”，不要求补齐系统主线
- `最小工作流` 指“进入该模块所需的最短闭环”，通常由 `先读什么 -> 跑什么最小示例/调用链 -> 看什么输出或状态变化` 组成，不要求给完整工程实现

### 8. 对比课程

- 适合 `FlashInfer vs vLLM`、`FlashInfer vs FlashAttention` 这类以 FlashInfer 为主对象的对比型课程
- 默认结构：`对比目的`、`对比维度`、`FlashInfer 的定位`、`关键差异`、`适用场景`、`延伸阅读`
- 默认按“定位 -> 抽象 -> 机制 -> 场景”组织，不按零散 benchmark、feature checklist 或逐 API 罗列组织正文
- 对比课程的主语必须仍然是 FlashInfer；若用户真正要的是双向中立对比分析，应明确说明“以下不再按本 skill 的课程模板输出”，然后改做普通对比分析

## 核心教学规则：单课单主题

### 主规则

- 同一课默认只讲 `一个重要问题`
- 一个主题可以带少量紧邻子点，但不能跨不同问题域
- 课时标题若同时出现 `KV-Cache`、`调度`、`量化`、`MoE`、`采样` 这类并列词，优先拆课

### 可以放在同一课内部展开的情况

- `Paged KV-Cache` 一课里带出 `kv_indptr / kv_indices / last_page_len`
- `Decode Wrapper` 一课里带出 `plan()` 与 `run()` 的配合
- `Cascade Attention` 一课里带出 `merge_state / merge_states`
- `Sampling` 一课里带出 `Top-K / Top-P / Min-P` 的排序规避思想

### 默认必须拆开的情况

- `Prefill` 和 `Decode`
- `Paged KV-Cache` 和 `Ragged KV-Cache`
- `Attention Wrapper` 和 `JIT Attention Variants`
- `MLA` 和 `普通 Attention`
- `GEMM` 和 `MoE`
- `Sampling` 和 `Communication`
- `Communication` 和 `CUDAGraph`
- `JIT Variants` 和 `多后端选择`

### 默认 6 课压缩版允许合并的例外

- 只在 `默认 6 课主线` 中，为了保住主线闭环，可把若干紧邻主题压进同一课
- 这类合并必须把课题写成“统一抽象 / 对照关系 / 运行时闭环”，不能退化成两个实现并讲
- 第 2 课允许把 `Paged / Ragged / Layout / Append / Page API` 合并为 `KV-Cache 与状态模型`
- 第 3 课允许把 `Prefill / Decode` 合并为“为什么 serving 中必须区分两条 attention 路径”
- 第 5 课允许把 `plan() / run() / workspace / partial state` 合并为 `Wrapper 两阶段执行`

### 主课程内容边界

默认 `6 课主线` 只围绕下面这条链路组织：

- FlashInfer 项目定位
- KV-Cache 与状态模型
- prefill / decode 的对照主线
- POD-Attention
- wrapper 的 `plan/run`
- cascade/shared prefix

`多后端选择 / CUDAGraph / 平台边界` 默认不进入 6 课主线，应放到：

- `12 课扩展版主课程`
- 专题课
- 或附录/收束模块

### 主课程与专题课的统一分界原则

- 主课程覆盖“理解 FlashInfer 如何工作所必须知道的最小知识集”
- 专题课程覆盖“使用、扩展或优化某个具体能力时需要知道的深度知识”
- 如果一个主题在主课程里已经出现，专题课应继续向下挖实现、约束、接口或性能，而不是重复主课程的入门叙述
- 例如：主课程可以讲 `POD-Attention 为什么重要`，专题课再讲 `POD-Attention 的 API、调度和性能权衡`
- 例如：主课程可以讲 `KV-Cache 是什么`，专题课再讲 `Page Table / append / layout` 的细节与接口

默认不进入主课程、应下放专题的内容：

- MoE 深入实现
- GEMM 量化细节
- Sampling 内核家族
- Communication / AllReduce / NVSHMEM
- 自定义 attention variants / JIT 模板展开
- MLA 的矩阵吸收与专用 paged attention

如果需要在主课程末尾补一个收束章节，该章节只能做“平台能力全景回看”，用于说明 FlashInfer 不止有 attention，还扩展到了 GEMM、MoE、sampling 与 communication；不得把这些主题重新展开成主课程内部的独立讲授内容。

## 必须覆盖的五大块

这五大块用于约束 skill 的整体能力地图。它们可以分布在 `默认 6 课主线`、`12 课扩展版`、专题课或附录中，不要求默认 6 课逐项全部展开。

### 1. 项目定位与问题定义

至少回答：

- FlashInfer 为什么不是“又一个 attention kernel”，而是推理内核库与 kernel generator
- 它主要服务什么场景：prefill、decode、mixed batching、dynamic batch serving
- 它与 FlashAttention、cuDNN、CUTLASS、TensorRT-LLM 的关系是什么

对应课次：

- `6 课主线第 1 课`
- `12 课扩展版第 1 课`

### 2. 统一数据抽象：KV-Cache 与变长输入

至少回答：

- 什么是 paged KV-Cache
- 什么是 ragged tensor / ragged KV-Cache
- `NHD / HND` 布局分别是什么
- page table、`indptr`、`indices`、`last_page_len` 在 API 中分别扮演什么角色

对应课次：

- `6 课主线第 2 课`
- `12 课扩展版第 2 到第 4 课`

### 3. Attention 主线：prefill / decode / append / cascade

至少回答：

- 为什么要把 prefill 和 decode 拆开看
- `BatchPrefillWithPagedKVCacheWrapper` 和 `BatchDecodeWithPagedKVCacheWrapper` 的职责差异
- POD-Attention / fused prefill + decode 在 mixed batching 中解决什么问题
- `plan()` 和 `run()` 为什么是两阶段
- cascade/shared prefix 解决什么问题，为什么需要 merge state

对应课次：

- `6 课主线第 3 到第 6 课`
- `12 课扩展版第 5 到第 10 课`

### 4. Runtime 组织：workspace、多后端、CUDAGraph

至少回答：

- workspace 保存了什么中间状态
- 多后端自动选择想解决什么现实问题
- CUDAGraph compatible wrapper 为什么存在
- FlashInfer 如何兼顾高吞吐和低延迟 serving

补充说明：

- `workspace` 部分默认由 `6 课主线第 5 课` 覆盖
- `多后端自动选择` 与 `CUDAGraph compatible wrapper` 默认放到 `12 课扩展版第 11 课`、专题课或附录

对应课次：

- `6 课主线第 5 课` 负责 `workspace`
- `12 课扩展版第 11 课` 负责 `多后端 / CUDAGraph`

### 5. 能力扩展：从 attention 到推理算子平台

至少回答：

- 除 attention 外，FlashInfer 还覆盖哪些能力：GEMM、MoE、sampling、communication
- 为什么这些能力适合和 attention 放在同一个推理内核库里
- 哪些主题适合做专题高阶课程

对应课次：

- 默认不进入 `6 课主线`
- `12 课扩展版第 12 课` 只做平台边界回看
- 深入内容下放专题课

## 主课程建议模板

默认主课程采用 `6 课硬核主线`。若用户未指定时长，默认按 `每课 1 小时（45 分钟讲授 + 15 分钟讨论/问答）` 估算内容深度：

1. FlashInfer 的项目定位与问题定义：它为什么是“推理内核库 + 生成器”
2. KV-Cache 与状态模型：Paged / Ragged / Layout / Append / Page API 如何构成统一数据抽象
3. Attention 主线：Prefill vs Decode 为什么必须对照着看
4. POD-Attention：mixed batching 下的 fused prefill + decode 为什么是 FlashInfer 的辨识度
5. Wrapper 两阶段执行：`plan()` / `run()` / workspace / partial state 怎样构成 runtime 闭环
6. Cascade / Shared Prefix：服务端前缀复用为什么值得单独建模

补充提醒：

- 这 6 课是默认输出，最适合 `kernel / runtime 开发者` 和想抓住主线的 serving 工程师。
- 第 2 课可以吸收 `Append/Page API`，因为它仍属于 KV-Cache 的状态写入路径；不要把它挪到 `POD-Attention` 一课里。
- 第 6 课默认只讲 `Cascade / Shared Prefix`，不要再把多后端、CUDAGraph、平台边界一起塞进来。
- `多后端选择 / CUDAGraph / 平台边界` 默认降为扩展版或附录；只有用户明确要求 runtime 全景时再展开。
- 第 3 课的核心主题是“为什么 serving 中必须区分 Prefill 和 Decode 两条路径”，不是把两类实现细节全部塞进一课。
- 第 6 课在讲 `merge_state / merge_states` 时，应显式回接第 5 课的 `workspace / partial state`，说明它是在既有运行时状态上的合并，而不是凭空出现的新机制。

## 扩展版主课程模板

若用户明确要求“完整版 / 更细拆分 / 讲师版 / 12 课版本”，可升级为下面的扩展版主课程：

1. FlashInfer 的项目定位与问题定义：它为什么是“推理内核库 + 生成器”
2. Paged KV-Cache：FlashInfer 的基础状态抽象
3. Ragged Tensor 与 Ragged KV-Cache：如何避免 padding 浪费
4. Append 与 Page API：新 K/V 如何进入缓存
5. Prefill Attention：长 query 阶段的核心计算路径
6. Decode Attention：单步生成阶段的核心计算路径
7. POD-Attention：mixed batching 下的 fused prefill + decode
8. Wrapper 的 `plan()`：调度规划与辅助结构复用
9. Wrapper 的 `run()`：workspace、partial state 与最终执行
10. Cascade Attention：共享前缀与分层 KV 复用
11. 多后端与运行时选择：FA/cuDNN/CUTLASS/TRT-LLM 如何协同，以及 CUDAGraph compatible wrapper 的存在动机与使用约束
12. FlashInfer 的平台边界：attention 主线之外还扩展到了哪些算子族

扩展版拆分原则：

- `plan()` 与 `run()` 在默认 6 课中可以合并，因为目标是理解 runtime 闭环
- 到了 12 课扩展版则应拆开，因为此时目标已从“理解闭环”升级为“分别理解计划阶段和执行阶段的职责、输入输出与实现差异”
- `NHD / HND` 布局对后端选择的影响，默认放回前面的 KV-Cache / 布局课程衔接中说明，不再塞进第 11 课

## 专题高阶课程建议

当用户要求深度版、kernel/runtime 开发者专题营或主线后的硬核补充时，优先拆成下面这些专题：

- `专题一` FlashInfer Attention API 全景：在主课程 attention 主线基础上，继续深入 single request、batch、paged、ragged 的 API 分层、调用约束与使用边界
- `专题二` KV Layout 与 Page Table：在主课程 KV-Cache 基础上，继续深入 `indptr`/`indices`/`last_page_len`、layout 选择与 append/page 接口细节
- `专题三` Cascade 与 Shared Prefix：在主课程 Cascade 基础上，继续深入多层级前缀复用、state merge 与 merge_state 路径
- `专题四` MLA Attention：DeepSeek 系列模型的专用支持。本专题覆盖主线课程未涉及的模型特化 attention 领域，建议在主课程之后按需选修。
- `专题五` Sampling 内核：Top-K / Top-P / Min-P / speculative sampling。本专题覆盖主线课程未涉及的生成后处理领域，建议在主课程之后按需选修。
- `专题六` Fused MoE：CUTLASS / TRT-LLM 后端与量化 MoE。本专题覆盖主线课程未涉及的专家模型推理领域，建议在主课程之后按需选修。
- `专题七` GEMM 与低精度计算：BF16 / FP8 / FP4。本专题覆盖主线课程未涉及的低精度矩阵计算领域，建议在主课程之后按需选修。
- `专题八` Communication：AllReduce、NVSHMEM、MNNVL。本专题覆盖主线课程未涉及的通信算子领域，建议在主课程之后按需选修。
- `专题九` JIT 与 Attention Variants：从模板到专用 kernel。本专题覆盖主线课程未涉及的可扩展 attention 变体领域，建议在主课程之后按需选修。
- `专题十` 基准测试与性能分析：benchmarks 与 profiler。本专题覆盖主线课程未深入展开的性能实验与分析领域，建议在主课程之后按需选修。

## 推荐阅读与链接来源

- 输出里若要写 `推荐阅读 / 推荐文档 / 推荐链接`，优先复用 [link-map.md](./references/link-map.md) 里已核对的官方链接，以及 [topic-map.md](./references/topic-map.md) 各主题下的“优先材料”。
- 不要手写或猜测 URL；若 `link-map.md` 中没有该链接，先核对官方页面，再写入输出。
- 若当前无法核对链接真实性，明确说明限制，并降级到“官方文档栏目 / GitHub 仓库目录 / 仓库模块路径”这一层。

## 输出风格要求

- 优先输出可以直接授课的中文 Markdown
- 课时标题尽量采用“问题 + 机制”式命名
- 若用户没有指定篇幅，默认先给“精简但完整”的版本：
  - 系统主课程每课按 6 个字段输出，每字段 1 到 2 句，精简但不省字段
  - 单主题课程 / 模块化 onboarding / 对比课程 仍按各自输出合同完整展开，不退化成只列标题
  - 只有在“专题列表/专题建议”场景下，专题课程才只列标题与定位
- `推荐阅读` 默认应使用真实、具体、可点击链接；只有在当前无法核对链接时，才退回到目录级或栏目级描述，并明确说明限制
- 每课尽量包含：
  - 学习目标
  - 为什么重要
  - 核心概念
  - 推荐阅读文件/文档
  - 与上下文的衔接关系
- 不要把 README 的 feature list 直接改写成课程目录，必须重排成教学顺序

## 快速判断模板

这部分只用于“用户需求很模糊、但明显是在要课程材料”的快速兜底。若它与上面的工作流程冲突，以工作流程为准。

如果用户只说“给我一个 FlashInfer 课程大纲”，默认输出：

- `课程目录` 模式
- `6 课硬核主课程`
- 用中文
- 严格单课单主题
- 以 attention serving 主线为主体
- 把 MoE / sampling / communication / JIT variants 放到专题高阶课程附录

如果用户明确说“我要母版总纲 / 知识地图 / 深度版”，则：

- 先给完整能力地图
- 再按 `6 课主线 + 硬核专题` 重组
- 保持主线与专题分离，不重复统计同一主题

如果用户明确说“我要完整版 / 更细课时 / 12 课版”，则：

- 使用扩展版主课程模板
- 保持 12 课仍然围绕主线细拆，而不是把专题硬塞回主课程

如果用户明确说“给我一个 MLA 课程 / Sampling 专题 / JIT 课程”这类单主题请求，则：

- 使用“单主题课程 / 专题课程”输出合同
- 默认输出 `1 门专题课 + 3 到 5 个子章节`
- 再从专题高阶课程建议里选择对应专题作为内容来源

如果用户明确说“给我一个 sampling onboarding / MLA onboarding”这类模块化 onboarding，则：

- 使用“模块化 Onboarding”输出合同
- 聚焦最小工作流，不扩成系统主课程

如果用户明确说“给我一个 FlashInfer vs vLLM / FlashAttention 对比课程”，则：

- 使用“对比课程”输出合同
- 以 FlashInfer 为主语组织课程；若用户要双向中立比较，则退出课程模板，改做普通对比分析
