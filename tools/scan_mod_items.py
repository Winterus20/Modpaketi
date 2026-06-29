#!/usr/bin/env python3
"""Mod jar'larından eşya ID'lerini çıkarır; isim çakışmalarını bulur."""
from __future__ import annotations

import json
import re
import zipfile
from collections import defaultdict
from pathlib import Path

INSTANCE = Path(__file__).resolve().parent.parent
MODS = INSTANCE / "mods"

TARGETS = [
    "oceansdelight-1.0.2-1.20.jar",
    "aquaculturedelight-1.1.0-forge-1.20.1.jar",
    "crabbersdelight-1.20.1-1.2.3.jar",
    "FarmersDelight-1.20.1-1.3.2.jar",
    "Croptopia-1.20.1-FORGE-4.0.1.jar",
    "letsdo-farm_and_charm-forge-1.0.14.jar",
    "letsdo-vinery-forge-1.4.41.jar",
    "letsdo-bakery-forge-2.0.6.jar",
    "letsdo-brewery-forge-2.0.6.jar",
    "letsdo-candlelight-forge-2.0.5.jar",
    "letsdo-beachparty-forge-2.0.3.jar",
    "honeys_delight-3.0.0-forge-1.20.1.jar",
    "buzzier_bees-1.20.1-6.0.1.jar",
    "FruitfulFun-1.20.1-Forge-7.8.5.jar",
]


def extract_items(jar_path: Path) -> dict[str, str]:
    """modid:path -> short name"""
    items: dict[str, str] = {}
    with zipfile.ZipFile(jar_path) as zf:
        for name in zf.namelist():
            m = re.match(r"assets/([^/]+)/models/item/(.+)\.json$", name)
            if m:
                modid, path = m.group(1), m.group(2)
                items[f"{modid}:{path}"] = path.replace("/", "_")
    return items


def main() -> None:
    by_name: dict[str, list[str]] = defaultdict(list)
    all_items: dict[str, dict[str, str]] = {}

    for jname in TARGETS:
        jp = MODS / jname
        if not jp.exists():
            print(f"MISSING {jname}")
            continue
        items = extract_items(jp)
        all_items[jname] = items
        for full_id, short in items.items():
            by_name[short].append(full_id)

    print("=== SAME SHORT NAME ACROSS MODS ===")
    for short, ids in sorted(by_name.items()):
        mods = {i.split(":")[0] for i in ids}
        if len(mods) > 1:
            print(f"  {short}: {', '.join(sorted(ids))}")

    for jname, items in all_items.items():
        print(f"\n=== {jname} ({len(items)} items) ===")
        for fid in sorted(items):
            print(f"  {fid}")


if __name__ == "__main__":
    main()
