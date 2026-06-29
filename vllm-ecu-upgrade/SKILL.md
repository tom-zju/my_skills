---
name: vllm-ecu-upgrade
description: |
  将 vllm-ecu 升级或适配到指定上游 vLLM release/tag。用户要求升级
  vllm-ecu、对比 vllm_ecu 与社区 vLLM API、迁移 ECU patch 到新版本、
  部署到 ECU Docker 容器，或运行 tests/test.py smoke test 时使用。
  默认不创建分支、commit、push 或 PR，除非用户明确要求。
---

# vllm-ecu-upgrade

将 `vllm_ecu` 适配到指定的上游 vLLM release，并在 ECU Docker 运行环境中验证。

## 执行边界

- 优先遵守当前仓库的 `AGENTS.md` 和本地开发指令。
- 宿主机仓库内：优先使用 `.venv/bin/python`（或 Windows `.venv\Scripts\python.exe`），其次按仓库要求使用 `uv run python`。不使用系统 `python3`、裸 `pip` 或 `pip install`。
- Docker 容器命令可以使用容器运行时的 `python3`，前提是 ECU 镜像就是这样配置的。这些命令属于容器运行时操作，不属于宿主机开发环境操作。
- 当命令需要网络访问、修改 Docker 运行时环境、安装或卸载包、拉取远程 tag，或删除运行时文件时，按当前环境要求请求批准。
- 如果容器可能是共享、长期运行或生产/准生产环境，先询问用户是否允许原地修改；用户不确定时，建议使用临时验证容器。
- 如果当前已在用户分支或脏工作树上，继续在当前工作树修改。不要为本 skill 自动创建或切换分支。
- 除非用户明确要求，不执行 `git branch`、创建 commit、push 或创建 PR。
- 不删除或重写宿主机源码目录。容器清理只能针对已经校验过的 ECU 运行时副本。

## 输入与路径发现

### 输入项

从用户请求中提取以下信息：

- `TARGET_TAG`：上游 vLLM tag，例如 `v0.20.0`。
- `TARGET_PKG_VERSION`：pip/package 版本，例如 `0.20.0`。
- 可选 `BASE_TAG`：只用于计算上游 diff 的旧版本基线。
- 可选 `ECU_REPO`：vllm-ecu 仓库根目录。
- 可选 `UPSTREAM_VLLM_REPO`：社区上游 vLLM git checkout。
- 可选 `CONTAINER`：ECU Docker 容器名。
- 可选 `ECU_CONTAINER_DIR`：容器内 ECU 运行时包路径。
- 可选 `SMOKE_TEST`：smoke test 文件路径。

### 版本规范化

将 `0.20.0`、`v0.20.0` 等用户输入规范为：

- `TARGET_TAG=v0.20.0`
- `TARGET_PKG_VERSION=0.20.0`

如果用户没有提供目标 vLLM 版本，先询问目标版本，不要开始改代码。

### 路径解析优先级

按以下顺序解析路径和名称：

1. 用户明确提供的值。
2. 当前 workspace；如果当前目录包含 `vllm_ecu/`，将其作为 ECU repo 候选。若同时存在 `tests/test.py`，作为默认 smoke test。
3. 环境变量，例如 `VLLM_ECU_REPO`、`UPSTREAM_VLLM_REPO`、`ECU_DOCKER_CONTAINER`、`ECU_CONTAINER_DIR`、`ECU_SMOKE_TEST`。
4. 历史默认值（适用于原 ECU Linux 开发环境；其他平台优先使用 workspace 或用户提供路径）：
   - ECU 仓库：`/home/jianping.tan/local-workspace/ecu_code/vllm`
   - ECU 源码：`vllm_ecu/`（相对于仓库根目录）
   - smoke test：`tests/test.py`（相对于仓库根目录）
   - Docker 容器：`tjp_omni_v019`
   - 容器内 ECU 运行时目录：`/usr/local/lib/python3.10/dist-packages/vllm_ecu`

### 变量定义

在运行命令前设置变量。必须替换为实际值；禁止把占位符原样执行：

```bash
# 升级变量（按实际值替换）
TARGET_TAG="v0.20.0"              # 上游 vLLM tag
TARGET_PKG_VERSION="0.20.0"       # pip 包版本
BASE_TAG="v0.19.0"                # 仅用于 diff 的旧基线
CONTAINER="tjp_omni_v019"         # ECU Docker 容器名
ECU_REPO="/home/jianping.tan/local-workspace/ecu_code/vllm"
UPSTREAM_VLLM_REPO="/path/to/upstream/vllm"
ECU_CONTAINER_DIR="/usr/local/lib/python3.10/dist-packages/vllm_ecu"
SMOKE_TEST="$ECU_REPO/tests/test.py"
# PYTHON_BIN 必须指向目标 vLLM 环境；优先 .venv/bin/python，Windows 用 .venv\Scripts\python.exe，容器内可用 python3
PYTHON_BIN=".venv/bin/python"
```

如果必需路径无法找到，停止并要求用户提供缺失路径。不要猜测 release 或仓库位置。

可能存在以下历史参考流程：

- `/home/jianping.tan/local-workspace/ecu_code/vllm/main2main`
- `/home/jianping.tan/local-workspace/ecu_code/vllm/ecu2community`

只有在这些路径存在且确实相关时才读取。`ecu2community` 只作为历史背景，不能覆盖本 skill 的单目标版本策略。

## Shell 选择

- 容器内命令默认使用 Linux shell：`docker exec "$CONTAINER" sh -lc '...'`。
- 宿主机 Linux/WSL 使用 bash 示例命令。
- 宿主机 Windows PowerShell 中，`sed -n '1,160p' file` 改用 `Get-Content file | Select-Object -First 160`；bash heredoc 改为临时 `.py` 脚本或 `python -c`。
- 如果宿主机是 Windows 但可通过 WSL 访问仓库，优先使用 WSL 路径和 bash 命令。

## 核心原则

- 将用户指定的 vLLM 版本视为升级后唯一支持的目标版本。
- 业务代码修改集中在 `vllm_ecu/`。只有依赖、包声明、测试入口或验证脚本确实需要变化时，才修改 `setup.py`、`pyproject.toml`、requirements 文件或 `tests/test.py`。
- 保留 ECU 专属语义。不能因为上游 vLLM 改了 CUDA 代码，就用 CUDA-only 行为替换 ECU 行为。
- 清理或迁移旧版本 import、patch 目标、签名适配和版本门控。除非用户明确改变要求，不保留同时支持 `BASE_TAG` 和 `TARGET_TAG` 的运行时分支。
- 修改代码前，先理解上游 API 变化和 ECU 调用点。不要只根据错误字符串盲改。
- 每次为了修复运行时失败而改代码后，都要重新部署 `vllm_ecu` 到容器并重新运行 smoke test。

## 停止条件

遇到以下任意情况时停止，向用户说明原因后再继续：

| 条件 | 说明 |
|---|---|
| 用户未提供目标版本 | 必须先询问 `TARGET_TAG` |
| 找不到 ECU repo | `vllm_ecu/` 不存在，要求用户提供 `ECU_REPO` |
| 找不到上游 vLLM repo | 要求用户提供 `UPSTREAM_VLLM_REPO` |
| `TARGET_TAG` 不存在且无法 fetch | 要求用户确认版本 |
| Docker 容器不存在且用户要求容器验证 | 要求用户确认容器名或跳过容器步骤 |
| 需要修改共享/生产容器但未获用户批准 | 要求用户明确批准 |
| `ECU_CONTAINER_DIR` 为空、为 `/` 或不在 `site-packages`/`dist-packages` 下 | 拒绝执行删除，要求用户确认路径 |

## 工作流

### 1. 建立升级前基线

在 ECU 仓库根目录记录基线。搜索命令优先使用 `rg`，不可用时回退到 `find`/`grep`：

```bash
pwd
git status --short
git rev-parse --show-toplevel
git rev-parse HEAD
rg --files vllm_ecu 2>/dev/null || find vllm_ecu -type f -name "*.py" | sort
```

宿主机 vLLM 版本检查按运行时优先级执行；如果宿主机没有安装 vLLM，不要停止，改在容器或上游 checkout 环境中检查：

```bash
if [ -f .venv/bin/python ]; then
  .venv/bin/python -c "import vllm; print(vllm.__version__, vllm.__file__)"
elif command -v uv >/dev/null 2>&1; then
  uv run python -c "import vllm; print(vllm.__version__, vllm.__file__)"
else
  echo "WARNING: 未找到宿主机 Python 运行时，将在容器内检查"
fi
```

读取存在的关键文件，并精确搜索版本门控：

```bash
for f in vllm_ecu/patch/__init__.py vllm_ecu/utils.py vllm_ecu/ecu.py \
         setup.py pyproject.toml tests/test.py; do
  [ -f "$f" ] && echo "=== $f ===" && head -200 "$f" && echo "--- END ---" || echo "SKIP: $f not found"
done
grep -n "is_vllm_equal\|__version__\|vllm\.__version__" \
  vllm_ecu/patch/__init__.py vllm_ecu/utils.py 2>/dev/null || true
```

按以下顺序推断 `BASE_TAG`：用户提供值、`vllm_ecu/patch/__init__.py` 的 `is_vllm_equal(...)` 门控、目标容器当前 vLLM 版本、依赖元数据或项目文档。如果仍无法确定：需要完整上游 diff 报告时询问用户；只修复当前运行时错误时可跳过 diff，并在报告中标注“未生成完整上游 diff（无 BASE_TAG）”。

已知历史模式：`vllm_ecu/patch/__init__.py` 可能通过 `is_vllm_equal("0.19.0")` 控制 patch 启用。升级到 `0.20.0` 时应迁移为目标版本逻辑。不要保留 `0.19.0` 运行时分支。

### 2. 准备上游 vLLM checkout

定位本地社区上游 vLLM git 仓库。找不到时要求用户提供 `UPSTREAM_VLLM_REPO`，或请求权限获取源码。在上游仓库验证：

```bash
git rev-parse "$TARGET_TAG"
git rev-parse "$BASE_TAG"
git log -1 --format="%H %s" "$TARGET_TAG"
```

如果本地缺少 tag，按需请求批准后运行 `git fetch --tags`。如果 tag 仍不存在，停止并要求用户确认版本。

### 3. 提取 ECU 与上游耦合点

运行 `scripts/extract_vllm_couplings.py` 从当前 `vllm_ecu` 源码提取 import、patch target、custom op 和 subclass 线索，输出 JSON。不要手工维护固定 import 检查列表。

```bash
"$PYTHON_BIN" scripts/extract_vllm_couplings.py "$ECU_REPO/vllm_ecu" > vllm_ecu_couplings.json
```

脚本只是降低漏扫风险；仍要结合真实源码阅读判断 ECU 语义。

脚本不可用时，使用手动 fallback：

```bash
grep -RIn --include="*.py" 'patch("vllm\.' vllm_ecu
grep -RIn --include="*.py" 'mock.patch("vllm\.' vllm_ecu
grep -RIn --include="*.py" '^from vllm\.\|^import vllm\b' vllm_ecu
grep -RIn --include="*.py" 'torch\.ops\.\|_custom_ops\|custom_op' vllm_ecu
```

### 4. 生成上游变更清单

如果有 `BASE_TAG`，对比 `BASE_TAG..TARGET_TAG`：

```bash
git diff --find-renames --name-status "$BASE_TAG..$TARGET_TAG" -- vllm
git diff --stat "$BASE_TAG..$TARGET_TAG" -- vllm
git log --oneline "$BASE_TAG..$TARGET_TAG" -- vllm
```

如果没有 `BASE_TAG`，跳过 diff，并在报告中标注“未生成完整上游 diff（无 BASE_TAG）”。

只检查与 ECU 耦合点或热点 reference 相交的上游变更文件。不要把整个上游仓库塞入上下文。升级过程中持续维护 ECU 仓库根目录下的 `vllm_ecu_upgrade_report.md`。

### 5. 分析上游热点

读取 `references/api-hotspots.md`。热点表是启发式优先级，不是完整清单；真实检查范围必须来自当前 `vllm_ecu` 耦合点扫描和上游 diff 的并集。

### 6. 映射到 ECU 文件

读取 `references/ecu-path-mapping.md`。对每个高优先级上游变化，在 ECU 目录中搜索相关符号；优先使用 `rg`，不可用时使用 reference 中的 `grep/find` fallback。

### 7. 运行静态兼容性检查

用目标 vLLM 环境运行 `scripts/verify_vllm_targets.py` 验证耦合 JSON 中的 import module 和 patch target 是否仍存在：

```bash
"$PYTHON_BIN" scripts/verify_vllm_targets.py vllm_ecu_couplings.json > vllm_ecu_verify_targets.json
```

对 ECU 会 subclass、override 或 patch 的函数/类，用 `inspect.signature()` 检查目标版本签名。必要时在容器内运行等价检查。

脚本不可用时，在目标 vLLM 环境中手动验证；`targets` 必须来自步骤 3 的耦合点扫描结果，不要硬编码固定列表。

### 8. 应用单版本迁移修复

读取 `references/fix-patterns.md`。修改前必须已经定位到至少一个证据来源：上游 diff、`vllm_ecu_couplings.json`、`vllm_ecu_verify_targets.json`、目标 vLLM 源码、运行时 traceback 或 ECU 调用点。没有证据时先回到前序步骤补充分析；不要机械套模板。

目标是让当前代码只面向 `TARGET_PKG_VERSION` 工作，而不是同时兼容 `BASE_TAG` 和 `TARGET_TAG`。默认删除旧版本分支和旧 patch 目标；不要添加 old/new fallback import、宽泛 `except Exception`、无证据的 `**kwargs` 或 CUDA-only 替代实现，除非用户明确要求多版本兼容并接受风险。

优先根据 `vllm_ecu_verify_targets.json` 的失败类型选择修复模式：`import_module/import_symbol` 对应 import 路径或 symbol 迁移，`patch_target` 对应 patch 目标迁移，`base_class/platform_signatures` 对应继承关系和平台接口变化，`custom_ops_not_verified` 对应 custom op 人工验证。

修复模式概要：版本门控迁移、import 路径移动、函数签名变化、patch 目标移动、平台接口变化、custom op 变化。除此之外，还要按热点处理配置字段迁移、sampling/spec decode、distributed/KV transfer、compilation backend、模型参数加载等专项变化；这些专项变化必须回到 `references/api-hotspots.md` 和 `references/ecu-path-mapping.md` 找对应 ECU 文件。

每次修改后，更新 `vllm_ecu_upgrade_report.md` 的 ECU 修改文件和验证结果。若修改 import、patch target、base class 或 custom op，重新运行相关静态验证；若修改是为了修复容器运行时失败，必须重新部署并重新运行 smoke test。custom op 决策必须记录上游 op 名称、ECU 等价实现或 fallback 选择、未覆盖风险和验证结果。

### 9. 维护升级报告

持续更新 `vllm_ecu_upgrade_report.md`。报告至少包含：概览、升级前基线、上游接口变化、ECU 修改文件、验证结果、未验证项、阻塞项和剩余风险。`Action` 列使用 `modified`、`checked-no-change`、`not-applicable` 或 `blocked`，并写明原因。

### 10. 检查修改 diff

修改后检查：

```bash
git diff -- vllm_ecu
git diff --stat -- vllm_ecu
for f in setup.py pyproject.toml requirements.txt tests/test.py; do
  [ -f "$f" ] && git diff -- "$f"
done
```

如果 `git diff` 因本地 git-lfs 问题失败，说明阻塞原因，并通过直接读取文件和升级报告总结每个改动文件。

### 11. 在 Docker 中升级 vLLM

只有用户要求容器验证或部署时才读取 `references/docker-deploy.md`。如果 ECU 容器依赖私有 wheel 源、预编译包或本地 checkout，优先使用用户/项目指定的安装方式，不默认强制 PyPI。记录升级前后的 vLLM 版本和路径。

### 12. 部署 vllm_ecu 到 Docker

读取 `references/docker-deploy.md`。所有删除容器文件的命令都必须在同一个 `sh -lc` 块内完成路径安全检查和删除，并通过参数传入 `ECU_CONTAINER_DIR`。不要裸执行 `rm -rf "$ECU_CONTAINER_DIR"`。

部署时使用安全变量边界：

```bash
docker cp "$ECU_REPO/vllm_ecu" "${CONTAINER}:${ECU_CONTAINER_DIR}"
```

### 13. 运行 smoke test

运行前可做轻量环境检查：`torch` 版本、`VLLM|ECU|CUDA|MODEL|HF` 相关环境变量。若宿主机路径已挂载到容器，直接运行 `SMOKE_TEST`；否则用安全变量边界复制到 `/tmp/vllm_ecu_test.py` 后运行：

```bash
docker cp "$SMOKE_TEST" "${CONTAINER}:/tmp/vllm_ecu_test.py"
docker exec "$CONTAINER" python3 /tmp/vllm_ecu_test.py
```

失败时捕获第一个真实 Python 异常。

### 14. 排查运行时失败

读取 `references/troubleshooting.md`。每次修复后，重新部署并重新运行 smoke test。

## 最终回复格式

以简洁结构化摘要结束：

```markdown
### vllm-ecu 升级摘要

**目标 vLLM：** `TARGET_TAG`
**diff 基线：** `BASE_TAG` 或 未生成完整上游 diff
**支持策略：** 仅支持目标 vLLM
**容器：** `CONTAINER`

#### 修改文件
| 文件 | 修改内容 | 上游原因 |
|---|---|---|

#### 已处理的接口差异
| vLLM API/路径 | ECU 文件 | 处理方式 |
|---|---|---|

#### 关键命令与结果
| 命令 | 结果 | 备注 |
|---|---|---|

#### 验证结果
| 步骤 | 结果 |
|---|---|
| 容器 vLLM 版本 | ... |
| 部署后的 `vllm_ecu` 路径 | ... |
| `tests/test.py` | pass/fail |

#### 未验证项
| 项目 | 原因 | 后续动作 |
|---|---|---|

#### 阻塞项
| 项目 | 失败命令/原因 | 需要用户提供什么 |
|---|---|---|

#### 剩余风险
- ...
```

如果无法运行验证，必须说明明确阻塞点和失败命令。



