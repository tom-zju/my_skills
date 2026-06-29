# 上游 vLLM 热点优先级

> **本表是启发式优先级参考，不是完整清单。真实检查范围必须来自当前 `vllm_ecu` 的耦合点扫描结果和上游 `$BASE_TAG..$TARGET_TAG` diff 的并集。不要被本表限制住。**

## 热点表

按以下优先级分析发生变化的上游 `vllm/` 文件：

| 优先级 | 上游区域 | 关注原因 |
|---|---|---|
| P0 | `vllm/platforms/` | 平台抽象方法、能力开关、设备行为 |
| P0 | `vllm/forward_context.py` 或等价路径 | ECU worker 和 omni worker 会 patch forward context |
| P0 | `vllm/v1/worker/` | ECU worker patch 依赖 worker/model runner 签名 |
| P0 | `vllm/v1/attention/` | Attention metadata、builder、flash attention 工具函数 |
| P0 | `vllm/v1/attention/backends/fa_utils.py`、`vllm/model_executor/layers/attention/mla_attention.py` | ECU 初始化和 flash attention patch 直接依赖这些符号 |
| P0 | `vllm/model_executor/layers/fused_moe/` | ECU 自定义 MoE kernel 和 router 会镜像这些 API |
| P1 | `vllm/v1/sample/` | ECU patch 了 penalties、rejection sampler、top-k/top-p sampler 等采样路径 |
| P1 | `vllm/model_executor/layers/quantization/` | ECU 量化适配代码可能继承或 patch 上游类 |
| P1 | `vllm/distributed/` | ECCL 替换 NCCL，KV transfer connector 依赖这些路径 |
| P1 | `vllm/device_allocator/` | ECU worker 可能替换 device allocator 或 cumem 路径 |
| P1 | `vllm/compilation/`、`vllm/compilation/backends.py` | ECU compiler patch 依赖 pass manager 和 backend API |
| P1 | `vllm/v1/spec_decode/` | ECU patch 了 eagle speculative decoding 的 slot mapping 和 batch 更新路径 |
| P1 | `vllm/config/`、`vllm/config*.py` | 配置字段频繁移动，容易触发 `AttributeError` |
| P2 | `vllm/v1/core/` | 核心调度器和 KV cache 管理器，变动影响范围大 |
| P2 | `vllm/model_executor/parameter/` | 模型参数加载接口，ECU import 频率较高 |
| P2 | `vllm/entrypoints/` | CLI/OpenAI 入口 patch 可能受影响 |
| P2 | `vllm/model_executor/models/` | 模型接口变化可能影响 omni 或模型专属 patch |

## 使用方式

1. 先运行 `scripts/extract_vllm_couplings.py` 获取真实耦合点。
2. 再从上游 diff 中找出发生变化的 `vllm/` 文件。
3. 对真实耦合点、上游变化文件、本热点表取并集。
4. 对 P0 项优先做源码阅读和签名验证；P1/P2 根据实际 diff 和失败症状推进。
