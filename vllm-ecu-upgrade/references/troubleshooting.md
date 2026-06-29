# 运行时失败排查

## 排查顺序

| 错误类型 | 优先检查位置 |
|---|---|
| `ImportError`、`ModuleNotFoundError` | 上游路径移动；检查 import 和 patch 目标 |
| vLLM 对象上的 `AttributeError` | 配置字段、方法或类移动/删除 |
| `TypeError` 参数缺失或多余 | 目标 vLLM 函数签名漂移 |
| 抽象类无法实例化 | `vllm_ecu/ecu.py` 缺少新的 `Platform` 方法 |
| 缺少 `torch.ops` 符号 | `vllm_ecu/kernels/_custom_ops.py` 或 fallback 路径 |
| Attention metadata/builder 失败 | `vllm_ecu/attention/`、`flash_attn.py`、worker patch |
| MoE router/kernel 失败 | `vllm_ecu/kernels/fused_moe.py`、`ecu_patch/fused_moe.py` |
| KV transfer/NCCL 路径失败 | `vllm_ecu/distributed/`、`p2p_eccl_*` |
| Compilation pass 失败 | `vllm_ecu/compilation/`、`compilation_backends.py` |

## 失败处理原则

- 先捕获第一个真实 Python 异常，再处理外层包装错误。
- 每次修复后，重新部署 `vllm_ecu` 到容器并重新运行 smoke test。
- 如果某个上游变化检查后无需修改，在升级报告中将 Action 记为 `checked-no-change`，并写明原因。
- 如果验证没有运行，放入“未验证项”；如果尝试运行但被权限、环境、资源或命令失败阻塞，放入“阻塞项”。

## 轻量环境检查

作为 smoke test 前的可选步骤，或 smoke test 失败后的首查项：

```bash
docker exec "$CONTAINER" python3 -c "import torch; print('torch', torch.__version__)"
docker exec "$CONTAINER" env | grep -E 'VLLM|ECU|CUDA|MODEL|HF' || true
```
