#!/usr/bin/env python3
import os
import re
import zipfile
import difflib
from pathlib import Path

# Paths
ROOT = Path(__file__).resolve().parent.parent
MODS_DIR = ROOT / "mods"
KUBEJS_DIR = ROOT / "kubejs"
CHAPTERS_DIR = ROOT / "tools" / "chapters"

# Common Vanilla Items Cache (Minecraft 1.20.1)
VANILLA_ITEMS = {
    "air", "stone", "grass_block", "dirt", "cobblestone", "water", "lava", "sand", "gravel", "gold_ore", "iron_ore",
    "coal_ore", "nether_gold_ore", "oak_log", "spruce_log", "birch_log", "jungle_log", "acacia_log", "dark_oak_log",
    "mangrove_log", "cherry_log", "crimson_stem", "warped_stem", "oak_planks", "spruce_planks", "birch_planks",
    "jungle_planks", "acacia_planks", "dark_oak_planks", "mangrove_planks", "cherry_planks", "crimson_planks",
    "warped_planks", "glass", "lapis_ore", "lapis_block", "sandstone", "white_wool", "gold_block", "iron_block",
    "brick", "bookshelf", "mossy_cobblestone", "obsidian", "torch", "oak_stairs", "chest", "diamond_ore",
    "diamond_block", "crafting_table", "wheat", "farmland", "furnace", "ladder", "cobblestone_stairs", "lever",
    "stone_pressure_plate", "redstone_ore", "redstone_torch", "stone_button", "snow", "ice", "clay", "sugar_cane",
    "soul_sand", "glowstone", "pumpkin", "netherrack", "soul_soil", "basalt", "polished_basalt", "smooth_basalt",
    "stone_brick_stairs", "mycelium", "nether_brick_stairs", "nether_wart", "enchanting_table", "brewing_stand",
    "cauldron", "end_stone", "emerald_ore", "emerald_block", "beacon", "redstone_block", "hopper", "dropper",
    "slime_block", "barrier", "iron_trapdoor", "prismarine", "sea_lantern", "coarse_dirt", "podzol", "wet_sponge",
    "sponge", "red_sandstone", "spruce_stairs", "birch_stairs", "jungle_stairs", "acacia_stairs", "dark_oak_stairs",
    "mangrove_stairs", "cherry_stairs", "crimson_stairs", "warped_stairs", "hay_block", "white_carpet", "coal_block",
    "packed_ice", "blue_ice", "sea_pickle", "turtle_egg", "bamboo", "scaffolding", "honeycomb_block", "honey_block",
    "lodestone", "respawn_anchor", "crying_obsidian", "blackstone", "gilded_blackstone", "chiseled_polished_blackstone",
    "polished_blackstone_bricks", "deepslate", "cobbled_deepslate", "raw_iron_block", "raw_copper_block",
    "raw_gold_block", "amethyst_cluster", "large_amethyst_bud", "medium_amethyst_bud", "small_amethyst_bud",
    "tuff", "calcite", "tinted_glass", "copper_ore", "deepslate_copper_ore", "copper_block", "exposed_copper",
    "weathered_copper", "oxidized_copper", "cut_copper", "exposed_cut_copper", "weathered_cut_copper",
    "oxidized_cut_copper", "cut_copper_stairs", "lightning_rod", "pointed_dripstone", "dripstone_block", "cave_vines",
    "glow_lichen", "moss_block", "moss_carpet", "sculk", "sculk_vein", "sculk_catalyst", "sculk_shrieker",
    "sculk_sensor", "mud", "packed_mud", "mud_bricks", "mangrove_roots", "muddy_mangrove_roots", "cherry_leaves",
    "pink_petals", "suspicious_sand", "suspicious_gravel", "sniffer_egg", "calibrated_sculk_sensor", "pitcher_crop",
    "pitcher_pod", "torchflower_seeds", "torchflower", "iron_shovel", "iron_pickaxe", "iron_axe", "flint_and_steel",
    "apple", "bow", "arrow", "coal", "charcoal", "diamond", "iron_ingot", "gold_ingot", "iron_sword", "wooden_sword",
    "wooden_shovel", "wooden_pickaxe", "wooden_axe", "stone_sword", "stone_shovel", "stone_pickaxe", "stone_axe",
    "diamond_sword", "diamond_shovel", "diamond_pickaxe", "diamond_axe", "stick", "bowl", "soup", "golden_sword",
    "golden_shovel", "golden_pickaxe", "golden_axe", "string", "feather", "gunpowder", "wooden_hoe", "stone_hoe",
    "iron_hoe", "diamond_hoe", "golden_hoe", "wheat_seeds", "bread", "leather_helmet", "leather_chestplate",
    "leather_leggings", "leather_boots", "chainmail_helmet", "chainmail_chestplate", "chainmail_leggings",
    "chainmail_boots", "iron_helmet", "iron_chestplate", "iron_leggings", "iron_boots", "diamond_helmet",
    "diamond_chestplate", "diamond_leggings", "diamond_boots", "golden_helmet", "golden_chestplate", "golden_leggings",
    "golden_boots", "flint", "porkchop", "cooked_porkchop", "painting", "golden_apple", "enchanted_golden_apple",
    "oak_sign", "spruce_sign", "birch_sign", "jungle_sign", "acacia_sign", "dark_oak_sign", "mangrove_sign",
    "cherry_sign", "crimson_sign", "warped_sign", "bucket", "water_bucket", "lava_bucket", "powder_snow_bucket",
    "minecart", "saddle", "iron_door", "redstone", "snowball", "oak_boat", "spruce_boat", "birch_boat", "jungle_boat",
    "acacia_boat", "dark_oak_boat", "mangrove_boat", "cherry_boat", "leather", "milk_bucket", "clay_ball", "paper",
    "book", "slime_ball", "chest_minecart", "furnace_minecart", "egg", "compass", "recovery_compass", "fishing_rod",
    "clock", "glowstone_dust", "cod", "salmon", "tropical_fish", "pufferfish", "cooked_cod", "cooked_salmon", "ink_sac",
    "glow_ink_sac", "cocoa_beans", "white_dye", "orange_dye", "magenta_dye", "light_blue_dye", "yellow_dye", "lime_dye",
    "pink_dye", "gray_dye", "light_gray_dye", "cyan_dye", "purple_dye", "blue_dye", "brown_dye", "green_dye", "red_dye",
    "black_dye", "bone", "bone_meal", "sugar", "cake", "bed", "repeater", "cookie", "shears", "melon_slice",
    "pumpkin_seeds", "melon_seeds", "beef", "cooked_beef", "chicken", "cooked_chicken", "rotten_flesh", "ender_pearl",
    "blaze_rod", "ghast_tear", "gold_nugget", "potion", "glass_bottle", "spider_eye", "fermented_spider_eye",
    "blaze_powder", "magma_cream", "eye_of_ender", "glistering_melon_slice", "experience_bottle", "fire_charge",
    "writable_book", "written_book", "emerald", "item_frame", "glow_item_frame", "flower_pot", "carrot", "potato",
    "baked_potato", "poisonous_potato", "map", "golden_carrot", "skeleton_skull", "wither_skeleton_skull",
    "zombie_head", "player_head", "creeper_head", "dragon_head", "piglin_head", "carrot_on_a_stick",
    "warped_fungus_on_a_stick", "nether_star", "pumpkin_pie", "firework_rocket", "firework_star", "enchanted_book",
    "nether_brick", "prismarine_shards", "prismarine_crystals", "rabbit", "cooked_rabbit", "rabbit_stew", "rabbit_foot",
    "rabbit_hide", "armor_stand", "iron_horse_armor", "golden_horse_armor", "diamond_horse_armor", "leather_horse_armor",
    "lead", "name_tag", "mutton", "cooked_mutton", "end_crystal", "chorus_fruit", "popped_chorus_fruit", "beetroot",
    "beetroot_seeds", "beetroot_soup", "dragon_breath", "splash_potion", "spectral_arrow", "tipped_arrow",
    "lingering_potion", "shield", "elytra", "spruce_boat_with_chest", "birch_boat_with_chest", "jungle_boat_with_chest",
    "acacia_boat_with_chest", "dark_oak_boat_with_chest", "mangrove_boat_with_chest", "cherry_boat_with_chest",
    "totem_of_undying", "shulker_shell", "iron_nugget", "trident", "phantom_membrane", "nautilus_shell",
    "heart_of_the_sea", "crossbow", "sweet_berries", "glow_berries", "honeycomb", "honey_bottle", "netherite_scrap",
    "netherite_ingot", "netherite_sword", "netherite_shovel", "netherite_pickaxe", "netherite_axe", "netherite_hoe",
    "netherite_helmet", "netherite_chestplate", "netherite_leggings", "netherite_boots", "disc_fragment_5",
    "goat_horn", "brush", "smithing_template_netherite_upgrade"
}

# Add standard tags/fluids to vanilla whitelist to reduce false positives
VANILLA_ITEMS.update({
    "water", "lava", "milk", "honey", "copper_ingot", "stone_bricks", "beehive",
    "andesite", "soul_lantern", "lantern"
})

# Whitelist of known recipe types, tags, or non-item IDs
KNOWN_TAGS_AND_TYPES = {
    "farmersdelight:cutting", "farmersdelight:cooking",
    "sereneseasons:spring_crops", "sereneseasons:summer_crops", "sereneseasons:autumn_crops", "sereneseasons:winter_crops",
    "tide:fish", "tide:cookable_fish", "tide:fishing_rods", "tide:lava_fishing_rods",
    "fishermens_trap:fish_baits"
}

# Namespaces that are entirely recipe or tag mappings (not modded items)
IGNORED_NAMESPACES = {
    "harborhaven", "forge", "tfc"
}

def scan_mod_jars() -> tuple[set[str], set[str]]:
    """Scan all jar files in mods/ to extract mod namespaces and valid item IDs."""
    valid_items = set()
    namespaces = {"minecraft"}
    
    if not MODS_DIR.exists():
        print(f"Error: mods directory not found at {MODS_DIR}")
        return valid_items, namespaces

    for file in MODS_DIR.iterdir():
        if file.suffix == ".jar":
            try:
                with zipfile.ZipFile(file, "r") as zf:
                    for name in zf.namelist():
                        # Extract namespaces from assets/ or data/
                        m_ns = re.match(r"^(assets|data)/([^/]+)/", name)
                        if m_ns:
                            namespaces.add(m_ns.group(2))
                            
                        # Extract item model paths
                        # assets/<namespace>/models/item/<path>.json
                        m_item = re.match(r"^assets/([^/]+)/models/item/(.+)\.json$", name)
                        if m_item:
                            modid, path = m_item.group(1), m_item.group(2)
                            valid_items.add(f"{modid}:{path.replace('/', '_')}")
                            valid_items.add(f"{modid}:{path}")
                            
                        # Extract blockstates (many blocks inherit item models dynamically)
                        # assets/<namespace>/blockstates/<path>.json
                        m_block = re.match(r"^assets/([^/]+)/blockstates/(.+)\.json$", name)
                        if m_block:
                            modid, path = m_block.group(1), m_block.group(2)
                            valid_items.add(f"{modid}:{path.replace('/', '_')}")
                            valid_items.add(f"{modid}:{path}")
            except Exception:
                pass
                
    return valid_items, namespaces

def find_item_references(file_path: Path) -> list[tuple[int, str]]:
    """Extract potential namespace:id references from a text file with their line numbers."""
    refs = []
    # Regex to catch namespace:id formats (ignoring comments/URLs/metadata where possible)
    # Allows letters, numbers, underscores, dashes, dots, and slashes
    pattern = re.compile(r'\b([a-z0-9_.-]+:[a-z0-9_./-]+)\b')
    
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            for idx, line in enumerate(f, 1):
                # Simple comment filtering
                clean_line = line.split("//")[0].split("/*")[0]
                if "#" in clean_line and file_path.suffix == ".py":
                    clean_line = clean_line.split("#")[0]
                
                # Find all patterns
                for match in pattern.findall(clean_line):
                    # Filter out URLs, typical file paths or common false positives
                    if match.startswith(("http:", "https:", "file:", "c:", "d:")):
                        continue
                    # Filter out purely numeric or short namespaces
                    ns, path = match.split(":", 1)
                    if len(ns) <= 1 or ns.isdigit() or len(path) <= 1:
                        continue
                    # Ignore common KubeJS priority headers or settings
                    if ns in ("priority", "requires", "packmode"):
                        continue
                    refs.append((idx, match))
    except Exception as e:
        print(f"Error reading {file_path.name}: {e}")
    return refs

def main():
    print("Scanning mod jars for valid namespaces and item registries...")
    valid_items, namespaces = scan_mod_jars()
    print(f"Found {len(namespaces)} namespaces and {len(valid_items)} modded items in jars.\n")
    
    # Files to check
    kubejs_files = []
    for root, dirs, files in os.walk(KUBEJS_DIR):
        for f in files:
            if f.endswith(".js"):
                kubejs_files.append(Path(root) / f)
                
    quest_files = []
    if CHAPTERS_DIR.exists():
        for f in CHAPTERS_DIR.iterdir():
            if f.suffix == ".py" and f.name != "__init__.py":
                quest_files.append(f)
                
    print(f"Validating {len(kubejs_files)} KubeJS files and {len(quest_files)} Quest files...")
    print("-" * 65)
    
    total_errors = 0
    
    for file_path in kubejs_files + quest_files:
        rel_path = file_path.relative_to(ROOT)
        refs = find_item_references(file_path)
        
        file_errors = []
        for line_num, ref in refs:
            ns, path = ref.split(":", 1)
            
            # Skip whitelisted tags and types
            if ref in KNOWN_TAGS_AND_TYPES:
                continue
                
            # Skip ignored namespaces (tags, recipe namespaces)
            if ns in IGNORED_NAMESPACES:
                continue
                
            # Check namespace validity first
            if ns not in namespaces:
                # Suggest namespace correction
                matches = difflib.get_close_matches(ns, namespaces, n=1, cutoff=0.7)
                suggestion = f" (Did you mean '{matches[0]}'?)" if matches else ""
                file_errors.append((line_num, f"Unknown namespace '{ns}' in reference '{ref}'{suggestion}"))
                continue
                
            # Check item validity
            if ns == "minecraft":
                if path not in VANILLA_ITEMS:
                    # Minecraft item typo check
                    matches = difflib.get_close_matches(path, VANILLA_ITEMS, n=1, cutoff=0.7)
                    suggestion = f" (Did you mean '{matches[0]}'?)" if matches else ""
                    # Don't throw errors for tags or placeholder names (e.g. forge:xxx or minecraft:air)
                    if not path.startswith("forge") and path != "air":
                        file_errors.append((line_num, f"Unknown vanilla item '{ref}'{suggestion}"))
            else:
                if ref not in valid_items:
                    # Ignore common tags that are checked by LootJS/KubeJS (using forge: namespace, etc.)
                    # Tag check
                    if "tags/" in path or path.startswith("tags") or "/" in path:
                        continue
                    
                    # Modded item typo check
                    mod_items = [i.split(":", 1)[1] for i in valid_items if i.startswith(ns + ":")]
                    matches = difflib.get_close_matches(path, mod_items, n=1, cutoff=0.7)
                    suggestion = f" (Did you mean '{ns}:{matches[0]}'?)" if matches else ""
                    
                    file_errors.append((line_num, f"Unknown modded item '{ref}'{suggestion}"))
                    
        if file_errors:
            print(f"\n[FILE] {rel_path}")
            for line_num, err in sorted(set(file_errors)):
                print(f"  Line {line_num}: {err}")
                total_errors += 1
                
    print("-" * 65)
    if total_errors == 0:
        print("Success! No invalid item references or typos found.")
    else:
        print(f"Completed with {total_errors} potential issues found.")

if __name__ == "__main__":
    main()
