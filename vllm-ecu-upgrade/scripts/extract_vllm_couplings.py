#!/usr/bin/env python3
"""从 vllm_ecu 源码中提取上游 vLLM 耦合点，输出 JSON。

用法：
  python scripts/extract_vllm_couplings.py [vllm_ecu_dir] > vllm_ecu_couplings.json
"""

from __future__ import annotations

import ast
import json
import sys
from pathlib import Path
from typing import Any


def _node_text(node: ast.AST) -> str:
    """将 AST 节点转换为字符串，Python < 3.9 时回退到 ast.dump。"""
    try:
        return ast.unparse(node)
    except Exception:
        return ast.dump(node, include_attributes=False)


def _is_patch_call(func: ast.AST) -> bool:
    """判断是否是 patch(...)、mock.patch(...) 或 unittest.mock.patch(...) 调用。"""
    if isinstance(func, ast.Name):
        return func.id == "patch"
    if isinstance(func, ast.Attribute):
        text = _node_text(func)
        return text.endswith(".patch") or text == "patch"
    return False


def _is_patch_object_call(func: ast.AST) -> bool:
    """判断是否是 patch.object(...)、mock.patch.object(...) 调用。"""
    if not isinstance(func, ast.Attribute):
        return False
    return _node_text(func).endswith(".patch.object")


def _is_super_call(node: ast.AST) -> bool:
    return (
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "super"
    )


def _string_arg(node: ast.AST) -> str | None:
    """提取字符串常量参数值。"""
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    return None


def _location(py_file: Path, node: ast.AST, root: Path) -> dict[str, Any]:
    try:
        file_name = str(py_file.relative_to(root))
    except ValueError:
        file_name = str(py_file)
    return {"file": file_name, "line": getattr(node, "lineno", None)}


def _dedupe(items: list[dict[str, Any]], keys: tuple[str, ...]) -> list[dict[str, Any]]:
    seen: set[tuple[Any, ...]] = set()
    result: list[dict[str, Any]] = []
    for item in items:
        marker = tuple(item.get(key) for key in keys)
        if marker in seen:
            continue
        seen.add(marker)
        result.append(item)
    return result


def _is_custom_op_expr(text: str) -> bool:
    """判断表达式是否引用 vLLM custom op 相关路径。

    高信号：torch.ops.xxx。
    中信号：属性链中的 _custom_ops/custom_op。避免把 my_custom_op 这类普通名字误判。
    """
    if "torch.ops." in text:
        return True
    return any(
        token in text
        for token in ("._custom_ops", "_custom_ops.", ".custom_op", "custom_op.")
    )


def _is_vllm_base(base_text: str, vllm_local_names: set[str]) -> bool:
    first = base_text.split(".", 1)[0]
    return (
        base_text == "vllm"
        or base_text.startswith("vllm.")
        or first in vllm_local_names
        or base_text in {"Platform", "Worker", "ModelRunner", "AttentionBackend"}
    )


def _collect_vllm_local_names(tree: ast.AST) -> set[str]:
    """收集文件中 vLLM import 引入的本地名字，用于 subclass 检测。"""
    names: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                if alias.name == "vllm" or alias.name.startswith("vllm."):
                    names.add(alias.asname or alias.name.split(".")[0])
        elif isinstance(node, ast.ImportFrom):
            if node.module and (
                node.module == "vllm" or node.module.startswith("vllm.")
            ):
                for alias in node.names:
                    if alias.name != "*":
                        names.add(alias.asname or alias.name)
    return names


def _build_parent_map(tree: ast.AST) -> dict[ast.AST, ast.AST]:
    parents: dict[ast.AST, ast.AST] = {}
    for parent in ast.walk(tree):
        for child in ast.iter_child_nodes(parent):
            parents[child] = parent
    return parents


def _is_leaf_custom_attr(node: ast.Attribute, parents: dict[ast.AST, ast.AST]) -> bool:
    """只记录属性链叶子，避免 torch.ops.vllm.fake_op 同时输出中间链。"""
    parent = parents.get(node)
    if isinstance(parent, ast.Attribute):
        return False
    if isinstance(parent, ast.Call) and parent.func is node:
        return False
    return True


def extract(ecu_dir: str) -> dict[str, Any]:
    root = Path(ecu_dir).resolve()
    if not root.exists():
        raise FileNotFoundError(f"ECU source directory not found: {root}")

    imports: list[dict[str, Any]] = []
    patch_targets: list[dict[str, Any]] = []
    classes: list[dict[str, Any]] = []
    overrides: list[dict[str, Any]] = []
    custom_ops: list[dict[str, Any]] = []
    parse_errors: list[dict[str, Any]] = []

    for py_file in sorted(root.rglob("*.py")):
        if "__pycache__" in py_file.parts:
            continue
        try:
            source = py_file.read_text(encoding="utf-8-sig")
            tree = ast.parse(source, filename=str(py_file))
        except Exception as exc:
            parse_errors.append({"file": str(py_file), "error": repr(exc)})
            continue

        vllm_local_names = _collect_vllm_local_names(tree)
        parents = _build_parent_map(tree)

        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    if alias.name == "vllm" or alias.name.startswith("vllm."):
                        item = _location(py_file, node, root)
                        item.update({
                            "module": alias.name,
                            "name": None,
                            "alias": alias.asname,
                        })
                        imports.append(item)
            elif isinstance(node, ast.ImportFrom):
                if node.module and (
                node.module == "vllm" or node.module.startswith("vllm.")
            ):
                    for alias in node.names:
                        item = _location(py_file, node, root)
                        item.update({
                            "module": node.module,
                            "name": alias.name,
                            "alias": alias.asname,
                        })
                        imports.append(item)
            elif isinstance(node, ast.Call):
                if _is_patch_call(node.func) and node.args:
                    target = _string_arg(node.args[0])
                    if target and (target == "vllm" or target.startswith("vllm.")):
                        item = _location(py_file, node, root)
                        item.update({"target": target, "call": _node_text(node.func)})
                        patch_targets.append(item)
                if _is_patch_object_call(node.func) and len(node.args) >= 2:
                    base = _node_text(node.args[0])
                    attr = _string_arg(node.args[1])
                    if attr and (base == "vllm" or base.startswith("vllm.")):
                        item = _location(py_file, node, root)
                        item.update({
                            "target": f"{base}.{attr}",
                            "call": _node_text(node.func),
                        })
                        patch_targets.append(item)
                if (
                    isinstance(node.func, ast.Attribute)
                    and _is_super_call(node.func.value)
                ):
                    item = _location(py_file, node, root)
                    item.update({
                        "method": node.func.attr,
                        "expr": f"super().{node.func.attr}()",
                    })
                    overrides.append(item)
                func_text = _node_text(node.func)
                if _is_custom_op_expr(func_text):
                    item = _location(py_file, node, root)
                    item.update({"expr": func_text})
                    custom_ops.append(item)
            elif isinstance(node, ast.Attribute):
                text = _node_text(node)
                if _is_leaf_custom_attr(node, parents) and _is_custom_op_expr(text):
                    item = _location(py_file, node, root)
                    item.update({"expr": text})
                    custom_ops.append(item)
            elif isinstance(node, ast.ClassDef):
                bases = [_node_text(base) for base in node.bases]
                upstream_bases = [
                    base for base in bases
                    if _is_vllm_base(base, vllm_local_names)
                ]
                if upstream_bases:
                    item = _location(py_file, node, root)
                    item.update({
                        "class": node.name,
                        "bases": bases,
                        "upstream_bases": upstream_bases,
                    })
                    classes.append(item)

    imports = _dedupe(imports, ("file", "line", "module", "name", "alias"))
    patch_targets = _dedupe(patch_targets, ("file", "line", "target", "call"))
    classes = _dedupe(classes, ("file", "line", "class"))
    overrides = _dedupe(overrides, ("file", "line", "method"))
    custom_ops = _dedupe(custom_ops, ("file", "line", "expr"))

    import_modules = sorted(set(item["module"] for item in imports))
    import_symbols = sorted(set(
        f"{item['module']}.{item['name']}"
        if item["name"] and item["name"] != "*"
        else item["module"]
        for item in imports
    ))
    patch_target_strings = sorted(set(item["target"] for item in patch_targets))

    return {
        "source_root": str(root),
        "import_modules": import_modules,
        "import_symbols": import_symbols,
        "imports": imports,
        "patch_targets": patch_targets,
        "patch_target_strings": patch_target_strings,
        "classes": classes,
        "overrides": overrides,
        "custom_ops": custom_ops,
        "parse_errors": parse_errors,
    }


def main() -> int:
    ecu_dir = sys.argv[1] if len(sys.argv) > 1 else "vllm_ecu"
    result = extract(ecu_dir)
    json.dump(result, sys.stdout, indent=2, ensure_ascii=False)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())




