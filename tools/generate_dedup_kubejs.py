#!/usr/bin/env python3
"""dedup_mappings.json → kubejs/startup_scripts/dedup_data.js üretir."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MAPPINGS = Path(__file__).resolve().parent / "dedup_mappings.json"
OUT = ROOT / "kubejs" / "startup_scripts" / "dedup_data.js"


def js_str_list(items: list[str], indent: int = 4) -> str:
    pad = " " * indent
    lines = [f"{pad}'{item}'," for item in items]
    return "\n".join(lines)


def js_pairs(pairs: list[list[str]], indent: int = 4) -> str:
    pad = " " * indent
    lines = [f"{pad}['{a}', '{b}']," for a, b in pairs]
    return "\n".join(lines)


def main() -> None:
    data = json.loads(MAPPINGS.read_text(encoding="utf-8"))
    pairs = data["pairs"]
    sources = [p[0] for p in pairs]
    hidden = sorted(set(sources + data["extra_hidden"]))

    content = f"""// priority: 100
// Otomatik üretim — elle düzenleme: tools/dedup_mappings.json + python tools/generate_dedup_kubejs.py

global.DEDUP_MAPPINGS = [
{js_pairs(pairs)}
]

global.DEDUP_REMOVED_RECIPES = [
{js_str_list(data["removed_recipes"])}
]

global.DEDUP_REMOVED_OUTPUTS = [
{js_str_list(data["removed_outputs"])}
]

global.HIDDEN_ITEMS = [
{js_str_list(hidden)}
]

global.TIDE_FISH_ITEMS = [
{js_str_list(data["tide_fish"])}
]

global.FISH_BAITS = [
{js_str_list(data["fish_baits"])}
]

global.TIDE_ROD_ITEMS = [
{js_str_list(data["tide_rods"])}
]
"""
    OUT.write_text(content, encoding="utf-8")
    print(f"Wrote {OUT} ({len(pairs)} pairs, {len(hidden)} hidden)")


if __name__ == "__main__":
    main()
