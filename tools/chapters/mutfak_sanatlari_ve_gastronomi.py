CHAPTER = {
    'order': 2,
    'filename': 'mutfak_sanatlari_ve_gastronomi',
    'title_en': 'Culinary Arts \\& Gastronomy',
    'title_tr': 'Mutfak Sanatları ve Gastronomi',
    'icon': 'farmersdelight:cooking_pot',
    'quests': [
        {
            'key': 'cooking_pot',
            'x': 0.0,
            'y': 0.0,
            'title_en': 'The Heart of the Kitchen',
            'title_tr': 'Mutfağın Kalbi',
            'desc_en': ["The Cooking Pot is the core of Farmer's Delight. Place it on a Stove or Campfire to prepare nourishing meals with lasting effects. Master the pot, master survival."],
            'desc_tr': ["Tencere (Cooking Pot), Farmer's Delight modunun kalbidir. Uzun süreli etkileri olan besleyici yemekler hazırlamak için onu bir Ocak veya Kamp Ateşi üzerine yerleştirin. Tencereyi ustalaştır, hayatta kalmayı ustalaştır."],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'farmersdelight:cooking_pot',
                },
                {
                    'type': 'item',
                    'item': 'farmersdelight:stove',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'minecraft:bowl',
                    'count': 4,
                },
                {
                    'type': 'item',
                    'item': 'farmersdelight:onion',
                    'count': 3,
                },
            ],
        },
        {
            'key': 'cutting_board',
            'x': 1.5,
            'y': 0.0,
            'title_en': 'Precision Cutting',
            'title_tr': 'Hassas Kesim',
            'desc_en': ['The Cutting Board lets you slice, dice, and process ingredients with a knife. Place items on it and right-click with a knife to break them down. Essential for advanced recipes.'],
            'desc_tr': ['Kesme Tahtası (Cutting Board), bıçakla malzemeleri dilimlemenizi, doğramanızı ve işlemenizi sağlar. Üzerine malzeme koyun ve bıçakla sağ tıklayarak parçalara ayırın. Gelişmiş tarifler için gereklidir.'],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'farmersdelight:cutting_board',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'farmersdelight:rich_soil',
                    'count': 4,
                },
            ],
        },
        {
            'key': 'bakery_apprentice',
            'x': -1.5,
            'y': 1.5,
            'dependency': 'cutting_board',
            'title_en': 'Bakery Apprentice',
            'title_tr': 'Fırıncı Çırağı',
            'desc_en': ["Let's Do Bakery brings the art of baking to life. Craft a Tray, learn to shape dough, and bake your first bread. Cakes, croissants, and pastries await the dedicated baker!"],
            'desc_tr': ["Let's Do Bakery, fırıncılık sanatını hayata geçirir. bir Tepsi yapın, hamur şekillendirmeyi öğrenin ve ilk ekmeğinizi pişirin. Kekler, kruvasanlar ve hamur işleri özverili fırıncıyı bekliyor!"],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'bakery:tray',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'bakery:sweet_dough',
                    'count': 4,
                },
                {
                    'type': 'item',
                    'item': 'minecraft:sugar',
                    'count': 6,
                },
            ],
        },
        {
            'key': 'farmers_breakfast',
            'x': 0.0,
            'y': 1.5,
            'dependency': 'cutting_board',
            'title_en': "Farmer's Breakfast",
            'title_tr': 'Çiftçi Kahvaltısı',
            'desc_en': ["Let's Do: Farm \\& Charm enriches farm life with new crops and meals. Grow Barley and Oats, raise Strawberries, and cook a hearty Farmer's Breakfast to start your day right."],
            'desc_tr': ["Let's Do: Farm \\& Charm, çiftlik yaşamını yeni ekinler ve yemeklerle zenginleştirir. Arpa ve Yulaf yetiştirin, Çilek toplayın ve güne doğru başlatan doyurucu bir Çiftçi Kahvaltısı pişirin."],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'farm_and_charm:farmers_breakfast',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'farm_and_charm:strawberry_seeds',
                    'count': 4,
                },
                {
                    'type': 'item',
                    'item': 'farm_and_charm:oat_seeds',
                    'count': 4,
                },
            ],
        },
        {
            'key': 'tea_time',
            'x': 1.5,
            'y': 1.5,
            'dependency': 'corn_field',
            'title_en': 'Tea Time',
            'title_tr': 'Çay Saati',
            'desc_en': ["Farmer's Respite brings tea and coffee culture. Craft a Kettle, brew it on a heat source, and enjoy Green Tea for gentle, long-lasting effects. Strong and Long brews last even longer."],
            'desc_tr': ["Farmer's Respite, çay ve kahve kültürünü getirir. Bir Çaydanlık yapın, ısı kaynağında demleyin ve hafif, uzun süreli etkiler için Yeşil Çay'ın tadını çıkarın. Güçlü ve Uzun demlemeler daha da uzun sürer."],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'farmersrespite:kettle',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'farmersrespite:green_tea',
                    'count': 4,
                },
                {
                    'type': 'item',
                    'item': 'farmersrespite:tea_seeds',
                    'count': 3,
                },
            ],
        },
        {
            'key': 'coffee_lover',
            'x': 1.5,
            'y': 3.0,
            'dependency': 'tea_time',
            'title_en': 'Coffee Connoisseur',
            'title_tr': 'Kahve Uzmanı',
            'desc_en': ["Discover coffee beans from Farmer's Respite and Croptopia. Brew a strong cup of Coffee for a powerful speed boost. Coffee Cake makes for an excellent treat alongside your brew."],
            'desc_tr': ["Farmer's Respite ve Croptopia'dan kahve çekirdeklerini keşfedin. Güçlü bir hız artışı için demlenmiş bir fincan Kahve yapın. Kahve Kek, içeceğinizin yanında mükemmel bir atıştırmalıktır."],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'farmersrespite:coffee_beans',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'farmersrespite:coffee',
                    'count': 3,
                },
                {
                    'type': 'item',
                    'item': 'farmersrespite:coffee_cake',
                },
            ],
        },
        {
            'key': 'winery',
            'x': -1.5,
            'y': 3.0,
            'dependency': 'seasons_awareness',
            'title_en': 'The Art of Winemaking',
            'title_tr': 'Şarapçılık Sanatı',
            'desc_en': ["Let's Do Vinery introduces grape cultivation and winemaking. Collect Red and White Grapes, plant them on vines, and press them into juice. A journey from vineyard to bottle begins."],
            'desc_tr': ["Let's Do Vinery, üzüm yetiştiriciliği ve şarap yapımını sunar. Kırmızı ve Beyaz Üzümleri toplayın, asmalara dikin ve suyunu sıkın. Bağdan şişeye bir yolculuk başlıyor."],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'vinery:red_grape',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'vinery:red_grape_seeds',
                    'count': 3,
                },
                {
                    'type': 'item',
                    'item': 'vinery:white_grape_seeds',
                    'count': 3,
                },
            ],
        },
        {
            'key': 'wine_cellar',
            'x': -1.5,
            'y': 4.5,
            'dependency': 'winery',
            'title_en': 'The Wine Cellar',
            'title_tr': 'Şarap Mahzeni',
            'desc_en': ['Build a proper wine production line: an Apple Press for juicing, a Fermentation Barrel for aging, and barrels for storage. Aged wines offer unique, powerful effects. Red Wine, White Wine, Apple Cider — each has its charm.'],
            'desc_tr': ['Gerçek bir şarap üretim hattı kurun: Sıkma için Elma Presi, yıllandırma için Fermantasyon Varili ve depolama için fıçılar. Yıllandırılmış şaraplar benzersiz, güçlü etkiler sunar. Kırmızı Şarap, Beyaz Şarap, Elma Şırası — her birinin kendine has bir çekiciliği var.'],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'vinery:apple_press',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'vinery:fermentation_barrel',
                },
                {
                    'type': 'item',
                    'item': 'vinery:wine_bottle',
                    'count': 4,
                },
            ],
        },
        {
            'key': 'farmhouse_meal',
            'x': 0.0,
            'y': 3.0,
            'dependency': 'cooking_pot',
            'title_en': 'A Farmhouse Meal',
            'title_tr': 'Çiftlik Evinden Bir Öğün',
            'desc_en': ["Prepare a proper farmhouse meal. Cook Steak and Potatoes from Farmer's Delight, a Goulash from Farm \\& Charm, or Ratatouille for a vegetarian option. These meals provide excellent saturation and effects."],
            'desc_tr': ["Düzgün bir çiftlik evi öğünü hazırlayın. Farmer's Delight'tan Biftek ve Patates, Farm \\& Charm'dan Gulaş veya vejetaryen seçenek olarak Ratatouille pişirin. Bu yemekler mükemmel doygunluk ve etkiler sağlar."],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'farmersdelight:steak_and_potatoes',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'farm_and_charm:goulash',
                },
                {
                    'type': 'item',
                    'item': 'farmersdelight:ratatouille',
                },
            ],
        },
        {
            'key': 'delightful_cuisine',
            'x': 0.0,
            'y': 4.5,
            'dependency': 'wine_cellar',
            'title_en': 'Delightful Creations',
            'title_tr': 'Lezzetli Yaratımlar',
            'desc_en': ['The Delightful mod adds exotic dishes and specialty knives. Try Coconut Curry, Baklava, Matcha, or Cheeseburger. Craft an Amethyst Knife or Quartz Knife for harvesting unique materials.'],
            'desc_tr': ['Delightful modu egzotik yemekler ve özel bıçaklar ekler. Hindistan Cevizi Curry, Baklava, Çay Tozu (Matcha) veya Cheeseburger deneyin. Benzersiz malzemeleri hasat etmek için Ametist Bıçak veya Kuvars Bıçak yapın.'],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'delightful:coconut_curry',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'delightful:matcha',
                    'count': 3,
                },
                {
                    'type': 'item',
                    'item': 'delightful:amethyst_knife',
                },
            ],
        },
        {
            'key': 'brewery',
            'x': -3.0,
            'y': 3.0,
            'dependency': 'delightful_cuisine',
            'title_en': 'The Brewery',
            'title_tr': 'Bira Fabrikası',
            'desc_en': ["Let's Do Brewery introduces Oktoberfest-style brewing. Craft a Wooden Brewingstation, grow Hops, and brew classic Beers and Whiskeys. Try the special craft whiskeys — each has a unique effect. Prost!"],
            'desc_tr': ["Let's Do Brewery, Oktoberfest tarzı bira yapımını sunar. Taşım Demleme İstasyonu yapın, Şerbetçi Otu yetiştirin ve klasik Biralar ve Visikiler üretin. Özel viskileri deneyin — her birinin benzersiz bir etkisi var. Prost!"],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'brewery:wooden_brewingstation',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'brewery:hops_seeds',
                    'count': 3,
                },
                {
                    'type': 'item',
                    'item': 'brewery:beer_mug',
                    'count': 2,
                },
            ],
        },
        {
            'key': 'keg_fermentation',
            'x': -3.0,
            'y': 1.5,
            'dependency': 'farmhouse_meal',
            'title_en': 'The Art of Fermentation',
            'title_tr': 'Fermantasyon Sanatı',
            'desc_en': ["Brewin' And Chewin's Keg lets you ferment drinks, cheese, and specialty foods. Craft a Keg and discover Mead, Beer, Vodka, Rice Wine, and even Flaxen Cheese. Temperature matters — some recipes need the Keg to be warm or chilly."],
            'desc_tr': ["Brewin' And Chewin'in Fıçısı (Keg), içecekler, peynir ve özel yiyecekler fermente etmenizi sağlar. bir Fıçı yapın ve Bal Şarabı, Bira, Votka, Pirinç Şarası ve hatta Keten Peyniri keşfedin. Sıcaklık önemlidir — bazı tarifler Fıçının sıcak veya soğuk olmasını gerektirir."],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'brewinandchewin:keg',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'brewinandchewin:tankard',
                    'count': 4,
                },
                {
                    'type': 'item',
                    'item': 'brewinandchewin:flaxen_cheese_wheel',
                },
            ],
        },
        {
            'key': 'grand_feast',
            'x': 0.0,
            'y': 6.0,
            'dependency': 'keg_fermentation',
            'title_en': 'The Grand Feast',
            'title_tr': 'Büyük Ziyafet',
            'desc_en': ["Prepare a full Roast Chicken Feast! Feasts are multi-serving blocks that can be placed and eaten by multiple players. They provide massive nourishment and status effects. A true chef's centerpiece achievement."],
            'desc_tr': ['Bütün bir Tavuk Kızartması Ziyafeti hazırlayın! Ziyafetler, yerleştirilebilen ve birden fazla oyuncu tarafından yenebilen çok porsiyonlu bloklardır. Büyük miktarda besin ve durum etkisi sağlarlar. Gerçek bir şefin merkez eseri başarısı.'],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'farmersdelight:roast_chicken_block',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'minecraft:golden_apple',
                },
                {
                    'type': 'item',
                    'item': 'farmersdelight:honey_glazed_ham_block',
                },
            ],
        },
        {
            'key': 'food_diversity',
            'x': 1.5,
            'y': 6.0,
            'dependency': 'irrigation',
            'title_en': 'A World of Flavors',
            'title_tr': 'Lezzetlerin Dünyası',
            'desc_en': ['Spice of Life: Carrot Edition rewards you for eating diverse foods with permanent health bonuses. Craft the Food Book to track your progress. The more unique foods you try, the more max health you gain. Aim for 30 unique foods!'],
            'desc_tr': ['Spice of Life: Carrot Edition, çeşitli yiyecekler yediğiniz için sizi kalıcı sağlık bonuslarıyla ödüllendirir. İlerlemenizi takip etmek için Yemek Kitabı yapın. Ne kadar çok farklı yiyecek denerseniz, o kadar çok maksimum sağlık kazanırsınız. 30 farklı yiyecek hedefleyin!'],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'solcarrot:food_book',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'minecraft:golden_carrot',
                    'count': 5,
                },
                {
                    'type': 'item',
                    'item': 'croptopia:the_big_breakfast',
                },
            ],
        },
        {
            'key': 'candlelight_dinner',
            'x': 0.0,
            'y': 7.5,
            'dependency': 'grand_feast',
            'title_en': 'A Candlelight Dinner',
            'title_tr': 'Mum Işığında Akşam Yemeği',
            'desc_en': ["Let's Do: Candlelight elevates dining to an art form. Craft a Hearth, lay a fine table, and prepare Beef Wellington or Salmon on White Wine. Complete the experience with a Chef's outfit — Hat, Jacket, Pants, and Boots."],
            'desc_tr': ["Let's Do: Candlelight, yemek yemeyi bir sanat formuna yükseltir. bir Şömine yapın, şık bir masa kurun ve Dana Wellington veya Beyaz Şaraplı Somon hazırlayın. Şef kıyafetiyle deneyimi tamamlayın — Şapka, Ceket, Pantolon ve Botlar."],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'candlelight:hearth',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'candlelight:chefs_jacket',
                },
                {
                    'type': 'item',
                    'item': 'candlelight:cooking_hat',
                },
                {
                    'type': 'item',
                    'item': 'candlelight:chocolate_box',
                },
            ],
        },
        {
            'key': 'mechanical_kitchen',
            'x': -1.5,
            'y': 7.5,
            'dependency': 'food_diversity',
            'title_en': 'The Mechanical Kitchen',
            'title_tr': 'Mekanik Mutfak',
            'desc_en': ["Combine Create's engineering with cooking! Use Deployers to automate Cutting Boards, Mechanical Presses for shaping, and the Blazing Stove from Create Central Kitchen for boosted cooking. The ultimate automated food factory awaits."],
            'desc_tr': ["Create'in mühendisliğini yemek pişirmeyle birleştirin! Kesme Tahtalarını otomatikleştirmek için Deployer, şekillendirmek için Mekanik Pres ve geliştirilmiş pişirme için Create Central Kitchen'dan Blazing Ocak kullanın. Nihai otomatik yemek fabrikası sizi bekliyor."],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'create:deployer',
                },
                {
                    'type': 'item',
                    'item': 'create:mechanical_press',
                },
                {
                    'type': 'item',
                    'item': 'create_central_kitchen:blaze_stove',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'create:brass_ingot',
                    'count': 4,
                },
                {
                    'type': 'item',
                    'item': 'create_central_kitchen:cooking_guide',
                },
            ],
        },
        {
            'key': 'master_chef',
            'x': 0.0,
            'y': 9.0,
            'dependencies': ['candlelight_dinner', 'brewery'],
            'title_en': 'Master Chef',
            'title_tr': 'Usta Şef',
            'desc_en': ["You have mastered every culinary art — from humble field cooking to grand feasts, from vineyard to brewery, from spice routes to mechanical kitchens. Craft the Netherite Brewingstation as proof of your ultimate gastronomic mastery. You are the realm's greatest chef."],
            'desc_tr': ['Her mutfak sanatında ustalaştınız — alçakgönüllü tarla yemeklerinden büyük ziyafetlere, bağdan birahaneye, baharat yollarından mekanik mutfaklara. Nihai gastronomi ustalığınızın kanıtı olarak Netherite Demleme İstasyonu yapın. Bu krallığın en büyük şefisiniz.'],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'brewery:netherite_brewingstation',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'minecraft:netherite_ingot',
                },
                {
                    'type': 'item',
                    'item': 'candlelight:dinner_bell',
                },
                {
                    'type': 'item',
                    'item': 'minecraft:diamond',
                    'count': 3,
                },
            ],
        },
    ],
}
