# vLLM-Omni 14 课权威硬核主课程模板

这个参考文件用于生成“第几课”形式的课程目录。默认不输出专题营，而是直接输出 14 课权威硬核主课程。

## 课程目录输出总规则

只要用户要求“课程目录”“课纲”“学习大纲”“按课时拆分”，默认优先输出 lesson 化课程目录。

### 标题格式要求

课程目录默认必须使用中文编号格式：

1. `第1课-vLLM-Omni 环境搭建、源码结构与运行基线`
2. `第2课-vLLM-Omni 项目定位与总体架构`
3. `第3课-Stage Configs 与异构多阶段 Pipeline 建模`

不要默认使用英文标题格式，例如：

- `Lesson 1`
- `Week 1`
- `Chapter 1`

### 最重要规则：单课单主题

课程目录默认必须遵守：

- 一课只讲一个重要主题
- 如果一课标题中出现多个不同问题域，应优先拆课
- 默认不再拆专题营
- 外围内容不挤占硬核主课程

## 模板一：14 课权威硬核主课程

适用于：

- 团队源码培训
- 工程硬核入门课
- vLLM-Omni 架构与 runtime 深度导读
- 多模态推理服务研发 onboarding

推荐课时：

- `14 课`

默认目录：

1. `第1课-vLLM-Omni 环境搭建、源码结构与运行基线`
2. `第2课-vLLM-Omni 项目定位与总体架构`
3. `第3课-Stage Configs 与异构多阶段 Pipeline 建模`
4. `第4课-AsyncOmniEngine 请求提交主链`
5. `第5课-Orchestrator 多阶段编排机制`
6. `第6课-多阶段输出路由与中间表示设计`
7. `第7课-AR Runtime：Scheduler、Worker 与执行主流程`
8. `第8课-AR ModelRunner、多模态 Payload 与 Hidden State 暴露`
9. `第9课-Diffusion Runtime：Engine、Scheduler 与 Pipeline`
10. `第10课-Diffusion Attention：Backend、Ring 与 Ulysses`
11. `第11课-Diffusion Parallelism：TP、SP、CFG、HSDP 与 VAE Patch Parallel`
12. `第12课-Diffusion Cache 加速：TeaCache 与 cache-dit`
13. `第13课-OmniConnector、CFG Companion Flow 与 Fully Disaggregated Serving`
14. `第14课-Stage Input Processor 与 Qwen3-Omni 全链路案例`

说明：

- 标准权威版主课程默认固定为 `14 课`
- 不再默认输出专题高阶课程
- 环境搭建被纳入第 1 课，但定位为源码课工程基线，而不是普通安装教程
- Diffusion Attention、Diffusion Parallelism、Diffusion Cache 都进入主课程
- OpenAI API 使用、ComfyUI、Helm、benchmark、metrics、profiler、生态集成默认不独立成课
- `OmniConnector` 是主课程硬核内容，与 CFG Companion Flow 和 fully disaggregated serving 一起讲

## 每一课默认结构

课程目录模式下，每一课默认应包含：

- `课程主题`
- `为什么这一课重要`
- `核心知识点`
- `学习目标`
- `推荐阅读文件`
- `建议练习或演示`

## 推荐阅读入口

默认按下面顺序组织阅读：

1. `README.md`
2. `docs/getting_started/installation/`
3. `docs/getting_started/quickstart.md`
4. `docs/design/architecture_overview.md`
5. `docs/configuration/stage_configs.md`
6. `docs/design/module/async_omni_architecture.md`
7. `docs/design/module/ar_module.md`
8. `docs/design/module/dit_module.md`
9. `docs/design/feature/tensor_parallel.md`
10. `docs/design/feature/sequence_parallel.md`
11. `docs/design/feature/cfg_parallel.md`
12. `docs/design/feature/hsdp.md`
13. `docs/design/feature/vae_parallel.md`
14. `docs/design/feature/cache_dit.md`
15. `docs/design/feature/teacache.md`
16. `docs/design/feature/disaggregated_inference.md`
17. `docs/models/supported_models.md`
18. `vllm_omni/engine/`
19. `vllm_omni/diffusion/`
20. `vllm_omni/distributed/omni_connectors/`
21. `vllm_omni/model_executor/stage_input_processors/`

## 压缩规则

如果用户要求减少课程：

- `12 课版`：可合并 `Diffusion Cache` 到 `Diffusion Runtime`，或合并 `AR Runtime` 与 `AR ModelRunner`
- `10 课版`：可把 `Diffusion Attention / Parallelism / Cache` 压成一课，把 `Stage Input Processor` 并入 Qwen3-Omni 案例
- `8 课版`：只保留架构、stage configs、AsyncOmniEngine、Orchestrator、AR、Diffusion、OmniConnector、Qwen3-Omni 案例

压缩时优先删除或合并外围内容，不要删除 `Stage Configs`、`AsyncOmniEngine`、`Orchestrator`、`AR Runtime`、`Diffusion Runtime`、`OmniConnector`。

## 常见错误

- 把第 1 课写成普通安装教程，而不是源码课运行基线
- 把 Diffusion Attention、Parallelism、Cache 重新下放成可选专题
- 把 API 使用、ComfyUI、Helm、benchmark 独立成主课
- 把 `OmniConnector` 只写成“序列化工具”
- 把 Qwen3-Omni 案例写成模型介绍，不回到 stage input processor 和全链路复盘
