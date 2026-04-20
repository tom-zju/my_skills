# vLLM-Omni 权威硬核课程覆盖地图

这个参考文件用于保证课程总纲或课程目录不会退化成普通 vLLM 课程、单一模型分析、API 使用教程或生态功能清单。

## 一、最低覆盖面

一份完整的 vLLM-Omni 权威硬核课程材料，默认至少覆盖七层主线：

1. `工程基线层`
   - 环境搭建
   - 仓库结构
   - 最小运行样例
   - 后续源码调试入口
2. `项目架构层`
   - vLLM-Omni 是什么
   - 为什么需要 any-to-any / omni-modality serving
   - 它和 vLLM text-only AR serving 的关系
   - AR + DiT + heterogeneous outputs
3. `多阶段建模层`
   - stage configs
   - `stage_args`
   - `engine_args`
   - `runtime.edges`
   - `engine_input_source`
   - `prompt_expand_func`
   - `cfg_kv_collect_func`
4. `编排与中间表示层`
   - AsyncOmniEngine
   - Orchestrator
   - stage client / proc
   - output routing
   - intermediate representation
   - final output aggregation
5. `AR Runtime 层`
   - OmniARScheduler
   - OmniGenerationScheduler
   - GPUARWorker
   - OmniGPUModelRunner
   - payload / hidden state / multimodal output
6. `Diffusion Runtime 与优化层`
   - DiffusionEngine
   - diffusion scheduler
   - pipeline forward
   - step execution
   - attention backend
   - Ring / Ulysses
   - TP / SP / CFG / HSDP / VAE Patch Parallel
   - TeaCache / cache-dit
7. `解耦执行与模型适配层`
   - OmniConnector
   - CFG Companion Flow
   - Fully Disaggregated Serving
   - Stage Input Processor
   - Qwen3-Omni 全链路案例

## 二、推荐阅读顺序

默认按这个顺序建立主线全景：

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
19. `vllm_omni/core/sched/`
20. `vllm_omni/worker/`
21. `vllm_omni/diffusion/`
22. `vllm_omni/distributed/omni_connectors/`
23. `vllm_omni/model_executor/stage_input_processors/`

如果用户要求对齐某个具体版本，必须补充核对：

- 官方 release/tag 或本地 tag
- 该版本发布日期
- 当前本地 commit
- README Latest News 中和课程相关的新增重点

具体输出模板见 [version-check-patterns.md](./version-check-patterns.md)。

## 三、课程设计优先级

本 skill 的课程设计优先级如下：

1. `保留 14 课硬核主线`
2. `同一课只讲一个重要主题`
3. `优先删除外围课，不删除系统主干`
4. `最后才考虑总课时数是否好看`

如果这四条冲突，优先级从上到下依次更高。

## 四、硬核主题覆盖清单

### 1. 工程运行基线

默认覆盖：

- 安装入口
- quickstart
- examples
- 仓库目录结构
- `vllm_omni/` 主包结构
- 最小 offline / online 运行路径

这一课不能写成普通“装包教程”，要服务于后续源码阅读。

### 2. 总体架构

默认覆盖：

- EntryPoints
- AsyncOmniEngine
- Orchestrator
- AR runtime
- Diffusion runtime
- OmniConnector
- AR as main
- DiT as main
- AR + DiT

### 3. Stage Configs

默认覆盖：

- `stage_args`
- `runtime.process`
- `runtime.devices`
- `engine_args`
- `worker_type`
- `scheduler_cls`
- `engine_output_type`
- `engine_input_source`
- `custom_process_input_func`
- `prompt_expand_func`
- `cfg_kv_collect_func`
- `runtime.edges`
- `window_size`
- `max_inflight`

写作时要讲清：stage configs 是课程里连接“模型结构”和“系统执行”的关键桥梁。

### 4. AsyncOmniEngine 与 Orchestrator

默认覆盖：

- `AsyncOmniEngine.add_request`
- input processor
- request queue / output queue
- `_bootstrap_orchestrator`
- `_initialize_stages`
- `Orchestrator._request_handler`
- stage output polling
- `_route_output`
- `_forward_to_next_stage`
- final output handler

### 5. 中间表示与输出路由

默认覆盖：

- `output_processor.py`
- `mm_outputs.py`
- `output_modality.py`
- `serialization.py`
- latent
- hidden states
- audio
- text
- final output aggregation

这课是硬核主线，不能被省略。

### 6. AR Runtime

默认覆盖：

- `OmniARScheduler`
- `OmniGenerationScheduler`
- `GPUARWorker`
- `GPUGenerationWorker`
- `OmniGPUModelRunner`
- `GPUARModelRunner`
- prompt embedding overlay
- additional information serialization
- hidden state exposure
- `MultimodalOutputProcessor`

### 7. Diffusion Runtime

默认覆盖：

- `DiffusionEngine`
- diffusion scheduler
- worker process
- `DiffusersPipelineLoader`
- model pipeline
- `OmniDiffusionRequest`
- pre/post processing registry
- diffusion step loop
- VAE decode

### 8. Diffusion Attention

默认覆盖：

- attention backend 抽象
- SDPA
- FlashAttention
- SageAttention
- Ring Attention
- Ulysses
- backend 与 parallel attention strategy 的层级差异

### 9. Diffusion Parallelism

默认覆盖：

- TP
- SP
- CFG parallel
- HSDP
- VAE Patch Parallel
- 切分对象
- 通信方式
- 适用场景

### 10. Diffusion Cache

默认覆盖：

- TeaCache
- cache-dit
- cache backend selector
- CFG-aware cache branch
- 与 pipeline / transformer / step loop 的关系

### 11. OmniConnector 与 CFG Companion Flow

默认覆盖：

- `OmniConnectorBase`
- `put/get` API
- metadata passing
- SharedMemoryConnector
- MooncakeStoreConnector
- MooncakeTransferEngineConnector
- YuanrongConnector
- CFG Companion Flow
- Fully Disaggregated Serving

不要把 OmniConnector 写成普通序列化工具；重点是跨 stage、跨进程、跨节点的 artifact transfer 抽象。

### 12. Stage Input Processor 与 Qwen3-Omni

默认覆盖：

- `stage_input_processors`
- Qwen3-Omni
- Thinker / Talker / Code2wav
- 输入改写
- 跨 stage 桥接
- 全链路复盘

## 五、默认不独立成课的内容

以下内容可以作为练习、附录或扩展阅读，但默认不独立成课：

- API 使用教程
- ComfyUI
- Helm
- benchmark
- metrics
- profiler
- custom pipeline
- 大而全模型支持列表
- LoRA
- CPU offload
- 单独 quantization 课程

## 六、单课单主题检查清单

在输出课程目录前，逐课检查：

- 这一课能不能用一句话说明“只解决哪个核心问题”
- 这课的推荐阅读文件是否集中在一个问题域
- 这课的核心知识点是否都围绕同一条执行链路
- 这一课是否有明确源码入口或设计文档
- 如果把其中一半内容删掉，剩下的一半是否还能独立成课

如果以上任一项回答不稳，说明这课大概率过宽，需要拆课。

## 七、常见偏题点

- 把环境搭建课写成普通安装说明，而不是源码课运行基线
- 把 vLLM-Omni 写成普通 vLLM 多模态输入课程
- 只讲 Qwen3-Omni，不讲项目架构和 stage pipeline
- 只讲 DiT，不讲 AR 与 DiT 的异构编排
- 只列 OpenAI API，不讲请求如何进入 engine 和 stage
- 把 Diffusion Attention、Parallelism、Cache 重新移出主课程
- 把 TeaCache/cache-dit 当成可有可无的边角优化
- 只列 connector 名称，不讲 per-edge wiring 与 metadata passing
- 把 stage configs 讲成 YAML 参数说明，不讲它如何驱动运行时
- 把模型支持列表当作课程目录
- 未核实就写具体版本时间线
