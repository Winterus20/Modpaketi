# Mevsimsel Balık Avı Planı (Serene Seasons × Tide)

Bu plan, paketteki **tüm yüzey balıklarının** Serene Seasons mevsimlerine göre
tutulabilir hale getirilmesi için hazırlanmıştır. Uygulama onaylanmadıkça
hiçbir oyun dosyasına dokunulmaz; bu belge yalnızca plan + üretici script taslağıdır.

---

## 1. Sistem nasıl çalışıyor (araştırma özeti)

- Pakette balıkçılık **Tide** modu üzerinden yürür. `config/tide.json5` içinde
  `overrideVanillaRod: true` → vanilla olta dahil tüm avlar Tide'in loot sistemini kullanır.
- Tide balıkları `data/<namespace>/fishing/fish/<kategori>/<balık>.json` yolundan okur.
  Her dosyanın `conditions` dizisindeki koşulların **hepsi** sağlanmalı, yoksa balık o avda seçilmez.
- Tide jar'ında `com/li64/tide/compat/seasons/SereneSeasonsCompat.class` ve
  `SeasonsCondition.class` var → Tide, Serene Seasons ile **native entegredir**.
- Mevsim koşulu:
  ```json
  { "type": "tide:seasons", "seasons": ["spring", "summer", "fall", "winter"] }
  ```
- Geçerli mevsim değerleri: **`spring`, `summer`, `fall`, `winter`** ("autumn" değil).
- Serene Seasons sadece **minecraft:overworld** boyutunda aktif
  (`config/sereneseasons/seasons.toml` → `whitelisted_dimensions = ["minecraft:overworld"]`).
  Paket 4 mevsim temperate döngü kullanıyor (starting_sub_season = 1, sub_season_duration = 8).

## 2. Kapsam

### Dahil edilen kategoriler (yüzey)
- `freshwater` (tatlı su)
- `saltwater` (tuzlu su)
- `misc` (Tide'in hybrid_aquatic balıklarını koyduğu açık su grubu)

### Hariç tutulan kategoriler
- `underground` (mağara balıkları — mevsim temasız)
- `lava` (Nether balıkları — Serene Seasons Nether'da aktif değil)
- `void` (End balıkları — Serene Seasons End'de aktif değil)

### Yüklü balık modları (sadece bunların balıkları yüklenir)
`tide`, `hybrid_aquatic`, `aquaculture`, `alexsmobs`, `crabbersdelight`,
`crittersandcompanions`, `minecraft`

> tide-extra-compatibility ve tide.jar, yüklü OLMAYAN modların
> (fishofthieves, stardew_fishing, finsandtails, rainbowreef, jellyfishing,
> unusualfishmod, netherdepthsupgrade, luminousworld, undergarden, blue_skies,
> betterend, ...) balık datalarını da içerir; Tide bunları zaten atlar
> (`associated_mods` kapısı veya mod jar'ı yokluğu). Üretici script sadece
> yüklü modlarınkilerini yazdırarak dosya kirliliğini önler.
>
> **Not:** `kubejs/data/unusualfishmod/` altındaki dosyalar vanilla fishing loot
> tablolarıdır (`unusual_catch_*_treasure.json`); Tide fish data'sı değildir.
> `unusualfishmod` modu pakette yüklü değil — `mods/` klasöründe jar yok, log'da
> mod yüklenme kaydı yok.

### Hariç tutulan Tide mükerrer balıkları (dedup)
`kubejs/data/tide/fishing/fish/...` içinde `associated_mods: ["disabled"]` ile
devre dışı bırakılmış 9 yüzey balığı üretim dışı tutulacak (Aquaculture/Hybrid
Aquatic eşdeğerleri tutulduğu için):
`tide:arapaima, bluegill, carp, catfish, rainbow_trout, smallmouth_bass,
coelacanth, mackerel, tuna`

### Tahmini üretilecek dosya sayısı
~119 override dosyası (yüklü namespace'ler + 9 dedup hariç; doğrulandı).

## 3. Mevsim atama kuralı (temp3 + nötr hash)

`preferred_temperature` (varsa) → **-1 (en soğuk) … +1 (en sıcak)** aralığında.

| Sıcaklık T | Mevsimler | Dışlanan mevsim |
|---|---|---|
| T ≤ -0.4 (soğuk su) | `spring`, `fall`, `winter` | `summer` |
| T ≥ +0.4 (sıcak su)  | `spring`, `summer`, `fall` | `winter` |
| -0.4 < T < +0.4 (nötr) **veya** sıcaklık datası yok | hash'e göre aşağıdaki | spring veya fall |

### Nötr balıklar için hash kuralı
Nötr balıklar **tam 1 mevsim dışarı** kalır; dışlanacak mevsim `spring`/`fall`
arasından, balık ID'sinin kararlı hash'ine göre 50/50 seçilir (yaz/kış
soğuk&sıcak balıklar tarafından zaten kapsandığı için nötrleri oradan seçmek
dengeyi bozmaz):

```js
function neutralSeasons(fishId) {
  const h = hashString(fishId);          // kararlı, örn. djb2
  return (h % 2 === 0)
    ? ["summer", "fall", "winter"]        // spring dışarı
    : ["spring", "summer", "winter"];     // fall dışarı
}
```

### Sonuç
Her balık tam 1 mevsim dışında kalır → tüm balıklar mevsimsel, hiçbir mevsim boş
kalmaz, her mevsimde ~balıkların %75'i tutulabilir. `tide:temperature`
modifier'ı zaten soğuk balığı yazınca zorlaştırıyordu; `tide:seasons` hard gate
onu imkansız yapar — istenen etki bu.

### Karar (kullanıcı)
- Nötr balıklar: **(b) 1 mevsim dışarı (hash)** ✓
- Zaten mevsimsel 24 balık: **(b) hepsi temp3 ile yeniden yaz** ✓
  (yazarın orijinal `tide:seasons` koşulu silinip temp3 sonucuyla değiştirilecek)

## 4. Parent kalıtımı çözümü (uygulama kararı — asistan seçimi)

Bazı balık dosyaları `"parent": "tide:tuna"` gibi bir ebeveyne bağlanır ve yalnızca
birkaç alanı (display/journal) geçersiz kılar; `conditions`, `modifiers`,
`selection_weight`, `size`, `speed`, `strength` gibi alanları child dosyada
**tanımlı değildir** — Tide'in bunları ebeveynden miras aldığı data yapısından
çıkarılır (6 dosya: hybrid_aquatic misc altında anglerfish, carp, coelacanth,
mackerel, mahi, tuna). Runtime birleştirme class decompile ile doğrulanmadı;
override'ları self-contained yazmak bu belirsizliği ortadan kaldırır.
Örnek: `hybrid_aquatic/fishing/fish/misc/tuna.json` → `parent: tide:tuna`.

**Seçilen yöntem: Tam parent çözümü + bağımsız dosya.**
1. Üretici script, child dosyayı okur; `parent` alanı varsa ebeveven dosyayı
   (aynı data kökünde) bulur ve **özyinelemeli** (parent'ın da parent'ı olabilir)
   şekilde tüm alanları birleştirir: ebevevenin tüm alanları baz alınır, child
   alanları override eder.
2. Birleştirilmiş `conditions` dizisine temp3 `tide:seasons` koşulu enjekte edilir
   (var olan `tide:seasons` varsa değiştirilir).
3. Çıktı dosyasına `parent` alanı **yazılmaz** — her override dosyası tamamen
   kendi kendine yeten (self-contained) bir balık tanımı olur.
4. Böylece Tide'in runtime parent birleştirme davranışına bağımlı kalmadan
   her balık deterministik ve doğru olur.

Risk: Tide sürüm güncellenirse orijinal parent/child dataları değişebilir,
override'lar bayatlar. Mod paketi snapshot'u için kabul edilebilir. Gerekirse
üretici script tekrar çalıştırılır.

## 5. Override mekanizği

- Override dosyaları: `kubejs/data/<namespace>/fishing/fish/<kategori>/<balık>.json`
- KubeJS `kubejs/data` bir datapacktir ve mod jar'ından **yüksek önceliğe** sahiptir
  → aynı yoldaki dosyayı geçersiz kılar. Tide merge etmez, **tam dosyayı değiştirir**.
- Bu yüzden her override, orijinalin **tüm alanlarını** korumalı, sadece
  `conditions` içine `tide:seasons` eklemelidir. Üretici script bunu garanti eder.
- Balık datası **server startup'ta** yüklenir → değişiklikler **tam oyun yeniden
  başlatma** gerektirir (`/reload` yeterli olmaz).

## 6. Üretici script tasarımı (PowerShell)

Script hiçbir oyun dosyasını doğrudan değiştirmez; sadece `kubejs/data` altına
yeni override dosyaları yazar + bir manifest üretir.

### Akış
1. İki kaynak jar'ı geçici klasöre çıkar (`tmp_tide`, `tmp_tide_extra`) —
   araştırma sırasında çıkarıldı, script tekrar kullanabilir.
2. Yüklü mod namespace kümesi: `{tide, hybrid_aquatic, minecraft, aquaculture,
   alexsmobs, crabbersdelight, crittersandcompanions}`.
3. Her iki data kökünde `**/fishing/fish/{freshwater,saltwater,misc}/*.json`
   dosyalarını tara; namespace'i yüklü kümede olanları al.
4. Tide mükerrer disabled listesini atla (Bölüm 2).
5. Her dosya için:
   a. Parent'ı özyinelemeli çöz, tüm alanları birleştir, `parent`ı drop et.
   b. `modifiers` içinden `tide:temperature` → `preferred_temperature` oku.
   c. temp3 + nötr hash kuralıyla seasons hesapla.
   d. `conditions` içinde `tide:seasons` varsa değiştir, yoksa ekle.
   e. `kubejs/data/<namespace>/fishing/fish/<kategori>/<balık>.json` yaz
      (güzelIndent'li JSON, UTF-8).
6. `kubejs/data/_seasonal_fish_manifest.json` üret: her balık →
   `{fish, namespace, category, preferred_temperature, seasons, source}`.
   Bu manifest, uygulamadan önce gözden geçirme için kullanılır.

### Script tarafından korunan orijinal alanlar
`fish`, `bucket`, `conditions` (seasons eklenmiş haliyle), `display_data`,
`journal_profile`, `modifiers`, `selection_weight`, `selection_quality`,
`size`, `speed`, `strength`, `associated_mods` — orijinalde olan ne varsa
aynen yazılır; sadece `parent` kaldırılır ve `conditions`'a seasons eklenir.

## 7. Örnek çıktı

Orijinal `hybrid_aquatic/fishing/fish/saltwater/lionfish.json`
(preferred_temperature = 0.8 → sıcak → winter dışarı):

```json
{
  "conditions": [
    { "type": "tide:dimension", "dimensions": ["minecraft:overworld"] },
    { "type": "tide:fluid", "fluid": "water" },
    { "type": "tide:above", "y": 40 },
    { "type": "tide:saltwater" },
    { "type": "tide:seasons", "seasons": ["spring", "summer", "fall"] }
  ],
  "display_data": { "entity": "hybrid_aquatic:lionfish", "roll": -90.0, "x": 0.1, "y": -0.2, "z": 0.08 },
  "fish": "hybrid_aquatic:lionfish",
  "journal_profile": { "description": "journal.description.hybrid_aquatic.lionfish", "group": "saltwater", "location": "journal.info.location.saltwater", "rarity": "uncommon" },
  "modifiers": [ { "type": "tide:temperature", "preferred_temperature": 0.8, "temperature_tolerance": 0.7 } ],
  "selection_weight": 25.0,
  "size": { "record_high_cm": 40.0, "typical_high_cm": 23.0, "typical_low_cm": 10.0 },
  "speed": 1.25,
  "strength": 0.45
}
```

Nötr balık örneği (sıcaklık yok, hash → fall dışarı):
`"seasons": ["spring", "summer", "winter"]`

## 8. Doğrulama adımları (uygulamadan sonra)

1. Oyunu tam yeniden başlat.
2. `logs/kubejs/` altında script hataları olmadığını kontrol et.
3. Tide komutu `/fishing test loot` ile mevcut mevsimde balık dağılımını incele.
4. `/season set early_winter` (vb.) ile mevsimi değiştir, kışlık balıkların
   (cold → winter dahil) çıktığını, yazlık balıkların (hot → winter dışı)
   çıkmadığını doğrula.
5. Journal'da (Tide fishing journal) balıkların mevsim bilgilerinin güncellendiğine bak.

## 9. Geri alma

Üretilen tüm dosyalar `kubejs/data/<namespace>/fishing/fish/...` altındadır.
Geri almak için:
- Yalnızca bu planla üretilen dosyaları sil (manifest'ten liste gelir), veya
- `kubejs/data` altındaki `fishing/fish` override dosyalarını toplu silip
  orijinal mod jar'larındaki datalara dön.

Üretimden önce mevcut `kubejs/data` içeriği yedeği alınacak (script
`kubejs/data/_backup_fishing_<tarih>/` oluşturacak).

## 10. Riskler & notlar

- **Boş mevsim riski:** Her balık 1 mevsim dışarı → her mevsimde ~%75 balık
  kalır; denge güvenli. Yine de script, manifest'te mevsim bazında balık
  sayısı özeti verecek (her mevsimde her kategoride en az N balık var mı).
- **Lava/void/underground balıkları** kapsamda değil → yıl boyu kalır,
  mevsim değişse de avlanmaya devam eder.
- **Alex's Mobs blobfish** Tide tarafında `saltwater` kategorisinde → yüzey
  sayılır ve mevsimsel yapılır (biyolojik olarak derin deniz olsa da Tide'in
  kategorizasyonuna uyulur).
- **Dedup etkileşimi:** `loot_deduplication.js` yakalanan balığı örn.
  `hybrid_aquatic:tuna` → `aquaculture:tuna` çevirir. Tide fish datası
  hangi balığın avlanabilir olduğunu belirler; LootJS ise avlanan öğeyi
  birleştirilmiş öğeye çevirir. Mevsim kapısı avlanabilirlik aşamasında
  çalıştığı için dedup ile çelişmez.
- **Tide sürüm güncellemesi** fish datalarını değiştirirse override'lar
  bayatlayabilir; script tekrar çalıştırılarak yenilenir.

## 11. Onay sonrası adımlar

1. Bu planı kullanıcı onaylar.
2. Üretici PowerShell script `generate_seasonal_fish.ps1` olarak yazılır
   (örnek kök: instance klasörü, oyun verisi dışında).
3. Script çalıştırılır → `kubejs/data` altına override dosyaları + manifest
   + backup üretilir.
4. Manifest gözden geçirilir (özellikle mevsim bazında balık sayısı dengesi).
5. Oyun yeniden başlatılır, Bölüm 8 doğrulaması yapılır.
