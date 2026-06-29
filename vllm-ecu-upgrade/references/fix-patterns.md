# 单版本迁移修复模式

> 本文件提供常见修复模式。每个模式都必须先由上游 diff、目标 API 或 ECU 调用点证明，不要机械套模板。

## 使用原则

- 先确认证据来源：上游 diff、目标 vLLM 源码、`vllm_ecu_couplings.json`、`vllm_ecu_verify_targets.json`、traceback 或 ECU 调用点。
- 修复只面向 `TARGET_PKG_VERSION`。默认删除旧版本分支，不添加 old/new fallback。
- 不用宽泛 `except Exception` 掩盖 API 漂移；只捕获已经证明会发生且可恢复的异常。
- 不用无证据的 `**kwargs` 消除 `TypeError`。只有目标上游本身就是可扩展 metadata 转发接口时才保留。
- 不用 CUDA-only 行为替代 ECU 语义。所有 device、kernel、通信和 fallback 决策必须能解释 ECU 等价性。
- 每个修改都要写入升级报告：上游原因、ECU 文件、处理方式、验证命令和剩余风险。

## 版本门控

如果代码使用 `is_vllm_equal("0.19.0")` 这类旧门控，迁移为单一目标路径。如果目标版本始终需要该 patch，直接导入：

```python
from vllm_ecu.patch import ecu_patch  # noqa
```

或者保留断言式目标门控，用于防止装错 vLLM 版本：

```python
from vllm_ecu.utils import is_vllm_equal

if is_vllm_equal("0.20.0"):
    from vllm_ecu.patch import ecu_patch  # noqa
else:
    raise RuntimeError("vllm-ecu 当前只支持 vLLM 0.20.0")
```

除非用户要求多版本支持，不要添加新旧版本并存的运行时分支。

## import 路径移动

如果上游移动了模块，改成目标版本路径：

```python
from vllm.new.path import Symbol
```

删除旧 import。除非用户要求多版本支持，不要保留 `try old path / fallback new path` 兼容写法。

## 函数签名变化

如果上游签名变化，明确调整 ECU wrapper 和调用点到目标版本签名。如果上游新增可选元数据转发，可以增加带默认值的参数：

```python
def ecu_impl(self, existing, new_param=None):
    ...
```

只有在上游调用路径本身就是可扩展元数据转发时才使用 `**kwargs`。不要用 `**kwargs` 掩盖 ECU 必须处理的必填参数。

## patch 目标移动

修改 `unittest.mock.patch("vllm...")`、`mock.patch("vllm...")` 或 `patch.object(...)` 前，必须验证目标路径在目标 vLLM 版本中存在。替换为目标版本路径，并删除旧 patch 目标。

## 平台接口变化

如果 vLLM 给 `Platform` 增加抽象方法或能力方法，在 `vllm_ecu/ecu.py` 中按 ECU 语义实现。不要返回 CUDA-only 能力，除非 ECU 确实支持该行为。

## Custom Op 变化

如果上游开始调用新的 `torch.ops._C` 或 `torch.ops.vllm` 符号，需要在 `vllm_ecu/kernels/_custom_ops.py` 注册 ECU 等价实现，或强制走 ECU 支持的 fallback 路径。该决策必须记录到升级报告中。

记录至少包含：

- 上游 op 名称和调用路径。
- ECU 是否已有等价 kernel、是否需要新增 wrapper、是否只能 fallback。
- fallback 对性能、精度、dtype、device placement 的影响。
- 已运行的验证命令；如果未运行，写入未验证项。

## 配置与参数字段迁移

当 `vllm/config*.py`、`vllm/config/` 或 `vllm/engine/arg_utils.py` 变化时，重点检查 ECU 是否读取旧字段名、旧嵌套结构或旧默认值。

修复方式：

- 用目标版本配置对象的真实字段替换旧字段。
- 如果字段被拆分，显式映射 ECU 需要的语义，不要简单 `getattr(config, "old", None)` 静默吞掉。
- 如果 CLI 参数或 engine arg 移动，检查 ECU patch 是否仍在正确阶段生效。
- 对 `AttributeError` 修复后，用最小 import/构造检查验证字段路径，必要时再跑 smoke test。

## Sampling 与 Spec Decode 迁移

当 `vllm/v1/sample/` 或 `vllm/v1/spec_decode/` 变化时，重点检查 penalties、top-k/top-p、rejection sampler、eagle slot mapping、batch 更新和 metadata shape。

修复方式：

- 对照目标上游函数签名和 tensor shape 更新 ECU patch。
- 保持 ECU device 和 dtype 语义，不要把采样逻辑迁回 CUDA-only helper。
- 对新增 metadata 字段，明确 ECU 是否消费、透传或构造默认值。
- 对 speculative decoding，特别记录 slot mapping、draft token 数量、batch index 更新方式是否与目标上游一致。

## Attention 与 Forward Context 迁移

当 `vllm/forward_context.py`、`vllm/v1/attention/`、`fa_utils.py` 或 `mla_attention.py` 变化时，重点检查 ECU worker patch、attention backend、builder、metadata、prefill/decode 分支和 flash attention wrapper。

修复方式：

- 先用 `inspect.signature()` 或源码确认目标符号和参数。
- 对 metadata 类字段变化，更新构造点和消费点，而不是只修复报错处。
- 如果上游拆分 attention backend，确认 ECU 注册路径、backend 选择逻辑和 fallback 是否仍生效。
- 对 forward context patch，验证 patch 生效位置与 worker/model runner 调用顺序一致。

## MoE 与量化迁移

当 `vllm/model_executor/layers/fused_moe/` 或 `quantization/` 变化时，重点检查 router、expert map、topk weight、scales、quant method、kernel wrapper 和 custom op。

修复方式：

- 对照目标上游的输入 tensor 顺序、shape、dtype 和返回值。
- 如果上游新增 quant metadata，确认 ECU kernel 是否需要消费；不能消费时记录 fallback 或 blocked。
- 不要只修改 Python wrapper 参数名而忽略底层 custom op ABI。
- 修复后优先跑能覆盖 MoE/quant 路径的最小用例；没有用例时在报告中标为未验证风险。

## Distributed 与 KV Transfer 迁移

当 `vllm/distributed/` 或 `vllm/distributed/kv_transfer/` 变化时，重点检查 NCCL 到 ECCL 替换、group 初始化、rank/world size、KV connector、p2p 传输和环境变量。

修复方式：

- 用目标上游 connector/group API 更新 ECU 分布式封装。
- 保留 ECCL 语义，不要回退到 NCCL-only 路径，除非用户明确只是临时绕过验证。
- 记录容器内通信库、环境变量和是否实际跑过多卡/多进程验证。

## Compilation Backend 迁移

当 `vllm/compilation/` 或 `vllm/compilation/backends.py` 变化时，重点检查 pass manager、backend 注册、graph capture、compile config 和 device backend 选择。

修复方式：

- 将 ECU backend 注册到目标版本实际使用的注册点。
- 如果上游改变 pass 名称或顺序，确认 ECU patch 是删除、替换还是插入 pass。
- 修复后至少做 import/注册检查；无法执行真实 compile 时写入未验证项。

## 参数加载与模型专属 Patch 迁移

当 `vllm/model_executor/parameter/` 或 `vllm/model_executor/models/` 变化时，重点检查参数类、weight loader、模型 forward 签名和 omni/model-specific patch。

修复方式：

- 对照目标模型类和 loader 的签名调整 ECU patch。
- 如果上游模型结构变化影响多模态或 omni 路径，记录受影响模型名。
- 不要为了让 import 通过而删除模型专属 patch；必须确认目标上游是否已经包含等价逻辑。

## 修复后的验证闭环

每轮修复后按改动类型选择验证：

| 改动类型 | 最低验证 |
|---|---|
| import、patch target、base class | 重新运行 `verify_vllm_targets.py` |
| Platform、config、worker、attention、sampling | import/签名检查 + smoke test |
| custom op、MoE、quant | custom op 注册检查 + 覆盖相关路径的运行测试 |
| distributed/KV transfer | 单进程 import 检查 + 可行时多进程/多卡验证 |
| Docker 部署修复 | 重新部署 `vllm_ecu` 并重新运行 smoke test |

如果验证因为环境、模型权重、权限或硬件不可用而未执行，必须写入升级报告的“未验证项”或“阻塞项”，不能在最终摘要中写成已通过。
