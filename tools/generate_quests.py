import os
import json
import hashlib

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
        parts.append(f"{tab}]")
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

# Define quest chapters
chapters_data = [
    {
        "filename": "macera_basi",
        "title_en": "Adventure Begins",
        "title_tr": "Macera Başlıyor",
        "icon": "minecraft:grass_block",
        "quests": [
            {
                "key": "welcome",
                "x": 0.0,
                "y": 0.0,
                "title_en": "Welcome to Balik!",
                "title_tr": "Balık Mod Paketine Hoş Geldiniz!",
                "desc_en": ["Welcome to your new life! This modpack is focused on agriculture, animal husbandry, beekeeping, custom engineering, and exploration. Open your Quest Book to guide your journey. Let's start with basic survival."],
                "desc_tr": ["Yeni hayatınıza hoş geldiniz! Bu mod paketi tarım, hayvancılık, arıcılık, özel mühendislik ve keşif odaklıdır. Yolculuğunuza rehberlik etmesi için görev kitabınızı açın. Temel hayatta kalma ile başlayalım."],
                "tasks": [{"type": "checkmark"}],
                "rewards": [{"type": "item", "item": "minecraft:bread", "count": 5}]
            },
            {
                "key": "seasons",
                "x": 0.0,
                "y": 2.0,
                "dependency": "welcome",
                "title_en": "Changing Seasons",
                "title_tr": "Değişen Mevsimler",
                "desc_en": ["Serene Seasons alters crop fertility and temperature over time. Crops only grow in their fertile seasons, and winters can be freezing! Craft a Calendar to keep track of time and plan your harvests. A Season Sensor can also emit a redstone signal when a chosen season arrives, great for automating greenhouses."],
                "desc_tr": ["Serene Seasons mevsimleri, bitkilerin verimliliğini ve sıcaklığı zamanla değiştirir. Ekinler sadece verimli oldukları mevsimlerde büyür ve kışlar dondurucu olabilir! Zamanı takip etmek ve hasatlarınızı planlamak için bir Takvim yapın. Bir Mevsim Sensörü (Season Sensor) seçtiğiniz mevsim geldiğinde redstone sinyali verir; seraları otomatikleştirmek için harikadır."],
                "tasks": [{"type": "item", "item": "sereneseasons:calendar"}],
                "rewards": [{"type": "item", "item": "sereneseasons:season_sensor"}]
            },
            {
                "key": "sol_carrot",
                "x": 1.5,
                "y": 1.0,
                "dependency": "welcome",
                "title_en": "A Diverse Diet",
                "title_tr": "Çeşitli Beslenme",
                "desc_en": ["Spice of Life (Carrot Edition) rewards you for eating unique foods. Eating new kinds of food grants permanent extra hearts! Collect and eat different foods to increase your max health. Start by gathering these basic foods."],
                "desc_tr": ["Spice of Life (Carrot Edition) sizi benzersiz yiyecekler yediğiniz için ödüllendirir. Yeni yiyecek türleri yemek kalıcı ekstra kalp kazandırır! Maksimum sağlığınızı artırmak için farklı yiyecekleri toplayın ve yiyin. Bu temel yiyecekleri toplayarak başlayın."],
                "tasks": [
                    {"type": "item", "item": "minecraft:apple"},
                    {"type": "item", "item": "minecraft:sweet_berries"},
                    {"type": "item", "item": "minecraft:carrot"}
                ],
                "rewards": [{"type": "item", "item": "minecraft:golden_carrot", "count": 4}]
            },
            {
                "key": "backpack",
                "x": -1.5,
                "y": 1.0,
                "dependency": "welcome",
                "title_en": "Portable Storage",
                "title_tr": "Taşınabilir Depolama",
                "desc_en": ["Sophisticated Backpacks are highly customizable, upgradable backpack items that you can wear or place. Craft a basic Leather Backpack to ease your inventory management during exploration."],
                "desc_tr": ["Sophisticated Backpacks, giyebileceğiniz veya yerleştirebileceğiniz, son derece özelleştirilebilir ve geliştirilebilir sırt çantalarıdır. Keşif sırasında envanter yönetiminizi kolaylaştırmak için temel bir Deri Sırt Çantası yapın."],
                "tasks": [{"type": "item", "item": "sophisticatedbackpacks:backpack"}],
                "rewards": [
                    {"type": "item", "item": "minecraft:leather", "count": 4},
                    {"type": "item", "item": "minecraft:string", "count": 4}
                ]
            },
            {
                "key": "sleeping_bag",
                "x": 0.0,
                "y": -2.0,
                "dependency": "welcome",
                "title_en": "Sweet Dreams on the Go",
                "title_tr": "Yolda Tatlı Rüyalar",
                "desc_en": ["Comforts sleeping bags allow you to sleep through the night without resetting your spawn point. Perfect for long journeys across the world!"],
                "desc_tr": ["Comforts uyku tulumları, doğma noktanızı sıfırlamadan geceyi uyuyarak geçirmenizi sağlar. Dünya genelindeki uzun yolculuklar için mükemmeldir!"],
                "tasks": [{"type": "item", "item": "comforts:sleeping_bag_white"}],
                "rewards": [{"type": "item", "item": "minecraft:white_wool", "count": 2}]
            },
            {
                "key": "compasses",
                "x": -1.5,
                "y": -1.0,
                "dependency": "welcome",
                "title_en": "Navigating Nature",
                "title_tr": "Doğada Yol Bulmak",
                "desc_en": ["Nature's Compass and Explorer's Compass are vital tools for finding biomes and structures in this vast world. Craft either compass to help guide your exploration."],
                "desc_tr": ["Nature's Compass (Doğa Pusulası) ve Explorer's Compass (Kaşif Pusulası), bu engin dünyadaki biyomları ve yapıları bulmak için hayati araçlardır. Keşfinize rehberlik etmesi için iki pusuladan birini yapın."],
                "tasks": [
                    {"type": "item", "item": "naturescompass:naturescompass"}
                ],
                "rewards": [{"type": "item", "item": "minecraft:ender_pearl", "count": 2}]
            },
            {
                "key": "waystone",
                "x": 1.5,
                "y": -1.0,
                "dependency": "welcome",
                "title_en": "Fast Travel",
                "title_tr": "Hızlı Yolculuk",
                "desc_en": ["Waystones let you teleport between any waystones you have activated, for a small emerald fee. Craft a Waystone, place it at your base, and activate it by right-clicking. Carry a Return Scroll to warp home from anywhere."],
                "desc_tr": ["Waystone'lar (Yol Taşları), küçük bir zümrüt karşılığında etkinleştirdiğiniz tüm yol taşları arasında ışınlanmanızı sağlar. Bir Yol Taşı yapın, üssünüze yerleştirin ve sağ tıklayarak etkinleştirin. Her yerden eve dönmek için bir Dönüş Parşömeni (Return Scroll) taşıyın."],
                "tasks": [{"type": "item", "item": "waystones:waystone"}],
                "rewards": [{"type": "item", "item": "waystones:return_scroll", "count": 3}]
            },
            {
                "key": "market",
                "x": -1.5,
                "y": -3.0,
                "dependency": "welcome",
                "title_en": "The Trading Market",
                "title_tr": "Ticaret Pazarı",
                "desc_en": ["Farming for Blockheads adds a Market where you can trade emeralds for seeds, saplings, and other farming supplies you may be missing. Craft a Market and place it down to browse all the seeds the modpack has to offer."],
                "desc_tr": ["Farming for Blockheads, zümrüt karşılığında eksik olduğunuz tohumlar, fidanlar ve diğer çiftlik malzemelerini takas edebileceğiniz bir Pazar (Market) ekler. Mod paketindeki tüm tohumlara göz atmak için bir Pazar yapıp yerleştirin."],
                "tasks": [{"type": "item", "item": "farmingforblockheads:market"}],
                "rewards": [
                    {"type": "item", "item": "minecraft:wheat_seeds", "count": 8},
                    {"type": "item", "item": "minecraft:emerald", "count": 2}
                ]
            }
        ]
    },
    {
        "filename": "ciftcilik_ve_gastronomi",
        "title_en": "Farming & Gastronomy",
        "title_tr": "Toprak Ana ve Lezzet Dünyası",
        "icon": "farmersdelight:cooking_pot",
        "quests": [
            {
                "key": "chef_knife",
                "x": 0.0,
                "y": 0.0,
                "title_en": "A Chef's First Tool",
                "title_tr": "Bir Şefin İlk Aleti",
                "desc_en": ["Knives from Farmer's Delight are crucial for clean harvesting. Use them to get straw from wild grass, and to get clean meat cuts from animals. Craft a Flint Knife to start."],
                "desc_tr": ["Farmer's Delight bıçakları, temiz hasat için çok önemlidir. Onları yabani otlardan saman elde etmek ve hayvanlardan temiz et kesimleri almak için kullanın. Başlamak için bir Çakmaktaşı Bıçak yapın."],
                "tasks": [{"type": "item", "item": "farmersdelight:flint_knife"}],
                "rewards": [{"type": "item", "item": "farmersdelight:tomato_seeds", "count": 5}]
            },
            {
                "key": "cooking_pot",
                "x": 0.0,
                "y": 2.0,
                "dependency": "chef_knife",
                "title_en": "Hot Pots",
                "title_tr": "Sıcak Tencereler",
                "desc_en": ["The Cooking Pot is the core of Farmer's Delight. Place it on a heat source (like a Stove or Campfire) to prepare delicious, nourishing meals that provide long-lasting health regeneration and hunger satisfaction."],
                "desc_tr": ["Cooking Pot (Tencere), Farmer's Delight modunun merkezidir. Uzun süreli sağlık yenilenmesi ve açlık doygunluğu sağlayan lezzetli, besleyici yemekler hazırlamak için onu bir ısı kaynağının (Ocak veya Kamp Ateşi gibi) üzerine yerleştirin."],
                "tasks": [
                    {"type": "item", "item": "farmersdelight:cooking_pot"},
                    {"type": "item", "item": "farmersdelight:stove"}
                ],
                "rewards": [
                    {"type": "item", "item": "minecraft:bowl", "count": 4},
                    {"type": "item", "item": "farmersdelight:onion", "count": 2}
                ]
            },
            {
                "key": "baking_tray",
                "x": -1.5,
                "y": 1.0,
                "dependency": "chef_knife",
                "title_en": "Bakery Apprentice",
                "title_tr": "Fırıncı Çırağı",
                "desc_en": ["Let's Do Bakery introduces pastries, bread, and cakes. Place dough on a Tray and bake it in the oven. Bread making has never been this rewarding!"],
                "desc_tr": ["Let's Do Bakery; hamur işleri, ekmekler ve kekler sunar. Hamuru bir Tepsiye (Tray) yerleştirin ve fırında pişirin. Ekmek yapmak hiç bu kadar ödüllendirici olmamıştı!"],
                "tasks": [{"type": "item", "item": "bakery:tray"}],
                "rewards": [
                    {"type": "item", "item": "minecraft:wheat", "count": 8},
                    {"type": "item", "item": "minecraft:sugar", "count": 4}
                ]
            },
            {
                "key": "winery",
                "x": 1.5,
                "y": 1.0,
                "dependency": "chef_knife",
                "title_en": "The Art of Winemaking",
                "title_tr": "Şarapçılık Sanatı",
                "desc_en": ["Let's Do Vinery introduces grape cultivation and winemaking. Collect grapes, press them in a juicer, and ferment them in barrels. Aged wines offer unique, helpful effects."],
                "desc_tr": ["Let's Do Vinery, üzüm yetiştiriciliği ve şarap yapımını sunar. Üzümleri toplayın, sıkacakta sıkın ve varillerde fermente edin. Yıllandırılmış şaraplar benzersiz ve yararlı etkiler sunar."],
                "tasks": [{"type": "item", "item": "vinery:red_grape"}],
                "rewards": [
                    {"type": "item", "item": "vinery:grapevine_stem", "count": 1},
                    {"type": "item", "item": "vinery:wine_bottle", "count": 2}
                ]
            },
            {
                "key": "ultimate_feast",
                "x": 0.0,
                "y": 4.0,
                "dependency": "cooking_pot",
                "title_en": "The Grand Feast",
                "title_tr": "Büyük Ziyafet",
                "desc_en": ["Prepare a full Roast Chicken Feast. Feasts are blocks that can be placed down and eaten multiple times by players, providing massive nourishment and status effects. A true master chef's achievement!"],
                "desc_tr": ["Bütün bir Tavuk Kızartması Ziyafeti (Roast Chicken Feast) hazırlayın. Ziyafetler, yere yerleştirilebilen ve oyuncular tarafından birden fazla kez yenerek büyük miktarda besin ve durum etkisi sağlayan bloklardır. Gerçek bir usta şefin başarısı!"],
                "tasks": [{"type": "item", "item": "farmersdelight:roast_chicken_block"}],
                "rewards": [
                    {"type": "item", "item": "minecraft:golden_apple", "count": 1},
                    {"type": "item", "item": "minecraft:diamond", "count": 1}
                ]
            },
            {
                "key": "sprinkler",
                "x": -1.5,
                "y": 3.0,
                "dependency": "cooking_pot",
                "title_en": "Automated Irrigation",
                "title_tr": "Otomatik Sulama",
                "desc_en": ["Let's Do: Farm & Charm adds a Water Sprinkler that hydrates and accelerates nearby crops. Place it above a water source and watch your fields grow faster, even out of season with the right setup."],
                "desc_tr": ["Let's Do: Farm & Charm, yakındaki ekinleri sularak ve büyütmeyi hızlandıran bir Su Serpme (Water Sprinkler) ekler. Bir su kaynağının üzerine yerleştirin ve doğru kurulumla mevsim dışı bile olsa tarlanızın daha hızlı büyümesini izleyin."],
                "tasks": [{"type": "item", "item": "farm_and_charm:water_sprinkler"}],
                "rewards": [{"type": "item", "item": "farm_and_charm:fertilizer", "count": 4}]
            },
            {
                "key": "tea_time",
                "x": 1.5,
                "y": 3.0,
                "dependency": "cooking_pot",
                "title_en": "Tea Time",
                "title_tr": "Çay Saati",
                "desc_en": ["Farmer's Respite brings tea and coffee culture. Craft a Kettle, brew it on a heat source, and pour yourself a cup of Green Tea for gentle, long-lasting effects. Strong and Long brews last even longer."],
                "desc_tr": ["Farmer's Respite, çay ve kahve kültürünü getirir. Bir Çaydanlık (Kettle) yapın, bir ısı kaynağında demleyin ve hafif, uzun süreli etkiler için kendinize bir fincan Yeşil Çay doldurun. Güçlü (Strong) ve Uzun (Long) demlemeler daha da uzun sürer."],
                "tasks": [{"type": "item", "item": "farmersrespite:kettle"}],
                "rewards": [{"type": "item", "item": "farmersrespite:green_tea", "count": 4}]
            },
            {
                "key": "candlelight_dinner",
                "x": 0.0,
                "y": 6.0,
                "dependency": "ultimate_feast",
                "title_en": "A Candlelight Dinner",
                "title_tr": "Mum Işığında Akşam Yemeği",
                "desc_en": ["Let's Do: Candlelight turns dining into a romantic experience. Set a Hearth, lay out a fine table, and prepare a dish like Beef Wellington or Salmon on White Wine. Fine dining for you and your companions!"],
                "desc_tr": ["Let's Do: Candlelight, yemek yemeyi romantik bir deneyime dönüştürür. bir Şömine (Hearth) kurun, şık bir masa hazırlayın ve Dana Wellington veya Beyaz Şaraplı Somon gibi bir yemek pişirin. Siz ve dostlarınız için şık bir akşam yemeği!"],
                "tasks": [{"type": "item", "item": "candlelight:hearth"}],
                "rewards": [{"type": "item", "item": "candlelight:wine_glass", "count": 2}]
            },
            {
                "key": "corn_delight",
                "x": -3.0,
                "y": 1.0,
                "dependency": "chef_knife",
                "title_en": "Corn Delight",
                "title_tr": "Mısır Ziyafeti",
                "desc_en": ["Corn Delight adds tall corn crops and a harvest of tasty recipes. Plant Corn Seeds, grow them into towering stalks, and craft comforting Cornbread or a warm Bowl of Corn Soup."],
                "desc_tr": ["Corn Delight, uzun mısır ekinleri ve lezzetli tarifler ekler. Mısır Tohumu ekin, onları kule gibi boylu saplara büyütün ve doyurucu Mısır Ekmeği (Cornbread) veya sıcak bir kase Mısır Çorbası yapın."],
                "tasks": [{"type": "item", "item": "corn_delight:corn_seeds"}],
                "rewards": [{"type": "item", "item": "corn_delight:cornbread", "count": 4}]
            }
        ]
    },
    {
        "filename": "aricilik_ve_dostlar",
        "title_en": "Beekeeping & Companions",
        "title_tr": "Arıcılık ve Doğa Dostları",
        "icon": "productivebees:advanced_oak_beehive",
        "quests": [
            {
                "key": "bees_intro",
                "x": 0.0,
                "y": 0.0,
                "title_en": "Modern Beekeeping",
                "title_tr": "Modern Arıcılık",
                "desc_en": ["Productive Bees builds on vanilla bees. While exploring you will find solitary bees living in hidden nests (e.g. an Oak Wood Nest) around the world. Solitary bees do not produce resources, but their genetics are used for breeding. Craft an Oak Wood Nest, place it in the right biome, and prime it with a Honey Treat to attract a wild solitary bee and start your apiary."],
                "desc_tr": ["Productive Bees, vanilya arılarının üzerine kuruludur. Keşif yaparken dünyanın çeşitli biyomlarındaki gizli yuvalarda (ör. Meşe Odunu Yuvası) yaşayan münzevi arılar bulacaksınız. Münzevi arılar kaynak üretmez, ancak genetikleri ıslah için kullanılır. Bir Meşe Odunu Yuvası yapın, doğru biyoma yerleştirin ve yabani bir münzevi arı çekmek için bir Bal Ödülü (Honey Treat) ile hazırlayın. Böylece arılığınızı kurun."],
                "tasks": [{"type": "item", "item": "productivebees:oak_wood_nest"}],
                "rewards": [
                    {"type": "item", "item": "minecraft:oak_log", "count": 4},
                    {"type": "item", "item": "minecraft:honeycomb", "count": 2}
                ]
            },
            {
                "key": "honey_treat",
                "x": -1.5,
                "y": 1.0,
                "dependency": "bees_intro",
                "title_en": "Sweeten the Deal",
                "title_tr": "Tatlı Bir Teklif",
                "desc_en": ["Honey Treats are the currency of beekeeping. Use them to prime artificial solitary nests (each extra treat speeds up attraction), to breed solitary bees into new species, and to lure bees into cages for transport. Craft a Honey Treat to take control of your bees."],
                "desc_tr": ["Bal Ödülleri (Honey Treat) arıcılığın para birimidir. Yapay münzevi yuvalarını hazırlamak (her ek ödül çekilişi hızlandırır), münzevi arıları yeni türlere dönüştürmek ve arıları taşımak için kafeslere çekmek için kullanılır. Arılarınızı kontrol altına almak için bir Bal Ödülü hazırlayın."],
                "tasks": [{"type": "item", "item": "productivebees:honey_treat"}],
                "rewards": [{"type": "item", "item": "productivebees:nest_locator", "count": 1}]
            },
            {
                "key": "advanced_hive",
                "x": 0.0,
                "y": 2.0,
                "dependency": "bees_intro",
                "title_en": "Industrial Apiary",
                "title_tr": "Endüstriyel Kovan",
                "desc_en": ["Advanced Beehives hold gregarious resource bees that actually produce honeycombs. Unlike vanilla hives, no smoke is needed to harvest safely. Add Expansion Boxes to fit more bees, and check JEI (press U on a bee) to see each bee's flower requirements."],
                "desc_tr": ["Gelişmiş Arı Kovanları (Advanced Beehives), gerçekten petek üreten sosyal kaynak arılarını barındırır. Vanilya kovanlarının aksine güvenli hasat için duman gerekmez. Daha fazla arı sığdırmak için Genişletme Kutuları ekleyin ve her arının çiçek gereksinimini görmek için JEI'de arıya U tuşuyla bakın."],
                "tasks": [{"type": "item", "item": "productivebees:advanced_oak_beehive"}],
                "rewards": [{"type": "item", "item": "minecraft:honey_bottle", "count": 2}]
            },
            {
                "key": "centrifuge",
                "x": 0.0,
                "y": 4.0,
                "dependency": "advanced_hive",
                "title_en": "Spinning the Honey",
                "title_tr": "Balı Süzmek",
                "desc_en": ["The Centrifuge spins honeycombs into honey bottles, wax, and resource-specific materials without breaking them. Hand-cranked to start, then upgrade to a Heated or Powered Centrifuge for automation. A crucial step for scaling bee production."],
                "desc_tr": ["Merkezkaç (Centrifuge), petekleri parçalamadan bal şişelerine, balmumuna ve kaynağa özel malzemelere dönüştürür. Başlangıçta elle çevrilir, ardından otomasyon için Isıtmalı (Heated) veya Güçlendirilmiş (Powered) Merkezkaç'a yükseltin. Arı üretimini ölçeklendirmek için çok önemli bir adım."],
                "tasks": [{"type": "item", "item": "productivebees:centrifuge"}],
                "rewards": [{"type": "item", "item": "minecraft:copper_ingot", "count": 4}]
            },
            {
                "key": "doggy_talents",
                "x": 2.5,
                "y": 0.0,
                "title_en": "Man's Best Friend",
                "title_tr": "İnsanın En İyi Dostu",
                "desc_en": ["Doggy Talents Next revamps wolves entirely. Craft Training Treats to teach your dog new skills, level them up, and assign talent points to customize their abilities."],
                "desc_tr": ["Doggy Talents Next, kurtları tamamen yeniler. Köpeğinize yeni beceriler öğretmek, seviyesini yükseltmek ve yeteneklerini özelleştirmek için Eğitim Mamaları (Training Treats) hazırlayın."],
                "tasks": [{"type": "item", "item": "doggytalents:training_treat"}],
                "rewards": [
                    {"type": "item", "item": "minecraft:clay_ball", "count": 4},
                    {"type": "item", "item": "minecraft:bone", "count": 2}
                ]
            },
            {
                "key": "dog_bed",
                "x": 2.5,
                "y": 2.0,
                "dependency": "doggy_talents",
                "title_en": "A Cozy Home",
                "title_tr": "Sıcak Bir Yuva",
                "desc_en": ["Provide your dog with a comfortable Bed to rest. Beds act as spawn points for your dogs, keeping them safe. You can also customize their collars."],
                "desc_tr": ["Köpeğinize dinlenmesi için rahat bir Yatak (Dog Bed) sağlayın. Yataklar köpekleriniz için doğma noktası görevi görerek onları güvende tutar. Tasmalarını da özelleştirebilirsiniz."],
                "tasks": [{"type": "item", "item": "doggytalents:dog_bed"}],
                "rewards": [
                    {"type": "item", "item": "minecraft:red_dye", "count": 1},
                    {"type": "item", "item": "minecraft:leather", "count": 1}
                ]
            },
            {
                "key": "pet_care",
                "x": 4.0,
                "y": 2.0,
                "dependency": "dog_bed",
                "title_en": "Pet Care",
                "title_tr": "Evcil Hayvan Bakımı",
                "desc_en": ["Domestication Innovation overhauls pet mechanics. Craft a Pet Bed as a respawn point for your pets and a Collar Tag to give them handy upgrades like a magnet or deflection shield. Keep your loyal companions safe and stylish!"],
                "desc_tr": ["Domestication Innovation, evcil hayvan mekaniğini yeniler. Evcil hayvanlarınız için bir doğma noktası olan Evcil Hayvan Yatağı (Pet Bed) ve onlara mıknatıs veya sapma kalkanı gibi kullanışlı yükseltmeler veren bir Tasma Etiketi (Collar Tag) yapın. Sadık dostlarınızı güvende ve şık tutun!"],
                "tasks": [{"type": "item", "item": "domesticationinnovation:pet_bed_red"}],
                "rewards": [{"type": "item", "item": "domesticationinnovation:collar_tag", "count": 2}]
            }
        ]
    },
    {
        "filename": "hayvancilik_reformu",
        "title_en": "Livestock Husbandry",
        "title_tr": "Hayvancılık Reformu",
        "icon": "dragnlivestock:gender_test_strip",
        "quests": [
            {
                "key": "gender_strip",
                "x": 0.0,
                "y": 0.0,
                "title_en": "Animal Genders",
                "title_tr": "Hayvan Cinsiyetleri",
                "desc_en": ["DragN's Livestock Overhaul introduces genders to animals! Animals now require both a male and female to mate. Milk and wool are also gender-restricted. Craft a Gender Test Strip to easily identify an animal's gender if you are unsure."],
                "desc_tr": ["DragN's Livestock Overhaul, hayvanlara cinsiyet getiriyor! Hayvanlar artık çiftleşmek için hem bir erkek hem de dişiye ihtiyaç duyuyor. Süt ve yün üretimi de cinsiyete göre sınırlandırılmıştır. Emin değilseniz bir hayvanın cinsiyetini kolayca belirlemek için Cinsiyet Test Şeridi hazırlayın."],
                "tasks": [{"type": "item", "item": "dragnlivestock:gender_test_strip"}],
                "rewards": [{"type": "item", "item": "dragnlivestock:gender_test_strip", "count": 4}]
            },
            {
                "key": "scissors",
                "x": -1.5,
                "y": 1.5,
                "dependency": "gender_strip",
                "title_en": "Mount Grooming",
                "title_tr": "Binek Tımarı",
                "desc_en": ["Horses' manes and tails grow over time. Use Mane Scissors and Tail Scissors to groom them, change their hairstyles, and maintain their speed and performance."],
                "desc_tr": ["Atların yeleleri ve kuyrukları zamanla büyür. Onları tımar etmek, saç stillerini değiştirmek ve hız/performanslarını korumak için Yele Makası ve Kuyruk Makası kullanın."],
                "tasks": [
                    {"type": "item", "item": "dragnlivestock:mane_scissors"}
                ],
                "rewards": [{"type": "item", "item": "dragnlivestock:tail_scissors", "count": 1}]
            },
            {
                "key": "brand_tags",
                "x": 1.5,
                "y": 1.5,
                "dependency": "gender_strip",
                "title_en": "Animal Identification",
                "title_tr": "Hayvan Kimliklendirme",
                "desc_en": ["Use color-coded Brand Tags to identify your animals. This helps manage breeding programs, dairy cattle, or sheep lineages in your farm."],
                "desc_tr": ["Hayvanlarınızı ayırt etmek için renk kodlu İşaret Etiketleri (Brand Tags) kullanın. Bu, çiftliğinizdeki damızlık programlarını, süt sığırlarını veya koyun soylarını yönetmenize yardımcı olur."],
                "tasks": [
                    {"type": "item", "item": "dragnlivestock:yellow_brand_tag"}
                ],
                "rewards": [
                    {"type": "item", "item": "minecraft:leather", "count": 2},
                    {"type": "item", "item": "minecraft:yellow_dye", "count": 1}
                ]
            },
            {
                "key": "cured_meat",
                "x": 0.0,
                "y": 2.0,
                "dependency": "gender_strip",
                "title_en": "Et Kurutma ve Salatalar",
                "title_tr": "Et Kurutma ve Salatalar",
                "desc_en": ["Process your livestock meat into thin strips and dry them into Pork Jerky or Beef Strips. You can also boil eggs to make delicious egg salads. High nutrition and long shelf life!"],
                "desc_tr": ["Hayvan etlerinizi ince şeritler halinde işleyin ve onları Domuz Eti Jerky veya Dana Şeritleri olarak kurutun. Ayrıca lezzetli yumurta salataları yapmak için yumurta kaynatabilirsiniz. Yüksek besin değeri ve uzun raf ömrü!"],
                "tasks": [
                    {"type": "item", "item": "dragnlivestock:pork_jerky"}
                ],
                "rewards": [
                    {"type": "item", "item": "dragnlivestock:pork_strips", "count": 2},
                    {"type": "item", "item": "minecraft:bowl", "count": 2}
                ]
            }
        ]
    },
    {
        "filename": "baliki_ve_deniz",
        "title_en": "Fishing & Oceans",
        "title_tr": "Derya Kuzuları ve Denizlerin Sırrı",
        "icon": "aquaculture:iron_fishing_rod",
        "quests": [
            {
                "key": "fishing_intro",
                "x": 0.0,
                "y": 0.0,
                "title_en": "Hook and Line",
                "title_tr": "İlk Olta",
                "desc_en": ["Aquaculture 2 replaces basic fishing rods with upgradable, durable metal rods. Craft an Iron Fishing Rod to catch fish from different biomes and find sunken loot crates."],
                "desc_tr": ["Aquaculture 2, temel oltaları geliştirilebilir, dayanıklı metal oltalarla değiştirir. Farklı biyomlardan balık yakalamak ve batık yağma kasaları bulmak için bir Demir Olta hazırlayın."],
                "tasks": [{"type": "item", "item": "aquaculture:iron_fishing_rod"}],
                "rewards": [{"type": "item", "item": "aquaculture:worm", "count": 8}]
            },
            {
                "key": "tackle_box",
                "x": -1.5,
                "y": 1.5,
                "dependency": "fishing_intro",
                "title_en": "The Tackle Box",
                "title_tr": "Tackle Box",
                "desc_en": ["The Tackle Box is the ultimate organizer for fishers. Use it to store your fishing rods, custom hooks, lures, lines, and bait in one convenient container."],
                "desc_tr": ["Tackle Box, balıkçılar için en gelişmiş düzenleyicidir. Oltalarınızı, özel kancalarınızı, yemlerinizi, misinalarınızı ve yemlerinizi tek bir kullanışlı kapta saklamak için kullanın."],
                "tasks": [{"type": "item", "item": "aquaculture:tackle_box"}],
                "rewards": [{"type": "item", "item": "aquaculture:double_hook", "count": 1}]
            },
            {
                "key": "tide_fish",
                "x": 0.0,
                "y": 2.0,
                "dependency": "fishing_intro",
                "title_en": "Catching the Tides",
                "title_tr": "Gelgit Balıkçılığı",
                "desc_en": ["Tide adds specialized seasonal fish and weather-dependent catches. Different fish only spawn in specific tides or seasons (Serene Seasons integration!). Catch a Largemouth Bass or Yellow Perch to prove your skill."],
                "desc_tr": ["Tide, mevsimlik balıklar ve hava durumuna bağlı avlar ekler. Farklı balıklar sadece belirli gelgitlerde veya mevsimlerde (Serene Seasons entegrasyonu!) ortaya çıkar. Yeteneğinizi kanıtlamak için bir Largemouth Bass veya Sarı Levrek yakalayın."],
                "tasks": [
                    {"type": "item", "item": "tide:largemouth_bass"}
                ],
                "rewards": [{"type": "item", "item": "minecraft:cooked_cod", "count": 4}]
            },
            {
                "key": "seafood",
                "x": 1.5,
                "y": 1.5,
                "dependency": "tide_fish",
                "title_en": "Seafood Cuisine",
                "title_tr": "Deniz Lezzetleri",
                "desc_en": ["Cut your caught fish on a Farmer's Delight cutting board to obtain fish slices. Use these slices to prepare gourmet meals like Salmon Salad or Fricassee in the Cooking Pot."],
                "desc_tr": ["Yakaladığınız balıkları balık dilimleri elde etmek için bir Farmer's Delight kesme tahtasında dilimleyin. Bu dilimleri Tencerede Somon Salatası veya Frikase gibi gurme yemekler hazırlamak için kullanın."],
                "tasks": [
                    {"type": "item", "item": "farmersdelight:cod_slice"}
                ],
                "rewards": [{"type": "item", "item": "minecraft:bowl", "count": 2}]
            },
            {
                "key": "celestial_fish",
                "x": 0.0,
                "y": 4.0,
                "dependency": "tide_fish",
                "title_en": "Celestial Catch",
                "title_tr": "Yıldızların Altında",
                "desc_en": ["Under rare conditions or astronomical alignments, celestial fish like the Neptune Koi, Shooting Starfish, or Sun Emblem appear in the water. Catch one of these legendary space fish!"],
                "desc_tr": ["Nadir koşullar veya astronomik dizilimler altında, Neptune Koi, Kayan Denizyıldızı (Shooting Starfish) veya Güneş Amblemi (Sun Emblem) gibi kozmik balıklar sularda görünür. Bu efsanevi uzay balıklarından birini yakalayın!"],
                "tasks": [
                    {"type": "item", "item": "tide:neptune_koi"}
                ],
                "rewards": [
                    {"type": "item", "item": "aquaculture:neptunes_bounty", "count": 1}
                ]
            },
            {
                "key": "crab_trap",
                "x": -3.0,
                "y": 2.0,
                "dependency": "fishing_intro",
                "title_en": "Crab Trapping",
                "title_tr": "Yengeç Kapanı",
                "desc_en": ["Crabber's Delight adds crabs, clams, shrimp, and a Crab Trap to passively catch them. Place a Crab Trap in water baited with fish, and harvest shellfish to craft Bisque, Crab Cakes, or Surf and Turf."],
                "desc_tr": ["Crabber's Delight, yengeçler, midyeler, karidesler ve bunları pasif olarak yakalayan bir Yengeç Kapanı (Crab Trap) ekler. Yemle birlikte suya bir Yengeç Kapanı yerleştirin ve kabuklu deniz ürünleri toplayarak Bisque, Yengeç Köftesi veya Surf and Turf yapın."],
                "tasks": [{"type": "item", "item": "crabbersdelight:crab_trap"}],
                "rewards": [{"type": "item", "item": "crabbersdelight:clam", "count": 4}]
            },
            {
                "key": "ocean_delight",
                "x": 3.0,
                "y": 3.0,
                "dependency": "seafood",
                "title_en": "Ocean's Bounty",
                "title_tr": "Okyanusun Bereketi",
                "desc_en": ["Ocean's Delight turns guardians and squid into gourmet cuisine. Slice a Guardian on a cutting board, then cook up a bowl of Guardian Soup or brave a Fugu Roll from pufferfish for big buffs."],
                "desc_tr": ["Ocean's Delight, guardianları ve mürekkep balıklarını gurme mutfak haline getirir. Bir Guardianı kesme tahtasında dilimleyin, ardından bir kase Guardian Çorbası yapın veya büyük güçlendirmeler için pufferfish'ten bir Fugu Roll'a cesaret edin."],
                "tasks": [{"type": "item", "item": "oceansdelight:guardian_soup"}],
                "rewards": [{"type": "item", "item": "oceansdelight:fugu_roll", "count": 2}]
            },
            {
                "key": "fish_trap",
                "x": -1.5,
                "y": 4.0,
                "dependency": "fishing_intro",
                "title_en": "Passive Fishing",
                "title_tr": "Pasif Balıkçılık",
                "desc_en": ["The Fisherman's Trap passively catches fish over time while you do other things. Place it in a body of water and check back periodically for your catch — perfect for keeping your colony's kitchen stocked."],
                "desc_tr": ["Fisherman's Trap, siz başka işlerle uğraşırken zamanla pasif olarak balık yakalar. Bir su kütlesine yerleştirin ve avınız için ara ara kontrol edin — koloninizin mutfağını taze tutmak için mükemmel."],
                "tasks": [{"type": "item", "item": "fishermens_trap:fishtrap"}],
                "rewards": [{"type": "item", "item": "minecraft:cod", "count": 8}]
            },
            {
                "key": "deep_dive",
                "x": 1.5,
                "y": 6.0,
                "dependency": "celestial_fish",
                "title_en": "Take a Deep Dive",
                "title_tr": "Derin Dalış",
                "desc_en": ["Hybrid Aquatic fills the oceans with hundreds of new fish, jellyfish, and crabs, plus a Diving Suit to explore the depths safely. Craft a Diving Helmet so you can stay underwater long enough to discover them all."],
                "desc_tr": ["Hybrid Aquatic, okyanusları yüzlerce yeni balık, denizanası ve yengeçle doldurur; ayrıca derinlikleri güvenle keşfetmek için bir Dalgıç Giysisi ekler. Hepsini keşfetmek için yeterince uzun süre su altında kalabilmek adına bir Dalgıç Kaskı (Diving Helmet) yapın."],
                "tasks": [{"type": "item", "item": "hybrid_aquatic:diving_helmet"}],
                "rewards": [{"type": "item", "item": "hybrid_aquatic:diving_boots", "count": 1}]
            }
        ]
    },
    {
        "filename": "muhendislik_ve_otomasyon",
        "title_en": "Kinetic Engineering",
        "title_tr": "Çarklar ve Dişliler",
        "icon": "create:water_wheel",
        "quests": [
            {
                "key": "create_intro",
                "x": 0.0,
                "y": 0.0,
                "title_en": "Kinetic Power",
                "title_tr": "Kinetik Güç",
                "desc_en": ["Create introduces mechanical engineering and kinetic stress. To generate rotational force, craft a Water Wheel, some Shafts, and Cogwheels to transmit rotational energy."],
                "desc_tr": ["Create, mekanik mühendisliği ve kinetik stresi sunar. Dönme gücü üretmek için bir Su Çarkı (Water Wheel), miller (Shafts) ve dönme enerjisini iletmek için dişliler (Cogwheels) yapın."],
                "tasks": [
                    {"type": "item", "item": "create:water_wheel"},
                    {"type": "item", "item": "create:shaft"},
                    {"type": "item", "item": "create:cogwheel"}
                ],
                "rewards": [{"type": "item", "item": "minecraft:andesite", "count": 16}]
            },
            {
                "key": "press",
                "x": -1.5,
                "y": 1.5,
                "dependency": "create_intro",
                "title_en": "Iron Sheets",
                "title_tr": "Demir Plakalar",
                "desc_en": ["The Mechanical Press squeezes ingots into metal sheets. Place items under it on a depot or belt to press them automatically. Crucial for advanced crafting recipes."],
                "desc_tr": ["Mekanik Pres (Mechanical Press), külçeleri ezerek metal plakalara dönüştürür. Otomatik olarak preslemek için eşyaları altına yerleştirin. Gelişmiş tarifler için çok önemlidir."],
                "tasks": [{"type": "item", "item": "create:mechanical_press"}],
                "rewards": [{"type": "item", "item": "minecraft:iron_ingot", "count": 4}]
            },
            {
                "key": "mixer",
                "x": 1.5,
                "y": 1.5,
                "dependency": "create_intro",
                "title_en": "Alloys and Mixing",
                "title_tr": "Alaşım ve Karıştırma",
                "desc_en": ["The Mechanical Mixer and Basin mix materials under rotational force. Some recipes require heat, which can be supplied by placing a Blaze Burner beneath the Basin."],
                "desc_tr": ["Mekanik Mikser ve Hazne (Basin), malzemeleri dönme kuvveti altında karıştırır. Bazı tarifler, Haznenin altına bir Blaze Burner yerleştirilerek sağlanabilecek ısı gerektirir."],
                "tasks": [
                    {"type": "item", "item": "create:mechanical_mixer"},
                    {"type": "item", "item": "create:basin"}
                ],
                "rewards": [{"type": "item", "item": "minecraft:coal", "count": 8}]
            },
            {
                "key": "automated_kitchen",
                "x": 0.0,
                "y": 3.0,
                "dependency_or": ["press", "mixer"],
                "title_en": "Automated Cooking",
                "title_tr": "Otomatik Mutfak",
                "desc_en": ["Integrate Create machinery with Farmer's Delight using Slice & Dice or Create Central Kitchen. Automate food slicing or soup cooking to supply your colony or spice of life goals effortlessly!"],
                "desc_tr": ["Slice & Dice veya Create Central Kitchen kullanarak Create makinelerini Farmer's Delight ile birleştirin. Koloninizi veya Spice of Life hedeflerinizi zahmetsizce beslemek için yiyecek dilimlemeyi veya çorba pişirmeyi otomatikleştirin!"],
                "tasks": [{"type": "checkmark"}],
                "rewards": [{"type": "item", "item": "minecraft:golden_carrot", "count": 8}]
            },
            {
                "key": "slicer",
                "x": -3.0,
                "y": 3.0,
                "dependency": "automated_kitchen",
                "title_en": "Slice & Dice",
                "title_tr": "Dilimle & Doğra",
                "desc_en": ["Slice & Dice adds a Slicer that automates Farmer's Delight cutting-board recipes, and a Sprinkler driven by Create's rotation. Hook a Slicer to a belt and a depot to mass-produce sliced ingredients without lifting a finger."],
                "desc_tr": ["Slice & Dice, Farmer's Delight kesme tahtası tariflerini otomatikleştiren bir Dilimleyici (Slicer) ve Create'in dönüşüyle çalışan bir Serpme ekler. Bir Dilimleyiciyi bant ve depoya bağlayın ve parmağınızı kıpırdatarak dilimlenmiş malzeme üretin."],
                "tasks": [{"type": "item", "item": "sliceanddice:slicer"}],
                "rewards": [{"type": "item", "item": "sliceanddice:sprinkler", "count": 1}]
            },
            {
                "key": "central_kitchen",
                "x": 3.0,
                "y": 3.0,
                "dependency": "automated_kitchen",
                "title_en": "Central Kitchen",
                "title_tr": "Merkez Mutfak",
                "desc_en": ["Create Central Kitchen integrates Farmer's Delight cooking with Create: a Blaze Stove heats multiple pots at once and automated recipes pour out syrup, tomato sauce, and more. Grab the Cooking Guide to learn the recipes and start your factory kitchen."],
                "desc_tr": ["Create Central Kitchen, Farmer's Delight pişirmeyi Create ile bütünleştirir: bir Blaze Stove aynı anda birden fazla tencereyi ısıtır ve otomatik tarifler şurup, domates sosu ve daha fazlasını döker. Tarifleri öğrenmek ve fabrika mutfağınızı kurmak için Pişirme Rehberini (Cooking Guide) alın."],
                "tasks": [{"type": "item", "item": "create_central_kitchen:cooking_guide"}],
                "rewards": [{"type": "item", "item": "create_central_kitchen:syrup_bucket", "count": 1}]
            }
        ]
    },
    {
        "filename": "kesif_ve_koloniler",
        "title_en": "Exploration & MineColonies",
        "title_tr": "Bilinmeyen Dünyalar ve Koloniler",
        "icon": "minecolonies:blockhuttownhall",
        "quests": [
            {
                "key": "explore_intro",
                "x": -2.0,
                "y": 0.0,
                "title_en": "Wildlife Encyclopedia",
                "title_tr": "Yaban Hayatı Ansiklopedisi",
                "desc_en": ["This world is full of wild beasts and birds. Craft the Animal Dictionary from Alex's Mobs to learn taming methods, drops, and ecosystem interactions for all creatures."],
                "desc_tr": ["Bu dünya vahşi hayvanlar ve kuşlarla doludur. Tüm canlıların evcilleştirme yöntemlerini, düşürdükleri eşyaları ve ekosistem etkileşimlerini öğrenmek için Alex's Mobs'tan Hayvan Sözlüğü'nü (Animal Dictionary) yapın."],
                "tasks": [{"type": "item", "item": "alexsmobs:animal_dictionary"}],
                "rewards": [{"type": "item", "item": "minecraft:melon_seeds", "count": 4}]
            },
            {
                "key": "caves_tablet",
                "x": -2.0,
                "y": 2.0,
                "dependency": "explore_intro",
                "title_en": "Deep Cave Biomes",
                "title_tr": "Derin Mağara Biyomları",
                "desc_en": ["Alex's Caves introduces 5 subterranean biomes filled with magnetic forces, toxic waste, prehistoric dinosaurs, bioluminescent oceans, and dark hollows. Locate one using a Cave Tablet."],
                "desc_tr": ["Alex's Caves; manyetik kuvvetler, toksik atıklar, tarih öncesi dinozorlar, biyolüminesans okyanuslar ve karanlık boşluklarla dolu 5 yeraltı biyomu sunar. Bir Mağara Tableti (Cave Tablet) kullanarak birini bulun."],
                "tasks": [{"type": "item", "item": "alexscaves:cave_tablet"}],
                "rewards": [{"type": "item", "item": "minecraft:iron_pickaxe", "count": 1}]
            },
            {
                "key": "minecolonies_intro",
                "x": 2.0,
                "y": 0.0,
                "title_en": "Supply Camp",
                "title_tr": "Tedarik Kampı",
                "desc_en": ["MineColonies lets you build a thriving city of citizens. Start by crafting a Supply Camp Deployer and right-clicking it on a flat, clear 16x17 area (no flowers, grass, or holes). Inside the deployed camp's rack you'll find the precious Build Tool and a Town Hall block — the two items every colony is founded on."],
                "desc_tr": ["MineColonies, vatandaşlardan oluşan gelişen bir şehir kurmanızı sağlar. Bir Tedarik Kampı Dağıtıcısı (Supply Camp Deployer) yapın ve düz, temiz bir 16x17 alana (çiçek, çimen veya çukur olmayan) sağ tıklayarak yerleştirin. Yerleştirilen kampın rafında değerli İnşaat Aletini (Build Tool) ve bir Belediye Binası bloğu bulacaksınız — her koloninin temelini oluşturan iki eşya."],
                "tasks": [{"type": "item", "item": "minecolonies:supplycampdeployer"}],
                "rewards": [
                    {"type": "item", "item": "minecraft:oak_log", "count": 32},
                    {"type": "item", "item": "minecraft:chest", "count": 2}
                ]
            },
            {
                "key": "town_hall",
                "x": 2.0,
                "y": 2.0,
                "dependency": "minecolonies_intro",
                "title_en": "Establishing a Colony",
                "title_tr": "Koloni Kurmak",
                "desc_en": ["Hold the Build Tool, right-click the ground, and select the Town Hall to preview and place it. Then right-click the placed Town Hall block and choose Create Colony. Sign the Settlement Covenant and your first citizens will arrive shortly!"],
                "desc_tr": ["İnşaat Aletini elinize alın, yere sağ tıklayın ve Belediye Binası'nı (Town Hall) seçerek önizleyip yerleştirin. Ardından yerleştirilen Belediye Binası bloğuna sağ tıklayıp Koloni Oluştur'u seçin. Yerleşim Sözleşmesi'ni imzalayın; ilk vatandaşlarınız kısa süre sonra gelecek!"],
                "tasks": [{"type": "item", "item": "minecolonies:blockhuttownhall"}],
                "rewards": [
                    {"type": "item", "item": "minecolonies:clipboard", "count": 1},
                    {"type": "item", "item": "minecraft:bread", "count": 8}
                ]
            },
            {
                "key": "builder",
                "x": 2.0,
                "y": 4.0,
                "dependency": "town_hall",
                "title_en": "The Colony Builder",
                "title_tr": "Koloni İnşaatçısı",
                "desc_en": ["Citizens cannot construct buildings on their own. Build a Builder's Hut, place it with the Build Tool, assign a Builder, then open its GUI and pick Build Options to start construction. Keep the builder's chest supplied to grow your town."],
                "desc_tr": ["Vatandaşlar binaları kendi başlarına kuramazlar. İnşaatçı Kulübesi (Builder's Hut) yapın, İnşaat Aleti ile yerleştirin, inşaatçı atayın, ardından GUI'sini açıp İnşaat Seçenekleri'ni seçerek inşaata başlayın. İstediği malzemeleri sandığına koyarak şehri genişletin."],
                "tasks": [{"type": "item", "item": "minecolonies:blockhutbuilder"}],
                "rewards": [
                    {"type": "item", "item": "minecraft:stone_bricks", "count": 32},
                    {"type": "item", "item": "minecraft:oak_planks", "count": 32}
                ]
            },
            {
                "key": "food_supply",
                "x": 3.5,
                "y": 4.0,
                "dependency": "builder",
                "title_en": "Feeding the Citizens",
                "title_tr": "Vatandaşları Besleme",
                "desc_en": ["Citizens get hungry and stop working if not fed. Establish a Farm Hut or Fishery Hut so your colonists can gather and produce food automatically. A Farmer also needs a Field block assigned nearby."],
                "desc_tr": ["Vatandaşlar acıkır ve beslenmezlerse çalışmayı bırakırlar. Kolonistlerinizin otomatik olarak yiyecek toplayıp üretebilmesi için Çiftçi Kulübesi (Farm Hut) veya Balıkçı Kulübesi (Fishery Hut) kurun. Çiftçinin yakınına bir Tarla (Field) bloğu atamanız da gerekir."],
                "tasks": [{"type": "checkmark"}],
                "rewards": [
                    {"type": "item", "item": "minecraft:wheat_seeds", "count": 8},
                    {"type": "item", "item": "minecraft:cooked_beef", "count": 8}
                ]
            },
            {
                "key": "guard_tower",
                "x": 2.0,
                "y": 6.0,
                "dependency": "builder",
                "title_en": "Raids & Security",
                "title_tr": "Baskınlar ve Güvenlik",
                "desc_en": ["As your colony grows, barbarians and raiders will attack during the night. Build Guard Towers and recruit guards to defend your citizens!"],
                "desc_tr": ["Koloniniz büyüdükçe, barbarlar ve akıncılar geceleri saldıracaktır. Vatandaşlarınızı savunmak için Nöbetçi Kuleleri (Guard Towers) inşa edin ve muhafızlar kiralayın!"],
                "tasks": [{"type": "checkmark"}],
                "rewards": [
                    {"type": "item", "item": "minecraft:iron_sword", "count": 1},
                    {"type": "item", "item": "minecraft:iron_shield", "count": 1}
                ]
            },
            {
                "key": "wildernature_bounty",
                "x": -2.0,
                "y": 4.0,
                "dependency": "explore_intro",
                "title_en": "Hunter's Bounties",
                "title_tr": "Avcı İlanları",
                "desc_en": ["Wildernature adds a Bounty Board where you can accept hunting contracts to track down wild animals for rewards. Craft a Bounty Board, take a Common Contract, and start earning loot bags and trophies from the wilderness."],
                "desc_tr": ["Wildernature, ödüller karşılığı vahşi hayvanları izlemeniz için avcılık sözleşmeleri kabul edebileceğiniz bir İlan Tahtası (Bounty Board) ekler. Bir İlan Tahtası yapın, bir Sözleşme alın ve doğadan ganimet çantaları ve trofe kazanmaya başlayın."],
                "tasks": [{"type": "item", "item": "wildernature:bounty_board"}],
                "rewards": [{"type": "item", "item": "wildernature:common_contract", "count": 2}]
            },
            {
                "key": "goblin_trader",
                "x": -2.0,
                "y": 6.0,
                "dependency": "explore_intro",
                "title_en": "Underground Merchants",
                "title_tr": "Yeraltı Tüccarları",
                "desc_en": ["Goblin Traders spawn deep in the caves and offer rare trades for emeralds. Some goblins even sell vein-mining tools. Explore the caves below, find a Goblin Trader, and trade for something shiny!"],
                "desc_tr": ["Goblin Tüccarlar mağaraların derinliklerinde belirir ve zümrüt karşılığında nadir takaslar sunar. Bazı goblinler damar-madenciliği aletleri bile satar. Aşağıdaki mağaraları keşfedin, bir Goblin Tüccar bulun ve parlayan bir şeyler alın!"],
                "tasks": [{"type": "checkmark"}],
                "rewards": [{"type": "item", "item": "minecraft:emerald", "count": 4}]
            }
        ]
    },
    {
        "filename": "icecekler_ve_eglence",
        "title_en": "Drinks & Nightlife",
        "title_tr": "İçecekler ve Eğlence",
        "icon": "brewinandchewin:keg",
        "quests": [
            {
                "key": "keg",
                "x": 0.0,
                "y": 0.0,
                "title_en": "Fermentation Station",
                "title_tr": "Fermentasyon İstasyonu",
                "desc_en": ["Brewin' & Chewin' introduces the Keg, which ferments drinks and ages cheese. Place a Keg, fill it, and let time work its magic to brew Beer, Mead, Rice Wine, or Kombucha — each with unique effects."],
                "desc_tr": ["Brewin' & Chewin', içecekleri fermente eden ve peyniri aged yapan Fıçıyı (Keg) sunar. Bir Fıçı yerleştirin, doldurun ve zamanın sihrini Beer, Mead, Pirinç Şarabı veya Kombucha üretmesine izin verin — her biri benzersiz etkilere sahiptir."],
                "tasks": [{"type": "item", "item": "brewinandchewin:keg"}],
                "rewards": [{"type": "item", "item": "brewinandchewin:beer", "count": 4}]
            },
            {
                "key": "brewery",
                "x": -1.5,
                "y": 1.5,
                "dependency": "keg",
                "title_en": "The Brewery",
                "title_tr": "Bira Fabrikası",
                "desc_en": ["Let's Do: Brewery adds a full brewing line. Build a Wooden Brewing Station, grow Hops, and craft mugs of Beer, Pretzels, and Sausage to host a proper brewfest. Don't drink too much, or the Breathalyzer will give you away!"],
                "desc_tr": ["Let's Do: Brewery, tam bir bira yapım hattı ekler. bir Ahşap Mayalama İstasyonu (Wooden Brewing Station) kurun, Şerbetçi Otunu (Hops) büyütün ve gerçek bir brewfest düzenlemek için biralar, Pretzel ve Sosis yapın. Çok içmeyin, yoksa Alkolmetre (Breathalyzer) sizi ele verir!"],
                "tasks": [{"type": "item", "item": "brewery:wooden_brewingstation"}],
                "rewards": [{"type": "item", "item": "brewery:beer_mug", "count": 2}]
            },
            {
                "key": "cheese",
                "x": 1.5,
                "y": 1.5,
                "dependency": "keg",
                "title_en": "Aged Cheese",
                "title_tr": "Yıllandırılmış Peynir",
                "desc_en": ["Age a Flaxen Cheese Wheel in the Keg to turn it into a sharp, sliceable delicacy. Combine it with bread, pasta, or use it in Cheesy Pasta and Fondue for a rich, comforting meal."],
                "desc_tr": ["Bir Külçe Peyniri (Flaxen Cheese Wheel) Fıçıda aged ederek keskin, dilimlenebilir bir lezzete dönüştürün. Ekmek, makarna ile birleştirin veya Peynirli Makarna (Cheesy Pasta) ve Fondü'de kullanarak zengin, doyurucu bir öğün hazırlayın."],
                "tasks": [{"type": "item", "item": "brewinandchewin:flaxen_cheese_wheel"}],
                "rewards": [{"type": "item", "item": "brewinandchewin:cheesy_pasta", "count": 2}]
            },
            {
                "key": "beach_party",
                "x": 0.0,
                "y": 3.5,
                "dependency": "keg",
                "title_en": "Beach Party!",
                "title_tr": "Plaj Partisi!",
                "desc_en": ["Let's Do: Beachparty brings tropical fun. Set down a Beach Chair and a Mini Fridge, then mix a Coconut Cocktail or Honey Cocktail. Hunt for buried message-in-a-bottle loot and relax by the waves."],
                "desc_tr": ["Let's Do: Beachparty, tropik eğlence getirir. bir Plaj Sandalyesi (Beach Chair) ve bir Mini Buzdolabı yerleştirin, ardından bir Hindistan Cevizi Kokteyli veya Bal Kokteyli karıştırın. Kumda gömülü şişedeki-mektup ganimetini arayın ve dalgaların yanında dinlenin."],
                "tasks": [
                    {"type": "item", "item": "beachparty:beach_chair"},
                    {"type": "item", "item": "beachparty:coconut_cocktail"}
                ],
                "rewards": [{"type": "item", "item": "beachparty:mini_fridge", "count": 1}]
            }
        ]
    }
]

def main():
    base_dir = "c:/Users/Yigit/AppData/Roaming/PrismLauncher/instances/Balik/minecraft"
    quests_dir = os.path.join(base_dir, "config/ftbquests/quests")
    chapters_dir = os.path.join(quests_dir, "chapters")
    lang_dir = os.path.join(base_dir, "kubejs/assets/kubejs/lang")

    os.makedirs(chapters_dir, exist_ok=True)
    os.makedirs(lang_dir, exist_ok=True)

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
    for order, ch in enumerate(chapters_data):
        filename = ch["filename"]
        ch_id = gen_id(f"chapter:{filename}")

        # Translation keys for chapter
        ch_title_key = f"kubejs.ftbquests.chapter.{filename}.title"
        en_translations[ch_title_key] = ch["title_en"]
        tr_translations[ch_title_key] = ch["title_tr"]

        quests_list = []
        for q in ch["quests"]:
            q_key = q["key"]
            q_id = gen_id(f"quest:{filename}:{q_key}")

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
                dep_id = gen_id(f"quest:{filename}:{q['dependency']}")
                q_snbt["dependencies"] = [dep_id]
            elif "dependency_or" in q:
                dep_ids = [gen_id(f"quest:{filename}:{d}") for d in q["dependency_or"]]
                q_snbt["dependencies"] = dep_ids
                q_snbt["dependency_requirement"] = "one_completed"

            quests_list.append(q_snbt)

        chapter_snbt = {
            "id": ch_id,
            "group": "",
            "order_index": order,
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
    with open(os.path.join(lang_dir, "en_us.json"), "w", encoding="utf-8") as f:
        json.dump(en_translations, f, indent=4, ensure_ascii=False)
    print("Generated en_us.json")

    with open(os.path.join(lang_dir, "tr_tr.json"), "w", encoding="utf-8") as f:
        json.dump(tr_translations, f, indent=4, ensure_ascii=False)
    print("Generated tr_tr.json")

if __name__ == "__main__":
    main()
