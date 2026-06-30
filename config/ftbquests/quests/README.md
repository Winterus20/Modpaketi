# FTB Quests — AI Düzenleme Kuralları

> **Tüm standartlar için → `.agents/AGENTS.md` okuyun.**
> Aşağıdaki kurallar AGENTS.md ile çelişirse AGENTS.md geçerlidir.

## Kısa özet

1. **Generator bölümleri:** Python dosyasını düzenle (`tools/chapters/*.py`) → `python tools/generate_quests.py` çalıştır. SNBT'yi elle düzenleme.
2. **`aricilik_sanati`:** Statik SNBT — doğrudan `.snbt` + lang dosyalarından düzenle. Generator çalıştırma.
3. **Script adlandırma:** Patch scriptleri açık isimlendir: `patch_beekeeping_quests.py` ✓, `fix.py` ✗

Detaylar ve format standartları → `.agents/AGENTS.md` §3
