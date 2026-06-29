# 上游 vLLM 到 vllm_ecu 路径映射

> **本表是启发式优先级参考，不是完整清单。真实检查范围必须来自当前 `vllm_ecu` 的耦合点扫描结果和上游 `$BASE_TAG..$TARGET_TAG` diff 的并集。不要被本表限制住。**

对每个高优先级上游变化，优先使用 `scripts/extract_vllm_couplings.py` 输出中的 `file` 字段定位对应 ECU 文件。脚本已自动完成耦合点定位，本表提供语义解释和补漏参考。

## 映射表

| 上游 vLLM 路径 | 需要检查的 ECU 文件 |
|---|---|
| `vllm/platforms/` | `vllm_ecu/ecu.py`、`vllm_ecu/__init__.py` |
| `vllm/forward_context.py` 或等价路径 | `vllm_ecu/utils.py`、`vllm_ecu/worker/worker_v1.py`、`vllm_ecu/patch/ecu_patch/forward_context.py`、`vllm_ecu/patch/vllm_omni_patch/workers.py` |
| `vllm/v1/worker/` | `vllm_ecu/worker/worker_v1.py`、`vllm_ecu/patch/vllm_omni_patch/workers.py` |
| `vllm/v1/attention/`、`vllm/v1/attention/backends/fa_utils.py` | `vllm_ecu/__init__.py`、`vllm_ecu/attention/`、`vllm_ecu/patch/ecu_patch/flash_attn.py` |
| `vllm/model_executor/layers/attention/` | `vllm_ecu/attention/`、`vllm_ecu/kernels/`、attention 相关 patch |
| `vllm/model_executor/layers/attention/mla_attention.py` | `vllm_ecu/attention/backends/mla_v1.py`、`vllm_ecu/patch/ecu_patch/flash_attn.py` |
| `vllm/model_executor/layers/fused_moe/` | `vllm_ecu/kernels/fused_moe.py`、`vllm_ecu/patch/ecu_patch/fused_moe.py`、`vllm_ecu/patch/ecu_patch/utils.py`（含 `layers/utils.py` 的 `apply_penalties`、`vocab_parallel_embedding`）、量化 MoE 文件 |
| `vllm/model_executor/layers/quantization/` | `vllm_ecu/kernels/quantization/`、`vllm_ecu/patch/ecu_patch/utils.py` |
| `vllm/v1/sample/` | `vllm_ecu/patch/ecu_patch/utils.py`（主要）、`vllm_ecu/patch/ecu_patch/sampler.py` |
| `vllm/v1/spec_decode/` | `vllm_ecu/patch/ecu_patch/utils.py`（eagle step 更新逻辑） |
| `vllm/utils/` | `vllm_ecu/__init__.py`、`vllm_ecu/patch/ecu_patch/utils.py`（`cuda_device_count`、triton kernel 检测） |
| `vllm/distributed/` | `vllm_ecu/distributed/` |
| `vllm/distributed/kv_transfer/` | `vllm_ecu/distributed/kv_transfer/`、`vllm_ecu/distributed/p2p_eccl_*` |
| `vllm/device_allocator/` | `vllm_ecu/worker/__init__.py`、`vllm_ecu/worker/worker_v1.py`、`vllm_ecu/patch/vllm_omni_patch/workers.py` |
| `vllm/engine/arg_utils.py` | `vllm_ecu/patch/ecu_patch/utils.py`、依赖配置字段的 patch |
| `vllm/compilation/`、`vllm/compilation/backends.py` | `vllm_ecu/compilation/`、`vllm_ecu/patch/ecu_patch/compilation_backends.py` |
| `vllm/config/`、`vllm/config*.py` | `vllm_ecu/utils.py`、依赖配置字段的 patch |
| `vllm/entrypoints/` | `vllm_ecu/patch/ecu_patch/entrypoints.py` |
| `vllm/model_executor/custom_op.py`、`_custom_ops.py` | `vllm_ecu/kernels/_custom_ops.py`、custom op 注册逻辑 |
| `vllm/model_executor/models/` | `vllm_ecu/patch/vllm_omni_patch/`、模型专属兼容 patch |

## 搜索 fallback

优先使用 `rg`。如果环境没有 `rg`，使用 `grep/find` fallback：

```bash
if command -v rg >/dev/null 2>&1; then
  rg -n 'patch\("vllm\.' vllm_ecu
  rg -n '^(from|import) vllm\b|^from vllm\.' vllm_ecu
else
  grep -RIn --include='*.py' 'patch("vllm\.' vllm_ecu
  grep -RIn --include='*.py' '^from vllm\.|^import vllm\b' vllm_ecu
fi
```

对具体上游符号，替换占位符后搜索：

```bash
if command -v rg >/dev/null 2>&1; then
  rg -n 'changed_symbol|changed_module' vllm_ecu
else
  grep -RIn --include='*.py' 'changed_symbol\|changed_module' vllm_ecu
fi
```
