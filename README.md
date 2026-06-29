# Balik — Mod Paketi

**Minecraft 1.20.1 · Forge 47.4.10 · Prism Launcher instance**

Bu belge, paketin **felsefesini**, **geliştirme yol haritasını** ve **teknik kurallarını** tanımlar.
Sonraki oturumlarda (insan veya yapay zeka) buradan okuyarak ne yapılmaya çalışıldığını anlamalıdır.

---

## Vizyon

Bu paket **yalnızca bir balıkçılık modu değildir**.

Uzun vadeli hedef: **Stardew Valley** veya **Sun Haven** tarzı bir **yaşam simülasyonu** —
mevsimlere bağlı çiftçilik, balıkçılık, yemek üretimi, keşif ve (ileride) köy/NPC/ekonomi döngüsü.

Paket şu an **Faz 1 tamamlandı, Faz 2–3 kısmen entegre** aşamasındadır.

> **Önemli:** Instance adı geçici olarak "Balik"tir. Nihai kimlik cozy farm-life sim'dir.

---

## Tasarım ilkeleri

1. **Mevsimler omurgadır.** Serene Seasons hem ekinleri hem balıkları etkiler.
2. **Tek kanonik eşya.** Duplikasyon tarif, loot ve JEI'den temizlenir.
3. **Tide = balıkçılık motoru.** `overrideVanillaRod: true`.
4. **KubeJS = entegrasyon katmanı.** Köprüler script ve üretici araçlarla yönetilir.
5. **Kademeli büyüme.** Fazlar sırayla; mevcut entegrasyon bozulmamalıdır.

---

## Geliştirme fazları

| Faz | Durum | Açıklama |
|-----|-------|----------|
| **1 — Balık temeli** | ✅ Tamam | Tide, dedup, mevsimsel balık, trap, tag'ler |
| **2 — Tarım & mevsim** | 🔄 Kısmen | Dedup + FFB pazar + Patchouli rehber; tam ekin takvimi ileride |
| **3 — Yemek zinciri** | 🔄 Kısmen | Let's Do / Croptopia / Delight dedup genişletildi |
| **4 — Ekonomi** | ⏳ Bekliyor | FFB pazar başlangıç var; para birimi yok |
| **5 — Rehber & görevler** | 🔄 Kısmen | Patchouli Köy Günlüğü + ilk giriş; FTB Quests yok |
| **6 — Köy & NPC** | ⏳ Bekliyor | Planlanmadı |

---

## Mod grupları (özet)

### Balık & deniz (Faz 1)
- **Tide** + tide-extra-compatibility
- **Hybrid Aquatic**, **Aquaculture** + Aquaculture Delight
- **Alex's Mobs**, **Crabber's Delight**, **Ocean's Delight**
- **Critters and Companions**, **Fishermen's Trap**

### Yaşam sim (Faz 2–3)
- **Serene Seasons**, **Farmer's Delight**, **Farm & Charm**, **Croptopia**
- **Let's Do:** Bakery, Beachparty, Brewery, Candlelight, Vinery
- **Farming for Blockheads**, **FruitfulFun**, **Botany Pots**, **Right Click Harvest**

### Arı & doğa
- **Productive Bees**, **Buzzier Bees**, **BeeFix**, **Realistic Bees**, **The Bumblezone**

### Teknik & QoL
- **KubeJS**, **LootJS**, **Rhino**, **Patchouli**, **JEI**, **Create** + **Slice and Dice**

Tam mod listesi: `mods/` klasörü (~57 jar).

---

## Teknik mimari

### Balıkçılık akışı

```
Oyuncu olta atar
    → Tide loot sistemi
    → Fish data: kubejs/data/<namespace>/fishing/fish/...
    → Koşullar: boyut, sıvı, derinlik, tide:seasons
    → LootJS dedup → kanonik eşya
```

### Mevsimsel balık

- Üretici: `generate_seasonal_fish.py` (kurallar bu README'de)
- Manifest: `kubejs/data/_seasonal_fish_manifest.json`
- **Kural:** Soğuk su (T≤−0.4) → ilkbahar+sonbahar+kış; sıcak su (T≥+0.4) → ilkbahar+yaz+sonbahar; nötr → 1 mevsim hariç
- **Kapsam dışı:** `underground`, `lava`, `void`
- Script sonrası **tam oyun yeniden başlatma** gerekir

### Mükerrer eşya yönetimi (dedup)

| Dosya | Ne yapar |
|-------|----------|
| `tools/dedup_mappings.json` | Tek kaynak — tüm eşleştirmeler |
| `tools/generate_dedup_kubejs.py` | → `kubejs/startup_scripts/dedup_data.js` üretir |
| `kubejs/server_scripts/deduplication.js` | Tarif + tag |
| `kubejs/server_scripts/loot_deduplication.js` | LootJS |
| `kubejs/client_scripts/hide_items.js` | JEI gizleme |

**Yeni duplike ekleme:** `dedup_mappings.json` düzenle → `python tools/generate_dedup_kubejs.py` çalıştır.

**Kanonik hub'lar:** FD (temel mutfak/sebze), F&C (tahıl), Bakery/Brewery/Vinery (işlenmiş), Aquaculture (balık), Crabber's (kabuklu), Beachparty (palmiye), Alex's Mobs (özel deniz), Critters (inci/istiridye).

### Fisherman's Trap

- Yem tag'leri: Aquaculture + Tide yemleri
- Ekmek yemi loot'u `tide:fish` tag'ini kullanır (`kubejs/data/fishermens_trap/.../bread.json`)

### Pazar (FFB)

- `config/farmingforblockheads/MarketRegistry.json` — mevsimsel tohum ve balık yemi kategorileri

### Rehber

- Patchouli kitabı: `balik:field_journal` (Köy Günlüğü)
- İlk girişte Köy Günlüğü envantere verilir (`kubejs/server_scripts/onboarding.js`)

### Önemli config

| Dosya | Not |
|-------|-----|
| `config/tide.json5` | `overrideVanillaRod: true`, `logDataErrors: true` |
| `config/sereneseasons/seasons.toml` | Overworld, `sub_season_duration = 8` |
| `config/sereneseasons/fertility.toml` | `seasonal_crops = true` |

---

## Dizin yapısı

```
minecraft/
├── README.md
├── generate_seasonal_fish.py
├── tools/
│   ├── dedup_mappings.json
│   ├── generate_dedup_kubejs.py
│   └── scan_mod_items.py
├── kubejs/
│   ├── startup_scripts/dedup_data.js   (üretilmiş)
│   ├── server_scripts/
│   ├── client_scripts/
│   └── data/                           (balık override, patchouli, trap loot)
├── config/
└── mods/
```

---

## Geliştirici kuralları

### Yap
- Dedup değişikliği → `dedup_mappings.json` + generator script
- Mevsimsel balık → `generate_seasonal_fish.py` + tam restart
- Üç KubeJS katmanı senkron (generator bunu sağlar)

### Yapma
- Kanonik eşyaları keyfi değiştirme
- Fish override'larını elle düzenleme
- Habersiz mod ekleme/çıkarma

---

## Bilinen açık işler

- [ ] Oyun içi doğrulama: `/fishing test loot`, `/season set`
- [ ] Tam mevsimsel ekin takvimi tasarımı (Faz 2)
- [ ] Para birimi ve ilerleme ekonomisi (Faz 4)
- [ ] FTB Quests entegrasyonu (Faz 5)
- [ ] Köy & NPC (Faz 6)
- [ ] Paket adı nihai vizyona göre güncellenecek

---

## Referanslar

- [KubeJS](https://kubejs.com/) · [Tide](https://modrinth.com/mod/tide) · [Serene Seasons](https://modrinth.com/mod/serene-seasons)
- Mevsimsel balık manifesti → `kubejs/data/_seasonal_fish_manifest.json`
