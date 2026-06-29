# Docker 升级、部署与验证

> 只有用户要求 Docker 验证、部署、安装 vLLM 或运行 smoke test 时才读取本文件。

## 环境确认

如果容器可能是共享、长期运行或生产/准生产环境，先询问用户是否允许原地修改。如用户不确定，建议复制容器或使用临时验证容器。

确认变量已设置为实际值：

```bash
echo "CONTAINER=$CONTAINER"
echo "ECU_CONTAINER_DIR=$ECU_CONTAINER_DIR"
echo "ECU_REPO=$ECU_REPO"
echo "TARGET_PKG_VERSION=$TARGET_PKG_VERSION"
```

检查容器和当前版本：

```bash
docker ps --filter name="$CONTAINER"
docker exec "$CONTAINER" python3 -c "import vllm; print(vllm.__version__, vllm.__file__)"
docker exec "$CONTAINER" python3 -c "import vllm_ecu; print(vllm_ecu.__file__)"
```

## 安装目标 vLLM

如果 ECU 容器依赖私有 wheel 源、预编译包或本地 checkout，优先使用用户/项目指定的安装方式，不默认强制 PyPI。安装前先询问用户确认安装源和方式。

PyPI 安装示例：

```bash
docker exec "$CONTAINER" python3 -m pip install -U "vllm==$TARGET_PKG_VERSION"
docker exec "$CONTAINER" python3 -c "import vllm; print(vllm.__version__, vllm.__file__)"
```

本地 checkout 安装示例：

```bash
docker exec "$CONTAINER" python3 -m pip uninstall -y vllm
docker exec "$CONTAINER" python3 -m pip install -e /path/to/upstream/vllm
docker exec "$CONTAINER" python3 -c "import vllm; print(vllm.__version__, vllm.__file__)"
```

记录安装前后的 vLLM 版本和路径。

## 校验 ECU 运行时路径

删除容器运行时副本前，在同一个容器 shell 中校验路径。路径通过参数传入，避免宿主机变量在单引号内失效：

```bash
docker exec "$CONTAINER" sh -lc '
target="$1"
if [ -z "$target" ] || [ "$target" = "/" ]; then
  echo "FATAL: unsafe target path: $target" >&2
  exit 1
fi
case "$target" in
  */python*/dist-packages/vllm_ecu|*/python*/site-packages/vllm_ecu) ;;
  *) echo "FATAL: target is not a vllm_ecu package dir under site-packages: $target" >&2; exit 1 ;;
esac
parent=$(dirname "$target")
test -d "$parent" || { echo "FATAL: parent dir missing: $parent" >&2; exit 1; }
echo "OK: $target"
' sh "$ECU_CONTAINER_DIR"
```

## 可选备份

```bash
docker exec "$CONTAINER" sh -lc '
target="$1"
case "$target" in
  */python*/dist-packages/vllm_ecu|*/python*/site-packages/vllm_ecu) ;;
  *) echo "FATAL: unsafe target: $target" >&2; exit 1 ;;
esac
if [ -d "$target" ]; then
  cp -a "$target" "${target}.bak.$(date +%Y%m%d%H%M%S)"
fi
' sh "$ECU_CONTAINER_DIR"
```

## 删除旧运行时副本

不要裸执行 `rm -rf "$ECU_CONTAINER_DIR"`。使用带内联安全检查的命令：

```bash
docker exec "$CONTAINER" sh -lc '
target="$1"
if [ -z "$target" ] || [ "$target" = "/" ]; then
  echo "FATAL: unsafe target path: $target" >&2
  exit 1
fi
case "$target" in
  */python*/dist-packages/vllm_ecu|*/python*/site-packages/vllm_ecu) ;;
  *) echo "FATAL: target is not a vllm_ecu package dir under site-packages: $target" >&2; exit 1 ;;
esac
echo "Removing: $target"
rm -rf "$target"
' sh "$ECU_CONTAINER_DIR"
```

## 部署新包

```bash
docker cp "$ECU_REPO/vllm_ecu" "${CONTAINER}:${ECU_CONTAINER_DIR}"
docker exec "$CONTAINER" python3 -c "import vllm_ecu; print(vllm_ecu.__file__)"
```

只复制可发布的 `vllm_ecu` 包目录。不要把测试、大模型权重、大资源或临时分析文件复制进包。

## 清理字节码缓存

```bash
docker exec "$CONTAINER" sh -lc '
target="$1"
case "$target" in
  */python*/dist-packages/vllm_ecu|*/python*/site-packages/vllm_ecu) ;;
  *) echo "FATAL: unsafe target: $target" >&2; exit 1 ;;
esac
find "$target" -name __pycache__ -type d -prune -exec rm -rf {} +
find "$target" -name "*.pyc" -delete
' sh "$ECU_CONTAINER_DIR"
```

## 运行 smoke test

轻量环境检查：

```bash
docker exec "$CONTAINER" python3 -c "import torch; print('torch', torch.__version__)"
docker exec "$CONTAINER" env | grep -E 'VLLM|ECU|CUDA|MODEL|HF' || true
```

如果宿主机路径已挂载：

```bash
docker exec "$CONTAINER" python3 "$SMOKE_TEST"
```

如果未挂载：

```bash
docker cp "$SMOKE_TEST" "${CONTAINER}:/tmp/vllm_ecu_test.py"
docker exec "$CONTAINER" python3 /tmp/vllm_ecu_test.py
```

失败时捕获第一个真实 Python 异常，并记录失败命令。
