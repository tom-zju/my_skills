# My Skills

A collection of Claude Code skills for structured, high-quality analysis tasks.

## Skills

### [paper-deep-dive](./paper-deep-dive/)

深度解读单篇学术论文，产出结构化、证据驱动、博客级的论文分析。

**适用场景：**
- 论文深读、方法架构拆解、研究脉络梳理
- 判断实验是否真正支撑论文 claim
- 为博客、技术分享、组会汇报准备高质量材料

**输出内容：** 论文概览 → 研究脉络 → 核心贡献 → 方法架构 → 实验解读 → 局限性分析 → 延伸阅读

### [vllm-course-outline](./vllm-course-outline/)

为 vLLM 生成中文课程总纲、课程目录、学习大纲、知识地图和学习路径。

**适用场景：**
- 系统梳理 vLLM 项目总览、技术发展、架构全景、核心组件、关键特性
- 设计分布式并行、offloading、attention backend、structured outputs、工具调用等专题课程
- 按"单课单主题"原则设计主课程或专题高阶课程
- 为内部培训、技术分享、onboarding 材料生成结构化中文课纲

**输出内容：** 课程总纲 → 课程目录（第X课格式）→ 学习路径 → 知识地图 → 专题高阶课程

### [sglang-course-outline](./sglang-course-outline/)

为 SGLang 生成中文课程总纲、课程目录、学习大纲、知识地图和学习路径。

**适用场景：**
- 系统梳理 SGLang 项目总览、技术发展、双层体系架构、SRT 运行时主链、调度与缓存机制
- 设计 RadixAttention、前缀缓存、Chunked Prefill、注意力后端、PD/EPD 解耦、HiCache、结构化输出、Tool/Reasoning Parser、并行与多模态等专题课程
- 按"单课单主题"原则设计主课程或专题高阶课程
- 为内部培训、技术分享、onboarding 材料生成结构化中文课纲

**输出内容：** 课程总纲 → 课程目录（第X课格式）→ 学习路径 → 知识地图 → 专题高阶课程

### [flashinfer-course-outline](./flashinfer-course-outline/)

为 FlashInfer 生成中文课程总纲、课程目录、学习路径、知识地图和培训提纲。

**适用场景：**
- 系统梳理 FlashInfer 的项目定位、attention serving 主线、KV-Cache、prefill/decode、wrapper 的 `plan/run` 与 cascade
- 设计 MLA、MoE、sampling、communication、JIT variants、量化 GEMM 等专题课程
- 按"单课单主题"原则设计主课程、专题高阶课程、模块化 onboarding 或以 FlashInfer 为主对象的对比课程
- 为内部培训、技术分享、onboarding 材料生成结构化中文课纲

**输出内容：** 课程总纲 → 课程目录（第X课格式）→ 学习路径 → 知识地图 → 专题高阶课程 → 培训/分享/onboarding 提纲

### [vllm-omni-course-outline](./vllm-omni-course-outline/)

为 vLLM-Omni 生成中文权威硬核课程总纲、课程目录、学习大纲、知识地图和学习路径。

**适用场景：**
- 系统梳理 vLLM-Omni 环境基线、项目定位、AR/DiT 异构多阶段架构、stage configs、AsyncOmniEngine、Orchestrator 与多阶段输出路由
- 设计 AR runtime、Diffusion runtime、Diffusion Attention/Parallelism/Cache、OmniConnector、CFG Companion Flow、Fully Disaggregated Serving、Stage Input Processor、Qwen3-Omni 等硬核课程
- 按“单课单主题”原则设计 14 课硬核主课程
- 为内部培训、技术分享、源码导读、onboarding 材料生成结构化中文课纲

**输出内容：** 课程总纲 → 课程目录（第X课格式）→ 学习路径 → 知识地图 → 14 课权威硬核主课程

## 使用方式

在 Claude Code 中，将 skill 目录加入配置后即可通过对应命令调用。

```bash
# 克隆仓库
git clone git@github.com:tom-zju/my_skills.git
```
