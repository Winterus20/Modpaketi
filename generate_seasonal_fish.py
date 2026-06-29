#!/usr/bin/env python3
"""Mevsimsel balık override üreticisi — kurallar README.md içinde."""

from __future__ import annotations

import json
import shutil
import zipfile
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path

LOADED_NAMESPACES = {
    "tide", "hybrid_aquatic", "minecraft", "aquaculture",
    "alexsmobs", "crabbersdelight", "crittersandcompanions",
}
SURFACE_CATEGORIES = ("freshwater", "saltwater", "misc")
DEDUP_FISH_IDS = {
    # Tide → Aquaculture / Hybrid (LootJS dedup kaynakları)
    "tide:arapaima", "tide:bluegill", "tide:carp", "tide:catfish",
    "tide:rainbow_trout", "tide:smallmouth_bass", "tide:coelacanth",
    "tide:mackerel", "tide:tuna",
    # Hybrid → Aquaculture / Alex's Mobs (canonical zaten ayrı fish data'ya sahip)
    "hybrid_aquatic:tuna", "hybrid_aquatic:carp", "hybrid_aquatic:piranha",
    "hybrid_aquatic:goldfish", "hybrid_aquatic:flying_fish", "hybrid_aquatic:blobfish",
}
DISABLED_STUB: dict = {"associated_mods": ["disabled"]}
# Canonical'ın jar'da fish data'sı yoksa, dedup kaynağından seasonal override üret
DEDUP_CANONICAL_FROM_SOURCE: dict[str, dict[str, str]] = {
    "hybrid_aquatic:goldfish": {
        "canonical": "aquaculture:goldfish",
        "output_rel": r"aquaculture\fishing\fish\freshwater\goldfish.json",
    },
}


def log(msg: str) -> None:
    try:
        print(f"[seasonal-fish] {msg}")
    except UnicodeEncodeError:
        print(f"[seasonal-fish] {msg}".encode("ascii", "replace").decode("ascii"))


def djb2_hash(text: str) -> int:
    h = 5381
    for ch in text:
        h = ((h << 5) + h + ord(ch)) & 0xFFFFFFFF
    return h


def get_preferred_temperature(fish: dict) -> float | None:
    for mod in fish.get("modifiers") or []:
        if mod.get("type") == "tide:temperature":
            pt = mod.get("preferred_temperature")
            if pt is not None:
                return float(pt)
    return None


ALL_SEASONS = ("spring", "summer", "fall", "winter")


def get_temperature_seasons(preferred_temp: float | None) -> list[str] | None:
    """Soğuk/sıcak balıklar için sabit mevsim; nötr için None."""
    if preferred_temp is not None:
        if preferred_temp <= -0.4:
            return ["spring", "fall", "winter"]
        if preferred_temp >= 0.4:
            return ["spring", "summer", "fall"]
    return None


def assign_neutral_seasons(fish_id: str, season_counts: dict[str, int]) -> list[str]:
    """Nötr balıklar: en kalabalık mevsimi dışarı bırakarak dengele."""
    ranked = sorted(
        ALL_SEASONS,
        key=lambda s: (season_counts[s], djb2_hash(f"{fish_id}:{s}")),
        reverse=True,
    )
    excluded = ranked[0]
    return [s for s in ALL_SEASONS if s != excluded]


def bump_season_counts(seasons: list[str], season_counts: dict[str, int]) -> None:
    for season in seasons:
        season_counts[season] += 1


def get_seasons_for_fish(
    fish_id: str,
    preferred_temp: float | None,
    season_counts: dict[str, int] | None = None,
) -> list[str]:
    temp_seasons = get_temperature_seasons(preferred_temp)
    if temp_seasons is not None:
        return temp_seasons
    if season_counts is not None:
        return assign_neutral_seasons(fish_id, season_counts)
    # season_counts olmadan (tek balık önizleme): kararlı hash yedek
    if djb2_hash(fish_id) % 2 == 0:
        return ["summer", "fall", "winter"]
    return ["spring", "summer", "winter"]


def deep_merge(base: dict, override: dict) -> dict:
    result = deepcopy(base)
    for key, val in override.items():
        if key in result and isinstance(result[key], dict) and isinstance(val, dict):
            result[key] = deep_merge(result[key], val)
        else:
            result[key] = deepcopy(val)
    return result


def remap_fish_to_canonical(fish: dict, canonical_id: str) -> dict:
    """Dedup kaynağı fish data'sını canonical ID'ye taşır (ör. hybrid goldfish → aquaculture)."""
    old_id = fish["fish"]
    old_ns, old_name = old_id.split(":", 1)
    new_ns, new_name = canonical_id.split(":", 1)
    result = deepcopy(fish)
    result["fish"] = canonical_id
    result["associated_mods"] = [new_ns]

    if bucket := result.get("bucket"):
        result["bucket"] = bucket.replace(old_ns, new_ns).replace(
            f"{old_name}_bucket", f"{new_name}_bucket"
        )

    if display := result.get("display_data"):
        if entity := display.get("entity"):
            display["entity"] = entity.replace(old_id, canonical_id)

    if journal := result.get("journal_profile"):
        for key in ("description",):
            if val := journal.get(key):
                journal[key] = val.replace(f"journal.description.{old_ns}.", f"journal.description.{new_ns}.")
                journal[key] = journal[key].replace(f"{old_ns}.{old_name}", f"{new_ns}.{new_name}")

    return result


def set_seasons_condition(fish: dict, seasons: list[str]) -> None:
    conditions = fish.get("conditions") or []
    conditions = [c for c in conditions if c.get("type") != "tide:seasons"]
    conditions.append({"type": "tide:seasons", "seasons": seasons})
    fish["conditions"] = conditions


def ensure_jar_extracted(jar_path: Path, dest_dir: Path, force: bool = False) -> None:
    marker = dest_dir / ".extracted"
    if not force and marker.exists() and (dest_dir / "data").is_dir():
        return
    if dest_dir.exists():
        shutil.rmtree(dest_dir)
    dest_dir.mkdir(parents=True)
    with zipfile.ZipFile(jar_path, "r") as zf:
        zf.extractall(dest_dir)
    marker.write_text(datetime.now(timezone.utc).isoformat(), encoding="utf-8")
    log(f"Çıkarıldı: {jar_path.name} -> {dest_dir.name}")


def build_indexes(data_roots: list[Path]) -> tuple[dict[str, Path], dict[str, str]]:
    """by_rel: rel_path -> full path; by_fish_id: fish_id -> rel_path"""
    by_rel: dict[str, Path] = {}
    by_fish_id: dict[str, str] = {}

    for root in data_roots:
        data_dir = root / "data"
        if not data_dir.is_dir():
            continue
        for path in data_dir.rglob("fishing/fish/**/*.json"):
            rel = path.relative_to(data_dir).as_posix().replace("/", "\\")
            by_rel[rel] = path
            try:
                data = json.loads(path.read_text(encoding="utf-8"))
            except json.JSONDecodeError as exc:
                log(f"UYARI: JSON okunamadı {path}: {exc}")
                continue
            fish_id = data.get("fish")
            if not fish_id:
                parts = rel.split("\\")
                fish_id = f"{parts[0]}:{Path(parts[-1]).stem}"
            by_fish_id[fish_id] = rel

    return by_rel, by_fish_id


def collect_surface_files(data_roots: list[Path]) -> dict[str, Path]:
    result: dict[str, Path] = {}
    for root in data_roots:
        data_dir = root / "data"
        if not data_dir.is_dir():
            continue
        for cat in SURFACE_CATEGORIES:
            for path in data_dir.rglob(f"fishing/fish/{cat}/*.json"):
                rel = path.relative_to(data_dir).as_posix().replace("/", "\\")
                ns = rel.split("\\")[0]
                if ns in LOADED_NAMESPACES:
                    result[rel] = path
    return result


def resolve_parent_chain(
    rel: str,
    by_rel: dict[str, Path],
    by_fish_id: dict[str, str],
    cache: dict[str, dict],
) -> dict:
    if rel not in cache:
        cache[rel] = json.loads(by_rel[rel].read_text(encoding="utf-8"))

    obj = deepcopy(cache[rel])
    parent_id = obj.pop("parent", None)
    if not parent_id:
        return obj

    if parent_id not in by_fish_id:
        raise KeyError(f"Parent bulunamadı: {parent_id} (kaynak: {rel})")

    parent_rel = by_fish_id[parent_id]
    parent_obj = resolve_parent_chain(parent_rel, by_rel, by_fish_id, cache)
    return deep_merge(parent_obj, obj)


def backup_existing(backup_dir: Path, kube_data: Path, output_paths: list[Path]) -> int:
    backup_dir.mkdir(parents=True, exist_ok=True)
    backed = 0
    for out_path in output_paths:
        if out_path.exists():
            rel = out_path.relative_to(kube_data)
            dest = backup_dir / rel
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(out_path, dest)
            backed += 1
    log(f"Yedeklendi: {backed} dosya -> {backup_dir}")
    return backed


def main() -> None:
    instance_root = Path(__file__).resolve().parent
    mods_dir = instance_root / "mods"
    kube_data = instance_root / "kubejs" / "data"
    tmp_tide = instance_root / "tmp_tide"
    tmp_extra = instance_root / "tmp_tide_extra"

    tide_jar = mods_dir / "tide-forge-1.20.1-2.1.jar"
    extra_jar = mods_dir / "tide-extra-compatibility-2.2.0.jar"

    log(f"Başlıyor — kök: {instance_root}")

    ensure_jar_extracted(tide_jar, tmp_tide)
    ensure_jar_extracted(extra_jar, tmp_extra)

    data_roots = [tmp_tide, tmp_extra]
    by_rel, by_fish_id = build_indexes(data_roots)
    surface_files = collect_surface_files(data_roots)
    log(f"Yüzey balık dosyası (yüklü namespace): {len(surface_files)}")

    cache: dict[str, dict] = {}
    manifest_entries: list[dict] = []
    pending_writes: list[tuple[Path, dict]] = []
    skipped_dedup = 0
    season_work: list[dict] = []

    for rel, source_path in sorted(surface_files.items()):
        try:
            merged = resolve_parent_chain(rel, by_rel, by_fish_id, cache)
        except KeyError as exc:
            log(f"UYARI: Atlandı {rel} — {exc}")
            continue

        fish_id = merged.get("fish")
        if not fish_id:
            parts = rel.split("\\")
            fish_id = f"{parts[0]}:{Path(parts[-1]).stem}"
            merged["fish"] = fish_id

        if fish_id in DEDUP_FISH_IDS:
            skipped_dedup += 1
            out_path = kube_data / rel.replace("\\", "/")
            pending_writes.append((out_path, deepcopy(DISABLED_STUB)))

            canon_info = DEDUP_CANONICAL_FROM_SOURCE.get(fish_id)
            if canon_info:
                canonical_id = canon_info["canonical"]
                canonical_fish = remap_fish_to_canonical(merged, canonical_id)
                canonical_fish.pop("parent", None)
                pref_temp = get_preferred_temperature(canonical_fish)
                category = canon_info["output_rel"].split("fishing\\fish\\")[1].split("\\")[0]
                season_work.append({
                    "fish": canonical_fish,
                    "fish_id": canonical_id,
                    "pref_temp": pref_temp,
                    "namespace": canonical_id.split(":")[0],
                    "category": category,
                    "source": str(source_path),
                    "output": canon_info["output_rel"],
                    "remapped_from": fish_id,
                })
            continue

        merged.pop("parent", None)
        pref_temp = get_preferred_temperature(merged)
        category = rel.split("fishing\\fish\\")[1].split("\\")[0]
        season_work.append({
            "fish": merged,
            "fish_id": fish_id,
            "pref_temp": pref_temp,
            "namespace": rel.split("\\")[0],
            "category": category,
            "source": str(source_path),
            "output": rel,
        })

    season_counts: dict[str, int] = {s: 0 for s in ALL_SEASONS}
    for item in season_work:
        temp_seasons = get_temperature_seasons(item["pref_temp"])
        if temp_seasons is not None:
            item["seasons"] = temp_seasons
            bump_season_counts(temp_seasons, season_counts)

    for item in sorted(
        (i for i in season_work if "seasons" not in i),
        key=lambda i: i["fish_id"],
    ):
        seasons = assign_neutral_seasons(item["fish_id"], season_counts)
        item["seasons"] = seasons
        bump_season_counts(seasons, season_counts)

    for item in season_work:
        set_seasons_condition(item["fish"], item["seasons"])
        out_path = kube_data / item["output"].replace("\\", "/")
        out_path.parent.mkdir(parents=True, exist_ok=True)
        pending_writes.append((out_path, item["fish"]))

        entry = {
            "fish": item["fish_id"],
            "namespace": item["namespace"],
            "category": item["category"],
            "preferred_temperature": item["pref_temp"],
            "seasons": item["seasons"],
            "source": item["source"],
            "output": item["output"],
        }
        if remapped := item.get("remapped_from"):
            entry["remapped_from"] = remapped
        manifest_entries.append(entry)

    backup_dir = kube_data / f"_backup_fishing_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    backup_existing(backup_dir, kube_data, [p for p, _ in pending_writes])

    for out_path, merged in pending_writes:
        out_path.write_text(
            json.dumps(merged, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )

    log(f"Yazıldı: {len(pending_writes)} override dosyası (dedup atlandı: {skipped_dedup})")

    season_summary: dict[str, dict] = {}
    for season in ALL_SEASONS:
        season_summary[season] = {
            "total": 0,
            "by_category": {cat: 0 for cat in SURFACE_CATEGORIES},
        }

    for entry in manifest_entries:
        for season in ALL_SEASONS:
            if season in entry["seasons"]:
                season_summary[season]["total"] += 1
                season_summary[season]["by_category"][entry["category"]] += 1

    totals = [season_summary[s]["total"] for s in ALL_SEASONS]
    season_balance = {
        "min": min(totals),
        "max": max(totals),
        "spread": max(totals) - min(totals),
    }

    manifest = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "total_fish": len(manifest_entries),
        "skipped_dedup": skipped_dedup,
        "backup_dir": str(backup_dir),
        "season_summary": season_summary,
        "season_balance": season_balance,
        "fish": manifest_entries,
    }
    manifest_path = kube_data / "_seasonal_fish_manifest.json"
    manifest_path.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    log(f"Manifest: {manifest_path}")

    log("--- Mevsim özeti ---")
    for season in ALL_SEASONS:
        info = season_summary[season]
        cats = ", ".join(f"{k}={v}" for k, v in info["by_category"].items())
        log(f"  {season}: {info['total']} balık ({cats})")
    log(f"  Denge: min={season_balance['min']}, max={season_balance['max']}, spread={season_balance['spread']}")

    log("Tamamlandı. Oyunu tam yeniden başlatın (/reload yetmez).")


if __name__ == "__main__":
    main()
