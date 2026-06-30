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
            'shape': 'gear',
            'size': 1.25,
            'title_en': 'The Heart of the Kitchen',
            'title_tr': 'Mutfağın Kalbi',
            'subtitle_en': 'The basic cooking pot and stove are the cornerstones of your kitchen.',
            'subtitle_tr': 'Temel tencere ve ocak, mutfağınızın temel taşlarıdır.',
            'desc_en': ["The Cooking Pot is the core of &eFarmer's Delight&r. Place it on a &eStove&r or Campfire to prepare nourishing meals with lasting effects. Master the pot, master survival."],
            'desc_tr': ["&eTencere (Cooking Pot)&r, &eFarmer's Delight&r modunun kalbidir. Uzun süreli etkileri olan besleyici yemekler hazırlamak için onu bir &eOcak (Stove)&r veya Kamp Ateşi üzerine yerleştirin. Tencereyi ustalaştır, hayatta kalmayı ustalaştır."],
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
            'key': 'farmhouse_meal',
            'x': 0.0,
            'y': 2.0,
            'dependency': 'cooking_pot',
            'title_en': 'A Farmhouse Meal',
            'title_tr': 'Çiftlik Evinden Bir Öğün',
            'subtitle_en': 'Cook a highly filling and nutritious meal.',
            'subtitle_tr': 'Doyurucu ve besleyici bir çiftlik yemeği pişir.',
            'desc_en': ["Prepare a proper farmhouse meal. Cook &eSteak and Potatoes&r from Farmer's Delight, a &eGoulash&r from Farm & Charm, or &eRatatouille&r for a vegetarian option. These meals provide excellent saturation and effects."],
            'desc_tr': ["Düzgün bir çiftlik evi öğünü hazırlayın. Farmer's Delight'tan &eBiftek ve Patates&r, Farm & Charm'dan &eGulaş&r veya vejetaryen seçenek olarak &eRatatouille&r pişirin. Bu yemekler mükemmel doygunluk ve etkiler sağlar."],
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
            'key': 'grand_feast',
            'x': 0.0,
            'y': 4.0,
            'shape': 'diamond',
            'dependency': 'farmhouse_meal',
            'title_en': 'The Grand Feast',
            'title_tr': 'Büyük Ziyafet',
            'subtitle_en': 'Prepare multi-serving feasts for sharing.',
            'subtitle_tr': 'Paylaşmak için çok porsiyonlu ziyafetler hazırla.',
            'desc_en': ["Prepare a full &eRoast Chicken Feast&r! Feasts are multi-serving blocks that can be placed and eaten by multiple players. They provide massive nourishment and status effects. A true chef's centerpiece achievement."],
            'desc_tr': ['Bütün bir &eTavuk Kızartması Ziyafeti (Roast Chicken Feast)&r hazırlayın! Ziyafetler, yerleştirilebilen ve birden fazla oyuncu tarafından yenebilen çok porsiyonlu bloklardır. Büyük miktarda besin ve durum etkisi sağlarlar. Gerçek bir şefin merkez eseri başarısı.'],
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
            'key': 'candlelight_dinner',
            'x': 0.0,
            'y': 6.0,
            'dependency': 'grand_feast',
            'title_en': 'A Candlelight Dinner',
            'title_tr': 'Mum Işığında Akşam Yemeği',
            'subtitle_en': 'Elevate dining to an art form with elegant meals.',
            'subtitle_tr': 'Şık yemeklerle sofra kültürünü bir sanat formuna yükselt.',
            'desc_en': ["&dLet's Do: Candlelight&r elevates dining to an art form. Craft a &eHearth&r, lay a fine table, and prepare Beef Wellington or Salmon on White Wine. Complete the experience with a Chef's outfit — Hat, Jacket, Pants, and Boots."],
            'desc_tr': ["&dLet's Do: Candlelight&r, yemek yemeyi bir sanat formuna yükseltir. bir &eŞömine (Hearth)&r yapın, şık bir masa kurun ve Dana Wellington veya Beyaz Şaraplı Somon hazırlayın. Şef kıyafetiyle deneyimi tamamlayın — Şapka, Ceket, Pantolon ve Botlar."],
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
            'key': 'master_chef',
            'x': 0.0,
            'y': 8.0,
            'shape': 'gear',
            'size': 1.5,
            'dependencies': ['candlelight_dinner', 'brewery'],
            'title_en': 'Master Chef',
            'title_tr': 'Usta Şef',
            'subtitle_en': 'Achieve the ultimate gastronomic mastery.',
            'subtitle_tr': 'Nihai gastronomi ustalığına ulaş.',
            'desc_en': ["You have mastered every culinary art — from humble field cooking to grand feasts, from vineyard to brewery, from spice routes to mechanical kitchens. Craft the &eNetherite Brewingstation&r as proof of your ultimate gastronomic mastery. You are the realm's greatest chef."],
            'desc_tr': ['Her mutfak sanatında ustalaştınız — alçakgönüllü tarla yemeklerinden büyük ziyafetlere, bağdan birahaneye, baharat yollarından mekanik mutfaklara. Nihai gastronomi ustalığınızın kanıtı olarak &eNetherite Demleme İstasyonu (Netherite Brewingstation)&r yapın. Bu krallığın en büyük şefisiniz.'],
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
        {
            'key': 'bakery_apprentice',
            'x': -2.0,
            'y': 0.0,
            'title_en': 'Bakery Apprentice',
            'title_tr': 'Fırıncı Çırağı',
            'subtitle_en': 'Start baking bread and learning the dough arts.',
            'subtitle_tr': 'Hamur sanatlarını öğrenmeye ve ekmek pişirmeye baş.',
            'desc_en': ["&dLet's Do Bakery&r brings the art of baking to life. Craft a &eTray&r, learn to shape dough, and bake your first bread. Cakes, croissants, and pastries await the dedicated baker!"],
            'desc_tr': ["&dLet's Do Bakery&r, fırıncılık sanatını hayata geçirir. bir &eTepsi (Tray)&r yapın, hamur şekillendirmeyi öğrenin ve ilk ekmeğinizi pişirin. Kekler, kruvasanlar ve hamur işleri özverili fırıncıyı bekliyor!"],
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
            'key': 'pastry_crafting',
            'x': -2.0,
            'y': 2.0,
            'dependency': 'bakery_apprentice',
            'title_en': 'Pastry Crafting',
            'title_tr': 'Hamur İşleri',
            'subtitle_en': 'Bake delicious cupcakes and sweet buns.',
            'subtitle_tr': 'Lezzetli kapkekler ve tatlı çörekler pişir.',
            'desc_en': ["Bake your first &eApple Cupcakes&r and learn to process sweet treats. Bakeries are all about presentation, so display your cakes proudly!"],
            'desc_tr': ["İlk &eElmalı Kapkeklerini (Apple Cupcake)&r pişir ve tatlı ikramları işlemeyi öğren. Fırıncılık tamamen sunumla ilgilidir, bu yüzden keklerini gururla sergile!"],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'bakery:apple_cupcake',
                },
                {
                    'type': 'item',
                    'item': 'bakery:cake_dough',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'bakery:apple_jam',
                },
            ],
        },
        {
            'key': 'delightful_bakery',
            'x': -2.0,
            'y': 4.0,
            'dependency': 'pastry_crafting',
            'title_en': 'Dessert Master',
            'title_tr': 'Tatlı Ustası',
            'subtitle_en': 'Create advanced multi-layered gateaus and traditional pastries.',
            'subtitle_tr': 'Gelişmiş katmanlı pastalar ve geleneksel tatlılar yap.',
            'desc_en': ["Craft traditional multi-layered &eBaklava&r and chocolate gateaus. These premium sweets are highly sought after by local villagers and provide amazing energy boosts."],
            'desc_tr': ["Geleneksel çok katmanlı &eBaklava&r ve çikolatalı pastalar (gateau) yap. Bu premium tatlılar yerel köylüler tarafından çok sevilir ve harika enerji artışları sağlar."],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'delightful:baklava',
                },
                {
                    'type': 'item',
                    'item': 'bakery:chocolate_gateau',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'delightful:blueberry_pie_slice',
                    'count': 3,
                },
                {
                    'type': 'item',
                    'item': 'minecraft:emerald',
                    'count': 4,
                },
            ],
        },
        {
            'key': 'winery',
            'x': -4.0,
            'y': 0.0,
            'title_en': 'The Art of Winemaking',
            'title_tr': 'Şarapçılık Sanatı',
            'subtitle_en': 'Grow grapes on vines and prepare to press juice.',
            'subtitle_tr': 'Asmalarda üzüm yetiştir ve şıra sıkmaya hazırlan.',
            'desc_en': ["&dLet's Do Vinery&r introduces grape cultivation and winemaking. Collect Red and White &eGrapes&r, plant them on vines, and press them into juice. A journey from vineyard to bottle begins."],
            'desc_tr': ["&dLet's Do Vinery&r, üzüm yetiştiriciliği ve şarap yapımını sunar. Kırmızı ve Beyaz &eÜzümleri&r toplayın, asmalara dikin ve suyunu sıkın. Bağdan şişeye bir yolculuk başlıyor."],
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
            'x': -4.0,
            'y': 2.0,
            'dependency': 'winery',
            'title_en': 'The Wine Cellar',
            'title_tr': 'Şarap Mahzeni',
            'subtitle_en': 'Age wine in barrels to unlock powerful properties.',
            'subtitle_tr': 'Güçlü özellikler kazanmak için şarabı fıçılarda yıllandır.',
            'desc_en': ["Build a proper wine production line: an &eApple Press&r for juicing, a &eFermentation Barrel&r for aging, and barrels for storage. Aged wines offer unique, powerful effects. Red Wine, White Wine, Apple Cider — each has its charm."],
            'desc_tr': ["Gerçek bir şarap üretim hattı kurun: Sıkma için &eElma Presi (Apple Press)&r, yıllandırma için &eFermantasyon Varili (Fermentation Barrel)&r ve depolama için fıçılar. Yıllandırılmış şaraplar benzersiz, güçlü etkiler sunar. Kırmızı Şarap, Beyaz Şarap, Elma Şırası — her birinin kendine has bir çekiciliği var."],
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
            'key': 'keg_fermentation',
            'x': -4.0,
            'y': 4.0,
            'dependency': 'wine_cellar',
            'title_en': 'The Art of Fermentation',
            'title_tr': 'Fermantasyon Sanatı',
            'subtitle_en': 'Use the keg to ferment cheese, mead, and spirits.',
            'subtitle_tr': 'Peynir, bal şarabı ve içkiler fermente etmek için fıçıyı kullan.',
            'desc_en': ["&eBrewin' And Chewin's&r Keg lets you ferment drinks, cheese, and specialty foods. Craft a &eKeg&r and discover Mead, Beer, Vodka, Rice Wine, and even Flaxen Cheese. Temperature matters — some recipes need the Keg to be warm or chilly."],
            'desc_tr': ["&eBrewin' And Chewin'in&r Fıçısı (Keg), içecekler, peynir ve özel yiyecekler fermente etmenizi sağlar. bir &eFıçı (Keg)&r yapın ve Bal Şarabı, Bira, Votka, Pirinç Şarası ve hatta Keten Peyniri keşfedin. Sıcaklık önemlidir — bazı tarifler Fıçının sıcak veya soğuk olmasını gerektirir."],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'brewinandchewin:keg',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'brewinandchewin:beer_tankard',
                    'count': 4,
                },
                {
                    'type': 'item',
                    'item': 'brewinandchewin:flaxen_cheese_wheel',
                },
            ],
        },
        {
            'key': 'brewery',
            'x': -4.0,
            'y': 6.0,
            'dependency': 'keg_fermentation',
            'title_en': 'The Brewery',
            'title_tr': 'Bira Fabrikası',
            'subtitle_en': 'Establish an Oktoberfest-style craft brewery.',
            'subtitle_tr': 'Oktoberfest tarzı bir zanaat birahanesi kur.',
            'desc_en': ["&dLet's Do Brewery&r introduces Oktoberfest-style brewing. Craft a &eWooden Brewingstation&r, grow &eHops&r, and brew classic Beers and Whiskeys. Try the special craft whiskeys — each has a unique effect. Prost!"],
            'desc_tr': ["&dLet's Do Brewery&r, Oktoberfest tarzı bira yapımını sunar. &eTaşım Demleme İstasyonu (Wooden Brewingstation)&r yapın, &eŞerbetçi Otu (Hops)&r yetiştirin ve klasik Biralar ve Visikiler üretin. Özel viskileri deneyin — her birinin benzersiz bir etkisi var. Prost!"],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'brewery:wooden_brewingstation',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'brewery:beer_hops',
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
            'key': 'tea_time',
            'x': 2.0,
            'y': 0.0,
            'dependency': 'cooking_pot',
            'title_en': 'Tea Time',
            'title_tr': 'Çay Saati',
            'subtitle_en': 'Brew soothing herbal teas for long-lasting buffs.',
            'subtitle_tr': 'Uzun süreli etkiler için yatıştırıcı bitki çayları demle.',
            'desc_en': ["&eFarmer's Respite&r brings tea and coffee culture. Craft a &eKettle&r, brew it on a heat source, and enjoy &eGreen Tea&r for gentle, long-lasting effects. Strong and Long brews last even longer."],
            'desc_tr': ["&eFarmer's Respite&r, çay ve kahve kültürünü getirir. Bir &eÇaydanlık (Kettle)&r yapın, ısı kaynağında demleyin ve hafif, uzun süreli etkiler için &eYeşil Çay (Green Tea)&r'ın tadını çıkarın. Güçlü ve Uzun demlemeler daha da uzun sürer."],
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
                    'item': 'farmersrespite:green_tea_leaves',
                    'count': 3,
                },
            ],
        },
        {
            'key': 'coffee_lover',
            'x': 2.0,
            'y': 2.0,
            'dependency': 'tea_time',
            'title_en': 'Coffee Connoisseur',
            'title_tr': 'Kahve Uzmanı',
            'subtitle_en': 'Cultivate coffee beans and brew a stimulating cup.',
            'subtitle_tr': 'Kahve çekirdekleri yetiştir ve uyarıcı bir fincan kahve demle.',
            'desc_en': ["Discover &eCoffee Beans&r from Farmer's Respite and Croptopia. Brew a strong cup of &eCoffee&r for a powerful speed boost. Coffee Cake makes for an excellent treat alongside your brew."],
            'desc_tr': ["Farmer's Respite ve Croptopia'dan &eKahve Çekirdeklerini&r keşfedin. Güçlü bir hız artışı için demlenmiş bir fincan &eKahve (Coffee)&r yapın. Kahve Kek, içeceğinizin yanında mükemmel bir atıştırmalıktır."],
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
            'key': 'food_diversity',
            'x': 2.0,
            'y': 4.0,
            'shape': 'diamond',
            'dependency': 'coffee_lover',
            'title_en': 'A World of Flavors',
            'title_tr': 'Lezzetlerin Dünyası',
            'subtitle_en': 'Track and expand your culinary palette for permanent health.',
            'subtitle_tr': 'Kalıcı sağlık için yemek yelpazeni genişlet ve takip et.',
            'desc_en': ['&cSpice of Life: Carrot Edition&r rewards you for eating diverse foods with permanent health bonuses. Craft the Food Book to track your progress. The more unique foods you try, the more &aMax Health&r you gain. Aim for 30 unique foods!'],
            'desc_tr': ['&cSpice of Life: Carrot Edition&r, çeşitli yiyecekler yediğiniz için sizi kalıcı sağlık bonuslarıyla ödüllendirir. İlerlemenizi takip etmek için Yemek Kitabı yapın. Ne kadar çok farklı yiyecek denerseniz, o kadar çok &aMaksimum Sağlık&r kazanırsınız. Olabildiğince farklı yiyecek hedefleyin!'],
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
            'key': 'mechanical_mixing',
            'x': 4.0,
            'y': 2.0,
            'dependency': 'cooking_pot',
            'title_en': 'Mechanical Mixing',
            'title_tr': 'Mekanik Karıştırma',
            'subtitle_en': 'Automate bulk ingredient mixing with Create mechanical mixing.',
            'subtitle_tr': 'Create mekanik karıştırıcı ile toplu malzeme karıştırmayı otomatikleştir.',
            'desc_en': ["Automate ingredient mixing by using Create's &eMechanical Mixer&r and a &eBasin&r. Mixing allows you to process multiple ingredients in bulk, laying the foundation for advanced food automation."],
            'desc_tr': ["Create modunun &eMekanik Karıştırıcısını&r ve bir &eHavzasını (Basin)&r kullanarak malzeme karıştırmayı otomatikleştirin. Karıştırma, birden fazla malzemeyi toplu olarak işlemenizi sağlayarak gelişmiş yemek otomasyonunun temelini atar."],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'create:mechanical_mixer',
                },
                {
                    'type': 'item',
                    'item': 'create:basin',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'create:whisk',
                },
                {
                    'type': 'item',
                    'item': 'create:andesite_alloy',
                    'count': 8,
                },
            ],
        },
        {
            'key': 'mechanical_kitchen',
            'x': 4.0,
            'y': 4.0,
            'dependency': 'mechanical_mixing',
            'title_en': 'The Mechanical Kitchen',
            'title_tr': 'Mekanik Mutfak',
            'subtitle_en': 'Build a fully automated cooking assembly line.',
            'subtitle_tr': 'Tam otomatik bir yemek montaj hattı kur.',
            'desc_en': ["Combine &eCreate&r's engineering with cooking! Use &eDeployers&r to automate Cutting Boards, Mechanical Presses for shaping, and the &eBlaze Stove&r from Create Central Kitchen for boosted cooking. The ultimate automated food factory awaits."],
            'desc_tr': ["&eCreate&r'in mühendisliğini yemek pişirmeyle birleştirin! Kesme Tahtalarını otomatikleştirmek için &eDeployer&r, şekillendirmek için Mekanik Pres ve geliştirilmiş pişirme için Create Central Kitchen'dan &eBlaze Ocak (Blaze Stove)&r kullanın. Nihai otomatik yemek fabrikası sizi bekliyor."],
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
    ],
}
