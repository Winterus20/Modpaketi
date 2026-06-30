CHAPTER = {
    'order': 1,
    'filename': 'toprak_ana_ve_hasat_zamani',
    'title_en': 'Mother Earth & Harvest Time',
    'title_tr': 'Toprak Ana ve Hasat Zamanı',
    'icon': 'minecraft:wheat',
    'quests': [
        {
            'key': 'first_harvest',
            'x': 0.0,
            'y': 0.0,
            'title_en': 'The First Harvest',
            'title_tr': 'İlk Hasat',
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
            'x': 0.0,
            'y': 1.5,
            'dependency': 'cutting_board',
            'title_en': 'Reading the Seasons',
            'title_tr': 'Mevsimleri Okumak',
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
            'key': 'corn_field',
            'x': -1.5,
            'y': 3.0,
            'dependency': 'cutting_board',
            'title_en': 'The Corn Field',
            'title_tr': 'Mısır Tarlası',
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
            'key': 'irrigation',
            'x': 0.0,
            'y': 4.5,
            'dependency': 'farmers_breakfast',
            'title_en': 'Automated Irrigation',
            'title_tr': 'Otomatik Sulama',
            'desc_en': ['The Water Sprinkler from Farm \\& Charm hydrates and accelerates nearby crops automatically. Place it above water and watch your fields thrive. Also try Fertilized Soil for even richer harvests.'],
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
            'key': 'compact_farming',
            'x': 0.0,
            'y': 6.0,
            'dependency': 'bakery_apprentice',
            'title_en': 'Compact Farming',
            'title_tr': 'Kompakt Tarım',
            'desc_en': ['Botany Pots let you grow crops in a single block — perfect for indoor farms or space-limited builds. Place soil and a seed in the pot and watch it grow. Upgrade to Hopper Botany Pots for auto-collection.'],
            'desc_tr': ["Botany Pots, tek bir blokta ekin yetiştirmenizi sağlar — iç mekan çiftlikleri veya alan sınırlı yapılar için mükemmeldir. Saksıya toprak ve tohum koyun ve büyümesini izleyin. Otomatik toplama için Hopper Botany Pots'a yükseltin."],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'botanypots:terracotta_botany_pot',
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
            'key': 'spice_route',
            'x': 0.0,
            'y': 7.5,
            'dependency': 'compact_farming',
            'title_en': 'The Spice Route',
            'title_tr': 'Baharat Yolu',
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
            'x': 1.5,
            'y': 3.0,
            'dependency': 'spice_route',
            'title_en': 'The Orchard',
            'title_tr': 'Meyve Bahçesi',
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
    ],
}
