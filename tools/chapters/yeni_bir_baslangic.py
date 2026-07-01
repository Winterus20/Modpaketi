CHAPTER = {
    'order': 0,
    'filename': 'yeni_bir_baslangic',
    'title_en': 'A New Beginning',
    'title_tr': 'Yeni Bir Başlangıç',
    'icon': 'minecraft:grass_block',
    'quests': [
        {
            'key': 'welcome',
            'x': 0.0,
            'y': 0.0,
            'shape': 'heart',
            'size': 1.5,
            'title_en': 'Welcome to Harbor Haven!',
            'title_tr': "Harbor Haven'e Hoş Geldiniz!",
            'subtitle_en': 'A warm welcome to your new cozy life-sim adventure.',
            'subtitle_tr': 'Yeni, huzurlu yaşam simülasyonu macerana sıcak bir hoş geldin.',
            'desc_en': ['Welcome to your new peaceful life! &6Harbor Haven&r is a cozy life-sim modpack about fishing, farming, cooking, and exploring a world full of seasons and secrets. Cast a line by the river, grow crops in your garden, cook warm meals, and build your dream homestead. Open your &aQuest Book&r in your inventory to guide your journey.'],
            'desc_tr': ["Yeni ve huzurlu yaşamına hoş geldin! &6Harbor Haven&r, mevsimlerin ve sırların dünyasında balıkçılık, tarım, yemek pişirme ve keşif üzerine kurulu bir yaşam simülasyonudur. Nehir kenarında olta at, bahçende sebze yetiştir, sıcak yemekler pişir ve hayalindeki çiftliği kur. Yolculuğuna rehberlik etmesi için envanterindeki &aGörev Kitabı&r'nı aç."],
            'tasks': [
                {
                    'type': 'checkmark',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'minecraft:bread',
                    'count': 3,
                },
            ],
        },
        {
            'key': 'basic_survival',
            'x': 0.0,
            'y': -1.5,
            'shape': 'gear',
            'size': 1.25,
            'dependency': 'welcome',
            'title_en': 'First Steps',
            'title_tr': 'İlk Adımlar',
            'subtitle_en': 'Crafting is the foundation of everything.',
            'subtitle_tr': 'İşleme, bu dünyadaki her şeyin temelidir.',
            'desc_en': ["Before you can fish, farm, or explore, you need the basics. Craft a &eCrafting Table&r — it's the foundation of everything you'll build in this world. Once you have it, a whole world of possibilities opens up!"],
            'desc_tr': ['Balık tutmadan, çiftçilik yapmadan veya keşfe çıkmadan önce temellere ihtiyacın var. Bir &eİşleme Tezgahı&r yap — bu dünyada inşa edeceğin her şeyin temeli odur. Tezgahı hazırladıktan sonra sonsuz olasılıklar seni bekliyor!'],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'minecraft:crafting_table',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'minecraft:stone_axe',
                },
                {
                    'type': 'item',
                    'item': 'minecraft:torch',
                    'count': 8,
                },
            ],
        },
        {
            'key': 'first_cast',
            'x': -1.5,
            'y': -1.5,
            'dependency': 'basic_survival',
            'title_en': 'First Fishing Rod',
            'title_tr': 'İlk Olta',
            'subtitle_en': 'Prepare your basic wooden angling tool.',
            'subtitle_tr': 'Temel ahşap balıkçılık aletini hazırla.',
            'desc_en': ["The heart of this modpack is fishing, driven by the &bTide&r mod. Craft a basic &eWooden Fishing Rod&r to begin your angling journey. Keep in mind that vanilla fishing rods are overridden to support the custom fishing mechanics!"],
            'desc_tr': ['Bu mod paketinin kalbi &bTide&r modu ile yönlendirilen balıkçılıktır. Balıkçılık macerana başlamak için temel bir &eAhşap Olta&r yap. Vanilya oltaların, özel balıkçılık mekaniklerini desteklemek üzere güncellendiğini unutma!'],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'minecraft:fishing_rod',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'aquaculture:worm',
                    'count': 4,
                },
                {
                    'type': 'item',
                    'item': 'tide:fishing_journal',
                },
            ],
        },
        {
            'key': 'first_fish',
            'x': -3.0,
            'y': -1.5,
            'shape': 'diamond',
            'dependency': 'first_cast',
            'title_en': 'First Catch',
            'title_tr': 'İlk Av',
            'subtitle_en': 'Catch your first fish in the wild.',
            'subtitle_tr': 'Doğada ilk balığını yakala.',
            'desc_en': ["Now that you have a fishing rod, head to the nearest body of water and catch your first fish. &eCod&r or other common fish are perfect starting catches. Don't forget that different fish appear depending on the season, time, and biome!"],
            'desc_tr': ['Artık bir oltan olduğuna göre, en yakın su kütlesine git ve ilk balığını yakala. &eMorina (Cod)&r veya diğer yaygın balıklar başlangıç için memnuniyet vericidir. Farklı balıkların mevsime, zamana ve biyoma göre ortaya çıktığını unutma!'],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'minecraft:cod',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'aquaculture:box',
                },
            ],
        },
        {
            'key': 'backpack',
            'x': -1.5,
            'y': -3.0,
            'dependency': 'basic_survival',
            'title_en': 'Portable Storage',
            'title_tr': 'Taşınabilir Depolama',
            'subtitle_en': 'Upgrade your inventory with a custom backpack.',
            'subtitle_tr': 'Envanterini özel bir sırt çantasıyla genişlet.',
            'desc_en': ['&dSophisticated Backpacks&r are highly customizable, upgradable backpack items that you can wear or place. Craft a basic Leather Backpack to ease your inventory management during exploration.', 'Tip: The &eCarry On&r mod lets you pick up small blocks like chests and furnaces by shift-right-clicking — combine it with your backpack for ultimate mobility!'],
            'desc_tr': ['&dSophisticated Backpacks&r, giyebileceğiniz veya yerleştirebileceğiniz, son derece özelleştirilebilir ve geliştirilebilir sırt çantalarıdır. Keşif sırasında envanter yönetiminizi kolaylaştırmak için temel bir Deri Sırt Çantası yapın.', 'İpucu: &eCarry On&r modu, sandık ve ocak gibi küçük blokları shift+sağ tıklayarak kaldırmanıza olanak tanır — sırt çantanızla birlikte kullanarak ultimate hareketlilik elde edin!'],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'sophisticatedbackpacks:backpack',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'minecraft:leather',
                    'count': 4,
                },
                {
                    'type': 'item',
                    'item': 'minecraft:string',
                    'count': 4,
                },
            ],
        },
        {
            'key': 'sleeping_bag',
            'x': -1.5,
            'y': -4.5,
            'dependency': 'backpack',
            'title_en': 'Sweet Dreams on the Go',
            'title_tr': 'Yolda Tatlı Rüyalar',
            'subtitle_en': 'Sleep through the night without resetting spawn.',
            'subtitle_tr': 'Doğma noktanı sıfırlamadan geceyi uyu.',
            'desc_en': ['&eComforts sleeping bags&r allow you to sleep through the night without resetting your spawn point. Perfect for long journeys across the world!'],
            'desc_tr': ['&eComforts uyku tulumları&r, doğma noktanızı sıfırlamadan geceyi uyuyarak geçirmenizi sağlar. Dünya genelindeki uzun yolculuklar için mükemmeldir!'],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'comforts:sleeping_bag_white',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'minecraft:white_wool',
                    'count': 2,
                },
            ],
        },
        {
            'key': 'compasses',
            'x': -3.0,
            'y': -3.0,
            'dependency': 'backpack',
            'title_en': 'Navigating Nature',
            'title_tr': 'Doğada Yol Bulmak',
            'subtitle_en': 'Find biomes and structures in this vast world.',
            'subtitle_tr': 'Bu engin dünyadaki biyomları ve yapıları bul.',
            'desc_en': ["&aNature's Compass&r and &aExplorer's Compass&r are vital tools for finding biomes and structures in this vast world. Craft either compass to help guide your exploration."],
            'desc_tr': ["&aNature's Compass (Doğa Pusulası)&r ve &aExplorer's Compass (Kaşif Pusulası)&r, bu engin dünyadaki biyomları ve yapıları bulmak için hayati araçlardır. Keşfinize rehberlik etmesi için iki pusuladan birini yapın."],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'naturescompass:naturescompass',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'minecraft:ender_pearl',
                    'count': 2,
                },
            ],
        },
        {
            'key': 'waystone',
            'x': -3.0,
            'y': -4.5,
            'shape': 'hexagon',
            'dependency': 'compasses',
            'title_en': 'Fast Travel',
            'title_tr': 'Hızlı Yolculuk',
            'subtitle_en': 'Teleport between activated waystones.',
            'subtitle_tr': 'Etkinleştirilmiş yol taşları arasında ışınlan.',
            'desc_en': ['&9Waystones&r let you teleport between any waystones you have activated, for a small emerald fee. Craft a Waystone, place it at your base, and activate it by right-clicking. Carry a &bReturn Scroll&r to warp home from anywhere.'],
            'desc_tr': ["&9Waystone'lar (Yol Taşları)&r, küçük bir zümrüt karşılığında etkinleştirdiğiniz tüm yol taşları arasında ışınlanmanızı sağlar. Bir Yol Taşı yapın, üssünüze yerleştirin ve sağ tıklayarak etkinleştirin. Her yerden eve dönmek için bir &bDönüş Parşömeni (Return Scroll)&r taşıyın."],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'waystones:waystone',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'waystones:return_scroll',
                    'count': 3,
                },
            ],
        },
        {
            'key': 'knife_and_board',
            'x': 1.5,
            'y': -1.5,
            'dependency': 'basic_survival',
            'title_en': 'Kitchen Preparation',
            'title_tr': 'Mutfak Hazırlıkları',
            'subtitle_en': 'Flint knives and cutting boards are essential.',
            'subtitle_tr': 'Çakmaktaşı bıçaklar ve kesme tahtaları elzemdir.',
            'desc_en': ["&eFarmer's Delight&r introduces the Cutting Board and Knives, which are essential for preparing ingredients and obtaining straw from wild grass. Craft a &eFlint Knife&r and a &eCutting Board&r to begin your culinary journey."],
            'desc_tr': ["&eFarmer's Delight&r modu, malzemeleri hazırlamak ve yabani otlardan saman elde etmek için temel olan Kesme Tahtası ve Bıçaklar ekler. Aşçılık yolculuğuna başlamak için bir &eÇakmaktaşı Bıçak&r ve bir &eKesme Tahtası&r yap."],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'farmersdelight:flint_knife',
                },
                {
                    'type': 'item',
                    'item': 'farmersdelight:cutting_board',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'farmersdelight:straw',
                    'count': 4,
                },
                {
                    'type': 'item',
                    'item': 'farmersdelight:canvas',
                    'count': 2,
                },
            ],
        },
        {
            'key': 'sol_carrot',
            'x': 3.0,
            'y': -1.5,
            'shape': 'diamond',
            'dependency': 'knife_and_board',
            'title_en': 'A Diverse Diet',
            'title_tr': 'Çeşitli Beslenme',
            'subtitle_en': 'Eat unique foods to gain extra hearts.',
            'subtitle_tr': 'Ekstra kalp kazanmak için benzersiz yiyecekler ye.',
            'desc_en': ['&cSpice of Life (Carrot Edition)&r rewards you for eating unique foods. Eating new kinds of food grants permanent &aextra hearts&r! Collect and eat different foods to increase your max health. Start by gathering these basic foods.'],
            'desc_tr': ['&cSpice of Life (Carrot Edition)&r sizi benzersiz yiyecekler yediğiniz için ödüllendirir. Yeni yiyecek türleri yemek kalıcı &aekstra kalp&r kazandırır! Maksimum sağlığınızı artırmak için farklı yiyecekleri toplayın ve yiyin. Bu temel yiyecekleri toplayarak başlayın.'],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'minecraft:apple',
                },
                {
                    'type': 'item',
                    'item': 'minecraft:sweet_berries',
                },
                {
                    'type': 'item',
                    'item': 'minecraft:carrot',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'minecraft:golden_carrot',
                    'count': 4,
                },
            ],
        },
        {
            'key': 'seasons',
            'x': 1.5,
            'y': -3.0,
            'dependency': 'basic_survival',
            'title_en': 'Changing Seasons',
            'title_tr': 'Değişen Mevsimler',
            'subtitle_en': "Understand Serene Seasons' time progression.",
            'subtitle_tr': "Serene Seasons'ın zaman akışını kavra.",
            'desc_en': ['&6Serene Seasons&r alters crop fertility and temperature over time. Crops only grow in their fertile seasons, and winters can be freezing! Craft a Calendar to keep track of time and plan your harvests. A Season Sensor can also emit a redstone signal when a chosen season arrives, great for automating greenhouses.'],
            'desc_tr': ['&6Serene Seasons&r mevsimleri, bitkilerin verimliliğini ve sıcaklığı zamanla değiştirir. Ekinler sadece verimli oldukları mevsimlerde büyür ve kışlar dondurucu olabilir! Zamanı takip etmek ve hasatlarınızı planlamak için bir Takvim yapın. Bir Mevsim Sensörü (Season Sensor) seçtiğiniz mevsim geldiğinde redstone sinyali verir; seraları otomatikleştirmek için harikadır.'],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'sereneseasons:calendar',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'sereneseasons:season_sensor',
                },
            ],
        },
        {
            'key': 'market',
            'x': 1.5,
            'y': -4.5,
            'shape': 'hexagon',
            'dependency': 'seasons',
            'title_en': 'The Trading Market',
            'title_tr': 'Ticaret Pazarı',
            'subtitle_en': 'Buy seeds and saplings using emeralds.',
            'subtitle_tr': 'Zümrüt kullanarak tohum ve fidan satın al.',
            'desc_en': ['&eFarming for Blockheads&r adds a &eMarket&r where you can trade emeralds for seeds, saplings, and other farming supplies. Once you understand the seasons, craft a Market and place it to browse all the seeds the modpack has to offer. Plan your crops according to the current season!'],
            'desc_tr': ['&eFarming for Blockheads&r, zümrüt karşılığında tohumlar, fidanlar ve diğer çiftlik malzemelerini takas edebileceğiniz bir &ePazar&r ekler. Mevsimleri anladıktan sonra bir Pazar yapıp yerleştirin ve mod paketindeki tüm tohumlara göz atın. Ekinlerinizi mevcut mevsime göre planlayın!'],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'farmingforblockheads:market',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'minecraft:wheat_seeds',
                    'count': 8,
                },
                {
                    'type': 'item',
                    'item': 'minecraft:carrot',
                    'count': 4,
                },
            ],
        },
    ],
}
