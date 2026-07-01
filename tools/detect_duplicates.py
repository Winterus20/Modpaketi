#!/usr/bin/env python3
import json
import os
import re
import zipfile
from collections import defaultdict
from pathlib import Path

# Paths
ROOT = Path(__file__).resolve().parent.parent
MODS_DIR = ROOT / "mods"
DEDUP_FILE = ROOT / "tools" / "dedup_mappings.json"

def scan_mod_jars() -> set[str]:
    """Scan all jar files in mods/ to extract valid modded item IDs."""
    valid_items = set()
    if not MODS_DIR.exists():
        print(f"Error: mods directory not found at {MODS_DIR}")
        return valid_items

    for file in MODS_DIR.iterdir():
        if file.suffix == ".jar":
            try:
                with zipfile.ZipFile(file, "r") as zf:
                    for name in zf.namelist():
                        m_item = re.match(r"^assets/([^/]+)/models/item/(.+)\.json$", name)
                        if m_item:
                            modid, path = m_item.group(1), m_item.group(2)
                            valid_items.add(f"{modid}:{path.replace('/', '_')}")
                            valid_items.add(f"{modid}:{path}")
            except Exception:
                pass
    return valid_items

def load_dedup_mappings() -> tuple[set[str], dict[str, str]]:
    """Load existing deduplication pairs."""
    mapped_duplicates = set()
    mappings = {}
    if DEDUP_FILE.exists():
        try:
            with open(DEDUP_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                for pair in data.get("pairs", []):
                    if len(pair) == 2:
                        dup, main = pair[0], pair[1]
                        mapped_duplicates.add(dup)
                        mappings[dup] = main
        except Exception as e:
            print(f"Error loading dedup_mappings.json: {e}")
    return mapped_duplicates, mappings

def main():
    print("Scanning mod jars for all item IDs...")
    all_items = scan_mod_jars()
    print(f"Found {len(all_items)} total modded items.")

    # Group items by their suffix (name of the item without namespace)
    by_suffix = defaultdict(list)
    for item in all_items:
        ns, suffix = item.split(":", 1)
        # Normalize folder paths inside model names if any
        suffix_clean = suffix.replace("/", "_")
        by_suffix[suffix_clean].append(item)

    # Load existing dedup pairings
    mapped_dups, mappings = load_dedup_mappings()
    print(f"Loaded {len(mapped_dups)} deduplicated items from dedup_mappings.json.\n")

    print("=== SUSPECTED UNRESOLVED DUPLICATES ===")
    print("Checking if items with matching names from different mods are mapped...")
    print("-" * 75)

    found_unresolved = 0

    for suffix, items in sorted(by_suffix.items()):
        # Filter duplicates (must exist in more than 1 namespace)
        namespaces = {item.split(":", 1)[0] for item in items}
        if len(namespaces) <= 1:
            continue

        # We have multiple namespaces adding this item suffix!
        # Check which of these are handled by dedup
        unmapped_items = []
        mapped_to = defaultdict(list)
        
        for item in items:
            if item in mapped_dups:
                # This item is marked as a duplicate, pointing to some main item
                target = mappings[item]
                mapped_to[target].append(item)
            elif item in mappings.values():
                # This item is a canonical item that duplicates point to
                pass
            else:
                # This item is completely unmapped!
                unmapped_items.append(item)

        # If there are multiple items that are not mapped, or if we have unmapped items mixed with mapped ones
        # e.g., we have [mod_a:tomato, mod_b:tomato, mod_c:tomato] and only mod_b:tomato is mapped
        if len(unmapped_items) > 0 and (len(unmapped_items) + len(mapped_to) > 1):
            print(f"\nItem Suffix: '{suffix}'")
            print(f"  Available in mods: {', '.join(sorted(namespaces))}")
            print(f"  All IDs found    : {sorted(set(items))}")
            if mapped_to:
                for target, dups in mapped_to.items():
                    print(f"  Already mapped   : {dups} -> {target}")
            print(f"  [UNMAPPED]      : {unmapped_items}")
            found_unresolved += 1

    print("-" * 75)
    if found_unresolved == 0:
        print("Success! All suspected duplicates are correctly mapped in dedup_mappings.json.")
    else:
        print(f"Found {found_unresolved} duplicate groups with unmapped items.")

if __name__ == "__main__":
    main()
