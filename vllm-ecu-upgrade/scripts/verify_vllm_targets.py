#!/usr/bin/env python3
"""在目标 vLLM 环境中验证模块、patch 目标和关键签名是否存在。

用法：
  python scripts/verify_vllm_targets.py vllm_ecu_couplings.json
"""

from __future__ import annotations

import importlib
import inspect
import json
import sys
from typing import Any


def _resolve_target(target: str) -> tuple[Any, str, list[str]]:
    """Resolve a dotted module/symbol path using the longest importable prefix."""
    parts = target.split(".")
    last_error: Exception | None = None
    for i in range(len(parts), 0, -1):
        module_name = ".".join(parts[:i])
        attrs = parts[i:]
        try:
            obj: Any = importlib.import_module(module_name)
        except Exception as exc:
            last_error = exc
            continue
        for attr in attrs:
            obj = getattr(obj, attr)
        return obj, module_name, attrs
    raise ImportError(f"Cannot resolve {target}: {last_error!r}")


def _append_ok(results: dict[str, Any], item: dict[str, Any]) -> None:
    results["ok"].append(item)


def _append_fail(results: dict[str, Any], item: dict[str, Any]) -> None:
    results["fail"].append(item)


def _append_warn(results: dict[str, Any], item: dict[str, Any]) -> None:
    results["warn"].append(item)


def _record_import_symbol(
    mapping: dict[str, str], module: str, name: str | None, alias: str | None
) -> None:
    """Record local imported names and aliases for one import statement."""
    if name and name != "*":
        fq_name = f"{module}.{name}"
        mapping[name] = fq_name
        if alias:
            mapping[alias] = fq_name
    elif alias:
        mapping[alias] = module
    else:
        mapping[module.split(".", 1)[0]] = module


def _import_symbol_maps(
    data: dict[str, Any],
) -> tuple[dict[str, str], dict[str, dict[str, str]]]:
    """Map imported names globally and per file.

    Base classes are resolved using the importing file first. This avoids a class
    in one ECU file being resolved through an unrelated same-name import in
    another file.
    """
    global_mapping: dict[str, str] = {}
    by_file: dict[str, dict[str, str]] = {}
    for item in data.get("imports", []):
        module = item.get("module")
        name = item.get("name")
        alias = item.get("alias")
        file_name = item.get("file")
        if not module:
            continue
        _record_import_symbol(global_mapping, module, name, alias)
        if file_name:
            file_mapping = by_file.setdefault(str(file_name), {})
            _record_import_symbol(file_mapping, module, name, alias)
    return global_mapping, by_file


def _iter_import_modules(data: dict[str, Any]) -> list[str]:
    modules = set(data.get("import_modules") or [])
    for item in data.get("imports", []):
        module = item.get("module")
        if module:
            modules.add(module)
    return sorted(modules)


def _iter_patch_targets(data: dict[str, Any]) -> list[str]:
    targets: set[str] = set(data.get("patch_target_strings") or [])
    for item in data.get("patch_targets", []):
        if isinstance(item, dict):
            target = item.get("target")
        else:
            target = item
        if target:
            targets.add(target)
    return sorted(targets)


def _verify_import_modules(data: dict[str, Any], results: dict[str, Any]) -> None:
    for module in _iter_import_modules(data):
        try:
            mod = importlib.import_module(module)
            _append_ok(results, {
                "kind": "import_module",
                "module": module,
                "file": getattr(mod, "__file__", None),
            })
        except Exception as exc:
            _append_fail(results, {
                "kind": "import_module",
                "module": module,
                "error": repr(exc),
            })


def _verify_import_symbols(data: dict[str, Any], results: dict[str, Any]) -> None:
    symbols = set(data.get("import_symbols") or [])
    for item in data.get("imports", []):
        module = item.get("module")
        name = item.get("name")
        if module and name and name != "*":
            symbols.add(f"{module}.{name}")
    for symbol in sorted(symbols):
        try:
            obj, module_name, attrs = _resolve_target(symbol)
            _append_ok(results, {
                "kind": "import_symbol",
                "symbol": symbol,
                "module": module_name,
                "attrs": attrs,
                "type": type(obj).__name__,
            })
        except Exception as exc:
            _append_fail(results, {
                "kind": "import_symbol",
                "symbol": symbol,
                "error": repr(exc),
            })


def _verify_patch_targets(data: dict[str, Any], results: dict[str, Any]) -> None:
    for target in _iter_patch_targets(data):
        try:
            obj, module_name, attrs = _resolve_target(target)
            _append_ok(results, {
                "kind": "patch_target",
                "target": target,
                "module": module_name,
                "attrs": attrs,
                "type": type(obj).__name__,
            })
        except Exception as exc:
            _append_fail(results, {
                "kind": "patch_target",
                "target": target,
                "error": repr(exc),
            })


def _verify_base_classes(data: dict[str, Any], results: dict[str, Any]) -> None:
    global_symbol_map, file_symbol_maps = _import_symbol_maps(data)
    seen: set[tuple[str, str, str]] = set()
    for cls_info in data.get("classes", []):
        ecu_class = cls_info.get("class")
        file_name = cls_info.get("file")
        file_symbol_map = file_symbol_maps.get(str(file_name), {})
        for base in cls_info.get("upstream_bases", []):
            target = file_symbol_map.get(base, global_symbol_map.get(base, base))
            marker = (str(file_name), str(ecu_class), str(target))
            if marker in seen:
                continue
            seen.add(marker)
            if "." not in target:
                _append_warn(results, {
                    "kind": "base_class",
                    "base": base,
                    "resolved": target,
                    "ecu_class": ecu_class,
                    "file": file_name,
                    "message": (
                        "Base class is unqualified and cannot be resolved "
                        "without import context"
                    ),
                })
                continue
            try:
                obj, module_name, attrs = _resolve_target(target)
                _append_ok(results, {
                    "kind": "base_class",
                    "base": base,
                    "resolved": target,
                    "ecu_class": ecu_class,
                    "file": file_name,
                    "module": module_name,
                    "attrs": attrs,
                    "type": type(obj).__name__,
                })
            except Exception as exc:
                _append_fail(results, {
                    "kind": "base_class",
                    "base": base,
                    "resolved": target,
                    "ecu_class": ecu_class,
                    "file": file_name,
                    "error": repr(exc),
                })


def _inspect_platform(results: dict[str, Any]) -> None:
    try:
        from vllm.platforms.interface import Platform
    except Exception as exc:
        _append_warn(results, {
            "kind": "platform_missing",
            "message": "vllm.platforms.interface.Platform not found",
            "error": repr(exc),
        })
        return

    signatures: dict[str, str] = {}
    abstract_methods: list[str] = []
    for name, member in inspect.getmembers(Platform):
        if not (inspect.isfunction(member) or inspect.ismethod(member)):
            continue
        try:
            signatures[name] = str(inspect.signature(member))
        except Exception:
            signatures[name] = "<unable to inspect>"
        if getattr(member, "__isabstractmethod__", False):
            abstract_methods.append(name)

    results["platform_signatures"] = signatures
    if abstract_methods:
        _append_warn(results, {
            "kind": "abstract_methods",
            "message": "Platform has abstract methods ECU may need to implement",
            "methods": sorted(abstract_methods),
        })


def verify(couplings_json: str) -> dict[str, Any]:
    with open(couplings_json, encoding="utf-8-sig") as handle:
        data = json.load(handle)

    results: dict[str, Any] = {"ok": [], "fail": [], "warn": []}

    if data.get("parse_errors"):
        _append_warn(results, {
            "kind": "parse_errors",
            "message": (
                f"{len(data['parse_errors'])} files failed to parse "
                "in extract step"
            ),
            "files": data["parse_errors"],
        })

    _verify_import_modules(data, results)
    _verify_import_symbols(data, results)
    _verify_patch_targets(data, results)
    _verify_base_classes(data, results)
    _inspect_platform(results)

    if data.get("custom_ops"):
        _append_warn(results, {
            "kind": "custom_ops_not_verified",
            "message": (
                "custom_ops are reported for manual review; "
                "this script does not execute torch ops"
            ),
            "count": len(data["custom_ops"]),
        })

    results["summary"] = {
        "total_ok": len(results["ok"]),
        "total_fail": len(results["fail"]),
        "total_warn": len(results["warn"]),
    }
    return results


def main() -> int:
    if len(sys.argv) < 2:
        print(
            "Usage: python verify_vllm_targets.py vllm_ecu_couplings.json",
            file=sys.stderr,
        )
        return 1
    result = verify(sys.argv[1])
    json.dump(result, sys.stdout, indent=2, ensure_ascii=False)
    sys.stdout.write("\n")
    return 1 if result["fail"] else 0


if __name__ == "__main__":
    raise SystemExit(main())



