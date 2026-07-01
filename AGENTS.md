---
description: Harbor Haven modpack — tüm AI geliştirme standartları (her oturumda geçerli)
alwaysApply: true
---

# Harbor Haven Modpack — AI Geliştirme Standartları

Bu dosya, Harbor Haven modpack üzerinde çalışan tüm yapay zeka asistanları için **tek otorite kaynağıdır**.
Önce burayı oku, sonra değişiklik yap. `README.md` vizyon ve mimari için; bu dosya **nasıl yapılacağını** tanımlar.

---

## 0. Hızlı özet

| Konu | Kural |
|------|-------|
| Vizyon | Cozy farm-life sim (Stardew / Sun Haven); balıkçılık omurga ama tek tema değil |
| Oyuncu dili | Türkçe birincil; İngilizce çeviri zorunlu ama TR kalitesi öncelikli |
| Kod dili | İngilizce (değişkenler, yorumlar, commit mesajları) |
| Oyuncu modu | Tek oyuncu birincil; arkadaşlarla coop uyumlu |
| Quest referansı | `yeni_bir_baslangic` — altın standart bölüm |
| Quest düzenleme | Hibrit: çoğu bölüm `tools/chapters/*.py` → generator; `aricilik_sanati` statik SNBT |
| Bölüm ilerlemesi | Yumuşak linear — sıra önerilir, sert kilit yok |
| Faz önceliği | Sabit yok — her oturumda kullanıcıya sor |
| Config | Gerekirse tüm `config/` düzenlenebilir |
| Performans config | Sadece crash/performans sorunu çözerken |
| Patchouli | Kaldırılacak (mod + dosyalar); FTB Quests tek rehber |
| Mod ekleme | Önerebilirsin; ekleme/çıkarma için kullanıcı onayı şart |
| Commit | Otomatik commit yapma; mantıklı parçalar halinde öner, kullanıcı onaylasın |
| Test notu | Yazma; kullanıcı istemedikçe |
| Dokümantasyon | Bu dosya birincil; `README.md` vizyon/mimari |

---

## 1. Proje bağlamı

- **Minecraft 1.20.1 · Forge 47.4.10**
- **Faz durumu:** Faz 1 ✅; Faz 2–3 kısmen; Faz 5 (FTB Quests) aktif geliştirmede
- **Omurga sistemler:** Serene Seasons, Tide (balıkçılık), KubeJS (entegrasyon), dedup (kanonik eşya)
- **Instance adı:** **Harbor Haven** (Prism Launcher: `HarborHaven`)

Detaylı mimari → `README.md`

---

## 2. Dosya ve iş akışı kuralları

### 2.1 Generator-first (tercih edilen yol)

Aşağıdakiler için **elle dosya düzenleme yerine generator kullan**:

| Ne | Kaynak | Komut |
|----|--------|-------|
| FTB Quests (çoğu bölüm) | `tools/chapters/*.py` | `python tools/generate_quests.py` |
| Dedup verisi | `tools/dedup_mappings.json` | `python tools/generate_dedup_kubejs.py` |
| Mevsimsel balık | `tools/generate_seasonal_fish.py` | script çalıştır → **tam oyun restart** |

**Asla elle düzenleme:**
- `kubejs/startup_scripts/dedup_data.js` (üretilmiş)
- `kubejs/data/*/fishing/fish/` altındaki mevsimsel balık override'ları
- Generator bölümlerinin `.snbt` çıktıları (generator üzerine yazar)

### 2.2 Hibrit quest düzenleme

| Bölüm | Nasıl düzenlenir |
|-------|------------------|
| `tools/chapters/*.py` ile tanımlı bölümler | Python dosyasını düzenle → generator çalıştır |
| `aricilik_sanati` | Doğrudan `config/ftbquests/quests/chapters/aricilik_sanati.snbt` + lang dosyaları |

**Kritik:** `tools/generate_quests.py` asla `aricilik_sanati` bölümünü üretmez veya ezmez.

### 2.3 Yeni dosya politikası

- **OK:** `tools/chapters/`, `tools/patch_<bölüm>_<iş>.py`, `kubejs/server_scripts/`, `kubejs/data/`
- **OK:** Bölüme özel patch scriptleri — ad açık olsun: `patch_beekeeping_quests.py` ✓, `fix.py` ✗
- **Yapma:** Gereksiz README/dokümantasyon dosyası oluşturma (kullanıcı istemedikçe)
- **Yapma:** Generic isimli tek seferlik scriptler

### 2.4 Config dosyaları

- Gerekirse **tüm** `config/` dosyalarına dokunulabilir (tide, seasons, FFB, oynanış ve diğerleri)
- Değişiklik yaparken dosyanın ne işe yaradığını anla; gereksiz tweak yapma
- **Performans modları** (Embeddium, ModernFix, C2ME, FerriteCore vb.): yalnızca crash veya ciddi performans sorunu çözerken düzenle

### 2.5 Git

- Otomatik commit **yapma**
- İş bitince mantıklı commit parçaları **öner** (kullanıcı onaylasın)
- Commit mesajları İngilizce, kısa, neden odaklı
- `.gitignore` kurallarına uy; runtime/önbellek dosyalarını commit etme (bkz. kök `.gitignore`)

---

## 3. FTB Quests standartları

### 3.1 Altın standart: `yeni_bir_baslangic`

Yeni veya güncellenen her görev bu bölümle **aynı kalite seviyesine** yaklaşmalı:

- Çeviri anahtarları (`kubejs.ftbquests.quest.<bölüm>.<key>.*`)
- TR metin sıcak ve rehberlik edici
- Mod ve eşya adları renklendirilmiş
- Anlamlı `shape` kullanımı (aşağıdaki tablo)
- Subtitle **opsiyonel** — sadece özel / milestone görevlerde

### 3.2 Açıklama metni şablonu

Her görev açıklaması şu yapıyı izler:

1. **Paragraf 1 (zorunlu):** Ne yapılacak + neden önemli (1–3 cümle)
2. **Paragraf 2 (opsiyonel):** İpucu, mod etkileşimi veya sıradaki adım

**Örnek (TR):**
```
Bu mod paketinin kalbi &bTide&r modu ile yönlendirilen balıkçılıktır.
Temel bir &eAhşap Olta&r yaparak macerana başla.

&7İpucu:&r Farklı balıklar mevsime, biyoma ve derinliğe göre değişir.
```

### 3.3 Renk kodları (standart palet)

Minecraft legacy formatı (`&` kodları). Her renkli segmentten sonra `&r` ile sıfırla.

| Kod | Kullanım |
|-----|----------|
| `&6` | Modpack öğeleri: Görev Kitabı, marka kavramlar |
| `&e` | Hedef eşya / craft hedefi / blok adı |
| `&a` | Olumlu ipuçları, keşif araçları, doğa |
| `&b` | Balıkçılık, su, Tide ile ilgili |
| `&d` | Cozy/dekoratif modlar (Let's Do, Sophisticated Backpacks) |
| `&c` | Uyarılar, Spice of Life, tehlike |
| `&9` | Ulaşım (Waystones vb.) |
| `&7` | İkincil ipucu satırı başlangıcı ("İpucu:") |

**Kurallar:**
- Mod adını ilk geçtiği yerde renklendir
- Hedef eşyayı `&e` ile vurgula
- Her görevde en az bir renk vurgusu olsun (düz duvar metin yazma)
- Raw JSON text kullanma; `&` kodları yeterli ve generator ile uyumlu

### 3.4 Subtitle (alt başlık)

- **Zorunlu değil**
- Kullan: bölüm açılışı, bölüm finali, önemli milestone, çok adımlı sistem girişi
- Kullanma: rutin craft/hasat ara görevleri
- Stil: kısa, şiirsel veya tematik (2–5 kelime). Örnek: `"Doğanın Ritmi"`, `"İlk Olta"`

### 3.5 Shape (görev şekli) — anlamlı eşleştirme

Varsayılan: `circle` (belirtilmezse). Shape boş yere kullanma.

| Shape | Ne zaman |
|-------|----------|
| `heart` | Hoş geldin, bölüm girişi |
| `diamond` | Balıkçılık, değerli hasat, milestone ödülü |
| `gear` | Craft, makine, mutfak, otomasyon |
| `hexagon` | Keşif, ışınlanma, mağara, uzak hedef |
| `rsphere` | Tarım, tohum, toprak, doğa |
| `octagon` | Hayvan / pet / arıcılık |
| `pentagon` | Köy / sosyal / pazar |
| `star` | Bölüm tamamlama (finale) |

`size`: sadece özel görevlerde (`1.25`–`1.5`); her görevde büyütme.

### 3.6 Ödüller

- **Tematik:** görevle ilgili eşya ver (balık görevi → yem, tarım → tohum)
- **Miktar:** abartma — oyunu bozacak kadar verme

| Aşama | Tipik ödül |
|-------|------------|
| Erken | 1–8 temel kaynak veya 1–4 orta eşya |
| Orta | küçük yığın + 1 araç veya tohum paketi |
| Milestone | 1 özel eşya + küçük destek yığını |
| Asla | Erken görevde nadir blokların tam yığını, üst seviye araç seti |

### 3.7 Görev grafiği (layout)

- Grid: `x` / `y` adımları çoğunlukla `1.5` birim
- Bölüm girişi: `(0, 0)`
- Bağımlılıklar: `dependency` (tek) veya `dependencies` (çoklu)
- `dependency_or` + `one_completed`: alternatif yollar için
- ID'leri elle değiştirme — generator `gen_id()` ile üretir; statik bölümde mevcut ID'leri koru

### 3.7b Bölümler arası ilerleme

- **Yumuşak linear:** `order_index` bölüm sırasını önerir; oyuncuya rehberlik eder
- Bölümler arası **sert kilit** koyma (bir bölüm bitmeden diğeri açılmasın — yapma)
- Bölüm içi `dependency` zincirleri normal şekilde kullanılır

### 3.7c Quest key / ID politikası

- Paket henüz yayınlanmadı — geliştirme aşamasında quest `key` değiştirilebilir
- Key değişince generator yeni ID üretir; mevcut test dünyasında ilerleme sıfırlanabilir (kabul edilebilir)
- Yayın sonrası key/ID değişikliği kullanıcıya sorulmalı

### 3.7d Task tipleri

- **Tematik kullan:** `item`, `checkmark`, `advancement`, `kill`, `dimension`, `fluid` vb. — görevin konusuna uyuyorsa
- Gereksiz kill quest veya anlamsız task tipi ekleme
- Yeni mod veya kritik ödül eklerken eşyanın varlığını doğrula (`tools/scan_mod_items.py` veya mod listesi)

### 3.7e Mod adları metinde

- **Mod adı İngilizce** kalır: `&dFarmer's Delight&r`, `&bTide&r
- Açıklama ve rehberlik metni **Türkçe**
- Registry ID'leri (`farmersdelight:cooking_pot`) oyuncuya gösterilmez — JEI'deki okunabilir ad kullanılır

### 3.7f Gizli görevler

- `hide: true` **kullanma** — tüm görevler görünür olsun
- Easter egg veya endgame sırı gerekirse kullanıcıya sor

### 3.7g `aricilik_sanati` lang anahtarları (refactor)

- **Hedef:** lang anahtarları `aricilik_ve_dostlar.*` → `aricilik_sanati.*` ile uyumlu hale getirilsin
- SNBT dosya adı: `aricilik_sanati.snbt` (değişmez)
- Refactor: SNBT title/description referansları + lang dosyaları birlikte güncellenir
- Quest ID'leri (`id:` alanı) mümkünse korunur — sadece lang key stringleri değişir

### 3.8 Çeviri anahtarları

```
kubejs.ftbquests.chapter.<filename>.title
kubejs.ftbquests.quest.<filename>.<key>.title
kubejs.ftbquests.quest.<filename>.<key>.subtitle   (opsiyonel)
kubejs.ftbquests.quest.<filename>.<key>.desc.<n>   (n = 0, 1, ...)
```

- TR: birincil, doğal, cozy ton
- EN: tam çeviri; placeholder veya Google Translate kalitesinde bırakma
- Generator çalıştırınca lang dosyalarına **merge** eder; mevcut anahtarları silmez

### 3.9 Bölüm tonları

Her bölümün kendi sesi var; `yeni_bir_baslangic` sıcaklığını koru ama temaya uy:

| Bölüm | Ton |
|-------|-----|
| `yeni_bir_baslangic` | Sıcak karşılama, rehber |
| `toprak_ana_ve_hasat_zamani` | Sabırlı öğretmen, toprak ve mevsim |
| `mutfak_sanatlari_ve_gastronomi` | Heyecanlı şef, lezzet odaklı |
| `baliki_ve_deniz` | Maceracı balıkçı |
| `kumes_ve_agil_gunlukleri` | Pastoral çiftlik günlüğü |
| `sadik_dostlar_ve_vahsi_yasam` | Dost canlısı, companion sevgisi |
| `gizemli_magaralar_ve_kesif` | Gizem ve keşif macerası |
| `kinetik_ciftlik_ve_mutfak_otomasyonu` | Mühendislik gururu, Create |
| `kendi_kasabani_kur` | Topluluk kurucu |
| `mahzen_gunlukleri_ve_bag_bozumu` | Rahat mahzen / şarap kültürü |
| `aricilik_sanati` | Nazik doğa rehberi (statik SNBT) |

---

## 4. KubeJS ve entegrasyon

### 4.1 Katmanlar

| Katman | Dizin | Ne zaman |
|--------|-------|----------|
| Startup | `kubejs/startup_scripts/` | Registry, item tanımları; çoğunlukla üretilmiş dedup |
| Server | `kubejs/server_scripts/` | Tarif, loot, event, onboarding |
| Client | `kubejs/client_scripts/` | JEI gizleme |
| Data | `kubejs/data/` | JSON override (balık, loot tabloları, trap) |

### 4.2 Yeni entegrasyon eklerken

1. Mevcut scriptlere bak — aynı deseni kullan
2. Mümkünse generator'a taşı (dedup, quest, balık gibi tekrarlayan işler)
3. Tek seferlik mantık → `server_scripts/` altında anlamlı isimle
4. Üç katmanı (startup/server/client) birbirine uyumlu tut
5. KubeJS tarif/recipe ID namespace: `harborhaven:`

---

## 5. Dedup (mükerrer eşya)

- Tek kaynak: `tools/dedup_mappings.json`
- Değişiklik yapılabilir ama **README.md'ye kısa not** ekle (ne değişti, neden)
- Generator sonrası: `dedup_data.js` + `deduplication.js` + `loot_deduplication.js` + `hide_items.js` tutarlı kalmalı
- Kanonik hub'lar: README'deki tabloya uy (FD, F&C, Aquaculture, vb.)

---

## 6. Mevsimsel balık

- **Sadece** `tools/generate_seasonal_fish.py` ile üret
- Kurallar README'de: sıcaklık → mevsim eşlemesi; `underground`, `lava`, `void` kapsam dışı
- Script sonrası tam oyun restart gerekir
- Manifest: `kubejs/data/_seasonal_fish_manifest.json`

---

## 7. Mod politikası

- Yeni mod **öner**ebilirsin (gerekçe ile)
- Mod **ekleme/çıkarma** için kullanıcı onayı **zorunlu**
- Mevcut ~57 mod listesi: `mods/` klasörü
- Habersiz mod ekleme → yasak

---

## 8. Patchouli — kaldırılacak

- **Karar:** Patchouli modu ve Köy Günlüğü (`harborhaven:field_journal`) tamamen kaldırılacak
- FTB Quests **tek** rehber sistemi
- Kaldırma kapsamı (kullanıcı onayı ile):
  - `mods/` içinden Patchouli jar
  - `kubejs/.../patchouli_books/`, `kubejs/data/harborhaven/patchouli_books/`
  - `kubejs/server_scripts/onboarding.js` içindeki Köy Günlüğü verme kodu
  - Quest metinlerindeki Köy Günlüğü referansları → Görev Kitabı'na yönlendir
- Mod kaldırma her zaman kullanıcı onayı gerektirir

---

## 8b. FFB Pazar

- `config/farmingforblockheads/MarketRegistry.json` — AI **önerebilir**, kullanıcı **onaylar**
- Şimdilik zümrüt ekonomisi yeterli; özel para birimi Faz 4'te gelecek
- Quest ödülü olarak para birimi verme; tematik eşya ödülleri tercih et
- Pazar ile quest içeriği uyumlu tutulması önerilir

---

## 8c. Faz önceliği ve kapsam dışı işler

- **Faz önceliği sabit değil** — birden fazla iş mümkünken kullanıcıya sor
- **Faz 6 (Köy & NPC):** dokunulmaz — kod, quest veya mod ekleme yok
- **README.md:** vizyon ve mimari; standart değişikliklerini bu dosyaya yaz, README'yi nadiren güncelle

---

## 9. Tutarlılık denetim listesi

Bir bölümü veya görev setini düzenledikten sonra kendine sor:

- [ ] TR metin doğal ve bölüm tonuna uygun mu?
- [ ] EN çeviri tam mı?
- [ ] Renk kodları palete uygun mu?
- [ ] Shape anlamlı mı (gereksiz shape yok mu)?
- [ ] Subtitle sadece özel görevlerde mi?
- [ ] Ödüller tematik ama abartısız mı?
- [ ] Generator bölümüyse Python'dan mı düzenledim (SNBT'den değil)?
- [ ] `aricilik_sanati` için generator çalıştırmadım mı?
- [ ] Dedup/balık değiştiyse generator çalıştırdım mı?
- [ ] Mod adları İngilizce, açıklama TR mi?
- [ ] `hide: true` kullanmadım mı?
- [ ] Config/performans değişikliği gerekçeli mi?

---

## 10. Yasaklar (Yapma)

- Generator bölümünün `.snbt` dosyasını elle düzenleyip generator'ı çalıştırmamak (değişiklik kaybolur)
- `aricilik_sanati` bölümünü generator ile ezme
- Kanonik eşyaları keyfi değiştirme (dedup notu olmadan)
- Mevsimsel balık JSON'larını elle düzenleme
- Kullanıcı onayı olmadan mod ekleme/çıkarma
- Otomatik git commit
- Gereksiz dokümantasyon dosyası üretme
- Test planı yazma (kullanıcı istemedikçe)
- `hide: true` ile gizli görev (kullanıcı istemedikçe)

---

## 11. Mevcut bölüm envanteri

| Dosya | Kaynak | Order |
|-------|--------|-------|
| `yeni_bir_baslangic` | generator | 0 |
| `toprak_ana_ve_hasat_zamani` | generator | 1 |
| `aricilik_sanati` | **statik SNBT** | 3 |
| `baliki_ve_deniz` | generator | — |
| `mutfak_sanatlari_ve_gastronomi` | generator | — |
| `sadik_dostlar_ve_vahsi_yasam` | generator | — |
| `kinetik_ciftlik_ve_mutfak_otomasyonu` | generator | — |
| `kendi_kasabani_kur` | generator | — |
| `gizemli_magaralar_ve_kesif` | generator | — |
| `mahzen_gunlukleri_ve_bag_bozumu` | generator | — |
| `kumes_ve_agil_gunlukleri` | generator | — |

**Öncelikli tutarlılık işi:** Eksik bölümlere renk/shape/subtitle → `yeni_bir_baslangic` standardı

---

## 12. Planlanan işler

| İş | Durum | Not |
|----|-------|-----|
| Quest bölüm tutarlılığı | Bekliyor | Eksik bölümlere renk/shape/subtitle |
| `aricilik_sanati` lang refactor | Bekliyor | `aricilik_ve_dostlar.*` → `aricilik_sanati.*` |
| Patchouli kaldırma | Kısmen | KubeJS dosyaları + onboarding yapıldı; mod jar bekliyor (kullanıcı onayı) |
| `.gitignore` genişletme | ✅ Bitti | runtime/önbellek dizinleri + kişisel scriptler eklendi |

---

## 13. Karar özeti

| # | Konu | Karar |
|---|------|-------|
| 1 | Config | Tüm config düzenlenebilir |
| 2 | Performans config | Sadece crash/perf sorunu çözerken |
| 3 | Gitignore | Genişlet (modernfix cache vb.) |
| 4 | Patchouli | Tamamen kaldırılacak |
| 5 | Arıcılık isimleri | Lang key refactor (`aricilik_ve_dostlar` → `aricilik_sanati`) |
| 6 | Bölüm ilerlemesi | Yumuşak linear |
| 7 | Quest key | Geliştirmede değişebilir |
| 8 | Faz önceliği | Her oturumda kullanıcıya sor |
| 9 | Task tipleri | Tematik kullan |
| 10 | Eşya doğrulama | Kritik eklemelerde |
| 11 | Mod adları | EN mod adı, TR açıklama |
| 12 | Oyuncu modu | Tek oyuncu birincil + coop uyumlu |
| 13 | FFB pazar | AI önerir, kullanıcı onaylar |
| 14 | Ekonomi | Zümrüt yeterli, Faz 4'te özel para |
| 15 | Faz 6 NPC | Dokunulmaz |
| 16 | Bölüm sonu ödül | Son görev milestone |
| 17 | Gizli görev | Kullanma |
| 18 | README | Bu dosya birincil; README vizyon/mimari |

---

*Son güncelleme: 2026-07-01. Değişiklik önerileri kullanıcıya sorulmalı.*
