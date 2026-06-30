import os
import sys
import json
import hashlib
import importlib

class SNBTDouble:
    def __init__(self, val):
        self.val = float(val)
    def __str__(self):
        return f"{self.val}d"

class SNBTLong:
    def __init__(self, val):
        self.val = int(val)
    def __str__(self):
        return f"{self.val}L"

def gen_id(key: str) -> str:
    h = hashlib.sha256(key.encode('utf-8')).hexdigest()
    return h[:16].upper()

def to_snbt(val, indent=0) -> str:
    tab = "\t" * indent
    if isinstance(val, dict):
        if not val:
            return "{ }"
        parts = ["{"]
        for k, v in val.items():
            key_str = k
            if not k.isalnum() and "_" not in k:
                key_str = f'"{k}"'
            parts.append(f"{tab}\t{key_str}: {to_snbt(v, indent + 1)}")
        parts.append(tab + "}")
        return "\n".join(parts)
    elif isinstance(val, list):
        if not val:
            return "[ ]"
        is_all_primitives = all(isinstance(x, (str, int, float, bool, SNBTDouble, SNBTLong)) for x in val)
        if is_all_primitives and len(val) <= 4:
            items = [to_snbt(x) for x in val]
            return f"[ {', '.join(items)} ]"
        parts = ["["]
        for x in val:
            parts.append(f"{tab}\t{to_snbt(x, indent + 1)}")
        parts.append(tab + "]")
        return "\n".join(parts)
    elif isinstance(val, str):
        escaped = val.replace('"', '\\"')
        return f'"{escaped}"'
    elif isinstance(val, bool):
        return "true" if val else "false"
    elif isinstance(val, (SNBTDouble, SNBTLong)):
        return str(val)
    elif isinstance(val, float):
        return f"{val}d"
    elif isinstance(val, int):
        return str(val)
    else:
        return str(val)

def load_chapters():
    """Load all chapter modules from the chapters/ directory."""
    chapters_dir = os.path.join(os.path.dirname(__file__), "chapters")
    sys.path.insert(0, chapters_dir)

    chapters = []
    for fname in os.listdir(chapters_dir):
        if fname.endswith(".py") and fname != "__init__.py":
            module_name = fname[:-3]
            mod = importlib.import_module(module_name)
            if hasattr(mod, "CHAPTER"):
                chapters.append(mod.CHAPTER)

    chapters.sort(key=lambda ch: ch.get("order", 999))
    sys.path.pop(0)
    return chapters

def main():
    base_dir = os.path.join(os.path.dirname(__file__), "..")
    quests_dir = os.path.join(base_dir, "config/ftbquests/quests")
    chapters_dir = os.path.join(quests_dir, "chapters")
    lang_dir = os.path.join(base_dir, "kubejs/assets/kubejs/lang")

    os.makedirs(chapters_dir, exist_ok=True)
    os.makedirs(lang_dir, exist_ok=True)

    chapters_data = load_chapters()

    en_translations = {}
    tr_translations = {}

    # 1. Generate data.snbt
    data_id = gen_id("data")
    data_snbt = {
        "default_page_width": 24.0,
        "default_quest_shape": "circle",
        "default_reward_team": False,
        "detection_delay": 20,
        "disable_gui": False,
        "drop_loot_crates": False,
        "enemy_max_stats": {
            "armor": 20.0,
            "armor_toughness": 12.0,
            "attack_damage": 10.0,
            "max_health": 40.0,
            "movement_speed": 0.25
        },
        "enemy_stats_by_difficulty": {},
        "grid_scale": 0.5,
        "icon": "minecraft:book",
        "id": data_id,
        "lock_message": "",
        "loot_crate_no_drop": {
            "boss": 0,
            "monster": 0,
            "passive": 0
        },
        "pause_game": False,
        "progression_mode": "linear",
        "title": "Modpack Görevleri",
        "version": "2001.4.22"
    }

    with open(os.path.join(quests_dir, "data.snbt"), "w", encoding="utf-8") as f:
        f.write(to_snbt(data_snbt))

    # 2. Generate each chapter snbt and collect lang entries
    for ch in chapters_data:
        filename = ch["filename"]
        ch_id = gen_id(f"chapter:{filename}")

        # Translation keys for chapter
        ch_title_key = f"kubejs.ftbquests.chapter.{filename}.title"
        en_translations[ch_title_key] = ch["title_en"]
        tr_translations[ch_title_key] = ch["title_tr"]

        quests_list = []
        for q in ch["quests"]:
            q_key = q["key"]
            q_id = q.get("custom_id", gen_id(f"quest:{filename}:{q_key}"))

            q_title_key = f"kubejs.ftbquests.quest.{filename}.{q_key}.title"
            en_translations[q_title_key] = q["title_en"]
            tr_translations[q_title_key] = q["title_tr"]

            # Set up description lines
            desc_lines = []
            for i, (line_en, line_tr) in enumerate(zip(q["desc_en"], q["desc_tr"])):
                desc_key = f"kubejs.ftbquests.quest.{filename}.{q_key}.desc.{i}"
                en_translations[desc_key] = line_en
                tr_translations[desc_key] = line_tr
                desc_lines.append(f"{{{desc_key}}}")

            # Construct tasks
            tasks_list = []
            for t_idx, t in enumerate(q["tasks"]):
                t_id = gen_id(f"task:{filename}:{q_key}:{t_idx}")
                t_snbt = {
                    "id": t_id,
                    "type": t["type"]
                }
                if t["type"] == "item":
                    if isinstance(t["item"], dict):
                        item_dict = {"id": t["item"]["id"], "Count": 1}
                        if "tag" in t["item"]:
                            item_dict["tag"] = t["item"]["tag"]
                        t_snbt["item"] = item_dict
                    else:
                        t_snbt["item"] = t["item"]
                        t_snbt["count"] = SNBTLong(t.get("count", 1))
                tasks_list.append(t_snbt)

            # Construct rewards
            rewards_list = []
            for r_idx, r in enumerate(q["rewards"]):
                r_id = gen_id(f"reward:{filename}:{q_key}:{r_idx}")
                r_snbt = {
                    "id": r_id,
                    "type": r["type"]
                }
                if r["type"] == "item":
                    r_snbt["item"] = r["item"]
                    r_snbt["count"] = r.get("count", 1)
                rewards_list.append(r_snbt)

            q_snbt = {
                "id": q_id,
                "title": f"{{{q_title_key}}}",
                "x": SNBTDouble(q["x"]),
                "y": SNBTDouble(q["y"]),
                "description": desc_lines,
                "tasks": tasks_list,
                "rewards": rewards_list
            }

            # Add dependencies
            if "dependency" in q:
                if isinstance(q["dependency"], list):
                    dep_ids = [gen_id(f"quest:{filename}:{d}") for d in q["dependency"]]
                    q_snbt["dependencies"] = dep_ids
                else:
                    dep_id = gen_id(f"quest:{filename}:{q['dependency']}")
                    q_snbt["dependencies"] = [dep_id]
            elif "dependency_or" in q:
                dep_ids = [gen_id(f"quest:{filename}:{d}") for d in q["dependency_or"]]
                q_snbt["dependencies"] = dep_ids
                q_snbt["dependency_requirement"] = "one_completed"
            elif "dependencies" in q:
                dep_ids = [gen_id(f"quest:{filename}:{d}") for d in q["dependencies"]]
                q_snbt["dependencies"] = dep_ids

            quests_list.append(q_snbt)

        chapter_snbt = {
            "id": ch_id,
            "group": "",
            "order_index": ch.get("order", 0),
            "filename": filename,
            "title": f"{{{ch_title_key}}}",
            "icon": ch["icon"],
            "default_quest_shape": "",
            "default_hide_dependency_lines": False,
            "quests": quests_list,
            "quest_links": []
        }

        with open(os.path.join(chapters_dir, f"{filename}.snbt"), "w", encoding="utf-8") as f:
            f.write(to_snbt(chapter_snbt))
        print(f"Generated chapter: {filename}.snbt")

    # 3. Write language files
    # English
    en_path = os.path.join(lang_dir, "en_us.json")
    try:
        with open(en_path, "r", encoding="utf-8") as f:
            existing_en = json.load(f)
    except:
        existing_en = {}
    existing_en.update(en_translations)
    with open(en_path, "w", encoding="utf-8") as f:
        json.dump(existing_en, f, indent=4, ensure_ascii=False)
    print("Updated en_us.json")

    # Turkish
    tr_path = os.path.join(lang_dir, "tr_tr.json")
    try:
        with open(tr_path, "r", encoding="utf-8") as f:
            existing_tr = json.load(f)
    except:
        existing_tr = {}
    existing_tr.update(tr_translations)
    with open(tr_path, "w", encoding="utf-8") as f:
        json.dump(existing_tr, f, indent=4, ensure_ascii=False)
    print("Updated tr_tr.json")

if __name__ == "__main__":
    main()
