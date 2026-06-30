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
            'title_en': 'Welcome to Balik!',
            'title_tr': 'Balık Mod Paketine Hoş Geldiniz!',
            'desc_en': ['Welcome to your new peaceful life! Balik is a cozy life-sim modpack about fishing, farming, cooking, and exploring a world full of seasons and secrets. Cast a line by the river, grow crops in your garden, cook warm meals, and build your dream homestead. Open your Quest Book to guide your journey.'],
            'desc_tr': ["Yeni ve huzurlu yaşamına hoş geldin! Balık, mevsimlerin ve sırların dünyasında balıkçılık, tarım, yemek pişirme ve keşif üzerine kurulu bir yaşam simülasyonudur. Nehir kenarında olta at, bahçende sebze yetiştir, sıcak yemekler pişir ve hayalindeki çiftliği kur. Yolculuğuna rehberlik etmesi için Görev Kitabı'nı aç."],
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
            'y': -2.0,
            'dependency': 'welcome',
            'title_en': 'First Steps',
            'title_tr': 'İlk Adımlar',
            'desc_en': ["Before you can fish, farm, or explore, you need the basics. Craft a Crafting Table — it's the foundation of everything you'll build in this world. Once you have it, a whole world of possibilities opens up!"],
            'desc_tr': ['Balık tutmadan, çiftçilik yapmadan veya keşfe çıkmadan önce temellere ihtiyacın var. Bir İşleme Tezgahı yap — bu dünyada inşa edeceğin her şeyin temeli odur. Tezgahı hazırladıktan sonra sonsuz olasılıklar seni bekliyor!'],
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
            'key': 'seasons',
            'x': 2.0,
            'y': -3.0,
            'dependency': 'basic_survival',
            'title_en': 'Changing Seasons',
            'title_tr': 'Değişen Mevsimler',
            'desc_en': ['Serene Seasons alters crop fertility and temperature over time. Crops only grow in their fertile seasons, and winters can be freezing! Craft a Calendar to keep track of time and plan your harvests. A Season Sensor can also emit a redstone signal when a chosen season arrives, great for automating greenhouses.'],
            'desc_tr': ['Serene Seasons mevsimleri, bitkilerin verimliliğini ve sıcaklığı zamanla değiştirir. Ekinler sadece verimli oldukları mevsimlerde büyür ve kışlar dondurucu olabilir! Zamanı takip etmek ve hasatlarınızı planlamak için bir Takvim yapın. Bir Mevsim Sensörü (Season Sensor) seçtiğiniz mevsim geldiğinde redstone sinyali verir; seraları otomatikleştirmek için harikadır.'],
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
            'key': 'sol_carrot',
            'x': 3.0,
            'y': -1.0,
            'dependency': 'basic_survival',
            'title_en': 'A Diverse Diet',
            'title_tr': 'Çeşitli Beslenme',
            'desc_en': ['Spice of Life (Carrot Edition) rewards you for eating unique foods. Eating new kinds of food grants permanent extra hearts! Collect and eat different foods to increase your max health. Start by gathering these basic foods.'],
            'desc_tr': ['Spice of Life (Carrot Edition) sizi benzersiz yiyecekler yediğiniz için ödüllendirir. Yeni yiyecek türleri yemek kalıcı ekstra kalp kazandırır! Maksimum sağlığınızı artırmak için farklı yiyecekleri toplayın ve yiyin. Bu temel yiyecekleri toplayarak başlayın.'],
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
            'key': 'backpack',
            'x': -2.0,
            'y': -3.0,
            'dependency': 'basic_survival',
            'title_en': 'Portable Storage',
            'title_tr': 'Taşınabilir Depolama',
            'desc_en': ['Sophisticated Backpacks are highly customizable, upgradable backpack items that you can wear or place. Craft a basic Leather Backpack to ease your inventory management during exploration.', 'Tip: The Carry On mod lets you pick up small blocks like chests and furnaces by shift-right-clicking — combine it with your backpack for ultimate mobility!'],
            'desc_tr': ['Sophisticated Backpacks, giyebileceğiniz veya yerleştirebileceğiniz, son derece özelleştirilebilir ve geliştirilebilir sırt çantalarıdır. Keşif sırasında envanter yönetiminizi kolaylaştırmak için temel bir Deri Sırt Çantası yapın.', 'İpucu: Carry On modu, sandık ve ocak gibi küçük blokları shift+sağ tıklayarak kaldırmanıza olanak tanır — sırt çantanızla birlikte kullanarak ultimate hareketlilik elde edin!'],
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
            'key': 'first_cast',
            'x': -3.0,
            'y': -1.0,
            'dependency': 'basic_survival',
            'title_en': 'First Cast',
            'title_tr': 'İlk Olta',
            'desc_en': ["The heart of this modpack is fishing! Head to the nearest river or ocean, catch your first fish, and begin your angling journey. The Aquaculture mod replaces vanilla rods with durable, upgradeable metal ones. As a reward, here's an Iron Fishing Rod and some worms to get you started. Tight lines!"],
            'desc_tr': ['Bu mod paketinin kalbi balıkçılıktır! En yakın nehir veya okyanusa git, ilk balığını yakala ve balıkçılık serüvenine başla. Aquaculture modu, vanilya oltalarını dayanıklı ve geliştirilebilir metal oltalarla değiştirir. Ödül olarak, başlaman için bir Demir Olta ve birkaç solucan al. Rastgele!'],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'minecraft:cod',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'aquaculture:iron_fishing_rod',
                },
                {
                    'type': 'item',
                    'item': 'aquaculture:worm',
                    'count': 4,
                },
            ],
        },
        {
            'key': 'sleeping_bag',
            'x': -2.0,
            'y': -5.0,
            'dependency': 'backpack',
            'title_en': 'Sweet Dreams on the Go',
            'title_tr': 'Yolda Tatlı Rüyalar',
            'desc_en': ['Comforts sleeping bags allow you to sleep through the night without resetting your spawn point. Perfect for long journeys across the world!'],
            'desc_tr': ['Comforts uyku tulumları, doğma noktanızı sıfırlamadan geceyi uyuyarak geçirmenizi sağlar. Dünya genelindeki uzun yolculuklar için mükemmeldir!'],
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
            'dependency': 'first_cast',
            'title_en': 'Navigating Nature',
            'title_tr': 'Doğada Yol Bulmak',
            'desc_en': ["Nature's Compass and Explorer's Compass are vital tools for finding biomes and structures in this vast world. Craft either compass to help guide your exploration."],
            'desc_tr': ["Nature's Compass (Doğa Pusulası) ve Explorer's Compass (Kaşif Pusulası), bu engin dünyadaki biyomları ve yapıları bulmak için hayati araçlardır. Keşfinize rehberlik etmesi için iki pusuladan birini yapın."],
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
            'x': 3.0,
            'y': -3.0,
            'dependency': 'sol_carrot',
            'title_en': 'Fast Travel',
            'title_tr': 'Hızlı Yolculuk',
            'desc_en': ['Waystones let you teleport between any waystones you have activated, for a small emerald fee. Craft a Waystone, place it at your base, and activate it by right-clicking. Carry a Return Scroll to warp home from anywhere.'],
            'desc_tr': ["Waystone'lar (Yol Taşları), küçük bir zümrüt karşılığında etkinleştirdiğiniz tüm yol taşları arasında ışınlanmanızı sağlar. Bir Yol Taşı yapın, üssünüze yerleştirin ve sağ tıklayarak etkinleştirin. Her yerden eve dönmek için bir Dönüş Parşömeni (Return Scroll) taşıyın."],
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
            'key': 'market',
            'x': 3.0,
            'y': -5.0,
            'dependency': 'seasons',
            'title_en': 'The Trading Market',
            'title_tr': 'Ticaret Pazarı',
            'desc_en': ['Farming for Blockheads adds a Market where you can trade emeralds for seeds, saplings, and other farming supplies. Once you understand the seasons, craft a Market and place it to browse all the seeds the modpack has to offer. Plan your crops according to the current season!'],
            'desc_tr': ['Farming for Blockheads, zümrüt karşılığında tohumlar, fidanlar ve diğer çiftlik malzemelerini takas edebileceğiniz bir Pazar ekler. Mevsimleri anladıktan sonra bir Pazar yapıp yerleştirin ve mod paketindeki tüm tohumlara göz atın. Ekinlerinizi mevcut mevsime göre planlayın!'],
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
