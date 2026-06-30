CHAPTER = {
    'order': 1,
    'filename': 'toprak_ana_ve_hasat_zamani',
    'title_en': 'Mother Earth \\& Harvest Time',
    'title_tr': 'Toprak Ana ve Hasat Zamanı',
    'icon': 'minecraft:wheat',
    'quests': [
        {
            'key': 'farming_basics',
            'x': 0.0,
            'y': 0.0,
            'shape': 'rsphere',
            'title_en': 'Farming Basics',
            'title_tr': 'Tarımın Temelleri',
            'subtitle_en': 'Meet the Soil',
            'subtitle_tr': 'Toprakla Tanışma',
            'desc_en': ["Your agricultural journey begins with a simple hoe. Till the soil and break grass to collect seeds. Plant your first crops. This is the first step towards self-sufficiency and survival."],
            'desc_tr': ["Tarım maceranız basit bir çapa ile başlar. Bir çapa yapın ve çimleri kırarak tohumlar toplayın. Toprağı sürün ve ilk ekinlerinizi ekin. Bu, hayatta kalmanın ve kendi yemeğinizi üretmenin ilk adımıdır."],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'minecraft:wooden_hoe',
                },
                {
                    'type': 'item',
                    'item': 'minecraft:wheat_seeds',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'minecraft:bone_meal',
                    'count': 8,
                },
            ],
        },
        {
            'key': 'first_harvest',
            'x': -1.5,
            'y': 1.5,
            'dependency': 'farming_basics',
            'title_en': 'The First Harvest',
            'title_tr': 'İlk Hasat',
            'subtitle_en': 'Straw and Blade',
            'subtitle_tr': 'Saman ve Bıçak',
            'desc_en': ["Every great meal starts with a simple blade. Craft a Flint Knife from Farmer's Delight — it lets you harvest Straw from grass and get clean cuts from animals. The foundation of all cooking begins here."],
            'desc_tr': ["Her büyük yemek basit bir bıçakla başlar. Farmer's Delight'tan bir Çakmaktaşı Bıçak yapın — otlardan Saman toplamanızı ve hayvanlardan temiz kesimler almanızı sağlar. Tüm yemek pişirme burada başlıyor."],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'farmersdelight:flint_knife',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'farmersdelight:tomato_seeds',
                    'count': 5,
                },
                {
                    'type': 'item',
                    'item': 'farmersdelight:cabbage_seeds',
                    'count': 3,
                },
            ],
        },
        {
            'key': 'seasons_awareness',
            'x': 1.5,
            'y': 1.5,
            'dependency': 'farming_basics',
            'title_en': 'Reading the Seasons',
            'title_tr': 'Mevsimleri Okumak',
            'subtitle_en': 'The Rhythm of Nature',
            'subtitle_tr': 'Doğanın Ritmi',
            'desc_en': ['With Serene Seasons, crops grow differently each season. Craft a Calendar to track the current season and plan your planting schedule. Some crops only thrive in spring, others in autumn — timing is everything.'],
            'desc_tr': ['Serene Seasons ile ekinler her mevsimde farklı büyür. Mevcut mevsimi takip etmek ve ekim planınızı yapmak için bir Takvim yapın. Bazı ekinler yalnızca ilkbaharda, bazıları sonbaharda yetişir — zamanlama her şeydir.'],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'sereneseasons:calendar',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'farm_and_charm:fertilizer',
                    'count': 6,
                },
            ],
        },
        {
            'key': 'farmers_market',
            'x': 0.0,
            'y': 2.0,
            'dependency': 'farming_basics',
            'title_en': "The Farmers' Market",
            'title_tr': 'Çiftçi Pazarı',
            'subtitle_en': 'Everything is for Sale',
            'subtitle_tr': 'Her Şey Satılık',
            'desc_en': ["Finding every seed in the wild can be tedious. Craft the Market block from Farming for Blockheads. It summons a merchant who sells all kinds of seeds and saplings in exchange for emeralds."],
            'desc_tr': ["Tüm tohumları doğada bulmak zordur. Farming for Blockheads modundan Market bloğunu yapın. Bu blok, zümrüt karşılığında her türlü tohumu ve fidanı almanızı sağlayan bir köylü tüccar çağırır."],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'farmingforblockheads:market',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'minecraft:emerald',
                    'count': 4,
                },
            ],
        },
        {
            'key': 'corn_field',
            'x': -3.0,
            'y': 3.5,
            'dependency': 'first_harvest',
            'title_en': 'The Corn Field',
            'title_tr': 'Mısır Tarlası',
            'subtitle_en': 'Golden Plains',
            'subtitle_tr': 'Altın Ovalar',
            'desc_en': ['Corn Delight adds towering corn crops and hearty recipes. Plant Corn Seeds, watch them grow tall, and craft Cornbread, Popcorn, or Corn Soup. The golden grain of the plains.'],
            'desc_tr': ['Corn Delight, devasa mısır ekinleri ve doyurucu tarifler ekler. Mısır Tohumu ekin, nasıl büyüdüklerini izleyin ve Mısır Ekmeği, Patlamış Mısır veya Mısır Çorbası yapın. Ovaların altın tahılı.'],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'corn_delight:corn_seeds',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'corn_delight:cornbread',
                    'count': 4,
                },
                {
                    'type': 'item',
                    'item': 'corn_delight:popcorn',
                    'count': 4,
                },
            ],
        },
        {
            'key': 'fd_crops',
            'x': -1.0,
            'y': 3.5,
            'dependency': 'first_harvest',
            'icon': 'farmersdelight:tomato_seeds',
            'title_en': "Farmer's Delight Crops",
            'title_tr': "Farmer's Delight Ekinleri",
            'subtitle_en': 'Delicious Variety',
            'subtitle_tr': 'Lezzetli Çeşitlilik',
            'desc_en': ["Farmer's Delight adds various vegetables and rice. Enrich your kitchen by collecting tomatoes, cabbages, onions, and rice. Each crop grows in different seasons and conditions."],
            'desc_tr': ["Farmer's Delight çeşitli sebzeler ve pirinç ekler. Domates, lahana, soğan ve pirinç toplayarak mutfağınızı zenginleştirin. Her biri farklı mevsimlerde ve koşullarda büyür."],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'farmersdelight:tomato_seeds',
                },
                {
                    'type': 'item',
                    'item': 'farmersdelight:cabbage_seeds',
                },
                {
                    'type': 'item',
                    'item': 'farmersdelight:onion',
                },
                {
                    'type': 'item',
                    'item': 'farmersdelight:rice',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'minecraft:bone_meal',
                    'count': 6,
                },
            ],
        },
        {
            'key': 'spice_route',
            'x': 1.0,
            'y': 3.5,
            'dependency': 'farmers_market',
            'title_en': 'The Spice Route',
            'title_tr': 'Baharat Yolu',
            'subtitle_en': 'Spices of Distant Biomes',
            'subtitle_tr': 'Uzak Biyomların Baharatları',
            'desc_en': ['Croptopia introduces a world of exotic crops. Collect Ginger, Turmeric, Basil, Coffee Beans, and Vanilla from different biomes. These spices and ingredients unlock hundreds of advanced recipes.'],
            'desc_tr': ['Croptopia, egzotik ekinler dünyası sunar. Farklı biyomlardan Zerdeçal, Zencefil, Fesleğen, Kahve Çekirdeği ve Vanilya toplayın. Bu baharatlar ve malzemeler yüzlerce gelişmiş tarifin kilidini açar.'],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'croptopia:ginger',
                },
                {
                    'type': 'item',
                    'item': 'croptopia:basil',
                },
                {
                    'type': 'item',
                    'item': 'croptopia:turmeric',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'croptopia:coffee_beans',
                    'count': 3,
                },
                {
                    'type': 'item',
                    'item': 'croptopia:vanilla_seeds',
                    'count': 2,
                },
            ],
        },
        {
            'key': 'the_orchard',
            'x': 3.0,
            'y': 3.5,
            'dependency': 'seasons_awareness',
            'title_en': 'The Orchard',
            'title_tr': 'Meyve Bahçesi',
            'subtitle_en': 'Tree Fruits',
            'subtitle_tr': 'Ağaç Meyveleri',
            'desc_en': ["Plant fruit trees from Croptopia: Oranges, Bananas, Cherries, Lemons, and more. Right-click mature leaf blocks to harvest fruit. Craft fruit Saplings by combining two fruits with a vanilla sapling. A thriving orchard is a chef's paradise."],
            'desc_tr': ["Croptopia'dan meyve ağaçları dikin: Portakal, Muz, Kiraz, Limon ve daha fazlası. Olgun yaprak bloklarına sağ tıklayarak meyve hasat edin. İki meyveyi vanilla fidanıyla birleştirerek meyve Fidanları yapın. Gelişen bir meyve bahçesi bir şefin cennetidir."],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'croptopia:orange_sapling',
                },
                {
                    'type': 'item',
                    'item': 'croptopia:banana_sapling',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'croptopia:orange',
                    'count': 6,
                },
                {
                    'type': 'item',
                    'item': 'croptopia:banana',
                    'count': 6,
                },
                {
                    'type': 'item',
                    'item': 'croptopia:lemon_sapling',
                },
            ],
        },
        {
            'key': 'fertile_soil',
            'x': -2.0,
            'y': 5.5,
            'dependencies': ['corn_field', 'fd_crops'],
            'icon': 'farmersdelight:rich_soil',
            'title_en': 'Compost \\& Rich Soil',
            'title_tr': 'Kompost ve Zengin Toprak',
            'subtitle_en': 'Soils of Abundance',
            'subtitle_tr': 'Can Veren Topraklar',
            'desc_en': ["Standard dirt only goes so far. Craft Organic Compost and let it mature into Rich Soil. Rich Soil boosts crop growth rates significantly and increases harvest yields."],
            'desc_tr': ["Sıradan toprak bir yere kadar yeter. Organik Kompost yapın ve onun Zengin Toprağa dönüşmesini bekleyin. Zengin Toprak, ekinlerin büyümesini inanılmaz derecede hızlandırır ve hasat miktarını artırır."],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'farmersdelight:organic_compost',
                },
                {
                    'type': 'item',
                    'item': 'farmersdelight:rich_soil',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'farmersdelight:straw',
                    'count': 16,
                },
            ],
        },
        {
            'key': 'irrigation',
            'x': 2.0,
            'y': 5.5,
            'dependencies': ['spice_route', 'the_orchard'],
            'title_en': 'Automated Irrigation',
            'title_tr': 'Otomatik Sulama',
            'subtitle_en': 'Keep the Fields Hydrated',
            'subtitle_tr': 'Tarlayı Nemli Tut',
            'desc_en': ["The Water Sprinkler from Farm \\& Charm hydrates and accelerates nearby crops automatically. Place it above water and watch your fields thrive. Also try Fertilized Soil for even richer harvests."],
            'desc_tr': ["Farm \\& Charm'dan Su Serpme, yakındaki ekinleri otomatik olarak sulayarak büyümeyi hızlandırır. Suyun üzerine yerleştirin ve tarlanızın nasıl geliştiğini izleyin. Daha zengin hasatlar için Gübrelenmiş Toprak da deneyin."],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'farm_and_charm:water_sprinkler',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'farm_and_charm:fertilized_soil',
                    'count': 4,
                },
            ],
        },
        {
            'key': 'fertilizers',
            'x': 0.0,
            'y': 6.5,
            'shape': 'hexagon',
            'dependencies': ['fertile_soil', 'irrigation'],
            'icon': 'farmingforblockheads:yellow_fertilizer',
            'title_en': "Farmer's Secret Weapons",
            'title_tr': 'Çiftçinin Gizli Silahları',
            'subtitle_en': 'Special Fertilizers',
            'subtitle_tr': 'Özel Gübreler',
            'desc_en': ["Craft three types of fertilizers from Farming for Blockheads. Red fertilizer speeds up growth, yellow increases crop yields, and green prevents trampling while keeping the soil hydrated. Fertilize wisely!"],
            'desc_tr': ["Farming for Blockheads modundaki üç farklı gübreyi üretin. Kırmızı gübre büyümeyi hızlandırır, sarı gübre hasat miktarını artırır, yeşil gübre ise tarlanın ezilmesini önler ve su tutar. Tarlalarınızda doğru gübreyi kullanın!"],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'farmingforblockheads:red_fertilizer',
                },
                {
                    'type': 'item',
                    'item': 'farmingforblockheads:yellow_fertilizer',
                },
                {
                    'type': 'item',
                    'item': 'farmingforblockheads:green_fertilizer',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'farmingforblockheads:chicken_nest',
                },
                {
                    'type': 'item',
                    'item': 'farmingforblockheads:feeding_trough',
                },
            ],
        },
        {
            'key': 'compact_farming',
            'x': -2.0,
            'y': 7.5,
            'dependency': 'fertilizers',
            'title_en': 'Compact Farming',
            'title_tr': 'Kompakt Tarım',
            'subtitle_en': 'Harvest in a Block',
            'subtitle_tr': 'Blok İçinde Hasat',
            'desc_en': ['Botany Pots let you grow crops in a single block — perfect for indoor farms or space-limited builds. Place soil and a seed in the pot and watch it grow. Upgrade to Hopper Botany Pots for auto-collection.'],
            'desc_tr': ["Botany Pots, tek bir blokta ekin yetiştirmenizi sağlar — iç mekan çiftlikleri veya alan sınırlı yapılar için mükemmeldir. Saksıya toprak ve tohum koyun ve büyümesini izleyin. Otomatik toplama için Hopper Botany Pots'a yükseltin."],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'botanypots:terracotta_botany_pot',
                },
                {
                    'type': 'item',
                    'item': 'botanypots:terracotta_hopper_botany_pot',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'botanypots:terracotta_hopper_botany_pot',
                },
            ],
        },
        {
            'key': 'bee_inspector',
            'x': 0.0,
            'y': 8.0,
            'dependency': 'fertilizers',
            'title_en': 'Bee Genetics',
            'title_tr': 'Arı Genetiği',
            'subtitle_en': 'The Buzzy Inspector',
            'subtitle_tr': 'Arı Denetçisi',
            'desc_en': ["Fruitful Fun adds a complex bee genetics and pollination system. Craft the Buzzy Inspector. Right-click and hold it on bees to inspect their genes, traits, and pollens. You can hold a book and quill in your off-hand to record the data."],
            'desc_tr': ["Fruitful Fun modu, arılar için karmaşık bir genetik ve tozlaşma sistemi ekler. Buzzy Inspector aracını yapın. Arılara sağ tıklayıp basılı tutarak genlerini, özelliklerini ve taşıdıkları polenleri inceleyebilirsiniz. Sol elinizde kitap tutarak verileri kaydedebilirsiniz."],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'fruitfulfun:inspector',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'minecraft:beehive',
                },
                {
                    'type': 'item',
                    'item': 'minecraft:honey_bottle',
                    'count': 2,
                },
            ],
        },
        {
            'key': 'scent_candles',
            'x': 1.5,
            'y': 9.0,
            'dependency': 'bee_inspector',
            'icon': 'fruitfulfun:ender_candle',
            'title_en': 'Scented Candles',
            'title_tr': 'Kokulu Mumlar',
            'subtitle_en': 'Steer the Bees',
            'subtitle_tr': 'Arıları Yönlendir',
            'desc_en': ["Special candles release active scents that alter bee behavior. Craft Ender, Phantom, or Wandering Trader candles to control pollination patterns and trigger genetic mutations."],
            'desc_tr': ["Özel mumlar, yayılan kokular sayesinde arıların davranışlarını etkiler. Ender, Phantom veya Wandering Trader mumları yaparak arıların tozlaşmasını ve genetik mutasyonlarını kontrol altına alın."],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'fruitfulfun:ender_candle',
                },
                {
                    'type': 'item',
                    'item': 'fruitfulfun:phantom_candle',
                },
                {
                    'type': 'item',
                    'item': 'fruitfulfun:wandering_trader_candle',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'minecraft:emerald',
                    'count': 8,
                },
            ],
        },
        {
            'key': 'mutagen_hybrid',
            'x': -1.5,
            'y': 9.0,
            'dependency': 'bee_inspector',
            'title_en': 'Mutagen \\& Hybridization',
            'title_tr': 'Mutajen ve Melezleme',
            'subtitle_en': 'Birth of New Species',
            'subtitle_tr': 'Yeni Türlerin Doğuşu',
            'desc_en': ["Craft Bee Mutagen to trigger genetic mutations in bees. Through proper pollination and mutation, you can hybridize brand new fruit trees (like Citron, Lemon, Pomelo) and even breed rideable bees."],
            'desc_tr': ["Arı Mutajeni üreterek arılarda genetik mutasyonları tetikleyin. Doğru tozlaşma ve mutasyonlarla yepyeni meyve ağaçları melezleyebilir (örneğin Limon, Citron, Pomelo) ve hatta binilebilir arılar elde edebilirsiniz."],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'fruitfulfun:mutagen',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'fruitfulfun:citron_sapling',
                },
                {
                    'type': 'item',
                    'item': 'fruitfulfun:pomegranate_sapling',
                },
            ],
        },
        {
            'key': 'quality_crops',
            'x': 0.0,
            'y': 10.5,
            'shape': 'gear',
            'size': 1.5,
            'dependencies': ['compact_farming', 'mutagen_hybrid', 'scent_candles'],
            'icon': 'minecraft:golden_apple',
            'title_en': 'Perfect Harvest \\& Master Farmer',
            'title_tr': 'Kusursuz Hasat ve Tarım Üstadı',
            'subtitle_en': 'Pinnacle of Agriculture',
            'subtitle_tr': 'Tarımın Zirvesi',
            'desc_en': ["Congratulations! You are now a master of agriculture. Thanks to the Quality Food mod, crops can now harvest with bronze, silver, gold, or diamond quality. Quality ingredients offer extra nutrition, saturation, and powerful potion effects. Complete this checkmark to prove your mastery."],
            'desc_tr': ["Tebrikler! Artık tam teşekküllü bir tarım uzmanısınız. Quality Food modu sayesinde, ekinleriniz artık bronz, gümüş, altın ve hatta elmas kalitede çıkabilir. Zengin topraklarda yetiştirilen ve kaliteli pişirme kaplarında hazırlanan yemekler çok daha fazla doygunluk verir ve güçlü iksir etkileri kazandırır. Bu görevi tamamlayarak ustalığınızı kanıtlayın."],
            'tasks': [
                {
                    'type': 'checkmark',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'minecraft:diamond',
                    'count': 3,
                },
                {
                    'type': 'item',
                    'item': 'minecraft:golden_apple',
                    'count': 4,
                },
            ],
        },
    ],
}
